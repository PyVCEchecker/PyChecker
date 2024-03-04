'''
# AWS::EventSchemas Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_eventschemas as eventschemas
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

import aws_cdk.core


@jsii.implements(aws_cdk.core.IInspectable)
class CfnDiscoverer(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eventschemas.CfnDiscoverer",
):
    '''A CloudFormation ``AWS::EventSchemas::Discoverer``.

    :cloudformationResource: AWS::EventSchemas::Discoverer
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        source_arn: builtins.str,
        cross_account: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["CfnDiscoverer.TagsEntryProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::EventSchemas::Discoverer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param source_arn: ``AWS::EventSchemas::Discoverer.SourceArn``.
        :param cross_account: ``AWS::EventSchemas::Discoverer.CrossAccount``.
        :param description: ``AWS::EventSchemas::Discoverer.Description``.
        :param tags: ``AWS::EventSchemas::Discoverer.Tags``.
        '''
        props = CfnDiscovererProps(
            source_arn=source_arn,
            cross_account=cross_account,
            description=description,
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
    @jsii.member(jsii_name="attrCrossAccount")
    def attr_cross_account(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: CrossAccount
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrCrossAccount"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDiscovererArn")
    def attr_discoverer_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: DiscovererArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDiscovererArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrDiscovererId")
    def attr_discoverer_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: DiscovererId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDiscovererId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::EventSchemas::Discoverer.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceArn")
    def source_arn(self) -> builtins.str:
        '''``AWS::EventSchemas::Discoverer.SourceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-sourcearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "sourceArn"))

    @source_arn.setter
    def source_arn(self, value: builtins.str) -> None:
        jsii.set(self, "sourceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="crossAccount")
    def cross_account(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::EventSchemas::Discoverer.CrossAccount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-crossaccount
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "crossAccount"))

    @cross_account.setter
    def cross_account(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "crossAccount", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::Discoverer.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eventschemas.CfnDiscoverer.TagsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsEntryProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: ``CfnDiscoverer.TagsEntryProperty.Key``.
            :param value: ``CfnDiscoverer.TagsEntryProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnDiscoverer.TagsEntryProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnDiscoverer.TagsEntryProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eventschemas.CfnDiscovererProps",
    jsii_struct_bases=[],
    name_mapping={
        "source_arn": "sourceArn",
        "cross_account": "crossAccount",
        "description": "description",
        "tags": "tags",
    },
)
class CfnDiscovererProps:
    def __init__(
        self,
        *,
        source_arn: builtins.str,
        cross_account: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[CfnDiscoverer.TagsEntryProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EventSchemas::Discoverer``.

        :param source_arn: ``AWS::EventSchemas::Discoverer.SourceArn``.
        :param cross_account: ``AWS::EventSchemas::Discoverer.CrossAccount``.
        :param description: ``AWS::EventSchemas::Discoverer.Description``.
        :param tags: ``AWS::EventSchemas::Discoverer.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "source_arn": source_arn,
        }
        if cross_account is not None:
            self._values["cross_account"] = cross_account
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def source_arn(self) -> builtins.str:
        '''``AWS::EventSchemas::Discoverer.SourceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-sourcearn
        '''
        result = self._values.get("source_arn")
        assert result is not None, "Required property 'source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cross_account(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::EventSchemas::Discoverer.CrossAccount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-crossaccount
        '''
        result = self._values.get("cross_account")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::Discoverer.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnDiscoverer.TagsEntryProperty]]:
        '''``AWS::EventSchemas::Discoverer.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnDiscoverer.TagsEntryProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDiscovererProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRegistry(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eventschemas.CfnRegistry",
):
    '''A CloudFormation ``AWS::EventSchemas::Registry``.

    :cloudformationResource: AWS::EventSchemas::Registry
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        registry_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["CfnRegistry.TagsEntryProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::EventSchemas::Registry``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::EventSchemas::Registry.Description``.
        :param registry_name: ``AWS::EventSchemas::Registry.RegistryName``.
        :param tags: ``AWS::EventSchemas::Registry.Tags``.
        '''
        props = CfnRegistryProps(
            description=description, registry_name=registry_name, tags=tags
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
    @jsii.member(jsii_name="attrRegistryArn")
    def attr_registry_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: RegistryArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegistryArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrRegistryName")
    def attr_registry_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: RegistryName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegistryName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::EventSchemas::Registry.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::Registry.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="registryName")
    def registry_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::Registry.RegistryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-registryname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryName"))

    @registry_name.setter
    def registry_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "registryName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eventschemas.CfnRegistry.TagsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsEntryProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: ``CfnRegistry.TagsEntryProperty.Key``.
            :param value: ``CfnRegistry.TagsEntryProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnRegistry.TagsEntryProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnRegistry.TagsEntryProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRegistryPolicy(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eventschemas.CfnRegistryPolicy",
):
    '''A CloudFormation ``AWS::EventSchemas::RegistryPolicy``.

    :cloudformationResource: AWS::EventSchemas::RegistryPolicy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        policy: typing.Any,
        registry_name: builtins.str,
        revision_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::EventSchemas::RegistryPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param policy: ``AWS::EventSchemas::RegistryPolicy.Policy``.
        :param registry_name: ``AWS::EventSchemas::RegistryPolicy.RegistryName``.
        :param revision_id: ``AWS::EventSchemas::RegistryPolicy.RevisionId``.
        '''
        props = CfnRegistryPolicyProps(
            policy=policy, registry_name=registry_name, revision_id=revision_id
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''``AWS::EventSchemas::RegistryPolicy.Policy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-policy
        '''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        jsii.set(self, "policy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="registryName")
    def registry_name(self) -> builtins.str:
        '''``AWS::EventSchemas::RegistryPolicy.RegistryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-registryname
        '''
        return typing.cast(builtins.str, jsii.get(self, "registryName"))

    @registry_name.setter
    def registry_name(self, value: builtins.str) -> None:
        jsii.set(self, "registryName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="revisionId")
    def revision_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::RegistryPolicy.RevisionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-revisionid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionId"))

    @revision_id.setter
    def revision_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "revisionId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eventschemas.CfnRegistryPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy": "policy",
        "registry_name": "registryName",
        "revision_id": "revisionId",
    },
)
class CfnRegistryPolicyProps:
    def __init__(
        self,
        *,
        policy: typing.Any,
        registry_name: builtins.str,
        revision_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EventSchemas::RegistryPolicy``.

        :param policy: ``AWS::EventSchemas::RegistryPolicy.Policy``.
        :param registry_name: ``AWS::EventSchemas::RegistryPolicy.RegistryName``.
        :param revision_id: ``AWS::EventSchemas::RegistryPolicy.RevisionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "policy": policy,
            "registry_name": registry_name,
        }
        if revision_id is not None:
            self._values["revision_id"] = revision_id

    @builtins.property
    def policy(self) -> typing.Any:
        '''``AWS::EventSchemas::RegistryPolicy.Policy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def registry_name(self) -> builtins.str:
        '''``AWS::EventSchemas::RegistryPolicy.RegistryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-registryname
        '''
        result = self._values.get("registry_name")
        assert result is not None, "Required property 'registry_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def revision_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::RegistryPolicy.RevisionId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-revisionid
        '''
        result = self._values.get("revision_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRegistryPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eventschemas.CfnRegistryProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "registry_name": "registryName",
        "tags": "tags",
    },
)
class CfnRegistryProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        registry_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[CfnRegistry.TagsEntryProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EventSchemas::Registry``.

        :param description: ``AWS::EventSchemas::Registry.Description``.
        :param registry_name: ``AWS::EventSchemas::Registry.RegistryName``.
        :param tags: ``AWS::EventSchemas::Registry.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if registry_name is not None:
            self._values["registry_name"] = registry_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::Registry.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registry_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::Registry.RegistryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-registryname
        '''
        result = self._values.get("registry_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnRegistry.TagsEntryProperty]]:
        '''``AWS::EventSchemas::Registry.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnRegistry.TagsEntryProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRegistryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSchema(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-eventschemas.CfnSchema",
):
    '''A CloudFormation ``AWS::EventSchemas::Schema``.

    :cloudformationResource: AWS::EventSchemas::Schema
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        content: builtins.str,
        registry_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence["CfnSchema.TagsEntryProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::EventSchemas::Schema``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param content: ``AWS::EventSchemas::Schema.Content``.
        :param registry_name: ``AWS::EventSchemas::Schema.RegistryName``.
        :param type: ``AWS::EventSchemas::Schema.Type``.
        :param description: ``AWS::EventSchemas::Schema.Description``.
        :param schema_name: ``AWS::EventSchemas::Schema.SchemaName``.
        :param tags: ``AWS::EventSchemas::Schema.Tags``.
        '''
        props = CfnSchemaProps(
            content=content,
            registry_name=registry_name,
            type=type,
            description=description,
            schema_name=schema_name,
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
    @jsii.member(jsii_name="attrSchemaArn")
    def attr_schema_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: SchemaArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchemaArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSchemaName")
    def attr_schema_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: SchemaName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchemaName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrSchemaVersion")
    def attr_schema_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: SchemaVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchemaVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::EventSchemas::Schema.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''``AWS::EventSchemas::Schema.Content``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-content
        '''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        jsii.set(self, "content", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="registryName")
    def registry_name(self) -> builtins.str:
        '''``AWS::EventSchemas::Schema.RegistryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-registryname
        '''
        return typing.cast(builtins.str, jsii.get(self, "registryName"))

    @registry_name.setter
    def registry_name(self, value: builtins.str) -> None:
        jsii.set(self, "registryName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::EventSchemas::Schema.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::Schema.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::Schema.SchemaName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-schemaname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "schemaName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-eventschemas.CfnSchema.TagsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsEntryProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: ``CfnSchema.TagsEntryProperty.Key``.
            :param value: ``CfnSchema.TagsEntryProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnSchema.TagsEntryProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnSchema.TagsEntryProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-eventschemas.CfnSchemaProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "registry_name": "registryName",
        "type": "type",
        "description": "description",
        "schema_name": "schemaName",
        "tags": "tags",
    },
)
class CfnSchemaProps:
    def __init__(
        self,
        *,
        content: builtins.str,
        registry_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[CfnSchema.TagsEntryProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::EventSchemas::Schema``.

        :param content: ``AWS::EventSchemas::Schema.Content``.
        :param registry_name: ``AWS::EventSchemas::Schema.RegistryName``.
        :param type: ``AWS::EventSchemas::Schema.Type``.
        :param description: ``AWS::EventSchemas::Schema.Description``.
        :param schema_name: ``AWS::EventSchemas::Schema.SchemaName``.
        :param tags: ``AWS::EventSchemas::Schema.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "registry_name": registry_name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if schema_name is not None:
            self._values["schema_name"] = schema_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content(self) -> builtins.str:
        '''``AWS::EventSchemas::Schema.Content``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def registry_name(self) -> builtins.str:
        '''``AWS::EventSchemas::Schema.RegistryName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-registryname
        '''
        result = self._values.get("registry_name")
        assert result is not None, "Required property 'registry_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::EventSchemas::Schema.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::Schema.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::EventSchemas::Schema.SchemaName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-schemaname
        '''
        result = self._values.get("schema_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnSchema.TagsEntryProperty]]:
        '''``AWS::EventSchemas::Schema.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnSchema.TagsEntryProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDiscoverer",
    "CfnDiscovererProps",
    "CfnRegistry",
    "CfnRegistryPolicy",
    "CfnRegistryPolicyProps",
    "CfnRegistryProps",
    "CfnSchema",
    "CfnSchemaProps",
]

publication.publish()
