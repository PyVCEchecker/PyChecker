from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ImproperlyConfigured


class DjangaeConfig(AppConfig):
    name = 'djangae'
    verbose_name = _("Djangae")

    def ready(self):
        from .patches import json
        json.patch()

        from djangae.db.backends.appengine.caching import reset_context
        from djangae.db.migrations.signals import check_migrations
        from django.core.signals import request_finished, request_started
        from django.db.models.signals import pre_migrate

        request_finished.connect(reset_context, dispatch_uid="request_finished_context_reset")
        request_started.connect(reset_context, dispatch_uid="request_started_context_reset")
        pre_migrate.connect(check_migrations, dispatch_uid="pre_migrate_check_connections")

        self._check_content_types()

    def _check_content_types(self):
        """ Check that if Django and/or Djangae contenttypes are being used that they are
            configured correctly.
        """
        from django.conf import settings
        contenttype_configuration_error = ImproperlyConfigured(
            "If you're using django.contrib.contenttypes, then you need "
            "to add djangae.contrib.contenttypes to INSTALLED_APPS after "
            "django.contrib.contenttypes."
        )
        if 'django.contrib.contenttypes' in settings.INSTALLED_APPS:
            from django.db import router, connections
            from django.contrib.contenttypes.models import ContentType
            conn = connections[router.db_for_read(ContentType)]

            if conn.settings_dict.get("ENGINE") != 'djangae.db.backends.appengine':
                # Don't enforce djangae.contrib.contenttypes if content types are being
                # saved to a different database backend
                return

            if not 'djangae.contrib.contenttypes' in settings.INSTALLED_APPS:
                # Raise error if User is using Django CT, but not Djangae
                raise contenttype_configuration_error
            else:
                if settings.INSTALLED_APPS.index('django.contrib.contenttypes') > \
                        settings.INSTALLED_APPS.index('djangae.contrib.contenttypes'):
                    # Raise error if User is using both Django and Djangae CT, but
                    # Django CT comes after Djangae CT
                    raise contenttype_configuration_error

        from django.core import checks
        from djangae import checks

