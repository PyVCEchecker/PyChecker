'''
# AWS::IoTEvents Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iotevents as iotevents
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
class CfnDetectorModel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel",
):
    '''A CloudFormation ``AWS::IoTEvents::DetectorModel``.

    :cloudformationResource: AWS::IoTEvents::DetectorModel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        detector_model_definition: typing.Union["CfnDetectorModel.DetectorModelDefinitionProperty", aws_cdk.core.IResolvable],
        role_arn: builtins.str,
        detector_model_description: typing.Optional[builtins.str] = None,
        detector_model_name: typing.Optional[builtins.str] = None,
        evaluation_method: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTEvents::DetectorModel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param detector_model_definition: ``AWS::IoTEvents::DetectorModel.DetectorModelDefinition``.
        :param role_arn: ``AWS::IoTEvents::DetectorModel.RoleArn``.
        :param detector_model_description: ``AWS::IoTEvents::DetectorModel.DetectorModelDescription``.
        :param detector_model_name: ``AWS::IoTEvents::DetectorModel.DetectorModelName``.
        :param evaluation_method: ``AWS::IoTEvents::DetectorModel.EvaluationMethod``.
        :param key: ``AWS::IoTEvents::DetectorModel.Key``.
        :param tags: ``AWS::IoTEvents::DetectorModel.Tags``.
        '''
        props = CfnDetectorModelProps(
            detector_model_definition=detector_model_definition,
            role_arn=role_arn,
            detector_model_description=detector_model_description,
            detector_model_name=detector_model_name,
            evaluation_method=evaluation_method,
            key=key,
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
        '''``AWS::IoTEvents::DetectorModel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorModelDefinition")
    def detector_model_definition(
        self,
    ) -> typing.Union["CfnDetectorModel.DetectorModelDefinitionProperty", aws_cdk.core.IResolvable]:
        '''``AWS::IoTEvents::DetectorModel.DetectorModelDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodeldefinition
        '''
        return typing.cast(typing.Union["CfnDetectorModel.DetectorModelDefinitionProperty", aws_cdk.core.IResolvable], jsii.get(self, "detectorModelDefinition"))

    @detector_model_definition.setter
    def detector_model_definition(
        self,
        value: typing.Union["CfnDetectorModel.DetectorModelDefinitionProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "detectorModelDefinition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::IoTEvents::DetectorModel.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorModelDescription")
    def detector_model_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::DetectorModel.DetectorModelDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodeldescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectorModelDescription"))

    @detector_model_description.setter
    def detector_model_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "detectorModelDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorModelName")
    def detector_model_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::DetectorModel.DetectorModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodelname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectorModelName"))

    @detector_model_name.setter
    def detector_model_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "detectorModelName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="evaluationMethod")
    def evaluation_method(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::DetectorModel.EvaluationMethod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-evaluationmethod
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationMethod"))

    @evaluation_method.setter
    def evaluation_method(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "evaluationMethod", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="key")
    def key(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::DetectorModel.Key``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-key
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "key"))

    @key.setter
    def key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "key", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "clear_timer": "clearTimer",
            "dynamo_db": "dynamoDb",
            "dynamo_d_bv2": "dynamoDBv2",
            "firehose": "firehose",
            "iot_events": "iotEvents",
            "iot_site_wise": "iotSiteWise",
            "iot_topic_publish": "iotTopicPublish",
            "lambda_": "lambda",
            "reset_timer": "resetTimer",
            "set_timer": "setTimer",
            "set_variable": "setVariable",
            "sns": "sns",
            "sqs": "sqs",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            clear_timer: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ClearTimerProperty"]] = None,
            dynamo_db: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.DynamoDBProperty"]] = None,
            dynamo_d_bv2: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.DynamoDBv2Property"]] = None,
            firehose: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.FirehoseProperty"]] = None,
            iot_events: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.IotEventsProperty"]] = None,
            iot_site_wise: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.IotSiteWiseProperty"]] = None,
            iot_topic_publish: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.IotTopicPublishProperty"]] = None,
            lambda_: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.LambdaProperty"]] = None,
            reset_timer: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ResetTimerProperty"]] = None,
            set_timer: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SetTimerProperty"]] = None,
            set_variable: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SetVariableProperty"]] = None,
            sns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SnsProperty"]] = None,
            sqs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SqsProperty"]] = None,
        ) -> None:
            '''
            :param clear_timer: ``CfnDetectorModel.ActionProperty.ClearTimer``.
            :param dynamo_db: ``CfnDetectorModel.ActionProperty.DynamoDB``.
            :param dynamo_d_bv2: ``CfnDetectorModel.ActionProperty.DynamoDBv2``.
            :param firehose: ``CfnDetectorModel.ActionProperty.Firehose``.
            :param iot_events: ``CfnDetectorModel.ActionProperty.IotEvents``.
            :param iot_site_wise: ``CfnDetectorModel.ActionProperty.IotSiteWise``.
            :param iot_topic_publish: ``CfnDetectorModel.ActionProperty.IotTopicPublish``.
            :param lambda_: ``CfnDetectorModel.ActionProperty.Lambda``.
            :param reset_timer: ``CfnDetectorModel.ActionProperty.ResetTimer``.
            :param set_timer: ``CfnDetectorModel.ActionProperty.SetTimer``.
            :param set_variable: ``CfnDetectorModel.ActionProperty.SetVariable``.
            :param sns: ``CfnDetectorModel.ActionProperty.Sns``.
            :param sqs: ``CfnDetectorModel.ActionProperty.Sqs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if clear_timer is not None:
                self._values["clear_timer"] = clear_timer
            if dynamo_db is not None:
                self._values["dynamo_db"] = dynamo_db
            if dynamo_d_bv2 is not None:
                self._values["dynamo_d_bv2"] = dynamo_d_bv2
            if firehose is not None:
                self._values["firehose"] = firehose
            if iot_events is not None:
                self._values["iot_events"] = iot_events
            if iot_site_wise is not None:
                self._values["iot_site_wise"] = iot_site_wise
            if iot_topic_publish is not None:
                self._values["iot_topic_publish"] = iot_topic_publish
            if lambda_ is not None:
                self._values["lambda_"] = lambda_
            if reset_timer is not None:
                self._values["reset_timer"] = reset_timer
            if set_timer is not None:
                self._values["set_timer"] = set_timer
            if set_variable is not None:
                self._values["set_variable"] = set_variable
            if sns is not None:
                self._values["sns"] = sns
            if sqs is not None:
                self._values["sqs"] = sqs

        @builtins.property
        def clear_timer(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ClearTimerProperty"]]:
            '''``CfnDetectorModel.ActionProperty.ClearTimer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-cleartimer
            '''
            result = self._values.get("clear_timer")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ClearTimerProperty"]], result)

        @builtins.property
        def dynamo_db(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.DynamoDBProperty"]]:
            '''``CfnDetectorModel.ActionProperty.DynamoDB``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-dynamodb
            '''
            result = self._values.get("dynamo_db")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.DynamoDBProperty"]], result)

        @builtins.property
        def dynamo_d_bv2(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.DynamoDBv2Property"]]:
            '''``CfnDetectorModel.ActionProperty.DynamoDBv2``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-dynamodbv2
            '''
            result = self._values.get("dynamo_d_bv2")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.DynamoDBv2Property"]], result)

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.FirehoseProperty"]]:
            '''``CfnDetectorModel.ActionProperty.Firehose``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-firehose
            '''
            result = self._values.get("firehose")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.FirehoseProperty"]], result)

        @builtins.property
        def iot_events(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.IotEventsProperty"]]:
            '''``CfnDetectorModel.ActionProperty.IotEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-iotevents
            '''
            result = self._values.get("iot_events")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.IotEventsProperty"]], result)

        @builtins.property
        def iot_site_wise(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.IotSiteWiseProperty"]]:
            '''``CfnDetectorModel.ActionProperty.IotSiteWise``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-iotsitewise
            '''
            result = self._values.get("iot_site_wise")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.IotSiteWiseProperty"]], result)

        @builtins.property
        def iot_topic_publish(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.IotTopicPublishProperty"]]:
            '''``CfnDetectorModel.ActionProperty.IotTopicPublish``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-iottopicpublish
            '''
            result = self._values.get("iot_topic_publish")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.IotTopicPublishProperty"]], result)

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.LambdaProperty"]]:
            '''``CfnDetectorModel.ActionProperty.Lambda``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-lambda
            '''
            result = self._values.get("lambda_")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.LambdaProperty"]], result)

        @builtins.property
        def reset_timer(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ResetTimerProperty"]]:
            '''``CfnDetectorModel.ActionProperty.ResetTimer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-resettimer
            '''
            result = self._values.get("reset_timer")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ResetTimerProperty"]], result)

        @builtins.property
        def set_timer(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SetTimerProperty"]]:
            '''``CfnDetectorModel.ActionProperty.SetTimer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-settimer
            '''
            result = self._values.get("set_timer")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SetTimerProperty"]], result)

        @builtins.property
        def set_variable(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SetVariableProperty"]]:
            '''``CfnDetectorModel.ActionProperty.SetVariable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-setvariable
            '''
            result = self._values.get("set_variable")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SetVariableProperty"]], result)

        @builtins.property
        def sns(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SnsProperty"]]:
            '''``CfnDetectorModel.ActionProperty.Sns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-sns
            '''
            result = self._values.get("sns")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SnsProperty"]], result)

        @builtins.property
        def sqs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SqsProperty"]]:
            '''``CfnDetectorModel.ActionProperty.Sqs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-action.html#cfn-iotevents-detectormodel-action-sqs
            '''
            result = self._values.get("sqs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.SqsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.AssetPropertyTimestampProperty",
        jsii_struct_bases=[],
        name_mapping={
            "time_in_seconds": "timeInSeconds",
            "offset_in_nanos": "offsetInNanos",
        },
    )
    class AssetPropertyTimestampProperty:
        def __init__(
            self,
            *,
            time_in_seconds: builtins.str,
            offset_in_nanos: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param time_in_seconds: ``CfnDetectorModel.AssetPropertyTimestampProperty.TimeInSeconds``.
            :param offset_in_nanos: ``CfnDetectorModel.AssetPropertyTimestampProperty.OffsetInNanos``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "time_in_seconds": time_in_seconds,
            }
            if offset_in_nanos is not None:
                self._values["offset_in_nanos"] = offset_in_nanos

        @builtins.property
        def time_in_seconds(self) -> builtins.str:
            '''``CfnDetectorModel.AssetPropertyTimestampProperty.TimeInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html#cfn-iotevents-detectormodel-assetpropertytimestamp-timeinseconds
            '''
            result = self._values.get("time_in_seconds")
            assert result is not None, "Required property 'time_in_seconds' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset_in_nanos(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.AssetPropertyTimestampProperty.OffsetInNanos``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertytimestamp.html#cfn-iotevents-detectormodel-assetpropertytimestamp-offsetinnanos
            '''
            result = self._values.get("offset_in_nanos")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyTimestampProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.AssetPropertyValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "value": "value",
            "quality": "quality",
            "timestamp": "timestamp",
        },
    )
    class AssetPropertyValueProperty:
        def __init__(
            self,
            *,
            value: typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.AssetPropertyVariantProperty"],
            quality: typing.Optional[builtins.str] = None,
            timestamp: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.AssetPropertyTimestampProperty"]] = None,
        ) -> None:
            '''
            :param value: ``CfnDetectorModel.AssetPropertyValueProperty.Value``.
            :param quality: ``CfnDetectorModel.AssetPropertyValueProperty.Quality``.
            :param timestamp: ``CfnDetectorModel.AssetPropertyValueProperty.Timestamp``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "value": value,
            }
            if quality is not None:
                self._values["quality"] = quality
            if timestamp is not None:
                self._values["timestamp"] = timestamp

        @builtins.property
        def value(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.AssetPropertyVariantProperty"]:
            '''``CfnDetectorModel.AssetPropertyValueProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html#cfn-iotevents-detectormodel-assetpropertyvalue-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.AssetPropertyVariantProperty"], result)

        @builtins.property
        def quality(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.AssetPropertyValueProperty.Quality``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html#cfn-iotevents-detectormodel-assetpropertyvalue-quality
            '''
            result = self._values.get("quality")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timestamp(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.AssetPropertyTimestampProperty"]]:
            '''``CfnDetectorModel.AssetPropertyValueProperty.Timestamp``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvalue.html#cfn-iotevents-detectormodel-assetpropertyvalue-timestamp
            '''
            result = self._values.get("timestamp")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.AssetPropertyTimestampProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.AssetPropertyVariantProperty",
        jsii_struct_bases=[],
        name_mapping={
            "boolean_value": "booleanValue",
            "double_value": "doubleValue",
            "integer_value": "integerValue",
            "string_value": "stringValue",
        },
    )
    class AssetPropertyVariantProperty:
        def __init__(
            self,
            *,
            boolean_value: typing.Optional[builtins.str] = None,
            double_value: typing.Optional[builtins.str] = None,
            integer_value: typing.Optional[builtins.str] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param boolean_value: ``CfnDetectorModel.AssetPropertyVariantProperty.BooleanValue``.
            :param double_value: ``CfnDetectorModel.AssetPropertyVariantProperty.DoubleValue``.
            :param integer_value: ``CfnDetectorModel.AssetPropertyVariantProperty.IntegerValue``.
            :param string_value: ``CfnDetectorModel.AssetPropertyVariantProperty.StringValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if boolean_value is not None:
                self._values["boolean_value"] = boolean_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if integer_value is not None:
                self._values["integer_value"] = integer_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def boolean_value(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.AssetPropertyVariantProperty.BooleanValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-booleanvalue
            '''
            result = self._values.get("boolean_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def double_value(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.AssetPropertyVariantProperty.DoubleValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def integer_value(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.AssetPropertyVariantProperty.IntegerValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-integervalue
            '''
            result = self._values.get("integer_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.AssetPropertyVariantProperty.StringValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-assetpropertyvariant.html#cfn-iotevents-detectormodel-assetpropertyvariant-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssetPropertyVariantProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.ClearTimerProperty",
        jsii_struct_bases=[],
        name_mapping={"timer_name": "timerName"},
    )
    class ClearTimerProperty:
        def __init__(self, *, timer_name: builtins.str) -> None:
            '''
            :param timer_name: ``CfnDetectorModel.ClearTimerProperty.TimerName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "timer_name": timer_name,
            }

        @builtins.property
        def timer_name(self) -> builtins.str:
            '''``CfnDetectorModel.ClearTimerProperty.TimerName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-cleartimer.html#cfn-iotevents-detectormodel-cleartimer-timername
            '''
            result = self._values.get("timer_name")
            assert result is not None, "Required property 'timer_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClearTimerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.DetectorModelDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"initial_state_name": "initialStateName", "states": "states"},
    )
    class DetectorModelDefinitionProperty:
        def __init__(
            self,
            *,
            initial_state_name: builtins.str,
            states: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.StateProperty"]]],
        ) -> None:
            '''
            :param initial_state_name: ``CfnDetectorModel.DetectorModelDefinitionProperty.InitialStateName``.
            :param states: ``CfnDetectorModel.DetectorModelDefinitionProperty.States``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "initial_state_name": initial_state_name,
                "states": states,
            }

        @builtins.property
        def initial_state_name(self) -> builtins.str:
            '''``CfnDetectorModel.DetectorModelDefinitionProperty.InitialStateName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html#cfn-iotevents-detectormodel-detectormodeldefinition-initialstatename
            '''
            result = self._values.get("initial_state_name")
            assert result is not None, "Required property 'initial_state_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def states(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.StateProperty"]]]:
            '''``CfnDetectorModel.DetectorModelDefinitionProperty.States``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-detectormodeldefinition.html#cfn-iotevents-detectormodel-detectormodeldefinition-states
            '''
            result = self._values.get("states")
            assert result is not None, "Required property 'states' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.StateProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DetectorModelDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.DynamoDBProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hash_key_field": "hashKeyField",
            "hash_key_value": "hashKeyValue",
            "table_name": "tableName",
            "hash_key_type": "hashKeyType",
            "operation": "operation",
            "payload": "payload",
            "payload_field": "payloadField",
            "range_key_field": "rangeKeyField",
            "range_key_type": "rangeKeyType",
            "range_key_value": "rangeKeyValue",
        },
    )
    class DynamoDBProperty:
        def __init__(
            self,
            *,
            hash_key_field: builtins.str,
            hash_key_value: builtins.str,
            table_name: builtins.str,
            hash_key_type: typing.Optional[builtins.str] = None,
            operation: typing.Optional[builtins.str] = None,
            payload: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]] = None,
            payload_field: typing.Optional[builtins.str] = None,
            range_key_field: typing.Optional[builtins.str] = None,
            range_key_type: typing.Optional[builtins.str] = None,
            range_key_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param hash_key_field: ``CfnDetectorModel.DynamoDBProperty.HashKeyField``.
            :param hash_key_value: ``CfnDetectorModel.DynamoDBProperty.HashKeyValue``.
            :param table_name: ``CfnDetectorModel.DynamoDBProperty.TableName``.
            :param hash_key_type: ``CfnDetectorModel.DynamoDBProperty.HashKeyType``.
            :param operation: ``CfnDetectorModel.DynamoDBProperty.Operation``.
            :param payload: ``CfnDetectorModel.DynamoDBProperty.Payload``.
            :param payload_field: ``CfnDetectorModel.DynamoDBProperty.PayloadField``.
            :param range_key_field: ``CfnDetectorModel.DynamoDBProperty.RangeKeyField``.
            :param range_key_type: ``CfnDetectorModel.DynamoDBProperty.RangeKeyType``.
            :param range_key_value: ``CfnDetectorModel.DynamoDBProperty.RangeKeyValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "hash_key_field": hash_key_field,
                "hash_key_value": hash_key_value,
                "table_name": table_name,
            }
            if hash_key_type is not None:
                self._values["hash_key_type"] = hash_key_type
            if operation is not None:
                self._values["operation"] = operation
            if payload is not None:
                self._values["payload"] = payload
            if payload_field is not None:
                self._values["payload_field"] = payload_field
            if range_key_field is not None:
                self._values["range_key_field"] = range_key_field
            if range_key_type is not None:
                self._values["range_key_type"] = range_key_type
            if range_key_value is not None:
                self._values["range_key_value"] = range_key_value

        @builtins.property
        def hash_key_field(self) -> builtins.str:
            '''``CfnDetectorModel.DynamoDBProperty.HashKeyField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-hashkeyfield
            '''
            result = self._values.get("hash_key_field")
            assert result is not None, "Required property 'hash_key_field' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hash_key_value(self) -> builtins.str:
            '''``CfnDetectorModel.DynamoDBProperty.HashKeyValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-hashkeyvalue
            '''
            result = self._values.get("hash_key_value")
            assert result is not None, "Required property 'hash_key_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''``CfnDetectorModel.DynamoDBProperty.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hash_key_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.DynamoDBProperty.HashKeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-hashkeytype
            '''
            result = self._values.get("hash_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operation(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.DynamoDBProperty.Operation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-operation
            '''
            result = self._values.get("operation")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]]:
            '''``CfnDetectorModel.DynamoDBProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]], result)

        @builtins.property
        def payload_field(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.DynamoDBProperty.PayloadField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-payloadfield
            '''
            result = self._values.get("payload_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_field(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.DynamoDBProperty.RangeKeyField``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-rangekeyfield
            '''
            result = self._values.get("range_key_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_type(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.DynamoDBProperty.RangeKeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-rangekeytype
            '''
            result = self._values.get("range_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range_key_value(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.DynamoDBProperty.RangeKeyValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodb.html#cfn-iotevents-detectormodel-dynamodb-rangekeyvalue
            '''
            result = self._values.get("range_key_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.DynamoDBv2Property",
        jsii_struct_bases=[],
        name_mapping={"table_name": "tableName", "payload": "payload"},
    )
    class DynamoDBv2Property:
        def __init__(
            self,
            *,
            table_name: builtins.str,
            payload: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]] = None,
        ) -> None:
            '''
            :param table_name: ``CfnDetectorModel.DynamoDBv2Property.TableName``.
            :param payload: ``CfnDetectorModel.DynamoDBv2Property.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "table_name": table_name,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def table_name(self) -> builtins.str:
            '''``CfnDetectorModel.DynamoDBv2Property.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html#cfn-iotevents-detectormodel-dynamodbv2-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]]:
            '''``CfnDetectorModel.DynamoDBv2Property.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-dynamodbv2.html#cfn-iotevents-detectormodel-dynamodbv2-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBv2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.EventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_name": "eventName",
            "actions": "actions",
            "condition": "condition",
        },
    )
    class EventProperty:
        def __init__(
            self,
            *,
            event_name: builtins.str,
            actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ActionProperty"]]]] = None,
            condition: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param event_name: ``CfnDetectorModel.EventProperty.EventName``.
            :param actions: ``CfnDetectorModel.EventProperty.Actions``.
            :param condition: ``CfnDetectorModel.EventProperty.Condition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "event_name": event_name,
            }
            if actions is not None:
                self._values["actions"] = actions
            if condition is not None:
                self._values["condition"] = condition

        @builtins.property
        def event_name(self) -> builtins.str:
            '''``CfnDetectorModel.EventProperty.EventName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html#cfn-iotevents-detectormodel-event-eventname
            '''
            result = self._values.get("event_name")
            assert result is not None, "Required property 'event_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def actions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ActionProperty"]]]]:
            '''``CfnDetectorModel.EventProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html#cfn-iotevents-detectormodel-event-actions
            '''
            result = self._values.get("actions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ActionProperty"]]]], result)

        @builtins.property
        def condition(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.EventProperty.Condition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-event.html#cfn-iotevents-detectormodel-event-condition
            '''
            result = self._values.get("condition")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.FirehoseProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_name": "deliveryStreamName",
            "payload": "payload",
            "separator": "separator",
        },
    )
    class FirehoseProperty:
        def __init__(
            self,
            *,
            delivery_stream_name: builtins.str,
            payload: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]] = None,
            separator: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param delivery_stream_name: ``CfnDetectorModel.FirehoseProperty.DeliveryStreamName``.
            :param payload: ``CfnDetectorModel.FirehoseProperty.Payload``.
            :param separator: ``CfnDetectorModel.FirehoseProperty.Separator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "delivery_stream_name": delivery_stream_name,
            }
            if payload is not None:
                self._values["payload"] = payload
            if separator is not None:
                self._values["separator"] = separator

        @builtins.property
        def delivery_stream_name(self) -> builtins.str:
            '''``CfnDetectorModel.FirehoseProperty.DeliveryStreamName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html#cfn-iotevents-detectormodel-firehose-deliverystreamname
            '''
            result = self._values.get("delivery_stream_name")
            assert result is not None, "Required property 'delivery_stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]]:
            '''``CfnDetectorModel.FirehoseProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html#cfn-iotevents-detectormodel-firehose-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]], result)

        @builtins.property
        def separator(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.FirehoseProperty.Separator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-firehose.html#cfn-iotevents-detectormodel-firehose-separator
            '''
            result = self._values.get("separator")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.IotEventsProperty",
        jsii_struct_bases=[],
        name_mapping={"input_name": "inputName", "payload": "payload"},
    )
    class IotEventsProperty:
        def __init__(
            self,
            *,
            input_name: builtins.str,
            payload: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]] = None,
        ) -> None:
            '''
            :param input_name: ``CfnDetectorModel.IotEventsProperty.InputName``.
            :param payload: ``CfnDetectorModel.IotEventsProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "input_name": input_name,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def input_name(self) -> builtins.str:
            '''``CfnDetectorModel.IotEventsProperty.InputName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html#cfn-iotevents-detectormodel-iotevents-inputname
            '''
            result = self._values.get("input_name")
            assert result is not None, "Required property 'input_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]]:
            '''``CfnDetectorModel.IotEventsProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotevents.html#cfn-iotevents-detectormodel-iotevents-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotEventsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.IotSiteWiseProperty",
        jsii_struct_bases=[],
        name_mapping={
            "property_value": "propertyValue",
            "asset_id": "assetId",
            "entry_id": "entryId",
            "property_alias": "propertyAlias",
            "property_id": "propertyId",
        },
    )
    class IotSiteWiseProperty:
        def __init__(
            self,
            *,
            property_value: typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.AssetPropertyValueProperty"],
            asset_id: typing.Optional[builtins.str] = None,
            entry_id: typing.Optional[builtins.str] = None,
            property_alias: typing.Optional[builtins.str] = None,
            property_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param property_value: ``CfnDetectorModel.IotSiteWiseProperty.PropertyValue``.
            :param asset_id: ``CfnDetectorModel.IotSiteWiseProperty.AssetId``.
            :param entry_id: ``CfnDetectorModel.IotSiteWiseProperty.EntryId``.
            :param property_alias: ``CfnDetectorModel.IotSiteWiseProperty.PropertyAlias``.
            :param property_id: ``CfnDetectorModel.IotSiteWiseProperty.PropertyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "property_value": property_value,
            }
            if asset_id is not None:
                self._values["asset_id"] = asset_id
            if entry_id is not None:
                self._values["entry_id"] = entry_id
            if property_alias is not None:
                self._values["property_alias"] = property_alias
            if property_id is not None:
                self._values["property_id"] = property_id

        @builtins.property
        def property_value(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.AssetPropertyValueProperty"]:
            '''``CfnDetectorModel.IotSiteWiseProperty.PropertyValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-propertyvalue
            '''
            result = self._values.get("property_value")
            assert result is not None, "Required property 'property_value' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.AssetPropertyValueProperty"], result)

        @builtins.property
        def asset_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.IotSiteWiseProperty.AssetId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-assetid
            '''
            result = self._values.get("asset_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entry_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.IotSiteWiseProperty.EntryId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-entryid
            '''
            result = self._values.get("entry_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_alias(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.IotSiteWiseProperty.PropertyAlias``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-propertyalias
            '''
            result = self._values.get("property_alias")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def property_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.IotSiteWiseProperty.PropertyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iotsitewise.html#cfn-iotevents-detectormodel-iotsitewise-propertyid
            '''
            result = self._values.get("property_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotSiteWiseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.IotTopicPublishProperty",
        jsii_struct_bases=[],
        name_mapping={"mqtt_topic": "mqttTopic", "payload": "payload"},
    )
    class IotTopicPublishProperty:
        def __init__(
            self,
            *,
            mqtt_topic: builtins.str,
            payload: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]] = None,
        ) -> None:
            '''
            :param mqtt_topic: ``CfnDetectorModel.IotTopicPublishProperty.MqttTopic``.
            :param payload: ``CfnDetectorModel.IotTopicPublishProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "mqtt_topic": mqtt_topic,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def mqtt_topic(self) -> builtins.str:
            '''``CfnDetectorModel.IotTopicPublishProperty.MqttTopic``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html#cfn-iotevents-detectormodel-iottopicpublish-mqtttopic
            '''
            result = self._values.get("mqtt_topic")
            assert result is not None, "Required property 'mqtt_topic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]]:
            '''``CfnDetectorModel.IotTopicPublishProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-iottopicpublish.html#cfn-iotevents-detectormodel-iottopicpublish-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotTopicPublishProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.LambdaProperty",
        jsii_struct_bases=[],
        name_mapping={"function_arn": "functionArn", "payload": "payload"},
    )
    class LambdaProperty:
        def __init__(
            self,
            *,
            function_arn: builtins.str,
            payload: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]] = None,
        ) -> None:
            '''
            :param function_arn: ``CfnDetectorModel.LambdaProperty.FunctionArn``.
            :param payload: ``CfnDetectorModel.LambdaProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "function_arn": function_arn,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def function_arn(self) -> builtins.str:
            '''``CfnDetectorModel.LambdaProperty.FunctionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html#cfn-iotevents-detectormodel-lambda-functionarn
            '''
            result = self._values.get("function_arn")
            assert result is not None, "Required property 'function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]]:
            '''``CfnDetectorModel.LambdaProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-lambda.html#cfn-iotevents-detectormodel-lambda-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.OnEnterProperty",
        jsii_struct_bases=[],
        name_mapping={"events": "events"},
    )
    class OnEnterProperty:
        def __init__(
            self,
            *,
            events: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.EventProperty"]]]] = None,
        ) -> None:
            '''
            :param events: ``CfnDetectorModel.OnEnterProperty.Events``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if events is not None:
                self._values["events"] = events

        @builtins.property
        def events(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.EventProperty"]]]]:
            '''``CfnDetectorModel.OnEnterProperty.Events``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onenter.html#cfn-iotevents-detectormodel-onenter-events
            '''
            result = self._values.get("events")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.EventProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnEnterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.OnExitProperty",
        jsii_struct_bases=[],
        name_mapping={"events": "events"},
    )
    class OnExitProperty:
        def __init__(
            self,
            *,
            events: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.EventProperty"]]]] = None,
        ) -> None:
            '''
            :param events: ``CfnDetectorModel.OnExitProperty.Events``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if events is not None:
                self._values["events"] = events

        @builtins.property
        def events(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.EventProperty"]]]]:
            '''``CfnDetectorModel.OnExitProperty.Events``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-onexit.html#cfn-iotevents-detectormodel-onexit-events
            '''
            result = self._values.get("events")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.EventProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnExitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.OnInputProperty",
        jsii_struct_bases=[],
        name_mapping={"events": "events", "transition_events": "transitionEvents"},
    )
    class OnInputProperty:
        def __init__(
            self,
            *,
            events: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.EventProperty"]]]] = None,
            transition_events: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.TransitionEventProperty"]]]] = None,
        ) -> None:
            '''
            :param events: ``CfnDetectorModel.OnInputProperty.Events``.
            :param transition_events: ``CfnDetectorModel.OnInputProperty.TransitionEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if events is not None:
                self._values["events"] = events
            if transition_events is not None:
                self._values["transition_events"] = transition_events

        @builtins.property
        def events(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.EventProperty"]]]]:
            '''``CfnDetectorModel.OnInputProperty.Events``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html#cfn-iotevents-detectormodel-oninput-events
            '''
            result = self._values.get("events")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.EventProperty"]]]], result)

        @builtins.property
        def transition_events(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.TransitionEventProperty"]]]]:
            '''``CfnDetectorModel.OnInputProperty.TransitionEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-oninput.html#cfn-iotevents-detectormodel-oninput-transitionevents
            '''
            result = self._values.get("transition_events")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.TransitionEventProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.PayloadProperty",
        jsii_struct_bases=[],
        name_mapping={"content_expression": "contentExpression", "type": "type"},
    )
    class PayloadProperty:
        def __init__(
            self,
            *,
            content_expression: builtins.str,
            type: builtins.str,
        ) -> None:
            '''
            :param content_expression: ``CfnDetectorModel.PayloadProperty.ContentExpression``.
            :param type: ``CfnDetectorModel.PayloadProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "content_expression": content_expression,
                "type": type,
            }

        @builtins.property
        def content_expression(self) -> builtins.str:
            '''``CfnDetectorModel.PayloadProperty.ContentExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html#cfn-iotevents-detectormodel-payload-contentexpression
            '''
            result = self._values.get("content_expression")
            assert result is not None, "Required property 'content_expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDetectorModel.PayloadProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-payload.html#cfn-iotevents-detectormodel-payload-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PayloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.ResetTimerProperty",
        jsii_struct_bases=[],
        name_mapping={"timer_name": "timerName"},
    )
    class ResetTimerProperty:
        def __init__(self, *, timer_name: builtins.str) -> None:
            '''
            :param timer_name: ``CfnDetectorModel.ResetTimerProperty.TimerName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "timer_name": timer_name,
            }

        @builtins.property
        def timer_name(self) -> builtins.str:
            '''``CfnDetectorModel.ResetTimerProperty.TimerName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-resettimer.html#cfn-iotevents-detectormodel-resettimer-timername
            '''
            result = self._values.get("timer_name")
            assert result is not None, "Required property 'timer_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResetTimerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.SetTimerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "timer_name": "timerName",
            "duration_expression": "durationExpression",
            "seconds": "seconds",
        },
    )
    class SetTimerProperty:
        def __init__(
            self,
            *,
            timer_name: builtins.str,
            duration_expression: typing.Optional[builtins.str] = None,
            seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param timer_name: ``CfnDetectorModel.SetTimerProperty.TimerName``.
            :param duration_expression: ``CfnDetectorModel.SetTimerProperty.DurationExpression``.
            :param seconds: ``CfnDetectorModel.SetTimerProperty.Seconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "timer_name": timer_name,
            }
            if duration_expression is not None:
                self._values["duration_expression"] = duration_expression
            if seconds is not None:
                self._values["seconds"] = seconds

        @builtins.property
        def timer_name(self) -> builtins.str:
            '''``CfnDetectorModel.SetTimerProperty.TimerName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html#cfn-iotevents-detectormodel-settimer-timername
            '''
            result = self._values.get("timer_name")
            assert result is not None, "Required property 'timer_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def duration_expression(self) -> typing.Optional[builtins.str]:
            '''``CfnDetectorModel.SetTimerProperty.DurationExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html#cfn-iotevents-detectormodel-settimer-durationexpression
            '''
            result = self._values.get("duration_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnDetectorModel.SetTimerProperty.Seconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-settimer.html#cfn-iotevents-detectormodel-settimer-seconds
            '''
            result = self._values.get("seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SetTimerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.SetVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "variable_name": "variableName"},
    )
    class SetVariableProperty:
        def __init__(self, *, value: builtins.str, variable_name: builtins.str) -> None:
            '''
            :param value: ``CfnDetectorModel.SetVariableProperty.Value``.
            :param variable_name: ``CfnDetectorModel.SetVariableProperty.VariableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "value": value,
                "variable_name": variable_name,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnDetectorModel.SetVariableProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html#cfn-iotevents-detectormodel-setvariable-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variable_name(self) -> builtins.str:
            '''``CfnDetectorModel.SetVariableProperty.VariableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-setvariable.html#cfn-iotevents-detectormodel-setvariable-variablename
            '''
            result = self._values.get("variable_name")
            assert result is not None, "Required property 'variable_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SetVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.SnsProperty",
        jsii_struct_bases=[],
        name_mapping={"target_arn": "targetArn", "payload": "payload"},
    )
    class SnsProperty:
        def __init__(
            self,
            *,
            target_arn: builtins.str,
            payload: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]] = None,
        ) -> None:
            '''
            :param target_arn: ``CfnDetectorModel.SnsProperty.TargetArn``.
            :param payload: ``CfnDetectorModel.SnsProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "target_arn": target_arn,
            }
            if payload is not None:
                self._values["payload"] = payload

        @builtins.property
        def target_arn(self) -> builtins.str:
            '''``CfnDetectorModel.SnsProperty.TargetArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html#cfn-iotevents-detectormodel-sns-targetarn
            '''
            result = self._values.get("target_arn")
            assert result is not None, "Required property 'target_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]]:
            '''``CfnDetectorModel.SnsProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sns.html#cfn-iotevents-detectormodel-sns-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.SqsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "queue_url": "queueUrl",
            "payload": "payload",
            "use_base64": "useBase64",
        },
    )
    class SqsProperty:
        def __init__(
            self,
            *,
            queue_url: builtins.str,
            payload: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]] = None,
            use_base64: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param queue_url: ``CfnDetectorModel.SqsProperty.QueueUrl``.
            :param payload: ``CfnDetectorModel.SqsProperty.Payload``.
            :param use_base64: ``CfnDetectorModel.SqsProperty.UseBase64``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "queue_url": queue_url,
            }
            if payload is not None:
                self._values["payload"] = payload
            if use_base64 is not None:
                self._values["use_base64"] = use_base64

        @builtins.property
        def queue_url(self) -> builtins.str:
            '''``CfnDetectorModel.SqsProperty.QueueUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html#cfn-iotevents-detectormodel-sqs-queueurl
            '''
            result = self._values.get("queue_url")
            assert result is not None, "Required property 'queue_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def payload(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]]:
            '''``CfnDetectorModel.SqsProperty.Payload``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html#cfn-iotevents-detectormodel-sqs-payload
            '''
            result = self._values.get("payload")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.PayloadProperty"]], result)

        @builtins.property
        def use_base64(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDetectorModel.SqsProperty.UseBase64``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-sqs.html#cfn-iotevents-detectormodel-sqs-usebase64
            '''
            result = self._values.get("use_base64")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.StateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "state_name": "stateName",
            "on_enter": "onEnter",
            "on_exit": "onExit",
            "on_input": "onInput",
        },
    )
    class StateProperty:
        def __init__(
            self,
            *,
            state_name: builtins.str,
            on_enter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.OnEnterProperty"]] = None,
            on_exit: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.OnExitProperty"]] = None,
            on_input: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.OnInputProperty"]] = None,
        ) -> None:
            '''
            :param state_name: ``CfnDetectorModel.StateProperty.StateName``.
            :param on_enter: ``CfnDetectorModel.StateProperty.OnEnter``.
            :param on_exit: ``CfnDetectorModel.StateProperty.OnExit``.
            :param on_input: ``CfnDetectorModel.StateProperty.OnInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "state_name": state_name,
            }
            if on_enter is not None:
                self._values["on_enter"] = on_enter
            if on_exit is not None:
                self._values["on_exit"] = on_exit
            if on_input is not None:
                self._values["on_input"] = on_input

        @builtins.property
        def state_name(self) -> builtins.str:
            '''``CfnDetectorModel.StateProperty.StateName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-statename
            '''
            result = self._values.get("state_name")
            assert result is not None, "Required property 'state_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def on_enter(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.OnEnterProperty"]]:
            '''``CfnDetectorModel.StateProperty.OnEnter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-onenter
            '''
            result = self._values.get("on_enter")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.OnEnterProperty"]], result)

        @builtins.property
        def on_exit(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.OnExitProperty"]]:
            '''``CfnDetectorModel.StateProperty.OnExit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-onexit
            '''
            result = self._values.get("on_exit")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.OnExitProperty"]], result)

        @builtins.property
        def on_input(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.OnInputProperty"]]:
            '''``CfnDetectorModel.StateProperty.OnInput``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-state.html#cfn-iotevents-detectormodel-state-oninput
            '''
            result = self._values.get("on_input")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.OnInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModel.TransitionEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition": "condition",
            "event_name": "eventName",
            "next_state": "nextState",
            "actions": "actions",
        },
    )
    class TransitionEventProperty:
        def __init__(
            self,
            *,
            condition: builtins.str,
            event_name: builtins.str,
            next_state: builtins.str,
            actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ActionProperty"]]]] = None,
        ) -> None:
            '''
            :param condition: ``CfnDetectorModel.TransitionEventProperty.Condition``.
            :param event_name: ``CfnDetectorModel.TransitionEventProperty.EventName``.
            :param next_state: ``CfnDetectorModel.TransitionEventProperty.NextState``.
            :param actions: ``CfnDetectorModel.TransitionEventProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "condition": condition,
                "event_name": event_name,
                "next_state": next_state,
            }
            if actions is not None:
                self._values["actions"] = actions

        @builtins.property
        def condition(self) -> builtins.str:
            '''``CfnDetectorModel.TransitionEventProperty.Condition``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-condition
            '''
            result = self._values.get("condition")
            assert result is not None, "Required property 'condition' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def event_name(self) -> builtins.str:
            '''``CfnDetectorModel.TransitionEventProperty.EventName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-eventname
            '''
            result = self._values.get("event_name")
            assert result is not None, "Required property 'event_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next_state(self) -> builtins.str:
            '''``CfnDetectorModel.TransitionEventProperty.NextState``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-nextstate
            '''
            result = self._values.get("next_state")
            assert result is not None, "Required property 'next_state' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def actions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ActionProperty"]]]]:
            '''``CfnDetectorModel.TransitionEventProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-detectormodel-transitionevent.html#cfn-iotevents-detectormodel-transitionevent-actions
            '''
            result = self._values.get("actions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDetectorModel.ActionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransitionEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotevents.CfnDetectorModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "detector_model_definition": "detectorModelDefinition",
        "role_arn": "roleArn",
        "detector_model_description": "detectorModelDescription",
        "detector_model_name": "detectorModelName",
        "evaluation_method": "evaluationMethod",
        "key": "key",
        "tags": "tags",
    },
)
class CfnDetectorModelProps:
    def __init__(
        self,
        *,
        detector_model_definition: typing.Union[CfnDetectorModel.DetectorModelDefinitionProperty, aws_cdk.core.IResolvable],
        role_arn: builtins.str,
        detector_model_description: typing.Optional[builtins.str] = None,
        detector_model_name: typing.Optional[builtins.str] = None,
        evaluation_method: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTEvents::DetectorModel``.

        :param detector_model_definition: ``AWS::IoTEvents::DetectorModel.DetectorModelDefinition``.
        :param role_arn: ``AWS::IoTEvents::DetectorModel.RoleArn``.
        :param detector_model_description: ``AWS::IoTEvents::DetectorModel.DetectorModelDescription``.
        :param detector_model_name: ``AWS::IoTEvents::DetectorModel.DetectorModelName``.
        :param evaluation_method: ``AWS::IoTEvents::DetectorModel.EvaluationMethod``.
        :param key: ``AWS::IoTEvents::DetectorModel.Key``.
        :param tags: ``AWS::IoTEvents::DetectorModel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "detector_model_definition": detector_model_definition,
            "role_arn": role_arn,
        }
        if detector_model_description is not None:
            self._values["detector_model_description"] = detector_model_description
        if detector_model_name is not None:
            self._values["detector_model_name"] = detector_model_name
        if evaluation_method is not None:
            self._values["evaluation_method"] = evaluation_method
        if key is not None:
            self._values["key"] = key
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def detector_model_definition(
        self,
    ) -> typing.Union[CfnDetectorModel.DetectorModelDefinitionProperty, aws_cdk.core.IResolvable]:
        '''``AWS::IoTEvents::DetectorModel.DetectorModelDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodeldefinition
        '''
        result = self._values.get("detector_model_definition")
        assert result is not None, "Required property 'detector_model_definition' is missing"
        return typing.cast(typing.Union[CfnDetectorModel.DetectorModelDefinitionProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::IoTEvents::DetectorModel.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def detector_model_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::DetectorModel.DetectorModelDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodeldescription
        '''
        result = self._values.get("detector_model_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def detector_model_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::DetectorModel.DetectorModelName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-detectormodelname
        '''
        result = self._values.get("detector_model_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluation_method(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::DetectorModel.EvaluationMethod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-evaluationmethod
        '''
        result = self._values.get("evaluation_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::DetectorModel.Key``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-key
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTEvents::DetectorModel.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html#cfn-iotevents-detectormodel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDetectorModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnInput(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-iotevents.CfnInput",
):
    '''A CloudFormation ``AWS::IoTEvents::Input``.

    :cloudformationResource: AWS::IoTEvents::Input
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        input_definition: typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDefinitionProperty"],
        input_description: typing.Optional[builtins.str] = None,
        input_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::IoTEvents::Input``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param input_definition: ``AWS::IoTEvents::Input.InputDefinition``.
        :param input_description: ``AWS::IoTEvents::Input.InputDescription``.
        :param input_name: ``AWS::IoTEvents::Input.InputName``.
        :param tags: ``AWS::IoTEvents::Input.Tags``.
        '''
        props = CfnInputProps(
            input_definition=input_definition,
            input_description=input_description,
            input_name=input_name,
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
        '''``AWS::IoTEvents::Input.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inputDefinition")
    def input_definition(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDefinitionProperty"]:
        '''``AWS::IoTEvents::Input.InputDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputdefinition
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDefinitionProperty"], jsii.get(self, "inputDefinition"))

    @input_definition.setter
    def input_definition(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnInput.InputDefinitionProperty"],
    ) -> None:
        jsii.set(self, "inputDefinition", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inputDescription")
    def input_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::Input.InputDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputDescription"))

    @input_description.setter
    def input_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "inputDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inputName")
    def input_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::Input.InputName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputName"))

    @input_name.setter
    def input_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "inputName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnInput.AttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"json_path": "jsonPath"},
    )
    class AttributeProperty:
        def __init__(self, *, json_path: builtins.str) -> None:
            '''
            :param json_path: ``CfnInput.AttributeProperty.JsonPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "json_path": json_path,
            }

        @builtins.property
        def json_path(self) -> builtins.str:
            '''``CfnInput.AttributeProperty.JsonPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-attribute.html#cfn-iotevents-input-attribute-jsonpath
            '''
            result = self._values.get("json_path")
            assert result is not None, "Required property 'json_path' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-iotevents.CfnInput.InputDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes"},
    )
    class InputDefinitionProperty:
        def __init__(
            self,
            *,
            attributes: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInput.AttributeProperty"]]],
        ) -> None:
            '''
            :param attributes: ``CfnInput.InputDefinitionProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "attributes": attributes,
            }

        @builtins.property
        def attributes(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.AttributeProperty"]]]:
            '''``CfnInput.InputDefinitionProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotevents-input-inputdefinition.html#cfn-iotevents-input-inputdefinition-attributes
            '''
            result = self._values.get("attributes")
            assert result is not None, "Required property 'attributes' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInput.AttributeProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-iotevents.CfnInputProps",
    jsii_struct_bases=[],
    name_mapping={
        "input_definition": "inputDefinition",
        "input_description": "inputDescription",
        "input_name": "inputName",
        "tags": "tags",
    },
)
class CfnInputProps:
    def __init__(
        self,
        *,
        input_definition: typing.Union[aws_cdk.core.IResolvable, CfnInput.InputDefinitionProperty],
        input_description: typing.Optional[builtins.str] = None,
        input_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::IoTEvents::Input``.

        :param input_definition: ``AWS::IoTEvents::Input.InputDefinition``.
        :param input_description: ``AWS::IoTEvents::Input.InputDescription``.
        :param input_name: ``AWS::IoTEvents::Input.InputName``.
        :param tags: ``AWS::IoTEvents::Input.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "input_definition": input_definition,
        }
        if input_description is not None:
            self._values["input_description"] = input_description
        if input_name is not None:
            self._values["input_name"] = input_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def input_definition(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnInput.InputDefinitionProperty]:
        '''``AWS::IoTEvents::Input.InputDefinition``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputdefinition
        '''
        result = self._values.get("input_definition")
        assert result is not None, "Required property 'input_definition' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnInput.InputDefinitionProperty], result)

    @builtins.property
    def input_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::Input.InputDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputdescription
        '''
        result = self._values.get("input_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::IoTEvents::Input.InputName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-inputname
        '''
        result = self._values.get("input_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::IoTEvents::Input.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html#cfn-iotevents-input-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDetectorModel",
    "CfnDetectorModelProps",
    "CfnInput",
    "CfnInputProps",
]

publication.publish()
