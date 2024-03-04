# Copyright 2019 Lenovo Corporation
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

import json
import os

import pyghmi.exceptions as exc
import pyghmi.media as media


class OEMHandler(object):
    hostnic = None

    def __init__(self, sysinfo, sysurl, webclient, cache):
        self._varsysinfo = sysinfo
        self._varsysurl = sysurl
        self._urlcache = cache
        self.webclient = webclient

    def _get_cache(self, url):
        now = os.times()[4]
        cachent = self._urlcache.get(url, None)
        if cachent and cachent['vintage'] > now - 30:
            return cachent['contents']
        return None

    def attach_remote_media(self, url, username, password, vmurls):
        return None

    def detach_remote_media(self):
        return None

    def get_description(self):
        return {}

    def get_firmware_inventory(self, components):
        return []

    def set_credentials(self, username, password):
        try:
            self.username = username.decode('utf-8')
        except AttributeError:
            self.username = username
        try:
            self.password = password.decode('utf-8')
        except AttributeError:
            self.password = password

    def list_media(self, fishclient):
        bmcinfo = fishclient._do_web_request(fishclient._bmcurl)
        vmcoll = bmcinfo.get('VirtualMedia', {}).get('@odata.id', None)
        if vmcoll:
            vmlist = fishclient._do_web_request(vmcoll)
            vmurls = [x['@odata.id'] for x in vmlist.get('Members', [])]
            for vminfo in fishclient._do_bulk_requests(vmurls):
                vminfo = vminfo[0]
                if vminfo['Image']:
                    imageurl = vminfo['Image'].replace(
                        '/' + vminfo['ImageName'], '')
                    yield media.Media(vminfo['ImageName'], imageurl)
                elif vminfo['Inserted'] and vminfo['ImageName']:
                    yield media.Media(vminfo['ImageName'])

    def get_storage_configuration(self):
        raise exc.UnsupportedFunctionality(
            'Remote storage configuration not supported on this platform')

    def remove_storage_configuration(self, cfgspec):
        raise exc.UnsupportedFunctionality(
            'Remote storage configuration not supported on this platform')

    def apply_storage_configuration(self, cfgspec):
        raise exc.UnsupportedFunctionality(
            'Remote storage configuration not supported on this platform')

    def upload_media(self, filename, progress=None):
        raise exc.UnsupportedFunctionality(
            'Remote media upload not supported on this platform')

    def update_firmware(self, filename, data=None, progress=None, bank=None):
        raise exc.UnsupportedFunctionality(
            'Firmware update not supported on this platform')

    def _do_web_request(self, url, payload=None, method=None, cache=True):
        res = None
        if cache and payload is None and method is None:
            res = self._get_cache(url)
        if res:
            return res
        wc = self.webclient.dupe()
        res = wc.grab_json_response_with_status(url, payload, method=method)
        if res[1] < 200 or res[1] >= 300:
            try:
                info = json.loads(res[0])
                errmsg = [
                    x.get('Message', x['MessageId']) for x in info.get(
                        'error', {}).get('@Message.ExtendedInfo', {})]
                errmsg = ','.join(errmsg)
                raise exc.RedfishError(errmsg)
            except (ValueError, KeyError):
                raise exc.PyghmiException(str(url) + ":" + res[0])
        if payload is None and method is None:
            self._urlcache[url] = {
                'contents': res[0],
                'vintage': os.times()[4]
            }
        return res[0]

    def get_diagnostic_data(self, savefile, progress=None, autosuffix=None):
        """Download diagnostic data about target to a file

        This should be a payload that the vendor's support team can use
        to do diagnostics.
        :param savefile: File object or filename to save to
        :param progress: Callback to be informed about progress
        :param autosuffix: Have the library automatically amend filename per
                           vendor support requirements.
        :return:
        """
        raise exc.UnsupportedFunctionality(
            'Retrieving diagnostic data is not implemented for this platform')

    def get_licenses(self):
        raise exc.UnsupportedFunctionality()

    def delete_license(self, name):
        raise exc.UnsupportedFunctionality()

    def save_licenses(self, directory):
        raise exc.UnsupportedFunctionality()

    def apply_license(self, filename, progress=None):
        raise exc.UnsupportedFunctionality()

    def get_user_expiration(self, uid):
        return None
