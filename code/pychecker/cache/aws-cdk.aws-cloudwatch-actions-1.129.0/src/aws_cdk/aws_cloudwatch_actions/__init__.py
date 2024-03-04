'''
# CloudWatch Alarm Actions library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This library contains a set of classes which can be used as CloudWatch Alarm actions.

The currently implemented actions are: EC2 Actions, SNS Actions, Autoscaling Actions and Aplication Autoscaling Actions

## EC2 Action Example

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_cloudwatch as cw
# Alarm must be configured with an EC2 per-instance metric
# alarm is of type Alarm
# Attach a reboot when alarm triggers
alarm.add_alarm_action(
    Ec2Action(Ec2InstanceActions.REBOOT))
```

See `@aws-cdk/aws-cloudwatch` for more information.
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

import aws_cdk.aws_applicationautoscaling
import aws_cdk.aws_autoscaling
import aws_cdk.aws_cloudwatch
import aws_cdk.aws_sns
import aws_cdk.core


@jsii.implements(aws_cdk.aws_cloudwatch.IAlarmAction)
class ApplicationScalingAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudwatch-actions.ApplicationScalingAction",
):
    '''Use an ApplicationAutoScaling StepScalingAction as an Alarm Action.'''

    def __init__(
        self,
        step_scaling_action: aws_cdk.aws_applicationautoscaling.StepScalingAction,
    ) -> None:
        '''
        :param step_scaling_action: -
        '''
        jsii.create(self.__class__, self, [step_scaling_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: aws_cdk.core.Construct,
        _alarm: aws_cdk.aws_cloudwatch.IAlarm,
    ) -> aws_cdk.aws_cloudwatch.AlarmActionConfig:
        '''Returns an alarm action configuration to use an ApplicationScaling StepScalingAction as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        return typing.cast(aws_cdk.aws_cloudwatch.AlarmActionConfig, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.implements(aws_cdk.aws_cloudwatch.IAlarmAction)
class AutoScalingAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudwatch-actions.AutoScalingAction",
):
    '''Use an AutoScaling StepScalingAction as an Alarm Action.'''

    def __init__(
        self,
        step_scaling_action: aws_cdk.aws_autoscaling.StepScalingAction,
    ) -> None:
        '''
        :param step_scaling_action: -
        '''
        jsii.create(self.__class__, self, [step_scaling_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: aws_cdk.core.Construct,
        _alarm: aws_cdk.aws_cloudwatch.IAlarm,
    ) -> aws_cdk.aws_cloudwatch.AlarmActionConfig:
        '''Returns an alarm action configuration to use an AutoScaling StepScalingAction as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        return typing.cast(aws_cdk.aws_cloudwatch.AlarmActionConfig, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.implements(aws_cdk.aws_cloudwatch.IAlarmAction)
class Ec2Action(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudwatch-actions.Ec2Action",
):
    '''Use an EC2 action as an Alarm action.'''

    def __init__(self, instance_action: "Ec2InstanceAction") -> None:
        '''
        :param instance_action: -
        '''
        jsii.create(self.__class__, self, [instance_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: aws_cdk.core.Construct,
        _alarm: aws_cdk.aws_cloudwatch.IAlarm,
    ) -> aws_cdk.aws_cloudwatch.AlarmActionConfig:
        '''Returns an alarm action configuration to use an EC2 action as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        return typing.cast(aws_cdk.aws_cloudwatch.AlarmActionConfig, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.enum(jsii_type="@aws-cdk/aws-cloudwatch-actions.Ec2InstanceAction")
class Ec2InstanceAction(enum.Enum):
    '''Types of EC2 actions available.'''

    STOP = "STOP"
    '''Stop the instance.'''
    TERMINATE = "TERMINATE"
    '''Terminatethe instance.'''
    RECOVER = "RECOVER"
    '''Recover the instance.'''
    REBOOT = "REBOOT"
    '''Reboot the instance.'''


@jsii.implements(aws_cdk.aws_cloudwatch.IAlarmAction)
class SnsAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudwatch-actions.SnsAction",
):
    '''Use an SNS topic as an alarm action.'''

    def __init__(self, topic: aws_cdk.aws_sns.ITopic) -> None:
        '''
        :param topic: -
        '''
        jsii.create(self.__class__, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: aws_cdk.core.Construct,
        _alarm: aws_cdk.aws_cloudwatch.IAlarm,
    ) -> aws_cdk.aws_cloudwatch.AlarmActionConfig:
        '''Returns an alarm action configuration to use an SNS topic as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        return typing.cast(aws_cdk.aws_cloudwatch.AlarmActionConfig, jsii.invoke(self, "bind", [_scope, _alarm]))


__all__ = [
    "ApplicationScalingAction",
    "AutoScalingAction",
    "Ec2Action",
    "Ec2InstanceAction",
    "SnsAction",
]

publication.publish()
