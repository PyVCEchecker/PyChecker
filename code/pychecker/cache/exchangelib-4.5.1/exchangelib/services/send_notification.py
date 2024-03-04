from .common import EWSService
from ..properties import Notification
from ..util import MNS


class SendNotification(EWSService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/sendnotification

    This is not an actual EWS service you can call. We only use it to parse the XML body of push notifications.
    """

    SERVICE_NAME = 'SendNotification'

    def call(self):
        raise NotImplementedError()

    def _elems_to_objs(self, elems):
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            yield Notification.from_xml(elem=elem, account=None)

    @classmethod
    def _response_tag(cls):
        """Return the name of the element containing the service response."""
        return '{%s}%s' % (MNS, cls.SERVICE_NAME)

    @classmethod
    def _get_elements_in_container(cls, container):
        return container.findall(Notification.response_tag())
