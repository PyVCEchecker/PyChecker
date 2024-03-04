from .common import EWSAccountService
from ..properties import AvailabilityMailbox
from ..settings import OofSettings
from ..util import create_element, set_xml_value, MNS, TNS


class GetUserOofSettings(EWSAccountService):
    """Get automatic reply settings for the specified mailbox.
    MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/getuseroofsettings-operation
    """

    SERVICE_NAME = 'GetUserOofSettings'
    element_container_name = '{%s}OofSettings' % TNS

    def call(self, mailbox):
        return self._elems_to_objs(self._get_elements(payload=self.get_payload(mailbox=mailbox)))

    def _elems_to_objs(self, elems):
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            yield OofSettings.from_xml(elem=elem, account=self.account)

    def get_payload(self, mailbox):
        payload = create_element('m:%sRequest' % self.SERVICE_NAME)
        return set_xml_value(payload, AvailabilityMailbox.from_mailbox(mailbox), version=self.account.version)

    @classmethod
    def _get_elements_in_container(cls, container):
        # This service only returns one result, directly in 'container'
        return [container]

    def _get_element_container(self, message, name=None):
        # This service returns the result container outside the response message
        super()._get_element_container(message=message.find(self._response_message_tag()), name=None)
        return message.find(name)

    @classmethod
    def _response_message_tag(cls):
        return '{%s}ResponseMessage' % MNS
