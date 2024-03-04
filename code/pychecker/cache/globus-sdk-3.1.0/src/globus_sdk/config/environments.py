import logging
import os
from typing import Any, Dict, List, Optional, Type, cast

log = logging.getLogger(__name__)
# the format string for a service URL pulled out of the environment
# these are handled with uppercased service names, e.g.
#   `GLOBUS_SDK_SERVICE_URL_SEARCH=...`
_SERVICE_URL_VAR_FORMAT = "GLOBUS_SDK_SERVICE_URL_{}"


class EnvConfig:
    envname: str
    domain: str
    no_dotapi: List[str] = ["auth"]

    # this same dict is inherited (and therefore shared!) by all subclasses
    _registry: Dict[str, Type["EnvConfig"]] = {}

    # this is an easier hook to use than metaclass definition -- register every subclass
    # in this dict automatically
    #
    # as a result, anyone can define
    #
    #       class BetaEnv(EnvConfig):
    #           domain = "beta.foo.bar.example.com"
    #           envname = "beta"
    #
    # and retrieve it with get_config_by_name("beta")
    def __init_subclass__(cls, **kwargs: Any):
        super().__init_subclass__(**kwargs)  # type: ignore
        cls._registry[cls.envname] = cls

    @classmethod
    def get_service_url(cls, service: str) -> str:
        # you can override any name with a config attribute
        service_url_attr = f"{service}_url"
        if hasattr(cls, service_url_attr):
            return cast(str, getattr(cls, service_url_attr))

        # the typical pattern for a service hostname is X.api.Y
        # X=transfer, Y=preview.globus.org => transfer.api.preview.globus.org
        # check `no_dotapi` for services which don't have `.api` in their names
        if service in cls.no_dotapi:
            return f"https://{service}.{cls.domain}/"
        return f"https://{service}.api.{cls.domain}/"

    @classmethod
    def get_by_name(cls, envname: str) -> Optional[Type["EnvConfig"]]:
        return cls._registry.get(envname)


def get_service_url(environment: str, service: str) -> str:
    log.debug(f'Service URL Lookup for "{service}" under env "{environment}"')
    # check for an environment variable of the form
    #   GLOBUS_SDK_SERVICE_URL_*
    # and use it ahead of any env config if set
    varname = _SERVICE_URL_VAR_FORMAT.format(service.upper())
    from_env = os.getenv(varname)
    if from_env:
        log.debug(f"Got URL from env var, {varname}={from_env}")
        return from_env
    conf = EnvConfig.get_by_name(environment)
    if not conf:
        raise ValueError(f'Unrecognized environment "{environment}"')
    url = conf.get_service_url(service)
    log.debug(f'Service URL Lookup Result: "{service}" is at "{url}"')
    return url


#
# public environments
#


class ProductionEnvConfig(EnvConfig):
    envname = "production"
    domain = "globus.org"
    nexus_url = "https://nexus.api.globusonline.org/"


class PreviewEnvConfig(EnvConfig):
    envname = "preview"
    domain = "preview.globus.org"


#
# environments for internal use only
#
for envname in ["sandbox", "integration", "test", "staging"]:
    # use `type()` rather than the `class` syntax to control classnames
    type(
        f"{envname.title()}EnvConfig",
        (EnvConfig,),
        {"envname": envname, "domain": f"{envname}.globuscs.info"},
    )
