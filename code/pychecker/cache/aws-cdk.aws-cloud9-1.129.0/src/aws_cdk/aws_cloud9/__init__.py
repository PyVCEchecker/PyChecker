'''
# AWS Cloud9 Construct Library

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

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

AWS Cloud9 is a cloud-based integrated development environment (IDE) that lets you write, run, and debug your code with just a browser. It includes a code editor, debugger, and terminal. Cloud9 comes prepackaged with essential tools for popular programming languages, including JavaScript, Python, PHP, and more, so you don’t need to install files or configure your development machine to start new projects. Since your Cloud9 IDE is cloud-based, you can work on your projects from your office, home, or anywhere using an internet-connected machine. Cloud9 also provides a seamless experience for developing serverless applications enabling you to easily define resources, debug, and switch between local and remote execution of serverless applications. With Cloud9, you can quickly share your development environment with your team, enabling you to pair program and track each other's inputs in real time.

## Creating EC2 Environment

EC2 Environments are defined with `Ec2Environment`. To create an EC2 environment in the private subnet, specify `subnetSelection` with private `subnetType`.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_cloud9 as cloud9

# create a cloud9 ec2 environment in a new VPC
vpc = ec2.Vpc(self, "VPC", max_azs=3)
cloud9.Ec2Environment(self, "Cloud9Env", vpc=vpc)

# or create the cloud9 environment in the default VPC with specific instanceType
default_vpc = ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True)
cloud9.Ec2Environment(self, "Cloud9Env2",
    vpc=default_vpc,
    instance_type=ec2.InstanceType("t3.large")
)

# or specify in a different subnetSelection
c9env = cloud9.Ec2Environment(self, "Cloud9Env3",
    vpc=vpc,
    subnet_selection=SubnetSelection(
        subnet_type=ec2.SubnetType.PRIVATE
    )
)

# print the Cloud9 IDE URL in the output
cdk.CfnOutput(self, "URL", value=c9env.ide_url)
```

## Cloning Repositories

Use `clonedRepositories` to clone one or multiple AWS Codecommit repositories into the environment:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# create a codecommit repository to clone into the cloud9 environment
repo_new = codecommit.Repository(self, "RepoNew",
    repository_name="new-repo"
)

# import an existing codecommit repository to clone into the cloud9 environment
repo_existing = codecommit.Repository.from_repository_name(stack, "RepoExisting", "existing-repo")

# create a new Cloud9 environment and clone the two repositories
cloud9.Ec2Environment(stack, "C9Env",
    vpc=vpc,
    cloned_repositories=[
        cloud9.CloneRepository.from_code_commit(repo_new, "/src/new-repo"),
        cloud9.CloneRepository.from_code_commit(repo_existing, "/src/existing-repo")
    ]
)
```
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

import aws_cdk.aws_codecommit
import aws_cdk.aws_ec2
import aws_cdk.core
import constructs


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEnvironmentEC2(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloud9.CfnEnvironmentEC2",
):
    '''A CloudFormation ``AWS::Cloud9::EnvironmentEC2``.

    :cloudformationResource: AWS::Cloud9::EnvironmentEC2
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_type: builtins.str,
        automatic_stop_time_minutes: typing.Optional[jsii.Number] = None,
        connection_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_arn: typing.Optional[builtins.str] = None,
        repositories: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnEnvironmentEC2.RepositoryProperty", aws_cdk.core.IResolvable]]]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Cloud9::EnvironmentEC2``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_type: ``AWS::Cloud9::EnvironmentEC2.InstanceType``.
        :param automatic_stop_time_minutes: ``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.
        :param connection_type: ``AWS::Cloud9::EnvironmentEC2.ConnectionType``.
        :param description: ``AWS::Cloud9::EnvironmentEC2.Description``.
        :param image_id: ``AWS::Cloud9::EnvironmentEC2.ImageId``.
        :param name: ``AWS::Cloud9::EnvironmentEC2.Name``.
        :param owner_arn: ``AWS::Cloud9::EnvironmentEC2.OwnerArn``.
        :param repositories: ``AWS::Cloud9::EnvironmentEC2.Repositories``.
        :param subnet_id: ``AWS::Cloud9::EnvironmentEC2.SubnetId``.
        :param tags: ``AWS::Cloud9::EnvironmentEC2.Tags``.
        '''
        props = CfnEnvironmentEC2Props(
            instance_type=instance_type,
            automatic_stop_time_minutes=automatic_stop_time_minutes,
            connection_type=connection_type,
            description=description,
            image_id=image_id,
            name=name,
            owner_arn=owner_arn,
            repositories=repositories,
            subnet_id=subnet_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Cloud9::EnvironmentEC2.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''``AWS::Cloud9::EnvironmentEC2.InstanceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-instancetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        jsii.set(self, "instanceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="automaticStopTimeMinutes")
    def automatic_stop_time_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-automaticstoptimeminutes
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "automaticStopTimeMinutes"))

    @automatic_stop_time_minutes.setter
    def automatic_stop_time_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "automaticStopTimeMinutes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="connectionType")
    def connection_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.ConnectionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-connectiontype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionType"))

    @connection_type.setter
    def connection_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "connectionType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.ImageId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-imageid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageId"))

    @image_id.setter
    def image_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "imageId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ownerArn")
    def owner_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.OwnerArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-ownerarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerArn"))

    @owner_arn.setter
    def owner_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ownerArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositories")
    def repositories(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnEnvironmentEC2.RepositoryProperty", aws_cdk.core.IResolvable]]]]:
        '''``AWS::Cloud9::EnvironmentEC2.Repositories``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-repositories
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnEnvironmentEC2.RepositoryProperty", aws_cdk.core.IResolvable]]]], jsii.get(self, "repositories"))

    @repositories.setter
    def repositories(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnEnvironmentEC2.RepositoryProperty", aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "repositories", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-subnetid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subnetId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-cloud9.CfnEnvironmentEC2.RepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "path_component": "pathComponent",
            "repository_url": "repositoryUrl",
        },
    )
    class RepositoryProperty:
        def __init__(
            self,
            *,
            path_component: builtins.str,
            repository_url: builtins.str,
        ) -> None:
            '''
            :param path_component: ``CfnEnvironmentEC2.RepositoryProperty.PathComponent``.
            :param repository_url: ``CfnEnvironmentEC2.RepositoryProperty.RepositoryUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "path_component": path_component,
                "repository_url": repository_url,
            }

        @builtins.property
        def path_component(self) -> builtins.str:
            '''``CfnEnvironmentEC2.RepositoryProperty.PathComponent``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html#cfn-cloud9-environmentec2-repository-pathcomponent
            '''
            result = self._values.get("path_component")
            assert result is not None, "Required property 'path_component' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def repository_url(self) -> builtins.str:
            '''``CfnEnvironmentEC2.RepositoryProperty.RepositoryUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html#cfn-cloud9-environmentec2-repository-repositoryurl
            '''
            result = self._values.get("repository_url")
            assert result is not None, "Required property 'repository_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloud9.CfnEnvironmentEC2Props",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "automatic_stop_time_minutes": "automaticStopTimeMinutes",
        "connection_type": "connectionType",
        "description": "description",
        "image_id": "imageId",
        "name": "name",
        "owner_arn": "ownerArn",
        "repositories": "repositories",
        "subnet_id": "subnetId",
        "tags": "tags",
    },
)
class CfnEnvironmentEC2Props:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        automatic_stop_time_minutes: typing.Optional[jsii.Number] = None,
        connection_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        image_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        owner_arn: typing.Optional[builtins.str] = None,
        repositories: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnEnvironmentEC2.RepositoryProperty, aws_cdk.core.IResolvable]]]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Cloud9::EnvironmentEC2``.

        :param instance_type: ``AWS::Cloud9::EnvironmentEC2.InstanceType``.
        :param automatic_stop_time_minutes: ``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.
        :param connection_type: ``AWS::Cloud9::EnvironmentEC2.ConnectionType``.
        :param description: ``AWS::Cloud9::EnvironmentEC2.Description``.
        :param image_id: ``AWS::Cloud9::EnvironmentEC2.ImageId``.
        :param name: ``AWS::Cloud9::EnvironmentEC2.Name``.
        :param owner_arn: ``AWS::Cloud9::EnvironmentEC2.OwnerArn``.
        :param repositories: ``AWS::Cloud9::EnvironmentEC2.Repositories``.
        :param subnet_id: ``AWS::Cloud9::EnvironmentEC2.SubnetId``.
        :param tags: ``AWS::Cloud9::EnvironmentEC2.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
        }
        if automatic_stop_time_minutes is not None:
            self._values["automatic_stop_time_minutes"] = automatic_stop_time_minutes
        if connection_type is not None:
            self._values["connection_type"] = connection_type
        if description is not None:
            self._values["description"] = description
        if image_id is not None:
            self._values["image_id"] = image_id
        if name is not None:
            self._values["name"] = name
        if owner_arn is not None:
            self._values["owner_arn"] = owner_arn
        if repositories is not None:
            self._values["repositories"] = repositories
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''``AWS::Cloud9::EnvironmentEC2.InstanceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def automatic_stop_time_minutes(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-automaticstoptimeminutes
        '''
        result = self._values.get("automatic_stop_time_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.ConnectionType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-connectiontype
        '''
        result = self._values.get("connection_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.ImageId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-imageid
        '''
        result = self._values.get("image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.OwnerArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-ownerarn
        '''
        result = self._values.get("owner_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repositories(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnEnvironmentEC2.RepositoryProperty, aws_cdk.core.IResolvable]]]]:
        '''``AWS::Cloud9::EnvironmentEC2.Repositories``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-repositories
        '''
        result = self._values.get("repositories")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnEnvironmentEC2.RepositoryProperty, aws_cdk.core.IResolvable]]]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Cloud9::EnvironmentEC2.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-subnetid
        '''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Cloud9::EnvironmentEC2.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentEC2Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloneRepository(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloud9.CloneRepository",
):
    '''(experimental) The class for different repository providers.

    :stability: experimental
    '''

    @jsii.member(jsii_name="fromCodeCommit") # type: ignore[misc]
    @builtins.classmethod
    def from_code_commit(
        cls,
        repository: aws_cdk.aws_codecommit.IRepository,
        path: builtins.str,
    ) -> "CloneRepository":
        '''(experimental) import repository to cloud9 environment from AWS CodeCommit.

        :param repository: the codecommit repository to clone from.
        :param path: the target path in cloud9 environment.

        :stability: experimental
        '''
        return typing.cast("CloneRepository", jsii.sinvoke(cls, "fromCodeCommit", [repository, path]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="pathComponent")
    def path_component(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "pathComponent"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryUrl")
    def repository_url(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryUrl"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloud9.Ec2EnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "vpc": "vpc",
        "cloned_repositories": "clonedRepositories",
        "description": "description",
        "ec2_environment_name": "ec2EnvironmentName",
        "instance_type": "instanceType",
        "subnet_selection": "subnetSelection",
    },
)
class Ec2EnvironmentProps:
    def __init__(
        self,
        *,
        vpc: aws_cdk.aws_ec2.IVpc,
        cloned_repositories: typing.Optional[typing.Sequence[CloneRepository]] = None,
        description: typing.Optional[builtins.str] = None,
        ec2_environment_name: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        subnet_selection: typing.Optional[aws_cdk.aws_ec2.SubnetSelection] = None,
    ) -> None:
        '''(experimental) Properties for Ec2Environment.

        :param vpc: (experimental) The VPC that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.
        :param cloned_repositories: (experimental) The AWS CodeCommit repository to be cloned. Default: - do not clone any repository
        :param description: (experimental) Description of the environment. Default: - no description
        :param ec2_environment_name: (experimental) Name of the environment. Default: - automatically generated name
        :param instance_type: (experimental) The type of instance to connect to the environment. Default: - t2.micro
        :param subnet_selection: (experimental) The subnetSelection of the VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance. Default: - all public subnets of the VPC are selected.

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        self._values: typing.Dict[str, typing.Any] = {
            "vpc": vpc,
        }
        if cloned_repositories is not None:
            self._values["cloned_repositories"] = cloned_repositories
        if description is not None:
            self._values["description"] = description
        if ec2_environment_name is not None:
            self._values["ec2_environment_name"] = ec2_environment_name
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(experimental) The VPC that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(aws_cdk.aws_ec2.IVpc, result)

    @builtins.property
    def cloned_repositories(self) -> typing.Optional[typing.List[CloneRepository]]:
        '''(experimental) The AWS CodeCommit repository to be cloned.

        :default: - do not clone any repository

        :stability: experimental
        '''
        result = self._values.get("cloned_repositories")
        return typing.cast(typing.Optional[typing.List[CloneRepository]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description of the environment.

        :default: - no description

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_environment_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Name of the environment.

        :default: - automatically generated name

        :stability: experimental
        '''
        result = self._values.get("ec2_environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[aws_cdk.aws_ec2.InstanceType]:
        '''(experimental) The type of instance to connect to the environment.

        :default: - t2.micro

        :stability: experimental
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.InstanceType], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) The subnetSelection of the VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance.

        :default: - all public subnets of the VPC are selected.

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2EnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-cloud9.IEc2Environment")
class IEc2Environment(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''(experimental) A Cloud9 Environment.

    :stability: experimental
    '''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2EnvironmentArn")
    def ec2_environment_arn(self) -> builtins.str:
        '''(experimental) The arn of the EnvironmentEc2.

        :stability: experimental
        :attribute: environmentE2Arn
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2EnvironmentName")
    def ec2_environment_name(self) -> builtins.str:
        '''(experimental) The name of the EnvironmentEc2.

        :stability: experimental
        :attribute: environmentEc2Name
        '''
        ...


class _IEc2EnvironmentProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''(experimental) A Cloud9 Environment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-cloud9.IEc2Environment"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2EnvironmentArn")
    def ec2_environment_arn(self) -> builtins.str:
        '''(experimental) The arn of the EnvironmentEc2.

        :stability: experimental
        :attribute: environmentE2Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "ec2EnvironmentArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2EnvironmentName")
    def ec2_environment_name(self) -> builtins.str:
        '''(experimental) The name of the EnvironmentEc2.

        :stability: experimental
        :attribute: environmentEc2Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "ec2EnvironmentName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEc2Environment).__jsii_proxy_class__ = lambda : _IEc2EnvironmentProxy


@jsii.implements(IEc2Environment)
class Ec2Environment(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloud9.Ec2Environment",
):
    '''(experimental) A Cloud9 Environment with Amazon EC2.

    :stability: experimental
    :resource: AWS::Cloud9::EnvironmentEC2
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        vpc: aws_cdk.aws_ec2.IVpc,
        cloned_repositories: typing.Optional[typing.Sequence[CloneRepository]] = None,
        description: typing.Optional[builtins.str] = None,
        ec2_environment_name: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        subnet_selection: typing.Optional[aws_cdk.aws_ec2.SubnetSelection] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param vpc: (experimental) The VPC that AWS Cloud9 will use to communicate with the Amazon Elastic Compute Cloud (Amazon EC2) instance.
        :param cloned_repositories: (experimental) The AWS CodeCommit repository to be cloned. Default: - do not clone any repository
        :param description: (experimental) Description of the environment. Default: - no description
        :param ec2_environment_name: (experimental) Name of the environment. Default: - automatically generated name
        :param instance_type: (experimental) The type of instance to connect to the environment. Default: - t2.micro
        :param subnet_selection: (experimental) The subnetSelection of the VPC that AWS Cloud9 will use to communicate with the Amazon EC2 instance. Default: - all public subnets of the VPC are selected.

        :stability: experimental
        '''
        props = Ec2EnvironmentProps(
            vpc=vpc,
            cloned_repositories=cloned_repositories,
            description=description,
            ec2_environment_name=ec2_environment_name,
            instance_type=instance_type,
            subnet_selection=subnet_selection,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEc2EnvironmentName") # type: ignore[misc]
    @builtins.classmethod
    def from_ec2_environment_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        ec2_environment_name: builtins.str,
    ) -> IEc2Environment:
        '''(experimental) import from EnvironmentEc2Name.

        :param scope: -
        :param id: -
        :param ec2_environment_name: -

        :stability: experimental
        '''
        return typing.cast(IEc2Environment, jsii.sinvoke(cls, "fromEc2EnvironmentName", [scope, id, ec2_environment_name]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2EnvironmentArn")
    def ec2_environment_arn(self) -> builtins.str:
        '''(experimental) The environment ARN of this Cloud9 environment.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "ec2EnvironmentArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ec2EnvironmentName")
    def ec2_environment_name(self) -> builtins.str:
        '''(experimental) The environment name of this Cloud9 environment.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "ec2EnvironmentName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environmentId")
    def environment_id(self) -> builtins.str:
        '''(experimental) The environment ID of this Cloud9 environment.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "environmentId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ideUrl")
    def ide_url(self) -> builtins.str:
        '''(experimental) The complete IDE URL of this Cloud9 environment.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "ideUrl"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(experimental) VPC ID.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.IVpc, jsii.get(self, "vpc"))


__all__ = [
    "CfnEnvironmentEC2",
    "CfnEnvironmentEC2Props",
    "CloneRepository",
    "Ec2Environment",
    "Ec2EnvironmentProps",
    "IEc2Environment",
]

publication.publish()
