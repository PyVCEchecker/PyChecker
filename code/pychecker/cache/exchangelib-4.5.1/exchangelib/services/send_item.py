from .common import EWSAccountService, create_item_ids_element
from ..util import create_element, set_xml_value


class SendItem(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/senditem-operation"""

    SERVICE_NAME = 'SendItem'
    returns_elements = False

    def call(self, items, saved_item_folder):
        from ..folders import BaseFolder, FolderId
        if saved_item_folder and not isinstance(saved_item_folder, (BaseFolder, FolderId)):
            raise ValueError("'saved_item_folder' %r must be a Folder or FolderId instance" % saved_item_folder)
        return self._chunked_get_elements(self.get_payload, items=items, saved_item_folder=saved_item_folder)

    def get_payload(self, items, saved_item_folder):
        senditem = create_element(
            'm:%s' % self.SERVICE_NAME,
            attrs=dict(SaveItemToFolder='true' if saved_item_folder else 'false'),
        )
        item_ids = create_item_ids_element(items=items, version=self.account.version)
        senditem.append(item_ids)
        if saved_item_folder:
            saveditemfolderid = create_element('m:SavedItemFolderId')
            set_xml_value(saveditemfolderid, saved_item_folder, version=self.account.version)
            senditem.append(saveditemfolderid)
        return senditem
