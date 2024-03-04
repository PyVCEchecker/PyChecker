from .common import EWSAccountService, to_item_id
from ..properties import PersonaId
from ..util import create_element, set_xml_value, MNS


class GetPersona(EWSAccountService):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/getpersona-operation"""

    SERVICE_NAME = 'GetPersona'

    def call(self, persona):
        return self._elems_to_objs(self._get_elements(payload=self.get_payload(persona=persona)))

    def _elems_to_objs(self, elems):
        from ..items import Persona
        elements = list(elems)
        if len(elements) != 1:
            raise ValueError('Expected exactly one element in response')
        elem = elements[0]
        if isinstance(elem, Exception):
            raise elem
        return Persona.from_xml(elem=elem, account=None)

    def get_payload(self, persona):
        version = self.protocol.version
        payload = create_element('m:%s' % self.SERVICE_NAME)
        set_xml_value(payload, to_item_id(persona, PersonaId, version=version), version=version)
        return payload

    @classmethod
    def _get_elements_in_container(cls, container):
        from ..items import Persona
        return container.findall('{%s}%s' % (MNS, Persona.ELEMENT_NAME))

    @classmethod
    def _response_tag(cls):
        return '{%s}%sResponseMessage' % (MNS, cls.SERVICE_NAME)
