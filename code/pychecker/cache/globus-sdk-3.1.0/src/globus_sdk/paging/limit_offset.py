from typing import Any, Callable, Dict, Iterator, List, Optional

from globus_sdk.response import GlobusHTTPResponse

from .base import Paginator


class _LimitOffsetBasedPaginator(Paginator):
    def __init__(
        self,
        method: Callable,
        *,
        items_key: Optional[str] = None,
        get_page_size: Callable[[dict], int],
        max_total_results: int,
        page_size: int,
        client_args: List[Any],
        client_kwargs: Dict[str, Any],
    ):
        super().__init__(
            method,
            items_key=items_key,
            client_args=client_args,
            client_kwargs=client_kwargs,
        )
        self.get_page_size = get_page_size
        self.max_total_results = max_total_results
        self.limit = page_size
        self.offset = 0

    def _update_limit(self) -> None:
        if (
            self.max_total_results is not None
            and self.offset + self.limit > self.max_total_results
        ):
            self.limit = self.max_total_results - self.offset
        self.client_kwargs["limit"] = self.limit

    def _update_and_check_offset(self, current_page: dict) -> bool:
        self.offset += self.get_page_size(current_page)
        self.client_kwargs["offset"] = self.offset
        return (
            self.max_total_results is not None and self.offset >= self.max_total_results
        )


class HasNextPaginator(_LimitOffsetBasedPaginator):
    def pages(self) -> Iterator[GlobusHTTPResponse]:
        has_next_page = True
        while has_next_page:
            self._update_limit()
            current_page = self.method(*self.client_args, **self.client_kwargs)
            yield current_page
            if self._update_and_check_offset(current_page):
                return
            has_next_page = current_page["has_next_page"]


class LimitOffsetTotalPaginator(_LimitOffsetBasedPaginator):
    def pages(self) -> Iterator[GlobusHTTPResponse]:
        has_next_page = True
        while has_next_page:
            self._update_limit()
            current_page = self.method(*self.client_args, **self.client_kwargs)
            yield current_page
            if self._update_and_check_offset(current_page):
                return
            has_next_page = self.offset < current_page["total"]
