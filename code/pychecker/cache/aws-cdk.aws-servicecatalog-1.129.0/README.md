# AWS Service Catalog Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

[AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/dg/what-is-service-catalog.html)
enables organizations to create and manage catalogs of products for their end users that are approved for use on AWS.

## Table Of Contents

* [Portfolio](#portfolio)

  * [Granting access to a portfolio](#granting-access-to-a-portfolio)
  * [Sharing a portfolio with another AWS account](#sharing-a-portfolio-with-another-aws-account)
* [Product](#product)

  * [Adding a product to a portfolio](#adding-a-product-to-a-portfolio)
* [TagOptions](#tag-options)
* [Constraints](#constraints)

  * [Tag update constraint](#tag-update-constraint)
  * [Notify on stack events](#notify-on-stack-events)
  * [CloudFormation parameters constraint](#cloudformation-parameters-constraint)
  * [Set launch role](#set-launch-role)
  * [Deploy with StackSets](#deploy-with-stacksets)

The `@aws-cdk/aws-servicecatalog` package contains resources that enable users to automate governance and management of their AWS resources at scale.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_servicecatalog as servicecatalog
```

## Portfolio

AWS Service Catalog portfolios allow admins to manage products that their end users have access to.
Using the CDK, a new portfolio can be created with the `Portfolio` construct:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
servicecatalog.Portfolio(self, "MyFirstPortfolio",
    display_name="MyFirstPortfolio",
    provider_name="MyTeam"
)
```

You can also specify properties such as `description` and `acceptLanguage`
to help better catalog and manage your portfolios.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
servicecatalog.Portfolio(self, "MyFirstPortfolio",
    display_name="MyFirstPortfolio",
    provider_name="MyTeam",
    description="Portfolio for a project",
    message_language=servicecatalog.MessageLanguage.EN
)
```

Read more at [Creating and Managing Portfolios](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios.html).

A portfolio that has been created outside the stack can be imported into your CDK app.
Portfolios can be imported by their ARN via the `Portfolio.fromPortfolioArn()` API:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
portfolio = servicecatalog.Portfolio.from_portfolio_arn(self, "MyImportedPortfolio", "arn:aws:catalog:region:account-id:portfolio/port-abcdefghi")
```

### Granting access to a portfolio

You can manage end user access to a portfolio by granting permissions to `IAM` entities like a user, group, or role.
Once resources are deployed end users will be able to access them via the console or service catalog CLI.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iam as iam


user = iam.User(self, "MyUser")
portfolio.give_access_to_user(user)

role = iam.Role(self, "MyRole",
    assumed_by=iam.AccountRootPrincipal()
)
portfolio.give_access_to_role(role)

group = iam.Group(self, "MyGroup")
portfolio.give_access_to_group(group)
```

### Sharing a portfolio with another AWS account

A portfolio can be programatically shared with other accounts so that specified users can also access it:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
portfolio.share_with_account("012345678901")
```

## Product

Products are the resources you are allowing end users to provision and utilize.
The CDK currently only supports adding products of type Cloudformation product.
Using the CDK, a new Product can be created with the `CloudFormationProduct` construct.
`CloudFormationTemplate.fromUrl` can be utilized to create a Product using a Cloudformation template directly from an URL:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
product = servicecatalog.CloudFormationProduct(self, "MyFirstProduct",
    product_name="My Product",
    owner="Product Owner",
    product_versions=[{
        "product_version_name": "v1",
        "cloud_formation_template": servicecatalog.CloudFormationTemplate.from_url("https://raw.githubusercontent.com/awslabs/aws-cloudformation-templates/master/aws/services/ServiceCatalog/Product.yaml")
    }
    ]
)
```

A `CloudFormationProduct` can also be created using a Cloudformation template from an Asset.
Assets are files that are uploaded to an S3 Bucket before deployment.
`CloudFormationTemplate.fromAsset` can be utilized to create a Product by passing the path to a local template file on your disk:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import path as path


product = servicecatalog.CloudFormationProduct(self, "MyFirstProduct",
    product_name="My Product",
    owner="Product Owner",
    product_versions=[{
        "product_version_name": "v1",
        "cloud_formation_template": servicecatalog.CloudFormationTemplate.from_url("https://raw.githubusercontent.com/awslabs/aws-cloudformation-templates/master/aws/services/ServiceCatalog/Product.yaml")
    }, {
        "product_version_name": "v2",
        "cloud_formation_template": servicecatalog.CloudFormationTemplate.from_asset(path.join(__dirname, "development-environment.template.json"))
    }
    ]
)
```

### Adding a product to a portfolio

You add products to a portfolio to manage your resources at scale.  After adding a product to a portfolio,
it creates a portfolio-product association, and will become visible from the portfolio side in both the console and service catalog CLI.
A product can be added to multiple portfolios depending on your resource and organizational needs.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
portfolio.add_product(product)
```

## Tag Options

TagOptions allow administrators to easily manage tags on provisioned products by creating a selection of tags for end users to choose from.
For example, an end user can choose an `ec2` for the instance type size.
TagOptions are created by specifying a key with a selection of values.
At the moment, TagOptions can only be disabled in the console.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
tag_options = servicecatalog.TagOptions({
    "ec2_instance_type": ["A1", "M4"],
    "ec2_instance_size": ["medium", "large"]
})
portfolio.associate_tag_options(tag_options)
```

## Constraints

Constraints define governance mechanisms that allow you to manage permissions, notifications, and options related to actions end users can perform on products,
Constraints are applied on a portfolio-product association.
Using the CDK, if you do not explicitly associate a product to a portfolio and add a constraint, it will automatically add an association for you.

There are rules around plurariliites of constraints for a portfolio and product.
For example, you can only have a single "tag update" constraint applied to a portfolio-product association.
If a misconfigured constraint is added, `synth` will fail with an error message.

Read more at [Service Catalog Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints.html).

### Tag update constraint

Tag update constraints allow or disallow end users to update tags on resources associated with an AWS Service Catalog product upon provisioning.
By default, tag updating is not permitted.
If tag updating is allowed, then new tags associated with the product or portfolio will be applied to provisioned resources during a provisioned product update.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
portfolio.add_product(product)

portfolio.constrain_tag_updates(product)
```

If you want to disable this feature later on, you can update it by setting the "allow" parameter to `false`:

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
# to disable tag updates:
portfolio.constrain_tag_updates(product,
    allow=False
)
```

### Notify on stack events

Allows users to subscribe an AWS `SNS` topic to the stack events of the product.
When an end user provisions a product it creates a product stack that notifies the subscribed topic on creation, edit, and delete events.
An individual `SNS` topic may only be subscribed once to a portfolio-product association.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_sns as sns


topic1 = sns.Topic(self, "MyTopic1")
portfolio.notify_on_stack_events(product, topic1)

topic2 = sns.Topic(self, "MyTopic2")
portfolio.notify_on_stack_events(product, topic2,
    description="description for this topic2"
)
```

### CloudFormation parameters constraint

CloudFormation parameters constraints allow you to configure the that are available to end users when they launch a product via defined rules.
A rule consists of one or more assertions that narrow the allowable values for parameters in a product.
You can configure multiple parameter constraints to govern the different parameters and parameter options in your products.
For example, a rule might define the various instance types that users can choose from when launching a stack that includes EC2 instances.
A parameter rule has an optional `condition` field that allows ability to configure when rules are applied.
If a `condition` is specified, all the assertions will be applied if the condition evalutates to true.
For information on rule-specific intrinsic functions to define rule conditions and assertions,
see [AWS Rule Functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-rules.html).

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.core as cdk


portfolio.constrain_cloud_formation_parameters(product,
    rule=TemplateRule(
        rule_name="testInstanceType",
        condition=cdk.Fn.condition_equals(cdk.Fn.ref("Environment"), "test"),
        assertions=[TemplateRuleAssertion(
            assert=cdk.Fn.condition_contains(["t2.micro", "t2.small"], cdk.Fn.ref("InstanceType")),
            description="For test environment, the instance type should be small"
        )]
    )
)
```

### Set launch role

Allows you to configure a specific AWS `IAM` role that a user must assume when launching a product.
By setting this launch role, you can control what policies and privileges end users can have.
The launch role must be assumed by the service catalog principal.
You can only have one launch role set for a portfolio-product association, and you cannot set a launch role if a StackSets deployment has been configured.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iam as iam


launch_role = iam.Role(self, "LaunchRole",
    assumed_by=iam.ServicePrincipal("servicecatalog.amazonaws.com")
)

portfolio.set_launch_role(product, launch_role)
```

See [Launch Constraint](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints-launch.html) documentation
to understand permissions roles need.

### Deploy with StackSets

A StackSets deployment constraint allows you to configure product deployment options using
[AWS CloudFormation StackSets](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/using-stacksets.html).
You can specify multiple accounts and regions for the product launch following StackSets conventions.
There is an additional field `allowStackSetInstanceOperations` that configures ability for end users to create, edit, or delete the stacks.
By default, this field is set to `false`.
End users can manage those accounts and determine where products deploy and the order of deployment.
You can only define one StackSets deployment configuration per portfolio-product association,
and you cannot both set a launch role and StackSets deployment configuration for an assocation.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_iam as iam


admin_role = iam.Role(self, "AdminRole",
    assumed_by=iam.AccountRootPrincipal()
)

portfolio.deploy_with_stack_sets(product,
    accounts=["012345678901", "012345678902", "012345678903"],
    regions=["us-west-1", "us-east-1", "us-west-2", "us-east-1"],
    admin_role=admin_role,
    execution_role_name="SCStackSetExecutionRole",  # Name of role deployed in end users accounts.
    allow_stack_set_instance_operations=True
)
```
