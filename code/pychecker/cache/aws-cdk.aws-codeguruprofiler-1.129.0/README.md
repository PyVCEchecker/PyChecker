# AWS::CodeGuruProfiler Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

Amazon CodeGuru Profiler collects runtime performance data from your live applications, and provides recommendations that can help you fine-tune your application performance.

## Installation

Import to your project:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_codeguruprofiler as codeguruprofiler
```

## Basic usage

Here's how to setup a profiling group and give your compute role permissions to publish to the profiling group to the profiling agent can publish profiling information:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# The execution role of your application that publishes to the ProfilingGroup via CodeGuru Profiler Profiling Agent. (the following is merely an example)
publish_app_role = Role(stack, "PublishAppRole",
    assumed_by=AccountRootPrincipal()
)

profiling_group = ProfilingGroup(stack, "MyProfilingGroup")
profiling_group.grant_publish(publish_app_role)
```

## Compute Platform configuration

Code Guru Profiler supports multiple compute environments.
They can be configured when creating a Profiling Group by using the `computePlatform` property:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
profiling_group = ProfilingGroup(stack, "MyProfilingGroup",
    compute_platform=ComputePlatform.AWS_LAMBDA
)
```
