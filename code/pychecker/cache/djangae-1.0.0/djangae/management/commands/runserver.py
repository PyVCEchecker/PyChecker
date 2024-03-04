import os
import re
import logging

from datetime import datetime

from django.conf import settings
from django.core.management.commands import runserver

from djangae import (
    sandbox,
    VERSION as DJANGAE_VERSION
)

from google.appengine.tools.devappserver2 import shutdown
from google.appengine.tools.sdk_update_checker import (
    GetVersionObject,
    _VersionList
)


DJANGAE_RUNSERVER_IGNORED_FILES_REGEXES = getattr(settings, "DJANGAE_RUNSERVER_IGNORED_FILES_REGEXES", [])
DJANGAE_RUNSERVER_IGNORED_DIR_REGEXES = getattr(settings, "DJANGAE_RUNSERVER_IGNORED_DIR_REGEXES", [])
if DJANGAE_RUNSERVER_IGNORED_FILES_REGEXES:
    DJANGAE_RUNSERVER_IGNORED_FILES_REGEXES = [re.compile(regex) for regex in DJANGAE_RUNSERVER_IGNORED_FILES_REGEXES]
if DJANGAE_RUNSERVER_IGNORED_DIR_REGEXES:
    DJANGAE_RUNSERVER_IGNORED_DIR_REGEXES = [re.compile(regex) for regex in DJANGAE_RUNSERVER_IGNORED_DIR_REGEXES]


def ignore_file(filename, *args, **kwargs):
    """ Replacement for devappserver2.watchter_common.ignore_file
        - to be monkeypatched into place.
    """
    from google.appengine.tools.devappserver2 import watcher_common
    filename = os.path.basename(filename)
    return(
        filename.startswith(watcher_common._IGNORED_PREFIX) or
        any(filename.endswith(suffix) for suffix in watcher_common._IGNORED_FILE_SUFFIXES) or
        watcher_common._IGNORED_REGEX.match(filename) or
        any(regex.match(filename) for regex in DJANGAE_RUNSERVER_IGNORED_FILES_REGEXES)
    )


def skip_ignored_dirs(*args, **kwargs):
    """ Replacement for devappserver2.watchter_common.skip_ignored_dirs
    - to be monkeypatched into place.
    """
    # Note that this function modifies the `dirs` list in place, it doesn't return anything.
    # Also note that `dirs` is a list of dir *names* not dir *paths*, which means that we can't
    # differentiate between /foo/bar and /moo/bar because we just get 'bar'. But allowing that
    # would require a whole load more monkey patching.
    from djangae import sandbox
    from google.appengine.tools.devappserver2 import watcher_common

    # since version 1.9.49 (which is incorrectly marked as [0, 0, 0] for now, until
    # https://code.google.com/p/googleappengine/issues/detail?id=13439 will be fixed,
    # skip_ignored_dirs have three arguments instead of one. To preserve
    # backwards compatibilty we check version here and use args to fetch one
    # or three arguments depending on version. We do not do any further error handling
    # here to make sure that this explicitly fail if there is another change in
    # the number of arguments with new SDK versions.
    current_version = _VersionList(GetVersionObject()['release'])
    if current_version == sandbox.TEMP_1_9_49_VERSION_NO:
        current_version = _VersionList('1.9.49')

    if current_version >= _VersionList('1.9.49'):
        dirpath, dirs, skip_files_re = args
    else:
        dirs = args[0]
    watcher_common._remove_pred(dirs, lambda d: d.startswith(watcher_common._IGNORED_PREFIX))
    watcher_common._remove_pred(
        dirs,
        lambda d: any(regex.search(d) for regex in DJANGAE_RUNSERVER_IGNORED_DIR_REGEXES)
    )


