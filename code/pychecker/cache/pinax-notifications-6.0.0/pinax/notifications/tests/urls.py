from django.conf.urls import include, url

urlpatterns = [
    url(r"^notifications/", include("pinax.notifications.urls", namespace="pinax_notifications")),
]
