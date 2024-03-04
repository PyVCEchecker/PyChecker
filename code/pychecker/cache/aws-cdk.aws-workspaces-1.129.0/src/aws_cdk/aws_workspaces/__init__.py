'''
# Amazon WorkSpaces Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnConnectionAlias(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-workspaces.CfnConnectionAlias",
):
    '''A CloudFormation ``AWS::WorkSpaces::ConnectionAlias``.

    :cloudformationResource: AWS::WorkSpaces::ConnectionAlias
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        connection_string: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::WorkSpaces::ConnectionAlias``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param connection_string: ``AWS::WorkSpaces::ConnectionAlias.ConnectionString``.
        :param tags: ``AWS::WorkSpaces::ConnectionAlias.Tags``.
        '''
        props = CfnConnectionAliasProps(connection_string=connection_string, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAliasId")
    def attr_alias_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AliasId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAliasId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrAssociations")
    def attr_associations(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: Associations
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrAssociations"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrConnectionAliasState")
    def attr_connection_alias_state(self) -> builtins.str:
        '''
        :cloudformationAttribute: ConnectionAliasState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionAliasState"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::WorkSpaces::ConnectionAlias.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> builtins.str:
        '''``AWS::WorkSpaces::ConnectionAlias.ConnectionString``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-connectionstring
        '''
        return typing.cast(builtins.str, jsii.get(self, "connectionString"))

    @connection_string.setter
    def connection_string(self, value: builtins.str) -> None:
        jsii.set(self, "connectionString", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-workspaces.CfnConnectionAlias.ConnectionAliasAssociationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "associated_account_id": "associatedAccountId",
            "association_status": "associationStatus",
            "connection_identifier": "connectionIdentifier",
            "resource_id": "resourceId",
        },
    )
    class ConnectionAliasAssociationProperty:
        def __init__(
            self,
            *,
            associated_account_id: typing.Optional[builtins.str] = None,
            association_status: typing.Optional[builtins.str] = None,
            connection_identifier: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param associated_account_id: ``CfnConnectionAlias.ConnectionAliasAssociationProperty.AssociatedAccountId``.
            :param association_status: ``CfnConnectionAlias.ConnectionAliasAssociationProperty.AssociationStatus``.
            :param connection_identifier: ``CfnConnectionAlias.ConnectionAliasAssociationProperty.ConnectionIdentifier``.
            :param resource_id: ``CfnConnectionAlias.ConnectionAliasAssociationProperty.ResourceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if associated_account_id is not None:
                self._values["associated_account_id"] = associated_account_id
            if association_status is not None:
                self._values["association_status"] = association_status
            if connection_identifier is not None:
                self._values["connection_identifier"] = connection_identifier
            if resource_id is not None:
                self._values["resource_id"] = resource_id

        @builtins.property
        def associated_account_id(self) -> typing.Optional[builtins.str]:
            '''``CfnConnectionAlias.ConnectionAliasAssociationProperty.AssociatedAccountId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-associatedaccountid
            '''
            result = self._values.get("associated_account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def association_status(self) -> typing.Optional[builtins.str]:
            '''``CfnConnectionAlias.ConnectionAliasAssociationProperty.AssociationStatus``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-associationstatus
            '''
            result = self._values.get("association_status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connection_identifier(self) -> typing.Optional[builtins.str]:
            '''``CfnConnectionAlias.ConnectionAliasAssociationProperty.ConnectionIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-connectionidentifier
            '''
            result = self._values.get("connection_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''``CfnConnectionAlias.ConnectionAliasAssociationProperty.ResourceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-connectionalias-connectionaliasassociation.html#cfn-workspaces-connectionalias-connectionaliasassociation-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionAliasAssociationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-workspaces.CfnConnectionAliasProps",
    jsii_struct_bases=[],
    name_mapping={"connection_string": "connectionString", "tags": "tags"},
)
class CfnConnectionAliasProps:
    def __init__(
        self,
        *,
        connection_string: builtins.str,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WorkSpaces::ConnectionAlias``.

        :param connection_string: ``AWS::WorkSpaces::ConnectionAlias.ConnectionString``.
        :param tags: ``AWS::WorkSpaces::ConnectionAlias.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "connection_string": connection_string,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connection_string(self) -> builtins.str:
        '''``AWS::WorkSpaces::ConnectionAlias.ConnectionString``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-connectionstring
        '''
        result = self._values.get("connection_string")
        assert result is not None, "Required property 'connection_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::WorkSpaces::ConnectionAlias.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-connectionalias.html#cfn-workspaces-connectionalias-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectionAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWorkspace(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-workspaces.CfnWorkspace",
):
    '''A CloudFormation ``AWS::WorkSpaces::Workspace``.

    :cloudformationResource: AWS::WorkSpaces::Workspace
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        bundle_id: builtins.str,
        directory_id: builtins.str,
        user_name: builtins.str,
        root_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        volume_encryption_key: typing.Optional[builtins.str] = None,
        workspace_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkspace.WorkspacePropertiesProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::WorkSpaces::Workspace``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param bundle_id: ``AWS::WorkSpaces::Workspace.BundleId``.
        :param directory_id: ``AWS::WorkSpaces::Workspace.DirectoryId``.
        :param user_name: ``AWS::WorkSpaces::Workspace.UserName``.
        :param root_volume_encryption_enabled: ``AWS::WorkSpaces::Workspace.RootVolumeEncryptionEnabled``.
        :param tags: ``AWS::WorkSpaces::Workspace.Tags``.
        :param user_volume_encryption_enabled: ``AWS::WorkSpaces::Workspace.UserVolumeEncryptionEnabled``.
        :param volume_encryption_key: ``AWS::WorkSpaces::Workspace.VolumeEncryptionKey``.
        :param workspace_properties: ``AWS::WorkSpaces::Workspace.WorkspaceProperties``.
        '''
        props = CfnWorkspaceProps(
            bundle_id=bundle_id,
            directory_id=directory_id,
            user_name=user_name,
            root_volume_encryption_enabled=root_volume_encryption_enabled,
            tags=tags,
            user_volume_encryption_enabled=user_volume_encryption_enabled,
            volume_encryption_key=volume_encryption_key,
            workspace_properties=workspace_properties,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::WorkSpaces::Workspace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> builtins.str:
        '''``AWS::WorkSpaces::Workspace.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-bundleid
        '''
        return typing.cast(builtins.str, jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: builtins.str) -> None:
        jsii.set(self, "bundleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        '''``AWS::WorkSpaces::Workspace.DirectoryId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-directoryid
        '''
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        jsii.set(self, "directoryId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''``AWS::WorkSpaces::Workspace.UserName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-username
        '''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        jsii.set(self, "userName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rootVolumeEncryptionEnabled")
    def root_volume_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::WorkSpaces::Workspace.RootVolumeEncryptionEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-rootvolumeencryptionenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "rootVolumeEncryptionEnabled"))

    @root_volume_encryption_enabled.setter
    def root_volume_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "rootVolumeEncryptionEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userVolumeEncryptionEnabled")
    def user_volume_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::WorkSpaces::Workspace.UserVolumeEncryptionEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-uservolumeencryptionenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "userVolumeEncryptionEnabled"))

    @user_volume_encryption_enabled.setter
    def user_volume_encryption_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "userVolumeEncryptionEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeEncryptionKey")
    def volume_encryption_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::WorkSpaces::Workspace.VolumeEncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-volumeencryptionkey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeEncryptionKey"))

    @volume_encryption_key.setter
    def volume_encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "volumeEncryptionKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workspaceProperties")
    def workspace_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkspace.WorkspacePropertiesProperty"]]:
        '''``AWS::WorkSpaces::Workspace.WorkspaceProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-workspaceproperties
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkspace.WorkspacePropertiesProperty"]], jsii.get(self, "workspaceProperties"))

    @workspace_properties.setter
    def workspace_properties(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkspace.WorkspacePropertiesProperty"]],
    ) -> None:
        jsii.set(self, "workspaceProperties", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-workspaces.CfnWorkspace.WorkspacePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compute_type_name": "computeTypeName",
            "root_volume_size_gib": "rootVolumeSizeGib",
            "running_mode": "runningMode",
            "running_mode_auto_stop_timeout_in_minutes": "runningModeAutoStopTimeoutInMinutes",
            "user_volume_size_gib": "userVolumeSizeGib",
        },
    )
    class WorkspacePropertiesProperty:
        def __init__(
            self,
            *,
            compute_type_name: typing.Optional[builtins.str] = None,
            root_volume_size_gib: typing.Optional[jsii.Number] = None,
            running_mode: typing.Optional[builtins.str] = None,
            running_mode_auto_stop_timeout_in_minutes: typing.Optional[jsii.Number] = None,
            user_volume_size_gib: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param compute_type_name: ``CfnWorkspace.WorkspacePropertiesProperty.ComputeTypeName``.
            :param root_volume_size_gib: ``CfnWorkspace.WorkspacePropertiesProperty.RootVolumeSizeGib``.
            :param running_mode: ``CfnWorkspace.WorkspacePropertiesProperty.RunningMode``.
            :param running_mode_auto_stop_timeout_in_minutes: ``CfnWorkspace.WorkspacePropertiesProperty.RunningModeAutoStopTimeoutInMinutes``.
            :param user_volume_size_gib: ``CfnWorkspace.WorkspacePropertiesProperty.UserVolumeSizeGib``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if compute_type_name is not None:
                self._values["compute_type_name"] = compute_type_name
            if root_volume_size_gib is not None:
                self._values["root_volume_size_gib"] = root_volume_size_gib
            if running_mode is not None:
                self._values["running_mode"] = running_mode
            if running_mode_auto_stop_timeout_in_minutes is not None:
                self._values["running_mode_auto_stop_timeout_in_minutes"] = running_mode_auto_stop_timeout_in_minutes
            if user_volume_size_gib is not None:
                self._values["user_volume_size_gib"] = user_volume_size_gib

        @builtins.property
        def compute_type_name(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkspace.WorkspacePropertiesProperty.ComputeTypeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-computetypename
            '''
            result = self._values.get("compute_type_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def root_volume_size_gib(self) -> typing.Optional[jsii.Number]:
            '''``CfnWorkspace.WorkspacePropertiesProperty.RootVolumeSizeGib``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-rootvolumesizegib
            '''
            result = self._values.get("root_volume_size_gib")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def running_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkspace.WorkspacePropertiesProperty.RunningMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmode
            '''
            result = self._values.get("running_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def running_mode_auto_stop_timeout_in_minutes(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''``CfnWorkspace.WorkspacePropertiesProperty.RunningModeAutoStopTimeoutInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-runningmodeautostoptimeoutinminutes
            '''
            result = self._values.get("running_mode_auto_stop_timeout_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def user_volume_size_gib(self) -> typing.Optional[jsii.Number]:
            '''``CfnWorkspace.WorkspacePropertiesProperty.UserVolumeSizeGib``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspaces-workspace-workspaceproperties.html#cfn-workspaces-workspace-workspaceproperties-uservolumesizegib
            '''
            result = self._values.get("user_volume_size_gib")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkspacePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-workspaces.CfnWorkspaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "bundle_id": "bundleId",
        "directory_id": "directoryId",
        "user_name": "userName",
        "root_volume_encryption_enabled": "rootVolumeEncryptionEnabled",
        "tags": "tags",
        "user_volume_encryption_enabled": "userVolumeEncryptionEnabled",
        "volume_encryption_key": "volumeEncryptionKey",
        "workspace_properties": "workspaceProperties",
    },
)
class CfnWorkspaceProps:
    def __init__(
        self,
        *,
        bundle_id: builtins.str,
        directory_id: builtins.str,
        user_name: builtins.str,
        root_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        user_volume_encryption_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        volume_encryption_key: typing.Optional[builtins.str] = None,
        workspace_properties: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkspace.WorkspacePropertiesProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WorkSpaces::Workspace``.

        :param bundle_id: ``AWS::WorkSpaces::Workspace.BundleId``.
        :param directory_id: ``AWS::WorkSpaces::Workspace.DirectoryId``.
        :param user_name: ``AWS::WorkSpaces::Workspace.UserName``.
        :param root_volume_encryption_enabled: ``AWS::WorkSpaces::Workspace.RootVolumeEncryptionEnabled``.
        :param tags: ``AWS::WorkSpaces::Workspace.Tags``.
        :param user_volume_encryption_enabled: ``AWS::WorkSpaces::Workspace.UserVolumeEncryptionEnabled``.
        :param volume_encryption_key: ``AWS::WorkSpaces::Workspace.VolumeEncryptionKey``.
        :param workspace_properties: ``AWS::WorkSpaces::Workspace.WorkspaceProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bundle_id": bundle_id,
            "directory_id": directory_id,
            "user_name": user_name,
        }
        if root_volume_encryption_enabled is not None:
            self._values["root_volume_encryption_enabled"] = root_volume_encryption_enabled
        if tags is not None:
            self._values["tags"] = tags
        if user_volume_encryption_enabled is not None:
            self._values["user_volume_encryption_enabled"] = user_volume_encryption_enabled
        if volume_encryption_key is not None:
            self._values["volume_encryption_key"] = volume_encryption_key
        if workspace_properties is not None:
            self._values["workspace_properties"] = workspace_properties

    @builtins.property
    def bundle_id(self) -> builtins.str:
        '''``AWS::WorkSpaces::Workspace.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-bundleid
        '''
        result = self._values.get("bundle_id")
        assert result is not None, "Required property 'bundle_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_id(self) -> builtins.str:
        '''``AWS::WorkSpaces::Workspace.DirectoryId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-directoryid
        '''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''``AWS::WorkSpaces::Workspace.UserName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def root_volume_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::WorkSpaces::Workspace.RootVolumeEncryptionEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-rootvolumeencryptionenabled
        '''
        result = self._values.get("root_volume_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::WorkSpaces::Workspace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def user_volume_encryption_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::WorkSpaces::Workspace.UserVolumeEncryptionEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-uservolumeencryptionenabled
        '''
        result = self._values.get("user_volume_encryption_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def volume_encryption_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::WorkSpaces::Workspace.VolumeEncryptionKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-volumeencryptionkey
        '''
        result = self._values.get("volume_encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workspace_properties(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkspace.WorkspacePropertiesProperty]]:
        '''``AWS::WorkSpaces::Workspace.WorkspaceProperties``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html#cfn-workspaces-workspace-workspaceproperties
        '''
        result = self._values.get("workspace_properties")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkspace.WorkspacePropertiesProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkspaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnectionAlias",
    "CfnConnectionAliasProps",
    "CfnWorkspace",
    "CfnWorkspaceProps",
]

publication.publish()
