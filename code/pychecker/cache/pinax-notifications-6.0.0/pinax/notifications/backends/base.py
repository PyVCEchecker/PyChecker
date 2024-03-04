from django.contrib.sites.models import Site
from django.template.loader import render_to_string

from ..conf import settings
from ..hooks import hookset


class BaseBackend:
    """
    The base backend.
    """
    def __init__(self, medium_id, spam_sensitivity=None):
        self.medium_id = medium_id
        if spam_sensitivity is not None:
            self.spam_sensitivity = spam_sensitivity

    def can_send(self, user, notice_type, scoping):
        """
        Determines whether this backend is allowed to send a notification to
        the given user and notice_type.
        """
        return hookset.notice_setting_for_user(user, notice_type, self.medium_id, scoping).send

    def deliver(self, recipient, sender, notice_type, extra_context):
        """
        Deliver a notification to the given recipient.
        """
        raise NotImplementedError()

    def get_formatted_messages(self, formats, label, context):
        """
        Returns a dictionary with the format identifier as the key. The values are
        are fully rendered templates with the given context.
        """
        format_templates = {}
        for fmt in formats:
            format_templates[fmt] = render_to_string((
                f"pinax/notifications/{label}/{fmt}",
                f"pinax/notifications/{fmt}"), context)
        return format_templates

    def default_context(self):
        use_ssl = getattr(settings, "PINAX_USE_SSL", False)
        default_http_protocol = "https" if use_ssl else "http"
        current_site = Site.objects.get_current()
        base_url = f"{default_http_protocol}://{current_site.domain}"
        return {
            "default_http_protocol": default_http_protocol,
            "current_site": current_site,
            "base_url": base_url
        }
