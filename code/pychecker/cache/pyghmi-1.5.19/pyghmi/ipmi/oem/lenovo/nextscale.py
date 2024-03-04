# Copyright 2016-2017 Lenovo
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

import fnmatch
import struct
import weakref
from xml.etree.ElementTree import fromstring
import zipfile

import six

import pyghmi.constants as pygconst
import pyghmi.exceptions as pygexc
import pyghmi.ipmi.private.session as ipmisession
from pyghmi.ipmi import sdr
import pyghmi.util.webclient as webclient

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

try:
    range = xrange
except NameError:
    pass


def stringtoboolean(originput, name):
    input = originput.lower()
    try:
        num = int(input)
    except ValueError:
        num = None
    if 'enabled'.startswith(input) or 'yes'.startswith(input) or num == 1:
        return True
    elif 'disabled'.startswith(input) or 'no'.startswith(input) or num == 0:
        return False
    raise pygexc.InvalidParameterValue('{0} is an invalid setting for '
                                       '{1}'.format(originput, name))


def fpc_read_ac_input(ipmicmd):
    rsp = ipmicmd.xraw_command(netfn=0x32, command=0x90, data=(1,))
    rsp = rsp['data']
    if len(rsp) == 6:
        rsp = b'\x00' + bytes(rsp)
    return struct.unpack_from('<H', rsp[3:5])[0]


def fpc_read_dc_output(ipmicmd):
    rsp = ipmicmd.xraw_command(netfn=0x32, command=0x90, data=(2,))
    rsp = rsp['data']
    if len(rsp) == 6:
        rsp = b'\x00' + bytes(rsp)
    return struct.unpack_from('<H', rsp[3:5])[0]


def fpc_read_fan_power(ipmicmd):
    rsp = ipmicmd.xraw_command(netfn=0x32, command=0x90, data=(3,))
    rsp = bytes(rsp['data'])
    rsp += b'\x00'
    return struct.unpack_from('<I', rsp[1:])[0] / 100.0


def fpc_read_psu_fan(ipmicmd, number, sz):
    rsp = ipmicmd.xraw_command(netfn=0x32, command=0xa5, data=(number,))
    rsp = bytes(rsp['data'])
    if len(rsp) > 5:
        return struct.unpack_from('<H', rsp[2:4])[0]
    else:
        return struct.unpack_from('<H', rsp[:2])[0]


def fpc_get_psustatus(ipmicmd, number, sz):
    rsp = ipmicmd.xraw_command(netfn=0x32, command=0x91)
    mask = 1 << (number - 1)
    if len(rsp['data']) == 6:
        statdata = bytearray([0])
    else:
        statdata = bytearray()
    statdata += bytearray(rsp['data'])
    presence = statdata[3] & mask == mask
    pwrgood = statdata[4] & mask == mask
    throttle = (statdata[6] | statdata[2]) & mask == mask
    health = pygconst.Health.Ok
    states = []
    if presence and not pwrgood:
        health = pygconst.Health.Critical
        states.append('Power input lost')
    if throttle:
        health = pygconst.Health.Critical
        states.append('Throttled')
    if presence:
        states.append('Present')
    else:
        states.append('Absent')
        health = pygconst.Health.Critical
    return (health, states)


def fpc_get_nodeperm(ipmicmd, number, sz):
    try:
        rsp = ipmicmd.xraw_command(netfn=0x32, command=0xa7, data=(number,))
    except pygexc.IpmiException as ie:
        if ie.ipmicode == 0xd5:  # no node present
            return (pygconst.Health.Ok, ['Absent'])
        raise
    health = pygconst.Health.Ok
    states = []
    if len(rsp['data']) == 4:  # different gens handled rc differently
        rsp['data'] = b'\x00' + bytes(rsp['data'])
    elif len(rsp['data']) == 6:  # New FPC format
        rsp['data'] = bytes(rsp['data'][:2]) + bytes(rsp['data'][3:])
    perminfo = bytearray(rsp['data'])[1]
    if sz == 6:  # FPC
        permfail = ('\x02', '\x03')
    else:  # SMM
        permfail = ('\x02',)
    if perminfo & 0x20:
        if rsp['data'][4] in permfail:
            states.append('Insufficient Power')
            health = pygconst.Health.Failed
        elif rsp['data'][3:5] != '\x00\x00':
            states.append('No Power Permission')
            health = pygconst.Health.Failed
    if perminfo & 0x40:
        states.append('Node Fault')
        health = pygconst.Health.Failed
    if rsp['data'][3:5] == '\x00\x00':
        states.append('Absent')
    return (health, states)


