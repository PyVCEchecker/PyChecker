# coding: utf8
# Copyright 2019 Lenovo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
The command module for redfish systems.  Provides https-only support
for redfish compliant endpoints
"""

import base64
from datetime import datetime
from datetime import timedelta
from fnmatch import fnmatch
import json
import os
import re
import socket
import struct
import sys
import time

from dateutil import tz

import pyghmi.constants as const
import pyghmi.exceptions as exc
import pyghmi.redfish.oem.lookup as oem
from pyghmi.util.parse import parse_time
import pyghmi.util.webclient as webclient


numregex = re.compile('([0-9]+)')


powerstates = {
    'on': 'On',
    'off': 'ForceOff',
    'softoff': 'GracefulShutdown',
    'shutdown': 'GracefulShutdown',
    'reset': 'ForceRestart',
    'boot': None,
}

boot_devices_write = {
    'net': 'Pxe',
    'network': 'Pxe',
    'pxe': 'Pxe',
    'hd': 'Hdd',
    'cd': 'Cd',
    'cdrom': 'Cd',
    'optical': 'Cd',
    'dvd': 'Cd',
    'floppy': 'Floppy',
    'default': 'None',
    'setup': 'BiosSetup',
    'bios': 'BiosSetup',
    'f1': 'BiosSetup',
}

boot_devices_read = {
    'BiosSetup': 'setup',
    'Cd': 'optical',
    'Floppy': 'floppy',
    'Hdd': 'hd',
    'None': 'default',
    'Pxe': 'network',
    'Usb': 'usb',
    'SDCard': 'sdcard',
}


_healthmap = {
    'Critical': const.Health.Critical,
    'Unknown': const.Health.Warning,
    'Warning': const.Health.Warning,
    'OK': const.Health.Ok,
}


def _mask_to_cidr(mask):
    maskn = socket.inet_pton(socket.AF_INET, mask)
    maskn = struct.unpack('!I', maskn)[0]
    cidr = 32
    while maskn & 0b1 == 0 and cidr > 0:
        cidr -= 1
        maskn >>= 1
    return cidr


def _to_boolean(attrval):
    attrval = attrval.lower()
    if not attrval:
        return False
    if ('true'.startswith(attrval) or 'yes'.startswith(attrval)
            or 'enabled'.startswith(attrval) or attrval == '1'):
        return True
    if ('false'.startswith(attrval) or 'no'.startswith(attrval)
            or 'disabled'.startswith(attrval) or attrval == '0'):
        return False
    raise Exception(
        'Unrecognized candidate for boolean: {0}'.format(attrval))


def _cidr_to_mask(cidr):
    return socket.inet_ntop(
        socket.AF_INET, struct.pack(
            '!I', (2**32 - 1) ^ (2**(32 - cidr) - 1)))


def naturalize_string(key):
    """Analyzes string in a human way to enable natural sort

    :param nodename: The node name to analyze
    :returns: A structure that can be consumed by 'sorted'
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(numregex, key)]


def natural_sort(iterable):
    """Return a sort using natural sort if possible

    :param iterable:
    :return:
    """
    try:
        return sorted(iterable, key=naturalize_string)
    except TypeError:
        # The natural sort attempt failed, fallback to ascii sort
        return sorted(iterable)


class SensorReading(object):
    def __init__(self, healthinfo, sensor=None, value=None, units=None,
                 unavailable=False):
        if sensor:
            self.name = sensor['name']
        else:
            self.name = healthinfo['Name']
            self.health = _healthmap.get(healthinfo.get(
                'Status', {}).get('Health', None), const.Health.Warning)
            self.states = [healthinfo.get('Status', {}).get('Health',
                                                            'Unknown')]
            self.health = _healthmap[healthinfo['Status']['Health']]
            self.states = [healthinfo['Status']['Health']]
        self.value = value
        self.state_ids = None
        self.imprecision = None
        self.units = units
        self.unavailable = unavailable


class AttrDependencyHandler(object):
    def __init__(self, dependencies, currsettings, pendingsettings):
        self.dependencymap = {}
        for dep in dependencies.get('Dependencies', [[]]):
            if dep['Type'] != 'Map':
                continue
            if 'Dependency' not in dep:
                continue
            if dep['DependencyFor'] in self.dependencymap:
                self.dependencymap[
                    dep['DependencyFor']].append(dep['Dependency'])
            else:
                self.dependencymap[
                    dep['DependencyFor']] = [dep['Dependency']]
        self.curr = currsettings
        self.pend = pendingsettings
        self.reg = dependencies['Attributes']

    def get_overrides(self, setting):
        overrides = {}
        blameattrs = []
        if setting not in self.dependencymap:
            return {}, []
        for depinfo in self.dependencymap[setting]:
            lastoper = None
            lastcond = None
            for mapfrom in depinfo.get('MapFrom', []):
                if lastcond is not None and not lastoper:
                    break  # MapTerm required to make sense of this, give up
                currattr = mapfrom['MapFromAttribute']
                blameattrs.append(currattr)
                currprop = mapfrom['MapFromProperty']
                if currprop == 'CurrentValue':
                    if currattr in self.pend:
                        currval = self.pend[currattr]
                    else:
                        currval = self.curr[currattr]
                else:
                    currval = self.reg[currattr][currprop]
                lastcond = self.process(currval, mapfrom, lastcond, lastoper)
                lastoper = mapfrom.get('MapTerms', None)
            if lastcond:
                if setting not in overrides:
                    overrides[setting] = {}
                if depinfo['MapToAttribute'] not in overrides[setting]:
                    overrides[depinfo['MapToAttribute']] = {}
                overrides[depinfo['MapToAttribute']][
                    depinfo['MapToProperty']] = depinfo['MapToValue']
        return overrides, blameattrs

    def process(self, currval, mapfrom, lastcond, lastoper):
        newcond = None
        mfc = mapfrom['MapFromCondition']
        if mfc == 'EQU':
            newcond = currval == mapfrom['MapFromValue']
        if mfc == 'NEQ':
            newcond = currval != mapfrom['MapFromValue']
        if mfc == 'GEQ':
            newcond = float(currval) >= float(mapfrom['MapFromValue'])
        if mfc == 'GTR':
            newcond = float(currval) > float(mapfrom['MapFromValue'])
        if mfc == 'LEQ':
            newcond = float(currval) <= float(mapfrom['MapFromValue'])
        if mfc == 'LSS':
            newcond = float(currval) < float(mapfrom['MapFromValue'])
        if lastcond is not None:
            if lastoper == 'AND':
                return lastcond and newcond
            elif lastoper == 'OR':
                return lastcond or newcond
            return None
        return newcond


