# Copyright 2019 Intel, Corp.
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

from tempest.common import utils
from tempest.common import waiters
from tempest import config
from tempest.lib import decorators

from cyborg_tempest_plugin.services import cyborg_data
from cyborg_tempest_plugin.tests.scenario import manager

CONF = config.CONF


class TestServerBasicOps(manager.ScenarioTest):

    """The test suite for accelerator basic operations

    This smoke test case follows this basic set of operations:
     * Create a keypair for use in launching an instance
     * Create a security group to control network access in instance
     * Add simple permissive rules to the security group
     * Launch an instance
     * Terminate the instance

    """

    @classmethod
    def skip_checks(cls):
        super(TestServerBasicOps, cls).skip_checks()

    def setUp(self):
        super(TestServerBasicOps, self).setUp()

    @decorators.idempotent_id('7fff3fb3-91d8-4fd0-bd7d-0204f1f180ba')
    @decorators.attr(type='smoke')
    @utils.services('compute', 'network')
    def test_server_basic_ops(self):
        """Test for booting a VM with attached accelerator"""
        keypair = self.create_keypair()
        security_group = self._create_security_group()
        # flavor = self.create_flavor()
        response = self.create_device_profile(
            cyborg_data.SCENARIO_DEVICE_PROFILE_DATA)
        device_profile_name = response["name"]
        accl_flavor = self.create_accel_flavor(device_profile_name)
        self.instance = self.create_server(
            key_name=keypair['name'],
            security_groups=[{'name': security_group['name']}],
            name="cyborg-tempest-test-server",
            flavor=accl_flavor)
        self.servers_client.delete_server(self.instance['id'])
        waiters.wait_for_server_termination(
            self.servers_client, self.instance['id'], ignore_error=False)
