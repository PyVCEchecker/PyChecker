# Continuous Integration / Continuous Delivery for CDK Applications

<!--BEGIN STABILITY BANNER-->---


![Deprecated](https://img.shields.io/badge/deprecated-critical.svg?style=for-the-badge)

> This API may emit warnings. Backward compatibility is not guaranteed.

---
<!--END STABILITY BANNER-->

This library includes a *CodePipeline* composite Action for deploying AWS CDK Applications.

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Replacement recommended

This library has been deprecated. We recommend you use the
[@aws-cdk/pipelines](https://docs.aws.amazon.com/cdk/api/latest/docs/pipelines-readme.html) module instead.

## Limitations

The construct library in it's current form has the following limitations:

1. It can only deploy stacks that are hosted in the same AWS account and region as the *CodePipeline* is.
2. Stacks that make use of `Asset`s cannot be deployed successfully.

## Getting Started

In order to add the `PipelineDeployStackAction` to your *CodePipeline*, you need to have a *CodePipeline* artifact that
contains the result of invoking `cdk synth -o <dir>` on your *CDK App*. You can for example achieve this using a
*CodeBuild* project.

The example below defines a *CDK App* that contains 3 stacks:

* `CodePipelineStack` manages the *CodePipeline* resources, and self-updates before deploying any other stack
* `ServiceStackA` and `ServiceStackB` are service infrastructure stacks, and need to be deployed in this order

```plaintext
  ┏━━━━━━━━━━━━━━━━┓  ┏━━━━━━━━━━━━━━━━┓  ┏━━━━━━━━━━━━━━━━━┓  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  ┃     Source     ┃  ┃     Build      ┃  ┃  Self-Update    ┃  ┃             Deploy              ┃
  ┃                ┃  ┃                ┃  ┃                 ┃  ┃                                 ┃
  ┃ ┌────────────┐ ┃  ┃ ┌────────────┐ ┃  ┃ ┌─────────────┐ ┃  ┃ ┌─────────────┐ ┌─────────────┐ ┃
  ┃ │   GitHub   ┣━╋━━╋━▶ CodeBuild  ┣━╋━━╋━▶Deploy Stack ┣━╋━━╋━▶Deploy Stack ┣━▶Deploy Stack │ ┃
  ┃ │            │ ┃  ┃ │            │ ┃  ┃ │PipelineStack│ ┃  ┃ │ServiceStackA│ │ServiceStackB│ ┃
  ┃ └────────────┘ ┃  ┃ └────────────┘ ┃  ┃ └─────────────┘ ┃  ┃ └─────────────┘ └─────────────┘ ┃
  ┗━━━━━━━━━━━━━━━━┛  ┗━━━━━━━━━━━━━━━━┛  ┗━━━━━━━━━━━━━━━━━┛  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

### `index.ts`

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_codebuild as codebuild
import aws_cdk.aws_codepipeline as codepipeline
import aws_cdk.aws_codepipeline_actions as codepipeline_actions
import aws_cdk.core as cdk
import aws_cdk.app_delivery as cicd

app = cdk.App()

# We define a stack that contains the CodePipeline
pipeline_stack = cdk.Stack(app, "PipelineStack")
pipeline = codepipeline.Pipeline(pipeline_stack, "CodePipeline",
    # Mutating a CodePipeline can cause the currently propagating state to be
    # "lost". Ensure we re-run the latest change through the pipeline after it's
    # been mutated so we're sure the latest state is fully deployed through.
    restart_execution_on_update=True
)

# Configure the CodePipeline source - where your CDK App's source code is hosted
source_output = codepipeline.Artifact()
source = codepipeline_actions.GitHubSourceAction(
    action_name="GitHub",
    output=source_output
)
pipeline.add_stage(
    stage_name="source",
    actions=[source]
)

project = codebuild.PipelineProject(pipeline_stack, "CodeBuild")
synthesized_app = codepipeline.Artifact()
build_action = codepipeline_actions.CodeBuildAction(
    action_name="CodeBuild",
    project=project,
    input=source_output,
    outputs=[synthesized_app]
)
pipeline.add_stage(
    stage_name="build",
    actions=[build_action]
)

# Optionally, self-update the pipeline stack
self_update_stage = pipeline.add_stage(stage_name="SelfUpdate")
self_update_stage.add_action(cicd.PipelineDeployStackAction(
    stack=pipeline_stack,
    input=synthesized_app,
    admin_permissions=True
))

# Now add our service stacks
deploy_stage = pipeline.add_stage(stage_name="Deploy")
service_stack_a = MyServiceStackA(app, "ServiceStackA")
# Add actions to deploy the stacks in the deploy stage:
deploy_service_aAction = cicd.PipelineDeployStackAction(
    stack=service_stack_a,
    input=synthesized_app,
    # See the note below for details about this option.
    admin_permissions=False
)
deploy_stage.add_action(deploy_service_aAction)
# Add the necessary permissions for you service deploy action. This role is
# is passed to CloudFormation and needs the permissions necessary to deploy
# stack. Alternatively you can enable [Administrator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#jf_administrator) permissions above,
# users should understand the privileged nature of this role.
deploy_service_aAction.add_to_role_policy(iam.PolicyStatement(
    actions=["service:SomeAction"],
    resources=[my_resource.my_resource_arn]
))

service_stack_b = MyServiceStackB(app, "ServiceStackB")
deploy_stage.add_action(cicd.PipelineDeployStackAction(
    stack=service_stack_b,
    input=synthesized_app,
    create_change_set_run_order=998,
    admin_permissions=True
))
```

### `buildspec.yml`

The repository can contain a file at the root level named `buildspec.yml`, or
you can in-line the buildspec. Note that `buildspec.yaml` is not compatible.

For example, a *TypeScript* or *Javascript* CDK App can add the following `buildspec.yml`
at the root of the repository:

```yml
version: 0.2
phases:
  install:
    commands:
      # Installs the npm dependencies as defined by the `package.json` file
      # present in the root directory of the package
      # (`cdk init app --language=typescript` would have created one for you)
      - npm install
  build:
    commands:
      # Builds the CDK App so it can be synthesized
      - npm run build
      # Synthesizes the CDK App and puts the resulting artifacts into `dist`
      - npm run cdk synth -- -o dist
artifacts:
  # The output artifact is all the files in the `dist` directory
  base-directory: dist
  files: '**/*'
```

The `PipelineDeployStackAction` expects it's `input` to contain the result of
synthesizing a CDK App using the `cdk synth -o <directory>`.
