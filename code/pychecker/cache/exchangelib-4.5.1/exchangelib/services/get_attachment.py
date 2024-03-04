from itertools import chain

from .common import EWSAccountService, create_attachment_ids_element
from ..util import create_element, add_xml_child, set_xml_value, DummyResponse, StreamingBase64Parser,\
    StreamingContentHandler, ElementNotFound, MNS

# https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/bodytype
BODY_TYPE_CHOICES = ('Best', 'HTML', 'Text')


class GetAttachment(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/getattachment-operation"""

    SERVICE_NAME = 'GetAttachment'
    element_container_name = '{%s}Attachments' % MNS

    def call(self, items, include_mime_content, body_type, filter_html_content, additional_fields):
        if body_type and body_type not in BODY_TYPE_CHOICES:
            raise ValueError("'body_type' %s must be one of %s" % (body_type, BODY_TYPE_CHOICES))
        return self._elems_to_objs(self._chunked_get_elements(
            self.get_payload, items=items, include_mime_content=include_mime_content,
            body_type=body_type, filter_html_content=filter_html_content, additional_fields=additional_fields,
        ))

    def _elems_to_objs(self, elems):
        from ..attachments import FileAttachment, ItemAttachment
        cls_map = {cls.response_tag(): cls for cls in (FileAttachment, ItemAttachment)}
        for elem in elems:
            if isinstance(elem, Exception):
                yield elem
                continue
            yield cls_map[elem.tag].from_xml(elem=elem, account=self.account)

    def get_payload(self, items, include_mime_content, body_type, filter_html_content, additional_fields):
        payload = create_element('m:%s' % self.SERVICE_NAME)
        shape_elem = create_element('m:AttachmentShape')
        if include_mime_content:
            add_xml_child(shape_elem, 't:IncludeMimeContent', 'true')
        if body_type:
            add_xml_child(shape_elem, 't:BodyType', body_type)
        if filter_html_content is not None:
            add_xml_child(shape_elem, 't:FilterHtmlContent', 'true' if filter_html_content else 'false')
        if additional_fields:
            additional_properties = create_element('t:AdditionalProperties')
            expanded_fields = chain(*(f.expand(version=self.account.version) for f in additional_fields))
            set_xml_value(additional_properties, sorted(
                expanded_fields,
                key=lambda f: (getattr(f.field, 'field_uri', ''), f.path)
            ), version=self.account.version)
            shape_elem.append(additional_properties)
        if len(shape_elem):
            payload.append(shape_elem)
        attachment_ids = create_attachment_ids_element(items=items, version=self.account.version)
        payload.append(attachment_ids)
        return payload

    def _update_api_version(self, api_version, header, **parse_opts):
        if not parse_opts.get('stream_file_content', False):
            super()._update_api_version(api_version, header, **parse_opts)
        # TODO: We're skipping this part in streaming mode because StreamingBase64Parser cannot parse the SOAP header

    @classmethod
    def _get_soap_parts(cls, response, **parse_opts):
        if not parse_opts.get('stream_file_content', False):
            return super()._get_soap_parts(response, **parse_opts)

        # Pass the response unaltered. We want to use our custom streaming parser
        return None, response

    def _get_soap_messages(self, body, **parse_opts):
        if not parse_opts.get('stream_file_content', False):
            return super()._get_soap_messages(body, **parse_opts)

        from ..attachments import FileAttachment
        # 'body' is actually the raw response passed on by '_get_soap_parts'
        r = body
        parser = StreamingBase64Parser()
        field = FileAttachment.get_field_by_fieldname('_content')
        handler = StreamingContentHandler(parser=parser, ns=field.namespace, element_name=field.field_uri)
        parser.setContentHandler(handler)
        return parser.parse(r)

    def stream_file_content(self, attachment_id):
        # The streaming XML parser can only stream content of one attachment
        payload = self.get_payload(
            items=[attachment_id], include_mime_content=False, body_type=None, filter_html_content=None,
            additional_fields=None,
        )
        self.streaming = True
        try:
            yield from self._get_response_xml(payload=payload, stream_file_content=True)
        except ElementNotFound as enf:
            # When the returned XML does not contain a Content element, ElementNotFound is thrown by parser.parse().
            # Let the non-streaming SOAP parser parse the response and hook into the normal exception handling.
            # Wrap in DummyResponse because _get_soap_parts() expects an iter_content() method.
            response = DummyResponse(url=None, headers=None, request_headers=None, content=enf.data)
            _, body = super()._get_soap_parts(response=response)
            res = super()._get_soap_messages(body=body)
            for e in self._get_elements_in_response(response=res):
                if isinstance(e, Exception):
                    raise e
            # The returned content did not contain any EWS exceptions. Give up and re-raise the original exception.
            raise enf
        finally:
            self.streaming = False
            self.stop_streaming()
