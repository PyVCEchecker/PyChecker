from typing import Any, Dict, List, Optional, Tuple, Union

from globus_sdk import utils


class SearchQuery(utils.PayloadWrapper):
    """
    A specialized dict which has helpers for creating and modifying a Search
    Query document.

    Example usage:

    >>> from globus_sdk import SearchClient, SearchQuery
    >>> sc = SearchClient(...)
    >>> index_id = ...
    >>> query = (SearchQuery(q='example query')
    >>>          .set_limit(100).set_offset(10)
    >>>          .add_filter('path.to.field1', ['foo', 'bar']))
    >>> result = sc.post_search(index_id, query)
    """

    def __init__(
        self,
        q: Optional[str] = None,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        advanced: Optional[bool] = None,
        additional_fields: Optional[Dict[str, Any]] = None,
    ):
        super().__init__()
        if q is not None:
            self["q"] = q
        if limit is not None:
            self["limit"] = limit
        if offset is not None:
            self["offset"] = offset
        if advanced is not None:
            self["advanced"] = advanced
        if additional_fields is not None:
            self.update(additional_fields)

    def set_query(self, query: str) -> "SearchQuery":
        self["q"] = query
        return self

    def set_limit(self, limit: int) -> "SearchQuery":
        self["limit"] = limit
        return self

    def set_offset(self, offset: int) -> "SearchQuery":
        self["offset"] = offset
        return self

    def set_advanced(self, advanced: bool) -> "SearchQuery":
        self["advanced"] = advanced
        return self

    def add_facet(
        self,
        name: str,
        field_name: str,
        *,
        type: str = "terms",
        size: Optional[int] = None,
        date_interval: Optional[str] = None,
        histogram_range: Optional[Tuple[Any, Any]] = None,
        additional_fields: Optional[Dict[str, Any]] = None,
    ) -> "SearchQuery":
        self["facets"] = self.get("facets", [])
        facet: Dict[str, Any] = {
            "name": name,
            "field_name": field_name,
            "type": type,
            **(additional_fields or {}),
        }
        if size is not None:
            facet["size"] = size
        if date_interval is not None:
            facet["date_interval"] = date_interval
        if histogram_range is not None:
            low, high = histogram_range
            facet["histogram_range"] = {"low": low, "high": high}
        self["facets"].append(facet)
        return self

    def add_filter(
        self,
        field_name: str,
        values: List[str],
        *,
        type: str = "match_all",
        additional_fields: Optional[Dict[str, Any]] = None,
    ) -> "SearchQuery":
        self["filters"] = self.get("filters", [])
        new_filter = {
            "field_name": field_name,
            "values": values,
            "type": type,
            **(additional_fields or {}),
        }
        self["filters"].append(new_filter)
        return self

    def add_boost(
        self,
        field_name: str,
        factor: Union[str, int, float],
        *,
        additional_fields: Optional[Dict[str, Any]] = None,
    ) -> "SearchQuery":
        self["boosts"] = self.get("boosts", [])
        boost = {
            "field_name": field_name,
            "factor": factor,
            **(additional_fields or {}),
        }
        self["boosts"].append(boost)
        return self

    def add_sort(
        self,
        field_name: str,
        *,
        order: Optional[str] = None,
        additional_fields: Optional[Dict[str, Any]] = None,
    ) -> "SearchQuery":
        self["sort"] = self.get("sort", [])
        sort = {"field_name": field_name, **(additional_fields or {})}
        if order is not None:
            sort["order"] = order
        self["sort"].append(sort)
        return self
