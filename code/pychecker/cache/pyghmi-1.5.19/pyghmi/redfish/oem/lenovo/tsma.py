# Copyright 2015-2017 Lenovo
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

import struct
import time
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

import pyghmi.exceptions as exc
import pyghmi.media as media
import pyghmi.redfish.oem.generic as generic
import pyghmi.util.webclient as webclient

hpm_by_filename = {}


class HpmSection(object):
    __slots__ = ['comp_id', 'comp_ver', 'comp_name', 'section_flash', 'data',
                 'hash_size', 'combo_image']


def read_hpm(filename):
    hpminfo = []
    with open(filename, 'rb') as hpmfile:
        hpmfile.seek(0x20)
        skip = struct.unpack('>H', hpmfile.read(2))[0]
        hpmfile.seek(skip + 1, 1)
        sectype, compid = struct.unpack('BB', hpmfile.read(2))
        while sectype == 2:
            currsec = HpmSection()
            currsec.comp_id = compid
            hpmfile.seek(1, 1)
            major, minor, pat = struct.unpack('<BBI', hpmfile.read(6))
            currsec.comp_ver = '{0}.{1}.{2}'.format(major, minor, pat)
            currsec.comp_name = hpmfile.read(21).rstrip(b'\x00')
            currlen = struct.unpack('<I', hpmfile.read(4))[0] - 16
            oemstr = hpmfile.read(4)
            if oemstr != b'OEM\x00':
                raise Exception(
                    'Unrecognized HPM field near {0}'.format(hpmfile.tell()))
            currsec.section_flash = struct.unpack('<I', hpmfile.read(4))[0]
            hashpresent, hdrsize, blocks = struct.unpack('BBB',
                                                         hpmfile.read(3))
            if hashpresent != 1:
                hashpresent = 0
            currsec.hash_size = hashpresent * (256 * blocks + hdrsize)
            hpmfile.seek(5, 1)
            currsec.data = hpmfile.read(currlen)
            hpminfo.append(currsec)
            sectype, compid = struct.unpack('BB', hpmfile.read(2))
        upimg = (hpminfo[1].data[:-hpminfo[1].hash_size]
                 + hpminfo[2].data[:-hpminfo[2].hash_size])
        hpminfo[2].combo_image = upimg
        hpminfo[1].combo_image = upimg
        currpos = hpmfile.tell()
        hpmfile.seek(0, 2)
        endpos = hpmfile.tell()
        if currpos < (endpos - 512):
            raise Exception("Unexpected end of HPM file")
    return hpminfo


