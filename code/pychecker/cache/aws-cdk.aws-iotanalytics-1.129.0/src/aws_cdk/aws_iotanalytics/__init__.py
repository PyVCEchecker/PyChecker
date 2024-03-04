'''
# AWS IoT Analytics Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iotanalytics as iotanalytics
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
class CfnChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotanalytics.CfnChannel",
):
    '''A CloudFormation ``AWS::IoTAnalytics::Channel``.

    :cloudformationResource: AWS::IoTAnalytics::Channel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        channel_name: typing.Optional[builtins.str] = None,
        channel_storage: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ChannelStorageProperty"]] = None,
        retention_period: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RetentionPeriodProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTAnalytics::Channel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param channel_name: ``AWS::IoTAnalytics::Channel.ChannelName``.
        :param channel_storage: ``AWS::IoTAnalytics::Channel.ChannelStorage``.
        :param retention_period: ``AWS::IoTAnalytics::Channel.RetentionPeriod``.
        :param tags: ``AWS::IoTAnalytics::Channel.Tags``.
        '''
        props = CfnChannelProps(
            channel_name=channel_name,
            channel_storage=channel_storage,
            retention_period=retention_period,
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
        '''``AWS::IoTAnalytics::Channel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTAnalytics::Channel.ChannelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-channelname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "channelName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="channelStorage")
    def channel_storage(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ChannelStorageProperty"]]:
        '''``AWS::IoTAnalytics::Channel.ChannelStorage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-channelstorage
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ChannelStorageProperty"]], jsii.get(self, "channelStorage"))

    @channel_storage.setter
    def channel_storage(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ChannelStorageProperty"]],
    ) -> None:
        jsii.set(self, "channelStorage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="retentionPeriod")
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RetentionPeriodProperty"]]:
        '''``AWS::IoTAnalytics::Channel.RetentionPeriod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-retentionperiod
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RetentionPeriodProperty"]], jsii.get(self, "retentionPeriod"))

    @retention_period.setter
    def retention_period(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.RetentionPeriodProperty"]],
    ) -> None:
        jsii.set(self, "retentionPeriod", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnChannel.ChannelStorageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_managed_s3": "customerManagedS3",
            "service_managed_s3": "serviceManagedS3",
        },
    )
    class ChannelStorageProperty:
        def __init__(
            self,
            *,
            customer_managed_s3: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CustomerManagedS3Property"]] = None,
            service_managed_s3: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ServiceManagedS3Property"]] = None,
        ) -> None:
            '''
            :param customer_managed_s3: ``CfnChannel.ChannelStorageProperty.CustomerManagedS3``.
            :param service_managed_s3: ``CfnChannel.ChannelStorageProperty.ServiceManagedS3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if customer_managed_s3 is not None:
                self._values["customer_managed_s3"] = customer_managed_s3
            if service_managed_s3 is not None:
                self._values["service_managed_s3"] = service_managed_s3

        @builtins.property
        def customer_managed_s3(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CustomerManagedS3Property"]]:
            '''``CfnChannel.ChannelStorageProperty.CustomerManagedS3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html#cfn-iotanalytics-channel-channelstorage-customermanageds3
            '''
            result = self._values.get("customer_managed_s3")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.CustomerManagedS3Property"]], result)

        @builtins.property
        def service_managed_s3(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ServiceManagedS3Property"]]:
            '''``CfnChannel.ChannelStorageProperty.ServiceManagedS3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html#cfn-iotanalytics-channel-channelstorage-servicemanageds3
            '''
            result = self._values.get("service_managed_s3")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnChannel.ServiceManagedS3Property"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChannelStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnChannel.CustomerManagedS3Property",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "role_arn": "roleArn",
            "key_prefix": "keyPrefix",
        },
    )
    class CustomerManagedS3Property:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            role_arn: builtins.str,
            key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket: ``CfnChannel.CustomerManagedS3Property.Bucket``.
            :param role_arn: ``CfnChannel.CustomerManagedS3Property.RoleArn``.
            :param key_prefix: ``CfnChannel.CustomerManagedS3Property.KeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
                "role_arn": role_arn,
            }
            if key_prefix is not None:
                self._values["key_prefix"] = key_prefix

        @builtins.property
        def bucket(self) -> builtins.str:
            '''``CfnChannel.CustomerManagedS3Property.Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html#cfn-iotanalytics-channel-customermanageds3-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnChannel.CustomerManagedS3Property.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html#cfn-iotanalytics-channel-customermanageds3-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnChannel.CustomerManagedS3Property.KeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html#cfn-iotanalytics-channel-customermanageds3-keyprefix
            '''
            result = self._values.get("key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedS3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnChannel.RetentionPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"number_of_days": "numberOfDays", "unlimited": "unlimited"},
    )
    class RetentionPeriodProperty:
        def __init__(
            self,
            *,
            number_of_days: typing.Optional[jsii.Number] = None,
            unlimited: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param number_of_days: ``CfnChannel.RetentionPeriodProperty.NumberOfDays``.
            :param unlimited: ``CfnChannel.RetentionPeriodProperty.Unlimited``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if number_of_days is not None:
                self._values["number_of_days"] = number_of_days
            if unlimited is not None:
                self._values["unlimited"] = unlimited

        @builtins.property
        def number_of_days(self) -> typing.Optional[jsii.Number]:
            '''``CfnChannel.RetentionPeriodProperty.NumberOfDays``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html#cfn-iotanalytics-channel-retentionperiod-numberofdays
            '''
            result = self._values.get("number_of_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unlimited(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnChannel.RetentionPeriodProperty.Unlimited``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html#cfn-iotanalytics-channel-retentionperiod-unlimited
            '''
            result = self._values.get("unlimited")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetentionPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnChannel.ServiceManagedS3Property",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class ServiceManagedS3Property:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-servicemanageds3.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceManagedS3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotanalytics.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_name": "channelName",
        "channel_storage": "channelStorage",
        "retention_period": "retentionPeriod",
        "tags": "tags",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        channel_name: typing.Optional[builtins.str] = None,
        channel_storage: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.ChannelStorageProperty]] = None,
        retention_period: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.RetentionPeriodProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTAnalytics::Channel``.

        :param channel_name: ``AWS::IoTAnalytics::Channel.ChannelName``.
        :param channel_storage: ``AWS::IoTAnalytics::Channel.ChannelStorage``.
        :param retention_period: ``AWS::IoTAnalytics::Channel.RetentionPeriod``.
        :param tags: ``AWS::IoTAnalytics::Channel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if channel_name is not None:
            self._values["channel_name"] = channel_name
        if channel_storage is not None:
            self._values["channel_storage"] = channel_storage
        if retention_period is not None:
            self._values["retention_period"] = retention_period
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTAnalytics::Channel.ChannelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-channelname
        '''
        result = self._values.get("channel_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channel_storage(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.ChannelStorageProperty]]:
        '''``AWS::IoTAnalytics::Channel.ChannelStorage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-channelstorage
        '''
        result = self._values.get("channel_storage")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.ChannelStorageProperty]], result)

    @builtins.property
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.RetentionPeriodProperty]]:
        '''``AWS::IoTAnalytics::Channel.RetentionPeriod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-retentionperiod
        '''
        result = self._values.get("retention_period")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnChannel.RetentionPeriodProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTAnalytics::Channel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDataset(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset",
):
    '''A CloudFormation ``AWS::IoTAnalytics::Dataset``.

    :cloudformationResource: AWS::IoTAnalytics::Dataset
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        actions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnDataset.ActionProperty", aws_cdk.core.IResolvable]]],
        content_delivery_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DatasetContentDeliveryRuleProperty"]]]] = None,
        dataset_name: typing.Optional[builtins.str] = None,
        late_data_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.LateDataRuleProperty"]]]] = None,
        retention_period: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.RetentionPeriodProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        triggers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.TriggerProperty"]]]] = None,
        versioning_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.VersioningConfigurationProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTAnalytics::Dataset``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param actions: ``AWS::IoTAnalytics::Dataset.Actions``.
        :param content_delivery_rules: ``AWS::IoTAnalytics::Dataset.ContentDeliveryRules``.
        :param dataset_name: ``AWS::IoTAnalytics::Dataset.DatasetName``.
        :param late_data_rules: ``AWS::IoTAnalytics::Dataset.LateDataRules``.
        :param retention_period: ``AWS::IoTAnalytics::Dataset.RetentionPeriod``.
        :param tags: ``AWS::IoTAnalytics::Dataset.Tags``.
        :param triggers: ``AWS::IoTAnalytics::Dataset.Triggers``.
        :param versioning_configuration: ``AWS::IoTAnalytics::Dataset.VersioningConfiguration``.
        '''
        props = CfnDatasetProps(
            actions=actions,
            content_delivery_rules=content_delivery_rules,
            dataset_name=dataset_name,
            late_data_rules=late_data_rules,
            retention_period=retention_period,
            tags=tags,
            triggers=triggers,
            versioning_configuration=versioning_configuration,
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
        '''``AWS::IoTAnalytics::Dataset.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataset.ActionProperty", aws_cdk.core.IResolvable]]]:
        '''``AWS::IoTAnalytics::Dataset.Actions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-actions
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataset.ActionProperty", aws_cdk.core.IResolvable]]], jsii.get(self, "actions"))

    @actions.setter
    def actions(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnDataset.ActionProperty", aws_cdk.core.IResolvable]]],
    ) -> None:
        jsii.set(self, "actions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contentDeliveryRules")
    def content_delivery_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DatasetContentDeliveryRuleProperty"]]]]:
        '''``AWS::IoTAnalytics::Dataset.ContentDeliveryRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-contentdeliveryrules
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DatasetContentDeliveryRuleProperty"]]]], jsii.get(self, "contentDeliveryRules"))

    @content_delivery_rules.setter
    def content_delivery_rules(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DatasetContentDeliveryRuleProperty"]]]],
    ) -> None:
        jsii.set(self, "contentDeliveryRules", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datasetName")
    def dataset_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTAnalytics::Dataset.DatasetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-datasetname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetName"))

    @dataset_name.setter
    def dataset_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "datasetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lateDataRules")
    def late_data_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.LateDataRuleProperty"]]]]:
        '''``AWS::IoTAnalytics::Dataset.LateDataRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-latedatarules
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.LateDataRuleProperty"]]]], jsii.get(self, "lateDataRules"))

    @late_data_rules.setter
    def late_data_rules(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.LateDataRuleProperty"]]]],
    ) -> None:
        jsii.set(self, "lateDataRules", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="retentionPeriod")
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.RetentionPeriodProperty"]]:
        '''``AWS::IoTAnalytics::Dataset.RetentionPeriod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-retentionperiod
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.RetentionPeriodProperty"]], jsii.get(self, "retentionPeriod"))

    @retention_period.setter
    def retention_period(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.RetentionPeriodProperty"]],
    ) -> None:
        jsii.set(self, "retentionPeriod", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="triggers")
    def triggers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.TriggerProperty"]]]]:
        '''``AWS::IoTAnalytics::Dataset.Triggers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-triggers
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.TriggerProperty"]]]], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.TriggerProperty"]]]],
    ) -> None:
        jsii.set(self, "triggers", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="versioningConfiguration")
    def versioning_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.VersioningConfigurationProperty"]]:
        '''``AWS::IoTAnalytics::Dataset.VersioningConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-versioningconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.VersioningConfigurationProperty"]], jsii.get(self, "versioningConfiguration"))

    @versioning_configuration.setter
    def versioning_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.VersioningConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "versioningConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_name": "actionName",
            "container_action": "containerAction",
            "query_action": "queryAction",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            action_name: builtins.str,
            container_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.ContainerActionProperty"]] = None,
            query_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.QueryActionProperty"]] = None,
        ) -> None:
            '''
            :param action_name: ``CfnDataset.ActionProperty.ActionName``.
            :param container_action: ``CfnDataset.ActionProperty.ContainerAction``.
            :param query_action: ``CfnDataset.ActionProperty.QueryAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "action_name": action_name,
            }
            if container_action is not None:
                self._values["container_action"] = container_action
            if query_action is not None:
                self._values["query_action"] = query_action

        @builtins.property
        def action_name(self) -> builtins.str:
            '''``CfnDataset.ActionProperty.ActionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html#cfn-iotanalytics-dataset-action-actionname
            '''
            result = self._values.get("action_name")
            assert result is not None, "Required property 'action_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def container_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.ContainerActionProperty"]]:
            '''``CfnDataset.ActionProperty.ContainerAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html#cfn-iotanalytics-dataset-action-containeraction
            '''
            result = self._values.get("container_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.ContainerActionProperty"]], result)

        @builtins.property
        def query_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.QueryActionProperty"]]:
            '''``CfnDataset.ActionProperty.QueryAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html#cfn-iotanalytics-dataset-action-queryaction
            '''
            result = self._values.get("query_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.QueryActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.ContainerActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execution_role_arn": "executionRoleArn",
            "image": "image",
            "resource_configuration": "resourceConfiguration",
            "variables": "variables",
        },
    )
    class ContainerActionProperty:
        def __init__(
            self,
            *,
            execution_role_arn: builtins.str,
            image: builtins.str,
            resource_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnDataset.ResourceConfigurationProperty"],
            variables: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.VariableProperty"]]]] = None,
        ) -> None:
            '''
            :param execution_role_arn: ``CfnDataset.ContainerActionProperty.ExecutionRoleArn``.
            :param image: ``CfnDataset.ContainerActionProperty.Image``.
            :param resource_configuration: ``CfnDataset.ContainerActionProperty.ResourceConfiguration``.
            :param variables: ``CfnDataset.ContainerActionProperty.Variables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "execution_role_arn": execution_role_arn,
                "image": image,
                "resource_configuration": resource_configuration,
            }
            if variables is not None:
                self._values["variables"] = variables

        @builtins.property
        def execution_role_arn(self) -> builtins.str:
            '''``CfnDataset.ContainerActionProperty.ExecutionRoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-executionrolearn
            '''
            result = self._values.get("execution_role_arn")
            assert result is not None, "Required property 'execution_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image(self) -> builtins.str:
            '''``CfnDataset.ContainerActionProperty.Image``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-image
            '''
            result = self._values.get("image")
            assert result is not None, "Required property 'image' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataset.ResourceConfigurationProperty"]:
            '''``CfnDataset.ContainerActionProperty.ResourceConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-resourceconfiguration
            '''
            result = self._values.get("resource_configuration")
            assert result is not None, "Required property 'resource_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataset.ResourceConfigurationProperty"], result)

        @builtins.property
        def variables(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.VariableProperty"]]]]:
            '''``CfnDataset.ContainerActionProperty.Variables``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-variables
            '''
            result = self._values.get("variables")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.VariableProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.DatasetContentDeliveryRuleDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iot_events_destination_configuration": "iotEventsDestinationConfiguration",
            "s3_destination_configuration": "s3DestinationConfiguration",
        },
    )
    class DatasetContentDeliveryRuleDestinationProperty:
        def __init__(
            self,
            *,
            iot_events_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.IotEventsDestinationConfigurationProperty"]] = None,
            s3_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.S3DestinationConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param iot_events_destination_configuration: ``CfnDataset.DatasetContentDeliveryRuleDestinationProperty.IotEventsDestinationConfiguration``.
            :param s3_destination_configuration: ``CfnDataset.DatasetContentDeliveryRuleDestinationProperty.S3DestinationConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if iot_events_destination_configuration is not None:
                self._values["iot_events_destination_configuration"] = iot_events_destination_configuration
            if s3_destination_configuration is not None:
                self._values["s3_destination_configuration"] = s3_destination_configuration

        @builtins.property
        def iot_events_destination_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.IotEventsDestinationConfigurationProperty"]]:
            '''``CfnDataset.DatasetContentDeliveryRuleDestinationProperty.IotEventsDestinationConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html#cfn-iotanalytics-dataset-datasetcontentdeliveryruledestination-ioteventsdestinationconfiguration
            '''
            result = self._values.get("iot_events_destination_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.IotEventsDestinationConfigurationProperty"]], result)

        @builtins.property
        def s3_destination_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.S3DestinationConfigurationProperty"]]:
            '''``CfnDataset.DatasetContentDeliveryRuleDestinationProperty.S3DestinationConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html#cfn-iotanalytics-dataset-datasetcontentdeliveryruledestination-s3destinationconfiguration
            '''
            result = self._values.get("s3_destination_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.S3DestinationConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetContentDeliveryRuleDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.DatasetContentDeliveryRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "entry_name": "entryName"},
    )
    class DatasetContentDeliveryRuleProperty:
        def __init__(
            self,
            *,
            destination: typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DatasetContentDeliveryRuleDestinationProperty"],
            entry_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param destination: ``CfnDataset.DatasetContentDeliveryRuleProperty.Destination``.
            :param entry_name: ``CfnDataset.DatasetContentDeliveryRuleProperty.EntryName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "destination": destination,
            }
            if entry_name is not None:
                self._values["entry_name"] = entry_name

        @builtins.property
        def destination(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DatasetContentDeliveryRuleDestinationProperty"]:
            '''``CfnDataset.DatasetContentDeliveryRuleProperty.Destination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html#cfn-iotanalytics-dataset-datasetcontentdeliveryrule-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DatasetContentDeliveryRuleDestinationProperty"], result)

        @builtins.property
        def entry_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataset.DatasetContentDeliveryRuleProperty.EntryName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html#cfn-iotanalytics-dataset-datasetcontentdeliveryrule-entryname
            '''
            result = self._values.get("entry_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetContentDeliveryRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.DatasetContentVersionValueProperty",
        jsii_struct_bases=[],
        name_mapping={"dataset_name": "datasetName"},
    )
    class DatasetContentVersionValueProperty:
        def __init__(
            self,
            *,
            dataset_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param dataset_name: ``CfnDataset.DatasetContentVersionValueProperty.DatasetName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable-datasetcontentversionvalue.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dataset_name is not None:
                self._values["dataset_name"] = dataset_name

        @builtins.property
        def dataset_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataset.DatasetContentVersionValueProperty.DatasetName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable-datasetcontentversionvalue.html#cfn-iotanalytics-dataset-variable-datasetcontentversionvalue-datasetname
            '''
            result = self._values.get("dataset_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetContentVersionValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.DeltaTimeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "offset_seconds": "offsetSeconds",
            "time_expression": "timeExpression",
        },
    )
    class DeltaTimeProperty:
        def __init__(
            self,
            *,
            offset_seconds: jsii.Number,
            time_expression: builtins.str,
        ) -> None:
            '''
            :param offset_seconds: ``CfnDataset.DeltaTimeProperty.OffsetSeconds``.
            :param time_expression: ``CfnDataset.DeltaTimeProperty.TimeExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "offset_seconds": offset_seconds,
                "time_expression": time_expression,
            }

        @builtins.property
        def offset_seconds(self) -> jsii.Number:
            '''``CfnDataset.DeltaTimeProperty.OffsetSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html#cfn-iotanalytics-dataset-deltatime-offsetseconds
            '''
            result = self._values.get("offset_seconds")
            assert result is not None, "Required property 'offset_seconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def time_expression(self) -> builtins.str:
            '''``CfnDataset.DeltaTimeProperty.TimeExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html#cfn-iotanalytics-dataset-deltatime-timeexpression
            '''
            result = self._values.get("time_expression")
            assert result is not None, "Required property 'time_expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeltaTimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.DeltaTimeSessionWindowConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"timeout_in_minutes": "timeoutInMinutes"},
    )
    class DeltaTimeSessionWindowConfigurationProperty:
        def __init__(self, *, timeout_in_minutes: jsii.Number) -> None:
            '''
            :param timeout_in_minutes: ``CfnDataset.DeltaTimeSessionWindowConfigurationProperty.TimeoutInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatimesessionwindowconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "timeout_in_minutes": timeout_in_minutes,
            }

        @builtins.property
        def timeout_in_minutes(self) -> jsii.Number:
            '''``CfnDataset.DeltaTimeSessionWindowConfigurationProperty.TimeoutInMinutes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatimesessionwindowconfiguration.html#cfn-iotanalytics-dataset-deltatimesessionwindowconfiguration-timeoutinminutes
            '''
            result = self._values.get("timeout_in_minutes")
            assert result is not None, "Required property 'timeout_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeltaTimeSessionWindowConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"delta_time": "deltaTime"},
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            delta_time: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DeltaTimeProperty"]] = None,
        ) -> None:
            '''
            :param delta_time: ``CfnDataset.FilterProperty.DeltaTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-filter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if delta_time is not None:
                self._values["delta_time"] = delta_time

        @builtins.property
        def delta_time(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DeltaTimeProperty"]]:
            '''``CfnDataset.FilterProperty.DeltaTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-filter.html#cfn-iotanalytics-dataset-filter-deltatime
            '''
            result = self._values.get("delta_time")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DeltaTimeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.GlueConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"database_name": "databaseName", "table_name": "tableName"},
    )
    class GlueConfigurationProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            table_name: builtins.str,
        ) -> None:
            '''
            :param database_name: ``CfnDataset.GlueConfigurationProperty.DatabaseName``.
            :param table_name: ``CfnDataset.GlueConfigurationProperty.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "database_name": database_name,
                "table_name": table_name,
            }

        @builtins.property
        def database_name(self) -> builtins.str:
            '''``CfnDataset.GlueConfigurationProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html#cfn-iotanalytics-dataset-glueconfiguration-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''``CfnDataset.GlueConfigurationProperty.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html#cfn-iotanalytics-dataset-glueconfiguration-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.IotEventsDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"input_name": "inputName", "role_arn": "roleArn"},
    )
    class IotEventsDestinationConfigurationProperty:
        def __init__(self, *, input_name: builtins.str, role_arn: builtins.str) -> None:
            '''
            :param input_name: ``CfnDataset.IotEventsDestinationConfigurationProperty.InputName``.
            :param role_arn: ``CfnDataset.IotEventsDestinationConfigurationProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "input_name": input_name,
                "role_arn": role_arn,
            }

        @builtins.property
        def input_name(self) -> builtins.str:
            '''``CfnDataset.IotEventsDestinationConfigurationProperty.InputName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html#cfn-iotanalytics-dataset-ioteventsdestinationconfiguration-inputname
            '''
            result = self._values.get("input_name")
            assert result is not None, "Required property 'input_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnDataset.IotEventsDestinationConfigurationProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html#cfn-iotanalytics-dataset-ioteventsdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotEventsDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.LateDataRuleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delta_time_session_window_configuration": "deltaTimeSessionWindowConfiguration",
        },
    )
    class LateDataRuleConfigurationProperty:
        def __init__(
            self,
            *,
            delta_time_session_window_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DeltaTimeSessionWindowConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param delta_time_session_window_configuration: ``CfnDataset.LateDataRuleConfigurationProperty.DeltaTimeSessionWindowConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedataruleconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if delta_time_session_window_configuration is not None:
                self._values["delta_time_session_window_configuration"] = delta_time_session_window_configuration

        @builtins.property
        def delta_time_session_window_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DeltaTimeSessionWindowConfigurationProperty"]]:
            '''``CfnDataset.LateDataRuleConfigurationProperty.DeltaTimeSessionWindowConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedataruleconfiguration.html#cfn-iotanalytics-dataset-latedataruleconfiguration-deltatimesessionwindowconfiguration
            '''
            result = self._values.get("delta_time_session_window_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DeltaTimeSessionWindowConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LateDataRuleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.LateDataRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rule_configuration": "ruleConfiguration",
            "rule_name": "ruleName",
        },
    )
    class LateDataRuleProperty:
        def __init__(
            self,
            *,
            rule_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnDataset.LateDataRuleConfigurationProperty"],
            rule_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param rule_configuration: ``CfnDataset.LateDataRuleProperty.RuleConfiguration``.
            :param rule_name: ``CfnDataset.LateDataRuleProperty.RuleName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "rule_configuration": rule_configuration,
            }
            if rule_name is not None:
                self._values["rule_name"] = rule_name

        @builtins.property
        def rule_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDataset.LateDataRuleConfigurationProperty"]:
            '''``CfnDataset.LateDataRuleProperty.RuleConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html#cfn-iotanalytics-dataset-latedatarule-ruleconfiguration
            '''
            result = self._values.get("rule_configuration")
            assert result is not None, "Required property 'rule_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDataset.LateDataRuleConfigurationProperty"], result)

        @builtins.property
        def rule_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataset.LateDataRuleProperty.RuleName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html#cfn-iotanalytics-dataset-latedatarule-rulename
            '''
            result = self._values.get("rule_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LateDataRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.OutputFileUriValueProperty",
        jsii_struct_bases=[],
        name_mapping={"file_name": "fileName"},
    )
    class OutputFileUriValueProperty:
        def __init__(self, *, file_name: typing.Optional[builtins.str] = None) -> None:
            '''
            :param file_name: ``CfnDataset.OutputFileUriValueProperty.FileName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable-outputfileurivalue.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if file_name is not None:
                self._values["file_name"] = file_name

        @builtins.property
        def file_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDataset.OutputFileUriValueProperty.FileName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable-outputfileurivalue.html#cfn-iotanalytics-dataset-variable-outputfileurivalue-filename
            '''
            result = self._values.get("file_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputFileUriValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.QueryActionProperty",
        jsii_struct_bases=[],
        name_mapping={"sql_query": "sqlQuery", "filters": "filters"},
    )
    class QueryActionProperty:
        def __init__(
            self,
            *,
            sql_query: builtins.str,
            filters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.FilterProperty"]]]] = None,
        ) -> None:
            '''
            :param sql_query: ``CfnDataset.QueryActionProperty.SqlQuery``.
            :param filters: ``CfnDataset.QueryActionProperty.Filters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "sql_query": sql_query,
            }
            if filters is not None:
                self._values["filters"] = filters

        @builtins.property
        def sql_query(self) -> builtins.str:
            '''``CfnDataset.QueryActionProperty.SqlQuery``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html#cfn-iotanalytics-dataset-queryaction-sqlquery
            '''
            result = self._values.get("sql_query")
            assert result is not None, "Required property 'sql_query' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def filters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.FilterProperty"]]]]:
            '''``CfnDataset.QueryActionProperty.Filters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html#cfn-iotanalytics-dataset-queryaction-filters
            '''
            result = self._values.get("filters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.FilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.ResourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compute_type": "computeType",
            "volume_size_in_gb": "volumeSizeInGb",
        },
    )
    class ResourceConfigurationProperty:
        def __init__(
            self,
            *,
            compute_type: builtins.str,
            volume_size_in_gb: jsii.Number,
        ) -> None:
            '''
            :param compute_type: ``CfnDataset.ResourceConfigurationProperty.ComputeType``.
            :param volume_size_in_gb: ``CfnDataset.ResourceConfigurationProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "compute_type": compute_type,
                "volume_size_in_gb": volume_size_in_gb,
            }

        @builtins.property
        def compute_type(self) -> builtins.str:
            '''``CfnDataset.ResourceConfigurationProperty.ComputeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html#cfn-iotanalytics-dataset-resourceconfiguration-computetype
            '''
            result = self._values.get("compute_type")
            assert result is not None, "Required property 'compute_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''``CfnDataset.ResourceConfigurationProperty.VolumeSizeInGB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html#cfn-iotanalytics-dataset-resourceconfiguration-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.RetentionPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"number_of_days": "numberOfDays", "unlimited": "unlimited"},
    )
    class RetentionPeriodProperty:
        def __init__(
            self,
            *,
            number_of_days: jsii.Number,
            unlimited: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        ) -> None:
            '''
            :param number_of_days: ``CfnDataset.RetentionPeriodProperty.NumberOfDays``.
            :param unlimited: ``CfnDataset.RetentionPeriodProperty.Unlimited``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "number_of_days": number_of_days,
                "unlimited": unlimited,
            }

        @builtins.property
        def number_of_days(self) -> jsii.Number:
            '''``CfnDataset.RetentionPeriodProperty.NumberOfDays``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html#cfn-iotanalytics-dataset-retentionperiod-numberofdays
            '''
            result = self._values.get("number_of_days")
            assert result is not None, "Required property 'number_of_days' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def unlimited(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnDataset.RetentionPeriodProperty.Unlimited``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html#cfn-iotanalytics-dataset-retentionperiod-unlimited
            '''
            result = self._values.get("unlimited")
            assert result is not None, "Required property 'unlimited' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetentionPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.S3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "key": "key",
            "role_arn": "roleArn",
            "glue_configuration": "glueConfiguration",
        },
    )
    class S3DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            role_arn: builtins.str,
            glue_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.GlueConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param bucket: ``CfnDataset.S3DestinationConfigurationProperty.Bucket``.
            :param key: ``CfnDataset.S3DestinationConfigurationProperty.Key``.
            :param role_arn: ``CfnDataset.S3DestinationConfigurationProperty.RoleArn``.
            :param glue_configuration: ``CfnDataset.S3DestinationConfigurationProperty.GlueConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
                "key": key,
                "role_arn": role_arn,
            }
            if glue_configuration is not None:
                self._values["glue_configuration"] = glue_configuration

        @builtins.property
        def bucket(self) -> builtins.str:
            '''``CfnDataset.S3DestinationConfigurationProperty.Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnDataset.S3DestinationConfigurationProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnDataset.S3DestinationConfigurationProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def glue_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.GlueConfigurationProperty"]]:
            '''``CfnDataset.S3DestinationConfigurationProperty.GlueConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-glueconfiguration
            '''
            result = self._values.get("glue_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.GlueConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule_expression": "scheduleExpression"},
    )
    class ScheduleProperty:
        def __init__(self, *, schedule_expression: builtins.str) -> None:
            '''
            :param schedule_expression: ``CfnDataset.ScheduleProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger-schedule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''``CfnDataset.ScheduleProperty.ScheduleExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger-schedule.html#cfn-iotanalytics-dataset-trigger-schedule-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.TriggerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule": "schedule",
            "triggering_dataset": "triggeringDataset",
        },
    )
    class TriggerProperty:
        def __init__(
            self,
            *,
            schedule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.ScheduleProperty"]] = None,
            triggering_dataset: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.TriggeringDatasetProperty"]] = None,
        ) -> None:
            '''
            :param schedule: ``CfnDataset.TriggerProperty.Schedule``.
            :param triggering_dataset: ``CfnDataset.TriggerProperty.TriggeringDataset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if schedule is not None:
                self._values["schedule"] = schedule
            if triggering_dataset is not None:
                self._values["triggering_dataset"] = triggering_dataset

        @builtins.property
        def schedule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.ScheduleProperty"]]:
            '''``CfnDataset.TriggerProperty.Schedule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html#cfn-iotanalytics-dataset-trigger-schedule
            '''
            result = self._values.get("schedule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.ScheduleProperty"]], result)

        @builtins.property
        def triggering_dataset(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.TriggeringDatasetProperty"]]:
            '''``CfnDataset.TriggerProperty.TriggeringDataset``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html#cfn-iotanalytics-dataset-trigger-triggeringdataset
            '''
            result = self._values.get("triggering_dataset")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.TriggeringDatasetProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.TriggeringDatasetProperty",
        jsii_struct_bases=[],
        name_mapping={"dataset_name": "datasetName"},
    )
    class TriggeringDatasetProperty:
        def __init__(self, *, dataset_name: builtins.str) -> None:
            '''
            :param dataset_name: ``CfnDataset.TriggeringDatasetProperty.DatasetName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-triggeringdataset.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "dataset_name": dataset_name,
            }

        @builtins.property
        def dataset_name(self) -> builtins.str:
            '''``CfnDataset.TriggeringDatasetProperty.DatasetName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-triggeringdataset.html#cfn-iotanalytics-dataset-triggeringdataset-datasetname
            '''
            result = self._values.get("dataset_name")
            assert result is not None, "Required property 'dataset_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggeringDatasetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.VariableProperty",
        jsii_struct_bases=[],
        name_mapping={
            "variable_name": "variableName",
            "dataset_content_version_value": "datasetContentVersionValue",
            "double_value": "doubleValue",
            "output_file_uri_value": "outputFileUriValue",
            "string_value": "stringValue",
        },
    )
    class VariableProperty:
        def __init__(
            self,
            *,
            variable_name: builtins.str,
            dataset_content_version_value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DatasetContentVersionValueProperty"]] = None,
            double_value: typing.Optional[jsii.Number] = None,
            output_file_uri_value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.OutputFileUriValueProperty"]] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param variable_name: ``CfnDataset.VariableProperty.VariableName``.
            :param dataset_content_version_value: ``CfnDataset.VariableProperty.DatasetContentVersionValue``.
            :param double_value: ``CfnDataset.VariableProperty.DoubleValue``.
            :param output_file_uri_value: ``CfnDataset.VariableProperty.OutputFileUriValue``.
            :param string_value: ``CfnDataset.VariableProperty.StringValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "variable_name": variable_name,
            }
            if dataset_content_version_value is not None:
                self._values["dataset_content_version_value"] = dataset_content_version_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if output_file_uri_value is not None:
                self._values["output_file_uri_value"] = output_file_uri_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def variable_name(self) -> builtins.str:
            '''``CfnDataset.VariableProperty.VariableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-variablename
            '''
            result = self._values.get("variable_name")
            assert result is not None, "Required property 'variable_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dataset_content_version_value(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DatasetContentVersionValueProperty"]]:
            '''``CfnDataset.VariableProperty.DatasetContentVersionValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-datasetcontentversionvalue
            '''
            result = self._values.get("dataset_content_version_value")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.DatasetContentVersionValueProperty"]], result)

        @builtins.property
        def double_value(self) -> typing.Optional[jsii.Number]:
            '''``CfnDataset.VariableProperty.DoubleValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def output_file_uri_value(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.OutputFileUriValueProperty"]]:
            '''``CfnDataset.VariableProperty.OutputFileUriValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-outputfileurivalue
            '''
            result = self._values.get("output_file_uri_value")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDataset.OutputFileUriValueProperty"]], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''``CfnDataset.VariableProperty.StringValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDataset.VersioningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"max_versions": "maxVersions", "unlimited": "unlimited"},
    )
    class VersioningConfigurationProperty:
        def __init__(
            self,
            *,
            max_versions: typing.Optional[jsii.Number] = None,
            unlimited: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param max_versions: ``CfnDataset.VersioningConfigurationProperty.MaxVersions``.
            :param unlimited: ``CfnDataset.VersioningConfigurationProperty.Unlimited``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if max_versions is not None:
                self._values["max_versions"] = max_versions
            if unlimited is not None:
                self._values["unlimited"] = unlimited

        @builtins.property
        def max_versions(self) -> typing.Optional[jsii.Number]:
            '''``CfnDataset.VersioningConfigurationProperty.MaxVersions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html#cfn-iotanalytics-dataset-versioningconfiguration-maxversions
            '''
            result = self._values.get("max_versions")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unlimited(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDataset.VersioningConfigurationProperty.Unlimited``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html#cfn-iotanalytics-dataset-versioningconfiguration-unlimited
            '''
            result = self._values.get("unlimited")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VersioningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotanalytics.CfnDatasetProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "content_delivery_rules": "contentDeliveryRules",
        "dataset_name": "datasetName",
        "late_data_rules": "lateDataRules",
        "retention_period": "retentionPeriod",
        "tags": "tags",
        "triggers": "triggers",
        "versioning_configuration": "versioningConfiguration",
    },
)
class CfnDatasetProps:
    def __init__(
        self,
        *,
        actions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnDataset.ActionProperty, aws_cdk.core.IResolvable]]],
        content_delivery_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDataset.DatasetContentDeliveryRuleProperty]]]] = None,
        dataset_name: typing.Optional[builtins.str] = None,
        late_data_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDataset.LateDataRuleProperty]]]] = None,
        retention_period: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataset.RetentionPeriodProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        triggers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnDataset.TriggerProperty]]]] = None,
        versioning_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataset.VersioningConfigurationProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTAnalytics::Dataset``.

        :param actions: ``AWS::IoTAnalytics::Dataset.Actions``.
        :param content_delivery_rules: ``AWS::IoTAnalytics::Dataset.ContentDeliveryRules``.
        :param dataset_name: ``AWS::IoTAnalytics::Dataset.DatasetName``.
        :param late_data_rules: ``AWS::IoTAnalytics::Dataset.LateDataRules``.
        :param retention_period: ``AWS::IoTAnalytics::Dataset.RetentionPeriod``.
        :param tags: ``AWS::IoTAnalytics::Dataset.Tags``.
        :param triggers: ``AWS::IoTAnalytics::Dataset.Triggers``.
        :param versioning_configuration: ``AWS::IoTAnalytics::Dataset.VersioningConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
        }
        if content_delivery_rules is not None:
            self._values["content_delivery_rules"] = content_delivery_rules
        if dataset_name is not None:
            self._values["dataset_name"] = dataset_name
        if late_data_rules is not None:
            self._values["late_data_rules"] = late_data_rules
        if retention_period is not None:
            self._values["retention_period"] = retention_period
        if tags is not None:
            self._values["tags"] = tags
        if triggers is not None:
            self._values["triggers"] = triggers
        if versioning_configuration is not None:
            self._values["versioning_configuration"] = versioning_configuration

    @builtins.property
    def actions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnDataset.ActionProperty, aws_cdk.core.IResolvable]]]:
        '''``AWS::IoTAnalytics::Dataset.Actions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-actions
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnDataset.ActionProperty, aws_cdk.core.IResolvable]]], result)

    @builtins.property
    def content_delivery_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataset.DatasetContentDeliveryRuleProperty]]]]:
        '''``AWS::IoTAnalytics::Dataset.ContentDeliveryRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-contentdeliveryrules
        '''
        result = self._values.get("content_delivery_rules")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataset.DatasetContentDeliveryRuleProperty]]]], result)

    @builtins.property
    def dataset_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTAnalytics::Dataset.DatasetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-datasetname
        '''
        result = self._values.get("dataset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def late_data_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataset.LateDataRuleProperty]]]]:
        '''``AWS::IoTAnalytics::Dataset.LateDataRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-latedatarules
        '''
        result = self._values.get("late_data_rules")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataset.LateDataRuleProperty]]]], result)

    @builtins.property
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataset.RetentionPeriodProperty]]:
        '''``AWS::IoTAnalytics::Dataset.RetentionPeriod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-retentionperiod
        '''
        result = self._values.get("retention_period")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataset.RetentionPeriodProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTAnalytics::Dataset.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def triggers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataset.TriggerProperty]]]]:
        '''``AWS::IoTAnalytics::Dataset.Triggers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-triggers
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnDataset.TriggerProperty]]]], result)

    @builtins.property
    def versioning_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataset.VersioningConfigurationProperty]]:
        '''``AWS::IoTAnalytics::Dataset.VersioningConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-versioningconfiguration
        '''
        result = self._values.get("versioning_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDataset.VersioningConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDatastore(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore",
):
    '''A CloudFormation ``AWS::IoTAnalytics::Datastore``.

    :cloudformationResource: AWS::IoTAnalytics::Datastore
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        datastore_name: typing.Optional[builtins.str] = None,
        datastore_partitions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastorePartitionsProperty"]] = None,
        datastore_storage: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastoreStorageProperty"]] = None,
        file_format_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.FileFormatConfigurationProperty"]] = None,
        retention_period: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.RetentionPeriodProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTAnalytics::Datastore``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param datastore_name: ``AWS::IoTAnalytics::Datastore.DatastoreName``.
        :param datastore_partitions: ``AWS::IoTAnalytics::Datastore.DatastorePartitions``.
        :param datastore_storage: ``AWS::IoTAnalytics::Datastore.DatastoreStorage``.
        :param file_format_configuration: ``AWS::IoTAnalytics::Datastore.FileFormatConfiguration``.
        :param retention_period: ``AWS::IoTAnalytics::Datastore.RetentionPeriod``.
        :param tags: ``AWS::IoTAnalytics::Datastore.Tags``.
        '''
        props = CfnDatastoreProps(
            datastore_name=datastore_name,
            datastore_partitions=datastore_partitions,
            datastore_storage=datastore_storage,
            file_format_configuration=file_format_configuration,
            retention_period=retention_period,
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
        '''``AWS::IoTAnalytics::Datastore.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datastoreName")
    def datastore_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTAnalytics::Datastore.DatastoreName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datastoreName"))

    @datastore_name.setter
    def datastore_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "datastoreName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datastorePartitions")
    def datastore_partitions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastorePartitionsProperty"]]:
        '''``AWS::IoTAnalytics::Datastore.DatastorePartitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorepartitions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastorePartitionsProperty"]], jsii.get(self, "datastorePartitions"))

    @datastore_partitions.setter
    def datastore_partitions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastorePartitionsProperty"]],
    ) -> None:
        jsii.set(self, "datastorePartitions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="datastoreStorage")
    def datastore_storage(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastoreStorageProperty"]]:
        '''``AWS::IoTAnalytics::Datastore.DatastoreStorage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorestorage
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastoreStorageProperty"]], jsii.get(self, "datastoreStorage"))

    @datastore_storage.setter
    def datastore_storage(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastoreStorageProperty"]],
    ) -> None:
        jsii.set(self, "datastoreStorage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fileFormatConfiguration")
    def file_format_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.FileFormatConfigurationProperty"]]:
        '''``AWS::IoTAnalytics::Datastore.FileFormatConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-fileformatconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.FileFormatConfigurationProperty"]], jsii.get(self, "fileFormatConfiguration"))

    @file_format_configuration.setter
    def file_format_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.FileFormatConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "fileFormatConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="retentionPeriod")
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.RetentionPeriodProperty"]]:
        '''``AWS::IoTAnalytics::Datastore.RetentionPeriod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-retentionperiod
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.RetentionPeriodProperty"]], jsii.get(self, "retentionPeriod"))

    @retention_period.setter
    def retention_period(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.RetentionPeriodProperty"]],
    ) -> None:
        jsii.set(self, "retentionPeriod", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.ColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "type": "type"},
    )
    class ColumnProperty:
        def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
            '''
            :param name: ``CfnDatastore.ColumnProperty.Name``.
            :param type: ``CfnDatastore.ColumnProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "type": type,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnDatastore.ColumnProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html#cfn-iotanalytics-datastore-column-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDatastore.ColumnProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html#cfn-iotanalytics-datastore-column-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
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
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.CustomerManagedS3Property",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "role_arn": "roleArn",
            "key_prefix": "keyPrefix",
        },
    )
    class CustomerManagedS3Property:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            role_arn: builtins.str,
            key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket: ``CfnDatastore.CustomerManagedS3Property.Bucket``.
            :param role_arn: ``CfnDatastore.CustomerManagedS3Property.RoleArn``.
            :param key_prefix: ``CfnDatastore.CustomerManagedS3Property.KeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
                "role_arn": role_arn,
            }
            if key_prefix is not None:
                self._values["key_prefix"] = key_prefix

        @builtins.property
        def bucket(self) -> builtins.str:
            '''``CfnDatastore.CustomerManagedS3Property.Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html#cfn-iotanalytics-datastore-customermanageds3-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnDatastore.CustomerManagedS3Property.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html#cfn-iotanalytics-datastore-customermanageds3-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnDatastore.CustomerManagedS3Property.KeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html#cfn-iotanalytics-datastore-customermanageds3-keyprefix
            '''
            result = self._values.get("key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedS3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.CustomerManagedS3StorageProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key_prefix": "keyPrefix"},
    )
    class CustomerManagedS3StorageProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket: ``CfnDatastore.CustomerManagedS3StorageProperty.Bucket``.
            :param key_prefix: ``CfnDatastore.CustomerManagedS3StorageProperty.KeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
            }
            if key_prefix is not None:
                self._values["key_prefix"] = key_prefix

        @builtins.property
        def bucket(self) -> builtins.str:
            '''``CfnDatastore.CustomerManagedS3StorageProperty.Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html#cfn-iotanalytics-datastore-customermanageds3storage-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnDatastore.CustomerManagedS3StorageProperty.KeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html#cfn-iotanalytics-datastore-customermanageds3storage-keyprefix
            '''
            result = self._values.get("key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedS3StorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.DatastorePartitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "partition": "partition",
            "timestamp_partition": "timestampPartition",
        },
    )
    class DatastorePartitionProperty:
        def __init__(
            self,
            *,
            partition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.PartitionProperty"]] = None,
            timestamp_partition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.TimestampPartitionProperty"]] = None,
        ) -> None:
            '''
            :param partition: ``CfnDatastore.DatastorePartitionProperty.Partition``.
            :param timestamp_partition: ``CfnDatastore.DatastorePartitionProperty.TimestampPartition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if partition is not None:
                self._values["partition"] = partition
            if timestamp_partition is not None:
                self._values["timestamp_partition"] = timestamp_partition

        @builtins.property
        def partition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.PartitionProperty"]]:
            '''``CfnDatastore.DatastorePartitionProperty.Partition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html#cfn-iotanalytics-datastore-datastorepartition-partition
            '''
            result = self._values.get("partition")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.PartitionProperty"]], result)

        @builtins.property
        def timestamp_partition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.TimestampPartitionProperty"]]:
            '''``CfnDatastore.DatastorePartitionProperty.TimestampPartition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html#cfn-iotanalytics-datastore-datastorepartition-timestamppartition
            '''
            result = self._values.get("timestamp_partition")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.TimestampPartitionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatastorePartitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.DatastorePartitionsProperty",
        jsii_struct_bases=[],
        name_mapping={"partitions": "partitions"},
    )
    class DatastorePartitionsProperty:
        def __init__(
            self,
            *,
            partitions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastorePartitionProperty"]]]] = None,
        ) -> None:
            '''
            :param partitions: ``CfnDatastore.DatastorePartitionsProperty.Partitions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if partitions is not None:
                self._values["partitions"] = partitions

        @builtins.property
        def partitions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastorePartitionProperty"]]]]:
            '''``CfnDatastore.DatastorePartitionsProperty.Partitions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html#cfn-iotanalytics-datastore-datastorepartitions-partitions
            '''
            result = self._values.get("partitions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.DatastorePartitionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatastorePartitionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.DatastoreStorageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_managed_s3": "customerManagedS3",
            "iot_site_wise_multi_layer_storage": "iotSiteWiseMultiLayerStorage",
            "service_managed_s3": "serviceManagedS3",
        },
    )
    class DatastoreStorageProperty:
        def __init__(
            self,
            *,
            customer_managed_s3: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.CustomerManagedS3Property"]] = None,
            iot_site_wise_multi_layer_storage: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.IotSiteWiseMultiLayerStorageProperty"]] = None,
            service_managed_s3: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.ServiceManagedS3Property"]] = None,
        ) -> None:
            '''
            :param customer_managed_s3: ``CfnDatastore.DatastoreStorageProperty.CustomerManagedS3``.
            :param iot_site_wise_multi_layer_storage: ``CfnDatastore.DatastoreStorageProperty.IotSiteWiseMultiLayerStorage``.
            :param service_managed_s3: ``CfnDatastore.DatastoreStorageProperty.ServiceManagedS3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if customer_managed_s3 is not None:
                self._values["customer_managed_s3"] = customer_managed_s3
            if iot_site_wise_multi_layer_storage is not None:
                self._values["iot_site_wise_multi_layer_storage"] = iot_site_wise_multi_layer_storage
            if service_managed_s3 is not None:
                self._values["service_managed_s3"] = service_managed_s3

        @builtins.property
        def customer_managed_s3(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.CustomerManagedS3Property"]]:
            '''``CfnDatastore.DatastoreStorageProperty.CustomerManagedS3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html#cfn-iotanalytics-datastore-datastorestorage-customermanageds3
            '''
            result = self._values.get("customer_managed_s3")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.CustomerManagedS3Property"]], result)

        @builtins.property
        def iot_site_wise_multi_layer_storage(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.IotSiteWiseMultiLayerStorageProperty"]]:
            '''``CfnDatastore.DatastoreStorageProperty.IotSiteWiseMultiLayerStorage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html#cfn-iotanalytics-datastore-datastorestorage-iotsitewisemultilayerstorage
            '''
            result = self._values.get("iot_site_wise_multi_layer_storage")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.IotSiteWiseMultiLayerStorageProperty"]], result)

        @builtins.property
        def service_managed_s3(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.ServiceManagedS3Property"]]:
            '''``CfnDatastore.DatastoreStorageProperty.ServiceManagedS3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html#cfn-iotanalytics-datastore-datastorestorage-servicemanageds3
            '''
            result = self._values.get("service_managed_s3")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.ServiceManagedS3Property"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatastoreStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.FileFormatConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "json_configuration": "jsonConfiguration",
            "parquet_configuration": "parquetConfiguration",
        },
    )
    class FileFormatConfigurationProperty:
        def __init__(
            self,
            *,
            json_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.JsonConfigurationProperty"]] = None,
            parquet_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.ParquetConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param json_configuration: ``CfnDatastore.FileFormatConfigurationProperty.JsonConfiguration``.
            :param parquet_configuration: ``CfnDatastore.FileFormatConfigurationProperty.ParquetConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if json_configuration is not None:
                self._values["json_configuration"] = json_configuration
            if parquet_configuration is not None:
                self._values["parquet_configuration"] = parquet_configuration

        @builtins.property
        def json_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.JsonConfigurationProperty"]]:
            '''``CfnDatastore.FileFormatConfigurationProperty.JsonConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html#cfn-iotanalytics-datastore-fileformatconfiguration-jsonconfiguration
            '''
            result = self._values.get("json_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.JsonConfigurationProperty"]], result)

        @builtins.property
        def parquet_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.ParquetConfigurationProperty"]]:
            '''``CfnDatastore.FileFormatConfigurationProperty.ParquetConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html#cfn-iotanalytics-datastore-fileformatconfiguration-parquetconfiguration
            '''
            result = self._values.get("parquet_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.ParquetConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileFormatConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.IotSiteWiseMultiLayerStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"customer_managed_s3_storage": "customerManagedS3Storage"},
    )
    class IotSiteWiseMultiLayerStorageProperty:
        def __init__(
            self,
            *,
            customer_managed_s3_storage: typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.CustomerManagedS3StorageProperty"],
        ) -> None:
            '''
            :param customer_managed_s3_storage: ``CfnDatastore.IotSiteWiseMultiLayerStorageProperty.CustomerManagedS3Storage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-iotsitewisemultilayerstorage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "customer_managed_s3_storage": customer_managed_s3_storage,
            }

        @builtins.property
        def customer_managed_s3_storage(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.CustomerManagedS3StorageProperty"]:
            '''``CfnDatastore.IotSiteWiseMultiLayerStorageProperty.CustomerManagedS3Storage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-iotsitewisemultilayerstorage.html#cfn-iotanalytics-datastore-iotsitewisemultilayerstorage-customermanageds3storage
            '''
            result = self._values.get("customer_managed_s3_storage")
            assert result is not None, "Required property 'customer_managed_s3_storage' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.CustomerManagedS3StorageProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotSiteWiseMultiLayerStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.JsonConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class JsonConfigurationProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-jsonconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.ParquetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"schema_definition": "schemaDefinition"},
    )
    class ParquetConfigurationProperty:
        def __init__(
            self,
            *,
            schema_definition: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.SchemaDefinitionProperty"]] = None,
        ) -> None:
            '''
            :param schema_definition: ``CfnDatastore.ParquetConfigurationProperty.SchemaDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-parquetconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if schema_definition is not None:
                self._values["schema_definition"] = schema_definition

        @builtins.property
        def schema_definition(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.SchemaDefinitionProperty"]]:
            '''``CfnDatastore.ParquetConfigurationProperty.SchemaDefinition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-parquetconfiguration.html#cfn-iotanalytics-datastore-parquetconfiguration-schemadefinition
            '''
            result = self._values.get("schema_definition")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.SchemaDefinitionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParquetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.PartitionProperty",
        jsii_struct_bases=[],
        name_mapping={"attribute_name": "attributeName"},
    )
    class PartitionProperty:
        def __init__(self, *, attribute_name: builtins.str) -> None:
            '''
            :param attribute_name: ``CfnDatastore.PartitionProperty.AttributeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "attribute_name": attribute_name,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''``CfnDatastore.PartitionProperty.AttributeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html#cfn-iotanalytics-datastore-partition-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PartitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.RetentionPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"number_of_days": "numberOfDays", "unlimited": "unlimited"},
    )
    class RetentionPeriodProperty:
        def __init__(
            self,
            *,
            number_of_days: typing.Optional[jsii.Number] = None,
            unlimited: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param number_of_days: ``CfnDatastore.RetentionPeriodProperty.NumberOfDays``.
            :param unlimited: ``CfnDatastore.RetentionPeriodProperty.Unlimited``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if number_of_days is not None:
                self._values["number_of_days"] = number_of_days
            if unlimited is not None:
                self._values["unlimited"] = unlimited

        @builtins.property
        def number_of_days(self) -> typing.Optional[jsii.Number]:
            '''``CfnDatastore.RetentionPeriodProperty.NumberOfDays``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html#cfn-iotanalytics-datastore-retentionperiod-numberofdays
            '''
            result = self._values.get("number_of_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unlimited(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDatastore.RetentionPeriodProperty.Unlimited``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html#cfn-iotanalytics-datastore-retentionperiod-unlimited
            '''
            result = self._values.get("unlimited")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetentionPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.SchemaDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"columns": "columns"},
    )
    class SchemaDefinitionProperty:
        def __init__(
            self,
            *,
            columns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.ColumnProperty"]]]] = None,
        ) -> None:
            '''
            :param columns: ``CfnDatastore.SchemaDefinitionProperty.Columns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-schemadefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if columns is not None:
                self._values["columns"] = columns

        @builtins.property
        def columns(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.ColumnProperty"]]]]:
            '''``CfnDatastore.SchemaDefinitionProperty.Columns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-schemadefinition.html#cfn-iotanalytics-datastore-schemadefinition-columns
            '''
            result = self._values.get("columns")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDatastore.ColumnProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.ServiceManagedS3Property",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class ServiceManagedS3Property:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-servicemanageds3.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceManagedS3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastore.TimestampPartitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_name": "attributeName",
            "timestamp_format": "timestampFormat",
        },
    )
    class TimestampPartitionProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            timestamp_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attribute_name: ``CfnDatastore.TimestampPartitionProperty.AttributeName``.
            :param timestamp_format: ``CfnDatastore.TimestampPartitionProperty.TimestampFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "attribute_name": attribute_name,
            }
            if timestamp_format is not None:
                self._values["timestamp_format"] = timestamp_format

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''``CfnDatastore.TimestampPartitionProperty.AttributeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html#cfn-iotanalytics-datastore-timestamppartition-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timestamp_format(self) -> typing.Optional[builtins.str]:
            '''``CfnDatastore.TimestampPartitionProperty.TimestampFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html#cfn-iotanalytics-datastore-timestamppartition-timestampformat
            '''
            result = self._values.get("timestamp_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestampPartitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotanalytics.CfnDatastoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "datastore_name": "datastoreName",
        "datastore_partitions": "datastorePartitions",
        "datastore_storage": "datastoreStorage",
        "file_format_configuration": "fileFormatConfiguration",
        "retention_period": "retentionPeriod",
        "tags": "tags",
    },
)
class CfnDatastoreProps:
    def __init__(
        self,
        *,
        datastore_name: typing.Optional[builtins.str] = None,
        datastore_partitions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.DatastorePartitionsProperty]] = None,
        datastore_storage: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.DatastoreStorageProperty]] = None,
        file_format_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.FileFormatConfigurationProperty]] = None,
        retention_period: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.RetentionPeriodProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTAnalytics::Datastore``.

        :param datastore_name: ``AWS::IoTAnalytics::Datastore.DatastoreName``.
        :param datastore_partitions: ``AWS::IoTAnalytics::Datastore.DatastorePartitions``.
        :param datastore_storage: ``AWS::IoTAnalytics::Datastore.DatastoreStorage``.
        :param file_format_configuration: ``AWS::IoTAnalytics::Datastore.FileFormatConfiguration``.
        :param retention_period: ``AWS::IoTAnalytics::Datastore.RetentionPeriod``.
        :param tags: ``AWS::IoTAnalytics::Datastore.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if datastore_name is not None:
            self._values["datastore_name"] = datastore_name
        if datastore_partitions is not None:
            self._values["datastore_partitions"] = datastore_partitions
        if datastore_storage is not None:
            self._values["datastore_storage"] = datastore_storage
        if file_format_configuration is not None:
            self._values["file_format_configuration"] = file_format_configuration
        if retention_period is not None:
            self._values["retention_period"] = retention_period
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def datastore_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTAnalytics::Datastore.DatastoreName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorename
        '''
        result = self._values.get("datastore_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datastore_partitions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.DatastorePartitionsProperty]]:
        '''``AWS::IoTAnalytics::Datastore.DatastorePartitions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorepartitions
        '''
        result = self._values.get("datastore_partitions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.DatastorePartitionsProperty]], result)

    @builtins.property
    def datastore_storage(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.DatastoreStorageProperty]]:
        '''``AWS::IoTAnalytics::Datastore.DatastoreStorage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorestorage
        '''
        result = self._values.get("datastore_storage")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.DatastoreStorageProperty]], result)

    @builtins.property
    def file_format_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.FileFormatConfigurationProperty]]:
        '''``AWS::IoTAnalytics::Datastore.FileFormatConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-fileformatconfiguration
        '''
        result = self._values.get("file_format_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.FileFormatConfigurationProperty]], result)

    @builtins.property
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.RetentionPeriodProperty]]:
        '''``AWS::IoTAnalytics::Datastore.RetentionPeriod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-retentionperiod
        '''
        result = self._values.get("retention_period")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDatastore.RetentionPeriodProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTAnalytics::Datastore.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatastoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPipeline(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline",
):
    '''A CloudFormation ``AWS::IoTAnalytics::Pipeline``.

    :cloudformationResource: AWS::IoTAnalytics::Pipeline
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        pipeline_activities: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.ActivityProperty"]]],
        pipeline_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTAnalytics::Pipeline``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param pipeline_activities: ``AWS::IoTAnalytics::Pipeline.PipelineActivities``.
        :param pipeline_name: ``AWS::IoTAnalytics::Pipeline.PipelineName``.
        :param tags: ``AWS::IoTAnalytics::Pipeline.Tags``.
        '''
        props = CfnPipelineProps(
            pipeline_activities=pipeline_activities,
            pipeline_name=pipeline_name,
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
        '''``AWS::IoTAnalytics::Pipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pipelineActivities")
    def pipeline_activities(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.ActivityProperty"]]]:
        '''``AWS::IoTAnalytics::Pipeline.PipelineActivities``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-pipelineactivities
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.ActivityProperty"]]], jsii.get(self, "pipelineActivities"))

    @pipeline_activities.setter
    def pipeline_activities(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.ActivityProperty"]]],
    ) -> None:
        jsii.set(self, "pipelineActivities", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pipelineName")
    def pipeline_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTAnalytics::Pipeline.PipelineName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-pipelinename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineName"))

    @pipeline_name.setter
    def pipeline_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "pipelineName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.ActivityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_attributes": "addAttributes",
            "channel": "channel",
            "datastore": "datastore",
            "device_registry_enrich": "deviceRegistryEnrich",
            "device_shadow_enrich": "deviceShadowEnrich",
            "filter": "filter",
            "lambda_": "lambda",
            "math": "math",
            "remove_attributes": "removeAttributes",
            "select_attributes": "selectAttributes",
        },
    )
    class ActivityProperty:
        def __init__(
            self,
            *,
            add_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.AddAttributesProperty"]] = None,
            channel: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.ChannelProperty"]] = None,
            datastore: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.DatastoreProperty"]] = None,
            device_registry_enrich: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.DeviceRegistryEnrichProperty"]] = None,
            device_shadow_enrich: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.DeviceShadowEnrichProperty"]] = None,
            filter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.FilterProperty"]] = None,
            lambda_: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.LambdaProperty"]] = None,
            math: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.MathProperty"]] = None,
            remove_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.RemoveAttributesProperty"]] = None,
            select_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.SelectAttributesProperty"]] = None,
        ) -> None:
            '''
            :param add_attributes: ``CfnPipeline.ActivityProperty.AddAttributes``.
            :param channel: ``CfnPipeline.ActivityProperty.Channel``.
            :param datastore: ``CfnPipeline.ActivityProperty.Datastore``.
            :param device_registry_enrich: ``CfnPipeline.ActivityProperty.DeviceRegistryEnrich``.
            :param device_shadow_enrich: ``CfnPipeline.ActivityProperty.DeviceShadowEnrich``.
            :param filter: ``CfnPipeline.ActivityProperty.Filter``.
            :param lambda_: ``CfnPipeline.ActivityProperty.Lambda``.
            :param math: ``CfnPipeline.ActivityProperty.Math``.
            :param remove_attributes: ``CfnPipeline.ActivityProperty.RemoveAttributes``.
            :param select_attributes: ``CfnPipeline.ActivityProperty.SelectAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if add_attributes is not None:
                self._values["add_attributes"] = add_attributes
            if channel is not None:
                self._values["channel"] = channel
            if datastore is not None:
                self._values["datastore"] = datastore
            if device_registry_enrich is not None:
                self._values["device_registry_enrich"] = device_registry_enrich
            if device_shadow_enrich is not None:
                self._values["device_shadow_enrich"] = device_shadow_enrich
            if filter is not None:
                self._values["filter"] = filter
            if lambda_ is not None:
                self._values["lambda_"] = lambda_
            if math is not None:
                self._values["math"] = math
            if remove_attributes is not None:
                self._values["remove_attributes"] = remove_attributes
            if select_attributes is not None:
                self._values["select_attributes"] = select_attributes

        @builtins.property
        def add_attributes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.AddAttributesProperty"]]:
            '''``CfnPipeline.ActivityProperty.AddAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-addattributes
            '''
            result = self._values.get("add_attributes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.AddAttributesProperty"]], result)

        @builtins.property
        def channel(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.ChannelProperty"]]:
            '''``CfnPipeline.ActivityProperty.Channel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-channel
            '''
            result = self._values.get("channel")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.ChannelProperty"]], result)

        @builtins.property
        def datastore(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.DatastoreProperty"]]:
            '''``CfnPipeline.ActivityProperty.Datastore``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-datastore
            '''
            result = self._values.get("datastore")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.DatastoreProperty"]], result)

        @builtins.property
        def device_registry_enrich(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.DeviceRegistryEnrichProperty"]]:
            '''``CfnPipeline.ActivityProperty.DeviceRegistryEnrich``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-deviceregistryenrich
            '''
            result = self._values.get("device_registry_enrich")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.DeviceRegistryEnrichProperty"]], result)

        @builtins.property
        def device_shadow_enrich(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.DeviceShadowEnrichProperty"]]:
            '''``CfnPipeline.ActivityProperty.DeviceShadowEnrich``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-deviceshadowenrich
            '''
            result = self._values.get("device_shadow_enrich")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.DeviceShadowEnrichProperty"]], result)

        @builtins.property
        def filter(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.FilterProperty"]]:
            '''``CfnPipeline.ActivityProperty.Filter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-filter
            '''
            result = self._values.get("filter")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.FilterProperty"]], result)

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.LambdaProperty"]]:
            '''``CfnPipeline.ActivityProperty.Lambda``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-lambda
            '''
            result = self._values.get("lambda_")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.LambdaProperty"]], result)

        @builtins.property
        def math(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.MathProperty"]]:
            '''``CfnPipeline.ActivityProperty.Math``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-math
            '''
            result = self._values.get("math")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.MathProperty"]], result)

        @builtins.property
        def remove_attributes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.RemoveAttributesProperty"]]:
            '''``CfnPipeline.ActivityProperty.RemoveAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-removeattributes
            '''
            result = self._values.get("remove_attributes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.RemoveAttributesProperty"]], result)

        @builtins.property
        def select_attributes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.SelectAttributesProperty"]]:
            '''``CfnPipeline.ActivityProperty.SelectAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-selectattributes
            '''
            result = self._values.get("select_attributes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPipeline.SelectAttributesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActivityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.AddAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "name": "name", "next": "next"},
    )
    class AddAttributesProperty:
        def __init__(
            self,
            *,
            attributes: typing.Any = None,
            name: typing.Optional[builtins.str] = None,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attributes: ``CfnPipeline.AddAttributesProperty.Attributes``.
            :param name: ``CfnPipeline.AddAttributesProperty.Name``.
            :param next: ``CfnPipeline.AddAttributesProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if name is not None:
                self._values["name"] = name
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def attributes(self) -> typing.Any:
            '''``CfnPipeline.AddAttributesProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html#cfn-iotanalytics-pipeline-addattributes-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Any, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.AddAttributesProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html#cfn-iotanalytics-pipeline-addattributes-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.AddAttributesProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html#cfn-iotanalytics-pipeline-addattributes-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.ChannelProperty",
        jsii_struct_bases=[],
        name_mapping={"channel_name": "channelName", "name": "name", "next": "next"},
    )
    class ChannelProperty:
        def __init__(
            self,
            *,
            channel_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param channel_name: ``CfnPipeline.ChannelProperty.ChannelName``.
            :param name: ``CfnPipeline.ChannelProperty.Name``.
            :param next: ``CfnPipeline.ChannelProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if channel_name is not None:
                self._values["channel_name"] = channel_name
            if name is not None:
                self._values["name"] = name
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def channel_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.ChannelProperty.ChannelName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html#cfn-iotanalytics-pipeline-channel-channelname
            '''
            result = self._values.get("channel_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.ChannelProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html#cfn-iotanalytics-pipeline-channel-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.ChannelProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html#cfn-iotanalytics-pipeline-channel-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.DatastoreProperty",
        jsii_struct_bases=[],
        name_mapping={"datastore_name": "datastoreName", "name": "name"},
    )
    class DatastoreProperty:
        def __init__(
            self,
            *,
            datastore_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param datastore_name: ``CfnPipeline.DatastoreProperty.DatastoreName``.
            :param name: ``CfnPipeline.DatastoreProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if datastore_name is not None:
                self._values["datastore_name"] = datastore_name
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def datastore_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DatastoreProperty.DatastoreName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html#cfn-iotanalytics-pipeline-datastore-datastorename
            '''
            result = self._values.get("datastore_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DatastoreProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html#cfn-iotanalytics-pipeline-datastore-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatastoreProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.DeviceRegistryEnrichProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute": "attribute",
            "name": "name",
            "next": "next",
            "role_arn": "roleArn",
            "thing_name": "thingName",
        },
    )
    class DeviceRegistryEnrichProperty:
        def __init__(
            self,
            *,
            attribute: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            next: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
            thing_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attribute: ``CfnPipeline.DeviceRegistryEnrichProperty.Attribute``.
            :param name: ``CfnPipeline.DeviceRegistryEnrichProperty.Name``.
            :param next: ``CfnPipeline.DeviceRegistryEnrichProperty.Next``.
            :param role_arn: ``CfnPipeline.DeviceRegistryEnrichProperty.RoleArn``.
            :param thing_name: ``CfnPipeline.DeviceRegistryEnrichProperty.ThingName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attribute is not None:
                self._values["attribute"] = attribute
            if name is not None:
                self._values["name"] = name
            if next is not None:
                self._values["next"] = next
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if thing_name is not None:
                self._values["thing_name"] = thing_name

        @builtins.property
        def attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DeviceRegistryEnrichProperty.Attribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-attribute
            '''
            result = self._values.get("attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DeviceRegistryEnrichProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DeviceRegistryEnrichProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DeviceRegistryEnrichProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def thing_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DeviceRegistryEnrichProperty.ThingName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-thingname
            '''
            result = self._values.get("thing_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceRegistryEnrichProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.DeviceShadowEnrichProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute": "attribute",
            "name": "name",
            "next": "next",
            "role_arn": "roleArn",
            "thing_name": "thingName",
        },
    )
    class DeviceShadowEnrichProperty:
        def __init__(
            self,
            *,
            attribute: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            next: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
            thing_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attribute: ``CfnPipeline.DeviceShadowEnrichProperty.Attribute``.
            :param name: ``CfnPipeline.DeviceShadowEnrichProperty.Name``.
            :param next: ``CfnPipeline.DeviceShadowEnrichProperty.Next``.
            :param role_arn: ``CfnPipeline.DeviceShadowEnrichProperty.RoleArn``.
            :param thing_name: ``CfnPipeline.DeviceShadowEnrichProperty.ThingName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attribute is not None:
                self._values["attribute"] = attribute
            if name is not None:
                self._values["name"] = name
            if next is not None:
                self._values["next"] = next
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if thing_name is not None:
                self._values["thing_name"] = thing_name

        @builtins.property
        def attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DeviceShadowEnrichProperty.Attribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-attribute
            '''
            result = self._values.get("attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DeviceShadowEnrichProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DeviceShadowEnrichProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DeviceShadowEnrichProperty.RoleArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def thing_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.DeviceShadowEnrichProperty.ThingName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-thingname
            '''
            result = self._values.get("thing_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceShadowEnrichProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"filter": "filter", "name": "name", "next": "next"},
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            filter: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param filter: ``CfnPipeline.FilterProperty.Filter``.
            :param name: ``CfnPipeline.FilterProperty.Name``.
            :param next: ``CfnPipeline.FilterProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if filter is not None:
                self._values["filter"] = filter
            if name is not None:
                self._values["name"] = name
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def filter(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.FilterProperty.Filter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html#cfn-iotanalytics-pipeline-filter-filter
            '''
            result = self._values.get("filter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.FilterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html#cfn-iotanalytics-pipeline-filter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.FilterProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html#cfn-iotanalytics-pipeline-filter-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.LambdaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "batch_size": "batchSize",
            "lambda_name": "lambdaName",
            "name": "name",
            "next": "next",
        },
    )
    class LambdaProperty:
        def __init__(
            self,
            *,
            batch_size: typing.Optional[jsii.Number] = None,
            lambda_name: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param batch_size: ``CfnPipeline.LambdaProperty.BatchSize``.
            :param lambda_name: ``CfnPipeline.LambdaProperty.LambdaName``.
            :param name: ``CfnPipeline.LambdaProperty.Name``.
            :param next: ``CfnPipeline.LambdaProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if lambda_name is not None:
                self._values["lambda_name"] = lambda_name
            if name is not None:
                self._values["name"] = name
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnPipeline.LambdaProperty.BatchSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lambda_name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.LambdaProperty.LambdaName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-lambdaname
            '''
            result = self._values.get("lambda_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.LambdaProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.LambdaProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.MathProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute": "attribute",
            "math": "math",
            "name": "name",
            "next": "next",
        },
    )
    class MathProperty:
        def __init__(
            self,
            *,
            attribute: typing.Optional[builtins.str] = None,
            math: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attribute: ``CfnPipeline.MathProperty.Attribute``.
            :param math: ``CfnPipeline.MathProperty.Math``.
            :param name: ``CfnPipeline.MathProperty.Name``.
            :param next: ``CfnPipeline.MathProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attribute is not None:
                self._values["attribute"] = attribute
            if math is not None:
                self._values["math"] = math
            if name is not None:
                self._values["name"] = name
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def attribute(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.MathProperty.Attribute``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-attribute
            '''
            result = self._values.get("attribute")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def math(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.MathProperty.Math``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-math
            '''
            result = self._values.get("math")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.MathProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.MathProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MathProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.RemoveAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "name": "name", "next": "next"},
    )
    class RemoveAttributesProperty:
        def __init__(
            self,
            *,
            attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
            name: typing.Optional[builtins.str] = None,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attributes: ``CfnPipeline.RemoveAttributesProperty.Attributes``.
            :param name: ``CfnPipeline.RemoveAttributesProperty.Name``.
            :param next: ``CfnPipeline.RemoveAttributesProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if name is not None:
                self._values["name"] = name
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def attributes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPipeline.RemoveAttributesProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html#cfn-iotanalytics-pipeline-removeattributes-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.RemoveAttributesProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html#cfn-iotanalytics-pipeline-removeattributes-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.RemoveAttributesProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html#cfn-iotanalytics-pipeline-removeattributes-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RemoveAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotanalytics.CfnPipeline.SelectAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "name": "name", "next": "next"},
    )
    class SelectAttributesProperty:
        def __init__(
            self,
            *,
            attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
            name: typing.Optional[builtins.str] = None,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param attributes: ``CfnPipeline.SelectAttributesProperty.Attributes``.
            :param name: ``CfnPipeline.SelectAttributesProperty.Name``.
            :param next: ``CfnPipeline.SelectAttributesProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if name is not None:
                self._values["name"] = name
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def attributes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPipeline.SelectAttributesProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html#cfn-iotanalytics-pipeline-selectattributes-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.SelectAttributesProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html#cfn-iotanalytics-pipeline-selectattributes-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''``CfnPipeline.SelectAttributesProperty.Next``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html#cfn-iotanalytics-pipeline-selectattributes-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelectAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotanalytics.CfnPipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "pipeline_activities": "pipelineActivities",
        "pipeline_name": "pipelineName",
        "tags": "tags",
    },
)
class CfnPipelineProps:
    def __init__(
        self,
        *,
        pipeline_activities: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnPipeline.ActivityProperty]]],
        pipeline_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTAnalytics::Pipeline``.

        :param pipeline_activities: ``AWS::IoTAnalytics::Pipeline.PipelineActivities``.
        :param pipeline_name: ``AWS::IoTAnalytics::Pipeline.PipelineName``.
        :param tags: ``AWS::IoTAnalytics::Pipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "pipeline_activities": pipeline_activities,
        }
        if pipeline_name is not None:
            self._values["pipeline_name"] = pipeline_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def pipeline_activities(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnPipeline.ActivityProperty]]]:
        '''``AWS::IoTAnalytics::Pipeline.PipelineActivities``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-pipelineactivities
        '''
        result = self._values.get("pipeline_activities")
        assert result is not None, "Required property 'pipeline_activities' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnPipeline.ActivityProperty]]], result)

    @builtins.property
    def pipeline_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTAnalytics::Pipeline.PipelineName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-pipelinename
        '''
        result = self._values.get("pipeline_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTAnalytics::Pipeline.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnChannel",
    "CfnChannelProps",
    "CfnDataset",
    "CfnDatasetProps",
    "CfnDatastore",
    "CfnDatastoreProps",
    "CfnPipeline",
    "CfnPipelineProps",
]

publication.publish()