class Command(object):

    def __init__(self, bmc, userid, password, verifycallback, sysurl=None,
                 bmcurl=None, chassisurl=None, pool=None, port=443):
        self.wc = webclient.SecureHTTPConnection(
            bmc, port, verifycallback=verifycallback)
        self._hwnamemap = {}
        self._fwnamemap = {}
        self._urlcache = {}
        self._varbmcurl = bmcurl
        self._varbiosurl = None
        self._varbmcnicurl = None
        self._varsetbiosurl = None
        self._varchassisurl = chassisurl
        self._varresetbmcurl = None
        self._varupdateservice = None
        self._varfwinventory = None
        self._oem = None
        self._gpool = pool
        self.wc.set_header('Accept', 'application/json')
        self.wc.set_header('User-Agent', 'pyghmi')
        self.wc.set_header('Accept-Encoding', 'gzip')
        self.wc.set_header('OData-Version', '4.0')
        overview = self.wc.grab_json_response('/redfish/v1/')
        self.wc.set_basic_credentials(userid, password)
        self.username = userid
        self.password = password
        self.wc.set_header('Content-Type', 'application/json')
        if 'Systems' not in overview:
            raise exc.PyghmiException('Redfish not ready')
        systems = overview['Systems']['@odata.id']
        res = self.wc.grab_json_response_with_status(systems)
        if res[1] == 401:
            raise exc.PyghmiException('Access Denied')
        elif res[1] < 200 or res[1] >= 300:
            raise exc.PyghmiException(repr(res[0]))
        members = res[0]
        self._varsensormap = {}
        systems = members['Members']
        if sysurl:
            for system in systems:
                if system['@odata.id'] == sysurl:
                    self.sysurl = sysurl
                    break
            else:
                raise exc.PyghmiException(
                    'Specified sysurl not found: {0}'.format(sysurl))
        else:
            if len(systems) != 1:
                raise exc.PyghmiException(
                    'Multi system manager, sysurl is required parameter')
            self.sysurl = systems[0]['@odata.id']
        self.powerurl = self.sysinfo.get('Actions', {}).get(
            '#ComputerSystem.Reset', {}).get('target', None)

    @property
    def _accountserviceurl(self):
        sroot = self._do_web_request('/redfish/v1/')
        return sroot.get('AccountService', {}).get('@odata.id', None)

    @property
    def _validroles(self):
        okroles = set([])
        roleurl = self._do_web_request(self._accountserviceurl).get(
            'Roles', {}).get('@odata.id', None)
        if roleurl:
            roles = self._do_web_request(roleurl).get('Members', [])
            for role in roles:
                role = role.get('@odata.id', '')
                if not role:
                    continue
                okroles.add(role.split('/')[-1])
        if not okroles:
            okroles.add('Administrator')
            okroles.add('Operator')
            okroles.add('ReadOnly')
        return okroles

    def get_users(self):
        """get list of users and channel access information (helper)

        :param channel: number [1:7]

        :return:
            name: (str)
            uid: (int)
            channel: (int)
            access:
                callback (bool)
                link_auth (bool)
                ipmi_msg (bool)
                privilege_level: (str)[callback, user, operatorm administrator,
                                       proprietary, no_access]
        """
        srvurl = self._accountserviceurl
        names = {}
        if srvurl:
            srvinfo = self._do_web_request(srvurl)
            srvurl = srvinfo.get('Accounts', {}).get('@odata.id', None)
            if srvurl:
                srvinfo = self._do_web_request(srvurl)
                accounts = srvinfo.get('Members', [])
                for account in accounts:
                    accinfo = self._do_web_request(account['@odata.id'])
                    currname = accinfo.get('UserName', '')
                    currid = accinfo.get('Id', None)
                    if currname:
                        names[currid] = {
                            'name': currname,
                            'uid': currid,
                            'expiration': self.oem.get_user_expiration(currid),
                            'access': {
                                'privilege_level': accinfo.get('RoleId',
                                                               'Unknown')
                            }
                        }
        return names

    def _account_url_info_by_id(self, uid):
        srvurl = self._accountserviceurl
        if srvurl:
            srvinfo = self._do_web_request(srvurl)
            srvurl = srvinfo.get('Accounts', {}).get('@odata.id', None)
            if srvurl:
                srvinfo = self._do_web_request(srvurl)
                accounts = srvinfo.get('Members', [])
                for account in accounts:
                    accinfo = self._do_web_request(account['@odata.id'])
                    currid = accinfo.get('Id', None)
                    if str(currid) == str(uid):
                        accinfo['expiration'] = self.oem.get_user_expiration(
                            uid)
                        return account['@odata.id'], accinfo

    def get_user(self, uid):
        srvurl = self._accountserviceurl
        if srvurl:
            srvinfo = self._do_web_request(srvurl)
            srvurl = srvinfo.get('Accounts', {}).get('@odata.id', None)
            if srvurl:
                srvinfo = self._do_web_request(srvurl)
                accounts = srvinfo.get('Members', [])
                for account in accounts:
                    accinfo = self._do_web_request(account['@odata.id'])
                    currname = accinfo.get('UserName', '')
                    currid = accinfo.get('Id', None)
                    if str(currid) == str(uid):
                        return {'name': currname, 'uid': uid,
                                'expiration': self.oem.get_user_expiration(
                                    uid),
                                'access': {
                                    'privilege_level': accinfo.get(
                                        'RoleId', 'Unknown')}}

    def set_user_password(self, uid, mode='set_password', password=None):
        """Set user password and (modes)

        :param uid: id number of user.  see: get_names_uid()['name']

        :param mode:
            disable       = disable user connections
            enable        = enable user connections
            set_password  = set or ensure password

        :param password: Password
            (optional when mode is [disable or enable])

        :return:
            True on success
        """

        accinfo = self._account_url_info_by_id(uid)
        if not accinfo:
            raise Exception("No such account found")
        etag = accinfo[1].get('@odata.etag', None)
        if mode == 'set_password':
            self._do_web_request(accinfo[0], {'Password': password},
                                 method='PATCH', etag=etag)
        elif mode == 'disable':
            self._do_web_request(accinfo[0], {'Enabled': False},
                                 method='PATCH', etag=etag)
        elif mode == 'enable':
            self._do_web_request(accinfo[0], {'Enabled': True},
                                 method='PATCH', etag=etag)
        return True

    def disable_user(self, uid, mode):
        """Disable User

        Just disable the User.
        This will not disable the password or revoke privileges.

        :param uid: user id
        :param mode:
            disable       = disable user connections
            enable        = enable user connections
        """
        self.set_user_password(uid, mode)
        return True

    def set_user_access(self, uid, privilege_level='ReadOnly'):
        accinfo = self._account_url_info_by_id(uid)
        if not accinfo:
            raise Exception("Unable to find indicated uid")
        etag = accinfo[1].get('@odata.etag', None)
        for role in self._validroles:
            if role.lower() == privilege_level.lower():
                privilege_level = role
                break
        self._do_web_request(accinfo[0], {'RoleId': privilege_level},
                             method='PATCH', etag=etag)

    def create_user(self, uid, name, password, privilege_level='ReadOnly'):
        """create/ensure a user is created with provided settings

        :param privilege_level:
            User Privilege level.  Redfish role, commonly Administrator,
            Operator, and ReadOnly
        """
        accinfo = self._account_url_info_by_id(uid)
        if not accinfo:
            raise Exception("Unable to find indicated uid")
        for role in self._validroles:
            if role.lower() == privilege_level.lower():
                privilege_level = role
                break
        etag = accinfo[1].get('@odata.etag', None)
        userinfo = {
            "UserName": name,
            "Password": password,
            "RoleId": privilege_level,
        }
        self._do_web_request(accinfo[0], userinfo, method='PATCH', etag=etag)
        return True

    def user_delete(self, uid):
        # Redfish doesn't do so well with Deleting users either...
        # Blanking the username seems to be the convention
        # First, set a bogus password in case the implementation does honor
        # blank user, at least render such an account harmless
        self.set_user_password(uid, base64.b64encode(os.urandom(15)))
        self.set_user_name(uid, '')
        return True

    def set_user_name(self, uid, name):
        """Set user name

        :param uid: user id
        :param name: username
        """
        accinfo = self._account_url_info_by_id(uid)
        if not accinfo:
            raise Exception("No such account found")
        etag = accinfo[1].get('@odata.etag', None)
        self._do_web_request(accinfo[0], {'UserName': name}, method='PATCH',
                             etag=etag)
        return True

    @property
    def _updateservice(self):
        if not self._varupdateservice:
            overview = self._do_web_request('/redfish/v1/')
            us = overview.get('UpdateService', {}).get('@odata.id', None)
            if not us:
                raise exc.UnsupportedFunctionality(
                    'BMC does not implement extended firmware information')
            self._varupdateservice = us
        return self._varupdateservice

    @property
    def _fwinventory(self):
        if not self._varfwinventory:
            usi = self._do_web_request(self._updateservice)
            self._varfwinventory = usi.get('FirmwareInventory', {}).get(
                '@odata.id', None)
            if not self._varfwinventory:
                raise exc.UnsupportedFunctionality(
                    'BMC does not implement extended firmware information')
        return self._varfwinventory

    @property
    def sysinfo(self):
        return self._do_web_request(self.sysurl)

    @property
    def bmcinfo(self):
        return self._do_web_request(self._bmcurl)

    def get_power(self):
        currinfo = self._do_web_request(self.sysurl, cache=False)
        return {'powerstate': str(currinfo['PowerState'].lower())}

    def set_power(self, powerstate, wait=False):
        if powerstate == 'boot':
            oldpowerstate = self.get_power()['powerstate']
            powerstate = 'on' if oldpowerstate == 'off' else 'reset'
        elif powerstate in ('on', 'off'):
            oldpowerstate = self.get_power()['powerstate']
            if oldpowerstate == powerstate:
                return {'powerstate': powerstate}
        reqpowerstate = powerstate
        if powerstate not in powerstates:
            raise exc.InvalidParameterValue(
                "Unknown power state %s requested" % powerstate)
        powerstate = powerstates[powerstate]
        result = self.wc.grab_json_response_with_status(
            self.powerurl, {'ResetType': powerstate})
        if result[1] < 200 or result[1] >= 300:
            raise exc.PyghmiException(result[0])
        if wait and reqpowerstate in ('on', 'off', 'softoff', 'shutdown'):
            if reqpowerstate in ('softoff', 'shutdown'):
                reqpowerstate = 'off'
            timeout = os.times()[4] + 300
            while (self.get_power()['powerstate'] != reqpowerstate
                   and os.times()[4] < timeout):
                time.sleep(1)
            if self.get_power()['powerstate'] != reqpowerstate:
                raise exc.PyghmiException(
                    "System did not accomplish power state change")
            return {'powerstate': reqpowerstate}
        return {'pendingpowerstate': reqpowerstate}

    def _get_cache(self, url, cache=30):
        now = os.times()[4]
        cachent = self._urlcache.get(url, None)
        if cachent and cachent['vintage'] > now - cache:
            return cachent['contents']
        return None

    def _do_bulk_requests(self, urls, cache=True):
        if self._gpool:
            urls = [(x, None, None, cache) for x in urls]
            for res in self._gpool.starmap(self._do_web_request_withurl, urls):
                yield res
        else:
            for url in urls:
                yield self._do_web_request_withurl(url, cache=cache)

    def _do_web_request_withurl(self, url, payload=None, method=None,
                                cache=True):
        return self._do_web_request(url, payload, method, cache), url

    def _do_web_request(self, url, payload=None, method=None, cache=True,
                        etag=None):
        res = None
        if cache and payload is None and method is None:
            res = self._get_cache(url, cache)
        if res:
            return res
        wc = self.wc.dupe()
        if etag:
            wc.stdheaders['If-Match'] = etag
        try:
            res = wc.grab_json_response_with_status(url, payload,
                                                    method=method)
        finally:
            if 'If-Match' in wc.stdheaders:
                del wc.stdheaders['If-Match']
        if res[1] < 200 or res[1] >= 300:
            try:
                info = json.loads(res[0])
                errmsg = [
                    x.get('Message', x['MessageId']) for x in info.get(
                        'error', {}).get('@Message.ExtendedInfo', {})]
                msgid = [
                    x['MessageId'] for x in info.get(
                        'error', {}).get('@Message.ExtendedInfo', {})]
                errmsg = ','.join(errmsg)
                msgid = ','.join(msgid)
                raise exc.RedfishError(errmsg, msgid=msgid)
            except (ValueError, KeyError):
                raise exc.PyghmiException(str(url) + ":" + res[0])
        if payload is None and method is None:
            self._urlcache[url] = {'contents': res[0],
                                   'vintage': os.times()[4]}
        return res[0]

    def get_bootdev(self):
        """Get current boot device override information.

        :raises: PyghmiException on error
        :returns: dict
        """
        result = self._do_web_request(self.sysurl)
        overridestate = result.get('Boot', {}).get(
            'BootSourceOverrideEnabled', None)
        if overridestate == 'Disabled':
            return {'bootdev': 'default', 'persistent': True}
        persistent = None
        if overridestate == 'Once':
            persistent = False
        elif overridestate == 'Continuous':
            persistent = True
        else:
            raise exc.PyghmiException('Unrecognized Boot state: %s'
                                      % repr(overridestate))
        uefimode = result.get('Boot', {}).get('BootSourceOverrideMode', None)
        if uefimode == 'UEFI':
            uefimode = True
        elif uefimode == 'Legacy':
            uefimode = False
        else:
            raise exc.PyghmiException('Unrecognized mode: %s' % uefimode)
        bootdev = result.get('Boot', {}).get('BootSourceOverrideTarget', None)
        if bootdev not in boot_devices_read:
            raise exc.PyghmiException('Unrecognized boot target: %s'
                                      % repr(bootdev))
        bootdev = boot_devices_read[bootdev]
        return {'bootdev': bootdev, 'persistent': persistent,
                'uefimode': uefimode}

    def set_bootdev(self, bootdev, persist=False, uefiboot=None):
        """Set boot device to use on next reboot

        :param bootdev:
                        *network -- Request network boot
                        *hd -- Boot from hard drive
                        *safe -- Boot from hard drive, requesting 'safe mode'
                        *optical -- boot from CD/DVD/BD drive
                        *setup -- Boot into setup utility
                        *default -- remove any directed boot device request
        :param persist: If true, ask that system firmware use this device
                        beyond next boot.  Be aware many systems do not honor
                        this
        :param uefiboot: If true, request UEFI boot explicitly.  If False,
                         request BIOS style boot.
                         None (default) does not modify the boot mode.
        :raises: PyghmiException on an error.
        :returns: dict or True -- If callback is not provided, the response
        """
        reqbootdev = bootdev
        if (bootdev not in boot_devices_write
                and bootdev not in boot_devices_read):
            raise exc.InvalidParameterValue('Unsupported device %s'
                                            % repr(bootdev))
        bootdev = boot_devices_write.get(bootdev, bootdev)
        if bootdev == 'None':
            payload = {'Boot': {'BootSourceOverrideEnabled': 'Disabled'}}
        else:
            payload = {'Boot': {
                'BootSourceOverrideEnabled': 'Continuous' if persist
                                             else 'Once',
                'BootSourceOverrideTarget': bootdev,
            }}
            if uefiboot is not None:
                uefiboot = 'UEFI' if uefiboot else 'Legacy'
                payload['BootSourceOverrideMode'] = uefiboot
                try:
                    self._do_web_request(self.sysurl, payload, method='PATCH')
                    return {'bootdev': reqbootdev}
                except Exception:
                    del payload['BootSourceOverrideMode']
        thetag = self.sysinfo.get('@odata.etag', None)
        self._do_web_request(self.sysurl, payload, method='PATCH', etag=thetag)
        return {'bootdev': reqbootdev}

    @property
    def _biosurl(self):
        if not self._varbiosurl:
            self._varbiosurl = self.sysinfo.get('Bios', {}).get('@odata.id',
                                                                None)
        if self._varbiosurl is None:
            raise exc.UnsupportedFunctionality(
                'Bios management not detected on this platform')
        return self._varbiosurl

    @property
    def _setbiosurl(self):
        if self._varsetbiosurl is None:
            biosinfo = self._do_web_request(self._biosurl)
            self._varsetbiosurl = biosinfo.get(
                '@Redfish.Settings', {}).get('SettingsObject', {}).get(
                    '@odata.id', None)
        if self._varsetbiosurl is None:
            raise exc.UnsupportedFunctionality('Ability to set BIOS settings '
                                               'not detected on this platform')
        return self._varsetbiosurl

    @property
    def _sensormap(self):
        if not self._varsensormap:
            for chassis in self.sysinfo.get('Links', {}).get('Chassis', []):
                self._mapchassissensors(chassis)
        return self._varsensormap

    def _mapchassissensors(self, chassis):
        chassisurl = chassis['@odata.id']
        chassisinfo = self._do_web_request(chassisurl)
        powurl = chassisinfo.get('Power', {}).get('@odata.id', '')
        if powurl:
            powinf = self._do_web_request(powurl)
            for voltage in powinf.get('Voltages', []):
                if 'Name' in voltage:
                    self._varsensormap[voltage['Name']] = {
                        'name': voltage['Name'], 'url': powurl,
                        'type': 'Voltage'}
        thermurl = chassisinfo.get('Thermal', {}).get('@odata.id', '')
        if thermurl:
            therminf = self._do_web_request(thermurl)
            for fan in therminf.get('Fans', []):
                if 'Name' in fan:
                    self._varsensormap[fan['Name']] = {
                        'name': fan['Name'], 'type': 'Fan',
                        'url': thermurl}
            for temp in therminf.get('Temperatures', []):
                if 'Name' in temp:
                    self._varsensormap[temp['Name']] = {
                        'name': temp['Name'], 'type': 'Temperature',
                        'url': thermurl}
        for subchassis in chassisinfo.get('Links', {}).get('Contains', []):
            self._mapchassissensors(subchassis)

    @property
    def _bmcurl(self):
        if not self._varbmcurl:
            self._varbmcurl = self.sysinfo.get('Links', {}).get(
                'ManagedBy', [{}])[0].get('@odata.id', None)
        return self._varbmcurl

    @property
    def _bmcnicurl(self):
        if not self._varbmcnicurl:
            self._varbmcnicurl = self._get_bmc_nic_url()
        return self._varbmcnicurl

    def list_network_interface_names(self):
        bmcinfo = self._do_web_request(self._bmcurl)
        nicurl = bmcinfo.get('EthernetInterfaces', {}).get('@odata.id', None)
        if not nicurl:
            return
        niclist = self._do_web_request(nicurl)
        for nic in niclist.get('Members', []):
            curl = nic.get('@odata.id', None)
            if not curl:
                continue
            yield curl.rsplit('/', 1)[1]

    def _get_bmc_nic_url(self, name=None):
        bmcinfo = self._do_web_request(self._bmcurl)
        nicurl = bmcinfo.get('EthernetInterfaces', {}).get('@odata.id', None)
        niclist = self._do_web_request(nicurl)
        foundnics = 0
        lastnicurl = None
        for nic in niclist.get('Members', []):
            curl = nic.get('@odata.id', None)
            if not curl:
                continue
            if name is not None:
                if curl.endswith('/{0}'.format(name)):
                    return curl
                continue
            if self.oem.hostnic and curl.endswith('/{0}'.format(
                    self.oem.hostnic)):
                continue
            nicinfo = self._do_web_request(curl)
            if nicinfo.get('Links', {}).get('HostInterface', None):
                # skip host interface
                continue
            if not nicinfo.get('InterfaceEnabled', True):
                # skip disabled interfaces
                continue
            foundnics += 1
            lastnicurl = curl
        if name is None and foundnics != 1:
            raise exc.PyghmiException(
                'BMC does not have exactly one interface')
        if name is None:
            return lastnicurl

    @property
    def _bmcresetinfo(self):
        if not self._varresetbmcurl:
            bmcinfo = self._do_web_request(self._bmcurl)
            resetinf = bmcinfo.get('Actions', {}).get('#Manager.Reset', {})
            url = resetinf.get('target', '')
            valid = resetinf.get('ResetType@Redfish.AllowableValues', [])
            if not valid:
                tmpurl = resetinf.get('@Redfish.ActionInfo', None)
                if tmpurl:
                    resetinf = self._do_web_request(tmpurl)
                    valid = resetinf.get('Parameters', [{}])[0].get(
                        'AllowableValues')
            resettype = None
            if 'GracefulRestart' in valid:
                resettype = 'GracefulRestart'
            elif 'ForceRestart' in valid:
                resettype = 'ForceRestart'
            elif 'ColdReset' in valid:
                resettype = 'ColdReset'
            self._varresetbmcurl = url, resettype
        return self._varresetbmcurl

    def reset_bmc(self):
        url, action = self._bmcresetinfo
        if not url:
            raise Exception('BMC does not provide reset action')
        if not action:
            raise Exception('BMC does not accept a recognized reset type')
        self._do_web_request(url, {'ResetType': action})

    def set_identify(self, on=True, blink=None):
        self._do_web_request(
            self.sysurl,
            {'IndicatorLED': 'Blinking' if blink else 'Lit' if on else 'Off'},
            method='PATCH', etag='*')

    _idstatemap = {
        'Blinking': 'blink',
        'Lit': 'on',
        'Off': 'off',
    }

    def get_identify(self):
        ledstate = self.sysinfo['IndicatorLED']
        return {'identifystate': self._idstatemap[ledstate]}

    def get_health(self, verbose=True):
        health = self.sysinfo.get('Status', {})
        health = health.get('HealthRollup', health.get('Health', 'Unknown'))
        warnunknown = health == 'Unknown'
        health = _healthmap[health]
        summary = {'badreadings': [], 'health': health}
        if health > 0 and verbose:
            # now have to manually peruse all psus, fans, processors, ram,
            # storage
            procsumstatus = self.sysinfo.get('ProcessorSummary', {}).get(
                'Status', {})
            procsumstatus = procsumstatus.get('HealthRollup',
                                              procsumstatus.get('Health',
                                                                None))
            if procsumstatus != 'OK':
                procfound = False
                procurl = self.sysinfo.get('Processors', {}).get('@odata.id',
                                                                 None)
                if procurl:
                    for cpu in self._do_web_request(procurl).get(
                            'Members', []):
                        cinfo = self._do_web_request(cpu['@odata.id'])
                        if cinfo.get('Status', {}).get(
                                'State', None) == 'Absent':
                            continue
                        if cinfo.get('Status', {}).get(
                                'Health', None) not in ('OK', None):
                            procfound = True
                            summary['badreadings'].append(SensorReading(cinfo))
                if not procfound:
                    procinfo = self.sysinfo['ProcessorSummary']
                    procinfo['Name'] = 'Processors'
                    summary['badreadings'].append(SensorReading(procinfo))
            memsumstatus = self.sysinfo.get(
                'MemorySummary', {}).get('Status', {})
            memsumstatus = memsumstatus.get('HealthRollup',
                                            memsumstatus.get('Health', None))
            if memsumstatus != 'OK':
                dimmfound = False
                for mem in self._do_web_request(
                        self.sysinfo['Memory']['@odata.id'])['Members']:
                    dimminfo = self._do_web_request(mem['@odata.id'])
                    if dimminfo.get('Status', {}).get(
                            'State', None) == 'Absent':
                        continue
                    if dimminfo.get('Status', {}).get(
                            'Health', None) not in ('OK', None):
                        summary['badreadings'].append(SensorReading(dimminfo))
                        dimmfound = True
                if not dimmfound:
                    meminfo = self.sysinfo['MemorySummary']
                    meminfo['Name'] = 'Memory'
                    summary['badreadings'].append(SensorReading(meminfo))
            for adapter in self.sysinfo['PCIeDevices']:
                adpinfo = self._do_web_request(adapter['@odata.id'])
                if adpinfo['Status']['Health'] not in ('OK', None):
                    summary['badreadings'].append(SensorReading(adpinfo))
            for fun in self.sysinfo['PCIeFunctions']:
                funinfo = self._do_web_request(fun['@odata.id'])
                if funinfo['Status']['Health'] not in ('OK', None):
                    summary['badreadings'].append(SensorReading(funinfo))
        if warnunknown and not summary['badreadings']:
            unkinf = SensorReading({'Name': 'BMC',
                                    'Status': {'Health': 'Unknown'}})
            unkinf.states = ['System does not provide health information']
            summary['badreadings'].append(unkinf)
        return summary

    def _get_biosreg(self, url):
        addon = {}
        valtodisplay = {}
        displaytoval = {}
        reg = self._do_web_request(url)
        reg = reg['RegistryEntries']
        for attr in reg['Attributes']:
            vals = attr.get('Value', [])
            if vals:
                valtodisplay[attr['AttributeName']] = {}
                displaytoval[attr['AttributeName']] = {}
                for val in vals:
                    valtodisplay[
                        attr['AttributeName']][val['ValueName']] = val[
                            'ValueDisplayName']
                    displaytoval[
                        attr['AttributeName']][val['ValueDisplayName']] = val[
                            'ValueName']
            defaultval = attr.get('DefaultValue', None)
            defaultval = valtodisplay.get(attr['AttributeName'], {}).get(
                defaultval, defaultval)
            if attr['Type'] == 'Integer' and defaultval:
                defaultval = int(defaultval)
            if attr['Type'] == 'Boolean':
                vals = [{'ValueDisplayName': 'True'},
                        {'ValueDisplayName': 'False'}]
            addon[attr['AttributeName']] = {
                'default': defaultval,
                'help': attr.get('HelpText', None),
                'sortid': attr.get('DisplayOrder', None),
                'possible': [x['ValueDisplayName'] for x in vals],
            }
        return addon, valtodisplay, displaytoval, reg

    def get_bmc_configuration(self):
        """Get miscellaneous BMC configuration

        In much the same way a bmc can present arbitrary key-value
        structure for BIOS/UEFI configuration, provide a mechanism
        for a BMC to provide arbitrary key-value for BMC specific
        settings.
        """

        # For now, this is a stub, no implementation for redfish currently
        return {}

    def set_bmc_configuration(self, changeset):
        """Get miscellaneous BMC configuration

        In much the same way a bmc can present arbitrary key-value
        structure for BIOS/UEFI configuration, provide a mechanism
        for a BMC to provide arbitrary key-value for BMC specific
        settings.
        """

        # For now, this is a stub, no implementation for redfish currently
        raise exc.UnsupportedFunctionality(
            'Set BMC configuration not supported in redfish yet')

    def clear_bmc_configuration(self):
        """Reset BMC to factory default

        Call appropriate function to clear BMC to factory default settings.
        In many cases, this may render remote network access impracticle or
        impossible."
        """
        raise exc.UnsupportedFunctionality(
            'Clear BMC configuration not supported in redfish yet')

    def get_system_configuration(self, hideadvanced=True):
        return self._getsyscfg()[0]

    def _getsyscfg(self):
        biosinfo = self._do_web_request(self._biosurl, cache=False)
        reginfo = ({}, {}, {}, {})
        extrainfo = {}
        valtodisplay = {}
        self.attrdeps = {'Dependencies': [], 'Attributes': []}
        if 'AttributeRegistry' in biosinfo:
            overview = self._do_web_request('/redfish/v1/')
            reglist = overview['Registries']['@odata.id']
            reglist = self._do_web_request(reglist)
            regurl = None
            for cand in reglist.get('Members', []):
                cand = cand.get('@odata.id', '')
                candname = cand.split('/')[-1]
                if candname == '':  # implementation uses trailing slash
                    candname = cand.split('/')[-2]
                if candname == biosinfo['AttributeRegistry']:
                    regurl = cand
                    break
            if not regurl:
                # Workaround a vendor bug where they link to a
                # non-existant name
                for cand in reglist.get('Members', []):
                    cand = cand.get('@odata.id', '')
                    candname = cand.split('/')[-1]
                    candname = candname.split('.')[0]
                    if candname == biosinfo[
                            'AttributeRegistry'].split('.')[0]:
                        regurl = cand
                        break
            if regurl:
                reginfo = self._do_web_request(regurl)
                for reg in reginfo.get('Location', []):
                    if reg.get('Language', 'en').startswith('en'):
                        reguri = reg['Uri']
                        reginfo = self._get_biosreg(reguri)
                        extrainfo, valtodisplay, _, self.attrdeps = reginfo
        currsettings = {}
        try:
            pendingsettings = self._do_web_request(self._setbiosurl)
        except exc.UnsupportedFunctionality:
            pendingsettings = {}
        pendingsettings = pendingsettings.get('Attributes', {})
        for setting in biosinfo.get('Attributes', {}):
            val = biosinfo['Attributes'][setting]
            currval = val
            if setting in pendingsettings:
                val = pendingsettings[setting]
            val = valtodisplay.get(setting, {}).get(val, val)
            currval = valtodisplay.get(setting, {}).get(currval, currval)
            val = {'value': val}
            if currval != val['value']:
                val['active'] = currval
            val.update(**extrainfo.get(setting, {}))
            currsettings[setting] = val
        return currsettings, reginfo

    def clear_system_configuration(self):
        """Clear the BIOS/UEFI configuration

        """
        biosinfo = self._do_web_request(self._biosurl)
        rb = biosinfo.get('Actions', {}).get('#Bios.ResetBios', {})
        actinf = rb.get('@Redfish.ActionInfo', None)
        rb = rb.get('target', '')
        parms = {}
        if actinf:
            actinf = self._do_web_request(
                '/redfish/v1/Systems/Self/Bios/ResetBiosActionInfo')
            for parm in actinf.get('Parameters', ()):
                if parm.get('Required', False):
                    if parm.get('Name', None) == 'ResetType' and parm.get(
                            'AllowableValues', [None])[0] == 'Reset':
                        parms['ResetType'] = 'Reset'
                    else:
                        raise Exception(
                            'Unrecognized required parameter {0}'.format(
                                parm.get('Name', 'Unknown')))
        if not rb:
            raise Exception('BIOS reset not detected on this system')
        if not parms:
            parms = {'Action': 'Bios.ResetBios'}
        self._do_web_request(rb, parms)

    def set_system_configuration(self, changeset):
        while True:
            try:
                self._set_system_configuration(changeset)
                return
            except exc.RedfishError as re:
                if 'etag' not in re.msgid.lower():
                    raise

    def _set_system_configuration(self, changeset):
        currsettings, reginfo = self._getsyscfg()
        rawsettings = self._do_web_request(self._biosurl, cache=False)
        rawsettings = rawsettings.get('Attributes', {})
        pendingsettings = self._do_web_request(self._setbiosurl)
        etag = pendingsettings.get('@odata.etag', None)
        pendingsettings = pendingsettings.get('Attributes', {})
        dephandler = AttrDependencyHandler(self.attrdeps, rawsettings,
                                           pendingsettings)
        for change in list(changeset):
            if change not in currsettings:
                found = False
                for attr in currsettings:
                    if fnmatch(attr.lower(), change.lower()):
                        found = True
                        changeset[attr] = changeset[change]
                if found:
                    del changeset[change]
        for change in changeset:
            changeval = changeset[change]
            overrides, blameattrs = dephandler.get_overrides(change)
            meta = {}
            for attr in self.attrdeps['Attributes']:
                if attr['AttributeName'] == change:
                    meta = dict(attr)
                    break
            meta.update(**overrides.get(change, {}))
            if meta.get('ReadOnly', False) or meta.get('GrayOut', False):
                errstr = '{0} is read only'.format(change)
                if blameattrs:
                    errstr += (' due to one of the following settings: '
                               '{0}'.format(','.join(sorted(blameattrs)))
                               )
                raise exc.InvalidParameterValue(errstr)
            if (currsettings.get(change, {}).get('possible', [])
                    and changeval not in currsettings[change]['possible']):
                normval = changeval.lower()
                normval = re.sub(r'\s+', ' ', normval)
                if not normval.endswith('*'):
                    normval += '*'
                for cand in currsettings[change]['possible']:
                    if fnmatch(cand.lower(), normval):
                        changeset[change] = cand
                        break
                else:
                    raise exc.InvalidParameterValue(
                        '{0} is not a valid value for {1} ({2})'.format(
                            changeval, change, ','.join(
                                currsettings[change]['possible'])))
            if changeset[change] in reginfo[2].get(change, {}):
                changeset[change] = reginfo[2][change][changeset[change]]
            for regentry in reginfo[3].get('Attributes', []):
                if change in (regentry.get('AttributeName', ''),
                              regentry.get('DisplayName', '')):
                    if regentry.get('Type', None) == 'Integer':
                        changeset[change] = int(changeset[change])
                    if regentry.get('Type', None) == 'Boolean':
                        changeset[change] = _to_boolean(changeset[change])
        redfishsettings = {'Attributes': changeset}
        self._do_web_request(self._setbiosurl, redfishsettings, 'PATCH',
                             etag=etag)

    def set_net_configuration(self, ipv4_address=None, ipv4_configuration=None,
                              ipv4_gateway=None, name=None):
        patch = {}
        ipinfo = {}
        dodhcp = None
        netmask = None
        if ipv4_address:
            if '/' in ipv4_address:
                ipv4_address, cidr = ipv4_address.split('/')
                netmask = _cidr_to_mask(int(cidr))
            patch['IPv4StaticAddresses'] = [ipinfo]
            ipinfo['Address'] = ipv4_address
            if netmask:
                ipinfo['SubnetMask'] = netmask
        if ipv4_gateway:
            patch['IPv4StaticAddresses'] = [ipinfo]
            ipinfo['Gateway'] = ipv4_gateway
        if ipv4_configuration.lower() == 'dhcp':
            dodhcp = True
            patch['DHCPv4'] = {'DHCPEnabled': True}
        elif (ipv4_configuration == 'static'
              or 'IPv4StaticAddresses' in patch):
            dodhcp = False
            patch['DHCPv4'] = {'DHCPEnabled': False}
        if patch:
            nicurl = self._get_bmc_nic_url(name)
            try:
                self._do_web_request(nicurl, patch, 'PATCH')
            except exc.RedfishError:
                patch = {'IPv4Addresses': [ipinfo]}
                if dodhcp:
                    ipinfo['AddressOrigin'] = 'DHCP'
                elif dodhcp is not None:
                    ipinfo['AddressOrigin'] = 'Static'
                self._do_web_request(nicurl, patch, 'PATCH')

    def get_net_configuration(self, name=None):
        nicurl = self._get_bmc_nic_url(name)
        netcfg = self._do_web_request(nicurl, cache=False)
        ipv4 = netcfg.get('IPv4Addresses', {})
        if not ipv4:
            raise exc.PyghmiException('Unable to locate network information')
        retval = {}
        if len(netcfg['IPv4Addresses']) != 1:
            netcfg['IPv4Addresses'] = [
                x for x in netcfg['IPv4Addresses']
                if x['Address'] != '0.0.0.0']
        if len(netcfg['IPv4Addresses']) != 1:
            raise exc.PyghmiException('Multiple IP addresses not supported')
        currip = netcfg['IPv4Addresses'][0]
        cidr = _mask_to_cidr(currip['SubnetMask'])
        retval['ipv4_address'] = '{0}/{1}'.format(currip['Address'], cidr)
        retval['mac_address'] = netcfg['MACAddress']
        hasgateway = _mask_to_cidr(currip['Gateway'])
        retval['ipv4_gateway'] = currip['Gateway'] if hasgateway else None
        retval['ipv4_configuration'] = currip['AddressOrigin']
        return retval

    def get_hostname(self):
        netcfg = self._do_web_request(self._bmcnicurl)
        return netcfg['HostName']

    def set_hostname(self, hostname):
        self._do_web_request(self._bmcnicurl,
                             {'HostName': hostname}, 'PATCH')

    def get_firmware(self, components=()):
        try:
            for firminfo in self.oem.get_firmware_inventory(components):
                yield firminfo
        except exc.BypassGenericBehavior:
            return
        fwlist = self._do_web_request(self._fwinventory)
        fwurls = [x['@odata.id'] for x in fwlist.get('Members', [])]
        self._fwnamemap = {}
        for res in self._do_bulk_requests(fwurls):
            res = self._extract_fwinfo(res)
            if res[0] is None:
                continue
            yield res

    def _extract_fwinfo(self, inf):
        currinf = {}
        fwi, url = inf
        fwname = fwi.get('Name', 'Unknown')
        if fwname in self._fwnamemap:
            fwname = fwi.get('Id', fwname)
        if fwname in self._fwnamemap:
            # Block duplicates for by name retrieval
            self._fwnamemap[fwname] = None
        else:
            self._fwnamemap[fwname] = url
        currinf['name'] = fwname
        currinf['id'] = fwi.get('Id', None)
        currinf['version'] = fwi.get('Version', 'Unknown')
        currinf['date'] = parse_time(fwi.get('ReleaseDate', ''))
        if not (currinf['version'] or currinf['date']):
            return None, None
        # TODO(Jarrod Johnson): OEM extended data with buildid
        currstate = fwi.get('Status', {}).get('State', 'Unknown')
        if currstate == 'StandbyOffline':
            currinf['state'] = 'pending'
        elif currstate == 'Enabled':
            currinf['state'] = 'active'
        elif currstate == 'StandbySpare':
            currinf['state'] = 'backup'
        return fwname, currinf

    def get_inventory_descriptions(self, withids=False):
        yield "System"
        self._hwnamemap = {}
        for cpu in self._get_cpu_inventory(True, withids):
            yield cpu
        for mem in self._get_mem_inventory(True, withids):
            yield mem
        for adp in self._get_adp_inventory(True, withids):
            yield adp

    def get_inventory_of_component(self, component):
        if component.lower() == 'system':
            sysinfo = {
                'UUID': self.sysinfo.get('UUID', ''),
                'Serial Number': self.sysinfo.get('SerialNumber', ''),
                'Manufacturer': self.sysinfo.get('Manufacturer', ''),
                'Product Name': self.sysinfo.get('Model', ''),
                'Model': self.sysinfo.get(
                    'SKU', self.sysinfo.get('PartNumber', '')),
            }
            return sysinfo
        else:
            for invpair in self.get_inventory():
                if invpair[0].lower() == component.lower():
                    return invpair[1]

    def get_inventory(self, withids=False):
        sysinfo = {
            'UUID': self.sysinfo.get('UUID', ''),
            'Serial Number': self.sysinfo.get('SerialNumber', ''),
            'Manufacturer': self.sysinfo.get('Manufacturer', ''),
            'Product Name': self.sysinfo.get('Model', ''),
            'Model': self.sysinfo.get(
                'SKU', self.sysinfo.get('PartNumber', '')),
        }
        yield ('System', sysinfo)
        self._hwnamemap = {}
        memurl = self.sysinfo.get('Memory', {}).get('@odata.id', None)
        cpurl = self.sysinfo.get('Processors', {}).get('@odata.id', None)
        list(self._do_bulk_requests([memurl, cpurl]))
        adpurls = self._get_adp_urls()
        cpurls = self._get_cpu_urls()
        memurls = self._get_mem_urls()
        diskurls = self._get_disk_urls()
        allurls = adpurls + cpurls + memurls + diskurls
        list(self._do_bulk_requests(allurls))
        for cpu in self._get_cpu_inventory(withids=withids, urls=cpurls):
            yield cpu
        for mem in self._get_mem_inventory(withids=withids, urls=memurls):
            yield mem
        for adp in self._get_adp_inventory(withids=withids, urls=adpurls):
            yield adp
        for disk in self._get_disk_inventory(withids=withids, urls=diskurls):
            yield disk

    def _get_disk_inventory(self, onlyname=False, withids=False, urls=None):
        if not urls:
            urls = self._get_disk_urls()
        for inf in self._do_bulk_requests(urls):
            inf, _ = inf
            ddata = {
                'Model': inf.get('Model', None),
                'Serial Number': inf.get('SerialNumber', None),
                'Description': inf.get('Name'),
            }
            loc = inf.get('PhysicalLocation', {}).get('Info', None)
            if loc:
                dname = 'Disk {0}'.format(loc)
            else:
                dname = inf.get('Id', 'Disk')
            yield (dname, ddata)

    def _get_adp_inventory(self, onlyname=False, withids=False, urls=None):
        if not urls:
            urls = self._get_adp_urls()
            if not urls:
                # No PCIe device inventory, but *maybe* ethernet inventory...
                aidx = 1
                for nicinfo in self._get_eth_urls():
                    nicinfo = self._do_web_request(nicinfo)
                    nicname = nicinfo.get('Name', None)
                    nicinfo = nicinfo.get('MACAddress', None)
                    if not nicname:
                        nicname = 'NIC'
                    if nicinfo:
                        yield (nicname,
                               {'MAC Address {0}'.format(aidx): nicinfo})
                        aidx += 1
                return
        for inf in self._do_bulk_requests(urls):
            adpinfo, url = inf
            aname = adpinfo.get('Name', 'Unknown')
            if aname in self._hwnamemap:
                aname = adpinfo.get('Id', aname)
            if aname in self._hwnamemap:
                self._hwnamemap[aname] = None
            else:
                self._hwnamemap[aname] = (url, self._get_adp_inventory)
            if onlyname:
                if withids:
                    yield aname, adpinfo.get('Id', aname)
                else:
                    yield aname
                continue
            functions = adpinfo.get('Links', {}).get('PCIeFunctions', [])
            nicidx = 1
            if withids:
                yieldinf = {'Id': adpinfo.get('Id', aname)}
            else:
                yieldinf = {}
            funurls = [x['@odata.id'] for x in functions]
            for fun in self._do_bulk_requests(funurls):
                funinfo, url = fun
                yieldinf['PCI Device ID'] = funinfo['DeviceId'].replace('0x',
                                                                        '')
                yieldinf['PCI Vendor ID'] = funinfo['VendorId'].replace('0x',
                                                                        '')
                yieldinf['PCI Subsystem Device ID'] = funinfo[
                    'SubsystemId'].replace('0x', '')
                yieldinf['PCI Subsystem Vendor ID'] = funinfo[
                    'SubsystemVendorId'].replace('0x', '')
                yieldinf['Type'] = funinfo['DeviceClass']
                for nicinfo in funinfo.get('Links', {}).get(
                        'EthernetInterfaces', []):
                    nicinfo = self._do_web_request(nicinfo['@odata.id'])
                    macaddr = nicinfo.get('MACAddress', None)
                    if macaddr:
                        yieldinf['MAC Address {0}'.format(nicidx)] = macaddr
                        nicidx += 1
            yield aname, yieldinf

    def _get_eth_urls(self):
        ethurls = self.sysinfo.get('EthernetInterfaces', {})
        ethurls = ethurls.get('@odata.id', None)
        if ethurls:
            ethurls = self._do_web_request(ethurls)
            ethurls = ethurls.get('Members', [])
            urls = [x['@odata.id'] for x in ethurls]
        else:
            urls = []
        return urls

    def _get_adp_urls(self):
        adpurls = self.sysinfo.get('PCIeDevices', [])
        if adpurls:
            urls = [x['@odata.id'] for x in adpurls]
        else:
            urls = []
        return urls

    @property
    def oem(self):
        if not self._oem:
            self._oem = oem.get_oem_handler(
                self.sysinfo, self.sysurl, self.wc, self._urlcache, self)
            self._oem.set_credentials(self.username, self.password)
        return self._oem

    def get_description(self):
        return self.oem.get_description()

    def _get_cpu_inventory(self, onlynames=False, withids=False, urls=None):
        if not urls:
            urls = self._get_cpu_urls()
        if not urls:
            return
        for res in self._do_bulk_requests(urls):
            currcpuinfo, url = res
            name = currcpuinfo.get('Name', 'CPU')
            if name in self._hwnamemap:
                self._hwnamemap[name] = None
            else:
                self._hwnamemap[name] = (url, self._get_cpu_inventory)
            if onlynames:
                yield name
                continue
            cpuinfo = {'Model': currcpuinfo.get('Model', None)}
            yield name, cpuinfo

    def _get_disk_urls(self):
        storurl = self.sysinfo.get('Storage', {}).get('@odata.id', None)
        urls = []
        if storurl:
            storurl = self._do_web_request(storurl)
            for url in storurl.get('Members', []):
                url = url['@odata.id']
                ctldata = self._do_web_request(url)
                for durl in ctldata.get('Drives', []):
                    urls.append(durl['@odata.id'])
        return urls

    def _get_cpu_urls(self):
        cpurl = self.sysinfo.get('Processors', {}).get('@odata.id', None)
        if cpurl is None:
            urls = []
        else:
            cpurl = self._do_web_request(cpurl)
            urls = [x['@odata.id'] for x in cpurl.get('Members', [])]
        return urls

    def _get_mem_inventory(self, onlyname=False, withids=False, urls=None):
        if not urls:
            urls = self._get_mem_urls()
        if not urls:
            return
        for mem in self._do_bulk_requests(urls):
            currmeminfo, url = mem
            name = currmeminfo.get('Name', 'Memory')
            if name in self._hwnamemap:
                self._hwnamemap[name] = None
            else:
                self._hwnamemap[name] = (url, self._get_mem_inventory)
            if onlyname:
                yield name
                continue
            if currmeminfo.get(
                    'Status', {}).get('State', 'Absent') == 'Absent':
                yield (name, None)
                continue
            currspeed = currmeminfo.get('OperatingSpeedMhz', None)
            if currspeed:
                currspeed = int(currspeed)
                currspeed = currspeed * 8 - (currspeed * 8 % 100)
            meminfo = {
                'capacity_mb': currmeminfo.get('CapacityMiB', None),
                'manufacturer': currmeminfo.get('Manufacturer', None),
                'memory_type': currmeminfo.get('MemoryDeviceType', None),
                'model': currmeminfo.get('PartNumber', None),
                'module_type': currmeminfo.get('BaseModuleType', None),
                'serial': currmeminfo.get('SerialNumber', None),
                'speed': currspeed,
            }
            yield (name, meminfo)

    def _get_mem_urls(self):
        memurl = self.sysinfo.get('Memory', {}).get('@odata.id', None)
        if not memurl:
            urls = []
        else:
            memurl = self._do_web_request(memurl)
            urls = [x['@odata.id'] for x in memurl.get('Members', [])]
        return urls

    def get_event_log(self, clear=False):
        bmcinfo = self._do_web_request(self._bmcurl)
        lsurl = bmcinfo.get('LogServices', {}).get('@odata.id', None)
        if not lsurl:
            return
        currtime = bmcinfo.get('DateTime', None)
        correction = timedelta(0)
        utz = tz.tzoffset('', 0)
        ltz = tz.gettz()
        if currtime:
            currtime = parse_time(currtime)
        if currtime:
            now = datetime.now(utz)
            try:
                correction = now - currtime
            except TypeError:
                correction = now - currtime.replace(tzinfo=utz)
        lurls = self._do_web_request(lsurl).get('Members', [])
        for lurl in lurls:
            lurl = lurl['@odata.id']
            loginfo = self._do_web_request(lurl, cache=(not clear))
            entriesurl = loginfo.get('Entries', {}).get('@odata.id', None)
            if not entriesurl:
                continue
            logid = loginfo.get('Id', '')
            entries = self._do_web_request(entriesurl, cache=False)
            if clear:
                # The clear is against the log service etag, not entries
                # so we have to fetch service etag after we fetch entries
                # until we can verify that the etag is consistent to prove
                # that the clear is atomic
                newloginfo = self._do_web_request(lurl, cache=False)
                clearurl = newloginfo.get('Actions', {}).get(
                    '#LogService.ClearLog', {}).get('target', '')
                while clearurl:
                    try:
                        self._do_web_request(clearurl, method='POST',
                                             payload={})
                        clearurl = False
                    except exc.PyghmiException as e:
                        if 'EtagPreconditionalFailed' not in str(e):
                            raise
                        # This doesn't guarantee atomicity, but it mitigates
                        # greatly.  Unfortunately some implementations
                        # mutate the tag endlessly and we have no hope
                        entries = self._do_web_request(entriesurl, cache=False)
                        newloginfo = self._do_web_request(lurl, cache=False)
            for log in entries.get('Members', []):
                record = {}
                record['log_id'] = logid
                parsedtime = parse_time(log.get('Created', ''))
                if parsedtime:
                    entime = parsedtime + correction
                    entime = entime.astimezone(ltz)
                    record['timestamp'] = entime.strftime('%Y-%m-%dT%H:%M:%S')
                else:
                    record['timestamp'] = log.get('Created', '')
                record['message'] = log.get('Message', None)
                record['severity'] = _healthmap.get(
                    entries.get('Severity', 'Warning'), const.Health.Critical)
                yield record

    def get_sensor_descriptions(self):
        for sensor in natural_sort(self._sensormap):
            yield self._sensormap[sensor]

    def get_sensor_reading(self, sensorname):
        if sensorname not in self._sensormap:
            raise Exception('Sensor not found')
        sensor = self._sensormap[sensorname]
        reading = self._do_web_request(sensor['url'], cache=1)
        return self._extract_reading(sensor, reading)

    def get_sensor_data(self):
        for sensor in natural_sort(self._sensormap):
            yield self.get_sensor_reading(sensor)

    def _extract_reading(self, sensor, reading):
        if sensor['type'] == 'Fan':
            for fan in reading['Fans']:
                if fan['Name'] == sensor['name']:
                    val = fan.get('Reading', None)
                    unavail = val is None
                    units = fan.get('ReadingUnits', None)
                    return SensorReading(
                        None, sensor, value=val, units=units,
                        unavailable=unavail)
        elif sensor['type'] == 'Temperature':
            for temp in reading['Temperatures']:
                if temp['Name'] == sensor['name']:
                    val = temp.get('ReadingCelsius', None)
                    unavail = val is None
                    return SensorReading(
                        None, sensor, value=val, units='°C',
                        unavailable=unavail)
        elif sensor['type'] == 'Voltage':
            for volt in reading['Voltages']:
                if volt['Name'] == sensor['name']:
                    val = volt.get('ReadingVolts', None)
                    unavail = val is None
                    return SensorReading(
                        None, sensor, value=val, units='V',
                        unavailable=unavail)

    def list_media(self):
        return self.oem.list_media(self)

    def get_storage_configuration(self):
        """"Get storage configuration data

        Retrieves the storage configuration from the target.  Data is given
        about disks, pools, and volumes.  When referencing something, use the
        relevant 'cfgpath' attribute to describe it.  It is not guaranteed that
        cfgpath will be consistent version to version, so a lookup is suggested
        in end user applications.

        :return: A pyghmi.storage.ConfigSpec object describing current config
        """
        return self.oem.get_storage_configuration()

    def remove_storage_configuration(self, cfgspec):
        """Remove specified storage configuration from controller.

        :param cfgspec: A pyghmi.storage.ConfigSpec describing what to remove
        :return:
        """
        return self.oem.remove_storage_configuration(cfgspec)

    def apply_storage_configuration(self, cfgspec=None):
        """Evaluate a configuration for validity

        This will check if configuration is currently available and, if given,
        whether the specified cfgspec can be applied.
        :param cfgspec: A pyghmi.storage.ConfigSpec describing desired oonfig
        :return:
        """
        return self.oem.apply_storage_configuration(cfgspec)

    def attach_remote_media(self, url, username=None, password=None):
        """Attach remote media by url

        Given a url, attach remote media (cd/usb image) to the target system.

        :param url:  URL to indicate where to find image (protocol support
                     varies by BMC)
        :param username: Username for endpoint to use when accessing the URL.
                         If applicable, 'domain' would be indicated by '@' or
                         '\' syntax.
        :param password: Password for endpoint to use when accessing the URL.
        """
        # At the moment, there isn't a viable way to
        # identify the correct resource ahead of time.
        # As such it's OEM specific until the standard
        # provides a better way.
        bmcinfo = self._do_web_request(self._bmcurl)
        vmcoll = bmcinfo.get('VirtualMedia', {}).get('@odata.id', None)
        vmurls = None
        if vmcoll:
            vmlist = self._do_web_request(vmcoll)
            vmurls = [x['@odata.id'] for x in vmlist.get('Members', [])]
        try:
            self.oem.attach_remote_media(url, username, password, vmurls)
        except exc.BypassGenericBehavior:
            return
        for vmurl in vmurls:
            vminfo = self._do_web_request(vmurl, cache=False)
            if vminfo['ConnectedVia'] != 'NotConnected':
                continue
            self._do_web_request(vmurl, {'Image': url, 'Inserted': True},
                                 'PATCH')
            break

    def detach_remote_media(self):
        bmcinfo = self._do_web_request(self._bmcurl)
        vmcoll = bmcinfo.get('VirtualMedia', {}).get('@odata.id', None)
        try:
            self.oem.detach_remote_media()
        except exc.BypassGenericBehavior:
            return
        if vmcoll:
            vmlist = self._do_web_request(vmcoll)
            vmurls = [x['@odata.id'] for x in vmlist.get('Members', [])]
            for vminfo in self._do_bulk_requests(vmurls):
                vminfo, currl = vminfo
                if vminfo['Image']:
                    self._do_web_request(currl,
                                         {'Image': None,
                                          'Inserted': False},
                                         method='PATCH')

    def upload_media(self, filename, progress=None):
        """Upload a file to be hosted on the target BMC

        This will upload the specified data to
        the BMC so that it will make it available to the system as an emulated
        USB device.

        :param filename: The filename to use, the basename of the parameter
                         will be given to the bmc.
        :param progress: Optional callback for progress updates
        """
        return self.oem.upload_media(filename, progress)

    def update_firmware(self, file, data=None, progress=None, bank=None):
        """Send file to BMC to perform firmware update

         :param filename:  The filename to upload to the target BMC
         :param data:  The payload of the firmware.  Default is to read from
                       specified filename.
         :param progress:  A callback that will be given a dict describing
                           update process.  Provide if
         :param bank: Indicate a target 'bank' of firmware if supported
        """
        return self.oem.update_firmware(file, data, progress, bank)

    def get_diagnostic_data(self, savefile, progress=None, autosuffix=False):
        if os.path.exists(savefile) and not os.path.isdir(savefile):
            raise exc.InvalidParameterValue(
                'Not allowed to overwrite existing file: {0}'.format(
                    savefile))
        return self.oem.get_diagnostic_data(savefile, progress, autosuffix)

    def get_licenses(self):
        return self.oem.get_licenses()

    def delete_license(self, name):
        return self.oem.delete_license(name)

    def save_licenses(self, directory):
        if os.path.exists(directory) and not os.path.isdir(directory):
            raise exc.InvalidParameterValue(
                'Not allowed to overwrite existing file: {0}'.format(
                    directory))
        return self.oem.save_licenses(directory)

    def apply_license(self, filename, progress=None):
        return self.oem.apply_license(filename, progress)


if __name__ == '__main__':
    print(repr(
        Command(sys.argv[1], os.environ['BMCUSER'], os.environ['BMCPASS'],
                verifycallback=lambda x: True).get_power()))
