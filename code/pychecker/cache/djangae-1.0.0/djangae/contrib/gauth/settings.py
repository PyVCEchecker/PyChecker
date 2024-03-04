
AUTHENTICATION_BACKENDS = (
    'djangae.contrib.gauth_datastore.backends.AppEngineUserAPIBackend',
)

AUTH_USER_MODEL = 'gauth_datastore.GaeDatastoreUser'
LOGIN_URL = 'djangae_login_redirect'

# Set this to True to allow unknown Google users to sign in. Matching is done
# by email.
# DJANGAE_CREATE_UNKNOWN_USER = True
