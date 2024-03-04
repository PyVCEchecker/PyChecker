'''
# AWS::LakeFormation Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_lakeformation as lakeformation
```
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
class CfnDataLakeSettings(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lakeformation.CfnDataLakeSettings",
):
    '''A CloudFormation ``AWS::LakeFormation::DataLakeSettings``.

    :cloudformationResource: AWS::LakeFormation::DataLakeSettings
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        admins: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", aws_cdk.core.IResolvable]]]] = None,
        trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::DataLakeSettings``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param admins: ``AWS::LakeFormation::DataLakeSettings.Admins``.
        :param trusted_resource_owners: ``AWS::LakeFormation::DataLakeSettings.TrustedResourceOwners``.
        '''
        props = CfnDataLakeSettingsProps(
            admins=admins, trusted_resource_owners=trusted_resource_owners
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
    @jsii.member(jsii_name="admins")
    def admins(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", aws_cdk.core.IResolvable]]]]:
        '''``AWS::LakeFormation::DataLakeSettings.Admins``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", aws_cdk.core.IResolvable]]]], jsii.get(self, "admins"))

    @admins.setter
    def admins(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataLakeSettings.DataLakePrincipalProperty", aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "admins", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trustedResourceOwners")
    def trusted_resource_owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LakeFormation::DataLakeSettings.TrustedResourceOwners``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "trustedResourceOwners"))

    @trusted_resource_owners.setter
    def trusted_resource_owners(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "trustedResourceOwners", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnDataLakeSettings.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(
            self,
            *,
            data_lake_principal_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_lake_principal_identifier: ``CfnDataLakeSettings.DataLakePrincipalProperty.DataLakePrincipalIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''``CfnDataLakeSettings.DataLakePrincipalProperty.DataLakePrincipalIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-datalakesettings-datalakeprincipal.html#cfn-lakeformation-datalakesettings-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lakeformation.CfnDataLakeSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "admins": "admins",
        "trusted_resource_owners": "trustedResourceOwners",
    },
)
class CfnDataLakeSettingsProps:
    def __init__(
        self,
        *,
        admins: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, aws_cdk.core.IResolvable]]]] = None,
        trusted_resource_owners: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::LakeFormation::DataLakeSettings``.

        :param admins: ``AWS::LakeFormation::DataLakeSettings.Admins``.
        :param trusted_resource_owners: ``AWS::LakeFormation::DataLakeSettings.TrustedResourceOwners``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if admins is not None:
            self._values["admins"] = admins
        if trusted_resource_owners is not None:
            self._values["trusted_resource_owners"] = trusted_resource_owners

    @builtins.property
    def admins(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, aws_cdk.core.IResolvable]]]]:
        '''``AWS::LakeFormation::DataLakeSettings.Admins``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-admins
        '''
        result = self._values.get("admins")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnDataLakeSettings.DataLakePrincipalProperty, aws_cdk.core.IResolvable]]]], result)

    @builtins.property
    def trusted_resource_owners(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LakeFormation::DataLakeSettings.TrustedResourceOwners``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html#cfn-lakeformation-datalakesettings-trustedresourceowners
        '''
        result = self._values.get("trusted_resource_owners")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataLakeSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPermissions(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions",
):
    '''A CloudFormation ``AWS::LakeFormation::Permissions``.

    :cloudformationResource: AWS::LakeFormation::Permissions
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        data_lake_principal: typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLakePrincipalProperty"],
        resource: typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ResourceProperty"],
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::Permissions``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param data_lake_principal: ``AWS::LakeFormation::Permissions.DataLakePrincipal``.
        :param resource: ``AWS::LakeFormation::Permissions.Resource``.
        :param permissions: ``AWS::LakeFormation::Permissions.Permissions``.
        :param permissions_with_grant_option: ``AWS::LakeFormation::Permissions.PermissionsWithGrantOption``.
        '''
        props = CfnPermissionsProps(
            data_lake_principal=data_lake_principal,
            resource=resource,
            permissions=permissions,
            permissions_with_grant_option=permissions_with_grant_option,
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
    @jsii.member(jsii_name="dataLakePrincipal")
    def data_lake_principal(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLakePrincipalProperty"]:
        '''``AWS::LakeFormation::Permissions.DataLakePrincipal``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLakePrincipalProperty"], jsii.get(self, "dataLakePrincipal"))

    @data_lake_principal.setter
    def data_lake_principal(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLakePrincipalProperty"],
    ) -> None:
        jsii.set(self, "dataLakePrincipal", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ResourceProperty"]:
        '''``AWS::LakeFormation::Permissions.Resource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ResourceProperty"], jsii.get(self, "resource"))

    @resource.setter
    def resource(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ResourceProperty"],
    ) -> None:
        jsii.set(self, "resource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LakeFormation::Permissions.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "permissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionsWithGrantOption")
    def permissions_with_grant_option(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LakeFormation::Permissions.PermissionsWithGrantOption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionsWithGrantOption"))

    @permissions_with_grant_option.setter
    def permissions_with_grant_option(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "permissionsWithGrantOption", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.ColumnWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={"excluded_column_names": "excludedColumnNames"},
    )
    class ColumnWildcardProperty:
        def __init__(
            self,
            *,
            excluded_column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param excluded_column_names: ``CfnPermissions.ColumnWildcardProperty.ExcludedColumnNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if excluded_column_names is not None:
                self._values["excluded_column_names"] = excluded_column_names

        @builtins.property
        def excluded_column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPermissions.ColumnWildcardProperty.ExcludedColumnNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-columnwildcard.html#cfn-lakeformation-permissions-columnwildcard-excludedcolumnnames
            '''
            result = self._values.get("excluded_column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.DataLakePrincipalProperty",
        jsii_struct_bases=[],
        name_mapping={"data_lake_principal_identifier": "dataLakePrincipalIdentifier"},
    )
    class DataLakePrincipalProperty:
        def __init__(
            self,
            *,
            data_lake_principal_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_lake_principal_identifier: ``CfnPermissions.DataLakePrincipalProperty.DataLakePrincipalIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if data_lake_principal_identifier is not None:
                self._values["data_lake_principal_identifier"] = data_lake_principal_identifier

        @builtins.property
        def data_lake_principal_identifier(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.DataLakePrincipalProperty.DataLakePrincipalIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalakeprincipal.html#cfn-lakeformation-permissions-datalakeprincipal-datalakeprincipalidentifier
            '''
            result = self._values.get("data_lake_principal_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLakePrincipalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.DataLocationResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "s3_resource": "s3Resource"},
    )
    class DataLocationResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            s3_resource: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param catalog_id: ``CfnPermissions.DataLocationResourceProperty.CatalogId``.
            :param s3_resource: ``CfnPermissions.DataLocationResourceProperty.S3Resource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if s3_resource is not None:
                self._values["s3_resource"] = s3_resource

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.DataLocationResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_resource(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.DataLocationResourceProperty.S3Resource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-datalocationresource.html#cfn-lakeformation-permissions-datalocationresource-s3resource
            '''
            result = self._values.get("s3_resource")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataLocationResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.DatabaseResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"catalog_id": "catalogId", "name": "name"},
    )
    class DatabaseResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param catalog_id: ``CfnPermissions.DatabaseResourceProperty.CatalogId``.
            :param name: ``CfnPermissions.DatabaseResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.DatabaseResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.DatabaseResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-databaseresource.html#cfn-lakeformation-permissions-databaseresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatabaseResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.ResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_resource": "databaseResource",
            "data_location_resource": "dataLocationResource",
            "table_resource": "tableResource",
            "table_with_columns_resource": "tableWithColumnsResource",
        },
    )
    class ResourceProperty:
        def __init__(
            self,
            *,
            database_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DatabaseResourceProperty"]] = None,
            data_location_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLocationResourceProperty"]] = None,
            table_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableResourceProperty"]] = None,
            table_with_columns_resource: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableWithColumnsResourceProperty"]] = None,
        ) -> None:
            '''
            :param database_resource: ``CfnPermissions.ResourceProperty.DatabaseResource``.
            :param data_location_resource: ``CfnPermissions.ResourceProperty.DataLocationResource``.
            :param table_resource: ``CfnPermissions.ResourceProperty.TableResource``.
            :param table_with_columns_resource: ``CfnPermissions.ResourceProperty.TableWithColumnsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if database_resource is not None:
                self._values["database_resource"] = database_resource
            if data_location_resource is not None:
                self._values["data_location_resource"] = data_location_resource
            if table_resource is not None:
                self._values["table_resource"] = table_resource
            if table_with_columns_resource is not None:
                self._values["table_with_columns_resource"] = table_with_columns_resource

        @builtins.property
        def database_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DatabaseResourceProperty"]]:
            '''``CfnPermissions.ResourceProperty.DatabaseResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-databaseresource
            '''
            result = self._values.get("database_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DatabaseResourceProperty"]], result)

        @builtins.property
        def data_location_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLocationResourceProperty"]]:
            '''``CfnPermissions.ResourceProperty.DataLocationResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-datalocationresource
            '''
            result = self._values.get("data_location_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.DataLocationResourceProperty"]], result)

        @builtins.property
        def table_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableResourceProperty"]]:
            '''``CfnPermissions.ResourceProperty.TableResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tableresource
            '''
            result = self._values.get("table_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableResourceProperty"]], result)

        @builtins.property
        def table_with_columns_resource(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableWithColumnsResourceProperty"]]:
            '''``CfnPermissions.ResourceProperty.TableWithColumnsResource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-resource.html#cfn-lakeformation-permissions-resource-tablewithcolumnsresource
            '''
            result = self._values.get("table_with_columns_resource")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableWithColumnsResourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.TableResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "name": "name",
            "table_wildcard": "tableWildcard",
        },
    )
    class TableResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            table_wildcard: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableWildcardProperty"]] = None,
        ) -> None:
            '''
            :param catalog_id: ``CfnPermissions.TableResourceProperty.CatalogId``.
            :param database_name: ``CfnPermissions.TableResourceProperty.DatabaseName``.
            :param name: ``CfnPermissions.TableResourceProperty.Name``.
            :param table_wildcard: ``CfnPermissions.TableResourceProperty.TableWildcard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name
            if name is not None:
                self._values["name"] = name
            if table_wildcard is not None:
                self._values["table_wildcard"] = table_wildcard

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.TableResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.TableResourceProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.TableResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_wildcard(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableWildcardProperty"]]:
            '''``CfnPermissions.TableResourceProperty.TableWildcard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tableresource.html#cfn-lakeformation-permissions-tableresource-tablewildcard
            '''
            result = self._values.get("table_wildcard")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.TableWildcardProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.TableWildcardProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class TableWildcardProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewildcard.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWildcardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-lakeformation.CfnPermissions.TableWithColumnsResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "column_names": "columnNames",
            "column_wildcard": "columnWildcard",
            "database_name": "databaseName",
            "name": "name",
        },
    )
    class TableWithColumnsResourceProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            column_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            column_wildcard: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ColumnWildcardProperty"]] = None,
            database_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param catalog_id: ``CfnPermissions.TableWithColumnsResourceProperty.CatalogId``.
            :param column_names: ``CfnPermissions.TableWithColumnsResourceProperty.ColumnNames``.
            :param column_wildcard: ``CfnPermissions.TableWithColumnsResourceProperty.ColumnWildcard``.
            :param database_name: ``CfnPermissions.TableWithColumnsResourceProperty.DatabaseName``.
            :param name: ``CfnPermissions.TableWithColumnsResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if column_names is not None:
                self._values["column_names"] = column_names
            if column_wildcard is not None:
                self._values["column_wildcard"] = column_wildcard
            if database_name is not None:
                self._values["database_name"] = database_name
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.TableWithColumnsResourceProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def column_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPermissions.TableWithColumnsResourceProperty.ColumnNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnnames
            '''
            result = self._values.get("column_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def column_wildcard(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ColumnWildcardProperty"]]:
            '''``CfnPermissions.TableWithColumnsResourceProperty.ColumnWildcard``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-columnwildcard
            '''
            result = self._values.get("column_wildcard")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPermissions.ColumnWildcardProperty"]], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.TableWithColumnsResourceProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPermissions.TableWithColumnsResourceProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lakeformation-permissions-tablewithcolumnsresource.html#cfn-lakeformation-permissions-tablewithcolumnsresource-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableWithColumnsResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lakeformation.CfnPermissionsProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_lake_principal": "dataLakePrincipal",
        "resource": "resource",
        "permissions": "permissions",
        "permissions_with_grant_option": "permissionsWithGrantOption",
    },
)
class CfnPermissionsProps:
    def __init__(
        self,
        *,
        data_lake_principal: typing.Union[aws_cdk.core.IResolvable, CfnPermissions.DataLakePrincipalProperty],
        resource: typing.Union[aws_cdk.core.IResolvable, CfnPermissions.ResourceProperty],
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_with_grant_option: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::LakeFormation::Permissions``.

        :param data_lake_principal: ``AWS::LakeFormation::Permissions.DataLakePrincipal``.
        :param resource: ``AWS::LakeFormation::Permissions.Resource``.
        :param permissions: ``AWS::LakeFormation::Permissions.Permissions``.
        :param permissions_with_grant_option: ``AWS::LakeFormation::Permissions.PermissionsWithGrantOption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "data_lake_principal": data_lake_principal,
            "resource": resource,
        }
        if permissions is not None:
            self._values["permissions"] = permissions
        if permissions_with_grant_option is not None:
            self._values["permissions_with_grant_option"] = permissions_with_grant_option

    @builtins.property
    def data_lake_principal(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnPermissions.DataLakePrincipalProperty]:
        '''``AWS::LakeFormation::Permissions.DataLakePrincipal``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-datalakeprincipal
        '''
        result = self._values.get("data_lake_principal")
        assert result is not None, "Required property 'data_lake_principal' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnPermissions.DataLakePrincipalProperty], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnPermissions.ResourceProperty]:
        '''``AWS::LakeFormation::Permissions.Resource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnPermissions.ResourceProperty], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LakeFormation::Permissions.Permissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permissions_with_grant_option(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::LakeFormation::Permissions.PermissionsWithGrantOption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html#cfn-lakeformation-permissions-permissionswithgrantoption
        '''
        result = self._values.get("permissions_with_grant_option")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResource(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lakeformation.CfnResource",
):
    '''A CloudFormation ``AWS::LakeFormation::Resource``.

    :cloudformationResource: AWS::LakeFormation::Resource
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resource_arn: builtins.str,
        use_service_linked_role: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::LakeFormation::Resource``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_arn: ``AWS::LakeFormation::Resource.ResourceArn``.
        :param use_service_linked_role: ``AWS::LakeFormation::Resource.UseServiceLinkedRole``.
        :param role_arn: ``AWS::LakeFormation::Resource.RoleArn``.
        '''
        props = CfnResourceProps(
            resource_arn=resource_arn,
            use_service_linked_role=use_service_linked_role,
            role_arn=role_arn,
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
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''``AWS::LakeFormation::Resource.ResourceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        jsii.set(self, "resourceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="useServiceLinkedRole")
    def use_service_linked_role(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::LakeFormation::Resource.UseServiceLinkedRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "useServiceLinkedRole"))

    @use_service_linked_role.setter
    def use_service_linked_role(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "useServiceLinkedRole", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::LakeFormation::Resource.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lakeformation.CfnResourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "resource_arn": "resourceArn",
        "use_service_linked_role": "useServiceLinkedRole",
        "role_arn": "roleArn",
    },
)
class CfnResourceProps:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        use_service_linked_role: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::LakeFormation::Resource``.

        :param resource_arn: ``AWS::LakeFormation::Resource.ResourceArn``.
        :param use_service_linked_role: ``AWS::LakeFormation::Resource.UseServiceLinkedRole``.
        :param role_arn: ``AWS::LakeFormation::Resource.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "use_service_linked_role": use_service_linked_role,
        }
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''``AWS::LakeFormation::Resource.ResourceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_service_linked_role(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::LakeFormation::Resource.UseServiceLinkedRole``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-useservicelinkedrole
        '''
        result = self._values.get("use_service_linked_role")
        assert result is not None, "Required property 'use_service_linked_role' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::LakeFormation::Resource.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html#cfn-lakeformation-resource-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataLakeSettings",
    "CfnDataLakeSettingsProps",
    "CfnPermissions",
    "CfnPermissionsProps",
    "CfnResource",
    "CfnResourceProps",
]

publication.publish()
