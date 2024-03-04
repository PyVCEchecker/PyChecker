import grpc
import gzip
import json
import enum
import threading
from google.protobuf import json_format
from robomotion import plugin_pb2
from robomotion.plugin_pb2_grpc import RuntimeHelperStub
from robomotion.struct_pb2 import Struct
from robomotion.message import Context

from types import SimpleNamespace as Namespace


class Runtime:
    active_nodes = 0
    client: RuntimeHelperStub = None
    event: threading.Event = threading.Event()
    factories = {}
    nodes = {}

    @staticmethod
    def set_client(client: RuntimeHelperStub):
        Runtime.client = client

    @staticmethod
    def check_runner_conn(connection: grpc.Channel):
        def cb(state: grpc.ChannelConnectivity):
            if state == grpc.TRANSIENT_FAILURE or state == grpc.SHUTDOWN:
                Runtime.event.set()

        connection.subscribe(cb, True)

    @staticmethod
    def create_node(name: str, factory):
        Runtime.factories[name] = factory

    @staticmethod
    def add_node(guid: str, node):
        Runtime.nodes[guid] = node

    @staticmethod
    def compress(data: bytes):
        return gzip.compress(data)

    @staticmethod
    def decompress(data: bytes):
        return gzip.decompress(data)

    @staticmethod
    def deserialize(data: bytes, c):
        node = c()
        obj = json.loads(data)
        for key in obj.keys():
            if key in node.__dict__.keys():
                if type(obj[key]) is dict:
                    node.__dict__[key] = type(node.__dict__[key])(**obj[key])
                else:
                    node.__dict__[key] = obj[key]

        return node

    @staticmethod
    def close():
        if Runtime.client is None:
            return

        request = plugin_pb2.Empty()
        Runtime.client.Close(request)

    @staticmethod
    def get_variable(variable, ctx: Context):
        scope = variable.scope
        name = variable.name

        if scope == 'Custom':
            return name

        if scope == 'Message':
            msg = json.loads(ctx.get_raw().decode('utf-8'))
            if name in msg:
                return msg[name]
            else:
                return None

        if Runtime.client is None:
            return None

        var = plugin_pb2.Variable(scope=scope, name=name)
        request = plugin_pb2.GetVariableRequest(variable=var)
        response = Runtime.client.GetVariable(request)

        return json_format.MessageToDict(response.value)['value']

    @staticmethod
    def set_variable(variable, ctx: Context, value: object):
        scope = variable.scope
        name = variable.name

        if scope == 'Message':
            ctx.set(name, value)
            return

        if Runtime.client is None:
            return

        val = Struct()
        val.update({'value': value})

        var = plugin_pb2.Variable(scope=scope, name=name)
        request = plugin_pb2.SetVariableRequest(variable=var, value=val)
        Runtime.client.SetVariable(request)

    @staticmethod
    def get_vault_item(cred):
        if Runtime.client is None:
            return {}

        request = plugin_pb2.GetVaultItemRequest(vaultId=cred.vaultId, ItemId=cred.itemId)
        response = Runtime.client.GetVaultItem(request)
        return json_format.MessageToDict(response.item)['value']
		
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
