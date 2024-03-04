from robomotion.runtime import Runtime
from robomotion import plugin_pb2
from google.protobuf import json_format
from robomotion.struct_pb2 import Struct
from robomotion.message import Context
import json
from enum import IntEnum


class _DefVal:
    def __init__(self, default: object):
        self.default = default

    def __init__(self, scope: str, name: str):
        self.default = {scope: scope, name: name}


class _Enum:
    def __init__(self, enums: [], enumNames: []):
        self.__enums = enums
        self.__enumNames = enumNames

    @property
    def enums(self):
        return self.__enums

    @property
    def enumNames(self):
        return self.__enumNames


class Variable:
    def __init__(self, scope: str='', name: str='', title: str='', type: str='', pyScope: bool=False, customScope: bool=False,
                 messageScope: bool=False, messageOnly: bool=False, hidden: bool=False, input: bool=False, output: bool=False,
                 option: bool=False, default: _DefVal=None, enum: _Enum=None):

        self.__scope = scope
        self.__name = name
        self.__title = title
        self.__type = type
        self.__pyScope = pyScope
        self.__customScope = customScope
        self.__messageScope = messageScope
        self.__messageOnly = messageOnly
        self.__hidden = hidden
        self.__isinput = input
        self.__isoutput = output
        self.__isoption = option
        self.__default = default
        self.__enum = enum

    @property
    def scope(self) -> str:
        return self.__scope

    @property
    def name(self) -> str:
        return self.__name

    @property
    def title(self) -> str:
        return self.__title

    @property
    def type(self) -> str:
        return self.__type

    @property
    def pyScope(self) -> bool:
        return self.__pyScope

    @property
    def customScope(self) -> bool:
        return self.__customScope

    @property
    def messageScope(self) -> bool:
        return self.__messageScope

    @property
    def messageOnly(self) -> bool:
        return self.__messageOnly

    @property
    def hidden(self) -> bool:
        return self.__hidden

    @property
    def __input(self) -> bool:
        return self.__isinput

    @property
    def output(self) -> bool:
        return self.__isoutput

    @property
    def option(self) -> bool:
        return self.__isoption

    @property
    def default(self) -> _DefVal:
        return self.__default

    @property
    def enum(self) -> _Enum:
        return self.__enum


class InVariable(Variable):
    def get(self, ctx: Context):
        return Runtime.get_variable(self, ctx)


class OutVariable(Variable):
    def set(self, ctx: Context, value: object):
        Runtime.set_variable(self, ctx, value)


class OptVariable(Variable):
    def get(self, ctx: Context):
        return Runtime.get_variable(self, ctx)


class ECategory(IntEnum):
    Null = 0,
    Login = 1
    Email = 2
    CreditCard = 3
    Token = 4
    Database = 5
    Document = 6


class Credentials:
    def __init__(self, vaultId: str='', itemId: str='', title: str='', category: ECategory=ECategory.Null):
        self.__vaultId = vaultId
        self.__itemId = itemId
        self.__title = title
        self.__category = category

    @property
    def vaultId(self) -> str:
        return self.__vaultId

    @property
    def itemId(self) -> str:
        return self.__itemId

    @property
    def title(self) -> str:
        return self.__title

    @property
    def category(self) -> ECategory:
        return self.__category

    def get_vault_item(self):
        if Runtime.client is None:
            return {}

        request = plugin_pb2.GetVaultItemRequest(vaultId=self.vaultId, ItemId=self.itemId)
        response = Runtime.client.GetVaultItem(request)
        return json_format.MessageToDict(response.item)['value']
