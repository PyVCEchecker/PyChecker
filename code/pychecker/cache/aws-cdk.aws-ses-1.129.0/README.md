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