class TsmHandler(generic.OEMHandler):
    hostnic = 'usb0'

    def __init__(self, sysinfo, sysurl, webclient, cache=None, fish=None):
        if cache is None:
            cache = {}
        self._wc = None
        self.username = None
        self.password = None
        self.csrftok = None
        self.isipmi = bool(fish)
        self.fish = fish
        super(TsmHandler, self).__init__(sysinfo, sysurl, webclient, cache)
        self.tsm = webclient.thehost
        self._certverify = webclient._certverify

    def clear_uefi_configuration(self):
        return self.fishclient.clear_system_configuration()

    def get_uefi_configuration(self, hideadvanced=True):
        return self.fishclient.get_system_configuration(hideadvanced)

    def set_uefi_configuration(self, changeset):
        return self.fishclient.set_system_configuration(changeset)

    def get_diagnostic_data(self, savefile, progress=None, autosuffix=False):
        wc = self.wc
        wc.grab_json_response('/api/mini_ffdc', {'action': 'trigger'})
        status = 1
        percent = 0
        while status == 1:
            time.sleep(5)
            check = wc.grab_json_response('/api/mini_ffdc',
                                          {'action': 'check'})
            status = check.get('status', -1)
            if progress:
                progress({'phase': 'initializing', 'progress': float(percent)})
            percent += 1
        if status != 2:
            raise Exception(
                "Unknown error generating service data: " + repr(check))
        if autosuffix and not savefile.endswith('.tar'):
            savefile += '.tar'
        fd = webclient.FileDownloader(wc, '/api/mini_ffdc/package', savefile)
        fd.start()
        while fd.isAlive():
            fd.join(1)
            if progress:
                currprog = self.wc.get_download_progress()
                if currprog:
                    progress({'phase': 'download',
                              'progress': 100 * currprog})
        if fd.exc:
            raise fd.exc
        if progress:
            progress({'phase': 'complete'})
        return savefile

    def init_redfish(self):
        self.fishclient = self.fish.Command(
            self.tsm, self.username, self.password,
            verifycallback=self._certverify)

    def get_firmware_inventory(self, components, raisebypass=True):
        wc = self.wc
        fwinf, status = wc.grab_json_response_with_status(
            '/api/DeviceVersion')
        gotinfo = False
        if status < 200 or status >= 300:
            raise Exception('Error connecting to HTTP API')
        for biosinf in fwinf:
            if biosinf.get('device', None) != 1:
                continue
            if not biosinf.get('buildname', False):
                break
            biosres = {
                'build': biosinf['buildname']
            }
            if biosinf.get('main', False):
                biosres['version'] = '{0}.{1}'.format(
                    biosinf['main'][0], biosinf['main'][1:])
            yield ('UEFI', biosres)
            gotinfo = True
            break
        for lxpminf in fwinf:
            if lxpminf.get('device', None) != 2:
                continue
            if not lxpminf.get('buildname', False):
                break
            lxpmres = {
                'build': lxpminf['buildname']
            }
            if lxpminf.get('main', False):
                subver = lxpminf.get('sub', 0)
                lxpmres['version'] = '{0}.{1:02x}'.format(
                    lxpminf['main'], subver)
            yield ('LXPM', lxpmres)
        name = 'TSM'
        fwinf, status = wc.grab_json_response_with_status('/api/get-sysfwinfo')
        if status != 200:
            raise Exception('Error {0} retrieving TSM version: {1}'.format(
                status, fwinf))
        for cinf in fwinf:
            bmcinf = {
                'version': cinf['fw_ver'],
                'build': cinf['buildname'],
                'date': cinf['builddate'],
            }
            yield (name, bmcinf)
            gotinfo = True
            name += ' Backup'
        if not gotinfo:
            raise Exception("Unable to retrieve firmware information")
        if raisebypass:
            raise exc.BypassGenericBehavior()

    @property
    def wc(self):
        self.fwid = None
        if self._wc:
            rsp, status = self._wc.grab_json_response_with_status(
                '/api/chassis-status')
            if status == 200:
                return self._wc
        authdata = {
            'username': self.username,
            'password': self.password,
        }
        wc = webclient.SecureHTTPConnection(self.tsm, 443,
                                            verifycallback=self._certverify,
                                            timeout=180)
        wc.set_header('Content-Type', 'application/json')
        rsp, status = wc.grab_json_response_with_status('/api/session',
                                                        authdata)
        if status == 403:
            wc.set_header('Content-Type', 'application/x-www-form-urlencoded')
            rsp, status = wc.grab_json_response_with_status(
                '/api/session', urlencode(authdata))

        if status < 200 or status >= 300:
            raise Exception('Error establishing web session')
        self.csrftok = rsp['CSRFToken']
        wc.set_header('X-CSRFTOKEN', self.csrftok)
        self._wc = wc
        return wc

    def update_firmware(self, filename, data=None, progress=None, bank=None):
        wc = self.wc
        wc.set_header('Content-Type', 'application/json')
        if filename.endswith('.hpm'):
            return self.update_hpm_firmware(filename, progress, wc)
        elif 'uefi' in filename and filename.endswith('.rom'):
            return self.update_sys_firmware(filename, progress, wc)
        elif 'amd-sas' in filename and filename.endswith('.bin'):
            return self.update_sys_firmware(filename, progress, wc, type='bp')
        elif 'lxpm' in filename and filename.endswith('.img'):
            return self.update_lxpm_firmware(filename, progress, wc)
        else:
            raise Exception('Unsupported filename {0}'.format(filename))

    def update_lxpm_firmware(self, filename, progress, wc):
        hdrs = wc.stdheaders.copy()
        hdrs['Content-Length'] = 0
        rsp = wc.grab_json_response_with_status(
            '/api/maintenance/LXPMUploadMode',
            method='PUT', headers=hdrs)
        # name fwimage filname filename application/x-raw-disk-image...
        fu = webclient.FileUploader(
            wc, '/api/maintenance/LXPMUpload',
            filename, formname='fwimage')
        fu.start()
        while fu.isAlive():
            fu.join(3)
            if progress:
                progress({
                    'phase': 'upload',
                    'progress': 100 * wc.get_upload_progress()})
        if progress:
            progress({
                'phase': 'apply',
                'progress': 0.0}
            )
        wc.grab_json_response('/api/maintenance/LXPMImageSplit', {'type': 3})
        completion = False
        while not completion:
            rsp = wc.grab_json_response('/api/maintenance/LXPMstatus')
            if rsp.get('state') == 0 and rsp.get('progress') == 4:
                break
        wc.grab_json_response_with_status(
            '/api/maintenance/Outofflash', method='PUT', headers=hdrs)
        return 'complete'

    def update_sys_firmware(self, filename, progress, wc, type='uefi'):
        if type == 'bp':
            rsp = wc.grab_json_response_with_status('/api/chassis-status')
            if rsp[0]['power_status'] == 1:
                raise Exception("Cannot update BP firmware while system is on")
            updatemode = 'BPUploadMode'
            fileupload = 'BPfileUpload'
            startit = 'BPUpgradeStart'
            statusname = 'BPstatus'
        else:
            updatemode = 'flash'
            rsp = wc.grab_json_response_with_status(
                '/api/maintenance/BIOSremoteSave',
                {"tftpip": "",
                 "tftpfile": ""}
            )
            fileupload = 'firmware/BIOS'
            startit = 'BIOSstart'
            statusname = 'BIOSstatus'
        hdrs = wc.stdheaders.copy()
        hdrs['Content-Length'] = 0
        rsp = wc.grab_json_response_with_status(
            '/api/maintenance/{0}'.format(updatemode),
            method='PUT', headers=hdrs)
        fu = webclient.FileUploader(
            wc, '/api/maintenance/{0}'.format(fileupload), filename,
            formname='fwimage')
        fu.start()
        while fu.isAlive():
            fu.join(3)
            if progress:
                progress({
                    'phase': 'upload',
                    'progress': 100 * wc.get_upload_progress()})
        if progress:
            progress({
                'phase': 'apply',
                'progress': 0.0}
            )
        rsp = wc.grab_json_response_with_status(
            '/api/maintenance/{0}'.format(startit))
        applypct = 0.0
        if rsp[1] >= 200 and rsp[1] < 300 and rsp[0]['wRet'] == 0:
            updone = False
            while not updone:
                rsp = wc.grab_json_response(
                    '/api/maintenance/{0}'.format(statusname))
                if rsp.get('state', 0) == 9:
                    break
                if rsp.get('state', 0) in (6, 10):
                    raise Exception('Update Failure')
                if (rsp.get('state', 0) == 8
                        and rsp.get('progress', 0) > 0 and progress):
                    progress({
                        'phase': 'apply',
                        'progress': 70 + float(rsp.get(
                            'progress', 0)) / 100 * 30})
                elif type == 'bp' and rsp.get('state', 0) == 1:
                    break
                elif progress and applypct < 70:
                    applypct += 1.4
                    progress({'phase': 'apply', 'progress': applypct})
            if type == 'bp':
                rsp = wc.grab_json_response('/api/maintenance/BPfinish')
                hdrs = wc.stdheaders.copy()
                hdrs['Content-Length'] = 0
                rsp = wc.grab_json_response_with_status(
                    '/api/maintenance/Outofflash', method='PUT', headers=hdrs)
                return 'complete'
            return 'pending'
        raise Exception('Update Failure')

    def update_hpm_firmware(self, filename, progress, wc):
        rsp = wc.grab_json_response('/api/maintenance/hpm/freemem')
        if 'MemFree' not in rsp:
            raise Exception('System Not Ready for update')
        if filename not in hpm_by_filename:
            hpminfo = read_hpm(filename)
            if len(hpminfo) != 3:
                raise Exception(
                    'This HPM update is currently not supported')
            hpm_by_filename[filename] = read_hpm(filename)
        else:
            hpminfo = hpm_by_filename[filename]
        rsp, status = wc.grab_json_response_with_status(
            '/api/maintenance/hpm/updatemode', method='PUT')
        # first segment, make sure it is mmc,
        # then do the preparecomponents with the following payload
        if status != 200:
            raise Exception(rsp)
        uid = rsp['unique_id']
        self.fwid = uid
        payload = {
            'FWUPDATEID': uid,
            'COMPONENT_ID': 1,
            'COMPONENT_DATA_LEN': len(hpminfo[0].data),
            'IS_MMC': 1,
        }
        rsp, status = wc.grab_json_response_with_status(
            '/api/maintenance/hpm/preparecomponents', payload, method='PUT')
        if status < 200 or status >= 300:
            wc.grab_json_response_with_status(
                '/api/maintenance/hpm/exitupdatemode', {'FWUPDATEID': uid},
                method='PUT')
            raise Exception(rsp)
        fu = webclient.FileUploader(
            wc, '/api/maintenance/hpm/mmcfw', 'blob', hpminfo[0].data, 'mmc')
        if progress:
            progress({'phase': 'upload', 'progress': 0.0})
        fu.start()
        while fu.isAlive():
            fu.join(3)
            if progress:
                progress({
                    'phase': 'upload',
                    'progress': 50 * wc.get_upload_progress()})
        del payload['IS_MMC']
        payload['SECTION_FLASH'] = hpminfo[0].section_flash
        rsp, status = wc.grab_json_response_with_status(
            '/api/maintenance/hpm/flash', payload, method='PUT')
        percent = 0
        while percent < 100:
            rsp, status = wc.grab_json_response_with_status(
                '/api/maintenance/hpm/upgradestatus?COMPONENT_ID=1')
            if status < 200 or status >= 300:
                raise Exception(rsp)
            percent = rsp['PROGRESS']
            if progress:
                progress({
                    'phase': 'apply',
                    'progress': .5 * percent})
            if percent < 100:
                time.sleep(3)
        if progress:
            progress({'phase': 'validating', 'progress': 0.0})
        del payload['SECTION_FLASH']
        rsp, status = wc.grab_json_response_with_status(
            '/api/maintenance/hpm/verifyimage', payload, method='PUT')
        percent = 0
        while percent < 100:
            rsp, status = wc.grab_json_response_with_status(
                '/api/maintenance/hpm/verifyimagestatus?COMPONENT_ID=1')
            if status < 200 or status >= 300:
                raise Exception(rsp)
            percent = rsp['PROGRESS']
            if progress:
                progress({
                    'phase': 'validating',
                    'progress': 0.5 * percent})
            if percent < 100:
                time.sleep(3)
        rsp, status = wc.grab_json_response_with_status(
            '/api/maintenance/hpm/exitupdatemode', {'FWUPDATEID': uid},
            method='PUT')
        fu = webclient.FileUploader(wc, '/api/maintenance/firmware/firmware',
                                    'blob', hpminfo[1].combo_image, 'fwimage')
        fu.start()
        while fu.isAlive():
            fu.join(3)
            if progress:
                progress({
                    'phase': 'upload',
                    'progress': 50 * wc.get_upload_progress() + 50})
        rsp = wc.grab_json_response('/api/maintenance/firmware/verification')
        upgradeparms = {
            'preserve_config': 1,
            'flash_status': 1,
        }
        rsp, status = wc.grab_json_response_with_status(
            '/api/maintenance/firmware/upgrade',
            upgradeparms, method='PUT')
        if progress:
            progress({'phase': 'apply', 'progress': 50.0})
        applied = False
        while not applied:
            rsp = wc.grab_json_response(
                '/api/maintenance/firmware/flash-progress')
            percent = float(rsp['progress'].split('%')[0])
            percent = percent * 0.5 + 50
            if progress:
                progress({'phase': 'apply', 'progress': percent})
            if rsp['progress'] == '100% done' and rsp['state'] == 0:
                applied = True
                break
            time.sleep(3)
        hdrs = wc.stdheaders.copy()
        hdrs['Content-Length'] = 0
        rsp = wc.grab_json_response_with_status(
            '/api/maintenance/reset', method='POST', headers=hdrs)
        self._wc = None
        return 'complete'

    def _detach_all_media(self, wc, slots):
        for slot in slots:  # Stop all active redirections to reconfigure
            if slot['redirection_status'] != 0:
                wc.grab_json_response(
                    '/api/settings/media/remote/stop-media',
                    {'image_name': slot['image_name'],
                     'image_type': slot['media_type'],
                     'image_index': slot['media_index']})

    def detach_remote_media(self):
        wc = self.wc
        slots = wc.grab_json_response(
            '/api/settings/media/remote/configurations')
        self._detach_all_media(wc, slots)
        if not self.isipmi:
            raise exc.BypassGenericBehavior()

    def _allocate_slot(self, slots, filetype, wc, server, path):
        currhdds = []
        currisos = []
        for slot in slots:
            if slot['image_name']:
                if slot['media_type'] == 1:
                    currisos.append(slot['image_name'])
                elif slot['media_type'] == 4:
                    currhdds.append(slot['image_name'])
                else:
                    raise exc.UnsupportedFunctionality(
                        'Unrecognized mounted image: ' + repr(slot))
        hddslots = len(currhdds)
        cdslots = len(currisos)
        if filetype == 1:
            cdslots += 1
        elif filetype == 4:
            hddslots += 1
        else:
            raise exc.UnsupportedFunctionality('Unknown slot type requested')
        gensettings = wc.grab_json_response('/api/settings/media/general')
        samesettings = gensettings['same_settings'] == 1
        if samesettings:
            hds = gensettings['cd_remote_server_address']
            hdp = gensettings['cd_remote_source_path'].replace('\\/', '/')
        else:
            hds = gensettings['hd_remote_server_address']
            hdp = gensettings['hd_remote_source_path'].replace('\\/', '/')
        if filetype == 1 and (currisos or (samesettings and currhdds)):
            if gensettings['cd_remote_server_address'] != server:
                raise exc.UnsupportedFunctionality(
                    'Cannot mount ISO images from multiple '
                    'servers at a time')
            if gensettings['cd_remote_source_path'].replace(
                    '\\/', '/') != path:
                raise exc.UnsupportedFunctionality(
                    'Cannot mount ISO images from different '
                    'directories at a time')
        if filetype == 4 and currhdds:
            if hds != server:
                raise exc.UnsupportedFunctionality(
                    'Cannot mount IMG images from multiple servers at a time')
            if hdp != path:
                raise exc.UnsupportedFunctionality(
                    'Cannot mount IMG images from muliple directories at a '
                    'time')
        self._detach_all_media(wc, slots)
        if filetype == 1 or (samesettings and currhdds):
            gensettings['cd_remote_server_address'] = server
            gensettings['cd_remote_source_path'] = path
            gensettings['cd_remote_share_type'] = 'nfs'
            gensettings['mount_cd'] = 1
        elif filetype == 4:
            gensettings['same_settings'] = 0
            gensettings['hd_remote_server_address'] = server
            gensettings['hd_remote_source_path'] = path
            gensettings['hd_remote_share_type'] = 'nfs'
            gensettings['mount_hd'] = 1
        gensettings['remote_media_support'] = 1
        gensettings['cd_remote_password'] = ''
        gensettings['hd_remote_password'] = ''
        wc.grab_json_response_with_status('/api/settings/media/general',
                                          gensettings, method='PUT')
        # need to calibrate instances correctly
        currinfo, status = wc.grab_json_response_with_status(
            '/api/settings/media/instance')
        currinfo['num_cd'] = cdslots
        currinfo['num_hd'] = hddslots
        if currinfo['kvm_num_cd'] > cdslots:
            currinfo['kvm_num_cd'] = cdslots
        if currinfo['kvm_num_hd'] > hddslots:
            currinfo['kvm_num_hd'] = hddslots
        wc.grab_json_response_with_status(
            '/api/settings/media/instance', currinfo, method='PUT')
        images = wc.grab_json_response('/api/settings/media/remote/images')
        tries = 20
        while tries and not images:
            tries -= 1
            time.sleep(1)
            images = wc.grab_json_response('/api/settings/media/remote/images')
        for iso in currisos:
            self._exec_mount(iso, images, wc)
        for iso in currhdds:
            self._exec_mount(iso, images, wc)

    def _exec_mount(self, name, images, wc):
        for img in images:
            if img['image_name'] == name:
                break
        else:
            raise exc.InvalidParameterValue(
                'Unable to locate image {0}'.format(name))
        wc.grab_json_response(
            '/api/settings/media/remote/start-media',
            {'image_name': name, 'image_type': img['image_type'],
             'image_index': img['image_index']})

    def upload_media(self, filename, progress=None):
        raise exc.UnsupportedFunctionality(
            'Remote media upload not supported on this system')

    def list_media(self, fishclient=None):
        wc = self.wc
        rsp = wc.grab_json_response('/api/settings/media/general')
        cds = rsp['cd_remote_server_address']
        cdpath = rsp['cd_remote_source_path']
        cdproto = rsp['cd_remote_share_type']
        if rsp['same_settings'] == 1:
            hds = cds
            hdpath = cdpath
            hdproto = cdproto
        else:
            hds = rsp['hd_remote_server_address']
            hdpath = rsp['hd_remote_source_path']
            hdproto = rsp['hd_remote_share_type']
        slots = wc.grab_json_response(
            '/api/settings/media/remote/configurations')
        for slot in slots:
            if slot['redirection_status'] == 1:
                url = None
                if slot['media_type'] == 1:
                    url = '{0}://{1}{2}'.format(
                        cdproto, cds, cdpath)
                elif slot['media_type'] == 4:
                    url = '{0}://{1}{2}'.format(
                        hdproto, hds, hdpath)
                if url:
                    yield media.Media(slot['image_name'], url)

    def attach_remote_media(self, url, user, password, vmurls):
        if not url.startswith('nfs://'):
            raise exc.UnsupportedFunctionality(
                'Only nfs:// urls are supported by this system')
        path = url.replace('nfs://', '')
        server, path = path.split('/', 1)
        path, filename = path.rsplit('/', 1)
        path = '/' + path
        filetype = filename.rsplit('.')[-1]
        if filetype == 'iso':
            filetype = 1
        elif filetype == 'img':
            filetype = 4
        else:
            raise exc.UnsupportedFunctionality(
                'Only iso and img files supported')
        wc = self.wc
        mountslots = wc.grab_json_response(
            '/api/settings/media/remote/configurations')
        images = wc.grab_json_response('/api/settings/media/remote/images')
        currtypeenabled = False
        for slot in mountslots:
            if slot['image_name'] == filename:
                return  # Already mounted...
        for img in images:
            if img['image_name'] == filename:
                break
            if img['image_type'] == filetype:
                currtypeenabled = True
        else:
            if currtypeenabled:
                raise exc.UnsupportedFunctionality(
                    'This system cannot mount images '
                    'from different locations at the same time')
            img = None
        for slot in mountslots:
            if slot['media_type'] != filetype:
                continue
            if slot['redirection_status'] == 0:
                break
        else:
            self._allocate_slot(mountslots, filetype, wc, server, path)
        images = wc.grab_json_response('/api/settings/media/remote/images')
        self._exec_mount(filename, images, wc)
        if not self.isipmi:
            raise exc.BypassGenericBehavior()
