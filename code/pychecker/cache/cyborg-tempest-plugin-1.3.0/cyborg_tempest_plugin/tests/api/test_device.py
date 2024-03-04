# Copyright 2020 Inspur, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from cyborg_tempest_plugin.tests.api import base


class TestDevice(base.BaseAPITest):

    @classmethod
    def skip_checks(cls):
        super(TestDevice, cls).skip_checks()

    credentials = ['admin']

    def test_list_get_device(self):
        response = self.os_admin.cyborg_client.list_devices()
        self.assertEqual('devices', list(response.keys())[0])

        device_uuid = response['devices'][0]['uuid']
        response = self.os_admin.cyborg_client.get_device(
            device_uuid)
        self.assertEqual(device_uuid, response['uuid'])

    @classmethod
    def resource_cleanup(cls):
        super(TestDevice, cls).resource_cleanup()
