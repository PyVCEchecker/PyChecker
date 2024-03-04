'''
# Amazon Simple Email Service Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Email receiving

Create a receipt rule set with rules and actions (actions can be found in the
`@aws-cdk/aws-ses-actions` package):

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_ses as ses
import aws_cdk.aws_ses_actions as actions
import aws_cdk.aws_sns as sns

bucket = s3.Bucket(stack, "Bucket")
topic = sns.Topic(stack, "Topic")

ses.ReceiptRuleSet(stack, "RuleSet",
    rules=[ReceiptRuleOptions(
        recipients=["hello@aws.com"],
        actions=[
            actions.AddHeader(
                name="X-Special-Header",
                value="aws"
            ),
            actions.S3(
                bucket=bucket,
                object_key_prefix="emails/",
                topic=topic
            )
        ]
    ), ReceiptRuleOptions(
        recipients=["aws.com"],
        actions=[
            actions.Sns(
                topic=topic
            )
        ]
    )
    ]
)
```

Alternatively, rules can be added to a rule set:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
rule_set = ses.ReceiptRuleSet(self, "RuleSet")

aws_rule = rule_set.add_rule("Aws",
    recipients=["aws.com"]
)
```

And actions to rules:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
aws_rule.add_action(actions.Sns(
    topic=topic
))
```

When using `addRule`, the new rule is added after the last added rule unless `after` is specified.

### Drop spams

A rule to drop spam can be added by setting `dropSpam` to `true`:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
ses.ReceiptRuleSet(self, "RuleSet",
    drop_spam=True
)
```

This will add a rule at the top of the rule set with a Lambda action that stops processing messages that have at least one spam indicator. See [Lambda Function Examples](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda-example-functions.html).

## Receipt filter

Create a receipt filter:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
ses.ReceiptFilter(self, "Filter",
    ip="1.2.3.4/16"
)
```

An allow list filter is also available:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
ses.AllowListReceiptFilter(self, "AllowList",
    ips=["10.0.0.0/16", "1.2.3.4/16"
    ]
)
```

This will first create a block all filter and then create allow filters for the listed ip addresses.
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
import constructs


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.AddHeaderActionConfig",
    jsii_struct_bases=[],
    name_mapping={"header_name": "headerName", "header_value": "headerValue"},
)
class AddHeaderActionConfig:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
    ) -> None:
        '''AddHeaderAction configuration.

        :param header_name: The name of the header that you want to add to the incoming message.
        :param header_value: The content that you want to include in the header.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header that you want to add to the incoming message.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headername
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The content that you want to include in the header.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headervalue
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddHeaderActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AllowListReceiptFilter(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.AllowListReceiptFilter",
):
    '''An allow list receipt filter.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ips: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ips: A list of ip addresses or ranges to allow list.
        '''
        props = AllowListReceiptFilterProps(ips=ips)

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.AllowListReceiptFilterProps",
    jsii_struct_bases=[],
    name_mapping={"ips": "ips"},
)
class AllowListReceiptFilterProps:
    def __init__(self, *, ips: typing.Sequence[builtins.str]) -> None:
        '''Construction properties for am AllowListReceiptFilter.

        :param ips: A list of ip addresses or ranges to allow list.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "ips": ips,
        }

    @builtins.property
    def ips(self) -> typing.List[builtins.str]:
        '''A list of ip addresses or ranges to allow list.'''
        result = self._values.get("ips")
        assert result is not None, "Required property 'ips' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AllowListReceiptFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.BounceActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "message": "message",
        "sender": "sender",
        "smtp_reply_code": "smtpReplyCode",
        "status_code": "statusCode",
        "topic_arn": "topicArn",
    },
)
class BounceActionConfig:
    def __init__(
        self,
        *,
        message: builtins.str,
        sender: builtins.str,
        smtp_reply_code: builtins.str,
        status_code: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''BoundAction configuration.

        :param message: Human-readable text to include in the bounce message.
        :param sender: The email address of the sender of the bounced email. This is the address that the bounce message is sent from.
        :param smtp_reply_code: The SMTP reply code, as defined by RFC 5321.
        :param status_code: The SMTP enhanced status code, as defined by RFC 3463. Default: - No status code.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. Default: - No notification is sent to SNS.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
            "sender": sender,
            "smtp_reply_code": smtp_reply_code,
        }
        if status_code is not None:
            self._values["status_code"] = status_code
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def message(self) -> builtins.str:
        '''Human-readable text to include in the bounce message.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-message
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sender(self) -> builtins.str:
        '''The email address of the sender of the bounced email.

        This is the address that the bounce message is sent from.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-sender
        '''
        result = self._values.get("sender")
        assert result is not None, "Required property 'sender' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def smtp_reply_code(self) -> builtins.str:
        '''The SMTP reply code, as defined by RFC 5321.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-smtpreplycode
        '''
        result = self._values.get("smtp_reply_code")
        assert result is not None, "Required property 'smtp_reply_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status_code(self) -> typing.Optional[builtins.str]:
        '''The SMTP enhanced status code, as defined by RFC 3463.

        :default: - No status code.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-statuscode
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BounceActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnConfigurationSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.CfnConfigurationSet",
):
    '''A CloudFormation ``AWS::SES::ConfigurationSet``.

    :cloudformationResource: AWS::SES::ConfigurationSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SES::ConfigurationSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::SES::ConfigurationSet.Name``.
        '''
        props = CfnConfigurationSetProps(name=name)

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
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::ConfigurationSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.implements(aws_cdk.core.IInspectable)
class CfnConfigurationSetEventDestination(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.CfnConfigurationSetEventDestination",
):
    '''A CloudFormation ``AWS::SES::ConfigurationSetEventDestination``.

    :cloudformationResource: AWS::SES::ConfigurationSetEventDestination
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        configuration_set_name: builtins.str,
        event_destination: typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"],
    ) -> None:
        '''Create a new ``AWS::SES::ConfigurationSetEventDestination``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param configuration_set_name: ``AWS::SES::ConfigurationSetEventDestination.ConfigurationSetName``.
        :param event_destination: ``AWS::SES::ConfigurationSetEventDestination.EventDestination``.
        '''
        props = CfnConfigurationSetEventDestinationProps(
            configuration_set_name=configuration_set_name,
            event_destination=event_destination,
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
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''``AWS::SES::ConfigurationSetEventDestination.ConfigurationSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-configurationsetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))

    @configuration_set_name.setter
    def configuration_set_name(self, value: builtins.str) -> None:
        jsii.set(self, "configurationSetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventDestination")
    def event_destination(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"]:
        '''``AWS::SES::ConfigurationSetEventDestination.EventDestination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-eventdestination
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"], jsii.get(self, "eventDestination"))

    @event_destination.setter
    def event_destination(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.EventDestinationProperty"],
    ) -> None:
        jsii.set(self, "eventDestination", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_configurations": "dimensionConfigurations"},
    )
    class CloudWatchDestinationProperty:
        def __init__(
            self,
            *,
            dimension_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]] = None,
        ) -> None:
            '''
            :param dimension_configurations: ``CfnConfigurationSetEventDestination.CloudWatchDestinationProperty.DimensionConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dimension_configurations is not None:
                self._values["dimension_configurations"] = dimension_configurations

        @builtins.property
        def dimension_configurations(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]]:
            '''``CfnConfigurationSetEventDestination.CloudWatchDestinationProperty.DimensionConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html#cfn-ses-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations
            '''
            result = self._values.get("dimension_configurations")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_dimension_value": "defaultDimensionValue",
            "dimension_name": "dimensionName",
            "dimension_value_source": "dimensionValueSource",
        },
    )
    class DimensionConfigurationProperty:
        def __init__(
            self,
            *,
            default_dimension_value: builtins.str,
            dimension_name: builtins.str,
            dimension_value_source: builtins.str,
        ) -> None:
            '''
            :param default_dimension_value: ``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DefaultDimensionValue``.
            :param dimension_name: ``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DimensionName``.
            :param dimension_value_source: ``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DimensionValueSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "default_dimension_value": default_dimension_value,
                "dimension_name": dimension_name,
                "dimension_value_source": dimension_value_source,
            }

        @builtins.property
        def default_dimension_value(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DefaultDimensionValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue
            '''
            result = self._values.get("default_dimension_value")
            assert result is not None, "Required property 'default_dimension_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_name(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DimensionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionname
            '''
            result = self._values.get("dimension_name")
            assert result is not None, "Required property 'dimension_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_value_source(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.DimensionConfigurationProperty.DimensionValueSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource
            '''
            result = self._values.get("dimension_value_source")
            assert result is not None, "Required property 'dimension_value_source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnConfigurationSetEventDestination.EventDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "matching_event_types": "matchingEventTypes",
            "cloud_watch_destination": "cloudWatchDestination",
            "enabled": "enabled",
            "kinesis_firehose_destination": "kinesisFirehoseDestination",
            "name": "name",
        },
    )
    class EventDestinationProperty:
        def __init__(
            self,
            *,
            matching_event_types: typing.Sequence[builtins.str],
            cloud_watch_destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            kinesis_firehose_destination: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param matching_event_types: ``CfnConfigurationSetEventDestination.EventDestinationProperty.MatchingEventTypes``.
            :param cloud_watch_destination: ``CfnConfigurationSetEventDestination.EventDestinationProperty.CloudWatchDestination``.
            :param enabled: ``CfnConfigurationSetEventDestination.EventDestinationProperty.Enabled``.
            :param kinesis_firehose_destination: ``CfnConfigurationSetEventDestination.EventDestinationProperty.KinesisFirehoseDestination``.
            :param name: ``CfnConfigurationSetEventDestination.EventDestinationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "matching_event_types": matching_event_types,
            }
            if cloud_watch_destination is not None:
                self._values["cloud_watch_destination"] = cloud_watch_destination
            if enabled is not None:
                self._values["enabled"] = enabled
            if kinesis_firehose_destination is not None:
                self._values["kinesis_firehose_destination"] = kinesis_firehose_destination
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def matching_event_types(self) -> typing.List[builtins.str]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.MatchingEventTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-matchingeventtypes
            '''
            result = self._values.get("matching_event_types")
            assert result is not None, "Required property 'matching_event_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def cloud_watch_destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.CloudWatchDestination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-cloudwatchdestination
            '''
            result = self._values.get("cloud_watch_destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def kinesis_firehose_destination(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.KinesisFirehoseDestination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-kinesisfirehosedestination
            '''
            result = self._values.get("kinesis_firehose_destination")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnConfigurationSetEventDestination.EventDestinationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_arn": "deliveryStreamArn",
            "iam_role_arn": "iamRoleArn",
        },
    )
    class KinesisFirehoseDestinationProperty:
        def __init__(
            self,
            *,
            delivery_stream_arn: builtins.str,
            iam_role_arn: builtins.str,
        ) -> None:
            '''
            :param delivery_stream_arn: ``CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty.DeliveryStreamARN``.
            :param iam_role_arn: ``CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty.IAMRoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "delivery_stream_arn": delivery_stream_arn,
                "iam_role_arn": iam_role_arn,
            }

        @builtins.property
        def delivery_stream_arn(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty.DeliveryStreamARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn
            '''
            result = self._values.get("delivery_stream_arn")
            assert result is not None, "Required property 'delivery_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iam_role_arn(self) -> builtins.str:
            '''``CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty.IAMRoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            assert result is not None, "Required property 'iam_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.CfnConfigurationSetEventDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_name": "configurationSetName",
        "event_destination": "eventDestination",
    },
)
class CfnConfigurationSetEventDestinationProps:
    def __init__(
        self,
        *,
        configuration_set_name: builtins.str,
        event_destination: typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSetEventDestination.EventDestinationProperty],
    ) -> None:
        '''Properties for defining a ``AWS::SES::ConfigurationSetEventDestination``.

        :param configuration_set_name: ``AWS::SES::ConfigurationSetEventDestination.ConfigurationSetName``.
        :param event_destination: ``AWS::SES::ConfigurationSetEventDestination.EventDestination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "configuration_set_name": configuration_set_name,
            "event_destination": event_destination,
        }

    @builtins.property
    def configuration_set_name(self) -> builtins.str:
        '''``AWS::SES::ConfigurationSetEventDestination.ConfigurationSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-configurationsetname
        '''
        result = self._values.get("configuration_set_name")
        assert result is not None, "Required property 'configuration_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_destination(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSetEventDestination.EventDestinationProperty]:
        '''``AWS::SES::ConfigurationSetEventDestination.EventDestination``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-eventdestination
        '''
        result = self._values.get("event_destination")
        assert result is not None, "Required property 'event_destination' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnConfigurationSetEventDestination.EventDestinationProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetEventDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.CfnConfigurationSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class CfnConfigurationSetProps:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''Properties for defining a ``AWS::SES::ConfigurationSet``.

        :param name: ``AWS::SES::ConfigurationSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::ConfigurationSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnContactList(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.CfnContactList",
):
    '''A CloudFormation ``AWS::SES::ContactList``.

    :cloudformationResource: AWS::SES::ContactList
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        contact_list_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        topics: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnContactList.TopicProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SES::ContactList``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param contact_list_name: ``AWS::SES::ContactList.ContactListName``.
        :param description: ``AWS::SES::ContactList.Description``.
        :param tags: ``AWS::SES::ContactList.Tags``.
        :param topics: ``AWS::SES::ContactList.Topics``.
        '''
        props = CfnContactListProps(
            contact_list_name=contact_list_name,
            description=description,
            tags=tags,
            topics=topics,
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
        '''``AWS::SES::ContactList.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="contactListName")
    def contact_list_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::ContactList.ContactListName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactListName"))

    @contact_list_name.setter
    def contact_list_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "contactListName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::ContactList.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="topics")
    def topics(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnContactList.TopicProperty"]]]]:
        '''``AWS::SES::ContactList.Topics``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnContactList.TopicProperty"]]]], jsii.get(self, "topics"))

    @topics.setter
    def topics(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnContactList.TopicProperty"]]]],
    ) -> None:
        jsii.set(self, "topics", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnContactList.TopicProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_subscription_status": "defaultSubscriptionStatus",
            "display_name": "displayName",
            "topic_name": "topicName",
            "description": "description",
        },
    )
    class TopicProperty:
        def __init__(
            self,
            *,
            default_subscription_status: builtins.str,
            display_name: builtins.str,
            topic_name: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param default_subscription_status: ``CfnContactList.TopicProperty.DefaultSubscriptionStatus``.
            :param display_name: ``CfnContactList.TopicProperty.DisplayName``.
            :param topic_name: ``CfnContactList.TopicProperty.TopicName``.
            :param description: ``CfnContactList.TopicProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "default_subscription_status": default_subscription_status,
                "display_name": display_name,
                "topic_name": topic_name,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def default_subscription_status(self) -> builtins.str:
            '''``CfnContactList.TopicProperty.DefaultSubscriptionStatus``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-defaultsubscriptionstatus
            '''
            result = self._values.get("default_subscription_status")
            assert result is not None, "Required property 'default_subscription_status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def display_name(self) -> builtins.str:
            '''``CfnContactList.TopicProperty.DisplayName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-displayname
            '''
            result = self._values.get("display_name")
            assert result is not None, "Required property 'display_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_name(self) -> builtins.str:
            '''``CfnContactList.TopicProperty.TopicName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-topicname
            '''
            result = self._values.get("topic_name")
            assert result is not None, "Required property 'topic_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''``CfnContactList.TopicProperty.Description``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TopicProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.CfnContactListProps",
    jsii_struct_bases=[],
    name_mapping={
        "contact_list_name": "contactListName",
        "description": "description",
        "tags": "tags",
        "topics": "topics",
    },
)
class CfnContactListProps:
    def __init__(
        self,
        *,
        contact_list_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        topics: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnContactList.TopicProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SES::ContactList``.

        :param contact_list_name: ``AWS::SES::ContactList.ContactListName``.
        :param description: ``AWS::SES::ContactList.Description``.
        :param tags: ``AWS::SES::ContactList.Tags``.
        :param topics: ``AWS::SES::ContactList.Topics``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if contact_list_name is not None:
            self._values["contact_list_name"] = contact_list_name
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if topics is not None:
            self._values["topics"] = topics

    @builtins.property
    def contact_list_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::ContactList.ContactListName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        '''
        result = self._values.get("contact_list_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::ContactList.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SES::ContactList.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def topics(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnContactList.TopicProperty]]]]:
        '''``AWS::SES::ContactList.Topics``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        '''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnContactList.TopicProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnReceiptFilter(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.CfnReceiptFilter",
):
    '''A CloudFormation ``AWS::SES::ReceiptFilter``.

    :cloudformationResource: AWS::SES::ReceiptFilter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        filter: typing.Union["CfnReceiptFilter.FilterProperty", aws_cdk.core.IResolvable],
    ) -> None:
        '''Create a new ``AWS::SES::ReceiptFilter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param filter: ``AWS::SES::ReceiptFilter.Filter``.
        '''
        props = CfnReceiptFilterProps(filter=filter)

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
    @jsii.member(jsii_name="filter")
    def filter(
        self,
    ) -> typing.Union["CfnReceiptFilter.FilterProperty", aws_cdk.core.IResolvable]:
        '''``AWS::SES::ReceiptFilter.Filter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html#cfn-ses-receiptfilter-filter
        '''
        return typing.cast(typing.Union["CfnReceiptFilter.FilterProperty", aws_cdk.core.IResolvable], jsii.get(self, "filter"))

    @filter.setter
    def filter(
        self,
        value: typing.Union["CfnReceiptFilter.FilterProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "filter", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnReceiptFilter.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"ip_filter": "ipFilter", "name": "name"},
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            ip_filter: typing.Union[aws_cdk.core.IResolvable, "CfnReceiptFilter.IpFilterProperty"],
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param ip_filter: ``CfnReceiptFilter.FilterProperty.IpFilter``.
            :param name: ``CfnReceiptFilter.FilterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "ip_filter": ip_filter,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def ip_filter(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnReceiptFilter.IpFilterProperty"]:
            '''``CfnReceiptFilter.FilterProperty.IpFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-ipfilter
            '''
            result = self._values.get("ip_filter")
            assert result is not None, "Required property 'ip_filter' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnReceiptFilter.IpFilterProperty"], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptFilter.FilterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-name
            '''
            result = self._values.get("name")
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
        jsii_type="@aws-cdk/aws-ses.CfnReceiptFilter.IpFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr": "cidr", "policy": "policy"},
    )
    class IpFilterProperty:
        def __init__(self, *, cidr: builtins.str, policy: builtins.str) -> None:
            '''
            :param cidr: ``CfnReceiptFilter.IpFilterProperty.Cidr``.
            :param policy: ``CfnReceiptFilter.IpFilterProperty.Policy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cidr": cidr,
                "policy": policy,
            }

        @builtins.property
        def cidr(self) -> builtins.str:
            '''``CfnReceiptFilter.IpFilterProperty.Cidr``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-cidr
            '''
            result = self._values.get("cidr")
            assert result is not None, "Required property 'cidr' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def policy(self) -> builtins.str:
            '''``CfnReceiptFilter.IpFilterProperty.Policy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-policy
            '''
            result = self._values.get("policy")
            assert result is not None, "Required property 'policy' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IpFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.CfnReceiptFilterProps",
    jsii_struct_bases=[],
    name_mapping={"filter": "filter"},
)
class CfnReceiptFilterProps:
    def __init__(
        self,
        *,
        filter: typing.Union[CfnReceiptFilter.FilterProperty, aws_cdk.core.IResolvable],
    ) -> None:
        '''Properties for defining a ``AWS::SES::ReceiptFilter``.

        :param filter: ``AWS::SES::ReceiptFilter.Filter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "filter": filter,
        }

    @builtins.property
    def filter(
        self,
    ) -> typing.Union[CfnReceiptFilter.FilterProperty, aws_cdk.core.IResolvable]:
        '''``AWS::SES::ReceiptFilter.Filter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html#cfn-ses-receiptfilter-filter
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(typing.Union[CfnReceiptFilter.FilterProperty, aws_cdk.core.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReceiptFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnReceiptRule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.CfnReceiptRule",
):
    '''A CloudFormation ``AWS::SES::ReceiptRule``.

    :cloudformationResource: AWS::SES::ReceiptRule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        rule: typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.RuleProperty"],
        rule_set_name: builtins.str,
        after: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SES::ReceiptRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param rule: ``AWS::SES::ReceiptRule.Rule``.
        :param rule_set_name: ``AWS::SES::ReceiptRule.RuleSetName``.
        :param after: ``AWS::SES::ReceiptRule.After``.
        '''
        props = CfnReceiptRuleProps(
            rule=rule, rule_set_name=rule_set_name, after=after
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
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.RuleProperty"]:
        '''``AWS::SES::ReceiptRule.Rule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rule
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.RuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.RuleProperty"],
    ) -> None:
        jsii.set(self, "rule", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ruleSetName")
    def rule_set_name(self) -> builtins.str:
        '''``AWS::SES::ReceiptRule.RuleSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rulesetname
        '''
        return typing.cast(builtins.str, jsii.get(self, "ruleSetName"))

    @rule_set_name.setter
    def rule_set_name(self, value: builtins.str) -> None:
        jsii.set(self, "ruleSetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="after")
    def after(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::ReceiptRule.After``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-after
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "after"))

    @after.setter
    def after(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "after", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnReceiptRule.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_header_action": "addHeaderAction",
            "bounce_action": "bounceAction",
            "lambda_action": "lambdaAction",
            "s3_action": "s3Action",
            "sns_action": "snsAction",
            "stop_action": "stopAction",
            "workmail_action": "workmailAction",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            add_header_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.AddHeaderActionProperty"]] = None,
            bounce_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.BounceActionProperty"]] = None,
            lambda_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.LambdaActionProperty"]] = None,
            s3_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.S3ActionProperty"]] = None,
            sns_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.SNSActionProperty"]] = None,
            stop_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.StopActionProperty"]] = None,
            workmail_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.WorkmailActionProperty"]] = None,
        ) -> None:
            '''
            :param add_header_action: ``CfnReceiptRule.ActionProperty.AddHeaderAction``.
            :param bounce_action: ``CfnReceiptRule.ActionProperty.BounceAction``.
            :param lambda_action: ``CfnReceiptRule.ActionProperty.LambdaAction``.
            :param s3_action: ``CfnReceiptRule.ActionProperty.S3Action``.
            :param sns_action: ``CfnReceiptRule.ActionProperty.SNSAction``.
            :param stop_action: ``CfnReceiptRule.ActionProperty.StopAction``.
            :param workmail_action: ``CfnReceiptRule.ActionProperty.WorkmailAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if add_header_action is not None:
                self._values["add_header_action"] = add_header_action
            if bounce_action is not None:
                self._values["bounce_action"] = bounce_action
            if lambda_action is not None:
                self._values["lambda_action"] = lambda_action
            if s3_action is not None:
                self._values["s3_action"] = s3_action
            if sns_action is not None:
                self._values["sns_action"] = sns_action
            if stop_action is not None:
                self._values["stop_action"] = stop_action
            if workmail_action is not None:
                self._values["workmail_action"] = workmail_action

        @builtins.property
        def add_header_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.AddHeaderActionProperty"]]:
            '''``CfnReceiptRule.ActionProperty.AddHeaderAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-addheaderaction
            '''
            result = self._values.get("add_header_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.AddHeaderActionProperty"]], result)

        @builtins.property
        def bounce_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.BounceActionProperty"]]:
            '''``CfnReceiptRule.ActionProperty.BounceAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-bounceaction
            '''
            result = self._values.get("bounce_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.BounceActionProperty"]], result)

        @builtins.property
        def lambda_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.LambdaActionProperty"]]:
            '''``CfnReceiptRule.ActionProperty.LambdaAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-lambdaaction
            '''
            result = self._values.get("lambda_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.LambdaActionProperty"]], result)

        @builtins.property
        def s3_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.S3ActionProperty"]]:
            '''``CfnReceiptRule.ActionProperty.S3Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-s3action
            '''
            result = self._values.get("s3_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.S3ActionProperty"]], result)

        @builtins.property
        def sns_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.SNSActionProperty"]]:
            '''``CfnReceiptRule.ActionProperty.SNSAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-snsaction
            '''
            result = self._values.get("sns_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.SNSActionProperty"]], result)

        @builtins.property
        def stop_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.StopActionProperty"]]:
            '''``CfnReceiptRule.ActionProperty.StopAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-stopaction
            '''
            result = self._values.get("stop_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.StopActionProperty"]], result)

        @builtins.property
        def workmail_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.WorkmailActionProperty"]]:
            '''``CfnReceiptRule.ActionProperty.WorkmailAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-workmailaction
            '''
            result = self._values.get("workmail_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.WorkmailActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnReceiptRule.AddHeaderActionProperty",
        jsii_struct_bases=[],
        name_mapping={"header_name": "headerName", "header_value": "headerValue"},
    )
    class AddHeaderActionProperty:
        def __init__(
            self,
            *,
            header_name: builtins.str,
            header_value: builtins.str,
        ) -> None:
            '''
            :param header_name: ``CfnReceiptRule.AddHeaderActionProperty.HeaderName``.
            :param header_value: ``CfnReceiptRule.AddHeaderActionProperty.HeaderValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "header_name": header_name,
                "header_value": header_value,
            }

        @builtins.property
        def header_name(self) -> builtins.str:
            '''``CfnReceiptRule.AddHeaderActionProperty.HeaderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headername
            '''
            result = self._values.get("header_name")
            assert result is not None, "Required property 'header_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def header_value(self) -> builtins.str:
            '''``CfnReceiptRule.AddHeaderActionProperty.HeaderValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headervalue
            '''
            result = self._values.get("header_value")
            assert result is not None, "Required property 'header_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddHeaderActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnReceiptRule.BounceActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "message": "message",
            "sender": "sender",
            "smtp_reply_code": "smtpReplyCode",
            "status_code": "statusCode",
            "topic_arn": "topicArn",
        },
    )
    class BounceActionProperty:
        def __init__(
            self,
            *,
            message: builtins.str,
            sender: builtins.str,
            smtp_reply_code: builtins.str,
            status_code: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param message: ``CfnReceiptRule.BounceActionProperty.Message``.
            :param sender: ``CfnReceiptRule.BounceActionProperty.Sender``.
            :param smtp_reply_code: ``CfnReceiptRule.BounceActionProperty.SmtpReplyCode``.
            :param status_code: ``CfnReceiptRule.BounceActionProperty.StatusCode``.
            :param topic_arn: ``CfnReceiptRule.BounceActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "message": message,
                "sender": sender,
                "smtp_reply_code": smtp_reply_code,
            }
            if status_code is not None:
                self._values["status_code"] = status_code
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def message(self) -> builtins.str:
            '''``CfnReceiptRule.BounceActionProperty.Message``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-message
            '''
            result = self._values.get("message")
            assert result is not None, "Required property 'message' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sender(self) -> builtins.str:
            '''``CfnReceiptRule.BounceActionProperty.Sender``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-sender
            '''
            result = self._values.get("sender")
            assert result is not None, "Required property 'sender' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def smtp_reply_code(self) -> builtins.str:
            '''``CfnReceiptRule.BounceActionProperty.SmtpReplyCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-smtpreplycode
            '''
            result = self._values.get("smtp_reply_code")
            assert result is not None, "Required property 'smtp_reply_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def status_code(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.BounceActionProperty.StatusCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-statuscode
            '''
            result = self._values.get("status_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.BounceActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BounceActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnReceiptRule.LambdaActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "function_arn": "functionArn",
            "invocation_type": "invocationType",
            "topic_arn": "topicArn",
        },
    )
    class LambdaActionProperty:
        def __init__(
            self,
            *,
            function_arn: builtins.str,
            invocation_type: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param function_arn: ``CfnReceiptRule.LambdaActionProperty.FunctionArn``.
            :param invocation_type: ``CfnReceiptRule.LambdaActionProperty.InvocationType``.
            :param topic_arn: ``CfnReceiptRule.LambdaActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "function_arn": function_arn,
            }
            if invocation_type is not None:
                self._values["invocation_type"] = invocation_type
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def function_arn(self) -> builtins.str:
            '''``CfnReceiptRule.LambdaActionProperty.FunctionArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-functionarn
            '''
            result = self._values.get("function_arn")
            assert result is not None, "Required property 'function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invocation_type(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.LambdaActionProperty.InvocationType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-invocationtype
            '''
            result = self._values.get("invocation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.LambdaActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnReceiptRule.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actions": "actions",
            "enabled": "enabled",
            "name": "name",
            "recipients": "recipients",
            "scan_enabled": "scanEnabled",
            "tls_policy": "tlsPolicy",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.ActionProperty"]]]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            name: typing.Optional[builtins.str] = None,
            recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
            scan_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            tls_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param actions: ``CfnReceiptRule.RuleProperty.Actions``.
            :param enabled: ``CfnReceiptRule.RuleProperty.Enabled``.
            :param name: ``CfnReceiptRule.RuleProperty.Name``.
            :param recipients: ``CfnReceiptRule.RuleProperty.Recipients``.
            :param scan_enabled: ``CfnReceiptRule.RuleProperty.ScanEnabled``.
            :param tls_policy: ``CfnReceiptRule.RuleProperty.TlsPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if actions is not None:
                self._values["actions"] = actions
            if enabled is not None:
                self._values["enabled"] = enabled
            if name is not None:
                self._values["name"] = name
            if recipients is not None:
                self._values["recipients"] = recipients
            if scan_enabled is not None:
                self._values["scan_enabled"] = scan_enabled
            if tls_policy is not None:
                self._values["tls_policy"] = tls_policy

        @builtins.property
        def actions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.ActionProperty"]]]]:
            '''``CfnReceiptRule.RuleProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-actions
            '''
            result = self._values.get("actions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnReceiptRule.ActionProperty"]]]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnReceiptRule.RuleProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.RuleProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnReceiptRule.RuleProperty.Recipients``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-recipients
            '''
            result = self._values.get("recipients")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def scan_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnReceiptRule.RuleProperty.ScanEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-scanenabled
            '''
            result = self._values.get("scan_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def tls_policy(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.RuleProperty.TlsPolicy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-tlspolicy
            '''
            result = self._values.get("tls_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnReceiptRule.S3ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "kms_key_arn": "kmsKeyArn",
            "object_key_prefix": "objectKeyPrefix",
            "topic_arn": "topicArn",
        },
    )
    class S3ActionProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            kms_key_arn: typing.Optional[builtins.str] = None,
            object_key_prefix: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket_name: ``CfnReceiptRule.S3ActionProperty.BucketName``.
            :param kms_key_arn: ``CfnReceiptRule.S3ActionProperty.KmsKeyArn``.
            :param object_key_prefix: ``CfnReceiptRule.S3ActionProperty.ObjectKeyPrefix``.
            :param topic_arn: ``CfnReceiptRule.S3ActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn
            if object_key_prefix is not None:
                self._values["object_key_prefix"] = object_key_prefix
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''``CfnReceiptRule.S3ActionProperty.BucketName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.S3ActionProperty.KmsKeyArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_key_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.S3ActionProperty.ObjectKeyPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-objectkeyprefix
            '''
            result = self._values.get("object_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.S3ActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnReceiptRule.SNSActionProperty",
        jsii_struct_bases=[],
        name_mapping={"encoding": "encoding", "topic_arn": "topicArn"},
    )
    class SNSActionProperty:
        def __init__(
            self,
            *,
            encoding: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param encoding: ``CfnReceiptRule.SNSActionProperty.Encoding``.
            :param topic_arn: ``CfnReceiptRule.SNSActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if encoding is not None:
                self._values["encoding"] = encoding
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def encoding(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.SNSActionProperty.Encoding``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-encoding
            '''
            result = self._values.get("encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.SNSActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SNSActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnReceiptRule.StopActionProperty",
        jsii_struct_bases=[],
        name_mapping={"scope": "scope", "topic_arn": "topicArn"},
    )
    class StopActionProperty:
        def __init__(
            self,
            *,
            scope: builtins.str,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param scope: ``CfnReceiptRule.StopActionProperty.Scope``.
            :param topic_arn: ``CfnReceiptRule.StopActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "scope": scope,
            }
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def scope(self) -> builtins.str:
            '''``CfnReceiptRule.StopActionProperty.Scope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-scope
            '''
            result = self._values.get("scope")
            assert result is not None, "Required property 'scope' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.StopActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StopActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnReceiptRule.WorkmailActionProperty",
        jsii_struct_bases=[],
        name_mapping={"organization_arn": "organizationArn", "topic_arn": "topicArn"},
    )
    class WorkmailActionProperty:
        def __init__(
            self,
            *,
            organization_arn: builtins.str,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param organization_arn: ``CfnReceiptRule.WorkmailActionProperty.OrganizationArn``.
            :param topic_arn: ``CfnReceiptRule.WorkmailActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "organization_arn": organization_arn,
            }
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def organization_arn(self) -> builtins.str:
            '''``CfnReceiptRule.WorkmailActionProperty.OrganizationArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-organizationarn
            '''
            result = self._values.get("organization_arn")
            assert result is not None, "Required property 'organization_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnReceiptRule.WorkmailActionProperty.TopicArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkmailActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.CfnReceiptRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_set_name": "ruleSetName", "after": "after"},
)
class CfnReceiptRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union[aws_cdk.core.IResolvable, CfnReceiptRule.RuleProperty],
        rule_set_name: builtins.str,
        after: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SES::ReceiptRule``.

        :param rule: ``AWS::SES::ReceiptRule.Rule``.
        :param rule_set_name: ``AWS::SES::ReceiptRule.RuleSetName``.
        :param after: ``AWS::SES::ReceiptRule.After``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "rule": rule,
            "rule_set_name": rule_set_name,
        }
        if after is not None:
            self._values["after"] = after

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnReceiptRule.RuleProperty]:
        '''``AWS::SES::ReceiptRule.Rule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnReceiptRule.RuleProperty], result)

    @builtins.property
    def rule_set_name(self) -> builtins.str:
        '''``AWS::SES::ReceiptRule.RuleSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rulesetname
        '''
        result = self._values.get("rule_set_name")
        assert result is not None, "Required property 'rule_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def after(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::ReceiptRule.After``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-after
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReceiptRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnReceiptRuleSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.CfnReceiptRuleSet",
):
    '''A CloudFormation ``AWS::SES::ReceiptRuleSet``.

    :cloudformationResource: AWS::SES::ReceiptRuleSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        rule_set_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::SES::ReceiptRuleSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param rule_set_name: ``AWS::SES::ReceiptRuleSet.RuleSetName``.
        '''
        props = CfnReceiptRuleSetProps(rule_set_name=rule_set_name)

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
    @jsii.member(jsii_name="ruleSetName")
    def rule_set_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::ReceiptRuleSet.RuleSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html#cfn-ses-receiptruleset-rulesetname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleSetName"))

    @rule_set_name.setter
    def rule_set_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ruleSetName", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.CfnReceiptRuleSetProps",
    jsii_struct_bases=[],
    name_mapping={"rule_set_name": "ruleSetName"},
)
class CfnReceiptRuleSetProps:
    def __init__(self, *, rule_set_name: typing.Optional[builtins.str] = None) -> None:
        '''Properties for defining a ``AWS::SES::ReceiptRuleSet``.

        :param rule_set_name: ``AWS::SES::ReceiptRuleSet.RuleSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if rule_set_name is not None:
            self._values["rule_set_name"] = rule_set_name

    @builtins.property
    def rule_set_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::SES::ReceiptRuleSet.RuleSetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html#cfn-ses-receiptruleset-rulesetname
        '''
        result = self._values.get("rule_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReceiptRuleSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTemplate(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.CfnTemplate",
):
    '''A CloudFormation ``AWS::SES::Template``.

    :cloudformationResource: AWS::SES::Template
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        template: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::SES::Template``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param template: ``AWS::SES::Template.Template``.
        '''
        props = CfnTemplateProps(template=template)

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
    @jsii.member(jsii_name="template")
    def template(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateProperty"]]:
        '''``AWS::SES::Template.Template``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html#cfn-ses-template-template
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateProperty"]], jsii.get(self, "template"))

    @template.setter
    def template(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnTemplate.TemplateProperty"]],
    ) -> None:
        jsii.set(self, "template", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-ses.CfnTemplate.TemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "html_part": "htmlPart",
            "subject_part": "subjectPart",
            "template_name": "templateName",
            "text_part": "textPart",
        },
    )
    class TemplateProperty:
        def __init__(
            self,
            *,
            html_part: typing.Optional[builtins.str] = None,
            subject_part: typing.Optional[builtins.str] = None,
            template_name: typing.Optional[builtins.str] = None,
            text_part: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param html_part: ``CfnTemplate.TemplateProperty.HtmlPart``.
            :param subject_part: ``CfnTemplate.TemplateProperty.SubjectPart``.
            :param template_name: ``CfnTemplate.TemplateProperty.TemplateName``.
            :param text_part: ``CfnTemplate.TemplateProperty.TextPart``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if html_part is not None:
                self._values["html_part"] = html_part
            if subject_part is not None:
                self._values["subject_part"] = subject_part
            if template_name is not None:
                self._values["template_name"] = template_name
            if text_part is not None:
                self._values["text_part"] = text_part

        @builtins.property
        def html_part(self) -> typing.Optional[builtins.str]:
            '''``CfnTemplate.TemplateProperty.HtmlPart``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-htmlpart
            '''
            result = self._values.get("html_part")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subject_part(self) -> typing.Optional[builtins.str]:
            '''``CfnTemplate.TemplateProperty.SubjectPart``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-subjectpart
            '''
            result = self._values.get("subject_part")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def template_name(self) -> typing.Optional[builtins.str]:
            '''``CfnTemplate.TemplateProperty.TemplateName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-templatename
            '''
            result = self._values.get("template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text_part(self) -> typing.Optional[builtins.str]:
            '''``CfnTemplate.TemplateProperty.TextPart``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-textpart
            '''
            result = self._values.get("text_part")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.CfnTemplateProps",
    jsii_struct_bases=[],
    name_mapping={"template": "template"},
)
class CfnTemplateProps:
    def __init__(
        self,
        *,
        template: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTemplate.TemplateProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SES::Template``.

        :param template: ``AWS::SES::Template.Template``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def template(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTemplate.TemplateProperty]]:
        '''``AWS::SES::Template.Template``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html#cfn-ses-template-template
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnTemplate.TemplateProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DropSpamReceiptRule(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.DropSpamReceiptRule",
):
    '''A rule added at the top of the rule set to drop spam/virus.

    :see: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda-example-functions.html
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        rule_set: "IReceiptRuleSet",
        actions: typing.Optional[typing.Sequence["IReceiptRuleAction"]] = None,
        after: typing.Optional["IReceiptRule"] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param rule_set: The name of the rule set that the receipt rule will be added to.
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        props = DropSpamReceiptRuleProps(
            rule_set=rule_set,
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rule")
    def rule(self) -> "ReceiptRule":
        return typing.cast("ReceiptRule", jsii.get(self, "rule"))


@jsii.interface(jsii_type="@aws-cdk/aws-ses.IReceiptRule")
class IReceiptRule(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''A receipt rule.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleName")
    def receipt_rule_name(self) -> builtins.str:
        '''The name of the receipt rule.

        :attribute: true
        '''
        ...


class _IReceiptRuleProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''A receipt rule.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-ses.IReceiptRule"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleName")
    def receipt_rule_name(self) -> builtins.str:
        '''The name of the receipt rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRule).__jsii_proxy_class__ = lambda : _IReceiptRuleProxy


