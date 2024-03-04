# Copyright 2015 Lenovo
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

from pyghmi.ipmi.oem.lenovo import inventory


firmware_fields = (
    inventory.EntryField("Revision", "B"),
    inventory.EntryField("Bios", "16s"),
    inventory.EntryField("Operational ME", "10s"),
    inventory.EntryField("Recovery ME", "10s"),
    inventory.EntryField("RAID 1", "16s"),
    inventory.EntryField("RAID 2", "16s"),
    inventory.EntryField("Mezz 1", "16s"),
    inventory.EntryField("Mezz 2", "16s"),
    inventory.EntryField("BMC", "16s"),
    inventory.EntryField("LEPT", "16s"),
    inventory.EntryField("PSU 1", "16s"),
    inventory.EntryField("PSU 2", "16s"),
    inventory.EntryField("CPLD", "16s"),
    inventory.EntryField("LIND", "16s"),
    inventory.EntryField("WIND", "16s"),
    inventory.EntryField("DIAG", "16s"))


def parse_firmware_info(raw):
    bytes_read, data = inventory.parse_inventory_category_entry(
        raw, firmware_fields)
    del data['Revision']
    for key in data:
        yield key, {'version': data[key]}


def get_categories():
    return {
        "firmware": {
            "idstr": "FW Version",
            "parser": parse_firmware_info,
            "command": {
                "netfn": 0x06,
                "command": 0x59,
                "data": (0x00, 0xc7, 0x00, 0x00)
            }
        }
    }
