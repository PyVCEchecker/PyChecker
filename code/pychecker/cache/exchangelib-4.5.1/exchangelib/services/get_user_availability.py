from .common import EWSService
from ..properties import FreeBusyView
from ..util import create_element, set_xml_value, MNS


class GetUserAvailability(EWSService):
    """Get detailed availability information for a list of users.
    MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/getuseravailability-operation
    """

    SERVICE_NAME = 'GetUserAvailability'

    def call(self, timezone, mailbox_data, free_busy_view_options):
        # TODO: Also supports SuggestionsViewOptions, see
        #  https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/suggestionsviewoptions
        return self._elems_to_objs(self._get_elements(payload=self.get_payload(
            timezone=timezone,
            mailbox_data=mailbox_data,
            free_busy_view_options=free_busy_view_options
        )))

    def _elems_to_objs(self, elems):
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            yield FreeBusyView.from_xml(elem=elem, account=None)

    def get_payload(self, timezone, mailbox_data, free_busy_view_options):
        payload = create_element('m:%sRequest' % self.SERVICE_NAME)
        set_xml_value(payload, timezone, version=self.protocol.version)
        mailbox_data_array = create_element('m:MailboxDataArray')
        set_xml_value(mailbox_data_array, mailbox_data, version=self.protocol.version)
        payload.append(mailbox_data_array)
        set_xml_value(payload, free_busy_view_options, version=self.protocol.version)
        return payload

    @staticmethod
    def _response_messages_tag():
        return '{%s}FreeBusyResponseArray' % MNS

    @classmethod
    def _response_message_tag(cls):
        return '{%s}FreeBusyResponse' % MNS

    def _get_elements_in_response(self, response):
        for msg in response:
            # Just check the response code and raise errors
            self._get_element_container(message=msg.find('{%s}ResponseMessage' % MNS))
            yield from self._get_elements_in_container(container=msg)

    @classmethod
    def _get_elements_in_container(cls, container):
        return [container.find('{%s}FreeBusyView' % MNS)]
