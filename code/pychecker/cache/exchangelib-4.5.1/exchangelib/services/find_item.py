from collections import OrderedDict

from .common import EWSAccountService, create_shape_element
from ..util import create_element, set_xml_value, TNS, MNS


class FindItem(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/finditem-operation"""

    SERVICE_NAME = 'FindItem'
    element_container_name = '{%s}Items' % TNS
    paging_container_name = '{%s}RootFolder' % MNS
    supports_paging = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # A hack to communicate parsing args to _elems_to_objs()
        self.additional_fields = None
        self.shape = None

    def call(self, folders, additional_fields, restriction, order_fields, shape, query_string, depth, calendar_view,
             max_items, offset):
        """Find items in an account.

        :param folders: the folders to act on
        :param additional_fields: the extra fields that should be returned with the item, as FieldPath objects
        :param restriction: a Restriction object for
        :param order_fields: the fields to sort the results by
        :param shape: The set of attributes to return
        :param query_string: a QueryString object
        :param depth: How deep in the folder structure to search for items
        :param calendar_view: If set, returns recurring calendar items unfolded
        :param max_items: the max number of items to return
        :param offset: the offset relative to the first item in the item collection. Usually 0.

        :return: XML elements for the matching items
        """
        self.additional_fields = additional_fields
        self.shape = shape
        return self._elems_to_objs(self._paged_call(
            payload_func=self.get_payload,
            max_items=max_items,
            expected_message_count=len(folders),
            **dict(
                folders=folders,
                additional_fields=additional_fields,
                restriction=restriction,
                order_fields=order_fields,
                query_string=query_string,
                shape=shape,
                depth=depth,
                calendar_view=calendar_view,
                page_size=self.chunk_size,
                offset=offset,
            )
        ))

    def _elems_to_objs(self, elems):
        from ..folders.base import BaseFolder
        from ..items import Item, ID_ONLY
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            if self.shape == ID_ONLY and self.additional_fields is None:
                yield Item.id_from_xml(elem)
                continue
            yield BaseFolder.item_model_from_tag(elem.tag).from_xml(elem=elem, account=self.account)

    def get_payload(self, folders, additional_fields, restriction, order_fields, query_string, shape, depth,
                    calendar_view, page_size, offset=0):
        finditem = create_element('m:%s' % self.SERVICE_NAME, attrs=dict(Traversal=depth))
        itemshape = create_shape_element(
            tag='m:ItemShape', shape=shape, additional_fields=additional_fields, version=self.account.version
        )
        finditem.append(itemshape)
        if calendar_view is None:
            view_type = create_element(
                'm:IndexedPageItemView',
                attrs=OrderedDict([
                    ('MaxEntriesReturned', str(page_size)),
                    ('Offset', str(offset)),
                    ('BasePoint', 'Beginning'),
                ])
            )
        else:
            view_type = calendar_view.to_xml(version=self.account.version)
        finditem.append(view_type)
        if restriction:
            finditem.append(restriction.to_xml(version=self.account.version))
        if order_fields:
            finditem.append(set_xml_value(
                create_element('m:SortOrder'),
                order_fields,
                version=self.account.version
            ))
        finditem.append(set_xml_value(
            create_element('m:ParentFolderIds'),
            folders,
            version=self.account.version
        ))
        if query_string:
            finditem.append(query_string.to_xml(version=self.account.version))
        return finditem
