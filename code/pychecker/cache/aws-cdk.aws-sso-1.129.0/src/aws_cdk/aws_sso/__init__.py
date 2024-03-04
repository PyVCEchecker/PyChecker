'''
# AWS::SSO Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_sso as sso
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
class CfnAssignment(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sso.CfnAssignment",
):
    '''A CloudFormation ``AWS::SSO::Assignment``.

    :cloudformationResource: AWS::SSO::Assignment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        permission_set_arn: builtins.str,
        principal_id: builtins.str,
        principal_type: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Create a new ``AWS::SSO::Assignment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: ``AWS::SSO::Assignment.InstanceArn``.
        :param permission_set_arn: ``AWS::SSO::Assignment.PermissionSetArn``.
        :param principal_id: ``AWS::SSO::Assignment.PrincipalId``.
        :param principal_type: ``AWS::SSO::Assignment.PrincipalType``.
        :param target_id: ``AWS::SSO::Assignment.TargetId``.
        :param target_type: ``AWS::SSO::Assignment.TargetType``.
        '''
        props = CfnAssignmentProps(
            instance_arn=instance_arn,
            permission_set_arn=permission_set_arn,
            principal_id=principal_id,
            principal_type=principal_type,
            target_id=target_id,
            target_type=target_type,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::SSO::Assignment.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="permissionSetArn")
    def permission_set_arn(self) -> builtins.str:
        '''``AWS::SSO::Assignment.PermissionSetArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "permissionSetArn"))

    @permission_set_arn.setter
    def permission_set_arn(self, value: builtins.str) -> None:
        jsii.set(self, "permissionSetArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        '''``AWS::SSO::Assignment.PrincipalId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid
        '''
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @principal_id.setter
    def principal_id(self, value: builtins.str) -> None:
        jsii.set(self, "principalId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="principalType")
    def principal_type(self) -> builtins.str:
        '''``AWS::SSO::Assignment.PrincipalType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype
        '''
        return typing.cast(builtins.str, jsii.get(self, "principalType"))

    @principal_type.setter
    def principal_type(self, value: builtins.str) -> None:
        jsii.set(self, "principalType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        '''``AWS::SSO::Assignment.TargetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @target_id.setter
    def target_id(self, value: builtins.str) -> None:
        jsii.set(self, "targetId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        '''``AWS::SSO::Assignment.TargetType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype
        '''
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        jsii.set(self, "targetType", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sso.CfnAssignmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "permission_set_arn": "permissionSetArn",
        "principal_id": "principalId",
        "principal_type": "principalType",
        "target_id": "targetId",
        "target_type": "targetType",
    },
)
class CfnAssignmentProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        permission_set_arn: builtins.str,
        principal_id: builtins.str,
        principal_type: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::SSO::Assignment``.

        :param instance_arn: ``AWS::SSO::Assignment.InstanceArn``.
        :param permission_set_arn: ``AWS::SSO::Assignment.PermissionSetArn``.
        :param principal_id: ``AWS::SSO::Assignment.PrincipalId``.
        :param principal_type: ``AWS::SSO::Assignment.PrincipalType``.
        :param target_id: ``AWS::SSO::Assignment.TargetId``.
        :param target_type: ``AWS::SSO::Assignment.TargetType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "permission_set_arn": permission_set_arn,
            "principal_id": principal_id,
            "principal_type": principal_type,
            "target_id": target_id,
            "target_type": target_type,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::SSO::Assignment.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permission_set_arn(self) -> builtins.str:
        '''``AWS::SSO::Assignment.PermissionSetArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn
        '''
        result = self._values.get("permission_set_arn")
        assert result is not None, "Required property 'permission_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_id(self) -> builtins.str:
        '''``AWS::SSO::Assignment.PrincipalId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid
        '''
        result = self._values.get("principal_id")
        assert result is not None, "Required property 'principal_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_type(self) -> builtins.str:
        '''``AWS::SSO::Assignment.PrincipalType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype
        '''
        result = self._values.get("principal_type")
        assert result is not None, "Required property 'principal_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_id(self) -> builtins.str:
        '''``AWS::SSO::Assignment.TargetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid
        '''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''``AWS::SSO::Assignment.TargetType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssignmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnInstanceAccessControlAttributeConfiguration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sso.CfnInstanceAccessControlAttributeConfiguration",
):
    '''A CloudFormation ``AWS::SSO::InstanceAccessControlAttributeConfiguration``.

    :cloudformationResource: AWS::SSO::InstanceAccessControlAttributeConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        access_control_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", aws_cdk.core.IResolvable]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SSO::InstanceAccessControlAttributeConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: ``AWS::SSO::InstanceAccessControlAttributeConfiguration.InstanceArn``.
        :param access_control_attributes: ``AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributes``.
        '''
        props = CfnInstanceAccessControlAttributeConfigurationProps(
            instance_arn=instance_arn,
            access_control_attributes=access_control_attributes,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::SSO::InstanceAccessControlAttributeConfiguration.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="accessControlAttributes")
    def access_control_attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", aws_cdk.core.IResolvable]]]]:
        '''``AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributes
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", aws_cdk.core.IResolvable]]]], jsii.get(self, "accessControlAttributes"))

    @access_control_attributes.setter
    def access_control_attributes(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "accessControlAttributes", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class AccessControlAttributeProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Union[aws_cdk.core.IResolvable, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty"],
        ) -> None:
            '''
            :param key: ``CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty.Key``.
            :param value: ``CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty"]:
            '''``CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessControlAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class AccessControlAttributeValueProperty:
        def __init__(self, *, source: typing.Sequence[builtins.str]) -> None:
            '''
            :param source: ``CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "source": source,
            }

        @builtins.property
        def source(self) -> typing.List[builtins.str]:
            '''``CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty.Source``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessControlAttributeValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sso.CfnInstanceAccessControlAttributeConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "access_control_attributes": "accessControlAttributes",
    },
)
class CfnInstanceAccessControlAttributeConfigurationProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        access_control_attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, aws_cdk.core.IResolvable]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSO::InstanceAccessControlAttributeConfiguration``.

        :param instance_arn: ``AWS::SSO::InstanceAccessControlAttributeConfiguration.InstanceArn``.
        :param access_control_attributes: ``AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
        }
        if access_control_attributes is not None:
            self._values["access_control_attributes"] = access_control_attributes

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::SSO::InstanceAccessControlAttributeConfiguration.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_control_attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, aws_cdk.core.IResolvable]]]]:
        '''``AWS::SSO::InstanceAccessControlAttributeConfiguration.AccessControlAttributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributes
        '''
        result = self._values.get("access_control_attributes")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, aws_cdk.core.IResolvable]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceAccessControlAttributeConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPermissionSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-sso.CfnPermissionSet",
):
    '''A CloudFormation ``AWS::SSO::PermissionSet``.

    :cloudformationResource: AWS::SSO::PermissionSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        inline_policy: typing.Any = None,
        managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        relay_state_type: typing.Optional[builtins.str] = None,
        session_duration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::SSO::PermissionSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_arn: ``AWS::SSO::PermissionSet.InstanceArn``.
        :param name: ``AWS::SSO::PermissionSet.Name``.
        :param description: ``AWS::SSO::PermissionSet.Description``.
        :param inline_policy: ``AWS::SSO::PermissionSet.InlinePolicy``.
        :param managed_policies: ``AWS::SSO::PermissionSet.ManagedPolicies``.
        :param relay_state_type: ``AWS::SSO::PermissionSet.RelayStateType``.
        :param session_duration: ``AWS::SSO::PermissionSet.SessionDuration``.
        :param tags: ``AWS::SSO::PermissionSet.Tags``.
        '''
        props = CfnPermissionSetProps(
            instance_arn=instance_arn,
            name=name,
            description=description,
            inline_policy=inline_policy,
            managed_policies=managed_policies,
            relay_state_type=relay_state_type,
            session_duration=session_duration,
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
    @jsii.member(jsii_name="attrPermissionSetArn")
    def attr_permission_set_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: PermissionSetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPermissionSetArn"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::SSO::PermissionSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="inlinePolicy")
    def inline_policy(self) -> typing.Any:
        '''``AWS::SSO::PermissionSet.InlinePolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy
        '''
        return typing.cast(typing.Any, jsii.get(self, "inlinePolicy"))

    @inline_policy.setter
    def inline_policy(self, value: typing.Any) -> None:
        jsii.set(self, "inlinePolicy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''``AWS::SSO::PermissionSet.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        jsii.set(self, "instanceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::SSO::PermissionSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSO::PermissionSet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="managedPolicies")
    def managed_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SSO::PermissionSet.ManagedPolicies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "managedPolicies"))

    @managed_policies.setter
    def managed_policies(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "managedPolicies", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="relayStateType")
    def relay_state_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSO::PermissionSet.RelayStateType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relayStateType"))

    @relay_state_type.setter
    def relay_state_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "relayStateType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sessionDuration")
    def session_duration(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSO::PermissionSet.SessionDuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionDuration"))

    @session_duration.setter
    def session_duration(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sessionDuration", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-sso.CfnPermissionSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "description": "description",
        "inline_policy": "inlinePolicy",
        "managed_policies": "managedPolicies",
        "relay_state_type": "relayStateType",
        "session_duration": "sessionDuration",
        "tags": "tags",
    },
)
class CfnPermissionSetProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        inline_policy: typing.Any = None,
        managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        relay_state_type: typing.Optional[builtins.str] = None,
        session_duration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::SSO::PermissionSet``.

        :param instance_arn: ``AWS::SSO::PermissionSet.InstanceArn``.
        :param name: ``AWS::SSO::PermissionSet.Name``.
        :param description: ``AWS::SSO::PermissionSet.Description``.
        :param inline_policy: ``AWS::SSO::PermissionSet.InlinePolicy``.
        :param managed_policies: ``AWS::SSO::PermissionSet.ManagedPolicies``.
        :param relay_state_type: ``AWS::SSO::PermissionSet.RelayStateType``.
        :param session_duration: ``AWS::SSO::PermissionSet.SessionDuration``.
        :param tags: ``AWS::SSO::PermissionSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if inline_policy is not None:
            self._values["inline_policy"] = inline_policy
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if relay_state_type is not None:
            self._values["relay_state_type"] = relay_state_type
        if session_duration is not None:
            self._values["session_duration"] = session_duration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''``AWS::SSO::PermissionSet.InstanceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::SSO::PermissionSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSO::PermissionSet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inline_policy(self) -> typing.Any:
        '''``AWS::SSO::PermissionSet.InlinePolicy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy
        '''
        result = self._values.get("inline_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::SSO::PermissionSet.ManagedPolicies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies
        '''
        result = self._values.get("managed_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def relay_state_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSO::PermissionSet.RelayStateType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype
        '''
        result = self._values.get("relay_state_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_duration(self) -> typing.Optional[builtins.str]:
        '''``AWS::SSO::PermissionSet.SessionDuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration
        '''
        result = self._values.get("session_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::SSO::PermissionSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssignment",
    "CfnAssignmentProps",
    "CfnInstanceAccessControlAttributeConfiguration",
    "CfnInstanceAccessControlAttributeConfigurationProps",
    "CfnPermissionSet",
    "CfnPermissionSetProps",
]

publication.publish()
