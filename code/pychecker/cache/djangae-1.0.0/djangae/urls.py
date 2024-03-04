from django.conf import settings
from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^start$', views.start),
    url(r'^stop$', views.stop),
    url(r'^warmup$', views.warmup),
    url(r'^clearsessions$', views.clearsessions),
    url(r'^queue/deferred/?$', views.deferred),
    url(r'^internalupload/$', views.internalupload, name='djangae_internal_upload_handler'),
]

# Set up the mapreduce URLs if the mapreduce processing module is installed
if 'djangae.contrib.processing.mapreduce' in settings.INSTALLED_APPS:
    import djangae.contrib.processing.mapreduce.urls

    urlpatterns.append(
       url(r'^mapreduce/', include(djangae.contrib.processing.mapreduce.urls)),
    )
