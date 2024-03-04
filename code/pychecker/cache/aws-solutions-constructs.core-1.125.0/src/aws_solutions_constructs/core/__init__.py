'''
# core module

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

| **Reference Documentation**:| <span style="font-weight: normal">https://docs.aws.amazon.com/solutions/latest/constructs/</span>|
|:-------------|:-------------|

<div style="height:8px"></div>

The core library includes the basic building blocks of the AWS Solutions Constructs Library. It defines the core classes that are used in the rest of the AWS Solutions Constructs Library.

## Default Properties for AWS CDK Constructs

Core library sets the default properties for the AWS CDK Constructs used by the AWS Solutions Constructs Library constructs.

For example, the following is the snippet of default properties for S3 Bucket construct created by AWS Solutions Constructs. By default, it will turn on the server-side encryption, bucket versioning, block all public access and setup the S3 access logging.

```
{
  encryption: s3.BucketEncryption.S3_MANAGED,
  versioned: true,
  blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
  removalPolicy: RemovalPolicy.RETAIN,
  serverAccessLogsBucket: loggingBucket
}
```

## Override the default properties

The default properties set by the Core library can be overridden by user provided properties. For example, the user can override the Amazon S3 Block Public Access property to meet specific requirements.

```
  const stack = new cdk.Stack();

  const props: CloudFrontToS3Props = {
    bucketProps: {
      blockPublicAccess: {
        blockPublicAcls: false,
        blockPublicPolicy: true,
        ignorePublicAcls: false,
        restrictPublicBuckets: true
      }
    }
  };

  new CloudFrontToS3(stack, 'test-cloudfront-s3', props);

  expect(stack).toHaveResource("AWS::S3::Bucket", {
    PublicAccessBlockConfiguration: {
      BlockPublicAcls: false,
      BlockPublicPolicy: true,
      IgnorePublicAcls: false,
      RestrictPublicBuckets: true
    },
  });
```

## Property override warnings

When a default property from the Core library is overridden by a user-provided property, Constructs will emit one or more warning messages to the console highlighting the change(s). These messages are intended to provide situational awareness to the user and prevent unintentional overrides that could create security risks. These messages will appear whenever deployment/build-related commands are executed, including `cdk deploy`, `cdk synth`, `npm test`, etc.

Example message:
`AWS_CONSTRUCTS_WARNING: An override has been provided for the property: BillingMode. Default value: 'PAY_PER_REQUEST'. You provided: 'PROVISIONED'.`

#### Toggling override warnings

Override warning messages are enabled by default, but can be explicitly turned on/off using the `overrideWarningsEnabled` shell variable.

* To explicitly <u>turn off</u> override warnings, run `export overrideWarningsEnabled=false`.
* To explicitly <u>turn on</u> override warnings, run `export overrideWarningsEnabled=true`.
* To revert to the default, run `unset overrideWarningsEnabled`.
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

import aws_cdk.aws_apigateway
import aws_cdk.aws_cognito
import aws_cdk.aws_dynamodb
import aws_cdk.aws_ec2
import aws_cdk.aws_events
import aws_cdk.aws_glue
import aws_cdk.aws_iam
import aws_cdk.aws_kinesis
import aws_cdk.aws_kinesisfirehose
import aws_cdk.aws_kms
import aws_cdk.aws_lambda
import aws_cdk.aws_lambda_event_sources
import aws_cdk.aws_mediastore
import aws_cdk.aws_s3
import aws_cdk.aws_sagemaker
import aws_cdk.aws_secretsmanager
import aws_cdk.aws_sns
import aws_cdk.aws_sqs
import aws_cdk.aws_wafv2


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.AddProxyMethodToApiResourceInputParams",
    jsii_struct_bases=[],
    name_mapping={
        "api_gateway_role": "apiGatewayRole",
        "api_method": "apiMethod",
        "api_resource": "apiResource",
        "request_template": "requestTemplate",
        "service": "service",
        "action": "action",
        "aws_integration_props": "awsIntegrationProps",
        "content_type": "contentType",
        "method_options": "methodOptions",
        "path": "path",
        "request_model": "requestModel",
        "request_validator": "requestValidator",
    },
)
class AddProxyMethodToApiResourceInputParams:
    def __init__(
        self,
        *,
        api_gateway_role: aws_cdk.aws_iam.IRole,
        api_method: builtins.str,
        api_resource: aws_cdk.aws_apigateway.IResource,
        request_template: builtins.str,
        service: builtins.str,
        action: typing.Optional[builtins.str] = None,
        aws_integration_props: typing.Any = None,
        content_type: typing.Optional[builtins.str] = None,
        method_options: typing.Optional[aws_cdk.aws_apigateway.MethodOptions] = None,
        path: typing.Optional[builtins.str] = None,
        request_model: typing.Optional[typing.Mapping[builtins.str, aws_cdk.aws_apigateway.IModel]] = None,
        request_validator: typing.Optional[aws_cdk.aws_apigateway.IRequestValidator] = None,
    ) -> None:
        '''
        :param api_gateway_role: -
        :param api_method: -
        :param api_resource: -
        :param request_template: -
        :param service: -
        :param action: -
        :param aws_integration_props: -
        :param content_type: -
        :param method_options: -
        :param path: -
        :param request_model: -
        :param request_validator: -
        '''
        if isinstance(method_options, dict):
            method_options = aws_cdk.aws_apigateway.MethodOptions(**method_options)
        self._values: typing.Dict[str, typing.Any] = {
            "api_gateway_role": api_gateway_role,
            "api_method": api_method,
            "api_resource": api_resource,
            "request_template": request_template,
            "service": service,
        }
        if action is not None:
            self._values["action"] = action
        if aws_integration_props is not None:
            self._values["aws_integration_props"] = aws_integration_props
        if content_type is not None:
            self._values["content_type"] = content_type
        if method_options is not None:
            self._values["method_options"] = method_options
        if path is not None:
            self._values["path"] = path
        if request_model is not None:
            self._values["request_model"] = request_model
        if request_validator is not None:
            self._values["request_validator"] = request_validator

    @builtins.property
    def api_gateway_role(self) -> aws_cdk.aws_iam.IRole:
        result = self._values.get("api_gateway_role")
        assert result is not None, "Required property 'api_gateway_role' is missing"
        return typing.cast(aws_cdk.aws_iam.IRole, result)

    @builtins.property
    def api_method(self) -> builtins.str:
        result = self._values.get("api_method")
        assert result is not None, "Required property 'api_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_resource(self) -> aws_cdk.aws_apigateway.IResource:
        result = self._values.get("api_resource")
        assert result is not None, "Required property 'api_resource' is missing"
        return typing.cast(aws_cdk.aws_apigateway.IResource, result)

    @builtins.property
    def request_template(self) -> builtins.str:
        result = self._values.get("request_template")
        assert result is not None, "Required property 'request_template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aws_integration_props(self) -> typing.Any:
        result = self._values.get("aws_integration_props")
        return typing.cast(typing.Any, result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def method_options(self) -> typing.Optional[aws_cdk.aws_apigateway.MethodOptions]:
        result = self._values.get("method_options")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.MethodOptions], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_model(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, aws_cdk.aws_apigateway.IModel]]:
        result = self._values.get("request_model")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, aws_cdk.aws_apigateway.IModel]], result)

    @builtins.property
    def request_validator(
        self,
    ) -> typing.Optional[aws_cdk.aws_apigateway.IRequestValidator]:
        result = self._values.get("request_validator")
        return typing.cast(typing.Optional[aws_cdk.aws_apigateway.IRequestValidator], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddProxyMethodToApiResourceInputParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildDeadLetterQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "dead_letter_queue_props": "deadLetterQueueProps",
        "deploy_dead_letter_queue": "deployDeadLetterQueue",
        "existing_queue_obj": "existingQueueObj",
        "max_receive_count": "maxReceiveCount",
    },
)
class BuildDeadLetterQueueProps:
    def __init__(
        self,
        *,
        dead_letter_queue_props: typing.Optional[aws_cdk.aws_sqs.QueueProps] = None,
        deploy_dead_letter_queue: typing.Optional[builtins.bool] = None,
        existing_queue_obj: typing.Optional[aws_cdk.aws_sqs.Queue] = None,
        max_receive_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dead_letter_queue_props: Optional user provided properties for the dead letter queue. Default: - Default props are used
        :param deploy_dead_letter_queue: Whether to deploy a secondary queue to be used as a dead letter queue. Default: - required field.
        :param existing_queue_obj: Existing instance of SQS queue object, providing both this and queueProps will cause an error. Default: - None.
        :param max_receive_count: The number of times a message can be unsuccessfully dequeued before being moved to the dead letter queue. Default: - Default props are used
        '''
        if isinstance(dead_letter_queue_props, dict):
            dead_letter_queue_props = aws_cdk.aws_sqs.QueueProps(**dead_letter_queue_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue_props is not None:
            self._values["dead_letter_queue_props"] = dead_letter_queue_props
        if deploy_dead_letter_queue is not None:
            self._values["deploy_dead_letter_queue"] = deploy_dead_letter_queue
        if existing_queue_obj is not None:
            self._values["existing_queue_obj"] = existing_queue_obj
        if max_receive_count is not None:
            self._values["max_receive_count"] = max_receive_count

    @builtins.property
    def dead_letter_queue_props(self) -> typing.Optional[aws_cdk.aws_sqs.QueueProps]:
        '''Optional user provided properties for the dead letter queue.

        :default: - Default props are used
        '''
        result = self._values.get("dead_letter_queue_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.QueueProps], result)

    @builtins.property
    def deploy_dead_letter_queue(self) -> typing.Optional[builtins.bool]:
        '''Whether to deploy a secondary queue to be used as a dead letter queue.

        :default: - required field.
        '''
        result = self._values.get("deploy_dead_letter_queue")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def existing_queue_obj(self) -> typing.Optional[aws_cdk.aws_sqs.Queue]:
        '''Existing instance of SQS queue object, providing both this and queueProps will cause an error.

        :default: - None.
        '''
        result = self._values.get("existing_queue_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.Queue], result)

    @builtins.property
    def max_receive_count(self) -> typing.Optional[jsii.Number]:
        '''The number of times a message can be unsuccessfully dequeued before being moved to the dead letter queue.

        :default: - Default props are used
        '''
        result = self._values.get("max_receive_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildDeadLetterQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildDynamoDBTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "dynamo_table_props": "dynamoTableProps",
        "existing_table_obj": "existingTableObj",
    },
)
class BuildDynamoDBTableProps:
    def __init__(
        self,
        *,
        dynamo_table_props: typing.Optional[aws_cdk.aws_dynamodb.TableProps] = None,
        existing_table_obj: typing.Optional[aws_cdk.aws_dynamodb.Table] = None,
    ) -> None:
        '''
        :param dynamo_table_props: Optional user provided props to override the default props. Default: - Default props are used
        :param existing_table_obj: Existing instance of dynamodb table object. Providing both this and ``dynamoTableProps`` will cause an error. Default: - None
        '''
        if isinstance(dynamo_table_props, dict):
            dynamo_table_props = aws_cdk.aws_dynamodb.TableProps(**dynamo_table_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if dynamo_table_props is not None:
            self._values["dynamo_table_props"] = dynamo_table_props
        if existing_table_obj is not None:
            self._values["existing_table_obj"] = existing_table_obj

    @builtins.property
    def dynamo_table_props(self) -> typing.Optional[aws_cdk.aws_dynamodb.TableProps]:
        '''Optional user provided props to override the default props.

        :default: - Default props are used
        '''
        result = self._values.get("dynamo_table_props")
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.TableProps], result)

    @builtins.property
    def existing_table_obj(self) -> typing.Optional[aws_cdk.aws_dynamodb.Table]:
        '''Existing instance of dynamodb table object.

        Providing both this and ``dynamoTableProps`` will cause an error.

        :default: - None
        '''
        result = self._values.get("existing_table_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.Table], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildDynamoDBTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildDynamoDBTableWithStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "dynamo_table_props": "dynamoTableProps",
        "existing_table_interface": "existingTableInterface",
    },
)
class BuildDynamoDBTableWithStreamProps:
    def __init__(
        self,
        *,
        dynamo_table_props: typing.Optional[aws_cdk.aws_dynamodb.TableProps] = None,
        existing_table_interface: typing.Optional[aws_cdk.aws_dynamodb.ITable] = None,
    ) -> None:
        '''
        :param dynamo_table_props: Optional user provided props to override the default props. Default: - Default props are used
        :param existing_table_interface: Existing instance of dynamodb table object. Providing both this and ``dynamoTableProps`` will cause an error. Default: - None
        '''
        if isinstance(dynamo_table_props, dict):
            dynamo_table_props = aws_cdk.aws_dynamodb.TableProps(**dynamo_table_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if dynamo_table_props is not None:
            self._values["dynamo_table_props"] = dynamo_table_props
        if existing_table_interface is not None:
            self._values["existing_table_interface"] = existing_table_interface

    @builtins.property
    def dynamo_table_props(self) -> typing.Optional[aws_cdk.aws_dynamodb.TableProps]:
        '''Optional user provided props to override the default props.

        :default: - Default props are used
        '''
        result = self._values.get("dynamo_table_props")
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.TableProps], result)

    @builtins.property
    def existing_table_interface(self) -> typing.Optional[aws_cdk.aws_dynamodb.ITable]:
        '''Existing instance of dynamodb table object.

        Providing both this and ``dynamoTableProps`` will cause an error.

        :default: - None
        '''
        result = self._values.get("existing_table_interface")
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.ITable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildDynamoDBTableWithStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildEventBusProps",
    jsii_struct_bases=[],
    name_mapping={
        "event_bus_props": "eventBusProps",
        "existing_event_bus_interface": "existingEventBusInterface",
    },
)
class BuildEventBusProps:
    def __init__(
        self,
        *,
        event_bus_props: typing.Optional[aws_cdk.aws_events.EventBusProps] = None,
        existing_event_bus_interface: typing.Optional[aws_cdk.aws_events.IEventBus] = None,
    ) -> None:
        '''
        :param event_bus_props: Optional user provided props to override the default props for the SNS topic. Default: - Default props are used.
        :param existing_event_bus_interface: Existing instance of SNS Topic object, providing both this and ``topicProps`` will cause an error. Default: - None.
        '''
        if isinstance(event_bus_props, dict):
            event_bus_props = aws_cdk.aws_events.EventBusProps(**event_bus_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if event_bus_props is not None:
            self._values["event_bus_props"] = event_bus_props
        if existing_event_bus_interface is not None:
            self._values["existing_event_bus_interface"] = existing_event_bus_interface

    @builtins.property
    def event_bus_props(self) -> typing.Optional[aws_cdk.aws_events.EventBusProps]:
        '''Optional user provided props to override the default props for the SNS topic.

        :default: - Default props are used.
        '''
        result = self._values.get("event_bus_props")
        return typing.cast(typing.Optional[aws_cdk.aws_events.EventBusProps], result)

    @builtins.property
    def existing_event_bus_interface(
        self,
    ) -> typing.Optional[aws_cdk.aws_events.IEventBus]:
        '''Existing instance of SNS Topic object, providing both this and ``topicProps`` will cause an error.

        :default: - None.
        '''
        result = self._values.get("existing_event_bus_interface")
        return typing.cast(typing.Optional[aws_cdk.aws_events.IEventBus], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildEventBusProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildGlueJobProps",
    jsii_struct_bases=[],
    name_mapping={
        "database": "database",
        "table": "table",
        "existing_cfn_job": "existingCfnJob",
        "glue_job_props": "glueJobProps",
        "output_data_store": "outputDataStore",
    },
)
class BuildGlueJobProps:
    def __init__(
        self,
        *,
        database: aws_cdk.aws_glue.CfnDatabase,
        table: aws_cdk.aws_glue.CfnTable,
        existing_cfn_job: typing.Optional[aws_cdk.aws_glue.CfnJob] = None,
        glue_job_props: typing.Any = None,
        output_data_store: typing.Optional["SinkDataStoreProps"] = None,
    ) -> None:
        '''
        :param database: AWS Glue database.
        :param table: AWS Glue table.
        :param existing_cfn_job: Existing instance of the S3 bucket object, if this is set then the script location is ignored.
        :param glue_job_props: Glue ETL job properties.
        :param output_data_store: Output storage options.
        '''
        if isinstance(output_data_store, dict):
            output_data_store = SinkDataStoreProps(**output_data_store)
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "table": table,
        }
        if existing_cfn_job is not None:
            self._values["existing_cfn_job"] = existing_cfn_job
        if glue_job_props is not None:
            self._values["glue_job_props"] = glue_job_props
        if output_data_store is not None:
            self._values["output_data_store"] = output_data_store

    @builtins.property
    def database(self) -> aws_cdk.aws_glue.CfnDatabase:
        '''AWS Glue database.'''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(aws_cdk.aws_glue.CfnDatabase, result)

    @builtins.property
    def table(self) -> aws_cdk.aws_glue.CfnTable:
        '''AWS Glue table.'''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(aws_cdk.aws_glue.CfnTable, result)

    @builtins.property
    def existing_cfn_job(self) -> typing.Optional[aws_cdk.aws_glue.CfnJob]:
        '''Existing instance of the S3 bucket object, if this is set then the script location is ignored.'''
        result = self._values.get("existing_cfn_job")
        return typing.cast(typing.Optional[aws_cdk.aws_glue.CfnJob], result)

    @builtins.property
    def glue_job_props(self) -> typing.Any:
        '''Glue ETL job properties.'''
        result = self._values.get("glue_job_props")
        return typing.cast(typing.Any, result)

    @builtins.property
    def output_data_store(self) -> typing.Optional["SinkDataStoreProps"]:
        '''Output storage options.'''
        result = self._values.get("output_data_store")
        return typing.cast(typing.Optional["SinkDataStoreProps"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildGlueJobProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildKinesisAnalyticsAppProps",
    jsii_struct_bases=[],
    name_mapping={
        "kinesis_firehose": "kinesisFirehose",
        "kinesis_analytics_props": "kinesisAnalyticsProps",
    },
)
class BuildKinesisAnalyticsAppProps:
    def __init__(
        self,
        *,
        kinesis_firehose: aws_cdk.aws_kinesisfirehose.CfnDeliveryStream,
        kinesis_analytics_props: typing.Any = None,
    ) -> None:
        '''
        :param kinesis_firehose: A Kinesis Data Firehose for the Kinesis Streams application to connect to. Default: - Default props are used
        :param kinesis_analytics_props: Optional user provided props to override the default props for the Kinesis analytics app. Default: - Default props are used
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "kinesis_firehose": kinesis_firehose,
        }
        if kinesis_analytics_props is not None:
            self._values["kinesis_analytics_props"] = kinesis_analytics_props

    @builtins.property
    def kinesis_firehose(self) -> aws_cdk.aws_kinesisfirehose.CfnDeliveryStream:
        '''A Kinesis Data Firehose for the Kinesis Streams application to connect to.

        :default: - Default props are used
        '''
        result = self._values.get("kinesis_firehose")
        assert result is not None, "Required property 'kinesis_firehose' is missing"
        return typing.cast(aws_cdk.aws_kinesisfirehose.CfnDeliveryStream, result)

    @builtins.property
    def kinesis_analytics_props(self) -> typing.Any:
        '''Optional user provided props to override the default props for the Kinesis analytics app.

        :default: - Default props are used
        '''
        result = self._values.get("kinesis_analytics_props")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildKinesisAnalyticsAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildKinesisStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "existing_stream_obj": "existingStreamObj",
        "kinesis_stream_props": "kinesisStreamProps",
    },
)
class BuildKinesisStreamProps:
    def __init__(
        self,
        *,
        existing_stream_obj: typing.Optional[aws_cdk.aws_kinesis.Stream] = None,
        kinesis_stream_props: typing.Optional[aws_cdk.aws_kinesis.StreamProps] = None,
    ) -> None:
        '''
        :param existing_stream_obj: Existing instance of Kinesis Stream, providing both this and ``kinesisStreamProps`` will cause an error. Default: - None
        :param kinesis_stream_props: Optional user provided props to override the default props for the Kinesis stream. Default: - Default props are used.
        '''
        if isinstance(kinesis_stream_props, dict):
            kinesis_stream_props = aws_cdk.aws_kinesis.StreamProps(**kinesis_stream_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if existing_stream_obj is not None:
            self._values["existing_stream_obj"] = existing_stream_obj
        if kinesis_stream_props is not None:
            self._values["kinesis_stream_props"] = kinesis_stream_props

    @builtins.property
    def existing_stream_obj(self) -> typing.Optional[aws_cdk.aws_kinesis.Stream]:
        '''Existing instance of Kinesis Stream, providing both this and ``kinesisStreamProps`` will cause an error.

        :default: - None
        '''
        result = self._values.get("existing_stream_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_kinesis.Stream], result)

    @builtins.property
    def kinesis_stream_props(self) -> typing.Optional[aws_cdk.aws_kinesis.StreamProps]:
        '''Optional user provided props to override the default props for the Kinesis stream.

        :default: - Default props are used.
        '''
        result = self._values.get("kinesis_stream_props")
        return typing.cast(typing.Optional[aws_cdk.aws_kinesis.StreamProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildKinesisStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildLambdaFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "existing_lambda_obj": "existingLambdaObj",
        "lambda_function_props": "lambdaFunctionProps",
        "vpc": "vpc",
    },
)
class BuildLambdaFunctionProps:
    def __init__(
        self,
        *,
        existing_lambda_obj: typing.Optional[aws_cdk.aws_lambda.Function] = None,
        lambda_function_props: typing.Optional[aws_cdk.aws_lambda.FunctionProps] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param existing_lambda_obj: Existing instance of Lambda Function object, Providing both this and lambdaFunctionProps will cause an error. Default: - None
        :param lambda_function_props: User provided props to override the default props for the Lambda function. Default: - Default props are used
        :param vpc: A VPC where the Lambda function will access internal resources. Default: - none
        '''
        if isinstance(lambda_function_props, dict):
            lambda_function_props = aws_cdk.aws_lambda.FunctionProps(**lambda_function_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if existing_lambda_obj is not None:
            self._values["existing_lambda_obj"] = existing_lambda_obj
        if lambda_function_props is not None:
            self._values["lambda_function_props"] = lambda_function_props
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def existing_lambda_obj(self) -> typing.Optional[aws_cdk.aws_lambda.Function]:
        '''Existing instance of Lambda Function object, Providing both this and lambdaFunctionProps will cause an error.

        :default: - None
        '''
        result = self._values.get("existing_lambda_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.Function], result)

    @builtins.property
    def lambda_function_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.FunctionProps]:
        '''User provided props to override the default props for the Lambda function.

        :default: - Default props are used
        '''
        result = self._values.get("lambda_function_props")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.FunctionProps], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''A VPC where the Lambda function will access internal resources.

        :default: - none
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildLambdaFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "enable_encryption_with_customer_managed_key": "enableEncryptionWithCustomerManagedKey",
        "encryption_key": "encryptionKey",
        "encryption_key_props": "encryptionKeyProps",
        "existing_queue_obj": "existingQueueObj",
        "queue_props": "queueProps",
    },
)
class BuildQueueProps:
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.DeadLetterQueue] = None,
        enable_encryption_with_customer_managed_key: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
        encryption_key_props: typing.Optional[aws_cdk.aws_kms.KeyProps] = None,
        existing_queue_obj: typing.Optional[aws_cdk.aws_sqs.Queue] = None,
        queue_props: typing.Optional[aws_cdk.aws_sqs.QueueProps] = None,
    ) -> None:
        '''
        :param dead_letter_queue: Optional dead letter queue to pass bad requests to after the max receive count is reached. Default: - Default props are used.
        :param enable_encryption_with_customer_managed_key: Use a KMS Key, either managed by this CDK app, or imported. If importing an encryption key, it must be specified in the encryptionKey property for this construct. Default: - false (encryption enabled with AWS Managed KMS Key).
        :param encryption_key: An optional, imported encryption key to encrypt the SQS queue with. Default: - not specified.
        :param encryption_key_props: Optional user-provided props to override the default props for the encryption key. Default: - Ignored if encryptionKey is provided
        :param existing_queue_obj: Existing instance of SQS queue object, providing both this and queueProps will cause an error. Default: - None.
        :param queue_props: Optional user provided props to override the default props for the primary queue. Default: - Default props are used.
        '''
        if isinstance(dead_letter_queue, dict):
            dead_letter_queue = aws_cdk.aws_sqs.DeadLetterQueue(**dead_letter_queue)
        if isinstance(encryption_key_props, dict):
            encryption_key_props = aws_cdk.aws_kms.KeyProps(**encryption_key_props)
        if isinstance(queue_props, dict):
            queue_props = aws_cdk.aws_sqs.QueueProps(**queue_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if enable_encryption_with_customer_managed_key is not None:
            self._values["enable_encryption_with_customer_managed_key"] = enable_encryption_with_customer_managed_key
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if encryption_key_props is not None:
            self._values["encryption_key_props"] = encryption_key_props
        if existing_queue_obj is not None:
            self._values["existing_queue_obj"] = existing_queue_obj
        if queue_props is not None:
            self._values["queue_props"] = queue_props

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.DeadLetterQueue]:
        '''Optional dead letter queue to pass bad requests to after the max receive count is reached.

        :default: - Default props are used.
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.DeadLetterQueue], result)

    @builtins.property
    def enable_encryption_with_customer_managed_key(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Use a KMS Key, either managed by this CDK app, or imported.

        If importing an encryption key, it must be specified in
        the encryptionKey property for this construct.

        :default: - false (encryption enabled with AWS Managed KMS Key).
        '''
        result = self._values.get("enable_encryption_with_customer_managed_key")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.Key]:
        '''An optional, imported encryption key to encrypt the SQS queue with.

        :default: - not specified.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.Key], result)

    @builtins.property
    def encryption_key_props(self) -> typing.Optional[aws_cdk.aws_kms.KeyProps]:
        '''Optional user-provided props to override the default props for the encryption key.

        :default: - Ignored if encryptionKey is provided
        '''
        result = self._values.get("encryption_key_props")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.KeyProps], result)

    @builtins.property
    def existing_queue_obj(self) -> typing.Optional[aws_cdk.aws_sqs.Queue]:
        '''Existing instance of SQS queue object, providing both this and queueProps will cause an error.

        :default: - None.
        '''
        result = self._values.get("existing_queue_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.Queue], result)

    @builtins.property
    def queue_props(self) -> typing.Optional[aws_cdk.aws_sqs.QueueProps]:
        '''Optional user provided props to override the default props for the primary queue.

        :default: - Default props are used.
        '''
        result = self._values.get("queue_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.QueueProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildS3BucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_props": "bucketProps",
        "logging_bucket_props": "loggingBucketProps",
    },
)
class BuildS3BucketProps:
    def __init__(
        self,
        *,
        bucket_props: typing.Optional[aws_cdk.aws_s3.BucketProps] = None,
        logging_bucket_props: typing.Optional[aws_cdk.aws_s3.BucketProps] = None,
    ) -> None:
        '''
        :param bucket_props: User provided props to override the default props for the S3 Bucket. Default: - Default props are used
        :param logging_bucket_props: User provided props to override the default props for the S3 Logging Bucket. Default: - Default props are used
        '''
        if isinstance(bucket_props, dict):
            bucket_props = aws_cdk.aws_s3.BucketProps(**bucket_props)
        if isinstance(logging_bucket_props, dict):
            logging_bucket_props = aws_cdk.aws_s3.BucketProps(**logging_bucket_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_props is not None:
            self._values["bucket_props"] = bucket_props
        if logging_bucket_props is not None:
            self._values["logging_bucket_props"] = logging_bucket_props

    @builtins.property
    def bucket_props(self) -> typing.Optional[aws_cdk.aws_s3.BucketProps]:
        '''User provided props to override the default props for the S3 Bucket.

        :default: - Default props are used
        '''
        result = self._values.get("bucket_props")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.BucketProps], result)

    @builtins.property
    def logging_bucket_props(self) -> typing.Optional[aws_cdk.aws_s3.BucketProps]:
        '''User provided props to override the default props for the S3 Logging Bucket.

        :default: - Default props are used
        '''
        result = self._values.get("logging_bucket_props")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.BucketProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildS3BucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildSagemakerEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_config_props": "endpointConfigProps",
        "endpoint_props": "endpointProps",
        "existing_sagemaker_endpoint_obj": "existingSagemakerEndpointObj",
        "model_props": "modelProps",
        "vpc": "vpc",
    },
)
class BuildSagemakerEndpointProps:
    def __init__(
        self,
        *,
        endpoint_config_props: typing.Optional[aws_cdk.aws_sagemaker.CfnEndpointConfigProps] = None,
        endpoint_props: typing.Optional[aws_cdk.aws_sagemaker.CfnEndpointProps] = None,
        existing_sagemaker_endpoint_obj: typing.Optional[aws_cdk.aws_sagemaker.CfnEndpoint] = None,
        model_props: typing.Any = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param endpoint_config_props: User provided props to create Sagemaker Endpoint Configuration. Default: - None
        :param endpoint_props: User provided props to create Sagemaker Endpoint. Default: - None
        :param existing_sagemaker_endpoint_obj: Existing Sagemaker Enpoint object, if this is set then the modelProps, endpointConfigProps, and endpointProps are ignored. Default: - None
        :param model_props: User provided props to create Sagemaker Model. Default: - None
        :param vpc: A VPC where the Sagemaker Endpoint will be placed. Default: - None
        '''
        if isinstance(endpoint_config_props, dict):
            endpoint_config_props = aws_cdk.aws_sagemaker.CfnEndpointConfigProps(**endpoint_config_props)
        if isinstance(endpoint_props, dict):
            endpoint_props = aws_cdk.aws_sagemaker.CfnEndpointProps(**endpoint_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if endpoint_config_props is not None:
            self._values["endpoint_config_props"] = endpoint_config_props
        if endpoint_props is not None:
            self._values["endpoint_props"] = endpoint_props
        if existing_sagemaker_endpoint_obj is not None:
            self._values["existing_sagemaker_endpoint_obj"] = existing_sagemaker_endpoint_obj
        if model_props is not None:
            self._values["model_props"] = model_props
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def endpoint_config_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_sagemaker.CfnEndpointConfigProps]:
        '''User provided props to create Sagemaker Endpoint Configuration.

        :default: - None
        '''
        result = self._values.get("endpoint_config_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sagemaker.CfnEndpointConfigProps], result)

    @builtins.property
    def endpoint_props(self) -> typing.Optional[aws_cdk.aws_sagemaker.CfnEndpointProps]:
        '''User provided props to create Sagemaker Endpoint.

        :default: - None
        '''
        result = self._values.get("endpoint_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sagemaker.CfnEndpointProps], result)

    @builtins.property
    def existing_sagemaker_endpoint_obj(
        self,
    ) -> typing.Optional[aws_cdk.aws_sagemaker.CfnEndpoint]:
        '''Existing Sagemaker Enpoint object, if this is set then the modelProps, endpointConfigProps, and endpointProps are ignored.

        :default: - None
        '''
        result = self._values.get("existing_sagemaker_endpoint_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_sagemaker.CfnEndpoint], result)

    @builtins.property
    def model_props(self) -> typing.Any:
        '''User provided props to create Sagemaker Model.

        :default: - None
        '''
        result = self._values.get("model_props")
        return typing.cast(typing.Any, result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''A VPC where the Sagemaker Endpoint will be placed.

        :default: - None
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildSagemakerEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildSagemakerNotebookProps",
    jsii_struct_bases=[],
    name_mapping={
        "role": "role",
        "deploy_inside_vpc": "deployInsideVpc",
        "existing_notebook_obj": "existingNotebookObj",
        "sagemaker_notebook_props": "sagemakerNotebookProps",
    },
)
class BuildSagemakerNotebookProps:
    def __init__(
        self,
        *,
        role: aws_cdk.aws_iam.Role,
        deploy_inside_vpc: typing.Optional[builtins.bool] = None,
        existing_notebook_obj: typing.Optional[aws_cdk.aws_sagemaker.CfnNotebookInstance] = None,
        sagemaker_notebook_props: typing.Any = None,
    ) -> None:
        '''
        :param role: IAM Role Arn for Sagemaker NoteBookInstance. Default: - None
        :param deploy_inside_vpc: Optional user provided props to deploy inside vpc. Default: - true
        :param existing_notebook_obj: An optional, Existing instance of notebook object. If this is set then the sagemakerNotebookProps is ignored Default: - None
        :param sagemaker_notebook_props: Optional user provided props for CfnNotebookInstanceProps. Default: - Default props are used
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "role": role,
        }
        if deploy_inside_vpc is not None:
            self._values["deploy_inside_vpc"] = deploy_inside_vpc
        if existing_notebook_obj is not None:
            self._values["existing_notebook_obj"] = existing_notebook_obj
        if sagemaker_notebook_props is not None:
            self._values["sagemaker_notebook_props"] = sagemaker_notebook_props

    @builtins.property
    def role(self) -> aws_cdk.aws_iam.Role:
        '''IAM Role Arn for Sagemaker NoteBookInstance.

        :default: - None
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(aws_cdk.aws_iam.Role, result)

    @builtins.property
    def deploy_inside_vpc(self) -> typing.Optional[builtins.bool]:
        '''Optional user provided props to deploy inside vpc.

        :default: - true
        '''
        result = self._values.get("deploy_inside_vpc")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def existing_notebook_obj(
        self,
    ) -> typing.Optional[aws_cdk.aws_sagemaker.CfnNotebookInstance]:
        '''An optional, Existing instance of notebook object.

        If this is set then the sagemakerNotebookProps is ignored

        :default: - None
        '''
        result = self._values.get("existing_notebook_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_sagemaker.CfnNotebookInstance], result)

    @builtins.property
    def sagemaker_notebook_props(self) -> typing.Any:
        '''Optional user provided props for CfnNotebookInstanceProps.

        :default: - Default props are used
        '''
        result = self._values.get("sagemaker_notebook_props")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildSagemakerNotebookProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildTopicProps",
    jsii_struct_bases=[],
    name_mapping={
        "enable_encryption_with_customer_managed_key": "enableEncryptionWithCustomerManagedKey",
        "encryption_key": "encryptionKey",
        "encryption_key_props": "encryptionKeyProps",
        "existing_topic_obj": "existingTopicObj",
        "topic_props": "topicProps",
    },
)
class BuildTopicProps:
    def __init__(
        self,
        *,
        enable_encryption_with_customer_managed_key: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
        encryption_key_props: typing.Optional[aws_cdk.aws_kms.KeyProps] = None,
        existing_topic_obj: typing.Optional[aws_cdk.aws_sns.Topic] = None,
        topic_props: typing.Optional[aws_cdk.aws_sns.TopicProps] = None,
    ) -> None:
        '''
        :param enable_encryption_with_customer_managed_key: Use a Customer Managed KMS Key, either managed by this CDK app, or imported. If importing an encryption key, it must be specified in the encryptionKey property for this construct. Default: - false (encryption enabled with AWS Managed KMS Key).
        :param encryption_key: An optional, imported encryption key to encrypt the SNS topic with. Default: - not specified.
        :param encryption_key_props: Optional user-provided props to override the default props for the encryption key. Default: - Ignored if encryptionKey is provided
        :param existing_topic_obj: Existing instance of SNS Topic object, providing both this and ``topicProps`` will cause an error. Default: - None.
        :param topic_props: Optional user provided props to override the default props for the SNS topic. Default: - Default props are used.
        '''
        if isinstance(encryption_key_props, dict):
            encryption_key_props = aws_cdk.aws_kms.KeyProps(**encryption_key_props)
        if isinstance(topic_props, dict):
            topic_props = aws_cdk.aws_sns.TopicProps(**topic_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_encryption_with_customer_managed_key is not None:
            self._values["enable_encryption_with_customer_managed_key"] = enable_encryption_with_customer_managed_key
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if encryption_key_props is not None:
            self._values["encryption_key_props"] = encryption_key_props
        if existing_topic_obj is not None:
            self._values["existing_topic_obj"] = existing_topic_obj
        if topic_props is not None:
            self._values["topic_props"] = topic_props

    @builtins.property
    def enable_encryption_with_customer_managed_key(
        self,
    ) -> typing.Optional[builtins.bool]:
        '''Use a Customer Managed KMS Key, either managed by this CDK app, or imported.

        If importing an encryption key, it must be specified in
        the encryptionKey property for this construct.

        :default: - false (encryption enabled with AWS Managed KMS Key).
        '''
        result = self._values.get("enable_encryption_with_customer_managed_key")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.Key]:
        '''An optional, imported encryption key to encrypt the SNS topic with.

        :default: - not specified.
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.Key], result)

    @builtins.property
    def encryption_key_props(self) -> typing.Optional[aws_cdk.aws_kms.KeyProps]:
        '''Optional user-provided props to override the default props for the encryption key.

        :default: - Ignored if encryptionKey is provided
        '''
        result = self._values.get("encryption_key_props")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.KeyProps], result)

    @builtins.property
    def existing_topic_obj(self) -> typing.Optional[aws_cdk.aws_sns.Topic]:
        '''Existing instance of SNS Topic object, providing both this and ``topicProps`` will cause an error.

        :default: - None.
        '''
        result = self._values.get("existing_topic_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.Topic], result)

    @builtins.property
    def topic_props(self) -> typing.Optional[aws_cdk.aws_sns.TopicProps]:
        '''Optional user provided props to override the default props for the SNS topic.

        :default: - Default props are used.
        '''
        result = self._values.get("topic_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.TopicProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildTopicProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildVpcProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_vpc_props": "defaultVpcProps",
        "construct_vpc_props": "constructVpcProps",
        "existing_vpc": "existingVpc",
        "user_vpc_props": "userVpcProps",
    },
)
class BuildVpcProps:
    def __init__(
        self,
        *,
        default_vpc_props: aws_cdk.aws_ec2.VpcProps,
        construct_vpc_props: typing.Optional[aws_cdk.aws_ec2.VpcProps] = None,
        existing_vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        user_vpc_props: typing.Optional[aws_cdk.aws_ec2.VpcProps] = None,
    ) -> None:
        '''
        :param default_vpc_props: One of the default VPC configurations available in vpc-defaults.
        :param construct_vpc_props: Construct specified props that override both the default props and user props for the VPC.
        :param existing_vpc: Existing instance of a VPC, if this is set then the all Props are ignored.
        :param user_vpc_props: User provided props to override the default props for the VPC.
        '''
        if isinstance(default_vpc_props, dict):
            default_vpc_props = aws_cdk.aws_ec2.VpcProps(**default_vpc_props)
        if isinstance(construct_vpc_props, dict):
            construct_vpc_props = aws_cdk.aws_ec2.VpcProps(**construct_vpc_props)
        if isinstance(user_vpc_props, dict):
            user_vpc_props = aws_cdk.aws_ec2.VpcProps(**user_vpc_props)
        self._values: typing.Dict[str, typing.Any] = {
            "default_vpc_props": default_vpc_props,
        }
        if construct_vpc_props is not None:
            self._values["construct_vpc_props"] = construct_vpc_props
        if existing_vpc is not None:
            self._values["existing_vpc"] = existing_vpc
        if user_vpc_props is not None:
            self._values["user_vpc_props"] = user_vpc_props

    @builtins.property
    def default_vpc_props(self) -> aws_cdk.aws_ec2.VpcProps:
        '''One of the default VPC configurations available in vpc-defaults.'''
        result = self._values.get("default_vpc_props")
        assert result is not None, "Required property 'default_vpc_props' is missing"
        return typing.cast(aws_cdk.aws_ec2.VpcProps, result)

    @builtins.property
    def construct_vpc_props(self) -> typing.Optional[aws_cdk.aws_ec2.VpcProps]:
        '''Construct specified props that override both the default props and user props for the VPC.'''
        result = self._values.get("construct_vpc_props")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.VpcProps], result)

    @builtins.property
    def existing_vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''Existing instance of a VPC, if this is set then the all Props are ignored.'''
        result = self._values.get("existing_vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    @builtins.property
    def user_vpc_props(self) -> typing.Optional[aws_cdk.aws_ec2.VpcProps]:
        '''User provided props to override the default props for the VPC.'''
        result = self._values.get("user_vpc_props")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.VpcProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildVpcProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.BuildWebaclProps",
    jsii_struct_bases=[],
    name_mapping={
        "existing_webacl_obj": "existingWebaclObj",
        "webacl_props": "webaclProps",
    },
)
class BuildWebaclProps:
    def __init__(
        self,
        *,
        existing_webacl_obj: typing.Optional[aws_cdk.aws_wafv2.CfnWebACL] = None,
        webacl_props: typing.Optional[aws_cdk.aws_wafv2.CfnWebACLProps] = None,
    ) -> None:
        '''
        :param existing_webacl_obj: Existing instance of a WAF web ACL, if this is set then the all props are ignored.
        :param webacl_props: User provided props to override the default ACL props for WAF web ACL.
        '''
        if isinstance(webacl_props, dict):
            webacl_props = aws_cdk.aws_wafv2.CfnWebACLProps(**webacl_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if existing_webacl_obj is not None:
            self._values["existing_webacl_obj"] = existing_webacl_obj
        if webacl_props is not None:
            self._values["webacl_props"] = webacl_props

    @builtins.property
    def existing_webacl_obj(self) -> typing.Optional[aws_cdk.aws_wafv2.CfnWebACL]:
        '''Existing instance of a WAF web ACL, if this is set then the all props are ignored.'''
        result = self._values.get("existing_webacl_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_wafv2.CfnWebACL], result)

    @builtins.property
    def webacl_props(self) -> typing.Optional[aws_cdk.aws_wafv2.CfnWebACLProps]:
        '''User provided props to override the default ACL props for WAF web ACL.'''
        result = self._values.get("webacl_props")
        return typing.cast(typing.Optional[aws_cdk.aws_wafv2.CfnWebACLProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildWebaclProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.CfnDomainOptions",
    jsii_struct_bases=[],
    name_mapping={
        "cognito_authorized_role_arn": "cognitoAuthorizedRoleARN",
        "identitypool": "identitypool",
        "userpool": "userpool",
        "service_role_arn": "serviceRoleARN",
    },
)
class CfnDomainOptions:
    def __init__(
        self,
        *,
        cognito_authorized_role_arn: builtins.str,
        identitypool: aws_cdk.aws_cognito.CfnIdentityPool,
        userpool: aws_cdk.aws_cognito.UserPool,
        service_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cognito_authorized_role_arn: -
        :param identitypool: -
        :param userpool: -
        :param service_role_arn: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "cognito_authorized_role_arn": cognito_authorized_role_arn,
            "identitypool": identitypool,
            "userpool": userpool,
        }
        if service_role_arn is not None:
            self._values["service_role_arn"] = service_role_arn

    @builtins.property
    def cognito_authorized_role_arn(self) -> builtins.str:
        result = self._values.get("cognito_authorized_role_arn")
        assert result is not None, "Required property 'cognito_authorized_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identitypool(self) -> aws_cdk.aws_cognito.CfnIdentityPool:
        result = self._values.get("identitypool")
        assert result is not None, "Required property 'identitypool' is missing"
        return typing.cast(aws_cdk.aws_cognito.CfnIdentityPool, result)

    @builtins.property
    def userpool(self) -> aws_cdk.aws_cognito.UserPool:
        result = self._values.get("userpool")
        assert result is not None, "Required property 'userpool' is missing"
        return typing.cast(aws_cdk.aws_cognito.UserPool, result)

    @builtins.property
    def service_role_arn(self) -> typing.Optional[builtins.str]:
        result = self._values.get("service_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.CfnNagSuppressRule",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "reason": "reason"},
)
class CfnNagSuppressRule:
    def __init__(self, *, id: builtins.str, reason: builtins.str) -> None:
        '''The CFN NAG suppress rule interface.

        :param id: -
        :param reason: -

        :interface: CfnNagSuppressRule
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "reason": reason,
        }

    @builtins.property
    def id(self) -> builtins.str:
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reason(self) -> builtins.str:
        result = self._values.get("reason")
        assert result is not None, "Required property 'reason' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNagSuppressRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.CognitoOptions",
    jsii_struct_bases=[],
    name_mapping={
        "identitypool": "identitypool",
        "userpool": "userpool",
        "userpoolclient": "userpoolclient",
    },
)
class CognitoOptions:
    def __init__(
        self,
        *,
        identitypool: aws_cdk.aws_cognito.CfnIdentityPool,
        userpool: aws_cdk.aws_cognito.UserPool,
        userpoolclient: aws_cdk.aws_cognito.UserPoolClient,
    ) -> None:
        '''
        :param identitypool: -
        :param userpool: -
        :param userpoolclient: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "identitypool": identitypool,
            "userpool": userpool,
            "userpoolclient": userpoolclient,
        }

    @builtins.property
    def identitypool(self) -> aws_cdk.aws_cognito.CfnIdentityPool:
        result = self._values.get("identitypool")
        assert result is not None, "Required property 'identitypool' is missing"
        return typing.cast(aws_cdk.aws_cognito.CfnIdentityPool, result)

    @builtins.property
    def userpool(self) -> aws_cdk.aws_cognito.UserPool:
        result = self._values.get("userpool")
        assert result is not None, "Required property 'userpool' is missing"
        return typing.cast(aws_cdk.aws_cognito.UserPool, result)

    @builtins.property
    def userpoolclient(self) -> aws_cdk.aws_cognito.UserPoolClient:
        result = self._values.get("userpoolclient")
        assert result is not None, "Required property 'userpoolclient' is missing"
        return typing.cast(aws_cdk.aws_cognito.UserPoolClient, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.EventSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "deploy_sqs_dlq_queue": "deploySqsDlqQueue",
        "event_source_props": "eventSourceProps",
        "sqs_dlq_queue_props": "sqsDlqQueueProps",
    },
)
class EventSourceProps:
    def __init__(
        self,
        *,
        deploy_sqs_dlq_queue: typing.Optional[builtins.bool] = None,
        event_source_props: typing.Optional[aws_cdk.aws_lambda_event_sources.StreamEventSourceProps] = None,
        sqs_dlq_queue_props: typing.Optional[aws_cdk.aws_sqs.QueueProps] = None,
    ) -> None:
        '''
        :param deploy_sqs_dlq_queue: -
        :param event_source_props: -
        :param sqs_dlq_queue_props: -
        '''
        if isinstance(event_source_props, dict):
            event_source_props = aws_cdk.aws_lambda_event_sources.StreamEventSourceProps(**event_source_props)
        if isinstance(sqs_dlq_queue_props, dict):
            sqs_dlq_queue_props = aws_cdk.aws_sqs.QueueProps(**sqs_dlq_queue_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if deploy_sqs_dlq_queue is not None:
            self._values["deploy_sqs_dlq_queue"] = deploy_sqs_dlq_queue
        if event_source_props is not None:
            self._values["event_source_props"] = event_source_props
        if sqs_dlq_queue_props is not None:
            self._values["sqs_dlq_queue_props"] = sqs_dlq_queue_props

    @builtins.property
    def deploy_sqs_dlq_queue(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("deploy_sqs_dlq_queue")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def event_source_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda_event_sources.StreamEventSourceProps]:
        result = self._values.get("event_source_props")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda_event_sources.StreamEventSourceProps], result)

    @builtins.property
    def sqs_dlq_queue_props(self) -> typing.Optional[aws_cdk.aws_sqs.QueueProps]:
        result = self._values.get("sqs_dlq_queue_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.QueueProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.SecurityGroupRuleDefinition",
    jsii_struct_bases=[],
    name_mapping={
        "connection": "connection",
        "peer": "peer",
        "description": "description",
        "remote_rule": "remoteRule",
    },
)
class SecurityGroupRuleDefinition:
    def __init__(
        self,
        *,
        connection: aws_cdk.aws_ec2.Port,
        peer: aws_cdk.aws_ec2.IPeer,
        description: typing.Optional[builtins.str] = None,
        remote_rule: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param connection: -
        :param peer: -
        :param description: -
        :param remote_rule: -
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "connection": connection,
            "peer": peer,
        }
        if description is not None:
            self._values["description"] = description
        if remote_rule is not None:
            self._values["remote_rule"] = remote_rule

    @builtins.property
    def connection(self) -> aws_cdk.aws_ec2.Port:
        result = self._values.get("connection")
        assert result is not None, "Required property 'connection' is missing"
        return typing.cast(aws_cdk.aws_ec2.Port, result)

    @builtins.property
    def peer(self) -> aws_cdk.aws_ec2.IPeer:
        result = self._values.get("peer")
        assert result is not None, "Required property 'peer' is missing"
        return typing.cast(aws_cdk.aws_ec2.IPeer, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_rule(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("remote_rule")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupRuleDefinition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-solutions-constructs/core.ServiceEndpointTypes")
class ServiceEndpointTypes(enum.Enum):
    DYNAMODB = "DYNAMODB"
    SNS = "SNS"
    SQS = "SQS"
    S3 = "S3"
    STEP_FUNCTIONS = "STEP_FUNCTIONS"
    SAGEMAKER_RUNTIME = "SAGEMAKER_RUNTIME"
    SECRETS_MANAGER = "SECRETS_MANAGER"
    SSM = "SSM"
    EVENTS = "EVENTS"


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.SinkDataStoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "datastore_type": "datastoreType",
        "existing_s3_output_bucket": "existingS3OutputBucket",
        "output_bucket_props": "outputBucketProps",
    },
)
class SinkDataStoreProps:
    def __init__(
        self,
        *,
        datastore_type: "SinkStoreType",
        existing_s3_output_bucket: typing.Optional[aws_cdk.aws_s3.Bucket] = None,
        output_bucket_props: typing.Optional[aws_cdk.aws_s3.BucketProps] = None,
    ) -> None:
        '''Interface to define potential outputs to allow the construct define additional output destinations for ETL transformation.

        :param datastore_type: Sink data store type.
        :param existing_s3_output_bucket: The output S3 location where the data should be written. The provided S3 bucket will be used to pass the output location to the etl script as an argument to the AWS Glue job. If no location is provided, it will check if @outputBucketProps are provided. If not it will create a new bucket if the @datastoreType is S3. The argument key is ``output_path``. The value of the argument can be retrieve in the python script as follows: getResolvedOptions(sys.argv, ["JOB_NAME", "output_path", ]) output_path = args["output_path"]
        :param output_bucket_props: If @existingS3OutputBUcket is provided, this parameter is ignored. If this parameter is not provided, the construct will create a new bucket if the @datastoreType is S3.
        '''
        if isinstance(output_bucket_props, dict):
            output_bucket_props = aws_cdk.aws_s3.BucketProps(**output_bucket_props)
        self._values: typing.Dict[str, typing.Any] = {
            "datastore_type": datastore_type,
        }
        if existing_s3_output_bucket is not None:
            self._values["existing_s3_output_bucket"] = existing_s3_output_bucket
        if output_bucket_props is not None:
            self._values["output_bucket_props"] = output_bucket_props

    @builtins.property
    def datastore_type(self) -> "SinkStoreType":
        '''Sink data store type.'''
        result = self._values.get("datastore_type")
        assert result is not None, "Required property 'datastore_type' is missing"
        return typing.cast("SinkStoreType", result)

    @builtins.property
    def existing_s3_output_bucket(self) -> typing.Optional[aws_cdk.aws_s3.Bucket]:
        '''The output S3 location where the data should be written.

        The provided S3 bucket will be used to pass
        the output location to the etl script as an argument to the AWS Glue job.

        If no location is provided, it will check if @outputBucketProps are provided. If not it will create a new
        bucket if the @datastoreType is S3.

        The argument key is ``output_path``. The value of the argument can be retrieve in the python script
        as follows:
        getResolvedOptions(sys.argv, ["JOB_NAME", "output_path",  ])
        output_path = args["output_path"]
        '''
        result = self._values.get("existing_s3_output_bucket")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.Bucket], result)

    @builtins.property
    def output_bucket_props(self) -> typing.Optional[aws_cdk.aws_s3.BucketProps]:
        '''If @existingS3OutputBUcket is provided, this parameter is ignored.

        If this parameter is not provided,
        the construct will create a new bucket if the @datastoreType is S3.
        '''
        result = self._values.get("output_bucket_props")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.BucketProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SinkDataStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-solutions-constructs/core.SinkStoreType")
