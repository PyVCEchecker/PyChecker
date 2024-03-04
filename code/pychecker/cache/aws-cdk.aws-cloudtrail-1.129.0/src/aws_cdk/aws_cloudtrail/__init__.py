'''
# AWS CloudTrail Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

## Trail

AWS CloudTrail enables governance, compliance, and operational and risk auditing of your AWS account. Actions taken by
a user, role, or an AWS service are recorded as events in CloudTrail. Learn more at the [CloudTrail
documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

The `Trail` construct enables ongoing delivery of events as log files to an Amazon S3 bucket. Learn more about [Creating
a Trail for Your AWS Account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html).
The following code creates a simple CloudTrail for your account -

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
trail = cloudtrail.Trail(self, "CloudTrail")
```

By default, this will create a new S3 Bucket that CloudTrail will write to, and choose a few other reasonable defaults
such as turning on multi-region and global service events.
The defaults for each property and how to override them are all documented on the `TrailProps` interface.

## Log File Validation

In order to validate that the CloudTrail log file was not modified after CloudTrail delivered it, CloudTrail provides a
digital signature for each file. Learn more at [Validating CloudTrail Log File
Integrity](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html).

This is enabled on the `Trail` construct by default, but can be turned off by setting `enableFileValidation` to `false`.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
trail = cloudtrail.Trail(self, "CloudTrail",
    enable_file_validation=False
)
```

## Notifications

Amazon SNS notifications can be configured upon new log files containing Trail events are delivered to S3.
Learn more at [Configuring Amazon SNS Notifications for
CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html).
The following code configures an SNS topic to be notified -

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
topic = sns.Topic(self, "TrailTopic")
trail = cloudtrail.Trail(self, "CloudTrail",
    sns_topic=topic
)
```

## Service Integrations

Besides sending trail events to S3, they can also be configured to notify other AWS services -

### Amazon CloudWatch Logs

CloudTrail events can be delivered to a CloudWatch Logs LogGroup. By default, a new LogGroup is created with a
default retention setting. The following code enables sending CloudWatch logs but specifies a particular retention
period for the created Log Group.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
trail = cloudtrail.Trail(self, "CloudTrail",
    send_to_cloud_watch_logs=True,
    cloud_watch_logs_retention=logs.RetentionDays.FOUR_MONTHS
)
```

If you would like to use a specific log group instead, this can be configured via `cloudwatchLogGroup`.

### Amazon EventBridge

Amazon EventBridge rules can be configured to be triggered when CloudTrail events occur using the `Trail.onEvent()` API.
Using APIs available in `aws-events`, these events can be filtered to match to those that are of interest, either from
a specific service, account or time range. See [Events delivered via
CloudTrail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html#events-for-services-not-listed)
to learn more about the event structure for events from CloudTrail.

The following code filters events for S3 from a specific AWS account and triggers a lambda function.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
my_function_handler = lambda_.Function(self, "MyFunction",
    code=lambda_.Code.from_asset("resource/myfunction"),
    runtime=lambda_.Runtime.NODEJS_12_X,
    handler="index.handler"
)

event_rule = Trail.on_event(self, "MyCloudWatchEvent",
    target=event_targets.LambdaFunction(my_function_handler)
)

event_rule.add_event_pattern(
    account="123456789012",
    source="aws.s3"
)
```

## Multi-Region & Global Service Events

By default, a `Trail` is configured to deliver log files from multiple regions to a single S3 bucket for a given
account. This creates shadow trails (replication of the trails) in all of the other regions. Learn more about [How
CloudTrail Behaves Regionally](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-regional-and-global-services)
and about the [`IsMultiRegion`
property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail).

For most services, events are recorded in the region where the action occurred. For global services such as AWS IAM,
AWS STS, Amazon CloudFront, Route 53, etc., events are delivered to any trail that includes global services. Learn more
[About Global Service Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events).

Events for global services are turned on by default for `Trail` constructs in the CDK.

The following code disables multi-region trail delivery and trail delivery for global services for a specific `Trail` -

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
trail = cloudtrail.Trail(self, "CloudTrail",
    # ...
    is_multi_region_trail=False,
    include_global_service_events=False
)
```

## Events Types

**Management events** provide information about management operations that are performed on resources in your AWS
account. These are also known as control plane operations. Learn more about [Management
Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-events).

By default, a `Trail` logs all management events. However, they can be configured to either be turned off, or to only
log 'Read' or 'Write' events.

The following code configures the `Trail` to only track management events that are of type 'Read'.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
trail = cloudtrail.Trail(self, "CloudTrail",
    # ...
    management_events=ReadWriteType.READ_ONLY
)
```

**Data events** provide information about the resource operations performed on or in a resource. These are also known
as data plane operations. Learn more about [Data
Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-events).
By default, no data events are logged for a `Trail`.

AWS CloudTrail supports data event logging for Amazon S3 objects and AWS Lambda functions.

The `logAllS3DataEvents()` API configures the trail to log all S3 data events while the `addS3EventSelector()` API can
be used to configure logging of S3 data events for specific buckets and specific object prefix. The following code
configures logging of S3 data events for `fooBucket` and with object prefix `bar/`.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_cloudtrail as cloudtrail

trail = cloudtrail.Trail(self, "MyAmazingCloudTrail")

# Adds an event selector to the bucket foo
trail.add_s3_event_selector([
    bucket=foo_bucket,  # 'fooBucket' is of type s3.IBucket
    object_prefix="bar/"
])
```

Similarly, the `logAllLambdaDataEvents()` configures the trail to log all Lambda data events while the
`addLambdaEventSelector()` API can be used to configure logging for specific Lambda functions. The following code
configures logging of Lambda data events for a specific Function.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
trail = cloudtrail.Trail(self, "MyAmazingCloudTrail")
amazing_function = lambda_.Function(stack, "AnAmazingFunction",
    runtime=lambda_.Runtime.NODEJS_12_X,
    handler="hello.handler",
    code=lambda_.Code.from_asset("lambda")
)

# Add an event selector to log data events for the provided Lambda functions.
trail.add_lambda_event_selector([lambda_function])
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

import aws_cdk.aws_events
import aws_cdk.aws_kms
import aws_cdk.aws_lambda
import aws_cdk.aws_logs
import aws_cdk.aws_s3
import aws_cdk.aws_sns
import aws_cdk.core
import constructs


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloudtrail.AddEventSelectorOptions",
    jsii_struct_bases=[],
    name_mapping={
        "include_management_events": "includeManagementEvents",
        "read_write_type": "readWriteType",
    },
)
class AddEventSelectorOptions:
    def __init__(
        self,
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional["ReadWriteType"] = None,
    ) -> None:
        '''Options for adding an event selector.

        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if include_management_events is not None:
            self._values["include_management_events"] = include_management_events
        if read_write_type is not None:
            self._values["read_write_type"] = read_write_type

    @builtins.property
    def include_management_events(self) -> typing.Optional[builtins.bool]:
        '''Specifies whether the event selector includes management events for the trail.

        :default: true
        '''
        result = self._values.get("include_management_events")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def read_write_type(self) -> typing.Optional["ReadWriteType"]:
        '''Specifies whether to log read-only events, write-only events, or all events.

        :default: ReadWriteType.All
        '''
        result = self._values.get("read_write_type")
        return typing.cast(typing.Optional["ReadWriteType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddEventSelectorOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnTrail(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudtrail.CfnTrail",
):
    '''A CloudFormation ``AWS::CloudTrail::Trail``.

    :cloudformationResource: AWS::CloudTrail::Trail
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        is_logging: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        s3_bucket_name: builtins.str,
        cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
        cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
        enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        event_selectors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.EventSelectorProperty"]]]] = None,
        include_global_service_events: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        insight_selectors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.InsightSelectorProperty"]]]] = None,
        is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        is_organization_trail: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        sns_topic_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::CloudTrail::Trail``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param is_logging: ``AWS::CloudTrail::Trail.IsLogging``.
        :param s3_bucket_name: ``AWS::CloudTrail::Trail.S3BucketName``.
        :param cloud_watch_logs_log_group_arn: ``AWS::CloudTrail::Trail.CloudWatchLogsLogGroupArn``.
        :param cloud_watch_logs_role_arn: ``AWS::CloudTrail::Trail.CloudWatchLogsRoleArn``.
        :param enable_log_file_validation: ``AWS::CloudTrail::Trail.EnableLogFileValidation``.
        :param event_selectors: ``AWS::CloudTrail::Trail.EventSelectors``.
        :param include_global_service_events: ``AWS::CloudTrail::Trail.IncludeGlobalServiceEvents``.
        :param insight_selectors: ``AWS::CloudTrail::Trail.InsightSelectors``.
        :param is_multi_region_trail: ``AWS::CloudTrail::Trail.IsMultiRegionTrail``.
        :param is_organization_trail: ``AWS::CloudTrail::Trail.IsOrganizationTrail``.
        :param kms_key_id: ``AWS::CloudTrail::Trail.KMSKeyId``.
        :param s3_key_prefix: ``AWS::CloudTrail::Trail.S3KeyPrefix``.
        :param sns_topic_name: ``AWS::CloudTrail::Trail.SnsTopicName``.
        :param tags: ``AWS::CloudTrail::Trail.Tags``.
        :param trail_name: ``AWS::CloudTrail::Trail.TrailName``.
        '''
        props = CfnTrailProps(
            is_logging=is_logging,
            s3_bucket_name=s3_bucket_name,
            cloud_watch_logs_log_group_arn=cloud_watch_logs_log_group_arn,
            cloud_watch_logs_role_arn=cloud_watch_logs_role_arn,
            enable_log_file_validation=enable_log_file_validation,
            event_selectors=event_selectors,
            include_global_service_events=include_global_service_events,
            insight_selectors=insight_selectors,
            is_multi_region_trail=is_multi_region_trail,
            is_organization_trail=is_organization_trail,
            kms_key_id=kms_key_id,
            s3_key_prefix=s3_key_prefix,
            sns_topic_name=sns_topic_name,
            tags=tags,
            trail_name=trail_name,
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
    @jsii.member(jsii_name="attrSnsTopicArn")
    def attr_sns_topic_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: SnsTopicArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSnsTopicArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::CloudTrail::Trail.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="isLogging")
    def is_logging(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::CloudTrail::Trail.IsLogging``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "isLogging"))

    @is_logging.setter
    def is_logging(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "isLogging", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        '''``AWS::CloudTrail::Trail.S3BucketName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname
        '''
        return typing.cast(builtins.str, jsii.get(self, "s3BucketName"))

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: builtins.str) -> None:
        jsii.set(self, "s3BucketName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cloudWatchLogsLogGroupArn")
    def cloud_watch_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.CloudWatchLogsLogGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudWatchLogsLogGroupArn"))

    @cloud_watch_logs_log_group_arn.setter
    def cloud_watch_logs_log_group_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "cloudWatchLogsLogGroupArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cloudWatchLogsRoleArn")
    def cloud_watch_logs_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.CloudWatchLogsRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudWatchLogsRoleArn"))

    @cloud_watch_logs_role_arn.setter
    def cloud_watch_logs_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "cloudWatchLogsRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableLogFileValidation")
    def enable_log_file_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::CloudTrail::Trail.EnableLogFileValidation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enableLogFileValidation"))

    @enable_log_file_validation.setter
    def enable_log_file_validation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enableLogFileValidation", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="eventSelectors")
    def event_selectors(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.EventSelectorProperty"]]]]:
        '''``AWS::CloudTrail::Trail.EventSelectors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-eventselectors
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.EventSelectorProperty"]]]], jsii.get(self, "eventSelectors"))

    @event_selectors.setter
    def event_selectors(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.EventSelectorProperty"]]]],
    ) -> None:
        jsii.set(self, "eventSelectors", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="includeGlobalServiceEvents")
    def include_global_service_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::CloudTrail::Trail.IncludeGlobalServiceEvents``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "includeGlobalServiceEvents"))

    @include_global_service_events.setter
    def include_global_service_events(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "includeGlobalServiceEvents", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="insightSelectors")
    def insight_selectors(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.InsightSelectorProperty"]]]]:
        '''``AWS::CloudTrail::Trail.InsightSelectors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-insightselectors
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.InsightSelectorProperty"]]]], jsii.get(self, "insightSelectors"))

    @insight_selectors.setter
    def insight_selectors(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.InsightSelectorProperty"]]]],
    ) -> None:
        jsii.set(self, "insightSelectors", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="isMultiRegionTrail")
    def is_multi_region_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::CloudTrail::Trail.IsMultiRegionTrail``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "isMultiRegionTrail"))

    @is_multi_region_trail.setter
    def is_multi_region_trail(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "isMultiRegionTrail", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="isOrganizationTrail")
    def is_organization_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::CloudTrail::Trail.IsOrganizationTrail``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-isorganizationtrail
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "isOrganizationTrail"))

    @is_organization_trail.setter
    def is_organization_trail(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "isOrganizationTrail", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.KMSKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "kmsKeyId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3KeyPrefix")
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.S3KeyPrefix``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KeyPrefix"))

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "s3KeyPrefix", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snsTopicName")
    def sns_topic_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.SnsTopicName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicName"))

    @sns_topic_name.setter
    def sns_topic_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "snsTopicName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trailName")
    def trail_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.TrailName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-trailname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trailName"))

    @trail_name.setter
    def trail_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "trailName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-cloudtrail.CfnTrail.DataResourceProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "values": "values"},
    )
    class DataResourceProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param type: ``CfnTrail.DataResourceProperty.Type``.
            :param values: ``CfnTrail.DataResourceProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnTrail.DataResourceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnTrail.DataResourceProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-dataresource.html#cfn-cloudtrail-trail-dataresource-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-cloudtrail.CfnTrail.EventSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_resources": "dataResources",
            "exclude_management_event_sources": "excludeManagementEventSources",
            "include_management_events": "includeManagementEvents",
            "read_write_type": "readWriteType",
        },
    )
    class EventSelectorProperty:
        def __init__(
            self,
            *,
            data_resources: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.DataResourceProperty"]]]] = None,
            exclude_management_event_sources: typing.Optional[typing.Sequence[builtins.str]] = None,
            include_management_events: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            read_write_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_resources: ``CfnTrail.EventSelectorProperty.DataResources``.
            :param exclude_management_event_sources: ``CfnTrail.EventSelectorProperty.ExcludeManagementEventSources``.
            :param include_management_events: ``CfnTrail.EventSelectorProperty.IncludeManagementEvents``.
            :param read_write_type: ``CfnTrail.EventSelectorProperty.ReadWriteType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if data_resources is not None:
                self._values["data_resources"] = data_resources
            if exclude_management_event_sources is not None:
                self._values["exclude_management_event_sources"] = exclude_management_event_sources
            if include_management_events is not None:
                self._values["include_management_events"] = include_management_events
            if read_write_type is not None:
                self._values["read_write_type"] = read_write_type

        @builtins.property
        def data_resources(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.DataResourceProperty"]]]]:
            '''``CfnTrail.EventSelectorProperty.DataResources``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-dataresources
            '''
            result = self._values.get("data_resources")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTrail.DataResourceProperty"]]]], result)

        @builtins.property
        def exclude_management_event_sources(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnTrail.EventSelectorProperty.ExcludeManagementEventSources``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-excludemanagementeventsources
            '''
            result = self._values.get("exclude_management_event_sources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include_management_events(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnTrail.EventSelectorProperty.IncludeManagementEvents``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-includemanagementevents
            '''
            result = self._values.get("include_management_events")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def read_write_type(self) -> typing.Optional[builtins.str]:
            '''``CfnTrail.EventSelectorProperty.ReadWriteType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-eventselector.html#cfn-cloudtrail-trail-eventselector-readwritetype
            '''
            result = self._values.get("read_write_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-cloudtrail.CfnTrail.InsightSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"insight_type": "insightType"},
    )
    class InsightSelectorProperty:
        def __init__(
            self,
            *,
            insight_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param insight_type: ``CfnTrail.InsightSelectorProperty.InsightType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if insight_type is not None:
                self._values["insight_type"] = insight_type

        @builtins.property
        def insight_type(self) -> typing.Optional[builtins.str]:
            '''``CfnTrail.InsightSelectorProperty.InsightType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html#cfn-cloudtrail-trail-insightselector-insighttype
            '''
            result = self._values.get("insight_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InsightSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloudtrail.CfnTrailProps",
    jsii_struct_bases=[],
    name_mapping={
        "is_logging": "isLogging",
        "s3_bucket_name": "s3BucketName",
        "cloud_watch_logs_log_group_arn": "cloudWatchLogsLogGroupArn",
        "cloud_watch_logs_role_arn": "cloudWatchLogsRoleArn",
        "enable_log_file_validation": "enableLogFileValidation",
        "event_selectors": "eventSelectors",
        "include_global_service_events": "includeGlobalServiceEvents",
        "insight_selectors": "insightSelectors",
        "is_multi_region_trail": "isMultiRegionTrail",
        "is_organization_trail": "isOrganizationTrail",
        "kms_key_id": "kmsKeyId",
        "s3_key_prefix": "s3KeyPrefix",
        "sns_topic_name": "snsTopicName",
        "tags": "tags",
        "trail_name": "trailName",
    },
)
class CfnTrailProps:
    def __init__(
        self,
        *,
        is_logging: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        s3_bucket_name: builtins.str,
        cloud_watch_logs_log_group_arn: typing.Optional[builtins.str] = None,
        cloud_watch_logs_role_arn: typing.Optional[builtins.str] = None,
        enable_log_file_validation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        event_selectors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnTrail.EventSelectorProperty]]]] = None,
        include_global_service_events: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        insight_selectors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnTrail.InsightSelectorProperty]]]] = None,
        is_multi_region_trail: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        is_organization_trail: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        sns_topic_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CloudTrail::Trail``.

        :param is_logging: ``AWS::CloudTrail::Trail.IsLogging``.
        :param s3_bucket_name: ``AWS::CloudTrail::Trail.S3BucketName``.
        :param cloud_watch_logs_log_group_arn: ``AWS::CloudTrail::Trail.CloudWatchLogsLogGroupArn``.
        :param cloud_watch_logs_role_arn: ``AWS::CloudTrail::Trail.CloudWatchLogsRoleArn``.
        :param enable_log_file_validation: ``AWS::CloudTrail::Trail.EnableLogFileValidation``.
        :param event_selectors: ``AWS::CloudTrail::Trail.EventSelectors``.
        :param include_global_service_events: ``AWS::CloudTrail::Trail.IncludeGlobalServiceEvents``.
        :param insight_selectors: ``AWS::CloudTrail::Trail.InsightSelectors``.
        :param is_multi_region_trail: ``AWS::CloudTrail::Trail.IsMultiRegionTrail``.
        :param is_organization_trail: ``AWS::CloudTrail::Trail.IsOrganizationTrail``.
        :param kms_key_id: ``AWS::CloudTrail::Trail.KMSKeyId``.
        :param s3_key_prefix: ``AWS::CloudTrail::Trail.S3KeyPrefix``.
        :param sns_topic_name: ``AWS::CloudTrail::Trail.SnsTopicName``.
        :param tags: ``AWS::CloudTrail::Trail.Tags``.
        :param trail_name: ``AWS::CloudTrail::Trail.TrailName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "is_logging": is_logging,
            "s3_bucket_name": s3_bucket_name,
        }
        if cloud_watch_logs_log_group_arn is not None:
            self._values["cloud_watch_logs_log_group_arn"] = cloud_watch_logs_log_group_arn
        if cloud_watch_logs_role_arn is not None:
            self._values["cloud_watch_logs_role_arn"] = cloud_watch_logs_role_arn
        if enable_log_file_validation is not None:
            self._values["enable_log_file_validation"] = enable_log_file_validation
        if event_selectors is not None:
            self._values["event_selectors"] = event_selectors
        if include_global_service_events is not None:
            self._values["include_global_service_events"] = include_global_service_events
        if insight_selectors is not None:
            self._values["insight_selectors"] = insight_selectors
        if is_multi_region_trail is not None:
            self._values["is_multi_region_trail"] = is_multi_region_trail
        if is_organization_trail is not None:
            self._values["is_organization_trail"] = is_organization_trail
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix
        if sns_topic_name is not None:
            self._values["sns_topic_name"] = sns_topic_name
        if tags is not None:
            self._values["tags"] = tags
        if trail_name is not None:
            self._values["trail_name"] = trail_name

    @builtins.property
    def is_logging(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::CloudTrail::Trail.IsLogging``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-islogging
        '''
        result = self._values.get("is_logging")
        assert result is not None, "Required property 'is_logging' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def s3_bucket_name(self) -> builtins.str:
        '''``AWS::CloudTrail::Trail.S3BucketName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3bucketname
        '''
        result = self._values.get("s3_bucket_name")
        assert result is not None, "Required property 's3_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_watch_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.CloudWatchLogsLogGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsloggrouparn
        '''
        result = self._values.get("cloud_watch_logs_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_watch_logs_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.CloudWatchLogsRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-cloudwatchlogsrolearn
        '''
        result = self._values.get("cloud_watch_logs_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_log_file_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::CloudTrail::Trail.EnableLogFileValidation``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-enablelogfilevalidation
        '''
        result = self._values.get("enable_log_file_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def event_selectors(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTrail.EventSelectorProperty]]]]:
        '''``AWS::CloudTrail::Trail.EventSelectors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-eventselectors
        '''
        result = self._values.get("event_selectors")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTrail.EventSelectorProperty]]]], result)

    @builtins.property
    def include_global_service_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::CloudTrail::Trail.IncludeGlobalServiceEvents``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-includeglobalserviceevents
        '''
        result = self._values.get("include_global_service_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def insight_selectors(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTrail.InsightSelectorProperty]]]]:
        '''``AWS::CloudTrail::Trail.InsightSelectors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-insightselectors
        '''
        result = self._values.get("insight_selectors")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnTrail.InsightSelectorProperty]]]], result)

    @builtins.property
    def is_multi_region_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::CloudTrail::Trail.IsMultiRegionTrail``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-ismultiregiontrail
        '''
        result = self._values.get("is_multi_region_trail")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def is_organization_trail(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::CloudTrail::Trail.IsOrganizationTrail``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-isorganizationtrail
        '''
        result = self._values.get("is_organization_trail")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.KMSKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.S3KeyPrefix``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-s3keyprefix
        '''
        result = self._values.get("s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.SnsTopicName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-snstopicname
        '''
        result = self._values.get("sns_topic_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::CloudTrail::Trail.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def trail_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::CloudTrail::Trail.TrailName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html#cfn-cloudtrail-trail-trailname
        '''
        result = self._values.get("trail_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrailProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-cloudtrail.DataResourceType")
class DataResourceType(enum.Enum):
    '''Resource type for a data event.'''

    LAMBDA_FUNCTION = "LAMBDA_FUNCTION"
    '''Data resource type for Lambda function.'''
    S3_OBJECT = "S3_OBJECT"
    '''Data resource type for S3 objects.'''


@jsii.enum(jsii_type="@aws-cdk/aws-cloudtrail.ReadWriteType")
class ReadWriteType(enum.Enum):
    '''Types of events that CloudTrail can log.'''

    READ_ONLY = "READ_ONLY"
    '''Read-only events include API operations that read your resources, but don't make changes.

    For example, read-only events include the Amazon EC2 DescribeSecurityGroups
    and DescribeSubnets API operations.
    '''
    WRITE_ONLY = "WRITE_ONLY"
    '''Write-only events include API operations that modify (or might modify) your resources.

    For example, the Amazon EC2 RunInstances and TerminateInstances API
    operations modify your instances.
    '''
    ALL = "ALL"
    '''All events.'''
    NONE = "NONE"
    '''No events.'''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloudtrail.S3EventSelector",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "object_prefix": "objectPrefix"},
)
class S3EventSelector:
    def __init__(
        self,
        *,
        bucket: aws_cdk.aws_s3.IBucket,
        object_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Selecting an S3 bucket and an optional prefix to be logged for data events.

        :param bucket: S3 bucket.
        :param object_prefix: Data events for objects whose key matches this prefix will be logged. Default: - all objects
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if object_prefix is not None:
            self._values["object_prefix"] = object_prefix

    @builtins.property
    def bucket(self) -> aws_cdk.aws_s3.IBucket:
        '''S3 bucket.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(aws_cdk.aws_s3.IBucket, result)

    @builtins.property
    def object_prefix(self) -> typing.Optional[builtins.str]:
        '''Data events for objects whose key matches this prefix will be logged.

        :default: - all objects
        '''
        result = self._values.get("object_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3EventSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Trail(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudtrail.Trail",
):
    '''Cloud trail allows you to log events that happen in your AWS account For example:.

    import { CloudTrail } from '@aws-cdk/aws-cloudtrail'

    const cloudTrail = new CloudTrail(this, 'MyTrail');

    NOTE the above example creates an UNENCRYPTED bucket by default,
    If you are required to use an Encrypted bucket you can supply a preconfigured bucket
    via TrailProps
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        bucket: typing.Optional[aws_cdk.aws_s3.IBucket] = None,
        cloud_watch_log_group: typing.Optional[aws_cdk.aws_logs.ILogGroup] = None,
        cloud_watch_logs_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        enable_file_validation: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        include_global_service_events: typing.Optional[builtins.bool] = None,
        is_multi_region_trail: typing.Optional[builtins.bool] = None,
        kms_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        management_events: typing.Optional[ReadWriteType] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        send_to_cloud_watch_logs: typing.Optional[builtins.bool] = None,
        sns_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param bucket: The Amazon S3 bucket. Default: - if not supplied a bucket will be created with all the correct permisions
        :param cloud_watch_log_group: Log Group to which CloudTrail to push logs to. Ignored if sendToCloudWatchLogs is set to false. Default: - a new log group is created and used.
        :param cloud_watch_logs_retention: How long to retain logs in CloudWatchLogs. Ignored if sendToCloudWatchLogs is false or if cloudWatchLogGroup is set. Default: logs.RetentionDays.ONE_YEAR
        :param enable_file_validation: To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation. This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection. You can use the AWS CLI to validate the files in the location where CloudTrail delivered them. Default: true
        :param encryption_key: The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs. Default: - No encryption.
        :param include_global_service_events: For most services, events are recorded in the region where the action occurred. For global services such as AWS Identity and Access Management (IAM), AWS STS, Amazon CloudFront, and Route 53, events are delivered to any trail that includes global services, and are logged as occurring in US East (N. Virginia) Region. Default: true
        :param is_multi_region_trail: Whether or not this trail delivers log files from multiple regions to a single S3 bucket for a single account. Default: true
        :param kms_key: (deprecated) The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs. Default: - No encryption.
        :param management_events: When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails. Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group. This method sets the management configuration for this trail. Management events provide insight into management operations that are performed on resources in your AWS account. These are also known as control plane operations. Management events can also include non-API events that occur in your account. For example, when a user logs in to your account, CloudTrail logs the ConsoleLogin event. Default: ReadWriteType.ALL
        :param s3_key_prefix: An Amazon S3 object key prefix that precedes the name of all log files. Default: - No prefix.
        :param send_to_cloud_watch_logs: If CloudTrail pushes logs to CloudWatch Logs in addition to S3. Disabled for cost out of the box. Default: false
        :param sns_topic: SNS topic that is notified when new log files are published. Default: - No notifications.
        :param trail_name: The name of the trail. We recommend customers do not set an explicit name. Default: - AWS CloudFormation generated name.
        '''
        props = TrailProps(
            bucket=bucket,
            cloud_watch_log_group=cloud_watch_log_group,
            cloud_watch_logs_retention=cloud_watch_logs_retention,
            enable_file_validation=enable_file_validation,
            encryption_key=encryption_key,
            include_global_service_events=include_global_service_events,
            is_multi_region_trail=is_multi_region_trail,
            kms_key=kms_key,
            management_events=management_events,
            s3_key_prefix=s3_key_prefix,
            send_to_cloud_watch_logs=send_to_cloud_watch_logs,
            sns_topic=sns_topic,
            trail_name=trail_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="onEvent") # type: ignore[misc]
    @builtins.classmethod
    def on_event(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Create an event rule for when an event is recorded by any Trail in the account.

        Note that the event doesn't necessarily have to come from this Trail, it can
        be captured from any one.

        Be sure to filter the event further down using an event pattern.

        :param scope: -
        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.sinvoke(cls, "onEvent", [scope, id, options]))

    @jsii.member(jsii_name="addEventSelector")
    def add_event_selector(
        self,
        data_resource_type: DataResourceType,
        data_resource_values: typing.Sequence[builtins.str],
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        '''When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method adds an Event Selector for filtering events that match either S3 or Lambda function operations.

        Data events: These events provide insight into the resource operations performed on or within a resource.
        These are also known as data plane operations.

        :param data_resource_type: -
        :param data_resource_values: the list of data resource ARNs to include in logging (maximum 250 entries).
        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All
        '''
        options = AddEventSelectorOptions(
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return typing.cast(None, jsii.invoke(self, "addEventSelector", [data_resource_type, data_resource_values, options]))

    @jsii.member(jsii_name="addLambdaEventSelector")
    def add_lambda_event_selector(
        self,
        handlers: typing.Sequence[aws_cdk.aws_lambda.IFunction],
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        '''When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method adds a Lambda Data Event Selector for filtering events that match Lambda function operations.

        Data events: These events provide insight into the resource operations performed on or within a resource.
        These are also known as data plane operations.

        :param handlers: the list of lambda function handlers whose data events should be logged (maximum 250 entries).
        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All
        '''
        options = AddEventSelectorOptions(
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return typing.cast(None, jsii.invoke(self, "addLambdaEventSelector", [handlers, options]))

    @jsii.member(jsii_name="addS3EventSelector")
    def add_s3_event_selector(
        self,
        s3_selector: typing.Sequence[S3EventSelector],
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        '''When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method adds an S3 Data Event Selector for filtering events that match S3 operations.

        Data events: These events provide insight into the resource operations performed on or within a resource.
        These are also known as data plane operations.

        :param s3_selector: the list of S3 bucket with optional prefix to include in logging (maximum 250 entries).
        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All
        '''
        options = AddEventSelectorOptions(
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return typing.cast(None, jsii.invoke(self, "addS3EventSelector", [s3_selector, options]))

    @jsii.member(jsii_name="logAllLambdaDataEvents")
    def log_all_lambda_data_events(
        self,
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        '''Log all Lamda data events for all lambda functions the account.

        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :default: false

        :see: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html
        '''
        options = AddEventSelectorOptions(
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return typing.cast(None, jsii.invoke(self, "logAllLambdaDataEvents", [options]))

    @jsii.member(jsii_name="logAllS3DataEvents")
    def log_all_s3_data_events(
        self,
        *,
        include_management_events: typing.Optional[builtins.bool] = None,
        read_write_type: typing.Optional[ReadWriteType] = None,
    ) -> None:
        '''Log all S3 data events for all objects for all buckets in the account.

        :param include_management_events: Specifies whether the event selector includes management events for the trail. Default: true
        :param read_write_type: Specifies whether to log read-only events, write-only events, or all events. Default: ReadWriteType.All

        :default: false

        :see: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html
        '''
        options = AddEventSelectorOptions(
            include_management_events=include_management_events,
            read_write_type=read_write_type,
        )

        return typing.cast(None, jsii.invoke(self, "logAllS3DataEvents", [options]))

    @jsii.member(jsii_name="onCloudTrailEvent")
    def on_cloud_trail_event(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''(deprecated) Create an event rule for when an event is recorded by any Trail in the account.

        Note that the event doesn't necessarily have to come from this Trail, it can
        be captured from any one.

        Be sure to filter the event further down using an event pattern.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        :deprecated: - use Trail.onEvent()

        :stability: deprecated
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onCloudTrailEvent", [id, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trailArn")
    def trail_arn(self) -> builtins.str:
        '''ARN of the CloudTrail trail i.e. arn:aws:cloudtrail:us-east-2:123456789012:trail/myCloudTrail.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "trailArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="trailSnsTopicArn")
    def trail_sns_topic_arn(self) -> builtins.str:
        '''ARN of the Amazon SNS topic that's associated with the CloudTrail trail, i.e. arn:aws:sns:us-east-2:123456789012:mySNSTopic.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "trailSnsTopicArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> typing.Optional[aws_cdk.aws_logs.ILogGroup]:
        '''The CloudWatch log group to which CloudTrail events are sent.

        ``undefined`` if ``sendToCloudWatchLogs`` property is false.
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_logs.ILogGroup], jsii.get(self, "logGroup"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloudtrail.TrailProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "cloud_watch_log_group": "cloudWatchLogGroup",
        "cloud_watch_logs_retention": "cloudWatchLogsRetention",
        "enable_file_validation": "enableFileValidation",
        "encryption_key": "encryptionKey",
        "include_global_service_events": "includeGlobalServiceEvents",
        "is_multi_region_trail": "isMultiRegionTrail",
        "kms_key": "kmsKey",
        "management_events": "managementEvents",
        "s3_key_prefix": "s3KeyPrefix",
        "send_to_cloud_watch_logs": "sendToCloudWatchLogs",
        "sns_topic": "snsTopic",
        "trail_name": "trailName",
    },
)
class TrailProps:
    def __init__(
        self,
        *,
        bucket: typing.Optional[aws_cdk.aws_s3.IBucket] = None,
        cloud_watch_log_group: typing.Optional[aws_cdk.aws_logs.ILogGroup] = None,
        cloud_watch_logs_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        enable_file_validation: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        include_global_service_events: typing.Optional[builtins.bool] = None,
        is_multi_region_trail: typing.Optional[builtins.bool] = None,
        kms_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        management_events: typing.Optional[ReadWriteType] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        send_to_cloud_watch_logs: typing.Optional[builtins.bool] = None,
        sns_topic: typing.Optional[aws_cdk.aws_sns.ITopic] = None,
        trail_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for an AWS CloudTrail trail.

        :param bucket: The Amazon S3 bucket. Default: - if not supplied a bucket will be created with all the correct permisions
        :param cloud_watch_log_group: Log Group to which CloudTrail to push logs to. Ignored if sendToCloudWatchLogs is set to false. Default: - a new log group is created and used.
        :param cloud_watch_logs_retention: How long to retain logs in CloudWatchLogs. Ignored if sendToCloudWatchLogs is false or if cloudWatchLogGroup is set. Default: logs.RetentionDays.ONE_YEAR
        :param enable_file_validation: To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation. This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing. This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection. You can use the AWS CLI to validate the files in the location where CloudTrail delivered them. Default: true
        :param encryption_key: The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs. Default: - No encryption.
        :param include_global_service_events: For most services, events are recorded in the region where the action occurred. For global services such as AWS Identity and Access Management (IAM), AWS STS, Amazon CloudFront, and Route 53, events are delivered to any trail that includes global services, and are logged as occurring in US East (N. Virginia) Region. Default: true
        :param is_multi_region_trail: Whether or not this trail delivers log files from multiple regions to a single S3 bucket for a single account. Default: true
        :param kms_key: (deprecated) The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs. Default: - No encryption.
        :param management_events: When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails. Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group. This method sets the management configuration for this trail. Management events provide insight into management operations that are performed on resources in your AWS account. These are also known as control plane operations. Management events can also include non-API events that occur in your account. For example, when a user logs in to your account, CloudTrail logs the ConsoleLogin event. Default: ReadWriteType.ALL
        :param s3_key_prefix: An Amazon S3 object key prefix that precedes the name of all log files. Default: - No prefix.
        :param send_to_cloud_watch_logs: If CloudTrail pushes logs to CloudWatch Logs in addition to S3. Disabled for cost out of the box. Default: false
        :param sns_topic: SNS topic that is notified when new log files are published. Default: - No notifications.
        :param trail_name: The name of the trail. We recommend customers do not set an explicit name. Default: - AWS CloudFormation generated name.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket is not None:
            self._values["bucket"] = bucket
        if cloud_watch_log_group is not None:
            self._values["cloud_watch_log_group"] = cloud_watch_log_group
        if cloud_watch_logs_retention is not None:
            self._values["cloud_watch_logs_retention"] = cloud_watch_logs_retention
        if enable_file_validation is not None:
            self._values["enable_file_validation"] = enable_file_validation
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if include_global_service_events is not None:
            self._values["include_global_service_events"] = include_global_service_events
        if is_multi_region_trail is not None:
            self._values["is_multi_region_trail"] = is_multi_region_trail
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if management_events is not None:
            self._values["management_events"] = management_events
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix
        if send_to_cloud_watch_logs is not None:
            self._values["send_to_cloud_watch_logs"] = send_to_cloud_watch_logs
        if sns_topic is not None:
            self._values["sns_topic"] = sns_topic
        if trail_name is not None:
            self._values["trail_name"] = trail_name

    @builtins.property
    def bucket(self) -> typing.Optional[aws_cdk.aws_s3.IBucket]:
        '''The Amazon S3 bucket.

        :default: - if not supplied a bucket will be created with all the correct permisions
        '''
        result = self._values.get("bucket")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.IBucket], result)

    @builtins.property
    def cloud_watch_log_group(self) -> typing.Optional[aws_cdk.aws_logs.ILogGroup]:
        '''Log Group to which CloudTrail to push logs to.

        Ignored if sendToCloudWatchLogs is set to false.

        :default: - a new log group is created and used.
        '''
        result = self._values.get("cloud_watch_log_group")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.ILogGroup], result)

    @builtins.property
    def cloud_watch_logs_retention(
        self,
    ) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''How long to retain logs in CloudWatchLogs.

        Ignored if sendToCloudWatchLogs is false or if cloudWatchLogGroup is set.

        :default: logs.RetentionDays.ONE_YEAR
        '''
        result = self._values.get("cloud_watch_logs_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def enable_file_validation(self) -> typing.Optional[builtins.bool]:
        '''To determine whether a log file was modified, deleted, or unchanged after CloudTrail delivered it, you can use CloudTrail log file integrity validation.

        This feature is built using industry standard algorithms: SHA-256 for hashing and SHA-256 with RSA for digital signing.
        This makes it computationally infeasible to modify, delete or forge CloudTrail log files without detection.
        You can use the AWS CLI to validate the files in the location where CloudTrail delivered them.

        :default: true
        '''
        result = self._values.get("enable_file_validation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        '''The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs.

        :default: - No encryption.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], result)

    @builtins.property
    def include_global_service_events(self) -> typing.Optional[builtins.bool]:
        '''For most services, events are recorded in the region where the action occurred.

        For global services such as AWS Identity and Access Management (IAM), AWS STS, Amazon CloudFront, and Route 53,
        events are delivered to any trail that includes global services, and are logged as occurring in US East (N. Virginia) Region.

        :default: true
        '''
        result = self._values.get("include_global_service_events")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_multi_region_trail(self) -> typing.Optional[builtins.bool]:
        '''Whether or not this trail delivers log files from multiple regions to a single S3 bucket for a single account.

        :default: true
        '''
        result = self._values.get("is_multi_region_trail")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        '''(deprecated) The AWS Key Management Service (AWS KMS) key ID that you want to use to encrypt CloudTrail logs.

        :default: - No encryption.

        :deprecated: - use encryptionKey instead.

        :stability: deprecated
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], result)

    @builtins.property
    def management_events(self) -> typing.Optional[ReadWriteType]:
        '''When an event occurs in your account, CloudTrail evaluates whether the event matches the settings for your trails.

        Only events that match your trail settings are delivered to your Amazon S3 bucket and Amazon CloudWatch Logs log group.

        This method sets the management configuration for this trail.

        Management events provide insight into management operations that are performed on resources in your AWS account.
        These are also known as control plane operations.
        Management events can also include non-API events that occur in your account.
        For example, when a user logs in to your account, CloudTrail logs the ConsoleLogin event.

        :default: ReadWriteType.ALL
        '''
        result = self._values.get("management_events")
        return typing.cast(typing.Optional[ReadWriteType], result)

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''An Amazon S3 object key prefix that precedes the name of all log files.

        :default: - No prefix.
        '''
        result = self._values.get("s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def send_to_cloud_watch_logs(self) -> typing.Optional[builtins.bool]:
        '''If CloudTrail pushes logs to CloudWatch Logs in addition to S3.

        Disabled for cost out of the box.

        :default: false
        '''
        result = self._values.get("send_to_cloud_watch_logs")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sns_topic(self) -> typing.Optional[aws_cdk.aws_sns.ITopic]:
        '''SNS topic that is notified when new log files are published.

        :default: - No notifications.
        '''
        result = self._values.get("sns_topic")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.ITopic], result)

    @builtins.property
    def trail_name(self) -> typing.Optional[builtins.str]:
        '''The name of the trail.

        We recommend customers do not set an explicit name.

        :default: - AWS CloudFormation generated name.
        '''
        result = self._values.get("trail_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrailProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AddEventSelectorOptions",
    "CfnTrail",
    "CfnTrailProps",
    "DataResourceType",
    "ReadWriteType",
    "S3EventSelector",
    "Trail",
    "TrailProps",
]

publication.publish()
