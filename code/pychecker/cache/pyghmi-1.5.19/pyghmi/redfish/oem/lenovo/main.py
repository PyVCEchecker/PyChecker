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

import pyghmi.redfish.oem.generic as generic
from pyghmi.redfish.oem.lenovo import tsma
from pyghmi.redfish.oem.lenovo import xcc


def get_handler(sysinfo, sysurl, webclient, cache, cmd):
    leninf = sysinfo.get('Oem', {}).get('Lenovo', {})
    if not leninf:
        bmcinfo = cmd.bmcinfo
        if 'Ami' in bmcinfo.get('Oem', {}):
            return tsma.TsmHandler(sysinfo, sysurl, webclient, cache)
    if 'FrontPanelUSB' in leninf or sysinfo.get('SKU', '').startswith('7X58'):
        return xcc.OEMHandler(sysinfo, sysurl, webclient, cache)
    else:
        leninv = sysinfo.get('Links', {}).get('OEM', {}).get(
            'Lenovo', {}).get('Inventory', {})
        if 'hdd' in leninv and 'hostMAC' in leninv and 'backPlane' in leninv:
            return tsma.TsmHandler(sysinfo, sysurl, webclient, cache)
        return generic.OEMHandler(sysinfo, sysurl, webclient, cache)
