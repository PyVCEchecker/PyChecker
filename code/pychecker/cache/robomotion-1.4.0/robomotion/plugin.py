from concurrent import futures
import grpc
import asyncio
import sys, inspect

from robomotion import health_pb2
from robomotion import health_pb2_grpc
from robomotion import plugin_pb2_grpc
from robomotion import health

from robomotion.factory import NodeFactory
from robomotion.node import NodeServicer, Node
from robomotion.runtime import Runtime
from robomotion.spec import Spec
from robomotion.debug import Debug


async def start():

    if len(sys.argv) > 3 and sys.argv[1] == '-s':
        Spec.generate(sys.argv[2], sys.argv[3])
        return

    init()

    healthServicer = health.HealthServicer()
    healthServicer.set_status("plugin", 1)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    health_pb2_grpc.add_HealthServicer_to_server(healthServicer, server)
    plugin_pb2_grpc.add_NodeServicer_to_server(NodeServicer(), server)

    port = server.add_insecure_port('[::]:0')
    server.start()

    print("1|1|tcp|127.0.0.1:%d|grpc\n" % port, flush=True)

    ns = ''
    if len(sys.argv) > 2 and sys.argv[1] == '-a':
        ns = sys.argv[2]
        Debug.attach('127.0.0.1:%d'%port, ns)

    Runtime.event.wait()

    if ns != '':
        Debug.detach(ns)


def init():
    frm = inspect.stack()[2]
    mod = inspect.getmodule(frm[0])
    clsmembers = inspect.getmembers(sys.modules[mod.__name__], inspect.isclass)
    for c in clsmembers:
        if issubclass(c[1], Node) and c[1] is not Node:
            cls = c[1]
            name = cls().name
            factory = NodeFactory(cls().cls)
            Runtime.create_node(name, factory)
