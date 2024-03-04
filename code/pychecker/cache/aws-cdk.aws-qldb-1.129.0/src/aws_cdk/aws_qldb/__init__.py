'''
# AWS::QLDB Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_qldb as qldb
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
class CfnLedger(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-qldb.CfnLedger",
):
    '''A CloudFormation ``AWS::QLDB::Ledger``.

    :cloudformationResource: AWS::QLDB::Ledger
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        permissions_mode: builtins.str,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        kms_key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::QLDB::Ledger``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param permissions_mode: ``AWS::QLDB::Ledger.PermissionsMode``.
        :param deletion_protection: ``AWS::QLDB::Ledger.DeletionProtection``.
        :param kms_key: ``AWS::QLDB::Ledger.KmsKey``.
        :param name: ``AWS::QLDB::Ledger.Name``.
        :param tags: ``AWS::QLDB::Ledger.Tags``.
        '''
        props = CfnLedgerProps(
            permissions_mode=permissions_mode,
            deletion_protection=deletion_protection,
            kms_key=kms_key,
            name=name,
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
        '''``AWS::QLDB::Ledger.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionsMode")
    def permissions_mode(self) -> builtins.str:
        '''``AWS::QLDB::Ledger.PermissionsMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-permissionsmode
        '''
        return typing.cast(builtins.str, jsii.get(self, "permissionsMode"))

    @permissions_mode.setter
    def permissions_mode(self, value: builtins.str) -> None:
        jsii.set(self, "permissionsMode", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::QLDB::Ledger.DeletionProtection``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-deletionprotection
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "deletionProtection", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::QLDB::Ledger.KmsKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-kmskey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QLDB::Ledger.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-qldb.CfnLedgerProps",
    jsii_struct_bases=[],
    name_mapping={
        "permissions_mode": "permissionsMode",
        "deletion_protection": "deletionProtection",
        "kms_key": "kmsKey",
        "name": "name",
        "tags": "tags",
    },
)
class CfnLedgerProps:
    def __init__(
        self,
        *,
        permissions_mode: builtins.str,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        kms_key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::QLDB::Ledger``.

        :param permissions_mode: ``AWS::QLDB::Ledger.PermissionsMode``.
        :param deletion_protection: ``AWS::QLDB::Ledger.DeletionProtection``.
        :param kms_key: ``AWS::QLDB::Ledger.KmsKey``.
        :param name: ``AWS::QLDB::Ledger.Name``.
        :param tags: ``AWS::QLDB::Ledger.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "permissions_mode": permissions_mode,
        }
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def permissions_mode(self) -> builtins.str:
        '''``AWS::QLDB::Ledger.PermissionsMode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-permissionsmode
        '''
        result = self._values.get("permissions_mode")
        assert result is not None, "Required property 'permissions_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::QLDB::Ledger.DeletionProtection``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-deletionprotection
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::QLDB::Ledger.KmsKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-kmskey
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::QLDB::Ledger.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::QLDB::Ledger.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html#cfn-qldb-ledger-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLedgerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStream(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-qldb.CfnStream",
):
    '''A CloudFormation ``AWS::QLDB::Stream``.

    :cloudformationResource: AWS::QLDB::Stream
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        inclusive_start_time: builtins.str,
        kinesis_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnStream.KinesisConfigurationProperty"],
        ledger_name: builtins.str,
        role_arn: builtins.str,
        stream_name: builtins.str,
        exclusive_end_time: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::QLDB::Stream``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param inclusive_start_time: ``AWS::QLDB::Stream.InclusiveStartTime``.
        :param kinesis_configuration: ``AWS::QLDB::Stream.KinesisConfiguration``.
        :param ledger_name: ``AWS::QLDB::Stream.LedgerName``.
        :param role_arn: ``AWS::QLDB::Stream.RoleArn``.
        :param stream_name: ``AWS::QLDB::Stream.StreamName``.
        :param exclusive_end_time: ``AWS::QLDB::Stream.ExclusiveEndTime``.
        :param tags: ``AWS::QLDB::Stream.Tags``.
        '''
        props = CfnStreamProps(
            inclusive_start_time=inclusive_start_time,
            kinesis_configuration=kinesis_configuration,
            ledger_name=ledger_name,
            role_arn=role_arn,
            stream_name=stream_name,
            exclusive_end_time=exclusive_end_time,
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::QLDB::Stream.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inclusiveStartTime")
    def inclusive_start_time(self) -> builtins.str:
        '''``AWS::QLDB::Stream.InclusiveStartTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-inclusivestarttime
        '''
        return typing.cast(builtins.str, jsii.get(self, "inclusiveStartTime"))

    @inclusive_start_time.setter
    def inclusive_start_time(self, value: builtins.str) -> None:
        jsii.set(self, "inclusiveStartTime", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kinesisConfiguration")
    def kinesis_configuration(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnStream.KinesisConfigurationProperty"]:
        '''``AWS::QLDB::Stream.KinesisConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-kinesisconfiguration
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnStream.KinesisConfigurationProperty"], jsii.get(self, "kinesisConfiguration"))

    @kinesis_configuration.setter
    def kinesis_configuration(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnStream.KinesisConfigurationProperty"],
    ) -> None:
        jsii.set(self, "kinesisConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ledgerName")
    def ledger_name(self) -> builtins.str:
        '''``AWS::QLDB::Stream.LedgerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-ledgername
        '''
        return typing.cast(builtins.str, jsii.get(self, "ledgerName"))

    @ledger_name.setter
    def ledger_name(self, value: builtins.str) -> None:
        jsii.set(self, "ledgerName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::QLDB::Stream.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> builtins.str:
        '''``AWS::QLDB::Stream.StreamName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-streamname
        '''
        return typing.cast(builtins.str, jsii.get(self, "streamName"))

    @stream_name.setter
    def stream_name(self, value: builtins.str) -> None:
        jsii.set(self, "streamName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="exclusiveEndTime")
    def exclusive_end_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::QLDB::Stream.ExclusiveEndTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-exclusiveendtime
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exclusiveEndTime"))

    @exclusive_end_time.setter
    def exclusive_end_time(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "exclusiveEndTime", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-qldb.CfnStream.KinesisConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregation_enabled": "aggregationEnabled",
            "stream_arn": "streamArn",
        },
    )
    class KinesisConfigurationProperty:
        def __init__(
            self,
            *,
            aggregation_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            stream_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param aggregation_enabled: ``CfnStream.KinesisConfigurationProperty.AggregationEnabled``.
            :param stream_arn: ``CfnStream.KinesisConfigurationProperty.StreamArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if aggregation_enabled is not None:
                self._values["aggregation_enabled"] = aggregation_enabled
            if stream_arn is not None:
                self._values["stream_arn"] = stream_arn

        @builtins.property
        def aggregation_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnStream.KinesisConfigurationProperty.AggregationEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-aggregationenabled
            '''
            result = self._values.get("aggregation_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def stream_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnStream.KinesisConfigurationProperty.StreamArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-qldb-stream-kinesisconfiguration.html#cfn-qldb-stream-kinesisconfiguration-streamarn
            '''
            result = self._values.get("stream_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-qldb.CfnStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "inclusive_start_time": "inclusiveStartTime",
        "kinesis_configuration": "kinesisConfiguration",
        "ledger_name": "ledgerName",
        "role_arn": "roleArn",
        "stream_name": "streamName",
        "exclusive_end_time": "exclusiveEndTime",
        "tags": "tags",
    },
)
class CfnStreamProps:
    def __init__(
        self,
        *,
        inclusive_start_time: builtins.str,
        kinesis_configuration: typing.Union[aws_cdk.core.IResolvable, CfnStream.KinesisConfigurationProperty],
        ledger_name: builtins.str,
        role_arn: builtins.str,
        stream_name: builtins.str,
        exclusive_end_time: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::QLDB::Stream``.

        :param inclusive_start_time: ``AWS::QLDB::Stream.InclusiveStartTime``.
        :param kinesis_configuration: ``AWS::QLDB::Stream.KinesisConfiguration``.
        :param ledger_name: ``AWS::QLDB::Stream.LedgerName``.
        :param role_arn: ``AWS::QLDB::Stream.RoleArn``.
        :param stream_name: ``AWS::QLDB::Stream.StreamName``.
        :param exclusive_end_time: ``AWS::QLDB::Stream.ExclusiveEndTime``.
        :param tags: ``AWS::QLDB::Stream.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "inclusive_start_time": inclusive_start_time,
            "kinesis_configuration": kinesis_configuration,
            "ledger_name": ledger_name,
            "role_arn": role_arn,
            "stream_name": stream_name,
        }
        if exclusive_end_time is not None:
            self._values["exclusive_end_time"] = exclusive_end_time
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def inclusive_start_time(self) -> builtins.str:
        '''``AWS::QLDB::Stream.InclusiveStartTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-inclusivestarttime
        '''
        result = self._values.get("inclusive_start_time")
        assert result is not None, "Required property 'inclusive_start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kinesis_configuration(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnStream.KinesisConfigurationProperty]:
        '''``AWS::QLDB::Stream.KinesisConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-kinesisconfiguration
        '''
        result = self._values.get("kinesis_configuration")
        assert result is not None, "Required property 'kinesis_configuration' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnStream.KinesisConfigurationProperty], result)

    @builtins.property
    def ledger_name(self) -> builtins.str:
        '''``AWS::QLDB::Stream.LedgerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-ledgername
        '''
        result = self._values.get("ledger_name")
        assert result is not None, "Required property 'ledger_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::QLDB::Stream.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_name(self) -> builtins.str:
        '''``AWS::QLDB::Stream.StreamName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-streamname
        '''
        result = self._values.get("stream_name")
        assert result is not None, "Required property 'stream_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def exclusive_end_time(self) -> typing.Optional[builtins.str]:
        '''``AWS::QLDB::Stream.ExclusiveEndTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-exclusiveendtime
        '''
        result = self._values.get("exclusive_end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::QLDB::Stream.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-stream.html#cfn-qldb-stream-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLedger",
    "CfnLedgerProps",
    "CfnStream",
    "CfnStreamProps",
]

publication.publish()
