import abc
import logging

from .common import EWSAccountService, add_xml_child, create_folder_ids_element, create_shape_element, parse_folder_elem
from ..properties import FolderId
from ..util import create_element, xml_text_to_value, MNS, TNS

log = logging.getLogger(__name__)


class SyncFolder(EWSAccountService, metaclass=abc.ABCMeta):
    """Base class for SyncFolderHierarchy and SyncFolderItems."""

    element_container_name = '{%s}Changes' % MNS
    # Change types
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'
    CHANGE_TYPES = (CREATE, UPDATE, DELETE)
    shape_tag = None
    last_in_range_name = None

    def __init__(self, *args, **kwargs):
        # These values are reset and set each time call() is consumed
        self.sync_state = None
        self.includes_last_item_in_range = None
        super().__init__(*args, **kwargs)

    def _change_types_map(self):
        return {
            '{%s}Create' % TNS: self.CREATE,
            '{%s}Update' % TNS: self.UPDATE,
            '{%s}Delete' % TNS: self.DELETE,
        }

    def _get_element_container(self, message, name=None):
        self.sync_state = message.find('{%s}SyncState' % MNS).text
        log.debug('Sync state is: %s', self.sync_state)
        self.includes_last_item_in_range = xml_text_to_value(
            message.find(self.last_in_range_name).text, bool
        )
        log.debug('Includes last item in range: %s', self.includes_last_item_in_range)
        return super()._get_element_container(message=message, name=name)

    def _partial_get_payload(self, folder, shape, additional_fields, sync_state):
        svc_elem = create_element('m:%s' % self.SERVICE_NAME)
        foldershape = create_shape_element(
            tag=self.shape_tag, shape=shape, additional_fields=additional_fields, version=self.account.version
        )
        svc_elem.append(foldershape)
        folder_id = create_folder_ids_element(tag='m:SyncFolderId', folders=[folder], version=self.account.version)
        svc_elem.append(folder_id)
        if sync_state:
            add_xml_child(svc_elem, 'm:SyncState', sync_state)
        return svc_elem


class SyncFolderHierarchy(SyncFolder):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/syncfolderhierarchy-operation
    """

    SERVICE_NAME = 'SyncFolderHierarchy'
    shape_tag = 'm:FolderShape'
    last_in_range_name = '{%s}IncludesLastFolderInRange' % MNS

    def call(self, folder, shape, additional_fields, sync_state):
        self.sync_state = sync_state
        change_types = self._change_types_map()
        for elem in self._get_elements(payload=self.get_payload(
                folder=folder,
                shape=shape,
                additional_fields=additional_fields,
                sync_state=sync_state,
        )):
            if isinstance(elem, Exception):
                yield elem
                continue
            change_type = change_types[elem.tag]
            if change_type == self.DELETE:
                folder = FolderId.from_xml(elem=elem.find(FolderId.response_tag()), account=self.account)
            else:
                # We can't find() the element because we don't know which tag to look for. The change element can
                # contain multiple folder types, each with their own tag.
                folder_elem = elem[0]
                folder = parse_folder_elem(elem=folder_elem, folder=folder, account=self.account)
            yield change_type, folder

    def get_payload(self, folder, shape, additional_fields, sync_state):
        return self._partial_get_payload(
            folder=folder, shape=shape, additional_fields=additional_fields, sync_state=sync_state
        )
