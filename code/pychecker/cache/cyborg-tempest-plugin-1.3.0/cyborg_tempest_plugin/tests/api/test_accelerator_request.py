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


class TestAcceleratorRequestController(base.BaseAPITest):

    @classmethod
    def skip_checks(cls):
        super(TestAcceleratorRequestController, cls).skip_checks()

    credentials = ['admin']

    def test_create_accelerator_request(self):
        dp = [{
            "name": "test_example_1",
            "groups": [
                {"resources:FPGA": "1",
                 "trait:CUSTOM_FPGA_1": "required",
                 "trait:CUSTOM_FUNCTION_ID_3AFB": "required",
                 }
                ]
        }]
        response = self.os_admin.cyborg_client.create_device_profile(dp)
        device_profile_name = response['name']
        self.addCleanup(self.os_admin.cyborg_client.delete_device_profile,
                        dp[0]['name'])
        response = self.os_admin.cyborg_client.create_accelerator_request(
            {"device_profile_name": device_profile_name})
        self.assertEqual(device_profile_name,
                         response['arqs'][0]['device_profile_name'])
        self.addCleanup(self.os_admin.cyborg_client.delete_accelerator_request,
                        response['arqs'][0]['uuid'])

    def test_list_get_delete_accelerator_request(self):
        dp = [{
            "name": "test_example_2",
            "groups": [
                {"resources:FPGA": "1",
                 "trait:CUSTOM_FPGA_1": "required",
                 "trait:CUSTOM_FUNCTION_ID_3AFB": "required",
                 }
                ]
        }]
        response = self.os_admin.cyborg_client.create_device_profile(dp)
        device_profile_name = response['name']
        self.addCleanup(self.os_admin.cyborg_client.delete_device_profile,
                        dp[0]['name'])

        # create_accelerator_request
        response = self.os_admin.cyborg_client.create_accelerator_request(
            {"device_profile_name": device_profile_name})
        accelerator_request_uuid = response['arqs'][0]['uuid']

        # list accelerator request
        response = self.os_admin.cyborg_client.list_accelerator_request()
        uuid_list = [it['uuid'] for it in response['arqs']]
        self.assertIn(accelerator_request_uuid, uuid_list)

        # get accelerator request
        response = self.os_admin.cyborg_client.get_accelerator_request(
            accelerator_request_uuid)
        self.assertEqual(accelerator_request_uuid, response['uuid'])
        self.assertEqual(device_profile_name, response['device_profile_name'])

        # delete_accelerator_request
        self.os_admin.cyborg_client.delete_accelerator_request(
            accelerator_request_uuid)
        response = self.os_admin.cyborg_client.list_accelerator_request()
        uuid_list = [it['uuid'] for it in response['arqs']]
        self.assertNotIn(accelerator_request_uuid, uuid_list)

    @classmethod
    def resource_cleanup(cls):
        super(TestAcceleratorRequestController, cls).resource_cleanup()
