from .common import EWSAccountService
from ..util import create_element, set_xml_value


class CreateUserConfiguration(EWSAccountService):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/createuserconfiguration-operation
    """

    SERVICE_NAME = 'CreateUserConfiguration'
    returns_elements = False

    def call(self, user_configuration):
        return self._get_elements(payload=self.get_payload(user_configuration=user_configuration))

    def get_payload(self, user_configuration):
        createuserconfiguration = create_element('m:%s' % self.SERVICE_NAME)
        set_xml_value(createuserconfiguration, user_configuration, version=self.protocol.version)
        return createuserconfiguration
