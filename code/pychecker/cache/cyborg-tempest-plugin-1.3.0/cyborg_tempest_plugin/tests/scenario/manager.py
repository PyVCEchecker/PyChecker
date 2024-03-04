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


from cyborg_tempest_plugin.services import cyborg_rest_client as clients
from cyborg_tempest_plugin.services.cyborg_rest_client import get_auth_provider

from oslo_log import log

from tempest.common import compute
from tempest.common import credentials_factory as common_creds
from tempest.common import waiters
from tempest import config
from tempest.lib.common.utils import data_utils
from tempest.lib.common.utils import test_utils
from tempest.lib import exceptions as lib_exc
import tempest.test


CONF = config.CONF

LOG = log.getLogger(__name__)


class ScenarioTest(tempest.test.BaseTestCase):
    """Base class for scenario tests. Uses tempest own clients. """

    credentials = ['primary', 'admin']

    @classmethod
    def skip_checks(cls):
        super(ScenarioTest, cls).skip_checks()
        if not CONF.service_available.cyborg:
            raise cls.skipException('Cyborg support is required')

    @classmethod
    def setup_clients(cls):
        super(ScenarioTest, cls).setup_clients()
        # Clients
        cls.admin_flavors_client = cls.admin_manager.flavors_client
        if CONF.service_available.glance:
            # Check if glance v1 is available to determine which client to use.
            if CONF.image_feature_enabled.api_v1:
                cls.image_client = cls.os_primary.image_client
            elif CONF.image_feature_enabled.api_v2:
                cls.image_client = cls.os_primary.image_client_v2
            else:
                raise lib_exc.InvalidConfiguration(
                    'Either api_v1 or api_v2 must be True in '
                    '[image-feature-enabled].')
        # Compute image client
        cls.compute_images_client = cls.os_primary.compute_images_client
        cls.keypairs_client = cls.os_primary.keypairs_client
        # Nova security groups client
        cls.compute_security_groups_client = (
            cls.os_primary.compute_security_groups_client)
        cls.compute_security_group_rules_client = (
            cls.os_primary.compute_security_group_rules_client)
        cls.servers_client = cls.os_primary.servers_client
        # Neutron network client
        cls.networks_client = cls.os_primary.networks_client
        cls.ports_client = cls.os_primary.ports_client

        credentials = common_creds.get_configured_admin_credentials(
            'identity_admin')

        auth_prov = get_auth_provider(credentials)
        cls.os_admin.cyborg_client = (
            clients.CyborgRestClient(auth_prov,
                                     'accelerator',
                                     CONF.identity.region))

    # ## Test functions library
    #
    # The create_[resource] functions only return body and discard the
    # resp part which is not used in scenario tests

    def create_keypair(self, client=None):
        if not client:
            client = self.keypairs_client
        name = data_utils.rand_name(self.__class__.__name__)
        # We don't need to create a keypair by pubkey in scenario
        body = client.create_keypair(name=name)
        self.addCleanup(client.delete_keypair, name)
        return body['keypair']

    def update_flavor_extra_specs(self, specs, flavor):
        set_body = self.admin_flavors_client.set_flavor_extra_spec(
            flavor['id'], **specs)['extra_specs']
        self.assertEqual(set_body, specs)
        # GET extra specs and verify
        get_body = (self.admin_flavors_client.list_flavor_extra_specs(
            flavor['id'])['extra_specs'])
        self.assertEqual(get_body, specs)
        return flavor

    def create_flavor(self, client=None):
        if not client:
            client = self.admin_flavors_client
        flavor_id = CONF.compute.flavor_ref
        flavor_base = self.admin_flavors_client.show_flavor(
            flavor_id)['flavor']
        name = data_utils.rand_name(self.__class__.__name__)
        ram = flavor_base['ram']
        vcpus = flavor_base['vcpus']
        disk = flavor_base['disk']
        body = client.create_flavor(name=name, ram=ram, vcpus=vcpus, disk=disk)
        flavor = body["flavor"]
        self.addCleanup(client.delete_flavor, flavor["id"])
        return flavor["id"]

    def create_device_profile(self, data, client=None):
        if not client:
            client = self.os_admin.cyborg_client
        body = client.create_device_profile(data)
        device_profile = body["name"]
        self.addCleanup(client.delete_device_profile, device_profile)
        return body

    def create_accel_flavor(self, dp_name, client=None):
        if not client:
            client = self.admin_flavors_client
        flavor_id = CONF.compute.flavor_ref
        flavor_base = self.admin_flavors_client.show_flavor(
            flavor_id)['flavor']
        name = data_utils.rand_name(self.__class__.__name__)
        ram = flavor_base['ram']
        vcpus = flavor_base['vcpus']
        disk = flavor_base['disk']
        body = client.create_flavor(name=name, ram=ram, vcpus=vcpus, disk=disk)
        flavor = body["flavor"]
        specs = {"accel:device_profile": dp_name}
        self.update_flavor_extra_specs(specs, flavor)
        return flavor["id"]

    def create_server(self, name=None, image_id=None, flavor=None,
                      validatable=False, wait_until='ACTIVE',
                      clients=None, **kwargs):

        """Wrapper utility that returns a test server.

        This wrapper utility calls the common create test server and
        returns a test server. The purpose of this wrapper is to minimize
        the impact on the code of the tests already using this
        function.

        """

        # NOTE(jlanoux): As a first step, ssh checks in the scenario
        # tests need to be run regardless of the run_validation and
        # validatable parameters and thus until the ssh validation job
        # becomes voting in CI. The test resources management and IP
        # association are taken care of in the scenario tests.
        # Therefore, the validatable parameter is set to false in all
        # those tests. In this way create_server just return a standard
        # server and the scenario tests always perform ssh checks.

        # Needed for the cross_tenant_traffic test:
        if clients is None:
            clients = self.os_primary

        if name is None:
            name = data_utils.rand_name(self.__class__.__name__ + "-server")

        vnic_type = CONF.network.port_vnic_type
        profile = CONF.network.port_profile

        # If vnic_type or profile are configured create port for
        # every network
        if vnic_type or profile:
            ports = []
            create_port_body = {}

            if vnic_type:
                create_port_body['binding:vnic_type'] = vnic_type

            if profile:
                create_port_body['binding:profile'] = profile

            if kwargs:
                # Convert security group names to security group ids
                # to pass to create_port
                if 'security_groups' in kwargs:
                    security_groups = \
                        clients.security_groups_client.list_security_groups(
                        ).get('security_groups')
                    sec_dict = dict([(s['name'], s['id'])
                                    for s in security_groups])

                    sec_groups_names = [s['name'] for s in kwargs.pop(
                        'security_groups')]
                    security_groups_ids = [sec_dict[s]
                                           for s in sec_groups_names]

                    if security_groups_ids:
                        create_port_body[
                            'security_groups'] = security_groups_ids
                networks = kwargs.pop('networks', [])
            else:
                networks = []

            # If there are no networks passed to us we look up
            # for the project's private networks and create a port.
            # The same behaviour as we would expect when passing
            # the call to the clients with no networks
            if not networks:
                networks = clients.networks_client.list_networks(
                    **{'router:external': False, 'fields': 'id'})['networks']

            # It's net['uuid'] if networks come from kwargs
            # and net['id'] if they come from
            # clients.networks_client.list_networks
            for net in networks:
                net_id = net.get('uuid', net.get('id'))
                if 'port' not in net:
                    port = self.create_port(network_id=net_id,
                                            client=clients.ports_client,
                                            **create_port_body)
                    ports.append({'port': port['id']})
                else:
                    ports.append({'port': net['port']})
            if ports:
                kwargs['networks'] = ports
            self.ports = ports

        tenant_network = self.get_tenant_network()
        body, _ = compute.create_test_server(
            clients,
            tenant_network=tenant_network,
            wait_until=wait_until,
            name=name, flavor=flavor,
            image_id=image_id, **kwargs)

        self.addCleanup(waiters.wait_for_server_termination,
                        clients.servers_client, body['id'])
        self.addCleanup(test_utils.call_and_ignore_notfound_exc,
                        clients.servers_client.delete_server, body['id'])
        server = clients.servers_client.show_server(body['id'])['server']
        return server

    def _create_loginable_secgroup_rule(self, secgroup_id=None):
        _client = self.compute_security_groups_client
        _client_rules = self.compute_security_group_rules_client
        if secgroup_id is None:
            sgs = _client.list_security_groups()['security_groups']
            for sg in sgs:
                if sg['name'] == 'default':
                    secgroup_id = sg['id']

        # These rules are intended to permit inbound ssh and icmp
        # traffic from all sources, so no group_id is provided.
        # Setting a group_id would only permit traffic from ports
        # belonging to the same security group.
        rulesets = [
            {
                # ssh
                'ip_protocol': 'tcp',
                'from_port': 22,
                'to_port': 22,
                'cidr': '0.0.0.0/0',
            },
            {
                # ping
                'ip_protocol': 'icmp',
                'from_port': -1,
                'to_port': -1,
                'cidr': '0.0.0.0/0',
            }
        ]
        rules = list()
        for ruleset in rulesets:
            sg_rule = _client_rules.create_security_group_rule(
                parent_group_id=secgroup_id, **ruleset)['security_group_rule']
            rules.append(sg_rule)
        return rules

    def _create_security_group(self):
        # Create security group
        sg_name = data_utils.rand_name(self.__class__.__name__)
        sg_desc = sg_name + " description"
        secgroup = self.compute_security_groups_client.create_security_group(
            name=sg_name, description=sg_desc)['security_group']
        self.assertEqual(secgroup['name'], sg_name)
        self.assertEqual(secgroup['description'], sg_desc)
        self.addCleanup(
            test_utils.call_and_ignore_notfound_exc,
            self.compute_security_groups_client.delete_security_group,
            secgroup['id'])

        # Add rules to the security group
        self._create_loginable_secgroup_rule(secgroup['id'])

        return secgroup
