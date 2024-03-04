# THIRD PARTY
from django.conf.urls import url

# DJANGAE
from .views import cleanup_locks


urlpatterns = [
    url(r'^djangae-cleanup-locks/$', cleanup_locks, name="cleanup_locks"),
]
