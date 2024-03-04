from django.conf.urls import url

from .views import NoticeSettingsView

app_name = "pinax_notifications"

urlpatterns = [
    url(r"^settings/$", NoticeSettingsView.as_view(), name="notice_settings"),
]
