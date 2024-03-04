import logging
from collections import OrderedDict

from .common import EWSAccountService, create_shape_element
from ..util import create_element, set_xml_value, MNS
from ..version import EXCHANGE_2013

log = logging.getLogger(__name__)


class FindPeople(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/findpeople-operation"""

    SERVICE_NAME = 'FindPeople'
    element_container_name = '{%s}People' % MNS
    supported_from = EXCHANGE_2013
    supports_paging = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # A hack to communicate parsing args to _elems_to_objs()
        self.additional_fields = None
        self.shape = None

    def call(self, folder, additional_fields, restriction, order_fields, shape, query_string, depth, max_items, offset):
        """Find items in an account.

        :param folder: the Folder object to query
        :param additional_fields: the extra fields that should be returned with the item, as FieldPath objects
        :param restriction: a Restriction object for
        :param order_fields: the fields to sort the results by
        :param shape: The set of attributes to return
        :param query_string: a QueryString object
        :param depth: How deep in the folder structure to search for items
        :param max_items: the max number of items to return
        :param offset: the offset relative to the first item in the item collection. Usually 0.

        :return: XML elements for the matching items
        """
        self.additional_fields = additional_fields
        self.shape = shape
        return self._elems_to_objs(self._paged_call(
            payload_func=self.get_payload,
            max_items=max_items,
            expected_message_count=1,  # We can only query one folder, so there will only be one element in response
            **dict(
                folder=folder,
                additional_fields=additional_fields,
                restriction=restriction,
                order_fields=order_fields,
                query_string=query_string,
                shape=shape,
                depth=depth,
                page_size=self.chunk_size,
                offset=offset,
            )
        ))

    def _elems_to_objs(self, elems):
        from ..items import Persona, ID_ONLY
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            if self.shape == ID_ONLY and self.additional_fields is None:
                yield Persona.id_from_xml(elem)
                continue
            yield Persona.from_xml(elem, account=self.account)

    def get_payload(self, folder, additional_fields, restriction, order_fields, query_string, shape, depth, page_size,
                    offset=0):
        findpeople = create_element('m:%s' % self.SERVICE_NAME, attrs=dict(Traversal=depth))
        personashape = create_shape_element(
            tag='m:PersonaShape', shape=shape, additional_fields=additional_fields, version=self.account.version
        )
        findpeople.append(personashape)
        view_type = create_element(
            'm:IndexedPageItemView',
            attrs=OrderedDict([
                ('MaxEntriesReturned', str(page_size)),
                ('Offset', str(offset)),
                ('BasePoint', 'Beginning'),
            ])
        )
        findpeople.append(view_type)
        if restriction:
            findpeople.append(restriction.to_xml(version=self.account.version))
        if order_fields:
            findpeople.append(set_xml_value(
                create_element('m:SortOrder'),
                order_fields,
                version=self.account.version
            ))
        findpeople.append(set_xml_value(
            create_element('m:ParentFolderId'),
            folder,
            version=self.account.version
        ))
        if query_string:
            findpeople.append(query_string.to_xml(version=self.account.version))
        return findpeople

    @staticmethod
    def _get_paging_values(elem):
        """Find paging values. The paging element from FindPeople is different from other paging containers."""
        item_count = int(elem.find('{%s}TotalNumberOfPeopleInView' % MNS).text)
        first_matching = int(elem.find('{%s}FirstMatchingRowIndex' % MNS).text)
        first_loaded = int(elem.find('{%s}FirstLoadedRowIndex' % MNS).text)
        log.debug('Got page with total items %s, first matching %s, first loaded %s ', item_count, first_matching,
                  first_loaded)
        next_offset = None  # GetPersona does not support fetching more pages
        return item_count, next_offset
