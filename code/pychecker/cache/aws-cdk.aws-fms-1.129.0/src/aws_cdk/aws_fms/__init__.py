'''
# AWS::FMS Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_fms as fms
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
class CfnNotificationChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-fms.CfnNotificationChannel",
):
    '''A CloudFormation ``AWS::FMS::NotificationChannel``.

    :cloudformationResource: AWS::FMS::NotificationChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        sns_role_name: builtins.str,
        sns_topic_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::FMS::NotificationChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param sns_role_name: ``AWS::FMS::NotificationChannel.SnsRoleName``.
        :param sns_topic_arn: ``AWS::FMS::NotificationChannel.SnsTopicArn``.
        '''
        props = CfnNotificationChannelProps(
            sns_role_name=sns_role_name, sns_topic_arn=sns_topic_arn
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
    @jsii.member(jsii_name="snsRoleName")
    def sns_role_name(self) -> builtins.str:
        '''``AWS::FMS::NotificationChannel.SnsRoleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename
        '''
        return typing.cast(builtins.str, jsii.get(self, "snsRoleName"))

    @sns_role_name.setter
    def sns_role_name(self, value: builtins.str) -> None:
        jsii.set(self, "snsRoleName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> builtins.str:
        '''``AWS::FMS::NotificationChannel.SnsTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: builtins.str) -> None:
        jsii.set(self, "snsTopicArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-fms.CfnNotificationChannelProps",
    jsii_struct_bases=[],
    name_mapping={"sns_role_name": "snsRoleName", "sns_topic_arn": "snsTopicArn"},
)
class CfnNotificationChannelProps:
    def __init__(
        self,
        *,
        sns_role_name: builtins.str,
        sns_topic_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::FMS::NotificationChannel``.

        :param sns_role_name: ``AWS::FMS::NotificationChannel.SnsRoleName``.
        :param sns_topic_arn: ``AWS::FMS::NotificationChannel.SnsTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "sns_role_name": sns_role_name,
            "sns_topic_arn": sns_topic_arn,
        }

    @builtins.property
    def sns_role_name(self) -> builtins.str:
        '''``AWS::FMS::NotificationChannel.SnsRoleName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename
        '''
        result = self._values.get("sns_role_name")
        assert result is not None, "Required property 'sns_role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sns_topic_arn(self) -> builtins.str:
        '''``AWS::FMS::NotificationChannel.SnsTopicArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        assert result is not None, "Required property 'sns_topic_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotificationChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPolicy(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-fms.CfnPolicy",
):
    '''A CloudFormation ``AWS::FMS::Policy``.

    :cloudformationResource: AWS::FMS::Policy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        exclude_resource_tags: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        policy_name: builtins.str,
        remediation_enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        resource_type: builtins.str,
        security_service_policy_data: typing.Any,
        delete_all_policy_resources: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        exclude_map: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.IEMapProperty"]] = None,
        include_map: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.IEMapProperty"]] = None,
        resource_tags: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.ResourceTagProperty"]]]] = None,
        resource_type_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence["CfnPolicy.PolicyTagProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::FMS::Policy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param exclude_resource_tags: ``AWS::FMS::Policy.ExcludeResourceTags``.
        :param policy_name: ``AWS::FMS::Policy.PolicyName``.
        :param remediation_enabled: ``AWS::FMS::Policy.RemediationEnabled``.
        :param resource_type: ``AWS::FMS::Policy.ResourceType``.
        :param security_service_policy_data: ``AWS::FMS::Policy.SecurityServicePolicyData``.
        :param delete_all_policy_resources: ``AWS::FMS::Policy.DeleteAllPolicyResources``.
        :param exclude_map: ``AWS::FMS::Policy.ExcludeMap``.
        :param include_map: ``AWS::FMS::Policy.IncludeMap``.
        :param resource_tags: ``AWS::FMS::Policy.ResourceTags``.
        :param resource_type_list: ``AWS::FMS::Policy.ResourceTypeList``.
        :param tags: ``AWS::FMS::Policy.Tags``.
        '''
        props = CfnPolicyProps(
            exclude_resource_tags=exclude_resource_tags,
            policy_name=policy_name,
            remediation_enabled=remediation_enabled,
            resource_type=resource_type,
            security_service_policy_data=security_service_policy_data,
            delete_all_policy_resources=delete_all_policy_resources,
            exclude_map=exclude_map,
            include_map=include_map,
            resource_tags=resource_tags,
            resource_type_list=resource_type_list,
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
    @jsii.member(jsii_name="excludeResourceTags")
    def exclude_resource_tags(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::FMS::Policy.ExcludeResourceTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excluderesourcetags
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "excludeResourceTags"))

    @exclude_resource_tags.setter
    def exclude_resource_tags(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "excludeResourceTags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyName")
    def policy_name(self) -> builtins.str:
        '''``AWS::FMS::Policy.PolicyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policyname
        '''
        return typing.cast(builtins.str, jsii.get(self, "policyName"))

    @policy_name.setter
    def policy_name(self, value: builtins.str) -> None:
        jsii.set(self, "policyName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="remediationEnabled")
    def remediation_enabled(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::FMS::Policy.RemediationEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-remediationenabled
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "remediationEnabled"))

    @remediation_enabled.setter
    def remediation_enabled(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "remediationEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''``AWS::FMS::Policy.ResourceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        jsii.set(self, "resourceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="securityServicePolicyData")
    def security_service_policy_data(self) -> typing.Any:
        '''``AWS::FMS::Policy.SecurityServicePolicyData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-securityservicepolicydata
        '''
        return typing.cast(typing.Any, jsii.get(self, "securityServicePolicyData"))

    @security_service_policy_data.setter
    def security_service_policy_data(self, value: typing.Any) -> None:
        jsii.set(self, "securityServicePolicyData", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="deleteAllPolicyResources")
    def delete_all_policy_resources(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::FMS::Policy.DeleteAllPolicyResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-deleteallpolicyresources
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "deleteAllPolicyResources"))

    @delete_all_policy_resources.setter
    def delete_all_policy_resources(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "deleteAllPolicyResources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="excludeMap")
    def exclude_map(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.IEMapProperty"]]:
        '''``AWS::FMS::Policy.ExcludeMap``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excludemap
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.IEMapProperty"]], jsii.get(self, "excludeMap"))

    @exclude_map.setter
    def exclude_map(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.IEMapProperty"]],
    ) -> None:
        jsii.set(self, "excludeMap", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="includeMap")
    def include_map(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.IEMapProperty"]]:
        '''``AWS::FMS::Policy.IncludeMap``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-includemap
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.IEMapProperty"]], jsii.get(self, "includeMap"))

    @include_map.setter
    def include_map(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.IEMapProperty"]],
    ) -> None:
        jsii.set(self, "includeMap", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.ResourceTagProperty"]]]]:
        '''``AWS::FMS::Policy.ResourceTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetags
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.ResourceTagProperty"]]]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnPolicy.ResourceTagProperty"]]]],
    ) -> None:
        jsii.set(self, "resourceTags", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceTypeList")
    def resource_type_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::FMS::Policy.ResourceTypeList``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetypelist
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceTypeList"))

    @resource_type_list.setter
    def resource_type_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "resourceTypeList", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]]:
        '''``AWS::FMS::Policy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-tags
        '''
        return typing.cast(typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.List["CfnPolicy.PolicyTagProperty"]],
    ) -> None:
        jsii.set(self, "tags", value)

    @jsii.interface(jsii_type="@aws-cdk/aws-fms.CfnPolicy.IEMapProperty")
    class IEMapProperty(typing_extensions.Protocol):
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html
        '''

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="account")
        def account(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPolicy.IEMapProperty.ACCOUNT``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-account
            '''
            ...

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="orgunit")
        def orgunit(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPolicy.IEMapProperty.ORGUNIT``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-orgunit
            '''
            ...


    class _IEMapPropertyProxy:
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html
        '''

        __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-fms.CfnPolicy.IEMapProperty"

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="account")
        def account(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPolicy.IEMapProperty.ACCOUNT``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-account
            '''
            return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "account"))

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="orgunit")
        def orgunit(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnPolicy.IEMapProperty.ORGUNIT``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-iemap.html#cfn-fms-policy-iemap-orgunit
            '''
            return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "orgunit"))

    # Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
    typing.cast(typing.Any, IEMapProperty).__jsii_proxy_class__ = lambda : _IEMapPropertyProxy

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-fms.CfnPolicy.PolicyTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class PolicyTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''
            :param key: ``CfnPolicy.PolicyTagProperty.Key``.
            :param value: ``CfnPolicy.PolicyTagProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnPolicy.PolicyTagProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnPolicy.PolicyTagProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-policytag.html#cfn-fms-policy-policytag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-fms.CfnPolicy.ResourceTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ResourceTagProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key: ``CfnPolicy.ResourceTagProperty.Key``.
            :param value: ``CfnPolicy.ResourceTagProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
            }
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnPolicy.ResourceTagProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''``CfnPolicy.ResourceTagProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-resourcetag.html#cfn-fms-policy-resourcetag-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-fms.CfnPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_resource_tags": "excludeResourceTags",
        "policy_name": "policyName",
        "remediation_enabled": "remediationEnabled",
        "resource_type": "resourceType",
        "security_service_policy_data": "securityServicePolicyData",
        "delete_all_policy_resources": "deleteAllPolicyResources",
        "exclude_map": "excludeMap",
        "include_map": "includeMap",
        "resource_tags": "resourceTags",
        "resource_type_list": "resourceTypeList",
        "tags": "tags",
    },
)
class CfnPolicyProps:
    def __init__(
        self,
        *,
        exclude_resource_tags: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        policy_name: builtins.str,
        remediation_enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        resource_type: builtins.str,
        security_service_policy_data: typing.Any,
        delete_all_policy_resources: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        exclude_map: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPolicy.IEMapProperty]] = None,
        include_map: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPolicy.IEMapProperty]] = None,
        resource_tags: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnPolicy.ResourceTagProperty]]]] = None,
        resource_type_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[CfnPolicy.PolicyTagProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::FMS::Policy``.

        :param exclude_resource_tags: ``AWS::FMS::Policy.ExcludeResourceTags``.
        :param policy_name: ``AWS::FMS::Policy.PolicyName``.
        :param remediation_enabled: ``AWS::FMS::Policy.RemediationEnabled``.
        :param resource_type: ``AWS::FMS::Policy.ResourceType``.
        :param security_service_policy_data: ``AWS::FMS::Policy.SecurityServicePolicyData``.
        :param delete_all_policy_resources: ``AWS::FMS::Policy.DeleteAllPolicyResources``.
        :param exclude_map: ``AWS::FMS::Policy.ExcludeMap``.
        :param include_map: ``AWS::FMS::Policy.IncludeMap``.
        :param resource_tags: ``AWS::FMS::Policy.ResourceTags``.
        :param resource_type_list: ``AWS::FMS::Policy.ResourceTypeList``.
        :param tags: ``AWS::FMS::Policy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "exclude_resource_tags": exclude_resource_tags,
            "policy_name": policy_name,
            "remediation_enabled": remediation_enabled,
            "resource_type": resource_type,
            "security_service_policy_data": security_service_policy_data,
        }
        if delete_all_policy_resources is not None:
            self._values["delete_all_policy_resources"] = delete_all_policy_resources
        if exclude_map is not None:
            self._values["exclude_map"] = exclude_map
        if include_map is not None:
            self._values["include_map"] = include_map
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags
        if resource_type_list is not None:
            self._values["resource_type_list"] = resource_type_list
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def exclude_resource_tags(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::FMS::Policy.ExcludeResourceTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excluderesourcetags
        '''
        result = self._values.get("exclude_resource_tags")
        assert result is not None, "Required property 'exclude_resource_tags' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''``AWS::FMS::Policy.PolicyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-policyname
        '''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def remediation_enabled(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::FMS::Policy.RemediationEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-remediationenabled
        '''
        result = self._values.get("remediation_enabled")
        assert result is not None, "Required property 'remediation_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''``AWS::FMS::Policy.ResourceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetype
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_service_policy_data(self) -> typing.Any:
        '''``AWS::FMS::Policy.SecurityServicePolicyData``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-securityservicepolicydata
        '''
        result = self._values.get("security_service_policy_data")
        assert result is not None, "Required property 'security_service_policy_data' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def delete_all_policy_resources(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::FMS::Policy.DeleteAllPolicyResources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-deleteallpolicyresources
        '''
        result = self._values.get("delete_all_policy_resources")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def exclude_map(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPolicy.IEMapProperty]]:
        '''``AWS::FMS::Policy.ExcludeMap``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-excludemap
        '''
        result = self._values.get("exclude_map")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPolicy.IEMapProperty]], result)

    @builtins.property
    def include_map(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPolicy.IEMapProperty]]:
        '''``AWS::FMS::Policy.IncludeMap``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-includemap
        '''
        result = self._values.get("include_map")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPolicy.IEMapProperty]], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnPolicy.ResourceTagProperty]]]]:
        '''``AWS::FMS::Policy.ResourceTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnPolicy.ResourceTagProperty]]]], result)

    @builtins.property
    def resource_type_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::FMS::Policy.ResourceTypeList``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-resourcetypelist
        '''
        result = self._values.get("resource_type_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnPolicy.PolicyTagProperty]]:
        '''``AWS::FMS::Policy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html#cfn-fms-policy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnPolicy.PolicyTagProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNotificationChannel",
    "CfnNotificationChannelProps",
    "CfnPolicy",
    "CfnPolicyProps",
]

publication.publish()
