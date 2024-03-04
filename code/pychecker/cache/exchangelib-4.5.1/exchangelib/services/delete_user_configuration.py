from .common import EWSAccountService
from ..util import create_element, set_xml_value


class DeleteUserConfiguration(EWSAccountService):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/deleteuserconfiguration-operation
    """

    SERVICE_NAME = 'DeleteUserConfiguration'
    returns_elements = False

    def call(self, user_configuration_name):
        return self._get_elements(payload=self.get_payload(user_configuration_name=user_configuration_name))

    def get_payload(self, user_configuration_name):
        deleteuserconfiguration = create_element('m:%s' % self.SERVICE_NAME)
        set_xml_value(deleteuserconfiguration, user_configuration_name, version=self.account.version)
        return deleteuserconfiguration
