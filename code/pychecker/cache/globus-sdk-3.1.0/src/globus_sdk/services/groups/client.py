from typing import Any, Callable, Dict, Optional, TypeVar, Union

from globus_sdk import client, response, utils
from globus_sdk.scopes import GroupsScopes
from globus_sdk.types import UUIDLike

from .data import BatchMembershipActions, GroupPolicies
from .errors import GroupsAPIError

C = TypeVar("C", bound=Callable)


def _groupdoc(message: str, link: str) -> Callable[[C], C]:
    # do not use functools.partial because it doesn't preserve type information
    # see: https://github.com/python/mypy/issues/1484
    def partial(func: C) -> C:
        return utils.doc_api_method(
            message,
            link,
            external_base_url="https://groups.api.globus.org/redoc#operation",
        )(func)

    return partial


class GroupsClient(client.BaseClient):
    """
    Client for the
    `Globus Groups API <https://docs.globus.org/api/groups/>`_.

    This provides a relatively low level client to public groups API endpoints.
    You may also consider looking at the GroupsManager as a simpler interface
    to more common actions.

    .. automethodlist:: globus_sdk.GroupsClient
    """

    base_path = "/v2/"
    error_class = GroupsAPIError
    service_name = "groups"
    scopes = GroupsScopes

    @_groupdoc(
        "Retrieve your groups and membership",
        "get_my_groups_and_memberships_v2_groups_my_groups_get",
    )
    def get_my_groups(
        self, *, query_params: Optional[Dict[str, Any]] = None
    ) -> response.GlobusHTTPResponse:
        """
        Return a list of groups your identity belongs to.
        """
        return self.get("/groups/my_groups", query_params=query_params)

    @_groupdoc("Get Group", "get_group_v2_groups__group_id__get")
    def get_group(
        self, group_id: UUIDLike, *, query_params: Optional[Dict[str, Any]] = None
    ) -> response.GlobusHTTPResponse:
        """
        Get details about a specific group
        """
        return self.get(f"/groups/{group_id}", query_params=query_params)

    @_groupdoc("Delete a group", "delete_group_v2_groups__group_id__delete")
    def delete_group(
        self, group_id: UUIDLike, *, query_params: Optional[Dict[str, Any]] = None
    ) -> response.GlobusHTTPResponse:
        """
        Delete a group.
        """
        return self.delete(f"/groups/{group_id}", query_params=query_params)

    @_groupdoc("Create a group", "create_group_v2_groups_post")
    def create_group(
        self, data: Dict[str, Any], *, query_params: Optional[Dict[str, Any]] = None
    ) -> response.GlobusHTTPResponse:
        """
        Create a group.
        """
        return self.post("/groups", data=data, query_params=query_params)

    @_groupdoc(
        "Get the policies for the group",
        "get_policies_v2_groups__group_id__policies_get",
    )
    def get_group_policies(
        self, group_id: UUIDLike, *, query_params: Optional[Dict[str, Any]] = None
    ) -> response.GlobusHTTPResponse:
        """
        Get policies for the given group
        """
        return self.get(f"/groups/{group_id}/policies", query_params=query_params)

    @_groupdoc(
        "Set the policies for the group",
        "update_policies_v2_groups__group_id__policies_put",
    )
    def set_group_policies(
        self,
        group_id: UUIDLike,
        data: Union[Dict[str, Any], GroupPolicies],
        *,
        query_params: Optional[Dict[str, Any]] = None,
    ) -> response.GlobusHTTPResponse:
        """
        Set policies for the group.
        """
        return self.put(
            f"/groups/{group_id}/policies", data=data, query_params=query_params
        )

    @_groupdoc(
        "Get the preferences for your identity set",
        "get_identity_set_preferences_v2_preferences_get",
    )
    def get_identity_preferences(
        self, *, query_params: Optional[Dict[str, Any]] = None
    ) -> response.GlobusHTTPResponse:
        """
        Get identity preferences.  Currently this only includes whether the
        user allows themselves to be added to groups.
        """
        return self.get("/preferences", query_params=query_params)

    @_groupdoc(
        "Set the preferences for your identity set",
        "put_identity_set_preferences_v2_preferences_put",
    )
    def set_identity_preferences(
        self,
        data: Dict[str, Any],
        *,
        query_params: Optional[Dict[str, Any]] = None,
    ) -> response.GlobusHTTPResponse:
        """
        Set identity preferences.  Currently this only includes whether the
        user allows themselves to be added to groups.
        """
        return self.put("/preferences", data=data, query_params=query_params)

    @_groupdoc(
        "Get the membership fields for your identity set",
        "get_membership_fields_v2_groups__group_id__membership_fields_get",
    )
    def get_membership_fields(
        self,
        group_id: UUIDLike,
        *,
        query_params: Optional[Dict[str, Any]] = None,
    ) -> response.GlobusHTTPResponse:
        """
        Get membership fields for your identities.
        """
        return self.get(
            f"/groups/{group_id}/membership_fields", query_params=query_params
        )

    @_groupdoc(
        "Set the membership fields for your identity set",
        "put_membership_fields_v2_groups__group_id__membership_fields_put",
    )
    def set_membership_fields(
        self,
        group_id: UUIDLike,
        data: Dict[Any, str],
        *,
        query_params: Optional[Dict[str, Any]] = None,
    ) -> response.GlobusHTTPResponse:
        """
        Get membership fields for your identities.
        """
        return self.put(
            f"/groups/{group_id}/membership_fields",
            data=data,
            query_params=query_params,
        )

    @_groupdoc(
        "Perform actions on members of the group",
        "group_membership_post_actions_v2_groups__group_id__post",
    )
    def batch_membership_action(
        self,
        group_id: UUIDLike,
        actions: Union[Dict[str, Any], BatchMembershipActions],
        *,
        query_params: Optional[Dict[str, Any]] = None,
    ) -> response.GlobusHTTPResponse:
        """
        Execute a batch of actions against several group memberships.
        """
        return self.post(f"/groups/{group_id}", data=actions, query_params=query_params)
