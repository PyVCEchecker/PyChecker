'''
# AWS::Cassandra Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_cassandra as cassandra
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
class CfnKeyspace(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cassandra.CfnKeyspace",
):
    '''A CloudFormation ``AWS::Cassandra::Keyspace``.

    :cloudformationResource: AWS::Cassandra::Keyspace
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        keyspace_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Cassandra::Keyspace``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param keyspace_name: ``AWS::Cassandra::Keyspace.KeyspaceName``.
        :param tags: ``AWS::Cassandra::Keyspace.Tags``.
        '''
        props = CfnKeyspaceProps(keyspace_name=keyspace_name, tags=tags)

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
        '''``AWS::Cassandra::Keyspace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keyspaceName")
    def keyspace_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cassandra::Keyspace.KeyspaceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-keyspacename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyspaceName"))

    @keyspace_name.setter
    def keyspace_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "keyspaceName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cassandra.CfnKeyspaceProps",
    jsii_struct_bases=[],
    name_mapping={"keyspace_name": "keyspaceName", "tags": "tags"},
)
class CfnKeyspaceProps:
    def __init__(
        self,
        *,
        keyspace_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Cassandra::Keyspace``.

        :param keyspace_name: ``AWS::Cassandra::Keyspace.KeyspaceName``.
        :param tags: ``AWS::Cassandra::Keyspace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if keyspace_name is not None:
            self._values["keyspace_name"] = keyspace_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def keyspace_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cassandra::Keyspace.KeyspaceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-keyspacename
        '''
        result = self._values.get("keyspace_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Cassandra::Keyspace.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html#cfn-cassandra-keyspace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKeyspaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTable(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cassandra.CfnTable",
):
    '''A CloudFormation ``AWS::Cassandra::Table``.

    :cloudformationResource: AWS::Cassandra::Table
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        keyspace_name: builtins.str,
        partition_key_columns: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable]]],
        billing_mode: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.BillingModeProperty"]] = None,
        clustering_key_columns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnTable.ClusteringKeyColumnProperty"]]]] = None,
        encryption_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.EncryptionSpecificationProperty"]] = None,
        point_in_time_recovery_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        regular_columns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable]]]] = None,
        table_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Cassandra::Table``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param keyspace_name: ``AWS::Cassandra::Table.KeyspaceName``.
        :param partition_key_columns: ``AWS::Cassandra::Table.PartitionKeyColumns``.
        :param billing_mode: ``AWS::Cassandra::Table.BillingMode``.
        :param clustering_key_columns: ``AWS::Cassandra::Table.ClusteringKeyColumns``.
        :param encryption_specification: ``AWS::Cassandra::Table.EncryptionSpecification``.
        :param point_in_time_recovery_enabled: ``AWS::Cassandra::Table.PointInTimeRecoveryEnabled``.
        :param regular_columns: ``AWS::Cassandra::Table.RegularColumns``.
        :param table_name: ``AWS::Cassandra::Table.TableName``.
        :param tags: ``AWS::Cassandra::Table.Tags``.
        '''
        props = CfnTableProps(
            keyspace_name=keyspace_name,
            partition_key_columns=partition_key_columns,
            billing_mode=billing_mode,
            clustering_key_columns=clustering_key_columns,
            encryption_specification=encryption_specification,
            point_in_time_recovery_enabled=point_in_time_recovery_enabled,
            regular_columns=regular_columns,
            table_name=table_name,
            tags=tags,
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
        '''``AWS::Cassandra::Table.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keyspaceName")
    def keyspace_name(self) -> builtins.str:
        '''``AWS::Cassandra::Table.KeyspaceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-keyspacename
        '''
        return typing.cast(builtins.str, jsii.get(self, "keyspaceName"))

    @keyspace_name.setter
    def keyspace_name(self, value: builtins.str) -> None:
        jsii.set(self, "keyspaceName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="partitionKeyColumns")
    def partition_key_columns(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable]]]:
        '''``AWS::Cassandra::Table.PartitionKeyColumns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-partitionkeycolumns
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable]]], jsii.get(self, "partitionKeyColumns"))

    @partition_key_columns.setter
    def partition_key_columns(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable]]],
    ) -> None:
        jsii.set(self, "partitionKeyColumns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="billingMode")
    def billing_mode(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.BillingModeProperty"]]:
        '''``AWS::Cassandra::Table.BillingMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-billingmode
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.BillingModeProperty"]], jsii.get(self, "billingMode"))

    @billing_mode.setter
    def billing_mode(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.BillingModeProperty"]],
    ) -> None:
        jsii.set(self, "billingMode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clusteringKeyColumns")
    def clustering_key_columns(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTable.ClusteringKeyColumnProperty"]]]]:
        '''``AWS::Cassandra::Table.ClusteringKeyColumns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-clusteringkeycolumns
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTable.ClusteringKeyColumnProperty"]]]], jsii.get(self, "clusteringKeyColumns"))

    @clustering_key_columns.setter
    def clustering_key_columns(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTable.ClusteringKeyColumnProperty"]]]],
    ) -> None:
        jsii.set(self, "clusteringKeyColumns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="encryptionSpecification")
    def encryption_specification(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.EncryptionSpecificationProperty"]]:
        '''``AWS::Cassandra::Table.EncryptionSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-encryptionspecification
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.EncryptionSpecificationProperty"]], jsii.get(self, "encryptionSpecification"))

    @encryption_specification.setter
    def encryption_specification(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.EncryptionSpecificationProperty"]],
    ) -> None:
        jsii.set(self, "encryptionSpecification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pointInTimeRecoveryEnabled")
    def point_in_time_recovery_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Cassandra::Table.PointInTimeRecoveryEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-pointintimerecoveryenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "pointInTimeRecoveryEnabled"))

    @point_in_time_recovery_enabled.setter
    def point_in_time_recovery_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "pointInTimeRecoveryEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="regularColumns")
    def regular_columns(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable]]]]:
        '''``AWS::Cassandra::Table.RegularColumns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-regularcolumns
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable]]]], jsii.get(self, "regularColumns"))

    @regular_columns.setter
    def regular_columns(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "regularColumns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cassandra::Table.TableName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tablename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tableName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-cassandra.CfnTable.BillingModeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mode": "mode",
            "provisioned_throughput": "provisionedThroughput",
        },
    )
    class BillingModeProperty:
        def __init__(
            self,
            *,
            mode: builtins.str,
            provisioned_throughput: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.ProvisionedThroughputProperty"]] = None,
        ) -> None:
            '''
            :param mode: ``CfnTable.BillingModeProperty.Mode``.
            :param provisioned_throughput: ``CfnTable.BillingModeProperty.ProvisionedThroughput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "mode": mode,
            }
            if provisioned_throughput is not None:
                self._values["provisioned_throughput"] = provisioned_throughput

        @builtins.property
        def mode(self) -> builtins.str:
            '''``CfnTable.BillingModeProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html#cfn-cassandra-table-billingmode-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def provisioned_throughput(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.ProvisionedThroughputProperty"]]:
            '''``CfnTable.BillingModeProperty.ProvisionedThroughput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-billingmode.html#cfn-cassandra-table-billingmode-provisionedthroughput
            '''
            result = self._values.get("provisioned_throughput")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTable.ProvisionedThroughputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BillingModeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-cassandra.CfnTable.ClusteringKeyColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"column": "column", "order_by": "orderBy"},
    )
    class ClusteringKeyColumnProperty:
        def __init__(
            self,
            *,
            column: typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable],
            order_by: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param column: ``CfnTable.ClusteringKeyColumnProperty.Column``.
            :param order_by: ``CfnTable.ClusteringKeyColumnProperty.OrderBy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "column": column,
            }
            if order_by is not None:
                self._values["order_by"] = order_by

        @builtins.property
        def column(
            self,
        ) -> typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable]:
            '''``CfnTable.ClusteringKeyColumnProperty.Column``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html#cfn-cassandra-table-clusteringkeycolumn-column
            '''
            result = self._values.get("column")
            assert result is not None, "Required property 'column' is missing"
            return typing.cast(typing.Union["CfnTable.ColumnProperty", aws_cdk.core.IResolvable], result)

        @builtins.property
        def order_by(self) -> typing.Optional[builtins.str]:
            '''``CfnTable.ClusteringKeyColumnProperty.OrderBy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-clusteringkeycolumn.html#cfn-cassandra-table-clusteringkeycolumn-orderby
            '''
            result = self._values.get("order_by")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClusteringKeyColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-cassandra.CfnTable.ColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"column_name": "columnName", "column_type": "columnType"},
    )
    class ColumnProperty:
        def __init__(
            self,
            *,
            column_name: builtins.str,
            column_type: builtins.str,
        ) -> None:
            '''
            :param column_name: ``CfnTable.ColumnProperty.ColumnName``.
            :param column_type: ``CfnTable.ColumnProperty.ColumnType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "column_name": column_name,
                "column_type": column_type,
            }

        @builtins.property
        def column_name(self) -> builtins.str:
            '''``CfnTable.ColumnProperty.ColumnName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html#cfn-cassandra-table-column-columnname
            '''
            result = self._values.get("column_name")
            assert result is not None, "Required property 'column_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def column_type(self) -> builtins.str:
            '''``CfnTable.ColumnProperty.ColumnType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-column.html#cfn-cassandra-table-column-columntype
            '''
            result = self._values.get("column_type")
            assert result is not None, "Required property 'column_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-cassandra.CfnTable.EncryptionSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_type": "encryptionType",
            "kms_key_identifier": "kmsKeyIdentifier",
        },
    )
    class EncryptionSpecificationProperty:
        def __init__(
            self,
            *,
            encryption_type: builtins.str,
            kms_key_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param encryption_type: ``CfnTable.EncryptionSpecificationProperty.EncryptionType``.
            :param kms_key_identifier: ``CfnTable.EncryptionSpecificationProperty.KmsKeyIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "encryption_type": encryption_type,
            }
            if kms_key_identifier is not None:
                self._values["kms_key_identifier"] = kms_key_identifier

        @builtins.property
        def encryption_type(self) -> builtins.str:
            '''``CfnTable.EncryptionSpecificationProperty.EncryptionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html#cfn-cassandra-table-encryptionspecification-encryptiontype
            '''
            result = self._values.get("encryption_type")
            assert result is not None, "Required property 'encryption_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_identifier(self) -> typing.Optional[builtins.str]:
            '''``CfnTable.EncryptionSpecificationProperty.KmsKeyIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-encryptionspecification.html#cfn-cassandra-table-encryptionspecification-kmskeyidentifier
            '''
            result = self._values.get("kms_key_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-cassandra.CfnTable.ProvisionedThroughputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "read_capacity_units": "readCapacityUnits",
            "write_capacity_units": "writeCapacityUnits",
        },
    )
    class ProvisionedThroughputProperty:
        def __init__(
            self,
            *,
            read_capacity_units: jsii.Number,
            write_capacity_units: jsii.Number,
        ) -> None:
            '''
            :param read_capacity_units: ``CfnTable.ProvisionedThroughputProperty.ReadCapacityUnits``.
            :param write_capacity_units: ``CfnTable.ProvisionedThroughputProperty.WriteCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "read_capacity_units": read_capacity_units,
                "write_capacity_units": write_capacity_units,
            }

        @builtins.property
        def read_capacity_units(self) -> jsii.Number:
            '''``CfnTable.ProvisionedThroughputProperty.ReadCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html#cfn-cassandra-table-provisionedthroughput-readcapacityunits
            '''
            result = self._values.get("read_capacity_units")
            assert result is not None, "Required property 'read_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def write_capacity_units(self) -> jsii.Number:
            '''``CfnTable.ProvisionedThroughputProperty.WriteCapacityUnits``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cassandra-table-provisionedthroughput.html#cfn-cassandra-table-provisionedthroughput-writecapacityunits
            '''
            result = self._values.get("write_capacity_units")
            assert result is not None, "Required property 'write_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedThroughputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cassandra.CfnTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "keyspace_name": "keyspaceName",
        "partition_key_columns": "partitionKeyColumns",
        "billing_mode": "billingMode",
        "clustering_key_columns": "clusteringKeyColumns",
        "encryption_specification": "encryptionSpecification",
        "point_in_time_recovery_enabled": "pointInTimeRecoveryEnabled",
        "regular_columns": "regularColumns",
        "table_name": "tableName",
        "tags": "tags",
    },
)
class CfnTableProps:
    def __init__(
        self,
        *,
        keyspace_name: builtins.str,
        partition_key_columns: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnTable.ColumnProperty, aws_cdk.core.IResolvable]]],
        billing_mode: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTable.BillingModeProperty]] = None,
        clustering_key_columns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnTable.ClusteringKeyColumnProperty]]]] = None,
        encryption_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTable.EncryptionSpecificationProperty]] = None,
        point_in_time_recovery_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        regular_columns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnTable.ColumnProperty, aws_cdk.core.IResolvable]]]] = None,
        table_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Cassandra::Table``.

        :param keyspace_name: ``AWS::Cassandra::Table.KeyspaceName``.
        :param partition_key_columns: ``AWS::Cassandra::Table.PartitionKeyColumns``.
        :param billing_mode: ``AWS::Cassandra::Table.BillingMode``.
        :param clustering_key_columns: ``AWS::Cassandra::Table.ClusteringKeyColumns``.
        :param encryption_specification: ``AWS::Cassandra::Table.EncryptionSpecification``.
        :param point_in_time_recovery_enabled: ``AWS::Cassandra::Table.PointInTimeRecoveryEnabled``.
        :param regular_columns: ``AWS::Cassandra::Table.RegularColumns``.
        :param table_name: ``AWS::Cassandra::Table.TableName``.
        :param tags: ``AWS::Cassandra::Table.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "keyspace_name": keyspace_name,
            "partition_key_columns": partition_key_columns,
        }
        if billing_mode is not None:
            self._values["billing_mode"] = billing_mode
        if clustering_key_columns is not None:
            self._values["clustering_key_columns"] = clustering_key_columns
        if encryption_specification is not None:
            self._values["encryption_specification"] = encryption_specification
        if point_in_time_recovery_enabled is not None:
            self._values["point_in_time_recovery_enabled"] = point_in_time_recovery_enabled
        if regular_columns is not None:
            self._values["regular_columns"] = regular_columns
        if table_name is not None:
            self._values["table_name"] = table_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def keyspace_name(self) -> builtins.str:
        '''``AWS::Cassandra::Table.KeyspaceName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-keyspacename
        '''
        result = self._values.get("keyspace_name")
        assert result is not None, "Required property 'keyspace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partition_key_columns(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnTable.ColumnProperty, aws_cdk.core.IResolvable]]]:
        '''``AWS::Cassandra::Table.PartitionKeyColumns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-partitionkeycolumns
        '''
        result = self._values.get("partition_key_columns")
        assert result is not None, "Required property 'partition_key_columns' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnTable.ColumnProperty, aws_cdk.core.IResolvable]]], result)

    @builtins.property
    def billing_mode(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTable.BillingModeProperty]]:
        '''``AWS::Cassandra::Table.BillingMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-billingmode
        '''
        result = self._values.get("billing_mode")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTable.BillingModeProperty]], result)

    @builtins.property
    def clustering_key_columns(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTable.ClusteringKeyColumnProperty]]]]:
        '''``AWS::Cassandra::Table.ClusteringKeyColumns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-clusteringkeycolumns
        '''
        result = self._values.get("clustering_key_columns")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTable.ClusteringKeyColumnProperty]]]], result)

    @builtins.property
    def encryption_specification(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTable.EncryptionSpecificationProperty]]:
        '''``AWS::Cassandra::Table.EncryptionSpecification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-encryptionspecification
        '''
        result = self._values.get("encryption_specification")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTable.EncryptionSpecificationProperty]], result)

    @builtins.property
    def point_in_time_recovery_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Cassandra::Table.PointInTimeRecoveryEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-pointintimerecoveryenabled
        '''
        result = self._values.get("point_in_time_recovery_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def regular_columns(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnTable.ColumnProperty, aws_cdk.core.IResolvable]]]]:
        '''``AWS::Cassandra::Table.RegularColumns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-regularcolumns
        '''
        result = self._values.get("regular_columns")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnTable.ColumnProperty, aws_cdk.core.IResolvable]]]], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cassandra::Table.TableName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tablename
        '''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Cassandra::Table.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnKeyspace",
    "CfnKeyspaceProps",
    "CfnTable",
    "CfnTableProps",
]

publication.publish()
