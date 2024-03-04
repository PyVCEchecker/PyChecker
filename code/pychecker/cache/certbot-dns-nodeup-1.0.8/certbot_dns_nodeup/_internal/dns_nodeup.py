from graphqlclient import GraphQLClient
import json
import logging
import zope.interface

logger = logging.getLogger(__name__)

from certbot import errors
from certbot import interfaces
from certbot.plugins import dns_common

@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)

class Authenticator(dns_common.DNSAuthenticator):
    """DNS Authenticator for Nodeup"""

    description = 'Obtain certs using a DNS TXT record.'

    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        self.credentials = None
        self.nodeup_dns_client = None # cached DNS client instance

    @classmethod
    def add_parser_arguments(cls, add):  # pylint: disable=arguments-differ
        super(Authenticator, cls).add_parser_arguments(add, default_propagation_seconds=5)
        add('credentials', help='Nodeup credentials INI file.')

    def more_info(self):  # pylint: disable=missing-function-docstring
        return 'This plugin configures a DNS TXT record to respond to a dns-01 challenge using the Nodeup API.'

    def _setup_credentials(self):
        self.credentials = self._configure_credentials('credentials', 'Nodeup credentials INI file', {'api_token': 'Must be written into nodeup.ini file and ini file given as a commandline parameter.'})

    def _perform(self, domain, validation_name, letsencrypt_txt_value):
        print('Nodeup: adding temporary TXT record for '+ repr((domain, letsencrypt_txt_value)))
        self.nodeup_dns_client = NodeupDNSClient(domain, nodeup_api_token=self.credentials.conf('api_token'))
        self.nodeup_dns_client.addDnsRecord(letsencrypt_txt_value)

    def _cleanup(self, domain, validation_name, letsencrypt_txt_value):
        if self.nodeup_dns_client:
            print('Nodeup: removing temporary TXT record for '+ repr((domain, letsencrypt_txt_value)))
            self.nodeup_dns_client.delDnsRecord()


class NodeupDNSClient:
    """
    Nodeup methods for LetsEncrypt DNS TXT validation.
    """
    def __init__(self, domain_name, nodeup_api_token):
        self.nodeup_api_token = nodeup_api_token
        self.domain_name = domain_name
        self.basedomain_name = ".".join(domain_name.split('.')[-2:])
        if len(domain_name.split('.')) >= 3:
            self.subdomain_name = ".".join(domain_name.split('.')[:-2])
        else:
            self.subdomain_name = None
        self.dns_record_id = None # ID of a created DNS record, needed by delete method later

    def client(self):
        QLClient = GraphQLClient('https://api.nodeup.io/graphql')
        QLClient.inject_token('Token '+self.nodeup_api_token)
        return QLClient
  
    def getDomainID(self):
        query = self.client().execute('''
            {
              domain(name: "'''+ self.basedomain_name +'''") {
                id
                name
                created
                updated
                expires
                dnsRecords {
                  id
                  name
                  type
                  data
                  ttl
                  __typename
                }
                __typename
              }
            }
            ''')
        res = json.loads(query)
        return res['data']['domain']['id']

    def addDnsRecord(self, letsencrypt_txt_value):
        record = {
            'dnsRecord': {
                'name': '_acme-challenge' + ".%s" % self.subdomain_name if self.subdomain_name else '_acme-challenge', 
                'type': 'TXT', 
                'data': '"'+ letsencrypt_txt_value +'"', 
                'ttl': 3600, 
                'domain': {
                  'id': self.getDomainID()
                }
            }
        }

        c = self.client()
        res_json = c.execute('''
            mutation CreateDnsRecord($dnsRecord: CreateDnsRecordInput!) {
                createDnsRecord(dnsRecord: $dnsRecord) {
                    id
                    name
                    type
                    data
                    ttl
                    domain {
                        id
                        name
                        created
                        updated
                        expires
                        __typename
                    }
                    __typename
                }
            }
            ''', json.dumps(record))

        res = json.loads(res_json)
        print("Nodeup response: " + repr(res))   
        self.dns_record_id = res['data']['createDnsRecord']['id']
        return res

    def delDnsRecord(self):
        c = self.client()
        res_json = c.execute('''
            mutation deleteDnsRecord($id: Int!) {
                deleteDnsRecord(id: $id) {
                    name
                    __typename
                }
            }
            ''', json.dumps({'id': self.dns_record_id}))
        res = json.loads(res_json)
        print("Nodeup response: " + repr(res))
        return res