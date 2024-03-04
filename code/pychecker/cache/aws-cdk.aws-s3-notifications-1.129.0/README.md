# S3 Bucket Notifications Destinations

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This module includes integration classes for using Topics, Queues or Lambdas
as S3 Notification Destinations.

## Example

The following example shows how to send a notification to an SNS
topic when an object is created in an S3 bucket:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_s3_notifications as s3n

bucket = s3.Bucket(stack, "Bucket")
topic = sns.Topic(stack, "Topic")

bucket.add_event_notification(s3.EventType.OBJECT_CREATED_PUT, s3n.SnsDestination(topic))
```
