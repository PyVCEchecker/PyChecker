import pkg_resources

default_app_config = "pinax.notifications.apps.AppConfig"
__version__ = pkg_resources.get_distribution("pinax-notifications").version