@jsii.interface(jsii_type="@aws-cdk/aws-ses.IReceiptRuleAction")
class IReceiptRuleAction(typing_extensions.Protocol):
    '''An abstract action for a receipt rule.'''

    @jsii.member(jsii_name="bind")
    def bind(self, receipt_rule: IReceiptRule) -> "ReceiptRuleActionConfig":
        '''Returns the receipt rule action specification.

        :param receipt_rule: -
        '''
        ...


class _IReceiptRuleActionProxy:
    '''An abstract action for a receipt rule.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-ses.IReceiptRuleAction"

    @jsii.member(jsii_name="bind")
    def bind(self, receipt_rule: IReceiptRule) -> "ReceiptRuleActionConfig":
        '''Returns the receipt rule action specification.

        :param receipt_rule: -
        '''
        return typing.cast("ReceiptRuleActionConfig", jsii.invoke(self, "bind", [receipt_rule]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRuleAction).__jsii_proxy_class__ = lambda : _IReceiptRuleActionProxy


@jsii.interface(jsii_type="@aws-cdk/aws-ses.IReceiptRuleSet")
class IReceiptRuleSet(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''A receipt rule set.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleSetName")
    def receipt_rule_set_name(self) -> builtins.str:
        '''The receipt rule set name.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        id: builtins.str,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> "ReceiptRule":
        '''Adds a new receipt rule in this rule set.

        The new rule is added after
        the last added rule unless ``after`` is specified.

        :param id: -
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        ...


class _IReceiptRuleSetProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''A receipt rule set.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-ses.IReceiptRuleSet"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleSetName")
    def receipt_rule_set_name(self) -> builtins.str:
        '''The receipt rule set name.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleSetName"))

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        id: builtins.str,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> "ReceiptRule":
        '''Adds a new receipt rule in this rule set.

        The new rule is added after
        the last added rule unless ``after`` is specified.

        :param id: -
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        options = ReceiptRuleOptions(
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        return typing.cast("ReceiptRule", jsii.invoke(self, "addRule", [id, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRuleSet).__jsii_proxy_class__ = lambda : _IReceiptRuleSetProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.LambdaActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "function_arn": "functionArn",
        "invocation_type": "invocationType",
        "topic_arn": "topicArn",
    },
)
class LambdaActionConfig:
    def __init__(
        self,
        *,
        function_arn: builtins.str,
        invocation_type: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''LambdaAction configuration.

        :param function_arn: The Amazon Resource Name (ARN) of the AWS Lambda function.
        :param invocation_type: The invocation type of the AWS Lambda function. Default: 'Event'
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed. Default: - No notification is sent to SNS.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "function_arn": function_arn,
        }
        if invocation_type is not None:
            self._values["invocation_type"] = invocation_type
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AWS Lambda function.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-functionarn
        '''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invocation_type(self) -> typing.Optional[builtins.str]:
        '''The invocation type of the AWS Lambda function.

        :default: 'Event'

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-invocationtype
        '''
        result = self._values.get("invocation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ReceiptFilter(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.ReceiptFilter",
):
    '''A receipt filter.

    When instantiated without props, it creates a
    block all receipt filter.
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ip: typing.Optional[builtins.str] = None,
        policy: typing.Optional["ReceiptFilterPolicy"] = None,
        receipt_filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ip: The ip address or range to filter. Default: 0.0.0.0/0
        :param policy: The policy for the filter. Default: Block
        :param receipt_filter_name: The name for the receipt filter. Default: a CloudFormation generated name
        '''
        props = ReceiptFilterProps(
            ip=ip, policy=policy, receipt_filter_name=receipt_filter_name
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.enum(jsii_type="@aws-cdk/aws-ses.ReceiptFilterPolicy")
class ReceiptFilterPolicy(enum.Enum):
    '''The policy for the receipt filter.'''

    ALLOW = "ALLOW"
    '''Allow the ip address or range.'''
    BLOCK = "BLOCK"
    '''Block the ip address or range.'''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.ReceiptFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "ip": "ip",
        "policy": "policy",
        "receipt_filter_name": "receiptFilterName",
    },
)
class ReceiptFilterProps:
    def __init__(
        self,
        *,
        ip: typing.Optional[builtins.str] = None,
        policy: typing.Optional[ReceiptFilterPolicy] = None,
        receipt_filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for a ReceiptFilter.

        :param ip: The ip address or range to filter. Default: 0.0.0.0/0
        :param policy: The policy for the filter. Default: Block
        :param receipt_filter_name: The name for the receipt filter. Default: a CloudFormation generated name
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if ip is not None:
            self._values["ip"] = ip
        if policy is not None:
            self._values["policy"] = policy
        if receipt_filter_name is not None:
            self._values["receipt_filter_name"] = receipt_filter_name

    @builtins.property
    def ip(self) -> typing.Optional[builtins.str]:
        '''The ip address or range to filter.

        :default: 0.0.0.0/0
        '''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[ReceiptFilterPolicy]:
        '''The policy for the filter.

        :default: Block
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[ReceiptFilterPolicy], result)

    @builtins.property
    def receipt_filter_name(self) -> typing.Optional[builtins.str]:
        '''The name for the receipt filter.

        :default: a CloudFormation generated name
        '''
        result = self._values.get("receipt_filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IReceiptRule)
class ReceiptRule(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.ReceiptRule",
):
    '''A new receipt rule.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        rule_set: IReceiptRuleSet,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param rule_set: The name of the rule set that the receipt rule will be added to.
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        props = ReceiptRuleProps(
            rule_set=rule_set,
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromReceiptRuleName") # type: ignore[misc]
    @builtins.classmethod
    def from_receipt_rule_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        receipt_rule_name: builtins.str,
    ) -> IReceiptRule:
        '''
        :param scope: -
        :param id: -
        :param receipt_rule_name: -
        '''
        return typing.cast(IReceiptRule, jsii.sinvoke(cls, "fromReceiptRuleName", [scope, id, receipt_rule_name]))

    @jsii.member(jsii_name="addAction")
    def add_action(self, action: IReceiptRuleAction) -> None:
        '''Adds an action to this receipt rule.

        :param action: -
        '''
        return typing.cast(None, jsii.invoke(self, "addAction", [action]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleName")
    def receipt_rule_name(self) -> builtins.str:
        '''The name of the receipt rule.'''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleName"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.ReceiptRuleActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "add_header_action": "addHeaderAction",
        "bounce_action": "bounceAction",
        "lambda_action": "lambdaAction",
        "s3_action": "s3Action",
        "sns_action": "snsAction",
        "stop_action": "stopAction",
        "workmail_action": "workmailAction",
    },
)
class ReceiptRuleActionConfig:
    def __init__(
        self,
        *,
        add_header_action: typing.Optional[AddHeaderActionConfig] = None,
        bounce_action: typing.Optional[BounceActionConfig] = None,
        lambda_action: typing.Optional[LambdaActionConfig] = None,
        s3_action: typing.Optional["S3ActionConfig"] = None,
        sns_action: typing.Optional["SNSActionConfig"] = None,
        stop_action: typing.Optional["StopActionConfig"] = None,
        workmail_action: typing.Optional["WorkmailActionConfig"] = None,
    ) -> None:
        '''Properties for a receipt rule action.

        :param add_header_action: Adds a header to the received email.
        :param bounce_action: Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon SNS.
        :param lambda_action: Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.
        :param s3_action: Saves the received message to an Amazon S3 bucket and, optionally, publishes a notification to Amazon SNS.
        :param sns_action: Publishes the email content within a notification to Amazon SNS.
        :param stop_action: Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.
        :param workmail_action: Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.
        '''
        if isinstance(add_header_action, dict):
            add_header_action = AddHeaderActionConfig(**add_header_action)
        if isinstance(bounce_action, dict):
            bounce_action = BounceActionConfig(**bounce_action)
        if isinstance(lambda_action, dict):
            lambda_action = LambdaActionConfig(**lambda_action)
        if isinstance(s3_action, dict):
            s3_action = S3ActionConfig(**s3_action)
        if isinstance(sns_action, dict):
            sns_action = SNSActionConfig(**sns_action)
        if isinstance(stop_action, dict):
            stop_action = StopActionConfig(**stop_action)
        if isinstance(workmail_action, dict):
            workmail_action = WorkmailActionConfig(**workmail_action)
        self._values: typing.Dict[str, typing.Any] = {}
        if add_header_action is not None:
            self._values["add_header_action"] = add_header_action
        if bounce_action is not None:
            self._values["bounce_action"] = bounce_action
        if lambda_action is not None:
            self._values["lambda_action"] = lambda_action
        if s3_action is not None:
            self._values["s3_action"] = s3_action
        if sns_action is not None:
            self._values["sns_action"] = sns_action
        if stop_action is not None:
            self._values["stop_action"] = stop_action
        if workmail_action is not None:
            self._values["workmail_action"] = workmail_action

    @builtins.property
    def add_header_action(self) -> typing.Optional[AddHeaderActionConfig]:
        '''Adds a header to the received email.'''
        result = self._values.get("add_header_action")
        return typing.cast(typing.Optional[AddHeaderActionConfig], result)

    @builtins.property
    def bounce_action(self) -> typing.Optional[BounceActionConfig]:
        '''Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("bounce_action")
        return typing.cast(typing.Optional[BounceActionConfig], result)

    @builtins.property
    def lambda_action(self) -> typing.Optional[LambdaActionConfig]:
        '''Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("lambda_action")
        return typing.cast(typing.Optional[LambdaActionConfig], result)

    @builtins.property
    def s3_action(self) -> typing.Optional["S3ActionConfig"]:
        '''Saves the received message to an Amazon S3 bucket and, optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("s3_action")
        return typing.cast(typing.Optional["S3ActionConfig"], result)

    @builtins.property
    def sns_action(self) -> typing.Optional["SNSActionConfig"]:
        '''Publishes the email content within a notification to Amazon SNS.'''
        result = self._values.get("sns_action")
        return typing.cast(typing.Optional["SNSActionConfig"], result)

    @builtins.property
    def stop_action(self) -> typing.Optional["StopActionConfig"]:
        '''Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.'''
        result = self._values.get("stop_action")
        return typing.cast(typing.Optional["StopActionConfig"], result)

    @builtins.property
    def workmail_action(self) -> typing.Optional["WorkmailActionConfig"]:
        '''Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("workmail_action")
        return typing.cast(typing.Optional["WorkmailActionConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.ReceiptRuleOptions",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "after": "after",
        "enabled": "enabled",
        "receipt_rule_name": "receiptRuleName",
        "recipients": "recipients",
        "scan_enabled": "scanEnabled",
        "tls_policy": "tlsPolicy",
    },
)
class ReceiptRuleOptions:
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> None:
        '''Options to add a receipt rule to a receipt rule set.

        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if actions is not None:
            self._values["actions"] = actions
        if after is not None:
            self._values["after"] = after
        if enabled is not None:
            self._values["enabled"] = enabled
        if receipt_rule_name is not None:
            self._values["receipt_rule_name"] = receipt_rule_name
        if recipients is not None:
            self._values["recipients"] = recipients
        if scan_enabled is not None:
            self._values["scan_enabled"] = scan_enabled
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[IReceiptRuleAction]]:
        '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        :default: - No actions.
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[IReceiptRuleAction]], result)

    @builtins.property
    def after(self) -> typing.Optional[IReceiptRule]:
        '''An existing rule after which the new rule will be placed.

        :default: - The new rule is inserted at the beginning of the rule list.
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[IReceiptRule], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the rule is active.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the rule.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The recipient domains and email addresses that the receipt rule applies to.

        :default: - Match all recipients under all verified domains.
        '''
        result = self._values.get("recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether to scan for spam and viruses.

        :default: false
        '''
        result = self._values.get("scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional["TlsPolicy"]:
        '''Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

        :default: - Optional which will not check for TLS.
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional["TlsPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.ReceiptRuleProps",
    jsii_struct_bases=[ReceiptRuleOptions],
    name_mapping={
        "actions": "actions",
        "after": "after",
        "enabled": "enabled",
        "receipt_rule_name": "receiptRuleName",
        "recipients": "recipients",
        "scan_enabled": "scanEnabled",
        "tls_policy": "tlsPolicy",
        "rule_set": "ruleSet",
    },
)
class ReceiptRuleProps(ReceiptRuleOptions):
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
        rule_set: IReceiptRuleSet,
    ) -> None:
        '''Construction properties for a ReceiptRule.

        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        :param rule_set: The name of the rule set that the receipt rule will be added to.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "rule_set": rule_set,
        }
        if actions is not None:
            self._values["actions"] = actions
        if after is not None:
            self._values["after"] = after
        if enabled is not None:
            self._values["enabled"] = enabled
        if receipt_rule_name is not None:
            self._values["receipt_rule_name"] = receipt_rule_name
        if recipients is not None:
            self._values["recipients"] = recipients
        if scan_enabled is not None:
            self._values["scan_enabled"] = scan_enabled
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[IReceiptRuleAction]]:
        '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        :default: - No actions.
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[IReceiptRuleAction]], result)

    @builtins.property
    def after(self) -> typing.Optional[IReceiptRule]:
        '''An existing rule after which the new rule will be placed.

        :default: - The new rule is inserted at the beginning of the rule list.
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[IReceiptRule], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the rule is active.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the rule.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The recipient domains and email addresses that the receipt rule applies to.

        :default: - Match all recipients under all verified domains.
        '''
        result = self._values.get("recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether to scan for spam and viruses.

        :default: false
        '''
        result = self._values.get("scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional["TlsPolicy"]:
        '''Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

        :default: - Optional which will not check for TLS.
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional["TlsPolicy"], result)

    @builtins.property
    def rule_set(self) -> IReceiptRuleSet:
        '''The name of the rule set that the receipt rule will be added to.'''
        result = self._values.get("rule_set")
        assert result is not None, "Required property 'rule_set' is missing"
        return typing.cast(IReceiptRuleSet, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IReceiptRuleSet)
