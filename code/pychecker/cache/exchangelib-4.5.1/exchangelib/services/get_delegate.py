from .common import EWSAccountService
from ..properties import DLMailbox, DelegateUser  # The service expects a Mailbox element in the MNS namespace
from ..util import create_element, set_xml_value, MNS
from ..version import EXCHANGE_2007_SP1


class GetDelegate(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/getdelegate-operation"""

    SERVICE_NAME = 'GetDelegate'
    supported_from = EXCHANGE_2007_SP1

    def call(self, user_ids, include_permissions):
        return self._elems_to_objs(self._chunked_get_elements(
            self.get_payload,
            items=user_ids or [None],
            mailbox=DLMailbox(email_address=self.account.primary_smtp_address),
            include_permissions=include_permissions,
        ))

    def _elems_to_objs(self, elems):
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            yield DelegateUser.from_xml(elem=elem, account=self.account)

    def get_payload(self, user_ids, mailbox, include_permissions):
        payload = create_element(
            'm:%s' % self.SERVICE_NAME,
            attrs=dict(IncludePermissions='true' if include_permissions else 'false'),
        )
        set_xml_value(payload, mailbox, version=self.protocol.version)
        if user_ids != [None]:
            set_xml_value(payload, user_ids, version=self.protocol.version)
        return payload

    @classmethod
    def _get_elements_in_container(cls, container):
        return container.findall(DelegateUser.response_tag())

    @classmethod
    def _response_message_tag(cls):
        return '{%s}DelegateUserResponseMessageType' % MNS
