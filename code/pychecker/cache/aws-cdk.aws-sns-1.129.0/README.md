# Amazon Simple Notification Service Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

Add an SNS Topic to your stack:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_sns as sns

topic = sns.Topic(self, "Topic",
    display_name="Customer subscription topic"
)
```

Add a FIFO SNS topic with content-based de-duplication to your stack:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_sns as sns

topic = sns.Topic(self, "Topic",
    content_based_deduplication=True,
    display_name="Customer subscription topic",
    fifo=True,
    topic_name="customerTopic"
)
```

Note that FIFO topics require a topic name to be provided. The required `.fifo` suffix will be automatically added to the topic name if it is not explicitly provided.

## Subscriptions

Various subscriptions can be added to the topic by calling the
`.addSubscription(...)` method on the topic. It accepts a *subscription* object,
default implementations of which can be found in the
`@aws-cdk/aws-sns-subscriptions` package:

Add an HTTPS Subscription to your topic:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_sns_subscriptions as subs

my_topic = sns.Topic(self, "MyTopic")

my_topic.add_subscription(subs.UrlSubscription("https://foobar.com/"))
```

Subscribe a queue to the topic:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
my_topic.add_subscription(subs.SqsSubscription(queue))
```

Note that subscriptions of queues in different accounts need to be manually confirmed by
reading the initial message from the queue and visiting the link found in it.

### Filter policy

A filter policy can be specified when subscribing an endpoint to a topic.

Example with a Lambda subscription:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
my_topic = sns.Topic(self, "MyTopic")
fn = lambda_.Function(self, "Function", ...)

# Lambda should receive only message matching the following conditions on attributes:
# color: 'red' or 'orange' or begins with 'bl'
# size: anything but 'small' or 'medium'
# price: between 100 and 200 or greater than 300
# store: attribute must be present
topic.add_subscription(subs.LambdaSubscription(fn,
    filter_policy={
        "color": sns.SubscriptionFilter.string_filter(
            allowlist=["red", "orange"],
            match_prefixes=["bl"]
        ),
        "size": sns.SubscriptionFilter.string_filter(
            denylist=["small", "medium"]
        ),
        "price": sns.SubscriptionFilter.numeric_filter(
            between=BetweenCondition(start=100, stop=200),
            greater_than=300
        ),
        "store": sns.SubscriptionFilter.exists_filter()
    }
))
```

### Example of Firehose Subscription

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from aws_cdk.aws_sns import Subscription, SubscriptionProtocol, Topic
from aws_cdk.aws_kinesisfirehose import DeliveryStream
topic = Topic(stack, "Topic")
stream = DeliveryStream(stack, "DeliveryStream", ...)
Subscription(stack, "Subscription",
    endpoint=stream.delivery_stream_arn,
    protocol=SubscriptionProtocol.FIREHOSE,
    subscription_role_arn="SAMPLE_ARN"
)
```

## DLQ setup for SNS Subscription

CDK can attach provided Queue as DLQ for your SNS subscription.
See the [SNS DLQ configuration docs](https://docs.aws.amazon.com/sns/latest/dg/sns-configure-dead-letter-queue.html) for more information about this feature.

Example of usage with user provided DLQ.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
topic = sns.Topic(stack, "Topic")
dl_queue = Queue(stack, "DeadLetterQueue",
    queue_name="MySubscription_DLQ",
    retention_period=cdk.Duration.days(14)
)

sns.Subscription(stack, "Subscription",
    endpoint="endpoint",
    protocol=sns.SubscriptionProtocol.LAMBDA,
    topic=topic,
    dead_letter_queue=dl_queue
)
```

## CloudWatch Event Rule Target

SNS topics can be used as targets for CloudWatch event rules.

Use the `@aws-cdk/aws-events-targets.SnsTopic`:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_events_targets as targets

code_commit_repository.on_commit(targets.SnsTopic(my_topic))
```

This will result in adding a target to the event rule and will also modify the
topic resource policy to allow CloudWatch events to publish to the topic.

## Topic Policy

A topic policy is automatically created when `addToResourcePolicy` is called, if
one doesn't already exist. Using `addToResourcePolicy` is the simplest way to
add policies, but a `TopicPolicy` can also be created manually.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
topic = sns.Topic(stack, "Topic")
topic_policy = sns.TopicPolicy(stack, "TopicPolicy",
    topics=[topic]
)

topic_policy.document.add_statements(iam.PolicyStatement(
    actions=["sns:Subscribe"],
    principals=[iam.AnyPrincipal()],
    resources=[topic.topic_arn]
))
```

A policy document can also be passed on `TopicPolicy` construction

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
topic = sns.Topic(stack, "Topic")
policy_document = iam.PolicyDocument(
    assign_sids=True,
    statements=[
        iam.PolicyStatement(
            actions=["sns:Subscribe"],
            principals=[iam.AnyPrincipal()],
            resources=[topic.topic_arn]
        )
    ]
)

topic_policy = sns.TopicPolicy(self, "Policy",
    topics=[topic],
    policy_document=policy_document
)
```
