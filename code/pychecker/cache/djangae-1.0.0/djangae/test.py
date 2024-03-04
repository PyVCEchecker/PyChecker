import contextlib
import logging
import os

from django import test
from django.http import Http404
from django.test import Client, RequestFactory
from django.test.runner import DiscoverRunner
from djangae.test_runner import bed_wrap

from djangae.environment import get_application_root

from django.conf.urls import handler404, handler500
from django.utils.module_loading import import_string

from google.appengine.api import apiproxy_stub_map, appinfo
from google.appengine.datastore import datastore_stub_util
from google.appengine.tools.devappserver2.application_configuration import ModuleConfiguration
from google.appengine.tools.devappserver2.module import _ScriptHandler


@contextlib.contextmanager
def inconsistent_db(probability=0, connection='default'):
    """
        A context manager that allows you to make the datastore inconsistent during testing.
        This is vital for writing applications that deal with the Datastore's eventual consistency
    """

    stub = apiproxy_stub_map.apiproxy.GetStub('datastore_v3')

    # Set the probability of the datastore stub
    original_policy = stub._consistency_policy
    stub.SetConsistencyPolicy(datastore_stub_util.PseudoRandomHRConsistencyPolicy(probability=probability))
    try:
        yield
    finally:
        # Restore to consistent mode
        stub.SetConsistencyPolicy(original_policy)


def _get_queued_tasks(stub, queue_name=None, flush=True, process_pull_tasks=True):
    tasks = []
    queues = stub.GetQueues()

    if queue_name is not None:
        queues = filter(lambda q: queue_name == q['name'], queues)

    for queue in queues:
        if not process_pull_tasks and queue.get('mode') == 'pull':
            continue

        for task in stub.GetTasks(queue['name']):
            tasks.append(task)

        if flush:
            stub.FlushQueue(queue["name"])

    return tasks

def _flush_tasks(stub, queue_name=None):
    if queue_name:
        stub.FlushQueue(queue_name)
    else:
        for queue in stub.GetQueues():
            stub.FlushQueue(queue["name"])


@contextlib.contextmanager
def environ_override(**kwargs):
    original = os.environ.copy()
    os.environ.update(kwargs)

    yield

    # Delete any keys that were introduced in kwargs
    for key in kwargs:
        if key not in original:
            del os.environ[key]

    # Restore original values
    os.environ.update(original)


class TaskFailedBehaviour:
    DO_NOTHING = 0
    RETRY_TASK = 1
    RAISE_ERROR = 2


class TaskFailedError(Exception):
    def __init__(self, task_name, status_code, original_exception=None):
        self.task_name = task_name
        self.status_code = status_code
        self.original_exception = original_exception

        super(TaskFailedError, self).__init__(
            "Task {} failed with status code: {}. \n\nMessage was: {}".format(
                task_name, status_code, original_exception
            )
        )


def process_task_queues(queue_name=None, failure_behaviour=TaskFailedBehaviour.RAISE_ERROR):
    """
        Processes any queued tasks inline without a server.
        This is useful for end-to-end testing background tasks.

        failure_behaviour: This controls the behaviour of the task processing in the case
        that the task returns a status_code other than 2xx. Options are:

        1. Do nothing (a message will be logged at INFO level though)
        2. Retry the task (WARNING! This will result in an infinite loop if the task fails forever)
        3. Throw a TaskFailedError
    """

    stub = apiproxy_stub_map.apiproxy.GetStub("taskqueue")

    tasks = _get_queued_tasks(stub, queue_name, process_pull_tasks=False)

    client = Client() # Instantiate a test client for processing the tasks

    while tasks:
        task = tasks.pop(0) # Get the first task

        decoded_body = task['body'].decode('base64')
        post_data = decoded_body
        headers = { "HTTP_{}".format(x.replace("-", "_").upper()): y for x, y in task['headers'] }

        method = task['method']

        # AppEngine sets the task headers in the environment, so we should do the same
        with environ_override(**headers):
            try:
                # The Django test client (which we use to call the task URL) doesn't handle
                # errors in the same way as traditional Django would; it lets exceptions propagate.
                # What we do here is wrap the client call in a try/except and then call either
                # handler404 or handler500 to get the appropriate response. We then pass any
                # original exception to TaskFailedError if the failure_behaviour is RAISE_ERROR

                original_exception = None
                factory = RequestFactory()

                if method.upper() == "POST":
                    request_kwargs = {
                        "path": task['url'],
                        "data": post_data,
                        "content_type": headers['HTTP_CONTENT_TYPE']
                    }
                    request_kwargs.update(headers)

                    #Fixme: post data?
                    request = factory.post(**request_kwargs)
                    response = client.post(**request_kwargs)
                else:
                    request_kwargs = {
                        "path": task['url']
                    }
                    request_kwargs.update(headers)

                    request = factory.get(**request_kwargs)
                    response = client.get(**request_kwargs)
            except Http404 as e:
                original_exception = e
                handler = import_string(handler404)
                response = handler(request, e)
            except Exception as e:
                original_exception = e
                handler = import_string(handler500)
                response = handler(request)

        if not str(response.status_code).startswith("2"):
            # If the response wasn't a 2xx return code, then handle as required

            if failure_behaviour == TaskFailedBehaviour.DO_NOTHING:
                # Log a message if the task fails
                logging.info("Unexpected status (%r) while simulating task with url: %r", response.status_code, task['url'])
            elif failure_behaviour == TaskFailedBehaviour.RETRY_TASK:
                # Add the task to the end of the task queue
                tasks.append(task)
            else:
                raise TaskFailedError(
                    headers['HTTP_X_APPENGINE_TASKNAME'],
                    response.status_code,
                    original_exception
                )

        if not tasks:
            #The map reduce may have added more tasks, so refresh the list
            tasks = _get_queued_tasks(stub, queue_name, process_pull_tasks=False)


