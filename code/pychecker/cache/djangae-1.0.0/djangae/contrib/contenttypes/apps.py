from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

try:
    from django.contrib.contenttypes.management import update_contenttypes as django_update_contenttypes
except ImportError:
    # Django 1.11
    from django.contrib.contenttypes.management import create_contenttypes as django_update_contenttypes

from django.db.models.signals import post_migrate

from .management import update_contenttypes
from .models import SimulatedContentTypeManager


class ContentTypesConfig(AppConfig):
    name = 'djangae.contrib.contenttypes'
    verbose_name = _("Djangae Content Types")
    label = "djangae_contenttypes"

    def ready(self):
        """ Patch the ContentTypes app so that:
            * The ContentType's manager is our SimulatedContentTypeManager.
            * The ContentType's PK field is BigIntegerField, so that ForeignKeys which point to it
              will acccept our large (signed 64 bit) IDs.
            * The update_contenttypes management function is replaced with our alternative version.
        """
        if django_update_contenttypes != update_contenttypes:
            post_migrate.disconnect(django_update_contenttypes)
            from django.db import models
            from django.contrib.contenttypes import models as django_models
            if not isinstance(django_models.ContentType.objects, SimulatedContentTypeManager):
                django_models.ContentType.objects = SimulatedContentTypeManager(django_models.ContentType)
                django_models.ContentType.objects.auto_created = True

                # Really force the default manager to use the Simulated one
                meta = django_models.ContentType._meta
                if hasattr(meta, "local_managers"):
                    # Django >= 1.10
                    meta.local_managers[0] = SimulatedContentTypeManager()
                else:
                    django_models.ContentType._default_manager = SimulatedContentTypeManager(django_models.ContentType)

                meta._expire_cache()

                # Our generated IDs take up a 64 bit range (signed) but aren't auto
                # incrementing so update the field to reflect that (for validation)
                meta.pk.__class__ = models.BigIntegerField
