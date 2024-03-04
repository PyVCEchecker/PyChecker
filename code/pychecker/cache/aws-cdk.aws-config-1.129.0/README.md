# AWS Config Construct Library

<!--BEGIN STABILITY BANNER-->---


Features                                                                               | Stability
---------------------------------------------------------------------------------------|------------
CFN Resources                                                                          | ![Stable](https://img.shields.io/badge/stable-success.svg?style=for-the-badge)
Higher level constructs for Config Rules                                               | ![Stable](https://img.shields.io/badge/stable-success.svg?style=for-the-badge)
Higher level constructs for initial set-up (delivery channel & configuration recorder) | ![Not Implemented](https://img.shields.io/badge/not--implemented-black.svg?style=for-the-badge)

> **CFN Resources:** All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always
> stable and safe to use.

<!-- -->

> **Stable:** Higher level constructs in this module that are marked stable will not undergo any
> breaking changes. They will strictly follow the [Semantic Versioning](https://semver.org/) model.

---
<!--END STABILITY BANNER-->

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the configuration of AWS resources in your AWS account.
This includes how the resources are related to one another and how they were configured in the
past so that you can see how the configurations and relationships change over time.

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Initial Setup

Before using the constructs provided in this module, you need to set up AWS Config
in the region in which it will be used. This setup includes the one-time creation of the
following resources per region:

* `ConfigurationRecorder`: Configure which resources will be recorded for config changes.
* `DeliveryChannel`: Configure where to store the recorded data.

The following guides provide the steps for getting started with AWS Config:

* [Using the AWS Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html)
* [Using the AWS CLI](https://docs.aws.amazon.com/config/latest/developerguide/gs-cli.html)

## Rules

AWS Config can evaluate the configuration settings of your AWS resources by creating AWS Config rules,
which represent your ideal configuration settings.

See [Evaluating Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) to learn more about AWS Config rules.

### AWS Managed Rules

AWS Config provides AWS managed rules, which are predefined, customizable rules that AWS Config
uses to evaluate whether your AWS resources comply with common best practices.

For example, you could create a managed rule that checks whether active access keys are rotated
within the number of days specified.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_config as config
import aws_cdk.core as cdk

# https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
config.ManagedRule(self, "AccessKeysRotated",
    identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
    input_parameters={
        "max_access_key_age": 60
    },
    maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
)
```

Identifiers for AWS managed rules are available through static constants in the `ManagedRuleIdentifiers` class.
You can find supported input parameters in the [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html).

The following higher level constructs for AWS managed rules are available.

#### Access Key rotation

Checks whether your active access keys are rotated within the number of days specified.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_config as config
import aws_cdk.aws_cdk as cdk

# compliant if access keys have been rotated within the last 90 days
config.AccessKeysRotated(self, "AccessKeyRotated")
```

#### CloudFormation Stack drift detection

Checks whether your CloudFormation stack's actual configuration differs, or has drifted,
from it's expected configuration.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_config as config
import aws_cdk.aws_cdk as cdk

# compliant if stack's status is 'IN_SYNC'
# non-compliant if the stack's drift status is 'DRIFTED'
config.CloudFormationStackDriftDetectionCheck(stack, "Drift",
    own_stack_only=True
)
```

#### CloudFormation Stack notifications

Checks whether your CloudFormation stacks are sending event notifications to a SNS topic.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_config as config
import aws_cdk.aws_cdk as cdk

# topics to which CloudFormation stacks may send event notifications
topic1 = sns.Topic(stack, "AllowedTopic1")
topic2 = sns.Topic(stack, "AllowedTopic2")

# non-compliant if CloudFormation stack does not send notifications to 'topic1' or 'topic2'
config.CloudFormationStackNotificationCheck(self, "NotificationCheck",
    topics=[topic1, topic2]
)
```

### Custom rules

You can develop custom rules and add them to AWS Config. You associate each custom rule with an
AWS Lambda function, which contains the logic that evaluates whether your AWS resources comply
with the rule.

### Triggers

AWS Lambda executes functions in response to events that are published by AWS Services.
The function for a custom Config rule receives an event that is published by AWS Config,
and is responsible for evaluating the compliance of the rule.

Evaluations can be triggered by configuration changes, periodically, or both.
To create a custom rule, define a `CustomRule` and specify the Lambda Function
to run and the trigger types.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_config as config

config.CustomRule(self, "CustomRule",
    lambda_function=eval_compliance_fn,
    configuration_changes=True,
    periodic=True,
    maximum_execution_frequency=config.MaximumExecutionFrequency.SIX_HOURS
)
```

When the trigger for a rule occurs, the Lambda function is invoked by publishing an event.
See [example events for AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_example-events.html)

The AWS documentation has examples of Lambda functions for evaluations that are
[triggered by configuration changes](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_nodejs-sample.html#event-based-example-rule) and [triggered periodically](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_nodejs-sample.html#periodic-example-rule)

### Scope

By default rules are triggered by changes to all [resources](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources).

Use the `RuleScope` APIs (`fromResource()`, `fromResources()` or `fromTag()`) to restrict
the scope of both managed and custom rules:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_config as config

ssh_rule = config.ManagedRule(self, "SSH",
    identifier=config.ManagedRuleIdentifiers.EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED,
    rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_SECURITY_GROUP, "sg-1234567890abcdefgh")
)

custom_rule = config.CustomRule(self, "Lambda",
    lambda_function=eval_compliance_fn,
    configuration_changes=True,
    rule_scope=config.RuleScope.from_resources([config.ResourceType.CLOUDFORMATION_STACK, config.ResourceType.S3_BUCKET])
)

tag_rule = config.CustomRule(self, "CostCenterTagRule",
    lambda_function=eval_compliance_fn,
    configuration_changes=True,
    rule_scope=config.RuleScope.from_tag("Cost Center", "MyApp")
)
```

### Events

You can define Amazon EventBridge event rules which trigger when a compliance check fails
or when a rule is re-evaluated.

Use the `onComplianceChange()` APIs to trigger an EventBridge event when a compliance check
of your AWS Config Rule fails:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_config as config
import aws_cdk.aws_sns as sns
import aws_cdk.aws_events_targets as targets

# Topic to which compliance notification events will be published
compliance_topic = sns.Topic(self, "ComplianceTopic")

rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")
rule.on_compliance_change("TopicEvent",
    target=targets.SnsTopic(compliance_topic)
)
```

Use the `onReEvaluationStatus()` status to trigger an EventBridge event when an AWS Config
rule is re-evaluated.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_config as config
import aws_cdk.aws_sns as sns
import aws_cdk.aws_events_targets as targets

# Topic to which re-evaluation notification events will be published
re_evaluation_topic = sns.Topic(self, "ComplianceTopic")
rule.on_re_evaluation_status("ReEvaluationEvent",
    target=targets.SnsTopic(re_evaluation_topic)
)
```

### Example

The following example creates a custom rule that evaluates whether EC2 instances are compliant.
Compliance events are published to an SNS topic.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_config as config
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_sns as sns
import aws_cdk.aws_events_targets as targets

# Lambda function containing logic that evaluates compliance with the rule.
eval_compliance_fn = lambda_.Function(self, "CustomFunction",
    code=lambda_.AssetCode.from_inline("exports.handler = (event) => console.log(event);"),
    handler="index.handler",
    runtime=lambda_.Runtime.NODEJS_12_X
)

# A custom rule that runs on configuration changes of EC2 instances
custom_rule = config.CustomRule(self, "Custom",
    configuration_changes=True,
    lambda_function=eval_compliance_fn,
    rule_scope=config.RuleScope.from_resource([config.ResourceType.EC2_INSTANCE])
)

# A rule to detect stack drifts
drift_rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")

# Topic to which compliance notification events will be published
compliance_topic = sns.Topic(self, "ComplianceTopic")

# Send notification on compliance change events
drift_rule.on_compliance_change("ComplianceChange",
    target=targets.SnsTopic(compliance_topic)
)
```