def fpc_read_powerbank(ipmicmd):
    rsp = ipmicmd.xraw_command(netfn=0x32, command=0xa2)
    return struct.unpack_from('<H', rsp['data'][3:])[0]


fpc_sensors = {
    'AC Power': {
        'type': 'Power',
        'units': 'W',
        'provider': fpc_read_ac_input,
    },
    'DC Power': {
        'type': 'Power',
        'units': 'W',
        'provider': fpc_read_dc_output,
    },
    'PSU Power Loss': {
        'type': 'Power',
        'units': 'W',
        'provider': fpc_read_dc_output,
    },
    'Fan Power': {
        'type': 'Power',
        'units': 'W',
        'provider': fpc_read_fan_power
    },
    'PSU Fan Speed': {
        'type': 'Fan',
        'units': 'RPM',
        'provider': fpc_read_psu_fan,
        'elements': 1,
    },
    'Total Power Capacity': {
        'type': 'Power',
        'units': 'W',
        'provider': fpc_read_powerbank,
    },
    'Node Power Permission': {
        'type': 'Management Subsystem Health',
        'returns': 'tuple',
        'units': None,
        'provider': fpc_get_nodeperm,
        'elements': 2,
    },
    'Power Supply': {
        'type': 'Power Supply',
        'returns': 'tuple',
        'units': None,
        'provider': fpc_get_psustatus,
        'elements': 1,
    }
}


def get_sensor_names(size):
    global fpc_sensors
    for name in fpc_sensors:
        if size != 6 and name in ('Fan Power', 'Total Power Capacity',
                                  'DC Power'):
            continue
        if size == 6 and name == 'PSU Power Loss':
            continue
        sensor = fpc_sensors[name]
        if 'elements' in sensor:
            for elemidx in range(sensor['elements'] * (size & 0b11111)):
                elemidx += 1
                yield '{0} {1}'.format(name, elemidx)
        else:
            yield name


def get_sensor_descriptions(size):
    global fpc_sensors
    for name in fpc_sensors:
        if size != 6 and name in ('Fan Power', 'Total Power Capacity',
                                  'DC Power'):
            continue
        if size == 6 and name == 'PSU Power Loss':
            continue
        sensor = fpc_sensors[name]
        if 'elements' in sensor:
            for elemidx in range(sensor['elements'] * (size & 0b11111)):
                elemidx += 1
                yield {'name': '{0} {1}'.format(name, elemidx),
                       'type': sensor['type']}
        else:
            yield {'name': name, 'type': sensor['type']}


def get_fpc_firmware(bmcver, ipmicmd, fpcorsmm):
    mymsg = ipmicmd.xraw_command(netfn=0x32, command=0xa8)
    builddata = bytearray(mymsg['data'])
    name = None
    if fpcorsmm != 6:  # SMM
        if fpcorsmm >> 5:
            name = 'SMM2'
        else:
            name = 'SMM'
        buildid = '{0}{1}{2}{3}{4}{5}{6}'.format(
            *[chr(x) for x in builddata[-7:]])
    elif len(builddata) == 8:
        builddata = builddata[1:]  # discard the 'completion code'
        name = 'FPC'
        buildid = '{0:02X}{1}'.format(builddata[-2], chr(builddata[-1]))
    bmcmajor, bmcminor = [int(x) for x in bmcver.split('.')]
    bmcver = '{0}.{1:02d}'.format(bmcmajor, bmcminor)
    yield (name, {'version': bmcver, 'build': buildid})
    if fpcorsmm == 6:
        yield ('PSOC', {'version': '{0}.{1}'.format(builddata[2],
                                                    builddata[3])})
    else:
        yield ('PSOC', {'version': '{0}.{1}'.format(builddata[3],
                                                    builddata[4])})


