import threading
from robomotion import health_pb2
from robomotion import health_pb2_grpc


class HealthServicer(health_pb2_grpc.HealthServicer):
    def __init__(self):
        self.lock = threading.Lock()
        self.status_map = {}

    def clear_all(self):
        self.lock.acquire()
        self.status_map.clear()
        self.lock.release()

    def clear_status(self, service):
        self.lock.acquire()
        del self.status_map[service]
        self.lock.release()

    def set_status(self, service, status):
        self.lock.acquire()
        self.status_map[service] = status
        self.lock.release()

    def Check(self, request, context):
        service = request.service
        status = self.status_map[service]
        return health_pb2.HealthCheckResponse(status=status)
