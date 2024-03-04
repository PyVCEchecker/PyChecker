'''
# CDK Construct Libray for AWS XXX

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

A short description here.
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

import aws_cdk.aws_kinesis
import aws_cdk.aws_lambda
import aws_cdk.aws_logs
import aws_cdk.core


@jsii.implements(aws_cdk.aws_logs.ILogSubscriptionDestination)
class KinesisDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-logs-destinations.KinesisDestination",
):
    '''Use a Kinesis stream as the destination for a log subscription.'''

    def __init__(self, stream: aws_cdk.aws_kinesis.IStream) -> None:
        '''
        :param stream: -
        '''
        jsii.create(self.__class__, self, [stream])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: aws_cdk.core.Construct,
        _source_log_group: aws_cdk.aws_logs.ILogGroup,
    ) -> aws_cdk.aws_logs.LogSubscriptionDestinationConfig:
        '''Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param _source_log_group: -
        '''
        return typing.cast(aws_cdk.aws_logs.LogSubscriptionDestinationConfig, jsii.invoke(self, "bind", [scope, _source_log_group]))


@jsii.implements(aws_cdk.aws_logs.ILogSubscriptionDestination)
class LambdaDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-logs-destinations.LambdaDestination",
):
    '''Use a Lambda Function as the destination for a log subscription.'''

    def __init__(
        self,
        fn: aws_cdk.aws_lambda.IFunction,
        *,
        add_permissions: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''LambdaDestinationOptions.

        :param fn: -
        :param add_permissions: Whether or not to add Lambda Permissions. Default: true
        '''
        options = LambdaDestinationOptions(add_permissions=add_permissions)

        jsii.create(self.__class__, self, [fn, options])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: aws_cdk.core.Construct,
        log_group: aws_cdk.aws_logs.ILogGroup,
    ) -> aws_cdk.aws_logs.LogSubscriptionDestinationConfig:
        '''Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param log_group: -
        '''
        return typing.cast(aws_cdk.aws_logs.LogSubscriptionDestinationConfig, jsii.invoke(self, "bind", [scope, log_group]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-logs-destinations.LambdaDestinationOptions",
    jsii_struct_bases=[],
    name_mapping={"add_permissions": "addPermissions"},
)
class LambdaDestinationOptions:
    def __init__(
        self,
        *,
        add_permissions: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options that may be provided to LambdaDestination.

        :param add_permissions: Whether or not to add Lambda Permissions. Default: true
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if add_permissions is not None:
            self._values["add_permissions"] = add_permissions

    @builtins.property
    def add_permissions(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to add Lambda Permissions.

        :default: true
        '''
        result = self._values.get("add_permissions")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDestinationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KinesisDestination",
    "LambdaDestination",
    "LambdaDestinationOptions",
]

publication.publish()
