'''
# AWS CodeCommit Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

AWS CodeCommit is a version control service that enables you to privately store and manage Git repositories in the AWS cloud.

For further information on CodeCommit,
see the [AWS CodeCommit documentation](https://docs.aws.amazon.com/codecommit).

To add a CodeCommit Repository to your stack:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_codecommit as codecommit

repo = codecommit.Repository(self, "Repository",
    repository_name="MyRepositoryName",
    description="Some description."
)
```

Use the `repositoryCloneUrlHttp`, `repositoryCloneUrlSsh` or `repositoryCloneUrlGrc`
property to clone your repository.

To add an Amazon SNS trigger to your repository:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# trigger is established for all repository actions on all branches by default.
repo.notify("arn:aws:sns:*:123456789012:my_topic")
```

## Events

CodeCommit repositories emit Amazon CloudWatch events for certain activities.
Use the `repo.onXxx` methods to define rules that trigger on these events
and invoke targets as a result:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
# starts a CodeBuild project when a commit is pushed to the "master" branch of the repo
repo.on_commit("CommitToMaster",
    target=targets.CodeBuildProject(project),
    branches=["master"]
)

# publishes a message to an Amazon SNS topic when a comment is made on a pull request
rule = repo.on_comment_on_pull_request("CommentOnPullRequest",
    target=targets.SnsTopic(my_topic)
)
```

## CodeStar Notifications

To define CodeStar Notification rules for Repositories, use one of the `notifyOnXxx()` methods.
They are very similar to `onXxx()` methods for CloudWatch events:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
target = chatbot.SlackChannelConfiguration(stack, "MySlackChannel",
    slack_channel_configuration_name="YOUR_CHANNEL_NAME",
    slack_workspace_id="YOUR_SLACK_WORKSPACE_ID",
    slack_channel_id="YOUR_SLACK_CHANNEL_ID"
)
rule = repository.notify_on_pull_request_created("NotifyOnPullRequestCreated", target)
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

import aws_cdk.aws_codestarnotifications
import aws_cdk.aws_events
import aws_cdk.aws_iam
import aws_cdk.core
import constructs


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRepository(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-codecommit.CfnRepository",
):
    '''A CloudFormation ``AWS::CodeCommit::Repository``.

    :cloudformationResource: AWS::CodeCommit::Repository
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        repository_name: builtins.str,
        code: typing.Optional[typing.Union["CfnRepository.CodeProperty", aws_cdk.core.IResolvable]] = None,
        repository_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        triggers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRepository.RepositoryTriggerProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::CodeCommit::Repository``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param repository_name: ``AWS::CodeCommit::Repository.RepositoryName``.
        :param code: ``AWS::CodeCommit::Repository.Code``.
        :param repository_description: ``AWS::CodeCommit::Repository.RepositoryDescription``.
        :param tags: ``AWS::CodeCommit::Repository.Tags``.
        :param triggers: ``AWS::CodeCommit::Repository.Triggers``.
        '''
        props = CfnRepositoryProps(
            repository_name=repository_name,
            code=code,
            repository_description=repository_description,
            tags=tags,
            triggers=triggers,
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
    @jsii.member(jsii_name="attrCloneUrlHttp")
    def attr_clone_url_http(self) -> builtins.str:
        '''
        :cloudformationAttribute: CloneUrlHttp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloneUrlHttp"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrCloneUrlSsh")
    def attr_clone_url_ssh(self) -> builtins.str:
        '''
        :cloudformationAttribute: CloneUrlSsh
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCloneUrlSsh"))

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
        '''``AWS::CodeCommit::Repository.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''``AWS::CodeCommit::Repository.RepositoryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-repositoryname
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

    @repository_name.setter
    def repository_name(self, value: builtins.str) -> None:
        jsii.set(self, "repositoryName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="code")
    def code(
        self,
    ) -> typing.Optional[typing.Union["CfnRepository.CodeProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::CodeCommit::Repository.Code``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-code
        '''
        return typing.cast(typing.Optional[typing.Union["CfnRepository.CodeProperty", aws_cdk.core.IResolvable]], jsii.get(self, "code"))

    @code.setter
    def code(
        self,
        value: typing.Optional[typing.Union["CfnRepository.CodeProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "code", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryDescription")
    def repository_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CodeCommit::Repository.RepositoryDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-repositorydescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryDescription"))

    @repository_description.setter
    def repository_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "repositoryDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="triggers")
    def triggers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRepository.RepositoryTriggerProperty"]]]]:
        '''``AWS::CodeCommit::Repository.Triggers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-triggers
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRepository.RepositoryTriggerProperty"]]]], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRepository.RepositoryTriggerProperty"]]]],
    ) -> None:
        jsii.set(self, "triggers", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-codecommit.CfnRepository.CodeProperty",
        jsii_struct_bases=[],
        name_mapping={"s3": "s3", "branch_name": "branchName"},
    )
    class CodeProperty:
        def __init__(
            self,
            *,
            s3: typing.Union[aws_cdk.core.IResolvable, "CfnRepository.S3Property"],
            branch_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param s3: ``CfnRepository.CodeProperty.S3``.
            :param branch_name: ``CfnRepository.CodeProperty.BranchName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3": s3,
            }
            if branch_name is not None:
                self._values["branch_name"] = branch_name

        @builtins.property
        def s3(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRepository.S3Property"]:
            '''``CfnRepository.CodeProperty.S3``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html#cfn-codecommit-repository-code-s3
            '''
            result = self._values.get("s3")
            assert result is not None, "Required property 's3' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRepository.S3Property"], result)

        @builtins.property
        def branch_name(self) -> typing.Optional[builtins.str]:
            '''``CfnRepository.CodeProperty.BranchName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.html#cfn-codecommit-repository-code-branchname
            '''
            result = self._values.get("branch_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-codecommit.CfnRepository.RepositoryTriggerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_arn": "destinationArn",
            "events": "events",
            "name": "name",
            "branches": "branches",
            "custom_data": "customData",
        },
    )
    class RepositoryTriggerProperty:
        def __init__(
            self,
            *,
            destination_arn: builtins.str,
            events: typing.Sequence[builtins.str],
            name: builtins.str,
            branches: typing.Optional[typing.Sequence[builtins.str]] = None,
            custom_data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param destination_arn: ``CfnRepository.RepositoryTriggerProperty.DestinationArn``.
            :param events: ``CfnRepository.RepositoryTriggerProperty.Events``.
            :param name: ``CfnRepository.RepositoryTriggerProperty.Name``.
            :param branches: ``CfnRepository.RepositoryTriggerProperty.Branches``.
            :param custom_data: ``CfnRepository.RepositoryTriggerProperty.CustomData``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "destination_arn": destination_arn,
                "events": events,
                "name": name,
            }
            if branches is not None:
                self._values["branches"] = branches
            if custom_data is not None:
                self._values["custom_data"] = custom_data

        @builtins.property
        def destination_arn(self) -> builtins.str:
            '''``CfnRepository.RepositoryTriggerProperty.DestinationArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-destinationarn
            '''
            result = self._values.get("destination_arn")
            assert result is not None, "Required property 'destination_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def events(self) -> typing.List[builtins.str]:
            '''``CfnRepository.RepositoryTriggerProperty.Events``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-events
            '''
            result = self._values.get("events")
            assert result is not None, "Required property 'events' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnRepository.RepositoryTriggerProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def branches(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRepository.RepositoryTriggerProperty.Branches``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-branches
            '''
            result = self._values.get("branches")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def custom_data(self) -> typing.Optional[builtins.str]:
            '''``CfnRepository.RepositoryTriggerProperty.CustomData``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-repositorytrigger.html#cfn-codecommit-repository-repositorytrigger-customdata
            '''
            result = self._values.get("custom_data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RepositoryTriggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-codecommit.CfnRepository.S3Property",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "key": "key",
            "object_version": "objectVersion",
        },
    )
    class S3Property:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket: ``CfnRepository.S3Property.Bucket``.
            :param key: ``CfnRepository.S3Property.Key``.
            :param object_version: ``CfnRepository.S3Property.ObjectVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }
            if object_version is not None:
                self._values["object_version"] = object_version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''``CfnRepository.S3Property.Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html#cfn-codecommit-repository-s3-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnRepository.S3Property.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html#cfn-codecommit-repository-s3-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version(self) -> typing.Optional[builtins.str]:
            '''``CfnRepository.S3Property.ObjectVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-s3.html#cfn-codecommit-repository-s3-objectversion
            '''
            result = self._values.get("object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-codecommit.CfnRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "repository_name": "repositoryName",
        "code": "code",
        "repository_description": "repositoryDescription",
        "tags": "tags",
        "triggers": "triggers",
    },
)
class CfnRepositoryProps:
    def __init__(
        self,
        *,
        repository_name: builtins.str,
        code: typing.Optional[typing.Union[CfnRepository.CodeProperty, aws_cdk.core.IResolvable]] = None,
        repository_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        triggers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnRepository.RepositoryTriggerProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::CodeCommit::Repository``.

        :param repository_name: ``AWS::CodeCommit::Repository.RepositoryName``.
        :param code: ``AWS::CodeCommit::Repository.Code``.
        :param repository_description: ``AWS::CodeCommit::Repository.RepositoryDescription``.
        :param tags: ``AWS::CodeCommit::Repository.Tags``.
        :param triggers: ``AWS::CodeCommit::Repository.Triggers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "repository_name": repository_name,
        }
        if code is not None:
            self._values["code"] = code
        if repository_description is not None:
            self._values["repository_description"] = repository_description
        if tags is not None:
            self._values["tags"] = tags
        if triggers is not None:
            self._values["triggers"] = triggers

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''``AWS::CodeCommit::Repository.RepositoryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-repositoryname
        '''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code(
        self,
    ) -> typing.Optional[typing.Union[CfnRepository.CodeProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::CodeCommit::Repository.Code``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-code
        '''
        result = self._values.get("code")
        return typing.cast(typing.Optional[typing.Union[CfnRepository.CodeProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def repository_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::CodeCommit::Repository.RepositoryDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-repositorydescription
        '''
        result = self._values.get("repository_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::CodeCommit::Repository.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def triggers(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnRepository.RepositoryTriggerProperty]]]]:
        '''``AWS::CodeCommit::Repository.Triggers``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html#cfn-codecommit-repository-triggers
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnRepository.RepositoryTriggerProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-codecommit.IRepository")
class IRepository(
    aws_cdk.core.IResource,
    aws_cdk.aws_codestarnotifications.INotificationRuleSource,
    typing_extensions.Protocol,
):
    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> builtins.str:
        '''The ARN of this Repository.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryCloneUrlGrc")
    def repository_clone_url_grc(self) -> builtins.str:
        '''The HTTPS (GRC) clone URL.

        HTTPS (GRC) is the protocol to use with git-remote-codecommit (GRC).

        It is the recommended method for supporting connections made with federated
        access, identity providers, and temporary credentials.

        :see: https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryCloneUrlHttp")
    def repository_clone_url_http(self) -> builtins.str:
        '''The HTTP clone URL.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryCloneUrlSsh")
    def repository_clone_url_ssh(self) -> builtins.str:
        '''The SSH clone URL.

        :attribute: true
        '''
        ...

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The human-visible name of this Repository.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
        *actions: builtins.str,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grant the given principal identity permissions to perform the actions on this repository.

        :param grantee: -
        :param actions: -
        '''
        ...

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        '''Grant the given identity permissions to pull this repository.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grant the given identity permissions to pull and push this repository.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        '''Grant the given identity permissions to read this repository.

        :param grantee: -
        '''
        ...

    @jsii.member(jsii_name="notifiyOnPullRequestMerged")
    def notifiy_on_pull_request_merged(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a pull request is merged.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOn")
    def notify_on(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        events: typing.Sequence["RepositoryNotificationEvents"],
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule triggered when the project events specified by you are emitted. Similar to ``onEvent`` API.

        You can also use the methods to define rules for the specific event emitted.
        eg: ``notifyOnPullRequstCreated``.

        :param id: -
        :param target: -
        :param events: A list of event types associated with this notification rule for CodeCommit repositories. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``

        :return: CodeStar Notifications rule associated with this repository.
        '''
        ...

    @jsii.member(jsii_name="notifyOnApprovalRuleOverridden")
    def notify_on_approval_rule_overridden(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when an approval rule is overridden.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnApprovalStatusChanged")
    def notify_on_approval_status_changed(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when an approval status is changed.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnBranchOrTagCreated")
    def notify_on_branch_or_tag_created(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a new branch or tag is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnBranchOrTagDeleted")
    def notify_on_branch_or_tag_deleted(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a branch or tag is deleted.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnPullRequestComment")
    def notify_on_pull_request_comment(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a comment is made on a pull request.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="notifyOnPullRequestCreated")
    def notify_on_pull_request_created(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a pull request is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        ...

    @jsii.member(jsii_name="onCommentOnCommit")
    def on_comment_on_commit(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a commit.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...

    @jsii.member(jsii_name="onCommentOnPullRequest")
    def on_comment_on_pull_request(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a pull request.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...

    @jsii.member(jsii_name="onCommit")
    def on_commit(
        self,
        id: builtins.str,
        *,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a commit is pushed to a branch.

        :param id: -
        :param branches: The branch to monitor. Default: - All branches
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers for repository events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...

    @jsii.member(jsii_name="onPullRequestStateChange")
    def on_pull_request_state_change(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a pull request state is changed.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...

    @jsii.member(jsii_name="onReferenceCreated")
    def on_reference_created(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a reference is created (i.e. a new branch/tag is created) to the repository.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...

    @jsii.member(jsii_name="onReferenceDeleted")
    def on_reference_deleted(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a reference is delete (i.e. a branch/tag is deleted) from the repository.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...

    @jsii.member(jsii_name="onReferenceUpdated")
    def on_reference_updated(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a reference is updated (i.e. a commit is pushed to an existing or new branch) from the repository.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...

    @jsii.member(jsii_name="onStateChange")
    def on_state_change(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a "CodeCommit Repository State Change" event occurs.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        ...


class _IRepositoryProxy(
    jsii.proxy_for(aws_cdk.core.IResource), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_codestarnotifications.INotificationRuleSource), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-codecommit.IRepository"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> builtins.str:
        '''The ARN of this Repository.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryCloneUrlGrc")
    def repository_clone_url_grc(self) -> builtins.str:
        '''The HTTPS (GRC) clone URL.

        HTTPS (GRC) is the protocol to use with git-remote-codecommit (GRC).

        It is the recommended method for supporting connections made with federated
        access, identity providers, and temporary credentials.

        :see: https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlGrc"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryCloneUrlHttp")
    def repository_clone_url_http(self) -> builtins.str:
        '''The HTTP clone URL.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlHttp"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryCloneUrlSsh")
    def repository_clone_url_ssh(self) -> builtins.str:
        '''The SSH clone URL.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlSsh"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The human-visible name of this Repository.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
        *actions: builtins.str,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grant the given principal identity permissions to perform the actions on this repository.

        :param grantee: -
        :param actions: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        '''Grant the given identity permissions to pull this repository.

        :param grantee: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantPull", [grantee]))

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grant the given identity permissions to pull and push this repository.

        :param grantee: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantPullPush", [grantee]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        '''Grant the given identity permissions to read this repository.

        :param grantee: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="notifiyOnPullRequestMerged")
    def notifiy_on_pull_request_merged(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a pull request is merged.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifiyOnPullRequestMerged", [id, target, options]))

    @jsii.member(jsii_name="notifyOn")
    def notify_on(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        events: typing.Sequence["RepositoryNotificationEvents"],
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule triggered when the project events specified by you are emitted. Similar to ``onEvent`` API.

        You can also use the methods to define rules for the specific event emitted.
        eg: ``notifyOnPullRequstCreated``.

        :param id: -
        :param target: -
        :param events: A list of event types associated with this notification rule for CodeCommit repositories. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``

        :return: CodeStar Notifications rule associated with this repository.
        '''
        options = RepositoryNotifyOnOptions(
            events=events,
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOn", [id, target, options]))

    @jsii.member(jsii_name="notifyOnApprovalRuleOverridden")
    def notify_on_approval_rule_overridden(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when an approval rule is overridden.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnApprovalRuleOverridden", [id, target, options]))

    @jsii.member(jsii_name="notifyOnApprovalStatusChanged")
    def notify_on_approval_status_changed(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when an approval status is changed.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnApprovalStatusChanged", [id, target, options]))

    @jsii.member(jsii_name="notifyOnBranchOrTagCreated")
    def notify_on_branch_or_tag_created(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a new branch or tag is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnBranchOrTagCreated", [id, target, options]))

    @jsii.member(jsii_name="notifyOnBranchOrTagDeleted")
    def notify_on_branch_or_tag_deleted(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a branch or tag is deleted.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnBranchOrTagDeleted", [id, target, options]))

    @jsii.member(jsii_name="notifyOnPullRequestComment")
    def notify_on_pull_request_comment(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a comment is made on a pull request.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnPullRequestComment", [id, target, options]))

    @jsii.member(jsii_name="notifyOnPullRequestCreated")
    def notify_on_pull_request_created(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a pull request is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnPullRequestCreated", [id, target, options]))

    @jsii.member(jsii_name="onCommentOnCommit")
    def on_comment_on_commit(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a commit.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onCommentOnCommit", [id, options]))

    @jsii.member(jsii_name="onCommentOnPullRequest")
    def on_comment_on_pull_request(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a pull request.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onCommentOnPullRequest", [id, options]))

    @jsii.member(jsii_name="onCommit")
    def on_commit(
        self,
        id: builtins.str,
        *,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a commit is pushed to a branch.

        :param id: -
        :param branches: The branch to monitor. Default: - All branches
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = OnCommitOptions(
            branches=branches,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onCommit", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers for repository events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onPullRequestStateChange")
    def on_pull_request_state_change(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a pull request state is changed.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onPullRequestStateChange", [id, options]))

    @jsii.member(jsii_name="onReferenceCreated")
    def on_reference_created(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a reference is created (i.e. a new branch/tag is created) to the repository.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onReferenceCreated", [id, options]))

    @jsii.member(jsii_name="onReferenceDeleted")
    def on_reference_deleted(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a reference is delete (i.e. a branch/tag is deleted) from the repository.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onReferenceDeleted", [id, options]))

    @jsii.member(jsii_name="onReferenceUpdated")
    def on_reference_updated(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a reference is updated (i.e. a commit is pushed to an existing or new branch) from the repository.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onReferenceUpdated", [id, options]))

    @jsii.member(jsii_name="onStateChange")
    def on_state_change(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a "CodeCommit Repository State Change" event occurs.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onStateChange", [id, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRepository).__jsii_proxy_class__ = lambda : _IRepositoryProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-codecommit.OnCommitOptions",
    jsii_struct_bases=[aws_cdk.aws_events.OnEventOptions],
    name_mapping={
        "description": "description",
        "event_pattern": "eventPattern",
        "rule_name": "ruleName",
        "target": "target",
        "branches": "branches",
    },
)
class OnCommitOptions(aws_cdk.aws_events.OnEventOptions):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Options for the onCommit() method.

        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param branches: The branch to monitor. Default: - All branches
        '''
        if isinstance(event_pattern, dict):
            event_pattern = aws_cdk.aws_events.EventPattern(**event_pattern)
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if event_pattern is not None:
            self._values["event_pattern"] = event_pattern
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if target is not None:
            self._values["target"] = target
        if branches is not None:
            self._values["branches"] = branches

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the rule's purpose.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_pattern(self) -> typing.Optional[aws_cdk.aws_events.EventPattern]:
        '''Additional restrictions for the event to route to the specified target.

        The method that generates the rule probably imposes some type of event
        filtering. The filtering implied by what you pass here is added
        on top of that filtering.

        :default: - No additional filtering based on an event pattern.

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html
        '''
        result = self._values.get("event_pattern")
        return typing.cast(typing.Optional[aws_cdk.aws_events.EventPattern], result)

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the rule.

        :default: AWS CloudFormation generates a unique physical ID.
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[aws_cdk.aws_events.IRuleTarget]:
        '''The target to register for the event.

        :default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[aws_cdk.aws_events.IRuleTarget], result)

    @builtins.property
    def branches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The branch to monitor.

        :default: - All branches
        '''
        result = self._values.get("branches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OnCommitOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ReferenceEvent(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-codecommit.ReferenceEvent",
):
    '''Fields of CloudWatch Events that change references.

    :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/EventTypes.html#codebuild_event_type
    '''

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="commitId")
    def commit_id(cls) -> builtins.str:
        '''Commit id this reference now points to.'''
        return typing.cast(builtins.str, jsii.sget(cls, "commitId"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="eventType")
    def event_type(cls) -> builtins.str:
        '''The type of reference event.

        'referenceCreated', 'referenceUpdated' or 'referenceDeleted'
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "eventType"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="referenceFullName")
    def reference_full_name(cls) -> builtins.str:
        '''Full reference name.

        For example, 'refs/tags/myTag'
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "referenceFullName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="referenceName")
    def reference_name(cls) -> builtins.str:
        '''Name of reference changed (branch or tag name).'''
        return typing.cast(builtins.str, jsii.sget(cls, "referenceName"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="referenceType")
    def reference_type(cls) -> builtins.str:
        '''Type of reference changed.

        'branch' or 'tag'
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "referenceType"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="repositoryId")
    def repository_id(cls) -> builtins.str:
        '''Id of the CodeCommit repository.'''
        return typing.cast(builtins.str, jsii.sget(cls, "repositoryId"))

    @jsii.python.classproperty # type: ignore[misc]
    @jsii.member(jsii_name="repositoryName")
    def repository_name(cls) -> builtins.str:
        '''Name of the CodeCommit repository.'''
        return typing.cast(builtins.str, jsii.sget(cls, "repositoryName"))


@jsii.implements(IRepository)
class Repository(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-codecommit.Repository",
):
    '''Provides a CodeCommit Repository.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        repository_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param repository_name: Name of the repository. This property is required for all CodeCommit repositories.
        :param description: A description of the repository. Use the description to identify the purpose of the repository. Default: - No description.
        '''
        props = RepositoryProps(
            repository_name=repository_name, description=description
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromRepositoryArn") # type: ignore[misc]
    @builtins.classmethod
    def from_repository_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        repository_arn: builtins.str,
    ) -> IRepository:
        '''Imports a codecommit repository.

        :param scope: -
        :param id: -
        :param repository_arn: (e.g. ``arn:aws:codecommit:us-east-1:123456789012:MyDemoRepo``).
        '''
        return typing.cast(IRepository, jsii.sinvoke(cls, "fromRepositoryArn", [scope, id, repository_arn]))

    @jsii.member(jsii_name="fromRepositoryName") # type: ignore[misc]
    @builtins.classmethod
    def from_repository_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        repository_name: builtins.str,
    ) -> IRepository:
        '''
        :param scope: -
        :param id: -
        :param repository_name: -
        '''
        return typing.cast(IRepository, jsii.sinvoke(cls, "fromRepositoryName", [scope, id, repository_name]))

    @jsii.member(jsii_name="bindAsNotificationRuleSource")
    def bind_as_notification_rule_source(
        self,
        _scope: constructs.Construct,
    ) -> aws_cdk.aws_codestarnotifications.NotificationRuleSourceConfig:
        '''Returns a source configuration for notification rule.

        :param _scope: -
        '''
        return typing.cast(aws_cdk.aws_codestarnotifications.NotificationRuleSourceConfig, jsii.invoke(self, "bindAsNotificationRuleSource", [_scope]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
        *actions: builtins.str,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grant the given principal identity permissions to perform the actions on this repository.

        :param grantee: -
        :param actions: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        '''Grant the given identity permissions to pull this repository.

        :param grantee: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantPull", [grantee]))

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''Grant the given identity permissions to pull and push this repository.

        :param grantee: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantPullPush", [grantee]))

    @jsii.member(jsii_name="grantRead")
    def grant_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        '''Grant the given identity permissions to read this repository.

        :param grantee: -
        '''
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantRead", [grantee]))

    @jsii.member(jsii_name="notifiyOnPullRequestMerged")
    def notifiy_on_pull_request_merged(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a pull request is merged.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifiyOnPullRequestMerged", [id, target, options]))

    @jsii.member(jsii_name="notify")
    def notify(
        self,
        arn: builtins.str,
        *,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_data: typing.Optional[builtins.str] = None,
        events: typing.Optional[typing.Sequence["RepositoryEventTrigger"]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "Repository":
        '''Create a trigger to notify another service to run actions on repository events.

        :param arn: Arn of the resource that repository events will notify.
        :param branches: The names of the branches in the AWS CodeCommit repository that contain events that you want to include in the trigger. If you don't specify at least one branch, the trigger applies to all branches.
        :param custom_data: When an event is triggered, additional information that AWS CodeCommit includes when it sends information to the target.
        :param events: The repository events for which AWS CodeCommit sends information to the target, which you specified in the DestinationArn property.If you don't specify events, the trigger runs for all repository events.
        :param name: A name for the trigger.Triggers on a repository must have unique names.
        '''
        options = RepositoryTriggerOptions(
            branches=branches, custom_data=custom_data, events=events, name=name
        )

        return typing.cast("Repository", jsii.invoke(self, "notify", [arn, options]))

    @jsii.member(jsii_name="notifyOn")
    def notify_on(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        events: typing.Sequence["RepositoryNotificationEvents"],
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule triggered when the project events specified by you are emitted. Similar to ``onEvent`` API.

        You can also use the methods to define rules for the specific event emitted.
        eg: ``notifyOnPullRequstCreated``.

        :param id: -
        :param target: -
        :param events: A list of event types associated with this notification rule for CodeCommit repositories. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = RepositoryNotifyOnOptions(
            events=events,
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOn", [id, target, options]))

    @jsii.member(jsii_name="notifyOnApprovalRuleOverridden")
    def notify_on_approval_rule_overridden(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when an approval rule is overridden.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnApprovalRuleOverridden", [id, target, options]))

    @jsii.member(jsii_name="notifyOnApprovalStatusChanged")
    def notify_on_approval_status_changed(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when an approval status is changed.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnApprovalStatusChanged", [id, target, options]))

    @jsii.member(jsii_name="notifyOnBranchOrTagCreated")
    def notify_on_branch_or_tag_created(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a new branch or tag is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnBranchOrTagCreated", [id, target, options]))

    @jsii.member(jsii_name="notifyOnBranchOrTagDeleted")
    def notify_on_branch_or_tag_deleted(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a branch or tag is deleted.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnBranchOrTagDeleted", [id, target, options]))

    @jsii.member(jsii_name="notifyOnPullRequestComment")
    def notify_on_pull_request_comment(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a comment is made on a pull request.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnPullRequestComment", [id, target, options]))

    @jsii.member(jsii_name="notifyOnPullRequestCreated")
    def notify_on_pull_request_created(
        self,
        id: builtins.str,
        target: aws_cdk.aws_codestarnotifications.INotificationRuleTarget,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_codestarnotifications.INotificationRule:
        '''Defines a CodeStar Notification rule which triggers when a pull request is created.

        :param id: -
        :param target: -
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        options = aws_cdk.aws_codestarnotifications.NotificationRuleOptions(
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        return typing.cast(aws_cdk.aws_codestarnotifications.INotificationRule, jsii.invoke(self, "notifyOnPullRequestCreated", [id, target, options]))

    @jsii.member(jsii_name="onCommentOnCommit")
    def on_comment_on_commit(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a commit.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onCommentOnCommit", [id, options]))

    @jsii.member(jsii_name="onCommentOnPullRequest")
    def on_comment_on_pull_request(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a comment is made on a pull request.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onCommentOnPullRequest", [id, options]))

    @jsii.member(jsii_name="onCommit")
    def on_commit(
        self,
        id: builtins.str,
        *,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a commit is pushed to a branch.

        :param id: -
        :param branches: The branch to monitor. Default: - All branches
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = OnCommitOptions(
            branches=branches,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onCommit", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers for repository events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onPullRequestStateChange")
    def on_pull_request_state_change(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a pull request state is changed.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onPullRequestStateChange", [id, options]))

    @jsii.member(jsii_name="onReferenceCreated")
    def on_reference_created(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a reference is created (i.e. a new branch/tag is created) to the repository.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onReferenceCreated", [id, options]))

    @jsii.member(jsii_name="onReferenceDeleted")
    def on_reference_deleted(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a reference is delete (i.e. a branch/tag is deleted) from the repository.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onReferenceDeleted", [id, options]))

    @jsii.member(jsii_name="onReferenceUpdated")
    def on_reference_updated(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a reference is updated (i.e. a commit is pushed to an existing or new branch) from the repository.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onReferenceUpdated", [id, options]))

    @jsii.member(jsii_name="onStateChange")
    def on_state_change(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern] = None,
        rule_name: typing.Optional[builtins.str] = None,
        target: typing.Optional[aws_cdk.aws_events.IRuleTarget] = None,
    ) -> aws_cdk.aws_events.Rule:
        '''Defines a CloudWatch event rule which triggers when a "CodeCommit Repository State Change" event occurs.

        :param id: -
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        '''
        options = aws_cdk.aws_events.OnEventOptions(
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
            target=target,
        )

        return typing.cast(aws_cdk.aws_events.Rule, jsii.invoke(self, "onStateChange", [id, options]))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> builtins.str:
        '''The ARN of this Repository.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryCloneUrlGrc")
    def repository_clone_url_grc(self) -> builtins.str:
        '''The HTTPS (GRC) clone URL.

        HTTPS (GRC) is the protocol to use with git-remote-codecommit (GRC).

        It is the recommended method for supporting connections made with federated
        access, identity providers, and temporary credentials.
        '''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlGrc"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryCloneUrlHttp")
    def repository_clone_url_http(self) -> builtins.str:
        '''The HTTP clone URL.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlHttp"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryCloneUrlSsh")
    def repository_clone_url_ssh(self) -> builtins.str:
        '''The SSH clone URL.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryCloneUrlSsh"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The human-visible name of this Repository.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))


@jsii.enum(jsii_type="@aws-cdk/aws-codecommit.RepositoryEventTrigger")
class RepositoryEventTrigger(enum.Enum):
    '''Repository events that will cause the trigger to run actions in another service.'''

    ALL = "ALL"
    UPDATE_REF = "UPDATE_REF"
    CREATE_REF = "CREATE_REF"
    DELETE_REF = "DELETE_REF"


@jsii.enum(jsii_type="@aws-cdk/aws-codecommit.RepositoryNotificationEvents")
class RepositoryNotificationEvents(enum.Enum):
    '''List of event types for AWS CodeCommit.

    :see: https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#events-ref-repositories
    '''

    COMMIT_COMMENT = "COMMIT_COMMENT"
    '''Trigger notication when comment made on commit.'''
    PULL_REQUEST_COMMENT = "PULL_REQUEST_COMMENT"
    '''Trigger notification when comment made on pull request.'''
    APPROVAL_STATUS_CHANGED = "APPROVAL_STATUS_CHANGED"
    '''Trigger notification when approval status changed.'''
    APPROVAL_RULE_OVERRIDDEN = "APPROVAL_RULE_OVERRIDDEN"
    '''Trigger notifications when approval rule is overridden.'''
    PULL_REQUEST_CREATED = "PULL_REQUEST_CREATED"
    '''Trigger notification when pull request created.'''
    PULL_REQUEST_SOURCE_UPDATED = "PULL_REQUEST_SOURCE_UPDATED"
    '''Trigger notification when pull request source updated.'''
    PULL_REQUEST_STATUS_CHANGED = "PULL_REQUEST_STATUS_CHANGED"
    '''Trigger notification when pull request status is changed.'''
    PULL_REQUEST_MERGED = "PULL_REQUEST_MERGED"
    '''Trigger notification when pull requset is merged.'''
    BRANCH_OR_TAG_CREATED = "BRANCH_OR_TAG_CREATED"
    '''Trigger notification when a branch or tag is created.'''
    BRANCH_OR_TAG_DELETED = "BRANCH_OR_TAG_DELETED"
    '''Trigger notification when a branch or tag is deleted.'''
    BRANCH_OR_TAG_UPDATED = "BRANCH_OR_TAG_UPDATED"
    '''Trigger notification when a branch or tag is updated.'''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-codecommit.RepositoryNotifyOnOptions",
    jsii_struct_bases=[aws_cdk.aws_codestarnotifications.NotificationRuleOptions],
    name_mapping={
        "detail_type": "detailType",
        "enabled": "enabled",
        "notification_rule_name": "notificationRuleName",
        "events": "events",
    },
)
class RepositoryNotifyOnOptions(
    aws_cdk.aws_codestarnotifications.NotificationRuleOptions,
):
    def __init__(
        self,
        *,
        detail_type: typing.Optional[aws_cdk.aws_codestarnotifications.DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
        events: typing.Sequence[RepositoryNotificationEvents],
    ) -> None:
        '''Additional options to pass to the notification rule.

        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        :param events: A list of event types associated with this notification rule for CodeCommit repositories. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "events": events,
        }
        if detail_type is not None:
            self._values["detail_type"] = detail_type
        if enabled is not None:
            self._values["enabled"] = enabled
        if notification_rule_name is not None:
            self._values["notification_rule_name"] = notification_rule_name

    @builtins.property
    def detail_type(
        self,
    ) -> typing.Optional[aws_cdk.aws_codestarnotifications.DetailType]:
        '''The level of detail to include in the notifications for this resource.

        BASIC will include only the contents of the event as it would appear in AWS CloudWatch.
        FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.

        :default: DetailType.FULL
        '''
        result = self._values.get("detail_type")
        return typing.cast(typing.Optional[aws_cdk.aws_codestarnotifications.DetailType], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''The status of the notification rule.

        If the enabled is set to DISABLED, notifications aren't sent for the notification rule.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notification_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the notification rule.

        Notification rule names must be unique in your AWS account.

        :default: - generated from the ``id``
        '''
        result = self._values.get("notification_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def events(self) -> typing.List[RepositoryNotificationEvents]:
        '''A list of event types associated with this notification rule for CodeCommit repositories.

        For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.

        :see: https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#concepts-api
        '''
        result = self._values.get("events")
        assert result is not None, "Required property 'events' is missing"
        return typing.cast(typing.List[RepositoryNotificationEvents], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryNotifyOnOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-codecommit.RepositoryProps",
    jsii_struct_bases=[],
    name_mapping={"repository_name": "repositoryName", "description": "description"},
)
class RepositoryProps:
    def __init__(
        self,
        *,
        repository_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param repository_name: Name of the repository. This property is required for all CodeCommit repositories.
        :param description: A description of the repository. Use the description to identify the purpose of the repository. Default: - No description.
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "repository_name": repository_name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''Name of the repository.

        This property is required for all CodeCommit repositories.
        '''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the repository.

        Use the description to identify the
        purpose of the repository.

        :default: - No description.
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-codecommit.RepositoryTriggerOptions",
    jsii_struct_bases=[],
    name_mapping={
        "branches": "branches",
        "custom_data": "customData",
        "events": "events",
        "name": "name",
    },
)
class RepositoryTriggerOptions:
    def __init__(
        self,
        *,
        branches: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_data: typing.Optional[builtins.str] = None,
        events: typing.Optional[typing.Sequence[RepositoryEventTrigger]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Creates for a repository trigger to an SNS topic or Lambda function.

        :param branches: The names of the branches in the AWS CodeCommit repository that contain events that you want to include in the trigger. If you don't specify at least one branch, the trigger applies to all branches.
        :param custom_data: When an event is triggered, additional information that AWS CodeCommit includes when it sends information to the target.
        :param events: The repository events for which AWS CodeCommit sends information to the target, which you specified in the DestinationArn property.If you don't specify events, the trigger runs for all repository events.
        :param name: A name for the trigger.Triggers on a repository must have unique names.
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if branches is not None:
            self._values["branches"] = branches
        if custom_data is not None:
            self._values["custom_data"] = custom_data
        if events is not None:
            self._values["events"] = events
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def branches(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The names of the branches in the AWS CodeCommit repository that contain events that you want to include in the trigger.

        If you don't specify at
        least one branch, the trigger applies to all branches.
        '''
        result = self._values.get("branches")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''When an event is triggered, additional information that AWS CodeCommit includes when it sends information to the target.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def events(self) -> typing.Optional[typing.List[RepositoryEventTrigger]]:
        '''The repository events for which AWS CodeCommit sends information to the target, which you specified in the DestinationArn property.If you don't specify events, the trigger runs for all repository events.'''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[RepositoryEventTrigger]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the trigger.Triggers on a repository must have unique names.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryTriggerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnRepository",
    "CfnRepositoryProps",
    "IRepository",
    "OnCommitOptions",
    "ReferenceEvent",
    "Repository",
    "RepositoryEventTrigger",
    "RepositoryNotificationEvents",
    "RepositoryNotifyOnOptions",
    "RepositoryProps",
    "RepositoryTriggerOptions",
]

publication.publish()
