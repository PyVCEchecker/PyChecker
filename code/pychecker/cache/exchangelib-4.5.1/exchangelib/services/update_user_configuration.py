from .common import EWSAccountService
from ..util import create_element, set_xml_value


class UpdateUserConfiguration(EWSAccountService):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/updateuserconfiguration-operation
    """

    SERVICE_NAME = 'UpdateUserConfiguration'
    returns_elements = False

    def call(self, user_configuration):
        return self._get_elements(payload=self.get_payload(user_configuration=user_configuration))

    def get_payload(self, user_configuration):
        updateuserconfiguration = create_element('m:%s' % self.SERVICE_NAME)
        set_xml_value(updateuserconfiguration, user_configuration, version=self.account.version)
        return updateuserconfiguration