class ReceiptRuleSet(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.ReceiptRuleSet",
):
    '''A new receipt rule set.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        drop_spam: typing.Optional[builtins.bool] = None,
        receipt_rule_set_name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Sequence[ReceiptRuleOptions]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param drop_spam: Whether to add a first rule to stop processing messages that have at least one spam indicator. Default: false
        :param receipt_rule_set_name: The name for the receipt rule set. Default: - A CloudFormation generated name.
        :param rules: The list of rules to add to this rule set. Rules are added in the same order as they appear in the list. Default: - No rules are added to the rule set.
        '''
        props = ReceiptRuleSetProps(
            drop_spam=drop_spam,
            receipt_rule_set_name=receipt_rule_set_name,
            rules=rules,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromReceiptRuleSetName") # type: ignore[misc]
    @builtins.classmethod
    def from_receipt_rule_set_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        receipt_rule_set_name: builtins.str,
    ) -> IReceiptRuleSet:
        '''Import an exported receipt rule set.

        :param scope: -
        :param id: -
        :param receipt_rule_set_name: -
        '''
        return typing.cast(IReceiptRuleSet, jsii.sinvoke(cls, "fromReceiptRuleSetName", [scope, id, receipt_rule_set_name]))

    @jsii.member(jsii_name="addDropSpamRule")
    def _add_drop_spam_rule(self) -> None:
        '''Adds a drop spam rule.'''
        return typing.cast(None, jsii.invoke(self, "addDropSpamRule", []))

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        id: builtins.str,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> ReceiptRule:
        '''Adds a new receipt rule in this rule set.

        The new rule is added after
        the last added rule unless ``after`` is specified.

        :param id: -
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        options = ReceiptRuleOptions(
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        return typing.cast(ReceiptRule, jsii.invoke(self, "addRule", [id, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="receiptRuleSetName")
    def receipt_rule_set_name(self) -> builtins.str:
        '''The receipt rule set name.'''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleSetName"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.ReceiptRuleSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "drop_spam": "dropSpam",
        "receipt_rule_set_name": "receiptRuleSetName",
        "rules": "rules",
    },
)
class ReceiptRuleSetProps:
    def __init__(
        self,
        *,
        drop_spam: typing.Optional[builtins.bool] = None,
        receipt_rule_set_name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Sequence[ReceiptRuleOptions]] = None,
    ) -> None:
        '''Construction properties for a ReceiptRuleSet.

        :param drop_spam: Whether to add a first rule to stop processing messages that have at least one spam indicator. Default: false
        :param receipt_rule_set_name: The name for the receipt rule set. Default: - A CloudFormation generated name.
        :param rules: The list of rules to add to this rule set. Rules are added in the same order as they appear in the list. Default: - No rules are added to the rule set.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if drop_spam is not None:
            self._values["drop_spam"] = drop_spam
        if receipt_rule_set_name is not None:
            self._values["receipt_rule_set_name"] = receipt_rule_set_name
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def drop_spam(self) -> typing.Optional[builtins.bool]:
        '''Whether to add a first rule to stop processing messages that have at least one spam indicator.

        :default: false
        '''
        result = self._values.get("drop_spam")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_set_name(self) -> typing.Optional[builtins.str]:
        '''The name for the receipt rule set.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[ReceiptRuleOptions]]:
        '''The list of rules to add to this rule set.

        Rules are added in the same
        order as they appear in the list.

        :default: - No rules are added to the rule set.
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[ReceiptRuleOptions]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.S3ActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "kms_key_arn": "kmsKeyArn",
        "object_key_prefix": "objectKeyPrefix",
        "topic_arn": "topicArn",
    },
)
class S3ActionConfig:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        kms_key_arn: typing.Optional[builtins.str] = None,
        object_key_prefix: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''S3Action configuration.

        :param bucket_name: The name of the Amazon S3 bucket that you want to send incoming mail to.
        :param kms_key_arn: The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. Default: - Emails are not encrypted.
        :param object_key_prefix: The key prefix of the Amazon S3 bucket. Default: - No prefix.
        :param topic_arn: The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. Default: - No notification is sent to SNS.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if object_key_prefix is not None:
            self._values["object_key_prefix"] = object_key_prefix
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The name of the Amazon S3 bucket that you want to send incoming mail to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-bucketname
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket.

        :default: - Emails are not encrypted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The key prefix of the Amazon S3 bucket.

        :default: - No prefix.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-objectkeyprefix
        '''
        result = self._values.get("object_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.SNSActionConfig",
    jsii_struct_bases=[],
    name_mapping={"encoding": "encoding", "topic_arn": "topicArn"},
)
class SNSActionConfig:
    def __init__(
        self,
        *,
        encoding: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''SNSAction configuration.

        :param encoding: The encoding to use for the email within the Amazon SNS notification. Default: 'UTF-8'
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. Default: - No notification is sent to SNS.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if encoding is not None:
            self._values["encoding"] = encoding
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''The encoding to use for the email within the Amazon SNS notification.

        :default: 'UTF-8'

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-encoding
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SNSActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.StopActionConfig",
    jsii_struct_bases=[],
    name_mapping={"scope": "scope", "topic_arn": "topicArn"},
)
class StopActionConfig:
    def __init__(
        self,
        *,
        scope: builtins.str,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''StopAction configuration.

        :param scope: The scope of the StopAction. The only acceptable value is RuleSet.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. Default: - No notification is sent to SNS.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "scope": scope,
        }
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def scope(self) -> builtins.str:
        '''The scope of the StopAction.

        The only acceptable value is RuleSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StopActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-ses.TlsPolicy")
