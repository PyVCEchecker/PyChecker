from collections import OrderedDict

from .common import EWSAccountService, create_folder_ids_element
from ..util import create_element


class EmptyFolder(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/emptyfolder-operation"""

    SERVICE_NAME = 'EmptyFolder'
    returns_elements = False

    def call(self, folders, delete_type, delete_sub_folders):
        return self._chunked_get_elements(
            self.get_payload, items=folders, delete_type=delete_type, delete_sub_folders=delete_sub_folders
        )

    def get_payload(self, folders, delete_type, delete_sub_folders):
        emptyfolder = create_element(
            'm:%s' % self.SERVICE_NAME,
            attrs=OrderedDict([
                ('DeleteType', delete_type),
                ('DeleteSubFolders', 'true' if delete_sub_folders else 'false'),
            ])
        )
        folder_ids = create_folder_ids_element(tag='m:FolderIds', folders=folders, version=self.account.version)
        emptyfolder.append(folder_ids)
        return emptyfolder
