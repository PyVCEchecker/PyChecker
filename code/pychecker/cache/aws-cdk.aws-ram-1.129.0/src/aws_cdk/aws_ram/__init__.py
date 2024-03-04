'''
# AWS Resource Access Manager Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_ram as ram
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
class CfnResourceShare(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-ram.CfnResourceShare",
):
    '''A CloudFormation ``AWS::RAM::ResourceShare``.

    :cloudformationResource: AWS::RAM::ResourceShare
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        allow_external_principals: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        permission_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::RAM::ResourceShare``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::RAM::ResourceShare.Name``.
        :param allow_external_principals: ``AWS::RAM::ResourceShare.AllowExternalPrincipals``.
        :param permission_arns: ``AWS::RAM::ResourceShare.PermissionArns``.
        :param principals: ``AWS::RAM::ResourceShare.Principals``.
        :param resource_arns: ``AWS::RAM::ResourceShare.ResourceArns``.
        :param tags: ``AWS::RAM::ResourceShare.Tags``.
        '''
        props = CfnResourceShareProps(
            name=name,
            allow_external_principals=allow_external_principals,
            permission_arns=permission_arns,
            principals=principals,
            resource_arns=resource_arns,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::RAM::ResourceShare.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::RAM::ResourceShare.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowExternalPrincipals")
    def allow_external_principals(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::RAM::ResourceShare.AllowExternalPrincipals``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-allowexternalprincipals
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "allowExternalPrincipals"))

    @allow_external_principals.setter
    def allow_external_principals(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "allowExternalPrincipals", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionArns")
    def permission_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RAM::ResourceShare.PermissionArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-permissionarns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionArns"))

    @permission_arns.setter
    def permission_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "permissionArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="principals")
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RAM::ResourceShare.Principals``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-principals
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "principals"))

    @principals.setter
    def principals(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "principals", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceArns")
    def resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RAM::ResourceShare.ResourceArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-resourcearns
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceArns"))

    @resource_arns.setter
    def resource_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "resourceArns", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-ram.CfnResourceShareProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allow_external_principals": "allowExternalPrincipals",
        "permission_arns": "permissionArns",
        "principals": "principals",
        "resource_arns": "resourceArns",
        "tags": "tags",
    },
)
class CfnResourceShareProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        allow_external_principals: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        permission_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::RAM::ResourceShare``.

        :param name: ``AWS::RAM::ResourceShare.Name``.
        :param allow_external_principals: ``AWS::RAM::ResourceShare.AllowExternalPrincipals``.
        :param permission_arns: ``AWS::RAM::ResourceShare.PermissionArns``.
        :param principals: ``AWS::RAM::ResourceShare.Principals``.
        :param resource_arns: ``AWS::RAM::ResourceShare.ResourceArns``.
        :param tags: ``AWS::RAM::ResourceShare.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if allow_external_principals is not None:
            self._values["allow_external_principals"] = allow_external_principals
        if permission_arns is not None:
            self._values["permission_arns"] = permission_arns
        if principals is not None:
            self._values["principals"] = principals
        if resource_arns is not None:
            self._values["resource_arns"] = resource_arns
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::RAM::ResourceShare.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_external_principals(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::RAM::ResourceShare.AllowExternalPrincipals``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-allowexternalprincipals
        '''
        result = self._values.get("allow_external_principals")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def permission_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RAM::ResourceShare.PermissionArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-permissionarns
        '''
        result = self._values.get("permission_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RAM::ResourceShare.Principals``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-principals
        '''
        result = self._values.get("principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::RAM::ResourceShare.ResourceArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-resourcearns
        '''
        result = self._values.get("resource_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::RAM::ResourceShare.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceShareProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnResourceShare",
    "CfnResourceShareProps",
]

publication.publish()