class Command(runserver.Command):
    """
    Overrides the default Django runserver command.

    Instead of starting the default Django development server this
    command fires up a copy of the full fledged App Engine
    dev_appserver that emulates the live environment your application
    will be deployed to.
    """
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.sandbox_options = sorted([option for option in dir(sandbox._OPTIONS) if not option.startswith('_')])

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

        parser.description = 'Starts Appengine SDK\'s dev_appserver.py for development and also serves static files.'
        parser.usage = '%(prog)s [options]'

        # Extra parameters that we're going to pass to GAE's `dev_appserver.py`.
        group = parser.add_argument_group('dev_appserver.py options')
        for option in self.sandbox_options:
            group.add_argument('--%s' % option, action='store', dest=option)

    def handle(self, addrport='', *args, **options):
        self.gae_options = {}

        # this way we populate the dictionary with the options that relevant
        # just for `dev_appserver.py`
        for option, value in options.items():
            if option in self.sandbox_options and value is not None:
                self.gae_options[option] = value

        super(Command, self).handle(addrport=addrport, *args, **options)

    def run(self, *args, **options):
        if self.addr:
            self.gae_options['host'] = self.addr

        if self.port:
            self.gae_options['port'] = int(self.port)

        # These options are Django options which need to have corresponding args
        # passed down to the dev_appserver
        self.use_reloader = options.get("use_reloader")
        self.use_threading = options.get("use_threading")

        # We force the option to false here because we use the dev_appserver reload
        # capabilities, not Django's reloading
        options["use_reloader"] = False
        return super(Command, self).run(*args, **options)

    def inner_run(self, *args, **options):
        import sys

        shutdown_message = options.get('shutdown_message', '')

        quit_command = 'CTRL-BREAK' if sys.platform == 'win32' else 'CONTROL-C'

        from djangae.environment import get_application_root
        from djangae.sandbox import _find_sdk_from_python_path
        from djangae.blobstore_service import stop_blobstore_service

        from django.conf import settings
        from django.utils import translation

        stop_blobstore_service()

        # Check for app.yaml
        expected_path = os.path.join(get_application_root(), "app.yaml")
        if not os.path.exists(expected_path):
            sys.stderr.write("Unable to find app.yaml at '%s'\n" % expected_path)
            sys.exit(1)

        self.stdout.write("Validating models...\n\n")
        self.check(display_num_errors=True)
        self.stdout.write((
            "%(started_at)s\n"
            "Djangae version %(djangae_version)s\n"
            "Django version %(django_version)s, using settings %(settings)r\n"
            "Starting development server at http://%(addr)s:%(port)s/\n"
            "Quit the server with %(quit_command)s.\n"
        ) % {
            "started_at": datetime.now().strftime('%B %d, %Y - %X'),
            "django_version": self.get_version(),
            "settings": settings.SETTINGS_MODULE,
            "addr": self._raw_ipv6 and '[%s]' % self.addr or self.addr,
            "port": self.port,
            "quit_command": quit_command,
            "djangae_version": DJANGAE_VERSION
        })
        sys.stdout.write("\n")
        sys.stdout.flush()

        # django.core.management.base forces the locale to en-us. We should
        # set it up correctly for the first request (particularly important
        # in the "--noreload" case).
        translation.activate(settings.LANGUAGE_CODE)

        # Will have been set by setup_paths
        sdk_path = _find_sdk_from_python_path()

        from google.appengine.tools.devappserver2 import devappserver2
        from google.appengine.tools.devappserver2 import python_runtime

        from djangae import sandbox

        # Add any additional modules specified in the settings
        additional_modules = getattr(settings, "DJANGAE_ADDITIONAL_MODULES", [])
        if additional_modules:
            sandbox._OPTIONS.config_paths.extend(additional_modules)

        if self.addr != sandbox._OPTIONS.host:
            sandbox._OPTIONS.host = sandbox._OPTIONS.admin_host = sandbox._OPTIONS.api_host = self.addr

        # Extra options for `dev_appserver.py`
        for param, value in self.gae_options.items():
            setattr(sandbox._OPTIONS, param, value)

        # External port is a new flag introduced in 1.9.19
        current_version = _VersionList(GetVersionObject()['release'])
        if current_version >= _VersionList('1.9.19') or \
                current_version == sandbox.TEMP_1_9_49_VERSION_NO:
            sandbox._OPTIONS.external_port = None

        # Apply equivalent options for Django args
        sandbox._OPTIONS.automatic_restart = self.use_reloader
        sandbox._OPTIONS.threadsafe_override = self.use_threading

        if sandbox._OPTIONS.host == "127.0.0.1" and os.environ["HTTP_HOST"].startswith("localhost"):
            hostname = "localhost"
            sandbox._OPTIONS.host = "localhost"
        else:
            hostname = sandbox._OPTIONS.host

        os.environ["HTTP_HOST"] = "%s:%s" % (hostname, sandbox._OPTIONS.port)
        os.environ['SERVER_NAME'] = os.environ['HTTP_HOST'].split(':', 1)[0]
        os.environ['SERVER_PORT'] = os.environ['HTTP_HOST'].split(':', 1)[1]
        os.environ['DEFAULT_VERSION_HOSTNAME'] = '%s:%s' % (os.environ['SERVER_NAME'], os.environ['SERVER_PORT'])

        from google.appengine.api.appinfo import EnvironmentVariables

        class NoConfigDevServer(devappserver2.DevelopmentServer):
            """
                This is horrible, but unfortunately necessary.

                Because we want to enable a sandbox outside of runserver (both when
                running different management commands, but also before/after dev_appserver)
                we have to make sure the following are true:

                1. There is only ever one api server
                2. There is only ever one dispatcher

                Unfortunately, most of the setup is done inside .start() of the DevelopmentServer
                class, there is not really an easy way to hook into part of this without overriding the
                whole .start() method which makes things even more brittle.

                What we do here is hook in at the point that self._dispatcher is set. We ignore whatever
                dispatcher is passed in, but user our own one. We patch api server creation in sandbox.py
                so only ever one api server exists.
            """
            def __init__(self, *args, **kwargs):
                self._patched_dispatcher = None
                super(NoConfigDevServer, self).__init__(*args, **kwargs)

            def start(self, options):
                self.options = options
                return super(NoConfigDevServer, self).start(options)

            def _get_dispatcher(self):
                return self._patched_dispatcher

            def _create_api_server(self, *args, **kwargs):
                """
                    For SDK around 1.9.40 - just return the existing API server
                """
                return sandbox._API_SERVER

            def _set_dispatcher(self, dispatcher):
                """
                    Ignore explicit setting of _dispatcher, use our own
                """

                if dispatcher is None:
                    # Allow wiping the patched dispatcher
                    self._patched_dispatcher = None
                    return

                if self._patched_dispatcher:
                    # We already created the dispatcher, ignore further sets
                    logging.warning("Attempted to set _dispatcher twice")
                    return


                # When the dispatcher is created this property is set so we use it
                # to construct *our* dispatcher
                configuration = dispatcher._configuration

                # We store options in .start() so it's available here
                options = self.options

                # sandbox._create_dispatcher returns a singleton dispatcher instance made in sandbox
                self._patched_dispatcher = sandbox._create_dispatcher(
                    configuration,
                    options
                )

                # the dispatcher may have passed environment variables, it should be propagated
                env_vars = self._dispatcher._configuration.modules[0]._app_info_external.env_variables or EnvironmentVariables()
                for module in configuration.modules:
                    module_name = module._module_name
                    if module_name == 'default' or module_name is None:
                        module_settings = 'DJANGO_SETTINGS_MODULE'
                    else:
                        module_settings = '%s_DJANGO_SETTINGS_MODULE' % module_name
                    if module_settings in env_vars:
                        module_env_vars = module.env_variables or EnvironmentVariables()
                        module_env_vars['DJANGO_SETTINGS_MODULE'] = env_vars[module_settings]

                        old_env_vars = module._app_info_external.env_variables
                        new_env_vars = EnvironmentVariables.Merge(module_env_vars, old_env_vars)
                        module._app_info_external.env_variables = new_env_vars
                self._dispatcher._configuration = configuration
                self._dispatcher._port = options.port
                self._dispatcher._host = options.host

                # Because the dispatcher is a singleton, we need to set the threadsafe override here
                # depending on what was passed to the runserver command. This entire file really needs rebuilding
                # we have way too many hacks in here!
                self._dispatcher._module_to_threadsafe_override[
                    configuration.modules[0].module_name
                ] = options.threadsafe_override

