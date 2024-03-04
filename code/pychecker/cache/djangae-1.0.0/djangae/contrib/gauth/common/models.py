import warnings

warnings.warn(
    "djangae.contrib.gauth.common is deprecated, please import from djangae.contrib.gauth "
    "directly instead."
)

from djangae.contrib.gauth import models, backends, validators
