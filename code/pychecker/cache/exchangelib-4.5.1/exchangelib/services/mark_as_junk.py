from .common import EWSAccountService, create_item_ids_element
from ..properties import MovedItemId
from ..util import create_element


class MarkAsJunk(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/markasjunk-operation"""

    SERVICE_NAME = 'MarkAsJunk'

    def call(self, items, is_junk, move_item):
        return self._elems_to_objs(
            self._chunked_get_elements(self.get_payload, items=items, is_junk=is_junk, move_item=move_item)
        )

    def _elems_to_objs(self, elems):
        for elem in elems:
            if isinstance(elem, (Exception, type(None))):
                yield elem
                continue
            yield MovedItemId.id_from_xml(elem)

    @classmethod
    def _get_elements_in_container(cls, container):
        return container.findall(MovedItemId.response_tag())

    def get_payload(self, items, is_junk, move_item):
        # Takes a list of items and returns either success or raises an error message
        mark_as_junk = create_element(
            'm:%s' % self.SERVICE_NAME,
            attrs=dict(IsJunk='true' if is_junk else 'false', MoveItem='true' if move_item else 'false')
        )
        item_ids = create_item_ids_element(items=items, version=self.account.version)
        mark_as_junk.append(item_ids)
        return mark_as_junk
