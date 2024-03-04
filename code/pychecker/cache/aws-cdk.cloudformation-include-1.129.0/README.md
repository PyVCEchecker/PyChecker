# Include CloudFormation templates in the CDK

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This module contains a set of classes whose goal is to facilitate working
with existing CloudFormation templates in the CDK.
It can be thought of as an extension of the capabilities of the
[`CfnInclude` class](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_core.CfnInclude.html).

## Basic usage

Assume we have a file with an existing template.
It could be in JSON format, in a file `my-template.json`:

```json
{
  "Resources": {
    "Bucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "some-bucket-name"
      }
    }
  }
}
```

Or it could by in YAML format, in a file `my-template.yaml`:

```yaml
Resources:
  Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: some-bucket-name
```

It can be included in a CDK application with the following code:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.cloudformation_include as cfn_inc

cfn_template = cfn_inc.CfnInclude(self, "Template",
    template_file="my-template.json"
)
```

Or, if your template uses YAML:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cfn_template = cfn_inc.CfnInclude(self, "Template",
    template_file="my-template.yaml"
)
```

**Note**: different YAML parsers sometimes don't agree on what exactly constitutes valid YAML.
If you get a YAML exception when including your template,
try converting it to JSON, and including that file instead.
If you're downloading your template from the CloudFormation AWS Console,
you can easily get it in JSON format by clicking the 'View in Designer'
button on the 'Template' tab -
once in Designer, select JSON in the "Choose template language"
radio buttons on the bottom pane.

This will add all resources from `my-template.json` / `my-template.yaml` into the CDK application,
preserving their original logical IDs from the template file.

Note that this including process will *not* execute any
[CloudFormation transforms](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html) -
including the [Serverless transform](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html).

Any resource from the included template can be retrieved by referring to it by its logical ID from the template.
If you know the class of the CDK object that corresponds to that resource,
you can cast the returned object to the correct type:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_s3 as s3

cfn_bucket = cfn_template.get_resource("Bucket")
```

Note that any resources not present in the latest version of the CloudFormation schema
at the time of publishing the version of this module that you depend on,
including [Custom Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html),
will be returned as instances of the class `CfnResource`,
and so cannot be cast to a different resource type.

Any modifications made to that resource will be reflected in the resulting CDK template;
for example, the name of the bucket can be changed:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cfn_bucket.bucket_name = "my-bucket-name"
```

You can also refer to the resource when defining other constructs,
including the higher-level ones
(those whose name does not start with `Cfn`),
for example:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iam as iam

role = iam.Role(self, "Role",
    assumed_by=iam.AnyPrincipal()
)
role.add_to_policy(iam.PolicyStatement(
    actions=["s3:*"],
    resources=[cfn_bucket.attr_arn]
))
```

### Converting L1 resources to L2

The resources the `getResource` method returns are what the CDK calls
[Layer 1 resources](https://docs.aws.amazon.com/cdk/latest/guide/cfn_layer.html#cfn_layer_cfn)
(like `CfnBucket`).
However, in many places in the Construct Library,
the CDK requires so-called Layer 2 resources, like `IBucket`.
There are two ways of going from an L1 to an L2 resource.

#### Using`fromCfn*()` methods

This is the preferred method of converting an L1 resource to an L2.
It works by invoking a static method of the class of the L2 resource
whose name starts with `fromCfn` -
for example, for KMS Keys, that would be the `Kms.fromCfnKey()` method -
and passing the L1 instance as an argument:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_kms as kms

cfn_key = cfn_template.get_resource("Key")
key = kms.Key.from_cfn_key(cfn_key)
```

This returns an instance of the `kms.IKey` type that can be passed anywhere in the CDK an `IKey` is expected.
What is more, that `IKey` instance will be mutable -
which means calling any mutating methods on it,
like `addToResourcePolicy()`,
will be reflected in the resulting template.

Note that, in some cases, the `fromCfn*()` method might not be able to create an L2 from the underlying L1.
This can happen when the underlying L1 heavily uses CloudFormation functions.
For example, if you tried to create an L2 `IKey`
from an L1 represented as this CloudFormation template:

```json
{
  "Resources": {
    "Key": {
      "Type": "AWS::KMS::Key",
      "Properties": {
        "KeyPolicy": {
          "Statement": [
            {
              "Fn::If": [
                "Condition",
                {
                  "Action": "kms:if-action",
                  "Resource": "*",
                  "Principal": "*",
                  "Effect": "Allow"
                },
                {
                  "Action": "kms:else-action",
                  "Resource": "*",
                  "Principal": "*",
                  "Effect": "Allow"
                }
              ]
            }
          ],
          "Version": "2012-10-17"
        }
      }
    }
  }
}
```

The `Key.fromCfnKey()` method does not know how to translate that into CDK L2 concepts,
and would throw an exception.

In those cases, you need the use the second method of converting an L1 to an L2.

#### Using `from*Name/Arn/Attributes()` methods

If the resource you need does not have a `fromCfn*()` method,
or if it does, but it throws an exception for your particular L1,
you need to use the second method of converting an L1 resource to L2.

Each L2 class has static factory methods with names like `from*Name()`,
`from*Arn()`, and/or `from*Attributes()`.
You can obtain an L2 resource from an L1 by passing the correct properties of the L1 as the arguments to those methods:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# using from*Name()
bucket = s3.Bucket.from_bucket_name(self, "L2Bucket", cfn_bucket.ref)

# using from*Arn()
key = kms.Key.from_key_arn(self, "L2Key", cfn_key.attr_arn)

