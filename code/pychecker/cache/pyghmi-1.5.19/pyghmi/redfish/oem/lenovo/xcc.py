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


import errno
import json
import math
import os
import random
import socket
import time

import pyghmi.exceptions as pygexc
import pyghmi.ipmi.private.util as util
import pyghmi.redfish.oem.generic as generic
import pyghmi.storage as storage
from pyghmi.util.parse import parse_time
import pyghmi.util.webclient as webclient


class OEMHandler(generic.OEMHandler):

    def __init__(self, sysinfo, sysurl, webclient, cache):
        super(OEMHandler, self).__init__(sysinfo, sysurl, webclient, cache)
        self._wc = None
        self.updating = False

    def get_description(self):
        description = self._do_web_request('/DeviceDescription.json')
        if description:
            description = description[0]
        u_height = description.get('u-height', '')
        if not u_height and description.get(
                'enclosure-machinetype-model', '').startswith('7Y36'):
            u_height = '2'
        if not u_height:
            return {}
        u_height = int(u_height)
        slot = description.get('slot', '0')
        slot = int(slot)
        return {'height': u_height, 'slot': slot}

    def _get_agentless_firmware(self, components):
        adata = self.wc.grab_json_response(
            '/api/dataset/imm_adapters?params=pci_GetAdapters')
        anames = set()
        for adata in adata.get('items', []):
            baseaname = adata['adapterName']
            aname = baseaname
            idx = 1
            while aname in anames:
                aname = '{0} {1}'.format(baseaname, idx)
                idx += 1
            anames.add(aname)
            donenames = set()
            for fundata in adata['functions']:
                for firm in fundata.get('firmwares', []):
                    fname = firm['firmwareName'].rstrip()
                    if '.' in fname:
                        fname = firm['description'].rstrip()
                    if fname in donenames:
                        # ignore redundant entry
                        continue
                    if not fname:
                        continue
                    donenames.add(fname)
                    bdata = {}
                    if 'versionStr' in firm and firm['versionStr']:
                        bdata['version'] = firm['versionStr']
                    if ('releaseDate' in firm
                            and firm['releaseDate']
                            and firm['releaseDate'] != 'N/A'):
                        try:
                            bdata['date'] = parse_time(firm['releaseDate'])
                        except ValueError:
                            pass
                    yield '{0} {1}'.format(aname, fname), bdata

    def _get_disk_firmware_single(self, diskent, prefix=''):
        bdata = {}
        if not prefix and diskent.get('location', '').startswith('M.2'):
            prefix = 'M.2-'
        diskname = 'Disk {1}{0}'.format(diskent['slotNo'], prefix)
        bdata['model'] = diskent[
            'productName'].rstrip()
        bdata['version'] = diskent['fwVersion']
        return (diskname, bdata)

    def _get_disk_firmware(self, coponents):
        storagedata = storagedata = self.wc.grab_json_response(
            '/api/function/raid_alldevices?params=storage_GetAllDisks')
        for adp in storagedata.get('items', []):
            for diskent in adp.get('disks', ()):
                yield self._get_disk_firmware_single(diskent)
            for diskent in adp.get('aimDisks', ()):
                yield self._get_disk_firmware_single(diskent)

    def get_firmware_inventory(self, components):
        sysinf = self.wc.grab_json_response('/api/dataset/sys_info')
        for item in sysinf.get('items', {}):
            for firm in item.get('firmware', []):
                firminfo = {
                    'version': firm['version'],
                    'build': firm['build'],
                    'date': parse_time(firm['release_date']),
                }
                if firm['type'] == 5:
                    yield ('XCC', firminfo)
                elif firm['type'] == 6:
                    yield ('XCC Backup', firminfo)
                elif firm['type'] == 0:
                    yield ('UEFI', firminfo)
                elif firm['type'] == 7:
                    yield ('LXPM', firminfo)
                elif firm['type'] == 8:
                    yield ('LXPM Windows Driver Bundle', firminfo)
                elif firm['type'] == 9:
                    yield ('LXPM Linux Driver Bundle', firminfo)
        for adpinfo in self._get_agentless_firmware(components):
            yield adpinfo
        for adpinfo in self._get_disk_firmware(components):
            yield adpinfo
        raise pygexc.BypassGenericBehavior()

    def get_storage_configuration(self, logout=True):
        rsp = self.wc.grab_json_response(
            '/api/function/raid_alldevices?params=storage_GetAllDevices,0')
        if not rsp:
            rsp = self.wc.grab_json_response(
                '/api/function/raid_alldevices?params=storage_GetAllDevices')
        standalonedisks = []
        pools = []
        for item in rsp.get('items', []):
            for cinfo in item['controllerInfo']:
                cid = '{0},{1},{2}'.format(
                    cinfo['id'], cinfo.get('slotNo', -1), cinfo.get(
                        'type', -1))
                for pool in cinfo['pools']:
                    volumes = []
                    disks = []
                    spares = []
                    for volume in pool['volumes']:
                        volumes.append(
                            storage.Volume(name=volume['name'],
                                           size=volume['capacity'],
                                           status=volume['statusStr'],
                                           id=(cid, volume['id'])))
                    for disk in pool['disks']:
                        diskinfo = storage.Disk(
                            name=disk['name'], description=disk['type'],
                            id=(cid, disk['id']), status=disk['RAIDState'],
                            serial=disk['serialNo'], fru=disk['fruPartNo'])
                        if disk['RAIDState'] == 'Dedicated Hot Spare':
                            spares.append(diskinfo)
                        else:
                            disks.append(diskinfo)
                    totalsize = pool['totalCapacityStr'].replace('GB', '')
                    totalsize = int(float(totalsize) * 1024)
                    freesize = pool['freeCapacityStr'].replace('GB', '')
                    freesize = int(float(freesize) * 1024)
                    pools.append(storage.Array(
                        disks=disks, raid=pool['rdlvlstr'], volumes=volumes,
                        id=(cid, pool['id']), hotspares=spares,
                        capacity=totalsize, available_capacity=freesize))
                for disk in cinfo.get('unconfiguredDisks', ()):
                    # can be unused, global hot spare, or JBOD
                    standalonedisks.append(
                        storage.Disk(
                            name=disk['name'], description=disk['type'],
                            id=(cid, disk['id']), status=disk['RAIDState'],
                            serial=disk['serialNo'], fru=disk['fruPartNo']))
        return storage.ConfigSpec(disks=standalonedisks, arrays=pools)

    def _set_drive_state(self, disk, state):
        rsp = self.wc.grab_json_response(
            '/api/function',
            {'raidlink_DiskStateAction': '{0},{1}'.format(disk.id[1], state)})
        if rsp.get('return', -1) != 0:
            raise Exception(
                'Unexpected return to set disk state: {0}'.format(
                    rsp.get('return', -1)))

    def _refresh_token(self):
        self._refresh_token_wc(self.wc)

    def _refresh_token_wc(self, wc):
        wc.grab_json_response('/api/providers/identity')
        if '_csrf_token' in wc.cookies:
            wc.set_header('X-XSRF-TOKEN', self.wc.cookies['_csrf_token'])
            wc.vintage = util._monotonic_time()

    def _make_available(self, disk, realcfg):
        # 8 if jbod, 4 if hotspare.., leave alone if already...
        currstatus = self._get_status(disk, realcfg)
        newstate = None
        if currstatus == 'Unconfigured Good':
            return
        elif currstatus.lower() == 'global hot spare':
            newstate = 4
        elif currstatus.lower() == 'jbod':
            newstate = 8
        self._set_drive_state(disk, newstate)

    def _make_jbod(self, disk, realcfg):
        currstatus = self._get_status(disk, realcfg)
        if currstatus.lower() == 'jbod':
            return
        self._make_available(disk, realcfg)
        self._set_drive_state(disk, 16)

    def _make_global_hotspare(self, disk, realcfg):
        currstatus = self._get_status(disk, realcfg)
        if currstatus.lower() == 'global hot spare':
            return
        self._make_available(disk, realcfg)
        self._set_drive_state(disk, 1)

    def _get_status(self, disk, realcfg):
        for cfgdisk in realcfg.disks:
            if disk.id == cfgdisk.id:
                currstatus = cfgdisk.status
                break
        else:
            raise pygexc.InvalidParameterValue('Requested disk not found')
        return currstatus

    def _raid_number_map(self, controller):
        themap = {}
        cid = controller.split(',')
        rsp = self.wc.grab_json_response(
            '/api/function/raid_conf?'
            'params=raidlink_GetDisksToConf,{0}'.format(cid[0]))
        if rsp.get('return') == 22:  # New style firmware
            if cid[2] == 2:
                arg = '{0},{1}'.format(cid[1], cid[2])
            else:
                arg = '{0},{1}'.format(cid[0], cid[2])
            arg = 'params=raidlink_GetDisksToConf,{0}'.format(arg)
            rsp = self.wc.grab_json_response(
                '/api/function/raid_conf?{0}'.format(arg))
        for lvl in rsp['items'][0]['supported_raidlvl']:
            mapdata = (lvl['rdlvl'], lvl['maxSpan'])
            raidname = lvl['rdlvlstr'].replace(' ', '').lower()
            themap[raidname] = mapdata
            raidname = raidname.replace('raid', 'r')
            themap[raidname] = mapdata
            raidname = raidname.replace('r', '')
            themap[raidname] = mapdata
        return themap

    def _wait_storage_async(self):
        rsp = {'items': [{'status': 0}]}
        while rsp['items'][0]['status'] == 0:
            time.sleep(1)
            rsp = self.wc.grab_json_response(
                '/api/function/raid_conf?params=raidlink_QueryAsyncStatus')

    def _parse_array_spec(self, arrayspec):
        controller = None
        if arrayspec.disks:
            for disk in list(arrayspec.disks) + list(arrayspec.hotspares):
                if controller is None:
                    controller = disk.id[0]
                if controller != disk.id[0]:
                    raise pygexc.UnsupportedFunctionality(
                        'Cannot span arrays across controllers')
            raidmap = self._raid_number_map(controller)
            if not raidmap:
                raise pygexc.InvalidParameterValue(
                    'There are no available drives for a new array')
            requestedlevel = str(arrayspec.raid).lower()
            if requestedlevel not in raidmap:
                raise pygexc.InvalidParameterValue(
                    'Requested RAID "{0}" not available on this '
                    'system with currently available drives'.format(
                        requestedlevel))
            rdinfo = raidmap[str(arrayspec.raid).lower()]
            rdlvl = str(rdinfo[0])
            defspan = 1 if rdinfo[1] == 1 else 2
            spancount = defspan if arrayspec.spans is None else arrayspec.spans
            drivesperspan = str(len(arrayspec.disks) // int(spancount))
            hotspares = arrayspec.hotspares
            drives = arrayspec.disks
            if hotspares:
                hstr = '|'.join([str(x.id[1]) for x in hotspares]) + '|'
            else:
                hstr = ''
            drvstr = '|'.join([str(x.id[1]) for x in drives]) + '|'
            ctl = controller.split(',')
            pth = '/api/function/raid_conf?params=raidlink_CheckConfisValid'
            args = [pth, ctl[0], rdlvl, spancount, drivesperspan, drvstr,
                    hstr]
            url = ','.join([str(x) for x in args])
            rsp = self.wc.grab_json_response(url)
            if rsp.get('return', -1) == 22:
                args.append(ctl[1])
                args = [pth, ctl[0], rdlvl, spancount, drivesperspan, drvstr,
                        hstr, ctl[1]]
                url = ','.join([str(x) for x in args])
                rsp = self.wc.grab_json_response(url)
            if rsp['items'][0]['errcode'] == 16:
                raise pygexc.InvalidParameterValue('Incorrect number of disks')
            elif rsp['items'][0]['errcode'] != 0:
                raise pygexc.InvalidParameterValue(
                    'Invalid configuration: {0}'.format(
                        rsp['items'][0]['errcode']))
            return {
                'capacity': rsp['items'][0]['freeCapacity'],
                'controller': controller,
                'drives': drvstr,
                'hotspares': hstr,
                'raidlevel': rdlvl,
                'spans': spancount,
                'perspan': drivesperspan,
            }
        else:
            # TODO(Jarrod Johnson): adding new volume to
            #  existing array would be here
            pass

    def _create_array(self, pool):
        params = self._parse_array_spec(pool)
        cid = params['controller'].split(',')[0]
        url = '/api/function/raid_conf?params=raidlink_GetDefaultVolProp'
        args = (url, cid, 0, params['drives'])
        props = self.wc.grab_json_response(','.join([str(x) for x in args]))
        props = props['items'][0]
        volumes = pool.volumes
        remainingcap = params['capacity']
        nameappend = 1
        vols = []
        currvolnames = None
        currcfg = None
        for vol in volumes:
            if vol.name is None:
                # need to iterate while there exists a volume of that name
                if currvolnames is None:
                    currcfg = self.get_storage_configuration(False)
                    currvolnames = set([])
                    for pool in currcfg.arrays:
                        for volume in pool.volumes:
                            currvolnames.add(volume.name)
                name = props['name'] + '_{0}'.format(nameappend)
                nameappend += 1
                while name in currvolnames:
                    name = props['name'] + '_{0}'.format(nameappend)
                    nameappend += 1
            else:
                name = vol.name
            if vol.stripsize:
                stripsize = int(math.log(vol.stripsize * 2, 2))
            else:
                stripsize = props['stripsize']
            strsize = 'remainder' if vol.size is None else str(vol.size)
            if strsize in ('all', '100%'):
                volsize = params['capacity']
            elif strsize in ('remainder', 'rest'):
                volsize = remainingcap
            elif strsize.endswith('%'):
                volsize = int(params['capacity']
                              * float(strsize.replace('%', ''))
                              / 100.0)
            else:
                try:
                    volsize = int(strsize)
                except ValueError:
                    raise pygexc.InvalidParameterValue(
                        'Unrecognized size ' + strsize)
            remainingcap -= volsize
            if remainingcap < 0:
                raise pygexc.InvalidParameterValue(
                    'Requested sizes exceed available capacity')
            vols.append('{0};{1};{2};{3};{4};{5};{6};{7};{8};|'.format(
                name, volsize, stripsize, props['cpwb'], props['cpra'],
                props['cpio'], props['ap'], props['dcp'], props['initstate']))
        url = '/api/function'
        cid = params['controller'].split(',')
        cnum = cid[0]
        arglist = '{0},{1},{2},{3},{4},{5},'.format(
            cnum, params['raidlevel'], params['spans'],
            params['perspan'], params['drives'], params['hotspares'])
        arglist += ''.join(vols)
        parms = {'raidlink_AddNewVolWithNaAsync': arglist}
        rsp = self.wc.grab_json_response(url, parms)
        if rsp['return'] == 14:  # newer firmware
            if cid[2] == 2:
                cnum = cid[1]
            arglist = '{0},{1},{2},{3},{4},{5},'.format(
                cnum, params['raidlevel'], params['spans'],
                params['perspan'], params['drives'], params['hotspares'])
            arglist += ''.join(vols) + ',{0}'.format(cid[2])
            parms = {'raidlink_AddNewVolWithNaAsync': arglist}
            rsp = self.wc.grab_json_response(url, parms)
        if rsp['return'] != 0:
            raise Exception(
                'Unexpected response to add volume command: ' + repr(rsp))
        self._wait_storage_async()

    def remove_storage_configuration(self, cfgspec):
        realcfg = self.get_storage_configuration(False)
        for pool in cfgspec.arrays:
            for volume in pool.volumes:
                cid = volume.id[0].split(',')
                if cid[2] == 2:
                    vid = '{0},{1},{2}'.format(volume.id[1], cid[1], cid[2])
                else:
                    vid = '{0},{1},{2}'.format(volume.id[1], cid[0], cid[2])
                rsp = self.wc.grab_json_response(
                    '/api/function', {'raidlink_RemoveVolumeAsync': vid})
                if rsp.get('return', -1) == 2:
                    # older firmware
                    vid = '{0},{1}'.format(volume.id[1], cid[0])
                    rsp = self.wc.grab_json_response(
                        '/api/function', {'raidlink_RemoveVolumeAsync': vid})
                if rsp.get('return', -1) != 0:
                    raise Exception(
                        'Unexpected return to volume deletion: ' + repr(rsp))
                self._wait_storage_async()
        for disk in cfgspec.disks:
            self._make_available(disk, realcfg)

    def apply_storage_configuration(self, cfgspec):
        realcfg = self.get_storage_configuration(False)
        for disk in cfgspec.disks:
            if disk.status.lower() == 'jbod':
                self._make_jbod(disk, realcfg)
            elif disk.status.lower() == 'hotspare':
                self._make_global_hotspare(disk, realcfg)
            elif disk.status.lower() in ('unconfigured', 'available', 'ugood',
                                         'unconfigured good'):
                self._make_available(disk, realcfg)
        for pool in cfgspec.arrays:
            if pool.disks:
                self._create_array(pool)

    @property
    def wc(self):
        if (not self._wc or (self._wc.vintage
                             and self._wc.vintage < util._monotonic_time()
                             - 30)):
            self._wc = self.get_webclient()
        return self._wc

    def get_webclient(self, login=True):
        wc = self.webclient.dupe()
        wc.vintage = util._monotonic_time()
        try:
            wc.connect()
        except socket.error as se:
            if se.errno != errno.ECONNREFUSED:
                raise
            return None
        if not login:
            return wc
        referer = 'https://xcc/'
        adata = json.dumps({'username': self.username,
                            'password': self.password
                            })
        headers = {'Connection': 'keep-alive',
                   'Referer': referer,
                   'Host': 'xcc',
                   'Content-Type': 'application/json'}
        wc.request('POST', '/api/login', adata, headers)
        rsp = wc.getresponse()
        if rsp.status == 200:
            rspdata = json.loads(rsp.read())
            wc.set_header('Content-Type', 'application/json')
            wc.set_header('Authorization', 'Bearer ' + rspdata['access_token'])
            wc.set_header('Referer', referer)
            wc.set_header('Host', 'xcc')
            if '_csrf_token' in wc.cookies:
                wc.set_header('X-XSRF-TOKEN', wc.cookies['_csrf_token'])
            return wc

    def attach_remote_media(self, url, user, password, vmurls):
        for vmurl in vmurls:
            if 'EXT' not in vmurl:
                continue
            vminfo = self._do_web_request(vmurl, cache=False)
            if vminfo['ConnectedVia'] != 'NotConnected':
                continue
            self._do_web_request(vmurl, {'Image': url, 'Inserted': True},
                                 'PATCH')
            raise pygexc.BypassGenericBehavior()
            break
        else:
            raise pygexc.InvalidParameterValue(
                'XCC does not have required license for operation')

    def upload_media(self, filename, progress=None):
        xid = random.randint(0, 1000000000)
        self._refresh_token()
        uploadthread = webclient.FileUploader(
            self.wc, '/upload?X-Progress-ID={0}'.format(xid), filename, None)
        uploadthread.start()
        while uploadthread.isAlive():
            uploadthread.join(3)
            rsp = self.wc.grab_json_response(
                '/upload/progress?X-Progress-ID={0}'.format(xid))
            if progress and rsp['state'] == 'uploading':
                progress({'phase': 'upload',
                          'progress': 100.0 * rsp['received'] / rsp['size']})
            self._refresh_token()
        rsp = json.loads(uploadthread.rsp)
        if progress:
            progress({'phase': 'upload',
                      'progress': 100.0})
        thepath = rsp['items'][0]['path']
        thename = rsp['items'][0]['name']
        writeable = 1 if filename.lower().endswith('.img') else 0
        addfile = {"Url": thepath, "Protocol": 6, "Write": writeable,
                   "Credential": ":", "Option": "", "Domain": "",
                   "WebUploadName": thename}
        rsp = self.wc.grab_json_response('/api/providers/rp_rdoc_addfile',
                                         addfile)
        self._refresh_token()
        if rsp.get('return', -1) != 0:
            errmsg = repr(rsp) if rsp else self.wc.lastjsonerror
            raise Exception('Unrecognized return: ' + errmsg)
        ready = False
        while not ready:
            time.sleep(3)
            rsp = self.wc.grab_json_response('/api/providers/rp_rdoc_getfiles')
            if 'items' not in rsp or len(rsp['items']) == 0:
                raise Exception(
                    'Image upload was not accepted, it may be too large')
            ready = rsp['items'][0]['size'] != 0
        self._refresh_token()
        rsp = self.wc.grab_json_response('/api/providers/rp_rdoc_mountall',
                                         {})
        self._refresh_token()
        if rsp.get('return', -1) != 0:
            errmsg = repr(rsp) if rsp else self.wc.lastjsonerror
            raise Exception('Unrecognized return: ' + errmsg)
        if progress:
            progress({'phase': 'complete'})

    def update_firmware(self, filename, data=None, progress=None, bank=None):
        result = None
        if self.updating:
            raise pygexc.TemporaryError('Cannot run multiple updates to same '
                                        'target concurrently')
        self.updating = True
        try:
            result = self.update_firmware_backend(filename, data, progress,
                                                  bank)
        except Exception:
            self.updating = False
            self._refresh_token()
            self.wc.grab_json_response('/api/providers/fwupdate', json.dumps(
                {'UPD_WebCancel': 1}))
            raise
        self.updating = False
        return result

    def update_firmware_backend(self, filename, data=None, progress=None,
                                bank=None):
        self._refresh_token()
        rsv = self.wc.grab_json_response('/api/providers/fwupdate', json.dumps(
            {'UPD_WebReserve': 1}))
        if rsv['return'] == 103:
            raise Exception('Update already in progress')
        if rsv['return'] != 0:
            raise Exception('Unexpected return to reservation: ' + repr(rsv))
        xid = random.randint(0, 1000000000)
        uploadthread = webclient.FileUploader(
            self.wc, '/upload?X-Progress-ID={0}'.format(xid), filename, data)
        uploadthread.start()
        uploadstate = None
        while uploadthread.isAlive():
            uploadthread.join(3)
            rsp = self.wc.grab_json_response(
                '/upload/progress?X-Progress-ID={0}'.format(xid))
            if rsp['state'] == 'uploading':
                progress({'phase': 'upload',
                          'progress': 100.0 * rsp['received'] / rsp['size']})
            elif rsp['state'] != 'done':
                if (rsp.get('status', None) == 413
                        or uploadthread.rspstatus == 413):
                    raise Exception('File is larger than supported')
                raise Exception('Unexpected result:' + repr(rsp))
            uploadstate = rsp['state']
            self._refresh_token()
        while uploadstate != 'done':
            rsp = self.wc.grab_json_response(
                '/upload/progress?X-Progress-ID={0}'.format(xid))
            uploadstate = rsp['state']
            self._refresh_token()
        rsp = json.loads(uploadthread.rsp)
        if rsp['items'][0]['name'] != os.path.basename(filename):
            raise Exception('Unexpected response: ' + repr(rsp))
        progress({'phase': 'validating',
                  'progress': 0.0})
        time.sleep(3)
        # aggressive timing can cause the next call to occasionally
        # return 25 and fail
        self._refresh_token()
        rsp = self.wc.grab_json_response('/api/providers/fwupdate', json.dumps(
            {'UPD_WebSetFileName': rsp['items'][0]['path']}))
        if rsp.get('return', 0) in (25, 108):
            raise Exception('Temporary error validating update, try again')
        if rsp.get('return', -1) != 0:
            errmsg = repr(rsp) if rsp else self.wc.lastjsonerror
            raise Exception('Unexpected return to set filename: ' + errmsg)
        self._refresh_token()
        progress({'phase': 'validating',
                  'progress': 25.0})
        rsp = self.wc.grab_json_response('/api/providers/fwupdate', json.dumps(
            {'UPD_WebVerifyUploadFile': 1}))
        if rsp.get('return', 0) == 115:
            raise Exception('Update image not intended for this system')
        elif rsp.get('return', -1) == 108:
            raise Exception('Temporary error validating update, try again')
        elif rsp.get('return', -1) == 109:
            raise Exception('Invalid update file or component '
                            'does not support remote update')
        elif rsp.get('return', -1) != 0:
            errmsg = repr(rsp) if rsp else self.wc.lastjsonerror
            raise Exception('Unexpected return to verify: ' + errmsg)
        verifystatus = 0
        verifyuploadfilersp = None
        while verifystatus != 1:
            self._refresh_token()
            rsp, status = self.wc.grab_json_response_with_status(
                '/api/providers/fwupdate',
                json.dumps({'UPD_WebVerifyUploadFileStatus': 1}))
            if not rsp or status != 200 or rsp.get('return', -1) == 2:
                # The XCC firmware predates the FileStatus api
                verifyuploadfilersp = rsp
                break
            if rsp.get('return', -1) == 109:
                raise Exception('Invalid update file or component '
                                'does not support remote update')
            if rsp.get('return', -1) != 0:
                errmsg = repr(rsp) if rsp else self.wc.lastjsonerror
                raise Exception(
                    'Unexpected return to verifystate: {0}'.format(errmsg))
            verifystatus = rsp['status']
            if verifystatus == 2:
                raise Exception('Failed to verify firmware image')
            if verifystatus != 1:
                time.sleep(1)
            if verifystatus not in (0, 1, 255):
                errmsg = repr(rsp) if rsp else self.wc.lastjsonerror
                raise Exception(
                    'Unexpected reply to verifystate: ' + errmsg)
        progress({'phase': 'validating',
                  'progress': 99.0})
        self._refresh_token()
        rsp = self.wc.grab_json_response('/api/dataset/imm_firmware_success')
        if len(rsp['items']) != 1:
            raise Exception('Unexpected result: ' + repr(rsp))
        firmtype = rsp['items'][0]['firmware_type']
        if not firmtype:
            raise Exception('Unknown firmware description returned: ' + repr(
                rsp['items'][0]) + ' last verify return was: ' + repr(
                    verifyuploadfilersp) + ' with code {0}'.format(status))
        if firmtype not in (
                'TDM', 'WINDOWS DRIV', 'LINUX DRIVER', 'UEFI', 'IMM'):
            # adapter firmware
            webid = rsp['items'][0]['webfile_build_id']
            locations = webid[webid.find('[') + 1:webid.find(']')]
            locations = locations.split(':')
            validselectors = set([])
            for loc in locations:
                validselectors.add(loc.replace('#', '-'))
            self._refresh_token()
            rsp = self.wc.grab_json_response(
                '/api/function/adapter_update?params=pci_GetAdapterListAndFW')
            foundselectors = []
            for adpitem in rsp['items']:
                selector = '{0}-{1}'.format(adpitem['location'],
                                            adpitem['slotNo'])
                if selector in validselectors:
                    foundselectors.append(selector)
                    if len(foundselectors) == len(validselectors):
                        break
            else:
                raise Exception('Could not find matching adapter for update')
            self._refresh_token()
            rsp = self.wc.grab_json_response('/api/function', json.dumps(
                {'pci_SetOOBFWSlots': '|'.join(foundselectors)}))
            if rsp.get('return', -1) != 0:
                errmsg = repr(rsp) if rsp else self.wc.lastjsonerror
                raise Exception(
                    'Unexpected result from PCI select: ' + errmsg)
        else:
            self._refresh_token()
            rsp = self.wc.grab_json_response(
                '/api/dataset/imm_firmware_update')
            if rsp['items'][0]['upgrades'][0]['id'] != 1:
                raise Exception('Unexpected answer: ' + repr(rsp))
        self._refresh_token()
        progress({'phase': 'apply',
                  'progress': 0.0})
        if bank in ('primary', None):
            rsp = self.wc.grab_json_response(
                '/api/providers/fwupdate', json.dumps(
                    {'UPD_WebStartDefaultAction': 1}))
        elif bank == 'backup':
            rsp = self.wc.grab_json_response(
                '/api/providers/fwupdate', json.dumps(
                    {'UPD_WebStartOptionalAction': 2}))

        if rsp.get('return', -1) != 0:
            errmsg = repr(rsp) if rsp else self.wc.lastjsonerror
            raise Exception('Unexpected result starting update: %s' % errmsg)
        complete = False
        while not complete:
            time.sleep(3)
            rsp = self.wc.grab_json_response(
                '/api/dataset/imm_firmware_progress')
            progress({'phase': 'apply',
                      'progress': rsp['items'][0]['action_percent_complete']})
            if rsp['items'][0]['action_state'] == 'Idle':
                complete = True
                break
            if rsp['items'][0]['action_state'] == 'Complete OK':
                complete = True
                if rsp['items'][0]['action_status'] != 0:
                    raise Exception('Unexpected failure: %s' % repr(rsp))
                break
            if (rsp['items'][0]['action_state'] == 'In Progress'
                    and rsp['items'][0]['action_status'] == 2):
                raise Exception('Unexpected failure: ' + repr(rsp))
            if rsp['items'][0]['action_state'] != 'In Progress':
                raise Exception(
                    'Unknown condition waiting for '
                    'firmware update: %s' % repr(rsp))
        if bank == 'backup':
            return 'complete'
        return 'pending'

    def get_diagnostic_data(self, savefile, progress=None, autosuffix=False):
        self.wc.grab_json_response('/api/providers/ffdc',
                                   {'Generate_FFDC': 1})
        percent = 0
        while percent != 100:
            time.sleep(3)
            result = self.wc.grab_json_response('/api/providers/ffdc',
                                                {'Generate_FFDC_status': 1})
            self._refresh_token()
            if progress:
                progress({'phase': 'initializing', 'progress': float(percent)})
            percent = result['progress']
        while 'FileName' not in result:
            result = self.wc.grab_json_response('/api/providers/ffdc',
                                                {'Generate_FFDC_status': 1})
        url = '/ffdc/{0}'.format(result['FileName'])
        if autosuffix and not savefile.endswith('.tzz'):
            savefile += '.tzz'
        fd = webclient.FileDownloader(self.wc, url, savefile)
        fd.start()
        while fd.isAlive():
            fd.join(1)
            if progress and self.wc.get_download_progress():
                progress({'phase': 'download',
                          'progress': 100 * self.wc.get_download_progress()})
            self._refresh_token()
        if fd.exc:
            raise fd.exc
        if progress:
            progress({'phase': 'complete'})
        return savefile

    def get_licenses(self):
        licdata = self.wc.grab_json_response('/api/providers/imm_fod')
        for lic in licdata.get('items', [{}])[0].get('keys', []):
            if lic['status'] == 0:
                yield {'name': lic['feature'], 'state': 'Active'}
            if lic['status'] == 10:
                yield {
                    'name': lic['feature'],
                    'state': 'Missing required license'
                }

    def delete_license(self, name):
        licdata = self.wc.grab_json_response('/api/providers/imm_fod')
        for lic in licdata.get('items', [{}])[0].get('keys', []):
            if lic.get('feature', None) == name:
                licid = ','.join((str(lic['type']), str(lic['id'])))
                self.wc.grab_json_response(
                    '/api/providers/imm_fod',
                    {
                        'FOD_LicenseKeyDelete': licid
                    }
                )
                break

    def save_licenses(self, directory):
        licdata = self.wc.grab_json_response('/api/providers/imm_fod')
        for lic in licdata.get('items', [{}])[0].get('keys', []):
            licid = ','.join((str(lic['type']), str(lic['id'])))
            rsp = self.wc.grab_json_response(
                '/api/providers/imm_fod', {'FOD_LicenseKeyExport': licid})
            filename = rsp.get('FileName', None)
            if filename:
                url = '/download/' + filename
                savefile = os.path.join(directory, filename)
                fd = webclient.FileDownloader(self.wc, url, savefile)
                fd.start()
                while fd.isAlive():
                    fd.join(1)
                    self._refresh_token()
                yield savefile

    def apply_license(self, filename, progress=None):
        license_errors = {
            310: "License is for a different model of system",
            311: "License is for a different system serial number",
            312: "License is invalid",
            313: "License is expired",
            314: "License usage limit reached",
        }
        uploadthread = webclient.FileUploader(self.wc, '/upload', filename)
        uploadthread.start()
        uploadthread.join()
        rsp = json.loads(uploadthread.rsp)
        licpath = rsp.get('items', [{}])[0].get('path', None)
        if licpath:
            rsp = self.wc.grab_json_response(
                '/api/providers/imm_fod',
                {
                    'FOD_LicenseKeyInstall': licpath
                }
            )
            if rsp.get('return', 0) in license_errors:
                raise pygexc.InvalidParameterValue(
                    license_errors[rsp['return']])
        return self.get_licenses()

    def get_user_expiration(self, uid):
        userinfo = self.wc.grab_json_response('/api/dataset/imm_users')
        for user in userinfo['items'][0]['users']:
            if str(user['users_user_id']) == str(uid):
                days = user['users_pass_left_days']
                if days == 366:
                    return 0
                else:
                    return days
