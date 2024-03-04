'''
# Amazon Kinesis Data Firehose Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

[Amazon Kinesis Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
is a service for fully-managed delivery of real-time streaming data to storage services
such as Amazon S3, Amazon Redshift, Amazon Elasticsearch, Splunk, or any custom HTTP
endpoint or third-party services such as Datadog, Dynatrace, LogicMonitor, MongoDB, New
Relic, and Sumo Logic.

Kinesis Data Firehose delivery streams are distinguished from Kinesis data streams in
their models of consumtpion. Whereas consumers read from a data stream by actively pulling
data from the stream, a delivery stream pushes data to its destination on a regular
cadence. This means that data streams are intended to have consumers that do on-demand
processing, like AWS Lambda or Amazon EC2. On the other hand, delivery streams are
intended to have destinations that are sources for offline processing and analytics, such
as Amazon S3 and Amazon Redshift.

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk)
project. It allows you to define Kinesis Data Firehose delivery streams.

## Defining a Delivery Stream

In order to define a Delivery Stream, you must specify a destination. An S3 bucket can be
used as a destination. More supported destinations are covered [below](#destinations).

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_kinesisfirehose_destinations as destinations
import aws_cdk.aws_s3 as s3


bucket = s3.Bucket(self, "Bucket")
DeliveryStream(self, "Delivery Stream",
    destinations=[destinations.S3Bucket(bucket)]
)
```

The above example defines the following resources:

* An S3 bucket
* A Kinesis Data Firehose delivery stream with Direct PUT as the source and CloudWatch
  error logging turned on.
* An IAM role which gives the delivery stream permission to write to the S3 bucket.

## Sources

There are two main methods of sourcing input data: Kinesis Data Streams and via a "direct
put".

See: [Sending Data to a Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-write.html)
in the *Kinesis Data Firehose Developer Guide*.

### Kinesis Data Stream

A delivery stream can read directly from a Kinesis data stream as a consumer of the data
stream. Configure this behaviour by providing a data stream in the `sourceStream`
property when constructing a delivery stream:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_kinesis as kinesis


source_stream = kinesis.Stream(self, "Source Stream")
DeliveryStream(self, "Delivery Stream",
    source_stream=source_stream,
    destinations=[destination]
)
```

### Direct Put

Data must be provided via "direct put", ie., by using a `PutRecord` or `PutRecordBatch` API call. There are a number of ways of doing
so, such as:

* Kinesis Agent: a standalone Java application that monitors and delivers files while
  handling file rotation, checkpointing, and retries. See: [Writing to Kinesis Data Firehose Using Kinesis Agent](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-agents.html)
  in the *Kinesis Data Firehose Developer Guide*.
* AWS SDK: a general purpose solution that allows you to deliver data to a delivery stream
  from anywhere using Java, .NET, Node.js, Python, or Ruby. See: [Writing to Kinesis Data Firehose Using the AWS SDK](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-sdk.html)
  in the *Kinesis Data Firehose Developer Guide*.
* CloudWatch Logs: subscribe to a log group and receive filtered log events directly into
  a delivery stream. See: [logs-destinations](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-logs-destinations-readme.html).
* Eventbridge: add an event rule target to send events to a delivery stream based on the
  rule filtering. See: [events-targets](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-events-targets-readme.html).
* SNS: add a subscription to send all notifications from the topic to a delivery
  stream. See: [sns-subscriptions](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-sns-subscriptions-readme.html).
* IoT: add an action to an IoT rule to send various IoT information to a delivery stream

## Destinations

The following destinations are supported. See [kinesisfirehose-destinations](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-kinesisfirehose-destinations-readme.html)
for the implementations of these destinations.

### S3

Defining a delivery stream with an S3 bucket destination:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_kinesisfirehose_destinations as destinations


bucket = s3.Bucket(self, "Bucket")

s3_destination = destinations.S3Bucket(bucket)

DeliveryStream(self, "Delivery Stream",
    destinations=[s3_destination]
)
```

The S3 destination also supports custom dynamic prefixes. `prefix` will be used for files
successfully delivered to S3. `errorOutputPrefix` will be added to failed records before
writing them to S3.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
s3_destination = destinations.S3Bucket(bucket,
    data_output_prefix="myFirehose/DeliveredYear=!{timestamp:yyyy}/anyMonth/rand=!{firehose:random-string}",
    error_output_prefix="myFirehoseFailures/!{firehose:error-output-type}/!{timestamp:yyyy}/anyMonth/!{timestamp:dd}"
)
```

See: [Custom S3 Prefixes](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) in the *Kinesis Data Firehose Developer Guide*.

## Server-side Encryption

Enabling server-side encryption (SSE) requires Kinesis Data Firehose to encrypt all data
sent to delivery stream when it is stored at rest. This means that data is encrypted
before being written to the service's internal storage layer and decrypted after it is
received from the internal storage layer. The service manages keys and cryptographic
operations so that sources and destinations do not need to, as the data is encrypted and
decrypted at the boundaries of the service (ie., before the data is delivered to a
destination). By default, delivery streams do not have SSE enabled.

The Key Management Service (KMS) Customer Managed Key (CMK) used for SSE can either be
AWS-owned or customer-managed. AWS-owned CMKs are keys that an AWS service (in this case
Kinesis Data Firehose) owns and manages for use in multiple AWS accounts. As a customer,
you cannot view, use, track, or manage these keys, and you are not charged for their
use. On the other hand, customer-managed CMKs are keys that are created and owned within
your account and managed entirely by you. As a customer, you are responsible for managing
access, rotation, aliases, and deletion for these keys, and you are changed for their
use. See: [Customer master keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys)
in the *KMS Developer Guide*.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_kms as kms


# SSE with an AWS-owned CMK
DeliveryStream(self, "Delivery Stream AWS Owned",
    encryption=StreamEncryption.AWS_OWNED,
    destinations=[destination]
)
# SSE with an customer-managed CMK that is created automatically by the CDK
DeliveryStream(self, "Delivery Stream Implicit Customer Managed",
    encryption=StreamEncryption.CUSTOMER_MANAGED,
    destinations=[destination]
)
# SSE with an customer-managed CMK that is explicitly specified
key = kms.Key(self, "Key")
DeliveryStream(self, "Delivery Stream Explicit Customer Managed",
    encryption_key=key,
    destinations=[destination]
)
```

See: [Data Protection](https://docs.aws.amazon.com/firehose/latest/dev/encryption.html) in
the *Kinesis Data Firehose Developer Guide*.

## Monitoring

Kinesis Data Firehose is integrated with CloudWatch, so you can monitor the performance of
your delivery streams via logs and metrics.

### Logs

Kinesis Data Firehose will send logs to CloudWatch when data transformation or data
delivery fails. The CDK will enable logging by default and create a CloudWatch LogGroup
and LogStream for your Delivery Stream.

You can provide a specific log group to specify where the CDK will create the log streams
where log events will be sent:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_kinesisfirehose_destinations as destinations
import aws_cdk.aws_logs as logs


log_group = logs.LogGroup(self, "Log Group")
destination = destinations.S3Bucket(bucket,
    log_group=log_group
)
DeliveryStream(self, "Delivery Stream",
    destinations=[destination]
)
```

Logging can also be disabled:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_kinesisfirehose_destinations as destinations


destination = destinations.S3Bucket(bucket,
    logging=False
)
DeliveryStream(self, "Delivery Stream",
    destinations=[destination]
)
```

See: [Monitoring using CloudWatch Logs](https://docs.aws.amazon.com/firehose/latest/dev/monitoring-with-cloudwatch-logs.html)
in the *Kinesis Data Firehose Developer Guide*.

### Metrics

Kinesis Data Firehose sends metrics to CloudWatch so that you can collect and analyze the
performance of the delivery stream, including data delivery, data ingestion, data
transformation, format conversion, API usage, encryption, and resource usage. You can then
use CloudWatch alarms to alert you, for example, when data freshness (the age of the
oldest record in the delivery stream) exceeds the buffering limit (indicating that data is
not being delivered to your destination), or when the rate of incoming records exceeds the
limit of records per second (indicating data is flowing into your delivery stream faster
than it is configured to process).

CDK provides methods for accessing delivery stream metrics with default configuration,
such as `metricIncomingBytes`, and `metricIncomingRecords` (see [`IDeliveryStream`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-kinesisfirehose.IDeliveryStream.html)
for a full list). CDK also provides a generic `metric` method that can be used to produce
metric configurations for any metric provided by Kinesis Data Firehose; the configurations
are pre-populated with the correct dimensions for the delivery stream.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_cloudwatch as cloudwatch


# Alarm that triggers when the per-second average of incoming bytes exceeds 90% of the current service limit
incoming_bytes_percent_of_limit = cloudwatch.MathExpression(
    expression="incomingBytes / 300 / bytePerSecLimit",
    using_metrics={
        "incoming_bytes": delivery_stream.metric_incoming_bytes(statistic=cloudwatch.Statistic.SUM),
        "byte_per_sec_limit": delivery_stream.metric("BytesPerSecondLimit")
    }
)
cloudwatch.Alarm(self, "Alarm",
    metric=incoming_bytes_percent_of_limit,
    threshold=0.9,
    evaluation_periods=3
)
```

See: [Monitoring Using CloudWatch Metrics](https://docs.aws.amazon.com/firehose/latest/dev/monitoring-with-cloudwatch-metrics.html)
in the *Kinesis Data Firehose Developer Guide*.

## Compression

Your data can automatically be compressed when it is delivered to S3 as either a final or
an intermediary/backup destination. Supported compression formats are: gzip, Snappy,
Hadoop-compatible Snappy, and ZIP, except for Redshift destinations, where Snappy
(regardless of Hadoop-compatibility) and ZIP are not supported. By default, data is
delivered to S3 without compression.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# Compress data delivered to S3 using Snappy
s3_destination = destinations.S3Bucket(bucket,
    compression=Compression.SNAPPY
)
DeliveryStream(self, "Delivery Stream",
    destinations=[destination]
)
```

## Buffering

Incoming data is buffered before it is delivered to the specified destination. The
delivery stream will wait until the amount of incoming data has exceeded some threshold
(the "buffer size") or until the time since the last data delivery occurred exceeds some
threshold (the "buffer interval"), whichever happens first. You can configure these
thresholds based on the capabilities of the destination and your use-case. By default, the
buffer size is 5 MiB and the buffer interval is 5 minutes.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk


# Increase the buffer interval and size to 10 minutes and 8 MiB, respectively
destination = destinations.S3Bucket(bucket,
    buffering_interval=cdk.Duration.minutes(10),
    buffering_size=cdk.Size.mebibytes(8)
)
DeliveryStream(self, "Delivery Stream",
    destinations=[destination]
)
```

See: [Data Delivery Frequency](https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#frequency)
in the *Kinesis Data Firehose Developer Guide*.

## Destination Encryption

Your data can be automatically encrypted when it is delivered to S3 as a final or
an intermediary/backup destination. Kinesis Data Firehose supports Amazon S3 server-side
encryption with AWS Key Management Service (AWS KMS) for encrypting delivered data
in Amazon S3. You can choose to not encrypt the data or to encrypt with a key from
the list of AWS KMS keys that you own. For more information, see [Protecting Data
Using Server-Side Encryption with AWS KMS–Managed Keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html). Data is not encrypted by default.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
import aws_cdk.aws_kms as kms


destination = destinations.S3Bucket(bucket,
    encryption_key=kms.Key(self, "MyKey")
)
DeliveryStream(self, "Delivery Stream",
    destinations=[destination]
)
```

## Backup

A delivery stream can be configured to backup data to S3 that it attempted to deliver to
the configured destination. Backed up data can be all the data that the delivery stream
attempted to deliver or just data that it failed to deliver (Redshift and S3 destinations
can only backup all data). CDK can create a new S3 bucket where it will back up data or
you can provide a bucket where data will be backed up. You can also provide a prefix under
which your backed-up data will be placed within the bucket. By default, source data is not
backed up to S3.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_kinesisfirehose_destinations as destinations
import aws_cdk.aws_s3 as s3


# Enable backup of all source records (to an S3 bucket created by CDK).
DeliveryStream(self, "Delivery Stream Backup All",
    destinations=[
        destinations.S3Bucket(bucket,
            s3_backup=DestinationS3BackupProps(
                mode=BackupMode.ALL
            )
        )
    ]
)
# Explicitly provide an S3 bucket to which all source records will be backed up.
backup_bucket = s3.Bucket(self, "Bucket")
DeliveryStream(self, "Delivery Stream Backup All Explicit Bucket",
    destinations=[
        destinations.S3Bucket(bucket,
            s3_backup=DestinationS3BackupProps(
                bucket=backup_bucket
            )
        )
    ]
)
# Explicitly provide an S3 prefix under which all source records will be backed up.
DeliveryStream(self, "Delivery Stream Backup All Explicit Prefix",
    destinations=[
        destinations.S3Bucket(bucket,
            s3_backup=DestinationS3BackupProps(
                mode=BackupMode.ALL,
                data_output_prefix="mybackup"
            )
        )
    ]
)
```

If any Data Processing or Transformation is configured on your Delivery Stream, the source
records will be backed up in their original format.

## Data Processing/Transformation

Data can be transformed before being delivered to destinations. There are two types of
data processing for delivery streams: record transformation with AWS Lambda, and record
format conversion using a schema stored in an AWS Glue table. If both types of data
processing are configured, then the Lambda transformation is performed first. By default,
no data processing occurs. This construct library currently only supports data
transformation with AWS Lambda. See [#15501](https://github.com/aws/aws-cdk/issues/15501)
to track the status of adding support for record format conversion.

### Data transformation with AWS Lambda

To transform the data, Kinesis Data Firehose will call a Lambda function that you provide
and deliver the data returned in place of the source record. The function must return a
result that contains records in a specific format, including the following fields:

* `recordId` -- the ID of the input record that corresponds the results.
* `result` -- the status of the transformation of the record: "Ok" (success), "Dropped"
  (not processed intentionally), or "ProcessingFailed" (not processed due to an error).
* `data` -- the transformed data, Base64-encoded.

The data is buffered up to 1 minute and up to 3 MiB by default before being sent to the
function, but can be configured using `bufferInterval` and `bufferSize` in the processor
configuration (see: [Buffering](#buffering)). If the function invocation fails due to a
network timeout or because of hitting an invocation limit, the invocation is retried 3
times by default, but can be configured using `retries` in the processor configuration.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk
import aws_cdk.aws_lambda as lambda_


# Provide a Lambda function that will transform records before delivery, with custom
# buffering and retry configuration
lambda_function = lambda_.Function(self, "Processor",
    runtime=lambda_.Runtime.NODEJS_12_X,
    handler="index.handler",
    code=lambda_.Code.from_asset(path.join(__dirname, "process-records"))
)
lambda_processor = LambdaFunctionProcessor(lambda_function,
    buffering_interval=cdk.Duration.minutes(5),
    buffering_size=cdk.Size.mebibytes(5),
    retries=5
)
s3_destination = destinations.S3Bucket(bucket,
    processor=lambda_processor
)
DeliveryStream(self, "Delivery Stream",
    destinations=[destination]
)
```

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import path as path
import aws_cdk.aws_kinesisfirehose as firehose
import aws_cdk.aws_kms as kms
import aws_cdk.aws_lambda_nodejs as lambdanodejs
import aws_cdk.aws_logs as logs
import aws_cdk.aws_s3 as s3
import aws_cdk.core as cdk
import ...lib as destinations

app = cdk.App()

stack = cdk.Stack(app, "aws-cdk-firehose-delivery-stream-s3-all-properties")

bucket = s3.Bucket(stack, "Bucket",
    removal_policy=cdk.RemovalPolicy.DESTROY,
    auto_delete_objects=True
)

backup_bucket = s3.Bucket(stack, "BackupBucket",
    removal_policy=cdk.RemovalPolicy.DESTROY,
    auto_delete_objects=True
)
log_group = logs.LogGroup(stack, "LogGroup",
    removal_policy=cdk.RemovalPolicy.DESTROY
)

data_processor_function = lambdanodejs.NodejsFunction(stack, "DataProcessorFunction",
    entry=path.join(__dirname, "lambda-data-processor.js"),
    timeout=cdk.Duration.minutes(1)
)

processor = firehose.LambdaFunctionProcessor(data_processor_function,
    buffer_interval=cdk.Duration.seconds(60),
    buffer_size=cdk.Size.mebibytes(1),
    retries=1
)

key = kms.Key(stack, "Key",
    removal_policy=cdk.RemovalPolicy.DESTROY
)

backup_key = kms.Key(stack, "BackupKey",
    removal_policy=cdk.RemovalPolicy.DESTROY
)

firehose.DeliveryStream(stack, "Delivery Stream",
    destinations=[destinations.S3Bucket(bucket,
        logging=True,
        log_group=log_group,
        processor=processor,
        compression=destinations.Compression.GZIP,
        data_output_prefix="regularPrefix",
        error_output_prefix="errorPrefix",
        buffering_interval=cdk.Duration.seconds(60),
        buffering_size=cdk.Size.mebibytes(1),
        encryption_key=key,
        s3_backup=DestinationS3BackupProps(
            mode=destinations.BackupMode.ALL,
            bucket=backup_bucket,
            compression=destinations.Compression.ZIP,
            data_output_prefix="backupPrefix",
            error_output_prefix="backupErrorPrefix",
            buffering_interval=cdk.Duration.seconds(60),
            buffering_size=cdk.Size.mebibytes(1),
            encryption_key=backup_key
        )
    )]
)

app.synth()
```

!cdk-integ pragma:ignore-assets

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import path as path
import aws_cdk.aws_kinesisfirehose as firehose
import aws_cdk.aws_kms as kms
import aws_cdk.aws_lambda_nodejs as lambdanodejs
import aws_cdk.aws_logs as logs
import aws_cdk.aws_s3 as s3
import aws_cdk.core as cdk
import ...lib as destinations

app = cdk.App()

stack = cdk.Stack(app, "aws-cdk-firehose-delivery-stream-s3-all-properties")

bucket = s3.Bucket(stack, "Bucket",
    removal_policy=cdk.RemovalPolicy.DESTROY,
    auto_delete_objects=True
)

backup_bucket = s3.Bucket(stack, "BackupBucket",
    removal_policy=cdk.RemovalPolicy.DESTROY,
    auto_delete_objects=True
)
log_group = logs.LogGroup(stack, "LogGroup",
    removal_policy=cdk.RemovalPolicy.DESTROY
)

data_processor_function = lambdanodejs.NodejsFunction(stack, "DataProcessorFunction",
    entry=path.join(__dirname, "lambda-data-processor.js"),
    timeout=cdk.Duration.minutes(1)
)

processor = firehose.LambdaFunctionProcessor(data_processor_function,
    buffer_interval=cdk.Duration.seconds(60),
    buffer_size=cdk.Size.mebibytes(1),
    retries=1
)

key = kms.Key(stack, "Key",
    removal_policy=cdk.RemovalPolicy.DESTROY
)

backup_key = kms.Key(stack, "BackupKey",
    removal_policy=cdk.RemovalPolicy.DESTROY
)

firehose.DeliveryStream(stack, "Delivery Stream",
    destinations=[destinations.S3Bucket(bucket,
        logging=True,
        log_group=log_group,
        processor=processor,
        compression=destinations.Compression.GZIP,
        data_output_prefix="regularPrefix",
        error_output_prefix="errorPrefix",
        buffering_interval=cdk.Duration.seconds(60),
        buffering_size=cdk.Size.mebibytes(1),
        encryption_key=key,
        s3_backup=DestinationS3BackupProps(
            mode=destinations.BackupMode.ALL,
            bucket=backup_bucket,
            compression=destinations.Compression.ZIP,
            data_output_prefix="backupPrefix",
            error_output_prefix="backupErrorPrefix",
            buffering_interval=cdk.Duration.seconds(60),
            buffering_size=cdk.Size.mebibytes(1),
            encryption_key=backup_key
        )
    )]
)

app.synth()
```

See: [Data Transformation](https://docs.aws.amazon.com/firehose/latest/dev/data-transformation.html)
in the *Kinesis Data Firehose Developer Guide*.

## Specifying an IAM role

The DeliveryStream class automatically creates IAM service roles with all the minimum
necessary permissions for Kinesis Data Firehose to access the resources referenced by your
delivery stream. One service role is created for the delivery stream that allows Kinesis
Data Firehose to read from a Kinesis data stream (if one is configured as the delivery
stream source) and for server-side encryption. Another service role is created for each
destination, which gives Kinesis Data Firehose write access to the destination resource,
as well as the ability to invoke data transformers and read schemas for record format
conversion. If you wish, you may specify your own IAM role for either the delivery stream
or the destination service role, or both. It must have the correct trust policy (it must
allow Kinesis Data Firehose to assume it) or delivery stream creation or data delivery
will fail. Other required permissions to destination resources, encryption keys, etc.,
will be provided automatically.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_kinesisfirehose_destinations as destinations
import aws_cdk.aws_iam as iam


# Create service roles for the delivery stream and destination.
# These can be used for other purposes and granted access to different resources.
# They must include the Kinesis Data Firehose service principal in their trust policies.
# Two separate roles are shown below, but the same role can be used for both purposes.
delivery_stream_role = iam.Role(self, "Delivery Stream Role",
    assumed_by=iam.ServicePrincipal("firehose.amazonaws.com")
)
destination_role = iam.Role(self, "Destination Role",
    assumed_by=iam.ServicePrincipal("firehose.amazonaws.com")
)

# Specify the roles created above when defining the destination and delivery stream.
destination = destinations.S3Bucket(bucket, role=destination_role)
DeliveryStream(self, "Delivery Stream",
    destinations=[destination],
    role=delivery_stream_role
)
```

See [Controlling Access](https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html)
in the *Kinesis Data Firehose Developer Guide*.

## Granting application access to a delivery stream

IAM roles, users or groups which need to be able to work with delivery streams should be
granted IAM permissions.

Any object that implements the `IGrantable` interface (ie., has an associated principal)
can be granted permissions to a delivery stream by calling:

* `grantPutRecords(principal)` - grants the principal the ability to put records onto the
  delivery stream
* `grant(principal, ...actions)` - grants the principal permission to a custom set of
  actions

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iam as iam


lambda_role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
)

# Give the role permissions to write data to the delivery stream
delivery_stream.grant_put_records(lambda_role)
```

The following write permissions are provided to a service principal by the `grantPutRecords()` method:

* `firehose:PutRecord`
* `firehose:PutRecordBatch`

## Granting a delivery stream access to a resource

Conversely to the above, Kinesis Data Firehose requires permissions in order for delivery
streams to interact with resources that you own. For example, if an S3 bucket is specified
as a destination of a delivery stream, the delivery stream must be granted permissions to
put and get objects from the bucket. When using the built-in AWS service destinations
found in the `@aws-cdk/aws-kinesisfirehose-destinations` module, the CDK grants the
permissions automatically. However, custom or third-party destinations may require custom
permissions. In this case, use the delivery stream as an `IGrantable`, as follows:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_lambda as lambda_


fn = lambda_.Function(self, "Function",
    code=lambda_.Code.from_inline("exports.handler = (event) => {}"),
    runtime=lambda_.Runtime.NODEJS_14_X,
    handler="index.handler"
)

fn.grant_invoke(delivery_stream)
```

## Multiple destinations

Though the delivery stream allows specifying an array of destinations, only one
destination per delivery stream is currently allowed. This limitation is enforced at CDK
synthesis time and will throw an error.
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

import aws_cdk.aws_cloudwatch
import aws_cdk.aws_ec2
import aws_cdk.aws_iam
import aws_cdk.aws_kinesis
import aws_cdk.aws_kms
import aws_cdk.aws_lambda
import aws_cdk.core
import constructs


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDeliveryStream(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream",
):
    '''A CloudFormation ``AWS::KinesisFirehose::DeliveryStream``.

    :cloudformationResource: AWS::KinesisFirehose::DeliveryStream
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        amazonopensearchservice_destination_configuration: typing.Optional[typing.Union["CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty", aws_cdk.core.IResolvable]] = None,
        delivery_stream_encryption_configuration_input: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty"]] = None,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        delivery_stream_type: typing.Optional[builtins.str] = None,
        elasticsearch_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty"]] = None,
        extended_s3_destination_configuration: typing.Optional[typing.Union["CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty", aws_cdk.core.IResolvable]] = None,
        http_endpoint_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty"]] = None,
        kinesis_stream_source_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.KinesisStreamSourceConfigurationProperty"]] = None,
        redshift_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RedshiftDestinationConfigurationProperty"]] = None,
        s3_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]] = None,
        splunk_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SplunkDestinationConfigurationProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::KinesisFirehose::DeliveryStream``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param amazonopensearchservice_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceDestinationConfiguration``.
        :param delivery_stream_encryption_configuration_input: ``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamEncryptionConfigurationInput``.
        :param delivery_stream_name: ``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamName``.
        :param delivery_stream_type: ``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamType``.
        :param elasticsearch_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.ElasticsearchDestinationConfiguration``.
        :param extended_s3_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.ExtendedS3DestinationConfiguration``.
        :param http_endpoint_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.HttpEndpointDestinationConfiguration``.
        :param kinesis_stream_source_configuration: ``AWS::KinesisFirehose::DeliveryStream.KinesisStreamSourceConfiguration``.
        :param redshift_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.RedshiftDestinationConfiguration``.
        :param s3_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.S3DestinationConfiguration``.
        :param splunk_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.SplunkDestinationConfiguration``.
        :param tags: ``AWS::KinesisFirehose::DeliveryStream.Tags``.
        '''
        props = CfnDeliveryStreamProps(
            amazonopensearchservice_destination_configuration=amazonopensearchservice_destination_configuration,
            delivery_stream_encryption_configuration_input=delivery_stream_encryption_configuration_input,
            delivery_stream_name=delivery_stream_name,
            delivery_stream_type=delivery_stream_type,
            elasticsearch_destination_configuration=elasticsearch_destination_configuration,
            extended_s3_destination_configuration=extended_s3_destination_configuration,
            http_endpoint_destination_configuration=http_endpoint_destination_configuration,
            kinesis_stream_source_configuration=kinesis_stream_source_configuration,
            redshift_destination_configuration=redshift_destination_configuration,
            s3_destination_configuration=s3_destination_configuration,
            splunk_destination_configuration=splunk_destination_configuration,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::KinesisFirehose::DeliveryStream.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="amazonopensearchserviceDestinationConfiguration")
    def amazonopensearchservice_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceDestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty", aws_cdk.core.IResolvable]], jsii.get(self, "amazonopensearchserviceDestinationConfiguration"))

    @amazonopensearchservice_destination_configuration.setter
    def amazonopensearchservice_destination_configuration(
        self,
        value: typing.Optional[typing.Union["CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "amazonopensearchserviceDestinationConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deliveryStreamEncryptionConfigurationInput")
    def delivery_stream_encryption_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty"]]:
        '''``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamEncryptionConfigurationInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty"]], jsii.get(self, "deliveryStreamEncryptionConfigurationInput"))

    @delivery_stream_encryption_configuration_input.setter
    def delivery_stream_encryption_configuration_input(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty"]],
    ) -> None:
        jsii.set(self, "deliveryStreamEncryptionConfigurationInput", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamName"))

    @delivery_stream_name.setter
    def delivery_stream_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "deliveryStreamName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deliveryStreamType")
    def delivery_stream_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamtype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamType"))

    @delivery_stream_type.setter
    def delivery_stream_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "deliveryStreamType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="elasticsearchDestinationConfiguration")
    def elasticsearch_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty"]]:
        '''``AWS::KinesisFirehose::DeliveryStream.ElasticsearchDestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty"]], jsii.get(self, "elasticsearchDestinationConfiguration"))

    @elasticsearch_destination_configuration.setter
    def elasticsearch_destination_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "elasticsearchDestinationConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="extendedS3DestinationConfiguration")
    def extended_s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::KinesisFirehose::DeliveryStream.ExtendedS3DestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty", aws_cdk.core.IResolvable]], jsii.get(self, "extendedS3DestinationConfiguration"))

    @extended_s3_destination_configuration.setter
    def extended_s3_destination_configuration(
        self,
        value: typing.Optional[typing.Union["CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "extendedS3DestinationConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="httpEndpointDestinationConfiguration")
    def http_endpoint_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty"]]:
        '''``AWS::KinesisFirehose::DeliveryStream.HttpEndpointDestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty"]], jsii.get(self, "httpEndpointDestinationConfiguration"))

    @http_endpoint_destination_configuration.setter
    def http_endpoint_destination_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "httpEndpointDestinationConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="kinesisStreamSourceConfiguration")
    def kinesis_stream_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.KinesisStreamSourceConfigurationProperty"]]:
        '''``AWS::KinesisFirehose::DeliveryStream.KinesisStreamSourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.KinesisStreamSourceConfigurationProperty"]], jsii.get(self, "kinesisStreamSourceConfiguration"))

    @kinesis_stream_source_configuration.setter
    def kinesis_stream_source_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.KinesisStreamSourceConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "kinesisStreamSourceConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="redshiftDestinationConfiguration")
    def redshift_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RedshiftDestinationConfigurationProperty"]]:
        '''``AWS::KinesisFirehose::DeliveryStream.RedshiftDestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RedshiftDestinationConfigurationProperty"]], jsii.get(self, "redshiftDestinationConfiguration"))

    @redshift_destination_configuration.setter
    def redshift_destination_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RedshiftDestinationConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "redshiftDestinationConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="s3DestinationConfiguration")
    def s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]]:
        '''``AWS::KinesisFirehose::DeliveryStream.S3DestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]], jsii.get(self, "s3DestinationConfiguration"))

    @s3_destination_configuration.setter
    def s3_destination_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "s3DestinationConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="splunkDestinationConfiguration")
    def splunk_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SplunkDestinationConfigurationProperty"]]:
        '''``AWS::KinesisFirehose::DeliveryStream.SplunkDestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SplunkDestinationConfigurationProperty"]], jsii.get(self, "splunkDestinationConfiguration"))

    @splunk_destination_configuration.setter
    def splunk_destination_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SplunkDestinationConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "splunkDestinationConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class AmazonopensearchserviceBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param interval_in_seconds: ``CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty.IntervalInSeconds``.
            :param size_in_m_bs: ``CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty.SizeInMBs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty.IntervalInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty.SizeInMBs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonopensearchserviceBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "cluster_endpoint": "clusterEndpoint",
            "domain_arn": "domainArn",
            "index_rotation_period": "indexRotationPeriod",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "type_name": "typeName",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class AmazonopensearchserviceDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"],
            buffering_hints: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty"]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]] = None,
            cluster_endpoint: typing.Optional[builtins.str] = None,
            domain_arn: typing.Optional[builtins.str] = None,
            index_rotation_period: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]] = None,
            retry_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty"]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            type_name: typing.Optional[builtins.str] = None,
            vpc_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.VpcConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param index_name: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.IndexName``.
            :param role_arn: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.RoleARN``.
            :param s3_configuration: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.S3Configuration``.
            :param buffering_hints: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.BufferingHints``.
            :param cloud_watch_logging_options: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.CloudWatchLoggingOptions``.
            :param cluster_endpoint: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.ClusterEndpoint``.
            :param domain_arn: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.DomainARN``.
            :param index_rotation_period: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.IndexRotationPeriod``.
            :param processing_configuration: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.ProcessingConfiguration``.
            :param retry_options: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.RetryOptions``.
            :param s3_backup_mode: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.S3BackupMode``.
            :param type_name: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.TypeName``.
            :param vpc_configuration: ``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "index_name": index_name,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if cluster_endpoint is not None:
                self._values["cluster_endpoint"] = cluster_endpoint
            if domain_arn is not None:
                self._values["domain_arn"] = domain_arn
            if index_rotation_period is not None:
                self._values["index_rotation_period"] = index_rotation_period
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if type_name is not None:
                self._values["type_name"] = type_name
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def index_name(self) -> builtins.str:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.IndexName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.RoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.S3Configuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty"]]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.BufferingHints``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.CloudWatchLoggingOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def cluster_endpoint(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.ClusterEndpoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-clusterendpoint
            '''
            result = self._values.get("cluster_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def domain_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.DomainARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-domainarn
            '''
            result = self._values.get("domain_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_rotation_period(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.IndexRotationPeriod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexrotationperiod
            '''
            result = self._values.get("index_rotation_period")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.ProcessingConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty"]]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.RetryOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.S3BackupMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.TypeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-typename
            '''
            result = self._values.get("type_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.VpcConfigurationProperty"]]:
            '''``CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.VpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonopensearchserviceDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class AmazonopensearchserviceRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param duration_in_seconds: ``CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty.DurationInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty.DurationInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonopensearchserviceRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class BufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param interval_in_seconds: ``CfnDeliveryStream.BufferingHintsProperty.IntervalInSeconds``.
            :param size_in_m_bs: ``CfnDeliveryStream.BufferingHintsProperty.SizeInMBs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.BufferingHintsProperty.IntervalInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.BufferingHintsProperty.SizeInMBs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "log_group_name": "logGroupName",
            "log_stream_name": "logStreamName",
        },
    )
    class CloudWatchLoggingOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            log_group_name: typing.Optional[builtins.str] = None,
            log_stream_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param enabled: ``CfnDeliveryStream.CloudWatchLoggingOptionsProperty.Enabled``.
            :param log_group_name: ``CfnDeliveryStream.CloudWatchLoggingOptionsProperty.LogGroupName``.
            :param log_stream_name: ``CfnDeliveryStream.CloudWatchLoggingOptionsProperty.LogStreamName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_stream_name is not None:
                self._values["log_stream_name"] = log_stream_name

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeliveryStream.CloudWatchLoggingOptionsProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.CloudWatchLoggingOptionsProperty.LogGroupName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_stream_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.CloudWatchLoggingOptionsProperty.LogStreamName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-logstreamname
            '''
            result = self._values.get("log_stream_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLoggingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.CopyCommandProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_table_name": "dataTableName",
            "copy_options": "copyOptions",
            "data_table_columns": "dataTableColumns",
        },
    )
    class CopyCommandProperty:
        def __init__(
            self,
            *,
            data_table_name: builtins.str,
            copy_options: typing.Optional[builtins.str] = None,
            data_table_columns: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param data_table_name: ``CfnDeliveryStream.CopyCommandProperty.DataTableName``.
            :param copy_options: ``CfnDeliveryStream.CopyCommandProperty.CopyOptions``.
            :param data_table_columns: ``CfnDeliveryStream.CopyCommandProperty.DataTableColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_table_name": data_table_name,
            }
            if copy_options is not None:
                self._values["copy_options"] = copy_options
            if data_table_columns is not None:
                self._values["data_table_columns"] = data_table_columns

        @builtins.property
        def data_table_name(self) -> builtins.str:
            '''``CfnDeliveryStream.CopyCommandProperty.DataTableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablename
            '''
            result = self._values.get("data_table_name")
            assert result is not None, "Required property 'data_table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def copy_options(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.CopyCommandProperty.CopyOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-copyoptions
            '''
            result = self._values.get("copy_options")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_table_columns(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.CopyCommandProperty.DataTableColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablecolumns
            '''
            result = self._values.get("data_table_columns")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CopyCommandProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.DataFormatConversionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "input_format_configuration": "inputFormatConfiguration",
            "output_format_configuration": "outputFormatConfiguration",
            "schema_configuration": "schemaConfiguration",
        },
    )
    class DataFormatConversionConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            input_format_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.InputFormatConfigurationProperty"]] = None,
            output_format_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.OutputFormatConfigurationProperty"]] = None,
            schema_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SchemaConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param enabled: ``CfnDeliveryStream.DataFormatConversionConfigurationProperty.Enabled``.
            :param input_format_configuration: ``CfnDeliveryStream.DataFormatConversionConfigurationProperty.InputFormatConfiguration``.
            :param output_format_configuration: ``CfnDeliveryStream.DataFormatConversionConfigurationProperty.OutputFormatConfiguration``.
            :param schema_configuration: ``CfnDeliveryStream.DataFormatConversionConfigurationProperty.SchemaConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if input_format_configuration is not None:
                self._values["input_format_configuration"] = input_format_configuration
            if output_format_configuration is not None:
                self._values["output_format_configuration"] = output_format_configuration
            if schema_configuration is not None:
                self._values["schema_configuration"] = schema_configuration

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeliveryStream.DataFormatConversionConfigurationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def input_format_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.InputFormatConfigurationProperty"]]:
            '''``CfnDeliveryStream.DataFormatConversionConfigurationProperty.InputFormatConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-inputformatconfiguration
            '''
            result = self._values.get("input_format_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.InputFormatConfigurationProperty"]], result)

        @builtins.property
        def output_format_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.OutputFormatConfigurationProperty"]]:
            '''``CfnDeliveryStream.DataFormatConversionConfigurationProperty.OutputFormatConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-outputformatconfiguration
            '''
            result = self._values.get("output_format_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.OutputFormatConfigurationProperty"]], result)

        @builtins.property
        def schema_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SchemaConfigurationProperty"]]:
            '''``CfnDeliveryStream.DataFormatConversionConfigurationProperty.SchemaConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-schemaconfiguration
            '''
            result = self._values.get("schema_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SchemaConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataFormatConversionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"key_type": "keyType", "key_arn": "keyArn"},
    )
    class DeliveryStreamEncryptionConfigurationInputProperty:
        def __init__(
            self,
            *,
            key_type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key_type: ``CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty.KeyType``.
            :param key_arn: ``CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty.KeyARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key_type": key_type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def key_type(self) -> builtins.str:
            '''``CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty.KeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keytype
            '''
            result = self._values.get("key_type")
            assert result is not None, "Required property 'key_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty.KeyARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeliveryStreamEncryptionConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.DeserializerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hive_json_ser_de": "hiveJsonSerDe",
            "open_x_json_ser_de": "openXJsonSerDe",
        },
    )
    class DeserializerProperty:
        def __init__(
            self,
            *,
            hive_json_ser_de: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HiveJsonSerDeProperty"]] = None,
            open_x_json_ser_de: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.OpenXJsonSerDeProperty"]] = None,
        ) -> None:
            '''
            :param hive_json_ser_de: ``CfnDeliveryStream.DeserializerProperty.HiveJsonSerDe``.
            :param open_x_json_ser_de: ``CfnDeliveryStream.DeserializerProperty.OpenXJsonSerDe``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if hive_json_ser_de is not None:
                self._values["hive_json_ser_de"] = hive_json_ser_de
            if open_x_json_ser_de is not None:
                self._values["open_x_json_ser_de"] = open_x_json_ser_de

        @builtins.property
        def hive_json_ser_de(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HiveJsonSerDeProperty"]]:
            '''``CfnDeliveryStream.DeserializerProperty.HiveJsonSerDe``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-hivejsonserde
            '''
            result = self._values.get("hive_json_ser_de")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HiveJsonSerDeProperty"]], result)

        @builtins.property
        def open_x_json_ser_de(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.OpenXJsonSerDeProperty"]]:
            '''``CfnDeliveryStream.DeserializerProperty.OpenXJsonSerDe``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-openxjsonserde
            '''
            result = self._values.get("open_x_json_ser_de")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.OpenXJsonSerDeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeserializerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "retry_options": "retryOptions"},
    )
    class DynamicPartitioningConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            retry_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RetryOptionsProperty"]] = None,
        ) -> None:
            '''
            :param enabled: ``CfnDeliveryStream.DynamicPartitioningConfigurationProperty.Enabled``.
            :param retry_options: ``CfnDeliveryStream.DynamicPartitioningConfigurationProperty.RetryOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if retry_options is not None:
                self._values["retry_options"] = retry_options

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeliveryStream.DynamicPartitioningConfigurationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RetryOptionsProperty"]]:
            '''``CfnDeliveryStream.DynamicPartitioningConfigurationProperty.RetryOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RetryOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamicPartitioningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.ElasticsearchBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class ElasticsearchBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param interval_in_seconds: ``CfnDeliveryStream.ElasticsearchBufferingHintsProperty.IntervalInSeconds``.
            :param size_in_m_bs: ``CfnDeliveryStream.ElasticsearchBufferingHintsProperty.SizeInMBs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.ElasticsearchBufferingHintsProperty.IntervalInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.ElasticsearchBufferingHintsProperty.SizeInMBs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "cluster_endpoint": "clusterEndpoint",
            "domain_arn": "domainArn",
            "index_rotation_period": "indexRotationPeriod",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "type_name": "typeName",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class ElasticsearchDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"],
            buffering_hints: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ElasticsearchBufferingHintsProperty"]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]] = None,
            cluster_endpoint: typing.Optional[builtins.str] = None,
            domain_arn: typing.Optional[builtins.str] = None,
            index_rotation_period: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]] = None,
            retry_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ElasticsearchRetryOptionsProperty"]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            type_name: typing.Optional[builtins.str] = None,
            vpc_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.VpcConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param index_name: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.IndexName``.
            :param role_arn: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.RoleARN``.
            :param s3_configuration: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.S3Configuration``.
            :param buffering_hints: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.BufferingHints``.
            :param cloud_watch_logging_options: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.CloudWatchLoggingOptions``.
            :param cluster_endpoint: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.ClusterEndpoint``.
            :param domain_arn: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.DomainARN``.
            :param index_rotation_period: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.IndexRotationPeriod``.
            :param processing_configuration: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.ProcessingConfiguration``.
            :param retry_options: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.RetryOptions``.
            :param s3_backup_mode: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.S3BackupMode``.
            :param type_name: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.TypeName``.
            :param vpc_configuration: ``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "index_name": index_name,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if cluster_endpoint is not None:
                self._values["cluster_endpoint"] = cluster_endpoint
            if domain_arn is not None:
                self._values["domain_arn"] = domain_arn
            if index_rotation_period is not None:
                self._values["index_rotation_period"] = index_rotation_period
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if type_name is not None:
                self._values["type_name"] = type_name
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def index_name(self) -> builtins.str:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.IndexName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.RoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.S3Configuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ElasticsearchBufferingHintsProperty"]]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.BufferingHints``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ElasticsearchBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.CloudWatchLoggingOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def cluster_endpoint(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.ClusterEndpoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-clusterendpoint
            '''
            result = self._values.get("cluster_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def domain_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.DomainARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-domainarn
            '''
            result = self._values.get("domain_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_rotation_period(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.IndexRotationPeriod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexrotationperiod
            '''
            result = self._values.get("index_rotation_period")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.ProcessingConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ElasticsearchRetryOptionsProperty"]]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.RetryOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ElasticsearchRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.S3BackupMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.TypeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-typename
            '''
            result = self._values.get("type_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.VpcConfigurationProperty"]]:
            '''``CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty.VpcConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.VpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.ElasticsearchRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class ElasticsearchRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param duration_in_seconds: ``CfnDeliveryStream.ElasticsearchRetryOptionsProperty.DurationInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.ElasticsearchRetryOptionsProperty.DurationInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html#cfn-kinesisfirehose-deliverystream-elasticsearchretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_encryption_config": "kmsEncryptionConfig",
            "no_encryption_config": "noEncryptionConfig",
        },
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            kms_encryption_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.KMSEncryptionConfigProperty"]] = None,
            no_encryption_config: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param kms_encryption_config: ``CfnDeliveryStream.EncryptionConfigurationProperty.KMSEncryptionConfig``.
            :param no_encryption_config: ``CfnDeliveryStream.EncryptionConfigurationProperty.NoEncryptionConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if kms_encryption_config is not None:
                self._values["kms_encryption_config"] = kms_encryption_config
            if no_encryption_config is not None:
                self._values["no_encryption_config"] = no_encryption_config

        @builtins.property
        def kms_encryption_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.KMSEncryptionConfigProperty"]]:
            '''``CfnDeliveryStream.EncryptionConfigurationProperty.KMSEncryptionConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-kmsencryptionconfig
            '''
            result = self._values.get("kms_encryption_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.KMSEncryptionConfigProperty"]], result)

        @builtins.property
        def no_encryption_config(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.EncryptionConfigurationProperty.NoEncryptionConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-noencryptionconfig
            '''
            result = self._values.get("no_encryption_config")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "role_arn": "roleArn",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "compression_format": "compressionFormat",
            "data_format_conversion_configuration": "dataFormatConversionConfiguration",
            "dynamic_partitioning_configuration": "dynamicPartitioningConfiguration",
            "encryption_configuration": "encryptionConfiguration",
            "error_output_prefix": "errorOutputPrefix",
            "prefix": "prefix",
            "processing_configuration": "processingConfiguration",
            "s3_backup_configuration": "s3BackupConfiguration",
            "s3_backup_mode": "s3BackupMode",
        },
    )
    class ExtendedS3DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            role_arn: builtins.str,
            buffering_hints: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.BufferingHintsProperty"]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]] = None,
            compression_format: typing.Optional[builtins.str] = None,
            data_format_conversion_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DataFormatConversionConfigurationProperty"]] = None,
            dynamic_partitioning_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DynamicPartitioningConfigurationProperty"]] = None,
            encryption_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.EncryptionConfigurationProperty"]] = None,
            error_output_prefix: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]] = None,
            s3_backup_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket_arn: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.BucketARN``.
            :param role_arn: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.RoleARN``.
            :param buffering_hints: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.BufferingHints``.
            :param cloud_watch_logging_options: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.CloudWatchLoggingOptions``.
            :param compression_format: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.CompressionFormat``.
            :param data_format_conversion_configuration: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.DataFormatConversionConfiguration``.
            :param dynamic_partitioning_configuration: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.DynamicPartitioningConfiguration``.
            :param encryption_configuration: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.EncryptionConfiguration``.
            :param error_output_prefix: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.ErrorOutputPrefix``.
            :param prefix: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.Prefix``.
            :param processing_configuration: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.ProcessingConfiguration``.
            :param s3_backup_configuration: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.S3BackupConfiguration``.
            :param s3_backup_mode: ``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.S3BackupMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "role_arn": role_arn,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if compression_format is not None:
                self._values["compression_format"] = compression_format
            if data_format_conversion_configuration is not None:
                self._values["data_format_conversion_configuration"] = data_format_conversion_configuration
            if dynamic_partitioning_configuration is not None:
                self._values["dynamic_partitioning_configuration"] = dynamic_partitioning_configuration
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if error_output_prefix is not None:
                self._values["error_output_prefix"] = error_output_prefix
            if prefix is not None:
                self._values["prefix"] = prefix
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if s3_backup_configuration is not None:
                self._values["s3_backup_configuration"] = s3_backup_configuration
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.BucketARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.RoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.BufferingHintsProperty"]]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.BufferingHints``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.BufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.CloudWatchLoggingOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def compression_format(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.CompressionFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-compressionformat
            '''
            result = self._values.get("compression_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_format_conversion_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DataFormatConversionConfigurationProperty"]]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.DataFormatConversionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dataformatconversionconfiguration
            '''
            result = self._values.get("data_format_conversion_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DataFormatConversionConfigurationProperty"]], result)

        @builtins.property
        def dynamic_partitioning_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DynamicPartitioningConfigurationProperty"]]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.DynamicPartitioningConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dynamicpartitioningconfiguration
            '''
            result = self._values.get("dynamic_partitioning_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DynamicPartitioningConfigurationProperty"]], result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.EncryptionConfigurationProperty"]]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.EncryptionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.EncryptionConfigurationProperty"]], result)

        @builtins.property
        def error_output_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.ErrorOutputPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-erroroutputprefix
            '''
            result = self._values.get("error_output_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.ProcessingConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def s3_backup_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.S3BackupConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupconfiguration
            '''
            result = self._values.get("s3_backup_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty.S3BackupMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtendedS3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={"timestamp_formats": "timestampFormats"},
    )
    class HiveJsonSerDeProperty:
        def __init__(
            self,
            *,
            timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param timestamp_formats: ``CfnDeliveryStream.HiveJsonSerDeProperty.TimestampFormats``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if timestamp_formats is not None:
                self._values["timestamp_formats"] = timestamp_formats

        @builtins.property
        def timestamp_formats(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDeliveryStream.HiveJsonSerDeProperty.TimestampFormats``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html#cfn-kinesisfirehose-deliverystream-hivejsonserde-timestampformats
            '''
            result = self._values.get("timestamp_formats")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HiveJsonSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.HttpEndpointCommonAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_name": "attributeName",
            "attribute_value": "attributeValue",
        },
    )
    class HttpEndpointCommonAttributeProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            attribute_value: builtins.str,
        ) -> None:
            '''
            :param attribute_name: ``CfnDeliveryStream.HttpEndpointCommonAttributeProperty.AttributeName``.
            :param attribute_value: ``CfnDeliveryStream.HttpEndpointCommonAttributeProperty.AttributeValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "attribute_name": attribute_name,
                "attribute_value": attribute_value,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''``CfnDeliveryStream.HttpEndpointCommonAttributeProperty.AttributeName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attribute_value(self) -> builtins.str:
            '''``CfnDeliveryStream.HttpEndpointCommonAttributeProperty.AttributeValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributevalue
            '''
            result = self._values.get("attribute_value")
            assert result is not None, "Required property 'attribute_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointCommonAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.HttpEndpointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"url": "url", "access_key": "accessKey", "name": "name"},
    )
    class HttpEndpointConfigurationProperty:
        def __init__(
            self,
            *,
            url: builtins.str,
            access_key: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param url: ``CfnDeliveryStream.HttpEndpointConfigurationProperty.Url``.
            :param access_key: ``CfnDeliveryStream.HttpEndpointConfigurationProperty.AccessKey``.
            :param name: ``CfnDeliveryStream.HttpEndpointConfigurationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "url": url,
            }
            if access_key is not None:
                self._values["access_key"] = access_key
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def url(self) -> builtins.str:
            '''``CfnDeliveryStream.HttpEndpointConfigurationProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def access_key(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.HttpEndpointConfigurationProperty.AccessKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-accesskey
            '''
            result = self._values.get("access_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.HttpEndpointConfigurationProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_configuration": "endpointConfiguration",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "processing_configuration": "processingConfiguration",
            "request_configuration": "requestConfiguration",
            "retry_options": "retryOptions",
            "role_arn": "roleArn",
            "s3_backup_mode": "s3BackupMode",
        },
    )
    class HttpEndpointDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointConfigurationProperty"],
            s3_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"],
            buffering_hints: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.BufferingHintsProperty"]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]] = None,
            processing_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]] = None,
            request_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointRequestConfigurationProperty"]] = None,
            retry_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RetryOptionsProperty"]] = None,
            role_arn: typing.Optional[builtins.str] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param endpoint_configuration: ``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.EndpointConfiguration``.
            :param s3_configuration: ``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.S3Configuration``.
            :param buffering_hints: ``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.BufferingHints``.
            :param cloud_watch_logging_options: ``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.CloudWatchLoggingOptions``.
            :param processing_configuration: ``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.ProcessingConfiguration``.
            :param request_configuration: ``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.RequestConfiguration``.
            :param retry_options: ``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.RetryOptions``.
            :param role_arn: ``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.RoleARN``.
            :param s3_backup_mode: ``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.S3BackupMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "endpoint_configuration": endpoint_configuration,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if request_configuration is not None:
                self._values["request_configuration"] = request_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode

        @builtins.property
        def endpoint_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointConfigurationProperty"]:
            '''``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.EndpointConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-endpointconfiguration
            '''
            result = self._values.get("endpoint_configuration")
            assert result is not None, "Required property 'endpoint_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointConfigurationProperty"], result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.S3Configuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.BufferingHintsProperty"]]:
            '''``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.BufferingHints``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.BufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.CloudWatchLoggingOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.ProcessingConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def request_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointRequestConfigurationProperty"]]:
            '''``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.RequestConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-requestconfiguration
            '''
            result = self._values.get("request_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointRequestConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RetryOptionsProperty"]]:
            '''``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.RetryOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RetryOptionsProperty"]], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.RoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty.S3BackupMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.HttpEndpointRequestConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "common_attributes": "commonAttributes",
            "content_encoding": "contentEncoding",
        },
    )
    class HttpEndpointRequestConfigurationProperty:
        def __init__(
            self,
            *,
            common_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointCommonAttributeProperty"]]]] = None,
            content_encoding: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param common_attributes: ``CfnDeliveryStream.HttpEndpointRequestConfigurationProperty.CommonAttributes``.
            :param content_encoding: ``CfnDeliveryStream.HttpEndpointRequestConfigurationProperty.ContentEncoding``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if common_attributes is not None:
                self._values["common_attributes"] = common_attributes
            if content_encoding is not None:
                self._values["content_encoding"] = content_encoding

        @builtins.property
        def common_attributes(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointCommonAttributeProperty"]]]]:
            '''``CfnDeliveryStream.HttpEndpointRequestConfigurationProperty.CommonAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-commonattributes
            '''
            result = self._values.get("common_attributes")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.HttpEndpointCommonAttributeProperty"]]]], result)

        @builtins.property
        def content_encoding(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.HttpEndpointRequestConfigurationProperty.ContentEncoding``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-contentencoding
            '''
            result = self._values.get("content_encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointRequestConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.InputFormatConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"deserializer": "deserializer"},
    )
    class InputFormatConfigurationProperty:
        def __init__(
            self,
            *,
            deserializer: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DeserializerProperty"]] = None,
        ) -> None:
            '''
            :param deserializer: ``CfnDeliveryStream.InputFormatConfigurationProperty.Deserializer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if deserializer is not None:
                self._values["deserializer"] = deserializer

        @builtins.property
        def deserializer(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DeserializerProperty"]]:
            '''``CfnDeliveryStream.InputFormatConfigurationProperty.Deserializer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-inputformatconfiguration-deserializer
            '''
            result = self._values.get("deserializer")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.DeserializerProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputFormatConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"awskms_key_arn": "awskmsKeyArn"},
    )
    class KMSEncryptionConfigProperty:
        def __init__(self, *, awskms_key_arn: builtins.str) -> None:
            '''
            :param awskms_key_arn: ``CfnDeliveryStream.KMSEncryptionConfigProperty.AWSKMSKeyARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "awskms_key_arn": awskms_key_arn,
            }

        @builtins.property
        def awskms_key_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.KMSEncryptionConfigProperty.AWSKMSKeyARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html#cfn-kinesisfirehose-deliverystream-kmsencryptionconfig-awskmskeyarn
            '''
            result = self._values.get("awskms_key_arn")
            assert result is not None, "Required property 'awskms_key_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KMSEncryptionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kinesis_stream_arn": "kinesisStreamArn", "role_arn": "roleArn"},
    )
    class KinesisStreamSourceConfigurationProperty:
        def __init__(
            self,
            *,
            kinesis_stream_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''
            :param kinesis_stream_arn: ``CfnDeliveryStream.KinesisStreamSourceConfigurationProperty.KinesisStreamARN``.
            :param role_arn: ``CfnDeliveryStream.KinesisStreamSourceConfigurationProperty.RoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "kinesis_stream_arn": kinesis_stream_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def kinesis_stream_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.KinesisStreamSourceConfigurationProperty.KinesisStreamARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-kinesisstreamarn
            '''
            result = self._values.get("kinesis_stream_arn")
            assert result is not None, "Required property 'kinesis_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.KinesisStreamSourceConfigurationProperty.RoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "case_insensitive": "caseInsensitive",
            "column_to_json_key_mappings": "columnToJsonKeyMappings",
            "convert_dots_in_json_keys_to_underscores": "convertDotsInJsonKeysToUnderscores",
        },
    )
    class OpenXJsonSerDeProperty:
        def __init__(
            self,
            *,
            case_insensitive: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            column_to_json_key_mappings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param case_insensitive: ``CfnDeliveryStream.OpenXJsonSerDeProperty.CaseInsensitive``.
            :param column_to_json_key_mappings: ``CfnDeliveryStream.OpenXJsonSerDeProperty.ColumnToJsonKeyMappings``.
            :param convert_dots_in_json_keys_to_underscores: ``CfnDeliveryStream.OpenXJsonSerDeProperty.ConvertDotsInJsonKeysToUnderscores``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if case_insensitive is not None:
                self._values["case_insensitive"] = case_insensitive
            if column_to_json_key_mappings is not None:
                self._values["column_to_json_key_mappings"] = column_to_json_key_mappings
            if convert_dots_in_json_keys_to_underscores is not None:
                self._values["convert_dots_in_json_keys_to_underscores"] = convert_dots_in_json_keys_to_underscores

        @builtins.property
        def case_insensitive(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeliveryStream.OpenXJsonSerDeProperty.CaseInsensitive``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-caseinsensitive
            '''
            result = self._values.get("case_insensitive")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def column_to_json_key_mappings(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnDeliveryStream.OpenXJsonSerDeProperty.ColumnToJsonKeyMappings``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-columntojsonkeymappings
            '''
            result = self._values.get("column_to_json_key_mappings")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def convert_dots_in_json_keys_to_underscores(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeliveryStream.OpenXJsonSerDeProperty.ConvertDotsInJsonKeysToUnderscores``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-convertdotsinjsonkeystounderscores
            '''
            result = self._values.get("convert_dots_in_json_keys_to_underscores")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenXJsonSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "block_size_bytes": "blockSizeBytes",
            "bloom_filter_columns": "bloomFilterColumns",
            "bloom_filter_false_positive_probability": "bloomFilterFalsePositiveProbability",
            "compression": "compression",
            "dictionary_key_threshold": "dictionaryKeyThreshold",
            "enable_padding": "enablePadding",
            "format_version": "formatVersion",
            "padding_tolerance": "paddingTolerance",
            "row_index_stride": "rowIndexStride",
            "stripe_size_bytes": "stripeSizeBytes",
        },
    )
    class OrcSerDeProperty:
        def __init__(
            self,
            *,
            block_size_bytes: typing.Optional[jsii.Number] = None,
            bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
            bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
            compression: typing.Optional[builtins.str] = None,
            dictionary_key_threshold: typing.Optional[jsii.Number] = None,
            enable_padding: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            format_version: typing.Optional[builtins.str] = None,
            padding_tolerance: typing.Optional[jsii.Number] = None,
            row_index_stride: typing.Optional[jsii.Number] = None,
            stripe_size_bytes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param block_size_bytes: ``CfnDeliveryStream.OrcSerDeProperty.BlockSizeBytes``.
            :param bloom_filter_columns: ``CfnDeliveryStream.OrcSerDeProperty.BloomFilterColumns``.
            :param bloom_filter_false_positive_probability: ``CfnDeliveryStream.OrcSerDeProperty.BloomFilterFalsePositiveProbability``.
            :param compression: ``CfnDeliveryStream.OrcSerDeProperty.Compression``.
            :param dictionary_key_threshold: ``CfnDeliveryStream.OrcSerDeProperty.DictionaryKeyThreshold``.
            :param enable_padding: ``CfnDeliveryStream.OrcSerDeProperty.EnablePadding``.
            :param format_version: ``CfnDeliveryStream.OrcSerDeProperty.FormatVersion``.
            :param padding_tolerance: ``CfnDeliveryStream.OrcSerDeProperty.PaddingTolerance``.
            :param row_index_stride: ``CfnDeliveryStream.OrcSerDeProperty.RowIndexStride``.
            :param stripe_size_bytes: ``CfnDeliveryStream.OrcSerDeProperty.StripeSizeBytes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if block_size_bytes is not None:
                self._values["block_size_bytes"] = block_size_bytes
            if bloom_filter_columns is not None:
                self._values["bloom_filter_columns"] = bloom_filter_columns
            if bloom_filter_false_positive_probability is not None:
                self._values["bloom_filter_false_positive_probability"] = bloom_filter_false_positive_probability
            if compression is not None:
                self._values["compression"] = compression
            if dictionary_key_threshold is not None:
                self._values["dictionary_key_threshold"] = dictionary_key_threshold
            if enable_padding is not None:
                self._values["enable_padding"] = enable_padding
            if format_version is not None:
                self._values["format_version"] = format_version
            if padding_tolerance is not None:
                self._values["padding_tolerance"] = padding_tolerance
            if row_index_stride is not None:
                self._values["row_index_stride"] = row_index_stride
            if stripe_size_bytes is not None:
                self._values["stripe_size_bytes"] = stripe_size_bytes

        @builtins.property
        def block_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.OrcSerDeProperty.BlockSizeBytes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-blocksizebytes
            '''
            result = self._values.get("block_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def bloom_filter_columns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnDeliveryStream.OrcSerDeProperty.BloomFilterColumns``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfiltercolumns
            '''
            result = self._values.get("bloom_filter_columns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def bloom_filter_false_positive_probability(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.OrcSerDeProperty.BloomFilterFalsePositiveProbability``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfilterfalsepositiveprobability
            '''
            result = self._values.get("bloom_filter_false_positive_probability")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def compression(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.OrcSerDeProperty.Compression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-compression
            '''
            result = self._values.get("compression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dictionary_key_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.OrcSerDeProperty.DictionaryKeyThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-dictionarykeythreshold
            '''
            result = self._values.get("dictionary_key_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def enable_padding(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeliveryStream.OrcSerDeProperty.EnablePadding``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-enablepadding
            '''
            result = self._values.get("enable_padding")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def format_version(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.OrcSerDeProperty.FormatVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-formatversion
            '''
            result = self._values.get("format_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def padding_tolerance(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.OrcSerDeProperty.PaddingTolerance``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-paddingtolerance
            '''
            result = self._values.get("padding_tolerance")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def row_index_stride(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.OrcSerDeProperty.RowIndexStride``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-rowindexstride
            '''
            result = self._values.get("row_index_stride")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stripe_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.OrcSerDeProperty.StripeSizeBytes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-stripesizebytes
            '''
            result = self._values.get("stripe_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrcSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.OutputFormatConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"serializer": "serializer"},
    )
    class OutputFormatConfigurationProperty:
        def __init__(
            self,
            *,
            serializer: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SerializerProperty"]] = None,
        ) -> None:
            '''
            :param serializer: ``CfnDeliveryStream.OutputFormatConfigurationProperty.Serializer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if serializer is not None:
                self._values["serializer"] = serializer

        @builtins.property
        def serializer(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SerializerProperty"]]:
            '''``CfnDeliveryStream.OutputFormatConfigurationProperty.Serializer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-outputformatconfiguration-serializer
            '''
            result = self._values.get("serializer")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SerializerProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputFormatConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "block_size_bytes": "blockSizeBytes",
            "compression": "compression",
            "enable_dictionary_compression": "enableDictionaryCompression",
            "max_padding_bytes": "maxPaddingBytes",
            "page_size_bytes": "pageSizeBytes",
            "writer_version": "writerVersion",
        },
    )
    class ParquetSerDeProperty:
        def __init__(
            self,
            *,
            block_size_bytes: typing.Optional[jsii.Number] = None,
            compression: typing.Optional[builtins.str] = None,
            enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            max_padding_bytes: typing.Optional[jsii.Number] = None,
            page_size_bytes: typing.Optional[jsii.Number] = None,
            writer_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param block_size_bytes: ``CfnDeliveryStream.ParquetSerDeProperty.BlockSizeBytes``.
            :param compression: ``CfnDeliveryStream.ParquetSerDeProperty.Compression``.
            :param enable_dictionary_compression: ``CfnDeliveryStream.ParquetSerDeProperty.EnableDictionaryCompression``.
            :param max_padding_bytes: ``CfnDeliveryStream.ParquetSerDeProperty.MaxPaddingBytes``.
            :param page_size_bytes: ``CfnDeliveryStream.ParquetSerDeProperty.PageSizeBytes``.
            :param writer_version: ``CfnDeliveryStream.ParquetSerDeProperty.WriterVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if block_size_bytes is not None:
                self._values["block_size_bytes"] = block_size_bytes
            if compression is not None:
                self._values["compression"] = compression
            if enable_dictionary_compression is not None:
                self._values["enable_dictionary_compression"] = enable_dictionary_compression
            if max_padding_bytes is not None:
                self._values["max_padding_bytes"] = max_padding_bytes
            if page_size_bytes is not None:
                self._values["page_size_bytes"] = page_size_bytes
            if writer_version is not None:
                self._values["writer_version"] = writer_version

        @builtins.property
        def block_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.ParquetSerDeProperty.BlockSizeBytes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-blocksizebytes
            '''
            result = self._values.get("block_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def compression(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ParquetSerDeProperty.Compression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-compression
            '''
            result = self._values.get("compression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_dictionary_compression(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeliveryStream.ParquetSerDeProperty.EnableDictionaryCompression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-enabledictionarycompression
            '''
            result = self._values.get("enable_dictionary_compression")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def max_padding_bytes(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.ParquetSerDeProperty.MaxPaddingBytes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-maxpaddingbytes
            '''
            result = self._values.get("max_padding_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def page_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.ParquetSerDeProperty.PageSizeBytes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-pagesizebytes
            '''
            result = self._values.get("page_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def writer_version(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.ParquetSerDeProperty.WriterVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-writerversion
            '''
            result = self._values.get("writer_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParquetSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "processors": "processors"},
    )
    class ProcessingConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            processors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessorProperty"]]]] = None,
        ) -> None:
            '''
            :param enabled: ``CfnDeliveryStream.ProcessingConfigurationProperty.Enabled``.
            :param processors: ``CfnDeliveryStream.ProcessingConfigurationProperty.Processors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if processors is not None:
                self._values["processors"] = processors

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDeliveryStream.ProcessingConfigurationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def processors(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessorProperty"]]]]:
            '''``CfnDeliveryStream.ProcessingConfigurationProperty.Processors``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-processors
            '''
            result = self._values.get("processors")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessorProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ProcessorParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''
            :param parameter_name: ``CfnDeliveryStream.ProcessorParameterProperty.ParameterName``.
            :param parameter_value: ``CfnDeliveryStream.ProcessorParameterProperty.ParameterValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''``CfnDeliveryStream.ProcessorParameterProperty.ParameterName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''``CfnDeliveryStream.ProcessorParameterProperty.ParameterValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessorParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.ProcessorProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "parameters": "parameters"},
    )
    class ProcessorProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessorParameterProperty"]]]] = None,
        ) -> None:
            '''
            :param type: ``CfnDeliveryStream.ProcessorProperty.Type``.
            :param parameters: ``CfnDeliveryStream.ProcessorProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnDeliveryStream.ProcessorProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessorParameterProperty"]]]]:
            '''``CfnDeliveryStream.ProcessorProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessorParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.RedshiftDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_jdbcurl": "clusterJdbcurl",
            "copy_command": "copyCommand",
            "password": "password",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "username": "username",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_configuration": "s3BackupConfiguration",
            "s3_backup_mode": "s3BackupMode",
        },
    )
    class RedshiftDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            cluster_jdbcurl: builtins.str,
            copy_command: typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CopyCommandProperty"],
            password: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"],
            username: builtins.str,
            cloud_watch_logging_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]] = None,
            processing_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]] = None,
            retry_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RedshiftRetryOptionsProperty"]] = None,
            s3_backup_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param cluster_jdbcurl: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.ClusterJDBCURL``.
            :param copy_command: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.CopyCommand``.
            :param password: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.Password``.
            :param role_arn: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.RoleARN``.
            :param s3_configuration: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.S3Configuration``.
            :param username: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.Username``.
            :param cloud_watch_logging_options: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.CloudWatchLoggingOptions``.
            :param processing_configuration: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.ProcessingConfiguration``.
            :param retry_options: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.RetryOptions``.
            :param s3_backup_configuration: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.S3BackupConfiguration``.
            :param s3_backup_mode: ``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.S3BackupMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cluster_jdbcurl": cluster_jdbcurl,
                "copy_command": copy_command,
                "password": password,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
                "username": username,
            }
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_configuration is not None:
                self._values["s3_backup_configuration"] = s3_backup_configuration
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode

        @builtins.property
        def cluster_jdbcurl(self) -> builtins.str:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.ClusterJDBCURL``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-clusterjdbcurl
            '''
            result = self._values.get("cluster_jdbcurl")
            assert result is not None, "Required property 'cluster_jdbcurl' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def copy_command(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CopyCommandProperty"]:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.CopyCommand``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-copycommand
            '''
            result = self._values.get("copy_command")
            assert result is not None, "Required property 'copy_command' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CopyCommandProperty"], result)

        @builtins.property
        def password(self) -> builtins.str:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.Password``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.RoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.S3Configuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def username(self) -> builtins.str:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.CloudWatchLoggingOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.ProcessingConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RedshiftRetryOptionsProperty"]]:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.RetryOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.RedshiftRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]]:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.S3BackupConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupconfiguration
            '''
            result = self._values.get("s3_backup_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.RedshiftDestinationConfigurationProperty.S3BackupMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.RedshiftRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class RedshiftRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param duration_in_seconds: ``CfnDeliveryStream.RedshiftRetryOptionsProperty.DurationInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.RedshiftRetryOptionsProperty.DurationInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html#cfn-kinesisfirehose-deliverystream-redshiftretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class RetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param duration_in_seconds: ``CfnDeliveryStream.RetryOptionsProperty.DurationInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.RetryOptionsProperty.DurationInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html#cfn-kinesisfirehose-deliverystream-retryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "role_arn": "roleArn",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "compression_format": "compressionFormat",
            "encryption_configuration": "encryptionConfiguration",
            "error_output_prefix": "errorOutputPrefix",
            "prefix": "prefix",
        },
    )
    class S3DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            role_arn: builtins.str,
            buffering_hints: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.BufferingHintsProperty"]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]] = None,
            compression_format: typing.Optional[builtins.str] = None,
            encryption_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.EncryptionConfigurationProperty"]] = None,
            error_output_prefix: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket_arn: ``CfnDeliveryStream.S3DestinationConfigurationProperty.BucketARN``.
            :param role_arn: ``CfnDeliveryStream.S3DestinationConfigurationProperty.RoleARN``.
            :param buffering_hints: ``CfnDeliveryStream.S3DestinationConfigurationProperty.BufferingHints``.
            :param cloud_watch_logging_options: ``CfnDeliveryStream.S3DestinationConfigurationProperty.CloudWatchLoggingOptions``.
            :param compression_format: ``CfnDeliveryStream.S3DestinationConfigurationProperty.CompressionFormat``.
            :param encryption_configuration: ``CfnDeliveryStream.S3DestinationConfigurationProperty.EncryptionConfiguration``.
            :param error_output_prefix: ``CfnDeliveryStream.S3DestinationConfigurationProperty.ErrorOutputPrefix``.
            :param prefix: ``CfnDeliveryStream.S3DestinationConfigurationProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "role_arn": role_arn,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if compression_format is not None:
                self._values["compression_format"] = compression_format
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if error_output_prefix is not None:
                self._values["error_output_prefix"] = error_output_prefix
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.S3DestinationConfigurationProperty.BucketARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.S3DestinationConfigurationProperty.RoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.BufferingHintsProperty"]]:
            '''``CfnDeliveryStream.S3DestinationConfigurationProperty.BufferingHints``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.BufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''``CfnDeliveryStream.S3DestinationConfigurationProperty.CloudWatchLoggingOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def compression_format(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.S3DestinationConfigurationProperty.CompressionFormat``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-compressionformat
            '''
            result = self._values.get("compression_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.EncryptionConfigurationProperty"]]:
            '''``CfnDeliveryStream.S3DestinationConfigurationProperty.EncryptionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.EncryptionConfigurationProperty"]], result)

        @builtins.property
        def error_output_prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.S3DestinationConfigurationProperty.ErrorOutputPrefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-erroroutputprefix
            '''
            result = self._values.get("error_output_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.S3DestinationConfigurationProperty.Prefix``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.SchemaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "region": "region",
            "role_arn": "roleArn",
            "table_name": "tableName",
            "version_id": "versionId",
        },
    )
    class SchemaConfigurationProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
            table_name: typing.Optional[builtins.str] = None,
            version_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param catalog_id: ``CfnDeliveryStream.SchemaConfigurationProperty.CatalogId``.
            :param database_name: ``CfnDeliveryStream.SchemaConfigurationProperty.DatabaseName``.
            :param region: ``CfnDeliveryStream.SchemaConfigurationProperty.Region``.
            :param role_arn: ``CfnDeliveryStream.SchemaConfigurationProperty.RoleARN``.
            :param table_name: ``CfnDeliveryStream.SchemaConfigurationProperty.TableName``.
            :param version_id: ``CfnDeliveryStream.SchemaConfigurationProperty.VersionId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name
            if region is not None:
                self._values["region"] = region
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if table_name is not None:
                self._values["table_name"] = table_name
            if version_id is not None:
                self._values["version_id"] = version_id

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.SchemaConfigurationProperty.CatalogId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.SchemaConfigurationProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.SchemaConfigurationProperty.Region``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.SchemaConfigurationProperty.RoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_name(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.SchemaConfigurationProperty.TableName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-tablename
            '''
            result = self._values.get("table_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version_id(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.SchemaConfigurationProperty.VersionId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-versionid
            '''
            result = self._values.get("version_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.SerializerProperty",
        jsii_struct_bases=[],
        name_mapping={"orc_ser_de": "orcSerDe", "parquet_ser_de": "parquetSerDe"},
    )
    class SerializerProperty:
        def __init__(
            self,
            *,
            orc_ser_de: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.OrcSerDeProperty"]] = None,
            parquet_ser_de: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ParquetSerDeProperty"]] = None,
        ) -> None:
            '''
            :param orc_ser_de: ``CfnDeliveryStream.SerializerProperty.OrcSerDe``.
            :param parquet_ser_de: ``CfnDeliveryStream.SerializerProperty.ParquetSerDe``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if orc_ser_de is not None:
                self._values["orc_ser_de"] = orc_ser_de
            if parquet_ser_de is not None:
                self._values["parquet_ser_de"] = parquet_ser_de

        @builtins.property
        def orc_ser_de(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.OrcSerDeProperty"]]:
            '''``CfnDeliveryStream.SerializerProperty.OrcSerDe``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-orcserde
            '''
            result = self._values.get("orc_ser_de")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.OrcSerDeProperty"]], result)

        @builtins.property
        def parquet_ser_de(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ParquetSerDeProperty"]]:
            '''``CfnDeliveryStream.SerializerProperty.ParquetSerDe``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-parquetserde
            '''
            result = self._values.get("parquet_ser_de")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ParquetSerDeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SerializerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.SplunkDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hec_endpoint": "hecEndpoint",
            "hec_endpoint_type": "hecEndpointType",
            "hec_token": "hecToken",
            "s3_configuration": "s3Configuration",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "hec_acknowledgment_timeout_in_seconds": "hecAcknowledgmentTimeoutInSeconds",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
        },
    )
    class SplunkDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            hec_endpoint: builtins.str,
            hec_endpoint_type: builtins.str,
            hec_token: builtins.str,
            s3_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"],
            cloud_watch_logging_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]] = None,
            hec_acknowledgment_timeout_in_seconds: typing.Optional[jsii.Number] = None,
            processing_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]] = None,
            retry_options: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SplunkRetryOptionsProperty"]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param hec_endpoint: ``CfnDeliveryStream.SplunkDestinationConfigurationProperty.HECEndpoint``.
            :param hec_endpoint_type: ``CfnDeliveryStream.SplunkDestinationConfigurationProperty.HECEndpointType``.
            :param hec_token: ``CfnDeliveryStream.SplunkDestinationConfigurationProperty.HECToken``.
            :param s3_configuration: ``CfnDeliveryStream.SplunkDestinationConfigurationProperty.S3Configuration``.
            :param cloud_watch_logging_options: ``CfnDeliveryStream.SplunkDestinationConfigurationProperty.CloudWatchLoggingOptions``.
            :param hec_acknowledgment_timeout_in_seconds: ``CfnDeliveryStream.SplunkDestinationConfigurationProperty.HECAcknowledgmentTimeoutInSeconds``.
            :param processing_configuration: ``CfnDeliveryStream.SplunkDestinationConfigurationProperty.ProcessingConfiguration``.
            :param retry_options: ``CfnDeliveryStream.SplunkDestinationConfigurationProperty.RetryOptions``.
            :param s3_backup_mode: ``CfnDeliveryStream.SplunkDestinationConfigurationProperty.S3BackupMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "hec_endpoint": hec_endpoint,
                "hec_endpoint_type": hec_endpoint_type,
                "hec_token": hec_token,
                "s3_configuration": s3_configuration,
            }
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if hec_acknowledgment_timeout_in_seconds is not None:
                self._values["hec_acknowledgment_timeout_in_seconds"] = hec_acknowledgment_timeout_in_seconds
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode

        @builtins.property
        def hec_endpoint(self) -> builtins.str:
            '''``CfnDeliveryStream.SplunkDestinationConfigurationProperty.HECEndpoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpoint
            '''
            result = self._values.get("hec_endpoint")
            assert result is not None, "Required property 'hec_endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hec_endpoint_type(self) -> builtins.str:
            '''``CfnDeliveryStream.SplunkDestinationConfigurationProperty.HECEndpointType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpointtype
            '''
            result = self._values.get("hec_endpoint_type")
            assert result is not None, "Required property 'hec_endpoint_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hec_token(self) -> builtins.str:
            '''``CfnDeliveryStream.SplunkDestinationConfigurationProperty.HECToken``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hectoken
            '''
            result = self._values.get("hec_token")
            assert result is not None, "Required property 'hec_token' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''``CfnDeliveryStream.SplunkDestinationConfigurationProperty.S3Configuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''``CfnDeliveryStream.SplunkDestinationConfigurationProperty.CloudWatchLoggingOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def hec_acknowledgment_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.SplunkDestinationConfigurationProperty.HECAcknowledgmentTimeoutInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecacknowledgmenttimeoutinseconds
            '''
            result = self._values.get("hec_acknowledgment_timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''``CfnDeliveryStream.SplunkDestinationConfigurationProperty.ProcessingConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SplunkRetryOptionsProperty"]]:
            '''``CfnDeliveryStream.SplunkDestinationConfigurationProperty.RetryOptions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryStream.SplunkRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnDeliveryStream.SplunkDestinationConfigurationProperty.S3BackupMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SplunkDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.SplunkRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class SplunkRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param duration_in_seconds: ``CfnDeliveryStream.SplunkRetryOptionsProperty.DurationInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''``CfnDeliveryStream.SplunkRetryOptionsProperty.DurationInSeconds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html#cfn-kinesisfirehose-deliverystream-splunkretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SplunkRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigurationProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param role_arn: ``CfnDeliveryStream.VpcConfigurationProperty.RoleARN``.
            :param security_group_ids: ``CfnDeliveryStream.VpcConfigurationProperty.SecurityGroupIds``.
            :param subnet_ids: ``CfnDeliveryStream.VpcConfigurationProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "role_arn": role_arn,
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''``CfnDeliveryStream.VpcConfigurationProperty.RoleARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''``CfnDeliveryStream.VpcConfigurationProperty.SecurityGroupIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''``CfnDeliveryStream.VpcConfigurationProperty.SubnetIds``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisfirehose.CfnDeliveryStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "amazonopensearchservice_destination_configuration": "amazonopensearchserviceDestinationConfiguration",
        "delivery_stream_encryption_configuration_input": "deliveryStreamEncryptionConfigurationInput",
        "delivery_stream_name": "deliveryStreamName",
        "delivery_stream_type": "deliveryStreamType",
        "elasticsearch_destination_configuration": "elasticsearchDestinationConfiguration",
        "extended_s3_destination_configuration": "extendedS3DestinationConfiguration",
        "http_endpoint_destination_configuration": "httpEndpointDestinationConfiguration",
        "kinesis_stream_source_configuration": "kinesisStreamSourceConfiguration",
        "redshift_destination_configuration": "redshiftDestinationConfiguration",
        "s3_destination_configuration": "s3DestinationConfiguration",
        "splunk_destination_configuration": "splunkDestinationConfiguration",
        "tags": "tags",
    },
)
class CfnDeliveryStreamProps:
    def __init__(
        self,
        *,
        amazonopensearchservice_destination_configuration: typing.Optional[typing.Union[CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty, aws_cdk.core.IResolvable]] = None,
        delivery_stream_encryption_configuration_input: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty]] = None,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        delivery_stream_type: typing.Optional[builtins.str] = None,
        elasticsearch_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty]] = None,
        extended_s3_destination_configuration: typing.Optional[typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, aws_cdk.core.IResolvable]] = None,
        http_endpoint_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty]] = None,
        kinesis_stream_source_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.KinesisStreamSourceConfigurationProperty]] = None,
        redshift_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.RedshiftDestinationConfigurationProperty]] = None,
        s3_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.S3DestinationConfigurationProperty]] = None,
        splunk_destination_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.SplunkDestinationConfigurationProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::KinesisFirehose::DeliveryStream``.

        :param amazonopensearchservice_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceDestinationConfiguration``.
        :param delivery_stream_encryption_configuration_input: ``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamEncryptionConfigurationInput``.
        :param delivery_stream_name: ``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamName``.
        :param delivery_stream_type: ``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamType``.
        :param elasticsearch_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.ElasticsearchDestinationConfiguration``.
        :param extended_s3_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.ExtendedS3DestinationConfiguration``.
        :param http_endpoint_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.HttpEndpointDestinationConfiguration``.
        :param kinesis_stream_source_configuration: ``AWS::KinesisFirehose::DeliveryStream.KinesisStreamSourceConfiguration``.
        :param redshift_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.RedshiftDestinationConfiguration``.
        :param s3_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.S3DestinationConfiguration``.
        :param splunk_destination_configuration: ``AWS::KinesisFirehose::DeliveryStream.SplunkDestinationConfiguration``.
        :param tags: ``AWS::KinesisFirehose::DeliveryStream.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if amazonopensearchservice_destination_configuration is not None:
            self._values["amazonopensearchservice_destination_configuration"] = amazonopensearchservice_destination_configuration
        if delivery_stream_encryption_configuration_input is not None:
            self._values["delivery_stream_encryption_configuration_input"] = delivery_stream_encryption_configuration_input
        if delivery_stream_name is not None:
            self._values["delivery_stream_name"] = delivery_stream_name
        if delivery_stream_type is not None:
            self._values["delivery_stream_type"] = delivery_stream_type
        if elasticsearch_destination_configuration is not None:
            self._values["elasticsearch_destination_configuration"] = elasticsearch_destination_configuration
        if extended_s3_destination_configuration is not None:
            self._values["extended_s3_destination_configuration"] = extended_s3_destination_configuration
        if http_endpoint_destination_configuration is not None:
            self._values["http_endpoint_destination_configuration"] = http_endpoint_destination_configuration
        if kinesis_stream_source_configuration is not None:
            self._values["kinesis_stream_source_configuration"] = kinesis_stream_source_configuration
        if redshift_destination_configuration is not None:
            self._values["redshift_destination_configuration"] = redshift_destination_configuration
        if s3_destination_configuration is not None:
            self._values["s3_destination_configuration"] = s3_destination_configuration
        if splunk_destination_configuration is not None:
            self._values["splunk_destination_configuration"] = splunk_destination_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def amazonopensearchservice_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::KinesisFirehose::DeliveryStream.AmazonopensearchserviceDestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration
        '''
        result = self._values.get("amazonopensearchservice_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def delivery_stream_encryption_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty]]:
        '''``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamEncryptionConfigurationInput``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput
        '''
        result = self._values.get("delivery_stream_encryption_configuration_input")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty]], result)

    @builtins.property
    def delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamname
        '''
        result = self._values.get("delivery_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_stream_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::KinesisFirehose::DeliveryStream.DeliveryStreamType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamtype
        '''
        result = self._values.get("delivery_stream_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticsearch_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty]]:
        '''``AWS::KinesisFirehose::DeliveryStream.ElasticsearchDestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration
        '''
        result = self._values.get("elasticsearch_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty]], result)

    @builtins.property
    def extended_s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::KinesisFirehose::DeliveryStream.ExtendedS3DestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration
        '''
        result = self._values.get("extended_s3_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def http_endpoint_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty]]:
        '''``AWS::KinesisFirehose::DeliveryStream.HttpEndpointDestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration
        '''
        result = self._values.get("http_endpoint_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty]], result)

    @builtins.property
    def kinesis_stream_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.KinesisStreamSourceConfigurationProperty]]:
        '''``AWS::KinesisFirehose::DeliveryStream.KinesisStreamSourceConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration
        '''
        result = self._values.get("kinesis_stream_source_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.KinesisStreamSourceConfigurationProperty]], result)

    @builtins.property
    def redshift_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.RedshiftDestinationConfigurationProperty]]:
        '''``AWS::KinesisFirehose::DeliveryStream.RedshiftDestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration
        '''
        result = self._values.get("redshift_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.RedshiftDestinationConfigurationProperty]], result)

    @builtins.property
    def s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.S3DestinationConfigurationProperty]]:
        '''``AWS::KinesisFirehose::DeliveryStream.S3DestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration
        '''
        result = self._values.get("s3_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.S3DestinationConfigurationProperty]], result)

    @builtins.property
    def splunk_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.SplunkDestinationConfigurationProperty]]:
        '''``AWS::KinesisFirehose::DeliveryStream.SplunkDestinationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration
        '''
        result = self._values.get("splunk_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDeliveryStream.SplunkDestinationConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::KinesisFirehose::DeliveryStream.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeliveryStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisfirehose.DataProcessorBindOptions",
    jsii_struct_bases=[],
    name_mapping={"role": "role"},
)
class DataProcessorBindOptions:
    def __init__(self, *, role: aws_cdk.aws_iam.IRole) -> None:
        '''(experimental) Options when binding a DataProcessor to a delivery stream destination.

        :param role: (experimental) The IAM role assumed by Kinesis Data Firehose to write to the destination that this DataProcessor will bind to.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "role": role,
        }

    @builtins.property
    def role(self) -> aws_cdk.aws_iam.IRole:
        '''(experimental) The IAM role assumed by Kinesis Data Firehose to write to the destination that this DataProcessor will bind to.

        :stability: experimental
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(aws_cdk.aws_iam.IRole, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProcessorBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisfirehose.DataProcessorConfig",
    jsii_struct_bases=[],
    name_mapping={
        "processor_identifier": "processorIdentifier",
        "processor_type": "processorType",
    },
)
class DataProcessorConfig:
    def __init__(
        self,
        *,
        processor_identifier: "DataProcessorIdentifier",
        processor_type: builtins.str,
    ) -> None:
        '''(experimental) The full configuration of a data processor.

        :param processor_identifier: (experimental) The key-value pair that identifies the underlying processor resource.
        :param processor_type: (experimental) The type of the underlying processor resource. Must be an accepted value in ``CfnDeliveryStream.ProcessorProperty.Type``.

        :stability: experimental
        '''
        if isinstance(processor_identifier, dict):
            processor_identifier = DataProcessorIdentifier(**processor_identifier)
        self._values: typing.Dict[str, typing.Any] = {
            "processor_identifier": processor_identifier,
            "processor_type": processor_type,
        }

    @builtins.property
    def processor_identifier(self) -> "DataProcessorIdentifier":
        '''(experimental) The key-value pair that identifies the underlying processor resource.

        :stability: experimental
        '''
        result = self._values.get("processor_identifier")
        assert result is not None, "Required property 'processor_identifier' is missing"
        return typing.cast("DataProcessorIdentifier", result)

    @builtins.property
    def processor_type(self) -> builtins.str:
        '''(experimental) The type of the underlying processor resource.

        Must be an accepted value in ``CfnDeliveryStream.ProcessorProperty.Type``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-type
        :stability: experimental

        Example::

            # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
            "Lambda"
        '''
        result = self._values.get("processor_type")
        assert result is not None, "Required property 'processor_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProcessorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisfirehose.DataProcessorIdentifier",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_name": "parameterName",
        "parameter_value": "parameterValue",
    },
)
class DataProcessorIdentifier:
    def __init__(
        self,
        *,
        parameter_name: builtins.str,
        parameter_value: builtins.str,
    ) -> None:
        '''(experimental) The key-value pair that identifies the underlying processor resource.

        :param parameter_name: (experimental) The parameter name that corresponds to the processor resource's identifier. Must be an accepted value in ``CfnDeliveryStream.ProcessoryParameterProperty.ParameterName``.
        :param parameter_value: (experimental) The identifier of the underlying processor resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html
        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "parameter_name": parameter_name,
            "parameter_value": parameter_value,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''(experimental) The parameter name that corresponds to the processor resource's identifier.

        Must be an accepted value in ``CfnDeliveryStream.ProcessoryParameterProperty.ParameterName``.

        :stability: experimental
        '''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_value(self) -> builtins.str:
        '''(experimental) The identifier of the underlying processor resource.

        :stability: experimental
        '''
        result = self._values.get("parameter_value")
        assert result is not None, "Required property 'parameter_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProcessorIdentifier(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisfirehose.DataProcessorProps",
    jsii_struct_bases=[],
    name_mapping={
        "buffer_interval": "bufferInterval",
        "buffer_size": "bufferSize",
        "retries": "retries",
    },
)
class DataProcessorProps:
    def __init__(
        self,
        *,
        buffer_interval: typing.Optional[aws_cdk.core.Duration] = None,
        buffer_size: typing.Optional[aws_cdk.core.Size] = None,
        retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Configure the data processor.

        :param buffer_interval: (experimental) The length of time Kinesis Data Firehose will buffer incoming data before calling the processor. s Default: Duration.minutes(1)
        :param buffer_size: (experimental) The amount of incoming data Kinesis Data Firehose will buffer before calling the processor. Default: Size.mebibytes(3)
        :param retries: (experimental) The number of times Kinesis Data Firehose will retry the processor invocation after a failure due to network timeout or invocation limits. Default: 3

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if buffer_interval is not None:
            self._values["buffer_interval"] = buffer_interval
        if buffer_size is not None:
            self._values["buffer_size"] = buffer_size
        if retries is not None:
            self._values["retries"] = retries

    @builtins.property
    def buffer_interval(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''(experimental) The length of time Kinesis Data Firehose will buffer incoming data before calling the processor.

        s

        :default: Duration.minutes(1)

        :stability: experimental
        '''
        result = self._values.get("buffer_interval")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def buffer_size(self) -> typing.Optional[aws_cdk.core.Size]:
        '''(experimental) The amount of incoming data Kinesis Data Firehose will buffer before calling the processor.

        :default: Size.mebibytes(3)

        :stability: experimental
        '''
        result = self._values.get("buffer_size")
        return typing.cast(typing.Optional[aws_cdk.core.Size], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of times Kinesis Data Firehose will retry the processor invocation after a failure due to network timeout or invocation limits.

        :default: 3

        :stability: experimental
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProcessorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisfirehose.DeliveryStreamAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "delivery_stream_arn": "deliveryStreamArn",
        "delivery_stream_name": "deliveryStreamName",
        "role": "role",
    },
)
class DeliveryStreamAttributes:
    def __init__(
        self,
        *,
        delivery_stream_arn: typing.Optional[builtins.str] = None,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''(experimental) A full specification of a delivery stream that can be used to import it fluently into the CDK application.

        :param delivery_stream_arn: (experimental) The ARN of the delivery stream. At least one of deliveryStreamArn and deliveryStreamName must be provided. Default: - derived from ``deliveryStreamName``.
        :param delivery_stream_name: (experimental) The name of the delivery stream. At least one of deliveryStreamName and deliveryStreamArn must be provided. Default: - derived from ``deliveryStreamArn``.
        :param role: (experimental) The IAM role associated with this delivery stream. Assumed by Kinesis Data Firehose to read from sources and encrypt data server-side. Default: - the imported stream cannot be granted access to other resources as an ``iam.IGrantable``.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if delivery_stream_arn is not None:
            self._values["delivery_stream_arn"] = delivery_stream_arn
        if delivery_stream_name is not None:
            self._values["delivery_stream_name"] = delivery_stream_name
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def delivery_stream_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) The ARN of the delivery stream.

        At least one of deliveryStreamArn and deliveryStreamName must be provided.

        :default: - derived from ``deliveryStreamName``.

        :stability: experimental
        '''
        result = self._values.get("delivery_stream_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the delivery stream.

        At least one of deliveryStreamName and deliveryStreamArn  must be provided.

        :default: - derived from ``deliveryStreamArn``.

        :stability: experimental
        '''
        result = self._values.get("delivery_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role associated with this delivery stream.

        Assumed by Kinesis Data Firehose to read from sources and encrypt data server-side.

        :default: - the imported stream cannot be granted access to other resources as an ``iam.IGrantable``.

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeliveryStreamAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisfirehose.DeliveryStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "destinations": "destinations",
        "delivery_stream_name": "deliveryStreamName",
        "encryption": "encryption",
        "encryption_key": "encryptionKey",
        "role": "role",
        "source_stream": "sourceStream",
    },
)
class DeliveryStreamProps:
    def __init__(
        self,
        *,
        destinations: typing.Sequence["IDestination"],
        delivery_stream_name: typing.Optional[builtins.str] = None,
        encryption: typing.Optional["StreamEncryption"] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        source_stream: typing.Optional[aws_cdk.aws_kinesis.IStream] = None,
    ) -> None:
        '''(experimental) Properties for a new delivery stream.

        :param destinations: (experimental) The destinations that this delivery stream will deliver data to. Only a singleton array is supported at this time.
        :param delivery_stream_name: (experimental) A name for the delivery stream. Default: - a name is generated by CloudFormation.
        :param encryption: (experimental) Indicates the type of customer master key (CMK) to use for server-side encryption, if any. Default: StreamEncryption.UNENCRYPTED - unless ``encryptionKey`` is provided, in which case this will be implicitly set to ``StreamEncryption.CUSTOMER_MANAGED``
        :param encryption_key: (experimental) Customer managed key to server-side encrypt data in the stream. Default: - no KMS key will be used; if ``encryption`` is set to ``CUSTOMER_MANAGED``, a KMS key will be created for you
        :param role: (experimental) The IAM role associated with this delivery stream. Assumed by Kinesis Data Firehose to read from sources and encrypt data server-side. Default: - a role will be created with default permissions.
        :param source_stream: (experimental) The Kinesis data stream to use as a source for this delivery stream. Default: - data must be written to the delivery stream via a direct put.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "destinations": destinations,
        }
        if delivery_stream_name is not None:
            self._values["delivery_stream_name"] = delivery_stream_name
        if encryption is not None:
            self._values["encryption"] = encryption
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if role is not None:
            self._values["role"] = role
        if source_stream is not None:
            self._values["source_stream"] = source_stream

    @builtins.property
    def destinations(self) -> typing.List["IDestination"]:
        '''(experimental) The destinations that this delivery stream will deliver data to.

        Only a singleton array is supported at this time.

        :stability: experimental
        '''
        result = self._values.get("destinations")
        assert result is not None, "Required property 'destinations' is missing"
        return typing.cast(typing.List["IDestination"], result)

    @builtins.property
    def delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for the delivery stream.

        :default: - a name is generated by CloudFormation.

        :stability: experimental
        '''
        result = self._values.get("delivery_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption(self) -> typing.Optional["StreamEncryption"]:
        '''(experimental) Indicates the type of customer master key (CMK) to use for server-side encryption, if any.

        :default: StreamEncryption.UNENCRYPTED - unless ``encryptionKey`` is provided, in which case this will be implicitly set to ``StreamEncryption.CUSTOMER_MANAGED``

        :stability: experimental
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional["StreamEncryption"], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        '''(experimental) Customer managed key to server-side encrypt data in the stream.

        :default: - no KMS key will be used; if ``encryption`` is set to ``CUSTOMER_MANAGED``, a KMS key will be created for you

        :stability: experimental
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role associated with this delivery stream.

        Assumed by Kinesis Data Firehose to read from sources and encrypt data server-side.

        :default: - a role will be created with default permissions.

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def source_stream(self) -> typing.Optional[aws_cdk.aws_kinesis.IStream]:
        '''(experimental) The Kinesis data stream to use as a source for this delivery stream.

        :default: - data must be written to the delivery stream via a direct put.

        :stability: experimental
        '''
        result = self._values.get("source_stream")
        return typing.cast(typing.Optional[aws_cdk.aws_kinesis.IStream], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeliveryStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisfirehose.DestinationBindOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DestinationBindOptions:
    def __init__(self) -> None:
        '''(experimental) Options when binding a destination to a delivery stream.

        :stability: experimental
        '''
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-kinesisfirehose.DestinationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "dependables": "dependables",
        "extended_s3_destination_configuration": "extendedS3DestinationConfiguration",
    },
)
class DestinationConfig:
    def __init__(
        self,
        *,
        dependables: typing.Optional[typing.Sequence[aws_cdk.core.IDependable]] = None,
        extended_s3_destination_configuration: typing.Optional[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty] = None,
    ) -> None:
        '''(experimental) A Kinesis Data Firehose delivery stream destination configuration.

        :param dependables: (experimental) Any resources that were created by the destination when binding it to the stack that must be deployed before the delivery stream is deployed. Default: []
        :param extended_s3_destination_configuration: (experimental) S3 destination configuration properties. Default: - S3 destination is not used.

        :stability: experimental
        '''
        if isinstance(extended_s3_destination_configuration, dict):
            extended_s3_destination_configuration = CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty(**extended_s3_destination_configuration)
        self._values: typing.Dict[str, typing.Any] = {}
        if dependables is not None:
            self._values["dependables"] = dependables
        if extended_s3_destination_configuration is not None:
            self._values["extended_s3_destination_configuration"] = extended_s3_destination_configuration

    @builtins.property
    def dependables(self) -> typing.Optional[typing.List[aws_cdk.core.IDependable]]:
        '''(experimental) Any resources that were created by the destination when binding it to the stack that must be deployed before the delivery stream is deployed.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("dependables")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.IDependable]], result)

    @builtins.property
    def extended_s3_destination_configuration(
        self,
    ) -> typing.Optional[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty]:
        '''(experimental) S3 destination configuration properties.

        :default: - S3 destination is not used.

        :stability: experimental
        '''
        result = self._values.get("extended_s3_destination_configuration")
        return typing.cast(typing.Optional[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-kinesisfirehose.IDataProcessor")
class IDataProcessor(typing_extensions.Protocol):
    '''(experimental) A data processor that Kinesis Data Firehose will call to transform records before delivering data.

    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> DataProcessorProps:
        '''(experimental) The constructor props of the DataProcessor.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: constructs.Construct,
        *,
        role: aws_cdk.aws_iam.IRole,
    ) -> DataProcessorConfig:
        '''(experimental) Binds this processor to a destination of a delivery stream.

        Implementers should use this method to grant processor invocation permissions to the provided stream and return the
        necessary configuration to register as a processor.

        :param scope: -
        :param role: (experimental) The IAM role assumed by Kinesis Data Firehose to write to the destination that this DataProcessor will bind to.

        :stability: experimental
        '''
        ...


class _IDataProcessorProxy:
    '''(experimental) A data processor that Kinesis Data Firehose will call to transform records before delivering data.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-kinesisfirehose.IDataProcessor"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> DataProcessorProps:
        '''(experimental) The constructor props of the DataProcessor.

        :stability: experimental
        '''
        return typing.cast(DataProcessorProps, jsii.get(self, "props"))

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: constructs.Construct,
        *,
        role: aws_cdk.aws_iam.IRole,
    ) -> DataProcessorConfig:
        '''(experimental) Binds this processor to a destination of a delivery stream.

        Implementers should use this method to grant processor invocation permissions to the provided stream and return the
        necessary configuration to register as a processor.

        :param scope: -
        :param role: (experimental) The IAM role assumed by Kinesis Data Firehose to write to the destination that this DataProcessor will bind to.

        :stability: experimental
        '''
        options = DataProcessorBindOptions(role=role)

        return typing.cast(DataProcessorConfig, jsii.invoke(self, "bind", [scope, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataProcessor).__jsii_proxy_class__ = lambda : _IDataProcessorProxy


@jsii.interface(jsii_type="@aws-cdk/aws-kinesisfirehose.IDeliveryStream")
class IDeliveryStream(
    aws_cdk.core.IResource,
    aws_cdk.aws_iam.IGrantable,
    aws_cdk.aws_ec2.IConnectable,
    typing_extensions.Protocol,
):
    '''(experimental) Represents a Kinesis Data Firehose delivery stream.

    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deliveryStreamArn")
    def delivery_stream_arn(self) -> builtins.str:
        '''(experimental) The ARN of the delivery stream.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        '''(experimental) The name of the delivery stream.

        :stability: experimental
        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
        *actions: builtins.str,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the ``grantee`` identity permissions to perform ``actions``.

        :param grantee: -
        :param actions: -

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantPutRecords")
    def grant_put_records(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the ``grantee`` identity permissions to perform ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` actions on this delivery stream.

        :param grantee: -

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric for this delivery stream.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricBackupToS3Bytes")
    def metric_backup_to_s3_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of bytes delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricBackupToS3DataFreshness")
    def metric_backup_to_s3_data_freshness(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the age (from getting into Kinesis Data Firehose to now) of the oldest record in Kinesis Data Firehose.

        Any record older than this age has been delivered to the Amazon S3 bucket for backup.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricBackupToS3Records")
    def metric_backup_to_s3_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of records delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricIncomingBytes")
    def metric_incoming_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of bytes ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metricIncomingRecords")
    def metric_incoming_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of records ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        ...


class _IDeliveryStreamProxy(
    jsii.proxy_for(aws_cdk.core.IResource), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_iam.IGrantable), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_ec2.IConnectable), # type: ignore[misc]
):
    '''(experimental) Represents a Kinesis Data Firehose delivery stream.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-kinesisfirehose.IDeliveryStream"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deliveryStreamArn")
    def delivery_stream_arn(self) -> builtins.str:
        '''(experimental) The ARN of the delivery stream.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        '''(experimental) The name of the delivery stream.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamName"))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
        *actions: builtins.str,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the ``grantee`` identity permissions to perform ``actions``.

        :param grantee: -
        :param actions: -

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantPutRecords")
    def grant_put_records(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the ``grantee`` identity permissions to perform ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` actions on this delivery stream.

        :param grantee: -

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantPutRecords", [grantee]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric for this delivery stream.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricBackupToS3Bytes")
    def metric_backup_to_s3_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of bytes delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricBackupToS3Bytes", [props]))

    @jsii.member(jsii_name="metricBackupToS3DataFreshness")
    def metric_backup_to_s3_data_freshness(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the age (from getting into Kinesis Data Firehose to now) of the oldest record in Kinesis Data Firehose.

        Any record older than this age has been delivered to the Amazon S3 bucket for backup.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricBackupToS3DataFreshness", [props]))

    @jsii.member(jsii_name="metricBackupToS3Records")
    def metric_backup_to_s3_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of records delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricBackupToS3Records", [props]))

    @jsii.member(jsii_name="metricIncomingBytes")
    def metric_incoming_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of bytes ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricIncomingBytes", [props]))

    @jsii.member(jsii_name="metricIncomingRecords")
    def metric_incoming_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of records ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricIncomingRecords", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeliveryStream).__jsii_proxy_class__ = lambda : _IDeliveryStreamProxy


@jsii.interface(jsii_type="@aws-cdk/aws-kinesisfirehose.IDestination")
class IDestination(typing_extensions.Protocol):
    '''(experimental) A Kinesis Data Firehose delivery stream destination.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self, scope: constructs.Construct) -> DestinationConfig:
        '''(experimental) Binds this destination to the Kinesis Data Firehose delivery stream.

        Implementers should use this method to bind resources to the stack and initialize values using the provided stream.

        :param scope: -

        :stability: experimental
        '''
        ...


class _IDestinationProxy:
    '''(experimental) A Kinesis Data Firehose delivery stream destination.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-kinesisfirehose.IDestination"

    @jsii.member(jsii_name="bind")
    def bind(self, scope: constructs.Construct) -> DestinationConfig:
        '''(experimental) Binds this destination to the Kinesis Data Firehose delivery stream.

        Implementers should use this method to bind resources to the stack and initialize values using the provided stream.

        :param scope: -

        :stability: experimental
        '''
        options = DestinationBindOptions()

        return typing.cast(DestinationConfig, jsii.invoke(self, "bind", [scope, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDestination).__jsii_proxy_class__ = lambda : _IDestinationProxy


@jsii.implements(IDataProcessor)
class LambdaFunctionProcessor(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kinesisfirehose.LambdaFunctionProcessor",
):
    '''(experimental) Use an AWS Lambda function to transform records.

    :stability: experimental
    '''

    def __init__(
        self,
        lambda_function: aws_cdk.aws_lambda.IFunction,
        *,
        buffer_interval: typing.Optional[aws_cdk.core.Duration] = None,
        buffer_size: typing.Optional[aws_cdk.core.Size] = None,
        retries: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param lambda_function: -
        :param buffer_interval: (experimental) The length of time Kinesis Data Firehose will buffer incoming data before calling the processor. s Default: Duration.minutes(1)
        :param buffer_size: (experimental) The amount of incoming data Kinesis Data Firehose will buffer before calling the processor. Default: Size.mebibytes(3)
        :param retries: (experimental) The number of times Kinesis Data Firehose will retry the processor invocation after a failure due to network timeout or invocation limits. Default: 3

        :stability: experimental
        '''
        props = DataProcessorProps(
            buffer_interval=buffer_interval, buffer_size=buffer_size, retries=retries
        )

        jsii.create(self.__class__, self, [lambda_function, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: constructs.Construct,
        *,
        role: aws_cdk.aws_iam.IRole,
    ) -> DataProcessorConfig:
        '''(experimental) Binds this processor to a destination of a delivery stream.

        Implementers should use this method to grant processor invocation permissions to the provided stream and return the
        necessary configuration to register as a processor.

        :param _scope: -
        :param role: (experimental) The IAM role assumed by Kinesis Data Firehose to write to the destination that this DataProcessor will bind to.

        :stability: experimental
        '''
        options = DataProcessorBindOptions(role=role)

        return typing.cast(DataProcessorConfig, jsii.invoke(self, "bind", [_scope, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="props")
    def props(self) -> DataProcessorProps:
        '''(experimental) The constructor props of the LambdaFunctionProcessor.

        :stability: experimental
        '''
        return typing.cast(DataProcessorProps, jsii.get(self, "props"))


@jsii.enum(jsii_type="@aws-cdk/aws-kinesisfirehose.StreamEncryption")
class StreamEncryption(enum.Enum):
    '''(experimental) Options for server-side encryption of a delivery stream.

    :stability: experimental
    '''

    UNENCRYPTED = "UNENCRYPTED"
    '''(experimental) Data in the stream is stored unencrypted.

    :stability: experimental
    '''
    CUSTOMER_MANAGED = "CUSTOMER_MANAGED"
    '''(experimental) Data in the stream is stored encrypted by a KMS key managed by the customer.

    :stability: experimental
    '''
    AWS_OWNED = "AWS_OWNED"
    '''(experimental) Data in the stream is stored encrypted by a KMS key owned by AWS and managed for use in multiple AWS accounts.

    :stability: experimental
    '''


@jsii.implements(IDeliveryStream)
class DeliveryStream(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-kinesisfirehose.DeliveryStream",
):
    '''(experimental) Create a Kinesis Data Firehose delivery stream.

    :stability: experimental
    :resource: AWS::KinesisFirehose::DeliveryStream
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        destinations: typing.Sequence[IDestination],
        delivery_stream_name: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[StreamEncryption] = None,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        source_stream: typing.Optional[aws_cdk.aws_kinesis.IStream] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param destinations: (experimental) The destinations that this delivery stream will deliver data to. Only a singleton array is supported at this time.
        :param delivery_stream_name: (experimental) A name for the delivery stream. Default: - a name is generated by CloudFormation.
        :param encryption: (experimental) Indicates the type of customer master key (CMK) to use for server-side encryption, if any. Default: StreamEncryption.UNENCRYPTED - unless ``encryptionKey`` is provided, in which case this will be implicitly set to ``StreamEncryption.CUSTOMER_MANAGED``
        :param encryption_key: (experimental) Customer managed key to server-side encrypt data in the stream. Default: - no KMS key will be used; if ``encryption`` is set to ``CUSTOMER_MANAGED``, a KMS key will be created for you
        :param role: (experimental) The IAM role associated with this delivery stream. Assumed by Kinesis Data Firehose to read from sources and encrypt data server-side. Default: - a role will be created with default permissions.
        :param source_stream: (experimental) The Kinesis data stream to use as a source for this delivery stream. Default: - data must be written to the delivery stream via a direct put.

        :stability: experimental
        '''
        props = DeliveryStreamProps(
            destinations=destinations,
            delivery_stream_name=delivery_stream_name,
            encryption=encryption,
            encryption_key=encryption_key,
            role=role,
            source_stream=source_stream,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDeliveryStreamArn") # type: ignore[misc]
    @builtins.classmethod
    def from_delivery_stream_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        delivery_stream_arn: builtins.str,
    ) -> IDeliveryStream:
        '''(experimental) Import an existing delivery stream from its ARN.

        :param scope: -
        :param id: -
        :param delivery_stream_arn: -

        :stability: experimental
        '''
        return typing.cast(IDeliveryStream, jsii.sinvoke(cls, "fromDeliveryStreamArn", [scope, id, delivery_stream_arn]))

    @jsii.member(jsii_name="fromDeliveryStreamAttributes") # type: ignore[misc]
    @builtins.classmethod
    def from_delivery_stream_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        delivery_stream_arn: typing.Optional[builtins.str] = None,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> IDeliveryStream:
        '''(experimental) Import an existing delivery stream from its attributes.

        :param scope: -
        :param id: -
        :param delivery_stream_arn: (experimental) The ARN of the delivery stream. At least one of deliveryStreamArn and deliveryStreamName must be provided. Default: - derived from ``deliveryStreamName``.
        :param delivery_stream_name: (experimental) The name of the delivery stream. At least one of deliveryStreamName and deliveryStreamArn must be provided. Default: - derived from ``deliveryStreamArn``.
        :param role: (experimental) The IAM role associated with this delivery stream. Assumed by Kinesis Data Firehose to read from sources and encrypt data server-side. Default: - the imported stream cannot be granted access to other resources as an ``iam.IGrantable``.

        :stability: experimental
        '''
        attrs = DeliveryStreamAttributes(
            delivery_stream_arn=delivery_stream_arn,
            delivery_stream_name=delivery_stream_name,
            role=role,
        )

        return typing.cast(IDeliveryStream, jsii.sinvoke(cls, "fromDeliveryStreamAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromDeliveryStreamName") # type: ignore[misc]
    @builtins.classmethod
    def from_delivery_stream_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        delivery_stream_name: builtins.str,
    ) -> IDeliveryStream:
        '''(experimental) Import an existing delivery stream from its name.

        :param scope: -
        :param id: -
        :param delivery_stream_name: -

        :stability: experimental
        '''
        return typing.cast(IDeliveryStream, jsii.sinvoke(cls, "fromDeliveryStreamName", [scope, id, delivery_stream_name]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
        *actions: builtins.str,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the ``grantee`` identity permissions to perform ``actions``.

        :param grantee: -
        :param actions: -

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantPutRecords")
    def grant_put_records(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the ``grantee`` identity permissions to perform ``firehose:PutRecord`` and ``firehose:PutRecordBatch`` actions on this delivery stream.

        :param grantee: -

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantPutRecords", [grantee]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric for this delivery stream.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [metric_name, props]))

    @jsii.member(jsii_name="metricBackupToS3Bytes")
    def metric_backup_to_s3_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of bytes delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricBackupToS3Bytes", [props]))

    @jsii.member(jsii_name="metricBackupToS3DataFreshness")
    def metric_backup_to_s3_data_freshness(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the age (from getting into Kinesis Data Firehose to now) of the oldest record in Kinesis Data Firehose.

        Any record older than this age has been delivered to the Amazon S3 bucket for backup.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricBackupToS3DataFreshness", [props]))

    @jsii.member(jsii_name="metricBackupToS3Records")
    def metric_backup_to_s3_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of records delivered to Amazon S3 for backup over the specified time period.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricBackupToS3Records", [props]))

    @jsii.member(jsii_name="metricIncomingBytes")
    def metric_incoming_bytes(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of bytes ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricIncomingBytes", [props]))

    @jsii.member(jsii_name="metricIncomingRecords")
    def metric_incoming_records(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.core.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Metric for the number of records ingested successfully into the delivery stream over the specified time period after throttling.

        By default, this metric will be calculated as an average over a period of 5 minutes.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions: (deprecated) Dimensions of the metric. Default: - No dimensions.
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions=dimensions,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricIncomingRecords", [props]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) Network connections between Kinesis Data Firehose and other resources, i.e. Redshift cluster.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deliveryStreamArn")
    def delivery_stream_arn(self) -> builtins.str:
        '''(experimental) The ARN of the delivery stream.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        '''(experimental) The name of the delivery stream.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) The principal to grant permissions to.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))


__all__ = [
    "CfnDeliveryStream",
    "CfnDeliveryStreamProps",
    "DataProcessorBindOptions",
    "DataProcessorConfig",
    "DataProcessorIdentifier",
    "DataProcessorProps",
    "DeliveryStream",
    "DeliveryStreamAttributes",
    "DeliveryStreamProps",
    "DestinationBindOptions",
    "DestinationConfig",
    "IDataProcessor",
    "IDeliveryStream",
    "IDestination",
    "LambdaFunctionProcessor",
    "StreamEncryption",
]

publication.publish()
