from .common import EWSAccountService, create_folder_ids_element
from ..util import create_element


class DeleteFolder(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/deletefolder-operation"""

    SERVICE_NAME = 'DeleteFolder'
    returns_elements = False

    def call(self, folders, delete_type):
        return self._chunked_get_elements(self.get_payload, items=folders, delete_type=delete_type)

    def get_payload(self, folders, delete_type):
        deletefolder = create_element('m:%s' % self.SERVICE_NAME, attrs=dict(DeleteType=delete_type))
        folder_ids = create_folder_ids_element(tag='m:FolderIds', folders=folders, version=self.account.version)
        deletefolder.append(folder_ids)
        return deletefolder
