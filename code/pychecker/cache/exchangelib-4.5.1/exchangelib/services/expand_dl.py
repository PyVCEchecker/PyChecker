from .common import EWSService
from ..errors import ErrorNameResolutionMultipleResults
from ..properties import Mailbox
from ..util import create_element, set_xml_value, MNS


class ExpandDL(EWSService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/expanddl-operation"""

    SERVICE_NAME = 'ExpandDL'
    element_container_name = '{%s}DLExpansion' % MNS
    WARNINGS_TO_IGNORE_IN_RESPONSE = ErrorNameResolutionMultipleResults

    def call(self, distribution_list):
        return self._elems_to_objs(self._get_elements(payload=self.get_payload(distribution_list=distribution_list)))

    def _elems_to_objs(self, elems):
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            yield Mailbox.from_xml(elem, account=None)

    def get_payload(self, distribution_list):
        payload = create_element('m:%s' % self.SERVICE_NAME)
        set_xml_value(payload, distribution_list, version=self.protocol.version)
        return payload
