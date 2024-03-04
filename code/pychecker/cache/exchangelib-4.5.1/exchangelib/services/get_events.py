import logging

from .common import EWSAccountService, add_xml_child
from ..properties import Notification
from ..util import create_element

log = logging.getLogger(__name__)


class GetEvents(EWSAccountService):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/getevents-operation
    """

    SERVICE_NAME = 'GetEvents'
    prefer_affinity = True

    def call(self, subscription_id, watermark):
        return self._elems_to_objs(self._get_elements(payload=self.get_payload(
                subscription_id=subscription_id, watermark=watermark,
        )))

    def _elems_to_objs(self, elems):
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            yield Notification.from_xml(elem=elem, account=None)

    @classmethod
    def _get_elements_in_container(cls, container):
        return container.findall(Notification.response_tag())

    def get_payload(self, subscription_id, watermark):
        getstreamingevents = create_element('m:%s' % self.SERVICE_NAME)
        add_xml_child(getstreamingevents, 'm:SubscriptionId', subscription_id)
        add_xml_child(getstreamingevents, 'm:Watermark', watermark)
        return getstreamingevents