#                self._dispatcher.request_data = request_data
#                request_data._dispatcher = self._dispatcher

                sandbox._API_SERVER._host = options.api_host
                sandbox._API_SERVER.bind_addr = (options.api_host, options.api_port)

                from google.appengine.api import apiproxy_stub_map
                task_queue = apiproxy_stub_map.apiproxy.GetStub('taskqueue')
                # Make sure task running is enabled (it's disabled in the sandbox by default)
                if not task_queue._auto_task_running:
                    task_queue._auto_task_running = True
                    task_queue.StartBackgroundExecution()

            _dispatcher = property(fget=_get_dispatcher, fset=_set_dispatcher)

        from google.appengine.tools.devappserver2 import module

        def fix_watcher_files(regex):
            """ Monkeypatch dev_appserver's file watcher to ignore any unwanted dirs or files. """
            from google.appengine.tools.devappserver2 import watcher_common
            watcher_common._IGNORED_REGEX = regex
            watcher_common.ignore_file = ignore_file
            watcher_common.skip_ignored_dirs = skip_ignored_dirs

        regex = sandbox._CONFIG.modules[0].skip_files
        if regex:
            fix_watcher_files(regex)

        def logging_wrapper(func):
            """
                Changes logging to use the DJANGO_COLORS settings
            """
            def _wrapper(level, format, *args, **kwargs):
                if args and len(args) == 1 and isinstance(args[0], dict):
                    args = args[0]
                    status = str(args.get("status", 200))
                else:
                    status = "200"

                try:
                    msg = format % args
                except UnicodeDecodeError:
                    msg += "\n" # This is what Django does in WSGIRequestHandler.log_message

                # Utilize terminal colors, if available
                if status[0] == '2':
                    # Put 2XX first, since it should be the common case
                    msg = self.style.HTTP_SUCCESS(msg)
                elif status[0] == '1':
                    msg = self.style.HTTP_INFO(msg)
                elif status == '304':
                    msg = self.style.HTTP_NOT_MODIFIED(msg)
                elif status[0] == '3':
                    msg = self.style.HTTP_REDIRECT(msg)
                elif status == '404':
                    msg = self.style.HTTP_NOT_FOUND(msg)
                elif status[0] == '4':
                    # 0x16 = Handshake, 0x03 = SSL 3.0 or TLS 1.x
                    if status.startswith(str('\x16\x03')):
                        msg = ("You're accessing the development server over HTTPS, "
                            "but it only supports HTTP.\n")
                    msg = self.style.HTTP_BAD_REQUEST(msg)
                else:
                    # Any 5XX, or any other response
                    msg = self.style.HTTP_SERVER_ERROR(msg)

                return func(level, msg)
            return _wrapper

        module.logging.log = logging_wrapper(module.logging.log)

        python_runtime._RUNTIME_PATH = os.path.join(sdk_path, '_python_runtime.py')
        python_runtime._RUNTIME_ARGS = [sys.executable, python_runtime._RUNTIME_PATH]

        dev_server = NoConfigDevServer()

        try:
            dev_server.start(sandbox._OPTIONS)
            try:
                shutdown.wait_until_shutdown()
            except KeyboardInterrupt:
                pass
        finally:
            dev_server.stop()


        if shutdown_message:
            sys.stdout.write(shutdown_message)

        return
