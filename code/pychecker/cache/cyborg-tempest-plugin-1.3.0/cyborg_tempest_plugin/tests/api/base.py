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


from cyborg_tempest_plugin.services import cyborg_rest_client as client
from cyborg_tempest_plugin.services.cyborg_rest_client import get_auth_provider

from oslo_log import log as logging
from tempest.common import credentials_factory as common_creds
from tempest import config
from tempest import test


CONF = config.CONF
LOG = logging.getLogger(__name__)


class BaseAPITest(test.BaseTestCase):
    """Base test class for all Cyborg API tests."""

    # client_manager = cyborgclient.Manager

    @classmethod
    def skip_checks(cls):
        super(BaseAPITest, cls).skip_checks()
        if not CONF.service_available.cyborg:
            raise cls.skipException('Cyborg support is required')

    @classmethod
    def setup_clients(cls):
        super(BaseAPITest, cls).setup_clients()
        credentials = common_creds.get_configured_admin_credentials(
            'identity_admin')
        auth_prov = get_auth_provider(credentials=credentials)
        cls.os_admin.cyborg_client = (
            client.CyborgRestClient(auth_prov,
                                    'accelerator',
                                    CONF.identity.region))

    @classmethod
    def setup_credentials(cls):
        super(BaseAPITest, cls).setup_credentials()

    @classmethod
    def resource_setup(cls):
        super(BaseAPITest, cls).resource_setup()

    @classmethod
    def resource_cleanup(cls):
        super(BaseAPITest, cls).resource_cleanup()
