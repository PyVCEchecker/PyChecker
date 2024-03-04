from .common import EWSAccountService, parse_folder_elem, create_folder_ids_element
from ..util import create_element, set_xml_value, MNS


class CreateFolder(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/createfolder-operation"""

    SERVICE_NAME = 'CreateFolder'
    element_container_name = '{%s}Folders' % MNS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.folders = []  # A hack to communicate parsing args to _elems_to_objs()

    def call(self, parent_folder, folders):
        # We can't easily find the correct folder class from the returned XML. Instead, return objects with the same
        # class as the folder instance it was requested with.
        self.folders = list(folders)  # Convert to a list, in case 'folders' is a generator. We're iterating twice.
        return self._elems_to_objs(self._chunked_get_elements(
                self.get_payload, items=self.folders, parent_folder=parent_folder,
        ))

    def _elems_to_objs(self, elems):
        for folder, elem in zip(self.folders, elems):
            if isinstance(elem, Exception):
                yield elem
                continue
            yield parse_folder_elem(elem=elem, folder=folder, account=self.account)

    def get_payload(self, folders, parent_folder):
        create_folder = create_element('m:%s' % self.SERVICE_NAME)
        parentfolderid = create_element('m:ParentFolderId')
        set_xml_value(parentfolderid, parent_folder, version=self.account.version)
        set_xml_value(create_folder, parentfolderid, version=self.account.version)
        folder_ids = create_folder_ids_element(tag='m:Folders', folders=folders, version=self.account.version)
        create_folder.append(folder_ids)
        return create_folder
