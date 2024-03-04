import json
import logging
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Iterator,
    Mapping,
    Optional,
    Union,
    cast,
)

from requests import Response

log = logging.getLogger(__name__)

if TYPE_CHECKING:
    import globus_sdk


class GlobusHTTPResponse:
    """
    Response object that wraps an HTTP response from the underlying HTTP
    library. If the response is JSON, the parsed data will be available in
    ``data``, otherwise ``data`` will be ``None`` and ``text`` should
    be used instead.

    The most common response data is a JSON dictionary. To make
    handling this type of response as seamless as possible, the
    ``GlobusHTTPResponse`` object implements the immutable mapping protocol for
    dict-style access. This is just an alias for access to the underlying data.

    If ``data`` is not a dictionary, item access will raise ``TypeError``.

    >>> print("Response ID": r["id"]) # alias for r.data["id"]

    :ivar http_status: HTTP status code returned by the server (int)
    :ivar content_type: Content-Type header returned by the server (str)
    :ivar client: The client instance which made the request
    """

    def __init__(
        self,
        response: Union[Response, "GlobusHTTPResponse"],
        client: Optional["globus_sdk.BaseClient"] = None,
    ):
        # init on a GlobusHTTPResponse: we are wrapping this data
        # the _response is None
        if isinstance(response, GlobusHTTPResponse):
            if client is not None:
                raise ValueError("Redundant client with wrapped response")
            self._wrapped: Optional[GlobusHTTPResponse] = response
            self._response: Optional[Response] = None
            self.client: "globus_sdk.BaseClient" = self._wrapped.client

            # copy attributes off of '_wrapped'
            self._parsed_json: Any = self._wrapped._parsed_json
            self._text: str = self._wrapped.text
            self.http_status: int = self._wrapped.http_status
            self.content_type: Optional[str] = self._wrapped.content_type

        # init on a Response object, this is the "normal" case
        # _wrapped is None
        else:
            if client is None:
                raise ValueError("Missing client with normal response")
            self._wrapped = None
            self._response = response
            self.client = client

            # JSON decoding may raise a ValueError due to an invalid JSON
            # document. In the case of trying to fetch the "data" on an HTTP
            # response, this means we didn't get a JSON response.
            # store this as None, as in "no data"
            #
            # if the caller *really* wants the raw body of the response, they can
            # always use `text`
            try:
                self._parsed_json = self._response.json()
            except ValueError:
                log.warning("response data did not parse as JSON, data=None")
                self._parsed_json = None

            self._text = self._response.text
            self.http_status = self._response.status_code
            self.content_type = self._response.headers.get("Content-Type")

    @property
    def data(self) -> Any:
        return self._parsed_json

    @property
    def text(self) -> str:
        """The raw response data as a string."""
        return self._text

    def get(self, key: str, default: Any = None) -> Any:
        """
        ``get`` is just an alias for ``data.get(key, default)``, but with the added
        check that if ``data`` is ``None``, it returns the default.
        """
        if self.data is None:
            return default
        # NB: `default` is provided as a positional because the native dict type
        # doesn't recognize a keyword argument `default`
        return self.data.get(key, default)

    def __str__(self) -> str:
        """The default __str__ for a response assumes that the data is valid
        JSON-dump-able."""
        if self.data is not None:
            return json.dumps(self.data, indent=2, separators=(",", ": "))
        return self.text

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text})"

    def __getitem__(self, key: str) -> Any:
        # force evaluation of the data property outside of the upcoming
        # try-catch so that we don't accidentally catch TypeErrors thrown
        # during the getter function itself
        data = self.data
        try:
            return data[key]
        except TypeError:
            log.error(
                f"Can't index into responses with underlying data of type {type(data)}"
            )
            # re-raise with an altered message and error type -- the issue is that
            # whatever data is in the response doesn't support indexing (e.g. a response
            # that is just an integer, parsed as json)
            #
            # "type" is ambiguous, but we don't know if it's the fault of the
            # class at large, or just a particular call's `data` property
            raise ValueError("This type of response data does not support indexing.")

    def __contains__(self, item: Any) -> bool:
        """
        ``x in response`` is an alias for ``x in response.data``
        """
        if self.data is None:
            return False
        return item in self.data


class IterableResponse(GlobusHTTPResponse):
    """This response class adds an __iter__ method on an 'iter_key' variable.
    The assumption is that iter produces dicts or dict-like mappings."""

    default_iter_key: ClassVar[str]
    iter_key: str

    def __init__(
        self,
        response: Union[Response, "GlobusHTTPResponse"],
        client: Optional["globus_sdk.BaseClient"] = None,
        *,
        iter_key: Optional[str] = None,
    ) -> None:
        if not hasattr(self, "default_iter_key"):
            raise TypeError(
                "Cannot instantiate an iterable response from a class "
                "which does not define a default iteration key."
            )
        iter_key = iter_key if iter_key is not None else self.default_iter_key
        self.iter_key = iter_key
        super().__init__(response, client)

    def __iter__(self) -> Iterator[Mapping]:
        return iter(cast(Mapping, self)[self.iter_key])
