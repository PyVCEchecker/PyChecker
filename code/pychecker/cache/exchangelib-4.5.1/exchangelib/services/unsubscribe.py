from .common import EWSAccountService, add_xml_child
from ..util import create_element


class Unsubscribe(EWSAccountService):
    """Unsubscribing is only valid for pull and streaming notifications.

    MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/unsubscribe-operation
    """

    SERVICE_NAME = 'Unsubscribe'
    returns_elements = False

    def call(self, subscription_id):
        return self._get_elements(payload=self.get_payload(subscription_id=subscription_id))

    def get_payload(self, subscription_id):
        unsubscribe = create_element('m:%s' % self.SERVICE_NAME)
        add_xml_child(unsubscribe, 'm:SubscriptionId', subscription_id)
        return unsubscribe
