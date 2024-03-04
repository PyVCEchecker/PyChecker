from django import VERSION as django_version
from django.contrib.auth import authenticate, login, logout, get_user, BACKEND_SESSION_KEY, load_backend
from django.contrib.auth.middleware import AuthenticationMiddleware as DjangoMiddleware
from django.contrib.auth.models import AnonymousUser, BaseUserManager
from djangae.contrib.gauth.backends import BaseAppEngineUserAPIBackend

from google.appengine.api import users


def user_is_authenticated(django_user):
    """ Since 1.10 Django is_authenticated is an attribute, not a method.
    The backward-compatibility is supported by the function. We could remove
    the function and replace all the calls to it with
    `django_user.is_authenticated` once we stop supporting Django versions
    lower than 1.10. """
    if django_version[:3] < (1, 10, 0):
        return django_user.is_authenticated()
    return django_user.is_authenticated


class AuthenticationMiddleware(DjangoMiddleware):
    def process_request(self, request):
        django_user = get_user(request)
        google_user = users.get_current_user()

        # Check to see if the user is authenticated with a different backend, if so, just set
        # request.user and bail
        if user_is_authenticated(django_user):
            backend_str = request.session.get(BACKEND_SESSION_KEY)
            if (not backend_str) or not isinstance(load_backend(backend_str), BaseAppEngineUserAPIBackend):
                request.user = django_user
                return

        if django_user.is_anonymous() and google_user:
            # If there is a google user, but we are anonymous, log in!
            # Note that if DJANGAE_CREATE_UNKNOWN_USER=False then this may not authenticate
            django_user = authenticate(google_user=google_user) or AnonymousUser()
            if user_is_authenticated(django_user):
                login(request, django_user)

        if user_is_authenticated(django_user):
            if not google_user:
                # If we are logged in with django, but not longer logged in with Google
                # then log out
                logout(request)
                django_user = AnonymousUser()
            elif django_user.username != google_user.user_id():
                # If the Google user changed, we need to log in with the new one
                logout(request)
                django_user = authenticate(google_user=google_user) or AnonymousUser()
                if user_is_authenticated(django_user):
                    login(request, django_user)

        # Note that the logic above may have logged us out, hence new `if` statement
        if user_is_authenticated(django_user):
            self.sync_user_data(django_user, google_user)

        request.user = django_user

    def sync_user_data(self, django_user, google_user):
        # Now make sure we update is_superuser and is_staff appropriately
        changed_fields = []

        is_superuser = users.is_current_user_admin()

        if is_superuser != django_user.is_superuser:
            django_user.is_superuser = django_user.is_staff = is_superuser
            changed_fields += ['is_superuser', 'is_staff']

        email = BaseUserManager.normalize_email(google_user.email())  # Normalizes the domain only.

        if email != django_user.email:
            django_user.email = email
            changed_fields += ['email', 'email_lower']

        if changed_fields:
            django_user.save(update_fields=changed_fields)