def get_task_count(queue_name=None):
    stub = apiproxy_stub_map.apiproxy.GetStub("taskqueue")
    return len(_get_queued_tasks(stub, queue_name, flush=False))


class TestCaseMixin(object):
    def setUp(self):
        super(TestCaseMixin, self).setUp()
        self.taskqueue_stub = apiproxy_stub_map.apiproxy.GetStub("taskqueue")
        # Make sure we clear the queue before every test
        self.flush_task_queues()

    def assertNumTasksEquals(self, num, queue_name='default'):
        self.assertEqual(num, len(_get_queued_tasks(self.taskqueue_stub, queue_name, flush=False)))

    def flush_task_queues(self, queue_name=None):
        if self.taskqueue_stub:
            _flush_tasks(self.taskqueue_stub, queue_name)

    def process_task_queues(self, queue_name=None, failure_behaviour=TaskFailedBehaviour.RAISE_ERROR):
        process_task_queues(queue_name, failure_behaviour)

    def get_task_count(self, queue_name=None):
        return get_task_count(queue_name)


class HandlerAssertionsMixin(object):
    """
    Custom assert methods which verifies a range of handler configuration
    setting specified in app.yaml.
    """

    msg_prefix = 'Handler configuration for {url} is not protected by {perm}.'

    def assert_login_admin(self, url):
        """
        Test that the handler defined in app.yaml which matches the url provided
        has `login: admin` in the configuration.
        """
        handler = self._match_handler(url)
        self.assertEqual(
            handler.url_map.login, appinfo.LOGIN_ADMIN, self.msg_prefix.format(
                url=url, perm='`login: admin`'
            )
        )

    def assert_login_required(self, url):
        """
        Test that the handler defined in app.yaml which matches the url provided
        has `login: required` or `login: admin` in the configruation.
        """
        handler = self._match_handler(url)
        login_admin = handler.url_map.login == appinfo.LOGIN_ADMIN
        login_required = handler.url_map.login == appinfo.LOGIN_REQUIRED or login_admin

        self.assertTrue(login_required, self.msg_prefix.format(
                url=url, perm='`login: admin` or `login: required`'
            )
        )

    def _match_handler(self, url):
        """
        Load script handler configurations from app.yaml and try to match
        the provided url path to a url_maps regex.
        """
        app_yaml_path = os.path.join(get_application_root(), "app.yaml")
        config = ModuleConfiguration(app_yaml_path)

        url_maps = config.handlers
        script_handlers = [
            _ScriptHandler(maps) for
            maps in url_maps if
            maps.GetHandlerType() == appinfo.HANDLER_SCRIPT
        ]

        for handler in script_handlers:
            if handler.match(url):
                return handler

        raise AssertionError('No handler found for {url}'.format(url=url))


class TestCase(HandlerAssertionsMixin, TestCaseMixin, test.TestCase):
    pass


class TransactionTestCase(HandlerAssertionsMixin, TestCaseMixin, test.TransactionTestCase):
    pass


class DjangaeDiscoverRunner(DiscoverRunner):
    def build_suite(self, *args, **kwargs):
        suite = super(DjangaeDiscoverRunner, self).build_suite(*args, **kwargs)
        suite._tests[:] = [bed_wrap(test) for test in suite._tests]
        return suite