class SinkStoreType(enum.Enum):
    '''Enumeration of data store types that could include S3, DynamoDB, DocumentDB, RDS or Redshift.

    Current
    construct implementation only supports S3, but potential to add other output types in the future
    '''

    S3 = "S3"


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/core.VerifiedProps",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_props": "bucketProps",
        "dead_letter_queue_props": "deadLetterQueueProps",
        "deploy_dead_letter_queue": "deployDeadLetterQueue",
        "deploy_vpc": "deployVpc",
        "dynamo_table_props": "dynamoTableProps",
        "encryption_key": "encryptionKey",
        "encryption_key_props": "encryptionKeyProps",
        "endpoint_props": "endpointProps",
        "existing_bucket_interface": "existingBucketInterface",
        "existing_bucket_obj": "existingBucketObj",
        "existing_glue_job": "existingGlueJob",
        "existing_lambda_obj": "existingLambdaObj",
        "existing_media_store_container_obj": "existingMediaStoreContainerObj",
        "existing_queue_obj": "existingQueueObj",
        "existing_sagemaker_endpoint_obj": "existingSagemakerEndpointObj",
        "existing_secret_obj": "existingSecretObj",
        "existing_stream_obj": "existingStreamObj",
        "existing_table_interface": "existingTableInterface",
        "existing_table_obj": "existingTableObj",
        "existing_topic_obj": "existingTopicObj",
        "existing_vpc": "existingVpc",
        "glue_job_props": "glueJobProps",
        "kinesis_stream_props": "kinesisStreamProps",
        "lambda_function_props": "lambdaFunctionProps",
        "media_store_container_props": "mediaStoreContainerProps",
        "queue_props": "queueProps",
        "secret_props": "secretProps",
        "topic_props": "topicProps",
        "vpc_props": "vpcProps",
    },
)
class VerifiedProps:
    def __init__(
        self,
        *,
        bucket_props: typing.Optional[aws_cdk.aws_s3.BucketProps] = None,
        dead_letter_queue_props: typing.Optional[aws_cdk.aws_sqs.QueueProps] = None,
        deploy_dead_letter_queue: typing.Optional[builtins.bool] = None,
        deploy_vpc: typing.Optional[builtins.bool] = None,
        dynamo_table_props: typing.Optional[aws_cdk.aws_dynamodb.TableProps] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.Key] = None,
        encryption_key_props: typing.Optional[aws_cdk.aws_kms.KeyProps] = None,
        endpoint_props: typing.Optional[aws_cdk.aws_sagemaker.CfnEndpointProps] = None,
        existing_bucket_interface: typing.Optional[aws_cdk.aws_s3.IBucket] = None,
        existing_bucket_obj: typing.Optional[aws_cdk.aws_s3.Bucket] = None,
        existing_glue_job: typing.Optional[aws_cdk.aws_glue.CfnJob] = None,
        existing_lambda_obj: typing.Optional[aws_cdk.aws_lambda.Function] = None,
        existing_media_store_container_obj: typing.Optional[aws_cdk.aws_mediastore.CfnContainer] = None,
        existing_queue_obj: typing.Optional[aws_cdk.aws_sqs.Queue] = None,
        existing_sagemaker_endpoint_obj: typing.Optional[aws_cdk.aws_sagemaker.CfnEndpoint] = None,
        existing_secret_obj: typing.Optional[aws_cdk.aws_secretsmanager.Secret] = None,
        existing_stream_obj: typing.Optional[aws_cdk.aws_kinesis.Stream] = None,
        existing_table_interface: typing.Optional[aws_cdk.aws_dynamodb.ITable] = None,
        existing_table_obj: typing.Optional[aws_cdk.aws_dynamodb.Table] = None,
        existing_topic_obj: typing.Optional[aws_cdk.aws_sns.Topic] = None,
        existing_vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        glue_job_props: typing.Optional[aws_cdk.aws_glue.CfnJobProps] = None,
        kinesis_stream_props: typing.Optional[aws_cdk.aws_kinesis.StreamProps] = None,
        lambda_function_props: typing.Optional[aws_cdk.aws_lambda.FunctionProps] = None,
        media_store_container_props: typing.Optional[aws_cdk.aws_mediastore.CfnContainerProps] = None,
        queue_props: typing.Optional[aws_cdk.aws_sqs.QueueProps] = None,
        secret_props: typing.Optional[aws_cdk.aws_secretsmanager.SecretProps] = None,
        topic_props: typing.Optional[aws_cdk.aws_sns.TopicProps] = None,
        vpc_props: typing.Optional[aws_cdk.aws_ec2.VpcProps] = None,
    ) -> None:
        '''
        :param bucket_props: -
        :param dead_letter_queue_props: -
        :param deploy_dead_letter_queue: -
        :param deploy_vpc: -
        :param dynamo_table_props: -
        :param encryption_key: -
        :param encryption_key_props: -
        :param endpoint_props: -
        :param existing_bucket_interface: -
        :param existing_bucket_obj: -
        :param existing_glue_job: -
        :param existing_lambda_obj: -
        :param existing_media_store_container_obj: -
        :param existing_queue_obj: -
        :param existing_sagemaker_endpoint_obj: -
        :param existing_secret_obj: -
        :param existing_stream_obj: -
        :param existing_table_interface: -
        :param existing_table_obj: -
        :param existing_topic_obj: -
        :param existing_vpc: -
        :param glue_job_props: -
        :param kinesis_stream_props: -
        :param lambda_function_props: -
        :param media_store_container_props: -
        :param queue_props: -
        :param secret_props: -
        :param topic_props: -
        :param vpc_props: -
        '''
        if isinstance(bucket_props, dict):
            bucket_props = aws_cdk.aws_s3.BucketProps(**bucket_props)
        if isinstance(dead_letter_queue_props, dict):
            dead_letter_queue_props = aws_cdk.aws_sqs.QueueProps(**dead_letter_queue_props)
        if isinstance(dynamo_table_props, dict):
            dynamo_table_props = aws_cdk.aws_dynamodb.TableProps(**dynamo_table_props)
        if isinstance(encryption_key_props, dict):
            encryption_key_props = aws_cdk.aws_kms.KeyProps(**encryption_key_props)
        if isinstance(endpoint_props, dict):
            endpoint_props = aws_cdk.aws_sagemaker.CfnEndpointProps(**endpoint_props)
        if isinstance(glue_job_props, dict):
            glue_job_props = aws_cdk.aws_glue.CfnJobProps(**glue_job_props)
        if isinstance(kinesis_stream_props, dict):
            kinesis_stream_props = aws_cdk.aws_kinesis.StreamProps(**kinesis_stream_props)
        if isinstance(lambda_function_props, dict):
            lambda_function_props = aws_cdk.aws_lambda.FunctionProps(**lambda_function_props)
        if isinstance(media_store_container_props, dict):
            media_store_container_props = aws_cdk.aws_mediastore.CfnContainerProps(**media_store_container_props)
        if isinstance(queue_props, dict):
            queue_props = aws_cdk.aws_sqs.QueueProps(**queue_props)
        if isinstance(secret_props, dict):
            secret_props = aws_cdk.aws_secretsmanager.SecretProps(**secret_props)
        if isinstance(topic_props, dict):
            topic_props = aws_cdk.aws_sns.TopicProps(**topic_props)
        if isinstance(vpc_props, dict):
            vpc_props = aws_cdk.aws_ec2.VpcProps(**vpc_props)
        self._values: typing.Dict[str, typing.Any] = {}
        if bucket_props is not None:
            self._values["bucket_props"] = bucket_props
        if dead_letter_queue_props is not None:
            self._values["dead_letter_queue_props"] = dead_letter_queue_props
        if deploy_dead_letter_queue is not None:
            self._values["deploy_dead_letter_queue"] = deploy_dead_letter_queue
        if deploy_vpc is not None:
            self._values["deploy_vpc"] = deploy_vpc
        if dynamo_table_props is not None:
            self._values["dynamo_table_props"] = dynamo_table_props
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if encryption_key_props is not None:
            self._values["encryption_key_props"] = encryption_key_props
        if endpoint_props is not None:
            self._values["endpoint_props"] = endpoint_props
        if existing_bucket_interface is not None:
            self._values["existing_bucket_interface"] = existing_bucket_interface
        if existing_bucket_obj is not None:
            self._values["existing_bucket_obj"] = existing_bucket_obj
        if existing_glue_job is not None:
            self._values["existing_glue_job"] = existing_glue_job
        if existing_lambda_obj is not None:
            self._values["existing_lambda_obj"] = existing_lambda_obj
        if existing_media_store_container_obj is not None:
            self._values["existing_media_store_container_obj"] = existing_media_store_container_obj
        if existing_queue_obj is not None:
            self._values["existing_queue_obj"] = existing_queue_obj
        if existing_sagemaker_endpoint_obj is not None:
            self._values["existing_sagemaker_endpoint_obj"] = existing_sagemaker_endpoint_obj
        if existing_secret_obj is not None:
            self._values["existing_secret_obj"] = existing_secret_obj
        if existing_stream_obj is not None:
            self._values["existing_stream_obj"] = existing_stream_obj
        if existing_table_interface is not None:
            self._values["existing_table_interface"] = existing_table_interface
        if existing_table_obj is not None:
            self._values["existing_table_obj"] = existing_table_obj
        if existing_topic_obj is not None:
            self._values["existing_topic_obj"] = existing_topic_obj
        if existing_vpc is not None:
            self._values["existing_vpc"] = existing_vpc
        if glue_job_props is not None:
            self._values["glue_job_props"] = glue_job_props
        if kinesis_stream_props is not None:
            self._values["kinesis_stream_props"] = kinesis_stream_props
        if lambda_function_props is not None:
            self._values["lambda_function_props"] = lambda_function_props
        if media_store_container_props is not None:
            self._values["media_store_container_props"] = media_store_container_props
        if queue_props is not None:
            self._values["queue_props"] = queue_props
        if secret_props is not None:
            self._values["secret_props"] = secret_props
        if topic_props is not None:
            self._values["topic_props"] = topic_props
        if vpc_props is not None:
            self._values["vpc_props"] = vpc_props

    @builtins.property
    def bucket_props(self) -> typing.Optional[aws_cdk.aws_s3.BucketProps]:
        result = self._values.get("bucket_props")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.BucketProps], result)

    @builtins.property
    def dead_letter_queue_props(self) -> typing.Optional[aws_cdk.aws_sqs.QueueProps]:
        result = self._values.get("dead_letter_queue_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.QueueProps], result)

    @builtins.property
    def deploy_dead_letter_queue(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("deploy_dead_letter_queue")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def deploy_vpc(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("deploy_vpc")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def dynamo_table_props(self) -> typing.Optional[aws_cdk.aws_dynamodb.TableProps]:
        result = self._values.get("dynamo_table_props")
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.TableProps], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.Key]:
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.Key], result)

    @builtins.property
    def encryption_key_props(self) -> typing.Optional[aws_cdk.aws_kms.KeyProps]:
        result = self._values.get("encryption_key_props")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.KeyProps], result)

    @builtins.property
    def endpoint_props(self) -> typing.Optional[aws_cdk.aws_sagemaker.CfnEndpointProps]:
        result = self._values.get("endpoint_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sagemaker.CfnEndpointProps], result)

    @builtins.property
    def existing_bucket_interface(self) -> typing.Optional[aws_cdk.aws_s3.IBucket]:
        result = self._values.get("existing_bucket_interface")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.IBucket], result)

    @builtins.property
    def existing_bucket_obj(self) -> typing.Optional[aws_cdk.aws_s3.Bucket]:
        result = self._values.get("existing_bucket_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_s3.Bucket], result)

    @builtins.property
    def existing_glue_job(self) -> typing.Optional[aws_cdk.aws_glue.CfnJob]:
        result = self._values.get("existing_glue_job")
        return typing.cast(typing.Optional[aws_cdk.aws_glue.CfnJob], result)

    @builtins.property
    def existing_lambda_obj(self) -> typing.Optional[aws_cdk.aws_lambda.Function]:
        result = self._values.get("existing_lambda_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.Function], result)

    @builtins.property
    def existing_media_store_container_obj(
        self,
    ) -> typing.Optional[aws_cdk.aws_mediastore.CfnContainer]:
        result = self._values.get("existing_media_store_container_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_mediastore.CfnContainer], result)

    @builtins.property
    def existing_queue_obj(self) -> typing.Optional[aws_cdk.aws_sqs.Queue]:
        result = self._values.get("existing_queue_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.Queue], result)

    @builtins.property
    def existing_sagemaker_endpoint_obj(
        self,
    ) -> typing.Optional[aws_cdk.aws_sagemaker.CfnEndpoint]:
        result = self._values.get("existing_sagemaker_endpoint_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_sagemaker.CfnEndpoint], result)

    @builtins.property
    def existing_secret_obj(self) -> typing.Optional[aws_cdk.aws_secretsmanager.Secret]:
        result = self._values.get("existing_secret_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_secretsmanager.Secret], result)

    @builtins.property
    def existing_stream_obj(self) -> typing.Optional[aws_cdk.aws_kinesis.Stream]:
        result = self._values.get("existing_stream_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_kinesis.Stream], result)

    @builtins.property
    def existing_table_interface(self) -> typing.Optional[aws_cdk.aws_dynamodb.ITable]:
        result = self._values.get("existing_table_interface")
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.ITable], result)

    @builtins.property
    def existing_table_obj(self) -> typing.Optional[aws_cdk.aws_dynamodb.Table]:
        result = self._values.get("existing_table_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_dynamodb.Table], result)

    @builtins.property
    def existing_topic_obj(self) -> typing.Optional[aws_cdk.aws_sns.Topic]:
        result = self._values.get("existing_topic_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.Topic], result)

    @builtins.property
    def existing_vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        result = self._values.get("existing_vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    @builtins.property
    def glue_job_props(self) -> typing.Optional[aws_cdk.aws_glue.CfnJobProps]:
        result = self._values.get("glue_job_props")
        return typing.cast(typing.Optional[aws_cdk.aws_glue.CfnJobProps], result)

    @builtins.property
    def kinesis_stream_props(self) -> typing.Optional[aws_cdk.aws_kinesis.StreamProps]:
        result = self._values.get("kinesis_stream_props")
        return typing.cast(typing.Optional[aws_cdk.aws_kinesis.StreamProps], result)

    @builtins.property
    def lambda_function_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_lambda.FunctionProps]:
        result = self._values.get("lambda_function_props")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.FunctionProps], result)

    @builtins.property
    def media_store_container_props(
        self,
    ) -> typing.Optional[aws_cdk.aws_mediastore.CfnContainerProps]:
        result = self._values.get("media_store_container_props")
        return typing.cast(typing.Optional[aws_cdk.aws_mediastore.CfnContainerProps], result)

    @builtins.property
    def queue_props(self) -> typing.Optional[aws_cdk.aws_sqs.QueueProps]:
        result = self._values.get("queue_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.QueueProps], result)

    @builtins.property
    def secret_props(self) -> typing.Optional[aws_cdk.aws_secretsmanager.SecretProps]:
        result = self._values.get("secret_props")
        return typing.cast(typing.Optional[aws_cdk.aws_secretsmanager.SecretProps], result)

    @builtins.property
    def topic_props(self) -> typing.Optional[aws_cdk.aws_sns.TopicProps]:
        result = self._values.get("topic_props")
        return typing.cast(typing.Optional[aws_cdk.aws_sns.TopicProps], result)

    @builtins.property
    def vpc_props(self) -> typing.Optional[aws_cdk.aws_ec2.VpcProps]:
        result = self._values.get("vpc_props")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.VpcProps], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerifiedProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AddProxyMethodToApiResourceInputParams",
    "BuildDeadLetterQueueProps",
    "BuildDynamoDBTableProps",
    "BuildDynamoDBTableWithStreamProps",
    "BuildEventBusProps",
    "BuildGlueJobProps",
    "BuildKinesisAnalyticsAppProps",
    "BuildKinesisStreamProps",
    "BuildLambdaFunctionProps",
    "BuildQueueProps",
    "BuildS3BucketProps",
    "BuildSagemakerEndpointProps",
    "BuildSagemakerNotebookProps",
    "BuildTopicProps",
    "BuildVpcProps",
    "BuildWebaclProps",
    "CfnDomainOptions",
    "CfnNagSuppressRule",
    "CognitoOptions",
    "EventSourceProps",
    "SecurityGroupRuleDefinition",
    "ServiceEndpointTypes",
    "SinkDataStoreProps",
    "SinkStoreType",
    "VerifiedProps",
]

publication.publish()
