import importlib

from django.apps import apps as django_apps
from django.conf import settings  # noqa
from django.core.exceptions import ImproperlyConfigured

from appconf import AppConf


def load_model(path):
    try:
        return django_apps.get_model(path)
    except ValueError:
        raise ImproperlyConfigured(
            f"{path} must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(f"{path} has not been installed")


def load_path_attr(path):
    i = path.rfind(".")
    module, attr = path[:i], path[i + 1:]
    try:
        mod = importlib.import_module(module)
    except ImportError as e:
        raise ImproperlyConfigured(f"Error importing {module}: '{e}'")
    try:
        attr = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured(f"Module '{module}' does not define a '{attr}'")
    return attr


def is_installed(package):
    try:
        __import__(package)
        return True
    except ImportError:
        return False


class PinaxNotificationsAppConf(AppConf):

    LOCK_WAIT_TIMEOUT = -1
    GET_LANGUAGE_MODEL = None
    LANGUAGE_MODEL = None
    QUEUE_ALL = False
    HOOKSET = "pinax.notifications.hooks.DefaultHookSet"
    BACKENDS = [
        ("email", "pinax.notifications.backends.email.EmailBackend"),
    ]

    def configure_backends(self, value):
        backends = []
        for medium_id, bits in enumerate(value):
            if len(bits) == 2:
                label, backend_path = bits
                spam_sensitivity = None
            elif len(bits) == 3:
                label, backend_path, spam_sensitivity = bits
            else:
                raise ImproperlyConfigured(
                    "NOTIFICATION_BACKENDS does not contain enough data."
                )
            backend_instance = load_path_attr(backend_path)(medium_id, spam_sensitivity)
            backends.append(((medium_id, label), backend_instance))
        return dict(backends)

    def configure_get_language_model(self, value):
        if value is None:
            return lambda: load_model(settings.PINAX_NOTIFICATIONS_LANGUAGE_MODEL)

    def configure_hookset(self, value):
        return load_path_attr(value)()

    class Meta:
        prefix = "pinax_notifications"
