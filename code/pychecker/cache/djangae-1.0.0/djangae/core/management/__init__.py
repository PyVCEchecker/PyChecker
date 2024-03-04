import os
import re
import sys
import argparse

import djangae.sandbox as sandbox
from djangae import environment

DEFAULTS = {
    "storage_path": os.path.join(environment.get_application_root(), ".storage"),
    "port": 8000,
    "admin_port": 8001,
    "api_port": 8002,
    "automatic_restart": "True",
    "allow_skipped_files": "True",
    "app_id": "managepy",
}


def execute_from_command_line(argv=None, **sandbox_overrides):
    """Wraps Django's `execute_from_command_line` to initialize a djangae
    sandbox before running a management command.
    """
    argv = argv or sys.argv[:]

    djangae_parser = argparse.ArgumentParser(description='Djangae arguments', add_help=False)
    djangae_parser.add_argument('--sandbox', default=sandbox.LOCAL, choices=sandbox.SANDBOXES.keys())
    djangae_parser.add_argument('--app_id', default=None, help='GAE APPLICATION ID')

    ignored_args = ('-v', '--version')
    stashed_args = [arg for arg in argv[1:] if arg in ignored_args]

    djangae_namespace, other_args = djangae_parser.parse_known_args([arg for arg in argv[1:] if arg not in ignored_args])

    argv = ['manage.py'] + other_args + stashed_args

    overrides = DEFAULTS.copy()
    overrides.update(sandbox_overrides)

    if djangae_namespace.app_id:
        overrides.update(app_id=djangae_namespace.app_id)

    return _execute_from_command_line(djangae_namespace.sandbox, argv, parser=djangae_parser, **overrides)


def _execute_from_command_line(sandbox_name, argv, parser=None, **sandbox_overrides):
    # Parses for a settings flag, adding it as an environment variable to
    # retrieve additional overridden module settings
    env_vars = {}
    for arg in argv:
        m = re.match(r'--(?P<module_name>.+)-settings=(?P<settings_path>.+)', arg)
        if m:
            argv.remove(arg)
            env_vars['%s_DJANGO_SETTINGS_MODULE' % m.group('module_name')] = m.group('settings_path')

        m = re.match(r'--settings=(?P<settings_path>.+)', arg)
        if m:
            env_vars['DJANGO_SETTINGS_MODULE'] = m.group('settings_path')

    with sandbox.activate(
        sandbox_name,
        add_sdk_to_path=True,
        new_env_vars=env_vars,
        **sandbox_overrides
    ):
        try:
            import django.core.management as django_management  # Now on the path
            return django_management.execute_from_command_line(argv)
        except SystemExit as e:
            # print Djangae parser options help message
            print_help = any([arg in ('-h', '--help') for arg in argv])
            if e.code == 0 and print_help:
                parser.print_help()
                sys.stdout.write('\n')
            raise


def remote_execute_from_command_line(argv=None, **sandbox_overrides):
    """Execute commands in the remote sandbox"""
    return _execute_from_command_line(sandbox.REMOTE, argv or sys.argv, **sandbox_overrides)


def local_execute_from_command_line(argv=None, **sandbox_overrides):
    """Execute commands in the local sandbox"""
    return _execute_from_command_line(sandbox.LOCAL, argv or sys.argv, **sandbox_overrides)


def test_execute_from_command_line(argv=None, **sandbox_overrides):
    """Execute commands in the test sandbox"""
    return _execute_from_command_line(sandbox.TEST, argv or sys.argv, **sandbox_overrides)
