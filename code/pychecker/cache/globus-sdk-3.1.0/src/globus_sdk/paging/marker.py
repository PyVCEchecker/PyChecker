from typing import Any, Callable, Dict, Iterator, List, Optional

from globus_sdk.response import GlobusHTTPResponse

from .base import Paginator


class MarkerPaginator(Paginator):
    """
    A paginator which uses `has_next_page` and `marker` from payloads, sets the `marker`
    query param to page.

    This is the default method for GCS pagination, so it's very simple.
    """

    def __init__(
        self,
        method: Callable,
        *,
        items_key: Optional[str] = None,
        client_args: List[Any],
        client_kwargs: Dict[str, Any]
    ):
        super().__init__(
            method,
            items_key=items_key,
            client_args=client_args,
            client_kwargs=client_kwargs,
        )
        self.marker: Optional[str] = None

    def pages(self) -> Iterator[GlobusHTTPResponse]:
        has_next_page = True
        while has_next_page:
            if self.marker:
                self.client_kwargs["marker"] = self.marker
            current_page = self.method(*self.client_args, **self.client_kwargs)
            yield current_page
            self.marker = current_page.get("marker")
            has_next_page = current_page.get("has_next_page", False)