def get_sensor_reading(name, ipmicmd, sz):
    value = None
    sensor = None
    health = pygconst.Health.Ok
    states = []
    if name in fpc_sensors and 'elements' not in fpc_sensors[name]:
        sensor = fpc_sensors[name]
        value = sensor['provider'](ipmicmd)
    else:
        bnam, _, idx = name.rpartition(' ')
        idx = int(idx)
        if bnam in fpc_sensors and idx <= fpc_sensors[bnam]['elements'] * sz:
            sensor = fpc_sensors[bnam]
            if 'returns' in sensor:
                health, states = sensor['provider'](ipmicmd, idx, sz)
            else:
                value = sensor['provider'](ipmicmd, idx, sz)
    if sensor is not None:
        return sdr.SensorReading({'name': name, 'imprecision': None,
                                  'value': value, 'states': states,
                                  'state_ids': [], 'health': health,
                                  'type': sensor['type']},
                                 sensor['units'])
    raise Exception('Sensor not found: ' + name)


class SMMClient(object):

    def __init__(self, ipmicmd):
        self.ipmicmd = weakref.proxy(ipmicmd)
        self.smm = ipmicmd.bmc
        self.username = ipmicmd.ipmi_session.userid
        self.password = ipmicmd.ipmi_session.password
        self._wc = None

    def clear_bmc_configuration(self):
        self.ipmicmd.xraw_command(0x32, 0xad)

    rulemap = {
        'password_reuse_count': 'passwordReuseCheckNum',
        'password_change_interval': 'passwordChangeInterval',
        'password_expiration': 'passwordDurationDays',
        'password_login_failures': 'passwordFailAllowdNum',
        'password_min_length': 'passwordMinLength',
        'password_lockout_period': 'passwordLockoutTimePeriod',
    }

    fanmodes = {
        1: 'Capped_20%',
        2: 'Capped_25%',
        3: 'Capped_30%',
        4: 'Capped_45%',
        0: 'Normal',
        5: 'Boosted',
    }

    def get_bmc_configuration(self):
        settings = {}
        self.wc.request(
            'POST', '/data',
            ('get=passwordMinLength,passwordForceChange,passwordDurationDays,'
             'passwordExpireWarningDays,passwordChangeInterval,'
             'passwordReuseCheckNum,passwordFailAllowdNum,'
             'passwordLockoutTimePeriod'))
        rsp = self.wc.getresponse()
        rspbody = rsp.read()
        accountinfo = fromstring(rspbody)
        for rule in self.rulemap:
            ruleinfo = accountinfo.find(self.rulemap[rule])
            if ruleinfo:
                settings[rule] = {'value': int(ruleinfo.text)}
        rsp = self.ipmicmd.xraw_command(0x34, 3)
        fanmode = self.fanmodes[bytearray(rsp['data'])[0]]
        settings['fanspeed'] = {
            'value': fanmode, 'default': 'Normal',
            'help': ('Adjust the fan speed of the D2 Chassis. Capped settings '
                     'will reduce fan speed for better acoustic experience at '
                     'the expense of performance.  Normal is using the Lenovo '
                     'engineered cooling adjustments across the full range. '
                     'Boosted adds fanspeed to the Normal response to '
                     'provide more aggressive cooling.'),
            'possible': [self.fanmodes[x] for x in self.fanmodes]}
        powercfg = self.ipmicmd.xraw_command(0x32, 0xa2)
        powercfg = bytearray(powercfg['data'])
        if len(powercfg) == 5:
            powercfg = powercfg[1:]
        val = powercfg[0]
        if val == 2:
            val = 'N+N'
        elif val == 1:
            val = 'N+1'
        elif val == 0:
            val = 'Disable'
        settings['power_redundancy'] = {
            'default': 'N+1',
            'value': val,
            'possible': ['N+N', 'N+1', 'Disable'],
            'help': ('Configures allowed power budget according to expected '
                     'redundancy. If N+1, power caps will be set to keep '
                     'servers from using more power than the installed power '
                     'supplies could supply if one fails.  If disabled, '
                     'power budget is set to allow nodes to exceed the '
                     'capacity of a single power supply')
        }
        ovs = powercfg[1]
        if ovs == 1:
            ovs = 'Enable'
        elif ovs == 0:
            ovs = 'Disable'
        settings['power_oversubscription'] = {
            'default': 'Enable',
            'value': ovs,
            'possible': ['Enable', 'Disable'],
            'help': ('In redundant power configuration, permit the power '
                     'budget to exceed the capacity of a single power supply '
                     'so long as both power supplies are functioning. This '
                     'excess is limited to an amount that the remaining power '
                     'supply can sustain for a brief period of time in the '
                     'event of losing the other. This excess will be removed '
                     'at the moment a power supply fails so that power '
                     'delivery is at the sustained capacity of the remaining '
                     'supplies.')
        }
        try:
            dhcpsendname = self.ipmicmd.xraw_command(0xc, 0x2,
                                                     data=[1, 0xc5, 0, 0])
            dhcpsendname = bytearray(dhcpsendname['data'])
            dhcpsendname = 'Enable' if dhcpsendname[1] == 1 else 'Disable'
            settings['dhcp_sends_hostname'] = {
                'value': dhcpsendname,
                'help': ('Have the device send  hostname as part of its '
                         'DHCP client requests in option 12'),
                'possible': ['Enable', 'Disable']
            }
            dhcpsendvci = self.ipmicmd.xraw_command(0xc, 0x2,
                                                    data=[1, 0xc6, 0, 0])
            dhcpsendvci = bytearray(dhcpsendvci['data'])
            dhcpsendvci = 'Enable' if dhcpsendvci[1] == 1 else 'Disable'
            settings['dhcp_sends_vendor_class_identifier'] = {
                'value': dhcpsendvci,
                'possible': ['Enable', 'Disable'],
                'help': ('Have the device send vendor class identifier '
                         'as part of its DHCP requests in option 60')
            }
        except Exception:
            pass
        return settings

    def set_bmc_configuration(self, changeset, variant):
        rules = []
        powercfg = [None, None]
        sendhost = None
        sendvci = None
        for key in changeset:
            if not key:
                raise pygexc.InvalidParameterValue('Empty key is invalid')
            if isinstance(changeset[key], six.string_types):
                changeset[key] = {'value': changeset[key]}
            for rule in self.rulemap:
                if fnmatch.fnmatch(rule, key.lower()):
                    rules.append('{0}:{1}'.format(
                        self.rulemap[rule], changeset[key]['value']))
            if fnmatch.fnmatch('power_redundancy', key.lower()):
                if 'n+n'.startswith(changeset[key]['value'].lower()):
                    powercfg[0] = 2
                elif 'n+1'.startswith(changeset[key]['value'].lower()):
                    powercfg[0] = 1
                elif 'disable'.startswith(changeset[key]['value'].lower()):
                    powercfg[0] = 0
            if fnmatch.fnmatch('power_oversubscription', key.lower()):
                ovs = changeset[key]['value']
                ovs = stringtoboolean(changeset[key]['value'],
                                      'power_oversubscription')
                powercfg[1] = 1 if ovs else 0
            if fnmatch.fnmatch('dhcp_sends_hostname', key.lower()):
                sendhost = changeset[key]['value']
                sendhost = stringtoboolean(changeset[key]['value'],
                                           'dhcp_sends_hostname')
            if fnmatch.fnmatch(
                    'dhcp_sends_vendor_class_identifier', key.lower()):
                sendvci = changeset[key]['value']
                sendvci = stringtoboolean(
                    changeset[key]['value'],
                    'dhcp_sends_vendor_class_identifier')
            if fnmatch.fnmatch('fanspeed', key.lower()):
                for mode in self.fanmodes:
                    byteval = mode
                    mode = self.fanmodes[mode]
                    if changeset[key]['value'].lower() == mode.lower():
                        self.ipmicmd.xraw_command(
                            0x32, 0x9b, data=[byteval])
                        break
                else:
                    raise pygexc.InvalidParameterValue(
                        '{0} not a valid mode for fanspeed'.format(
                            changeset[key]['value']))
        if rules:
            rules = 'set={0}'.format(','.join(rules))
            self.wc.request('POST', '/data', rules)
            self.wc.getresponse().read()
        if powercfg != [None, None]:
            if variant == 2:
                if None in powercfg:
                    currcfg = self.ipmicmd.xraw_command(0x32, 0xa2)
                    currcfg = bytearray(currcfg['data'])
                    if powercfg[0] is None:
                        powercfg[0] = currcfg[0]
                    if powercfg[1] is None:
                        powercfg[1] = currcfg[1]
                self.ipmicmd.xraw_command(0x32, 0xa3, data=powercfg)
            elif variant == 6:
                if powercfg[0] is not None:
                    self.ipmicmd.xraw_command(0x32, 0xa3, data=powercfg[:1])
                if powercfg[1] is not None:
                    self.ipmicmd.xraw_command(0x32, 0x9c, data=powercfg[1:])
        if sendhost is not None:
            sendhost = 1 if sendhost else 0
            self.ipmicmd.xraw_command(0xc, 1, data=[1, 0xc5, sendhost])
        if sendvci is not None:
            sendvci = 1 if sendvci else 0
            self.ipmicmd.xraw_command(0xc, 1, data=[1, 0xc6, sendvci])

    def set_user_priv(self, uid, priv):
        if priv.lower() == 'administrator':
            rsp = self.ipmicmd.xraw_command(netfn=6, command=0x46, data=(uid,))
            username = bytes(rsp['data']).rstrip(b'\x00')
            self.wc.request(
                'POST', '/data', b'set=user({0},1,{1},511,,4,15,0)'.format(
                    uid, username))
            rsp = self.wc.getresponse()
            rsp.read()

    def reseat_bay(self, bay):
        self.ipmicmd.xraw_command(netfn=0x32, command=0xa4,
                                  data=[int(bay), 2])

    def get_diagnostic_data(self, savefile, progress=None):
        rsp = self.ipmicmd.xraw_command(netfn=0x32, command=0xb1, data=[0])
        if bytearray(rsp['data'])[0] != 0:
            raise Exception("Service data generation already in progress")
        rsp = self.ipmicmd.xraw_command(netfn=0x34, command=0x12, data=[0])
        if bytearray(rsp['data'])[0] != 0:
            raise Exception("Service data generation already in progress")
        rsp['data'] = b'\x01'
        initpct = 1.0
        if progress:
            progress({'phase': 'initializing', 'progress': initpct})
        while bytearray(rsp['data'])[0] != 0:
            ipmisession.Session.pause(3)
            initpct += 3.0
            if initpct > 99.0:
                initpct = 99.0
            rsp = self.ipmicmd.xraw_command(netfn=0x34, command=0x12, data=[1])
            if progress:
                progress({'phase': 'initializing', 'progress': initpct})
        if self.wc is None:
            raise Exception("Failed to connect to web api")
        url = '/preview/smm-ffdc.tgz?ST1={0}'.format(self.st1)
        fd = webclient.FileDownloader(self.wc, url, savefile)
        fd.start()
        while fd.isAlive():
            fd.join(1)
            if progress and self.wc.get_download_progress():
                progress({'phase': 'download',
                          'progress': 100 * self.wc.get_download_progress()})
        if progress:
            progress({'phase': 'complete'})
        return savefile

    def process_fru(self, fru):
        # TODO(jjohnson2): can also get EIOM, SMM, and riser data if warranted
        fru['Serial Number'] = bytes(self.ipmicmd.xraw_command(
            netfn=0x32, command=0xb0, data=(5, 1))['data'][:]).strip(
                b' \x00\xff').replace(b'\xff', b'')
        fru['Model'] = bytes(self.ipmicmd.xraw_command(
            netfn=0x32, command=0xb0, data=(5, 0))['data'][:]).strip(
                b' \x00\xff').replace(b'\xff', b'')
        return fru

    def get_webclient(self):
        cv = self.ipmicmd.certverify
        wc = webclient.SecureHTTPConnection(self.smm, 443, verifycallback=cv)
        wc.connect()
        loginform = urlencode(
            {
                'user': self.username,
                'password': self.password
            }
        )
        wc.request('POST', '/data/login', loginform)
        rsp = wc.getresponse()
        if rsp.status != 200:
            raise Exception(rsp.read())
        authdata = rsp.read()
        authdata = fromstring(authdata)
        for data in authdata.findall('authResult'):
            if int(data.text) != 0:
                raise Exception("Firmware update already in progress")
        for data in authdata.findall('forwardUrl'):
            if 'renew' in data.text:
                raise Exception("Account password has expired on remote "
                                "device")
        self.st1 = None
        self.st2 = None
        for data in authdata.findall('st1'):
            self.st1 = data.text
        for data in authdata.findall('st2'):
            self.st2 = data.text
        if not self.st2:
            # This firmware puts tokens in the html file, parse that
            wc.request('GET', '/index.html')
            rsp = wc.getresponse()
            if rsp.status != 200:
                raise Exception(rsp.read())
            indexhtml = rsp.read()
            if not isinstance(indexhtml, str):
                indexhtml = indexhtml.decode('utf8')
            for line in indexhtml.split('\n'):
                if '"ST1"' in line:
                    self.st1 = line.split()[-1].replace(
                        '"', '').replace(',', '')
                if '"ST2"' in line:
                    self.st2 = line.split()[-1].replace(
                        '"', '').replace(',', '')
        if not self.st2:
            wc.request('GET', '/scripts/index.ajs')
            rsp = wc.getresponse()
            body = rsp.read()
            if rsp.status != 200:
                raise Exception(body)
            if not isinstance(body, str):
                body = body.decode('utf8')
            for line in body.split('\n'):
                if '"ST1"' in line:
                    self.st1 = line.split()[-1].replace(
                        '"', '').replace(',', '')
                if '"ST2"' in line:
                    self.st2 = line.split()[-1].replace(
                        '"', '').replace(',', '')
        if not self.st2:
            raise Exception('Unable to locate ST2 token')
        wc.set_header('ST2', self.st2)
        return wc

    def set_hostname(self, hostname):
        self.wc.request('POST', '/data', 'set=hostname:' + hostname)
        rsp = self.wc.getresponse()
        if rsp.status != 200:
            raise Exception(rsp.read())
        rsp.read()
        self.logout()

    def get_hostname(self):
        currinfo = self.get_netinfo()
        self.logout()
        for data in currinfo.find('netConfig').findall('hostname'):
            return data.text

    def get_netinfo(self):
        self.wc.request('POST', '/data', 'get=hostname')
        rsp = self.wc.getresponse()
        data = rsp.read()
        if rsp.status == 400:
            self.wc.request('POST', '/data?get=hostname', '')
            rsp = self.wc.getresponse()
            data = rsp.read()
        if rsp.status != 200:
            raise Exception(data)
        currinfo = fromstring(data)
        return currinfo

    def set_domain(self, domain):
        self.wc.request('POST', '/data', 'set=dnsDomain:' + domain)
        rsp = self.wc.getresponse()
        if rsp.status != 200:
            raise Exception(rsp.read())
        rsp.read()
        self.logout()

    def get_domain(self):
        currinfo = self.get_netinfo()
        self.logout()
        for data in currinfo.find('netConfig').findall('dnsDomain'):
            return data.text

    def get_ntp_enabled(self, variant):
        self.wc.request('POST', '/data', 'get=ntpOpMode')
        rsp = self.wc.getresponse()
        info = fromstring(rsp.read())
        self.logout()
        for data in info.findall('ntpOpMode'):
            return data.text == '1'

    def set_ntp_enabled(self, enabled):
        self.wc.request('POST', '/data', 'set=ntpOpMode:{0}'.format(
            1 if enabled else 0))
        rsp = self.wc.getresponse()
        result = rsp.read()
        if not isinstance(result, str):
            result = result.decode('utf8')
        self.logout()
        if '<status>ok</status>' not in result:
            raise Exception("Unrecognized result: " + result)

    def set_ntp_server(self, server, index):
        self.wc.request('POST', '/data', 'set=ntpServer{0}:{1}'.format(
            index + 1, server))
        rsp = self.wc.getresponse()
        result = rsp.read()
        if not isinstance(result, str):
            result = result.decode('utf8')
        if '<status>ok</status>' not in result:
            raise Exception("Unrecognized result: " + result)
        self.logout()
        return True

    def get_ntp_servers(self):
        self.wc.request(
            'POST', '/data', 'get=ntpServer1,ntpServer2,ntpServer3')
        rsp = self.wc.getresponse()
        result = fromstring(rsp.read())
        srvs = []
        for data in result.findall('ntpServer1'):
            srvs.append(data.text)
        for data in result.findall('ntpServer2'):
            srvs.append(data.text)
        for data in result.findall('ntpServer3'):
            srvs.append(data.text)
        self.logout()
        return srvs

    def update_firmware(self, filename, data=None, progress=None, bank=None):
        if progress is None:
            progress = lambda x: True
        if not data and zipfile.is_zipfile(filename):
            z = zipfile.ZipFile(filename)
            for tmpname in z.namelist():
                if tmpname.endswith('.rom'):
                    filename = tmpname
                    data = z.open(filename)
                    break
        progress({'phase': 'upload', 'progress': 0.0})
        self.wc.request('POST', '/data', 'set=fwType:10')  # SMM firmware
        rsp = self.wc.getresponse()
        rsp.read()
        url = '/fwupload/fwupload.esp?ST1={0}'.format(self.st1)
        fu = webclient.FileUploader(
            self.wc, url, filename, data, formname='fileUpload',
            otherfields={'preConfig': 'on'})
        fu.start()
        while fu.isAlive():
            fu.join(3)
            if progress:
                progress({'phase': 'upload',
                          'progress': 100 * self.wc.get_upload_progress()})
        progress({'phase': 'validating', 'progress': 0.0})
        url = '/data'
        self.wc.request('POST', url, 'get=fwVersion,spfwInfo')
        rsp = self.wc.getresponse()
        rsp.read()
        if rsp.status != 200:
            raise Exception('Error validating firmware')
        progress({'phase': 'apply', 'progress': 0.0})
        self.wc.request('POST', '/data', 'set=securityrollback:1')
        self.wc.getresponse().read()
        self.wc.request('POST', '/data', 'set=fwUpdate:1')
        rsp = self.wc.getresponse()
        rsp.read()
        complete = False
        while not complete:
            ipmisession.Session.pause(3)
            self.wc.request('POST', '/data', 'get=fwProgress,fwUpdate')
            rsp = self.wc.getresponse()
            progdata = rsp.read()
            if rsp.status != 200:
                raise Exception('Error applying firmware')
            progdata = fromstring(progdata)
            if progdata.findall('fwUpdate')[0].text == 'invalid signature':
                raise Exception('Firmware signature invalid')
            percent = float(progdata.findall('fwProgress')[0].text)

            progress({'phase': 'apply',
                      'progress': percent})
            complete = percent >= 100.0
        return 'complete'

    def logout(self):
        self.wc.request('POST', '/data/logout', None)
        rsp = self.wc.getresponse()
        rsp.read()
        self._wc = None

    @property
    def wc(self):
        if not self._wc or self._wc.broken:
            self._wc = self.get_webclient()
        return self._wc