# using from*Attributes()
vpc = ec2.Vpc.from_vpc_attributes(self, "L2Vpc",
    vpc_id=cfn_vpc.ref,
    availability_zones=cdk.Fn.get_azs(),
    private_subnet_ids=[private_cfn_subnet1.ref, private_cfn_subnet2.ref]
)
```

As long as they just need to be referenced,
and not changed in any way, everything should work;
however, note that resources returned from those methods,
unlike those returned by `fromCfn*()` methods,
are immutable, which means calling any mutating methods on them will have no effect.
You will have to mutate the underlying L1 in order to change them.

## Non-resource template elements

In addition to resources,
you can also retrieve and mutate all other template elements:

* [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html):

  ```python
  # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
  import aws_cdk.core as core

  param = cfn_template.get_parameter("MyParameter")

  # mutating the parameter
  param.default = "MyDefault"
  ```
* [Conditions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/conditions-section-structure.html):

  ```python
  # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
  import aws_cdk.core as core

  condition = cfn_template.get_condition("MyCondition")

  # mutating the condition
  condition.expression = core.Fn.condition_equals(1, 2)
  ```
* [Mappings](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html):

  ```python
  # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
  import aws_cdk.core as core

  mapping = cfn_template.get_mapping("MyMapping")

  # mutating the mapping
  mapping.set_value("my-region", "AMI", "ami-04681a1dbd79675a5")
  ```
* [Service Catalog template Rules](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/reference-template_constraint_rules.html):

  ```python
  # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
  import aws_cdk.core as core

  rule = cfn_template.get_rule("MyRule")

  # mutating the rule
  rule.add_assertion(core.Fn.condition_contains(["m1.small"], my_parameter.value), "MyParameter has to be m1.small")
  ```
* [Outputs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html):

  ```python
  # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
  import aws_cdk.core as core

  output = cfn_template.get_output("MyOutput")

  # mutating the output
  output.value = cfn_bucket.attr_arn
  ```
* [Hooks for blue-green deployments](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html):

  ```python
  # Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
  import aws_cdk.core as core

  hook = cfn_template.get_hook("MyOutput")

  # mutating the hook
  code_deploy_hook = hook
  code_deploy_hook.service_role = my_role.role_arn
  ```

## Parameter replacement

If your existing template uses CloudFormation Parameters,
you may want to remove them in favor of build-time values.
You can do that using the `parameters` property:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
inc.CfnInclude(self, "includeTemplate",
    template_file="path/to/my/template",
    parameters={
        "MyParam": "my-value"
    }
)
```

This will replace all references to `MyParam` with the string `'my-value'`,
and `MyParam` will be removed from the 'Parameters' section of the resulting template.

## Nested Stacks

This module also supports templates that use [nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html).

For example, if you have the following parent template:

```json
{
  "Resources": {
    "ChildStack": {
      "Type": "AWS::CloudFormation::Stack",
      "Properties": {
        "TemplateURL": "https://my-s3-template-source.s3.amazonaws.com/child-stack.json"
      }
    }
  }
}
```

where the child template pointed to by `https://my-s3-template-source.s3.amazonaws.com/child-stack.json` is:

```json
{
  "Resources": {
    "MyBucket": {
      "Type": "AWS::S3::Bucket"
    }
  }
}
```

You can include both the parent stack,
and the nested stack in your CDK application as follows:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
parent_template = inc.CfnInclude(self, "ParentStack",
    template_file="path/to/my-parent-template.json",
    load_nested_stacks={
        "ChildStack": {
            "template_file": "path/to/my-nested-template.json"
        }
    }
)
```

Here, `path/to/my-nested-template.json`
represents the path on disk to the downloaded template file from the original template URL of the nested stack
(`https://my-s3-template-source.s3.amazonaws.com/child-stack.json`).
In the CDK application,
this file will be turned into an [Asset](https://docs.aws.amazon.com/cdk/latest/guide/assets.html),
and the `TemplateURL` property of the nested stack resource
will be modified to point to that asset.

The included nested stack can be accessed with the `getNestedStack` method:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
included_child_stack = parent_template.get_nested_stack("ChildStack")
child_stack = included_child_stack.stack
child_template = included_child_stack.included_template
```

Now you can reference resources from `ChildStack`,
and modify them like any other included template:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cfn_bucket = child_template.get_resource("MyBucket")
cfn_bucket.bucket_name = "my-new-bucket-name"

role = iam.Role(child_stack, "MyRole",
    assumed_by=iam.AccountRootPrincipal()
)

role.add_to_policy(iam.PolicyStatement(
    actions=["s3:GetObject*", "s3:GetBucket*", "s3:List*"
    ],
    resources=[cfn_bucket.attr_arn]
))
```

You can also include the nested stack after the `CfnInclude` object was created,
instead of doing it on construction:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
included_child_stack = parent_template.load_nested_stack("ChildTemplate",
    template_file="path/to/my-nested-template.json"
)
```

## Vending CloudFormation templates as Constructs

In many cases, there are existing CloudFormation templates that are not entire applications,
but more like specialized fragments, implementing a particular pattern or best practice.
If you have templates like that,
you can use the `CfnInclude` class to vend them as CDK Constructs:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import path as path


class MyConstruct(Construct):
    def __init__(self, scope, id):
        super().__init__(scope, id)

        # include a template inside the Construct
        cfn_inc.CfnInclude(self, "MyConstruct",
            template_file=path.join(__dirname, "my-template.json"),
            preserve_logical_ids=False
        )
```

Notice the `preserveLogicalIds` parameter -
it makes sure the logical IDs of all the included template elements are re-named using CDK's algorithm,
guaranteeing they are unique within your application.
Without that parameter passed,
instantiating `MyConstruct` twice in the same Stack would result in duplicated logical IDs.
