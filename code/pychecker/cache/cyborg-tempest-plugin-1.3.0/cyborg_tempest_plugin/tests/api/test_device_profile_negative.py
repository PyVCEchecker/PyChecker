# Copyright 2020 Inspur
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

import uuid

from cyborg_tempest_plugin.tests.api import base
from tempest.lib import exceptions as lib_exc
from tempest import test


class DeviceProfileNegativeTest(base.BaseAPITest):

    @classmethod
    def skip_checks(cls):
        super(DeviceProfileNegativeTest, cls).skip_checks()

    credentials = ['admin']

    @test.attr(type=['negative', 'gate'])
    def test_get_non_existent_device_profile(self):
        # get the non-existent device_profile
        non_existent_id = str(uuid.uuid4())
        self.assertRaises(lib_exc.NotFound,
                          self.os_admin.cyborg_client.get_device_profile,
                          non_existent_id)

    @test.attr(type=['negative', 'gate'])
    def test_delete_non_existent_device_profile(self):
        # delete the non-existent device_profile
        non_existent_id = str(uuid.uuid4())
        self.assertRaises(
            lib_exc.NotFound,
            self.os_admin.cyborg_client.delete_device_profile_by_uuid,
            non_existent_id)

    @test.attr(type=['negative', 'gate'])
    def test_create_device_profile_server_fault(self):
        # create device profile name same
        dp = [{
            "name": "fpga_same_test",
            "groups": [
                {
                    "resources:FPGA": "1",
                    "trait:CUSTOM_FAKE_DEVICE": "required"
                }]
        }]
        # create a device profile with named "fpga_same_test"
        response = self.os_admin.cyborg_client.create_device_profile(dp)
        self.assertEqual(dp[0]['name'], response['name'])
        self.addCleanup(self.os_admin.cyborg_client.delete_device_profile,
                        dp[0]['name'])
        dp[0]['name'] = 'new-fpga'
        dp[0]['uuid'] = response['uuid']

        # create a same device profile with the same uuid
        self.assertRaises(lib_exc.ServerFault,
                          self.os_admin.cyborg_client.create_device_profile,
                          dp)

    @test.attr(type=['negative', 'gate'])
    def test_create_device_profile_conflict(self):
        # create device profile name same
        dp = [{
            "name": "fpga_same_test",
            "groups": [
                {
                    "resources:FPGA": "1",
                    "trait:CUSTOM_FAKE_DEVICE": "required"
                }],
            "description": "null"
        }]
        # create a device profile with named "fpga_same_test"
        response = self.os_admin.cyborg_client.create_device_profile(dp)
        self.assertEqual(dp[0]['name'], response['name'])
        self.addCleanup(self.os_admin.cyborg_client.delete_device_profile,
                        dp[0]['name'])

        # create a same device profile with the same name "fpga_same_test"
        self.assertRaises(lib_exc.Conflict,
                          self.os_admin.cyborg_client.create_device_profile,
                          dp)
