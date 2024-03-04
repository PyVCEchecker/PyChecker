from .conf import settings


def load_media_defaults():
    media = []
    defaults = {}
    for key, backend in settings.PINAX_NOTIFICATIONS_BACKENDS.items():
        # key is a tuple (medium_id, backend_label)
        media.append(key)
        defaults[key[0]] = backend.spam_sensitivity
    return media, defaults
