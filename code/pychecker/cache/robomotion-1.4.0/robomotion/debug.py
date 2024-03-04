from enum import Enum
import grpc
from json import dumps, loads
import os
from robomotion.utils import File
from robomotion import plugin_pb2
from robomotion import plugin_pb2_grpc


class AttachConfig:
    def __init__(self, protocol: str, addr: str, pid: int, namespace: str):
        self.protocol = protocol
        self.addr = addr
        self.pid = pid
        self.namespace = namespace


class EProtocol(Enum):
    ProtocolInvalid = ''
    ProtocolNetRPC = 'netrpc'
    ProtocolGRPC = 'grpc'


class Debug:
    @staticmethod
    def attach(g_addr: str, ns: str):
        cfg = AttachConfig(str(EProtocol.ProtocolGRPC.value), g_addr, os.getpid(), ns)
        cfg_data = dumps(cfg.__dict__)
        addr = Debug.get_rpc_addr()
        if addr == '':
            print('runner RPC address is None')
            exit(0)

        channel = grpc.insecure_channel(addr)
        client = plugin_pb2_grpc.DebugStub(channel)

        request = plugin_pb2.AttachRequest(config=cfg_data.encode())
        client.Attach(request)
        channel.close()

    @staticmethod
    def detach(ns: str):
        addr = Debug.get_rpc_addr()
        if addr == '':
            print('runner RPC address is None')
            exit(0)

        channel = grpc.insecure_channel(addr)
        client = plugin_pb2_grpc.DebugStub(channel)

        request = plugin_pb2.DetachRequest(namespace=ns)
        client.Detach(request)
        channel.close()

    @staticmethod
    def get_rpc_addr() -> str:
        dir = File.temp_dir()
        path = os.path.join(dir, 'runcfg.json')

        f = open(path, 'r')
        data = f.read()
        obj = loads(data)
        return str(obj['listen']).replace('[::]', '127.0.0.1')
