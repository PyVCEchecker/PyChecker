from .common import EWSService
from ..errors import MalformedResponseError
from ..properties import SearchableMailbox, FailedMailbox
from ..util import create_element, add_xml_child, MNS
from ..version import EXCHANGE_2013


class GetSearchableMailboxes(EWSService):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/getsearchablemailboxes-operation
    """

    SERVICE_NAME = 'GetSearchableMailboxes'
    element_container_name = '{%s}SearchableMailboxes' % MNS
    failed_mailboxes_container_name = '{%s}FailedMailboxes' % MNS
    supported_from = EXCHANGE_2013

    def call(self, search_filter, expand_group_membership):
        return self._elems_to_objs(self._get_elements(payload=self.get_payload(
                search_filter=search_filter,
                expand_group_membership=expand_group_membership,
        )))

    def _elems_to_objs(self, elems):
        cls_map = {cls.response_tag(): cls for cls in (SearchableMailbox, FailedMailbox)}
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            yield cls_map[elem.tag].from_xml(elem=elem, account=None)

    def get_payload(self, search_filter, expand_group_membership):
        payload = create_element('m:%s' % self.SERVICE_NAME)
        if search_filter:
            add_xml_child(payload, 'm:SearchFilter', search_filter)
        if expand_group_membership is not None:
            add_xml_child(payload, 'm:ExpandGroupMembership', 'true' if expand_group_membership else 'false')
        return payload

    def _get_elements_in_response(self, response):
        for msg in response:
            for container_name in (self.element_container_name, self.failed_mailboxes_container_name):
                try:
                    container_or_exc = self._get_element_container(message=msg, name=container_name)
                except MalformedResponseError:
                    # Responses may contain no failed mailboxes. _get_element_container() does not accept this.
                    if container_name == self.failed_mailboxes_container_name:
                        continue
                    raise
                if isinstance(container_or_exc, (bool, Exception)):
                    yield container_or_exc
                    continue
                yield from self._get_elements_in_container(container=container_or_exc)
