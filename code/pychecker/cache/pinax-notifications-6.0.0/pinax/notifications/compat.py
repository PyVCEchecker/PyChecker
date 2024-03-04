try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote  # noqa

try:
    from threading import get_ident
except ImportError:
    from thread import get_ident  # noqa

try:
    from account.decorators import login_required
except ImportError:
    from django.contrib.auth.decorators import login_required  # noqa
