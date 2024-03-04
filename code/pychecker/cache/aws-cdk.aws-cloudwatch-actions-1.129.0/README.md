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