class TlsPolicy(enum.Enum):
    '''The type of TLS policy for a receipt rule.'''

    OPTIONAL = "OPTIONAL"
    '''Do not check for TLS.'''
    REQUIRE = "REQUIRE"
    '''Bounce emails that are not received over TLS.'''


class WhiteListReceiptFilter(
    AllowListReceiptFilter,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ses.WhiteListReceiptFilter",
):
    '''(deprecated) An allow list receipt filter.

    :deprecated: use ``AllowListReceiptFilter``

    :stability: deprecated
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ips: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ips: A list of ip addresses or ranges to allow list.

        :stability: deprecated
        '''
        props = WhiteListReceiptFilterProps(ips=ips)

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.WhiteListReceiptFilterProps",
    jsii_struct_bases=[AllowListReceiptFilterProps],
    name_mapping={"ips": "ips"},
)
class WhiteListReceiptFilterProps(AllowListReceiptFilterProps):
    def __init__(self, *, ips: typing.Sequence[builtins.str]) -> None:
        '''(deprecated) Construction properties for a WhiteListReceiptFilter.

        :param ips: A list of ip addresses or ranges to allow list.

        :deprecated: use ``AllowListReceiptFilterProps``

        :stability: deprecated
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "ips": ips,
        }

    @builtins.property
    def ips(self) -> typing.List[builtins.str]:
        '''A list of ip addresses or ranges to allow list.'''
        result = self._values.get("ips")
        assert result is not None, "Required property 'ips' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WhiteListReceiptFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.WorkmailActionConfig",
    jsii_struct_bases=[],
    name_mapping={"organization_arn": "organizationArn", "topic_arn": "topicArn"},
)
class WorkmailActionConfig:
    def __init__(
        self,
        *,
        organization_arn: builtins.str,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''WorkmailAction configuration.

        :param organization_arn: The Amazon Resource Name (ARN) of the Amazon WorkMail organization.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. Default: - No notification is sent to SNS.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "organization_arn": organization_arn,
        }
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def organization_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon WorkMail organization.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-organizationarn
        '''
        result = self._values.get("organization_arn")
        assert result is not None, "Required property 'organization_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkmailActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ses.DropSpamReceiptRuleProps",
    jsii_struct_bases=[ReceiptRuleProps],
    name_mapping={
        "actions": "actions",
        "after": "after",
        "enabled": "enabled",
        "receipt_rule_name": "receiptRuleName",
        "recipients": "recipients",
        "scan_enabled": "scanEnabled",
        "tls_policy": "tlsPolicy",
        "rule_set": "ruleSet",
    },
)
class DropSpamReceiptRuleProps(ReceiptRuleProps):
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional[TlsPolicy] = None,
        rule_set: IReceiptRuleSet,
    ) -> None:
        '''
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        :param rule_set: The name of the rule set that the receipt rule will be added to.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "rule_set": rule_set,
        }
        if actions is not None:
            self._values["actions"] = actions
        if after is not None:
            self._values["after"] = after
        if enabled is not None:
            self._values["enabled"] = enabled
        if receipt_rule_name is not None:
            self._values["receipt_rule_name"] = receipt_rule_name
        if recipients is not None:
            self._values["recipients"] = recipients
        if scan_enabled is not None:
            self._values["scan_enabled"] = scan_enabled
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[IReceiptRuleAction]]:
        '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        :default: - No actions.
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[IReceiptRuleAction]], result)

    @builtins.property
    def after(self) -> typing.Optional[IReceiptRule]:
        '''An existing rule after which the new rule will be placed.

        :default: - The new rule is inserted at the beginning of the rule list.
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[IReceiptRule], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the rule is active.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the rule.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The recipient domains and email addresses that the receipt rule applies to.

        :default: - Match all recipients under all verified domains.
        '''
        result = self._values.get("recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether to scan for spam and viruses.

        :default: false
        '''
        result = self._values.get("scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional[TlsPolicy]:
        '''Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

        :default: - Optional which will not check for TLS.
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional[TlsPolicy], result)

    @builtins.property
    def rule_set(self) -> IReceiptRuleSet:
        '''The name of the rule set that the receipt rule will be added to.'''
        result = self._values.get("rule_set")
        assert result is not None, "Required property 'rule_set' is missing"
        return typing.cast(IReceiptRuleSet, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DropSpamReceiptRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AddHeaderActionConfig",
    "AllowListReceiptFilter",
    "AllowListReceiptFilterProps",
    "BounceActionConfig",
    "CfnConfigurationSet",
    "CfnConfigurationSetEventDestination",
    "CfnConfigurationSetEventDestinationProps",
    "CfnConfigurationSetProps",
    "CfnContactList",
    "CfnContactListProps",
    "CfnReceiptFilter",
    "CfnReceiptFilterProps",
    "CfnReceiptRule",
    "CfnReceiptRuleProps",
    "CfnReceiptRuleSet",
    "CfnReceiptRuleSetProps",
    "CfnTemplate",
    "CfnTemplateProps",
    "DropSpamReceiptRule",
    "DropSpamReceiptRuleProps",
    "IReceiptRule",
    "IReceiptRuleAction",
    "IReceiptRuleSet",
    "LambdaActionConfig",
    "ReceiptFilter",
    "ReceiptFilterPolicy",
    "ReceiptFilterProps",
    "ReceiptRule",
    "ReceiptRuleActionConfig",
    "ReceiptRuleOptions",
    "ReceiptRuleProps",
    "ReceiptRuleSet",
    "ReceiptRuleSetProps",
    "S3ActionConfig",
    "SNSActionConfig",
    "StopActionConfig",
    "TlsPolicy",
    "WhiteListReceiptFilter",
    "WhiteListReceiptFilterProps",
    "WorkmailActionConfig",
]

publication.publish()
