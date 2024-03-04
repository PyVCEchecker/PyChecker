from django.db import models

from ..conf import settings


class Language(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.CharField("language", max_length=10)
