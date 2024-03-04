import abc
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional

from globus_sdk.response import GlobusHTTPResponse


class Paginator(Iterable[GlobusHTTPResponse], metaclass=abc.ABCMeta):
    """
    Base class for all paginators.
    This guarantees is that they have generator methods named ``pages`` and ``items``.

    Iterating on a Paginator is equivalent to iterating on its ``pages``.

    :param method: A bound method of an SDK client, used to generate a paginated variant
    :type method: callable
    :param items_key: The key to use within pages of results to get an array of items
    :type items_key: str
    :param client_args: Arguments to the underlying method which are passed when the
        paginator is instantiated. i.e. given ``client.paginated.foo(a, b, c=1)``, this
        will be ``(a, b)``. The paginator will pass these arguments to each call of the
        bound method as it pages.
    :type client_args: tuple
    :param client_kwargs: Keyword arguments to the underlying method, like
        ``client_args`` above. ``client.paginated.foo(a, b, c=1)`` will pass this as
        ``{"c": 1}``. As with ``client_args``, it's passed to each paginated call.
    :type client_kwargs: dict
    """

    def __init__(
        self,
        method: Callable,
        *,
        items_key: Optional[str] = None,
        client_args: List[Any],
        client_kwargs: Dict[str, Any]
    ):
        self.method = method
        self.items_key = items_key
        self.client_args = client_args
        self.client_kwargs = client_kwargs

    def __iter__(self) -> Iterator[GlobusHTTPResponse]:
        yield from self.pages()

    @abc.abstractmethod
    def pages(self) -> Iterator[GlobusHTTPResponse]:
        """``pages()`` yields GlobusHTTPResponse objects, each one representing a page
        of results."""

    def items(self) -> Iterator:
        """
        ``items()`` of a paginator is a generator which yields each item in each page of
        results.

        ``items()`` may raise a ``ValueError`` if the paginator was constructed without
        identifying a key for use within each page of results. This may be the case for
        paginators whose pages are not primarily an array of data.
        """
        if self.items_key is None:
            raise ValueError(
                "Cannot provide items() iteration on a paginator where 'items_key' "
                "is not set."
            )
        for page in self.pages():
            yield from page[self.items_key]
