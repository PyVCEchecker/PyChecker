# Copyright 2019 Intel, Inc.
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

from cyborg_tempest_plugin.services import cyborg_data
from cyborg_tempest_plugin.tests.api import base


class TestDeviceProfileController(base.BaseAPITest):

    @classmethod
    def skip_checks(cls):
        super(TestDeviceProfileController, cls).skip_checks()

    credentials = ['admin']

    def test_create_device_profile(self):
        dp = cyborg_data.NORMAL_DEVICE_PROFILE_DATA1
        response = self.os_admin.cyborg_client.create_device_profile(dp)
        self.assertEqual(dp[0]['name'], response['name'])
        self.addCleanup(self.os_admin.cyborg_client.delete_device_profile,
                        dp[0]['name'])

    def test_delete_multiple_device_profile(self):
        dp_one = cyborg_data.BATCH_DELETE_DEVICE_PROFILE_DATA1
        dp_two = cyborg_data.BATCH_DELETE_DEVICE_PROFILE_DATA2
        dp_one_resp = self.os_admin.cyborg_client.create_device_profile(dp_one)
        dp_two_resp = self.os_admin.cyborg_client.create_device_profile(dp_two)
        self.assertEqual(dp_one[0]['name'], dp_one_resp['name'])
        self.assertEqual(dp_two[0]['name'], dp_two_resp['name'])
        self.os_admin.cyborg_client.delete_multiple_device_profile_by_names(
            dp_one[0]['name'], dp_two[0]['name'])
        list_resp = self.os_admin.cyborg_client.list_device_profile()
        device_profile_list = list_resp['device_profiles']
        device_profile_name_list = [it['name'] for it in device_profile_list]
        self.assertNotIn(dp_one[0]['name'], device_profile_name_list)
        self.assertNotIn(dp_two[0]['name'], device_profile_name_list)

    def test_get_and_delete_device_profile(self):
        dp = cyborg_data.NORMAL_DEVICE_PROFILE_DATA1
        create_resp = self.os_admin.cyborg_client.create_device_profile(dp)
        device_profile_uuid = create_resp['uuid']
        self.assertEqual(dp[0]['name'], create_resp['name'])
        self.assertEqual(dp[0]['groups'], create_resp['groups'])
        self.assertEqual(dp[0]['description'], create_resp['description'])

        list_resp = self.os_admin.cyborg_client.list_device_profile()
        device_profile_list = list_resp['device_profiles']
        device_profile_uuid_list = [it['uuid'] for it in device_profile_list]
        self.assertIn(device_profile_uuid, device_profile_uuid_list)

        get_resp = self.os_admin.cyborg_client.get_device_profile(
            device_profile_uuid)
        self.assertEqual(dp[0]['name'], get_resp['device_profile']['name'])
        self.assertEqual(device_profile_uuid,
                         get_resp['device_profile']['uuid'])

        self.os_admin.cyborg_client.delete_device_profile_by_uuid(
            device_profile_uuid)
        list_resp = self.os_admin.cyborg_client.list_device_profile()
        device_profile_list = list_resp['device_profiles']
        device_profile_uuid_list = [it['uuid'] for it in device_profile_list]
        self.assertNotIn(device_profile_uuid, device_profile_uuid_list)

    @classmethod
    def resource_cleanup(cls):
        super(TestDeviceProfileController, cls).resource_cleanup()
