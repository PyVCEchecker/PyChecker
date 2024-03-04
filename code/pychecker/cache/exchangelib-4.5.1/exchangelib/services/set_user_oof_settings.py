from .common import EWSAccountService
from ..properties import AvailabilityMailbox, Mailbox
from ..settings import OofSettings
from ..util import create_element, set_xml_value, MNS


class SetUserOofSettings(EWSAccountService):
    """Set automatic replies for the specified mailbox.
    MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/setuseroofsettings-operation
    """

    SERVICE_NAME = 'SetUserOofSettings'
    returns_elements = False

    def call(self, oof_settings, mailbox):
        if not isinstance(oof_settings, OofSettings):
            raise ValueError("'oof_settings' %r must be an OofSettings instance" % oof_settings)
        if not isinstance(mailbox, Mailbox):
            raise ValueError("'mailbox' %r must be an Mailbox instance" % mailbox)
        return self._get_elements(payload=self.get_payload(oof_settings=oof_settings, mailbox=mailbox))

    def get_payload(self, oof_settings, mailbox):
        payload = create_element('m:%sRequest' % self.SERVICE_NAME)
        set_xml_value(payload, AvailabilityMailbox.from_mailbox(mailbox), version=self.account.version)
        set_xml_value(payload, oof_settings, version=self.account.version)
        return payload

    def _get_element_container(self, message, name=None):
        message = message.find(self._response_message_tag())
        return super()._get_element_container(message=message, name=name)

    @classmethod
    def _response_message_tag(cls):
        return '{%s}ResponseMessage' % MNS
