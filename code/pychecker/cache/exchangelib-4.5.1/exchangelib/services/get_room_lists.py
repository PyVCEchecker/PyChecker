from .common import EWSService
from ..properties import RoomList
from ..util import create_element, MNS
from ..version import EXCHANGE_2010


class GetRoomLists(EWSService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/getroomlists-operation"""

    SERVICE_NAME = 'GetRoomLists'
    element_container_name = '{%s}RoomLists' % MNS
    supported_from = EXCHANGE_2010

    def call(self):
        return self._elems_to_objs(self._get_elements(payload=self.get_payload()))

    def _elems_to_objs(self, elems):
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            yield RoomList.from_xml(elem=elem, account=None)

    def get_payload(self):
        return create_element('m:%s' % self.SERVICE_NAME)
