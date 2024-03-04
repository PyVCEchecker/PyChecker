'''
# Amazon Lambda Destinations Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This library provides constructs for adding destinations to a Lambda function.
Destinations can be added by specifying the `onFailure` or `onSuccess` props when creating a function or alias.

## Destinations

The following destinations are supported

* Lambda function
* SQS queue
* SNS topic
* EventBridge event bus

Example with a SNS topic for successful invocations:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_lambda_destinations as destinations
import aws_cdk.aws_sns as sns

my_topic = sns.Topic(self, "Topic")

my_fn = lambda_.Function(self, "Fn",
    # other props
    on_success=destinations.SnsDestination(my_topic)
)
```

See also [Configuring Destinations for Asynchronous Invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations).

### Invocation record

When a lambda function is configured with a destination, an invocation record is created by the Lambda service
when the lambda function completes. The invocation record contains the details of the function, its context, and
the request and response payloads.

The following example shows the format of the invocation record for a successful invocation:

```json
{
	"version": "1.0",
	"timestamp": "2019-11-24T23:08:25.651Z",
	"requestContext": {
		"requestId": "c2a6f2ae-7dbb-4d22-8782-d0485c9877e2",
		"functionArn": "arn:aws:lambda:sa-east-1:123456789123:function:event-destinations:$LATEST",
		"condition": "Success",
		"approximateInvokeCount": 1
	},
	"requestPayload": {
		"Success": true
	},
	"responseContext": {
		"statusCode": 200,
		"executedVersion": "$LATEST"
	},
	"responsePayload": "<data returned by the function here>"
}
```

In case of failure, the record contains the reason and error object:

```json
{
    "version": "1.0",
    "timestamp": "2019-11-24T21:52:47.333Z",
    "requestContext": {
        "requestId": "8ea123e4-1db7-4aca-ad10-d9ca1234c1fd",
        "functionArn": "arn:aws:lambda:sa-east-1:123456678912:function:event-destinations:$LATEST",
        "condition": "RetriesExhausted",
        "approximateInvokeCount": 3
    },
    "requestPayload": {
        "Success": false
    },
    "responseContext": {
        "statusCode": 200,
        "executedVersion": "$LATEST",
        "functionError": "Handled"
    },
    "responsePayload": {
        "errorMessage": "Failure from event, Success = false, I am failing!",
        "errorType": "Error",
        "stackTrace": [ "exports.handler (/var/task/index.js:18:18)" ]
    }
}
```

#### Destination-specific JSON format

* For SNS/SQS (`SnsDestionation`/`SqsDestination`), the invocation record JSON is passed as the `Message` to the destination.
* For Lambda (`LambdaDestination`), the invocation record JSON is passed as the payload to the function.
* For EventBridge (`EventBridgeDestination`), the invocation record JSON is passed as the `detail` in the PutEvents call.
  The value for the event field `source` is `lambda`, and the value for the event field `detail-type`
  is either 'Lambda Function Invocation Result - Success' or 'Lambda Function Invocation Result – Failure',
  depending on whether the lambda function invocation succeeded or failed. The event field `resource`
  contains the function and destination ARNs. See [AWS Events](https://docs.aws.amazon.com/eventbridge/latest/userguide/aws-events.html)
  for the different event fields.

### Auto-extract response payload with lambda destination

The `responseOnly` option of `LambdaDestination` allows to auto-extract the response payload from the
invocation record:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_lambda_destinations as destinations

destination_fn = lambda_.Function(self, "Destination")

source_fn = lambda_.Function(self, "Source",
    # other props
    on_success=destinations.LambdaDestination(destination_fn,
        response_only=True
    )
)
```

In the above example, `destinationFn` will be invoked with the payload returned by `sourceFn`
(`responsePayload` in the invocation record, not the full record).

When used with `onFailure`, the destination function is invoked with the error object returned
by the source function.

Using the `responseOnly` option allows to easily chain asynchronous Lambda functions without
having to deal with data extraction in the runtime code.
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
import aws_cdk.aws_lambda
import aws_cdk.aws_sns
import aws_cdk.aws_sqs
import aws_cdk.core


@jsii.implements(aws_cdk.aws_lambda.IDestination)
class EventBridgeDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lambda-destinations.EventBridgeDestination",
):
    '''Use an Event Bridge event bus as a Lambda destination.

    If no event bus is specified, the default event bus is used.
    '''

    def __init__(
        self,
        event_bus: typing.Optional[aws_cdk.aws_events.IEventBus] = None,
    ) -> None:
        '''
        :param event_bus: -

        :default: - use the default event bus
        '''
        jsii.create(self.__class__, self, [event_bus])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: aws_cdk.core.Construct,
        fn: aws_cdk.aws_lambda.IFunction,
        *,
        type: aws_cdk.aws_lambda.DestinationType,
    ) -> aws_cdk.aws_lambda.DestinationConfig:
        '''Returns a destination configuration.

        :param _scope: -
        :param fn: -
        :param type: The destination type.
        '''
        _options = aws_cdk.aws_lambda.DestinationOptions(type=type)

        return typing.cast(aws_cdk.aws_lambda.DestinationConfig, jsii.invoke(self, "bind", [_scope, fn, _options]))


@jsii.implements(aws_cdk.aws_lambda.IDestination)
class LambdaDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lambda-destinations.LambdaDestination",
):
    '''Use a Lambda function as a Lambda destination.'''

    def __init__(
        self,
        fn: aws_cdk.aws_lambda.IFunction,
        *,
        response_only: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param fn: -
        :param response_only: Whether the destination function receives only the ``responsePayload`` of the source function. When set to ``true`` and used as ``onSuccess`` destination, the destination function will be invoked with the payload returned by the source function. When set to ``true`` and used as ``onFailure`` destination, the destination function will be invoked with the error object returned by source function. See the README of this module to see a full explanation of this option. Default: false The destination function receives the full invocation record.
        '''
        options = LambdaDestinationOptions(response_only=response_only)

        jsii.create(self.__class__, self, [fn, options])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: aws_cdk.core.Construct,
        fn: aws_cdk.aws_lambda.IFunction,
        *,
        type: aws_cdk.aws_lambda.DestinationType,
    ) -> aws_cdk.aws_lambda.DestinationConfig:
        '''Returns a destination configuration.

        :param scope: -
        :param fn: -
        :param type: The destination type.
        '''
        options = aws_cdk.aws_lambda.DestinationOptions(type=type)

        return typing.cast(aws_cdk.aws_lambda.DestinationConfig, jsii.invoke(self, "bind", [scope, fn, options]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-lambda-destinations.LambdaDestinationOptions",
    jsii_struct_bases=[],
    name_mapping={"response_only": "responseOnly"},
)
class LambdaDestinationOptions:
    def __init__(self, *, response_only: typing.Optional[builtins.bool] = None) -> None:
        '''Options for a Lambda destination.

        :param response_only: Whether the destination function receives only the ``responsePayload`` of the source function. When set to ``true`` and used as ``onSuccess`` destination, the destination function will be invoked with the payload returned by the source function. When set to ``true`` and used as ``onFailure`` destination, the destination function will be invoked with the error object returned by source function. See the README of this module to see a full explanation of this option. Default: false The destination function receives the full invocation record.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if response_only is not None:
            self._values["response_only"] = response_only

    @builtins.property
    def response_only(self) -> typing.Optional[builtins.bool]:
        '''Whether the destination function receives only the ``responsePayload`` of the source function.

        When set to ``true`` and used as ``onSuccess`` destination, the destination
        function will be invoked with the payload returned by the source function.

        When set to ``true`` and used as ``onFailure`` destination, the destination
        function will be invoked with the error object returned by source function.

        See the README of this module to see a full explanation of this option.

        :default: false The destination function receives the full invocation record.
        '''
        result = self._values.get("response_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDestinationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_lambda.IDestination)
class SnsDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lambda-destinations.SnsDestination",
):
    '''Use a SNS topic as a Lambda destination.'''

    def __init__(self, topic: aws_cdk.aws_sns.ITopic) -> None:
        '''
        :param topic: -
        '''
        jsii.create(self.__class__, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: aws_cdk.core.Construct,
        fn: aws_cdk.aws_lambda.IFunction,
        *,
        type: aws_cdk.aws_lambda.DestinationType,
    ) -> aws_cdk.aws_lambda.DestinationConfig:
        '''Returns a destination configuration.

        :param _scope: -
        :param fn: -
        :param type: The destination type.
        '''
        _options = aws_cdk.aws_lambda.DestinationOptions(type=type)

        return typing.cast(aws_cdk.aws_lambda.DestinationConfig, jsii.invoke(self, "bind", [_scope, fn, _options]))


@jsii.implements(aws_cdk.aws_lambda.IDestination)
class SqsDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-lambda-destinations.SqsDestination",
):
    '''Use a SQS queue as a Lambda destination.'''

    def __init__(self, queue: aws_cdk.aws_sqs.IQueue) -> None:
        '''
        :param queue: -
        '''
        jsii.create(self.__class__, self, [queue])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: aws_cdk.core.Construct,
        fn: aws_cdk.aws_lambda.IFunction,
        *,
        type: aws_cdk.aws_lambda.DestinationType,
    ) -> aws_cdk.aws_lambda.DestinationConfig:
        '''Returns a destination configuration.

        :param _scope: -
        :param fn: -
        :param type: The destination type.
        '''
        _options = aws_cdk.aws_lambda.DestinationOptions(type=type)

        return typing.cast(aws_cdk.aws_lambda.DestinationConfig, jsii.invoke(self, "bind", [_scope, fn, _options]))


__all__ = [
    "EventBridgeDestination",
    "LambdaDestination",
    "LambdaDestinationOptions",
    "SnsDestination",
    "SqsDestination",
]

publication.publish()
