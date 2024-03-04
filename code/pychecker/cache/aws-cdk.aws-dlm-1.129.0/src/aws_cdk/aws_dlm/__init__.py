'''
# Amazon Data Lifecycle Manager Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_dlm as dlm
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
class CfnLifecyclePolicy(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy",
):
    '''A CloudFormation ``AWS::DLM::LifecyclePolicy``.

    :cloudformationResource: AWS::DLM::LifecyclePolicy
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        policy_details: typing.Optional[typing.Union["CfnLifecyclePolicy.PolicyDetailsProperty", aws_cdk.core.IResolvable]] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::DLM::LifecyclePolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param description: ``AWS::DLM::LifecyclePolicy.Description``.
        :param execution_role_arn: ``AWS::DLM::LifecyclePolicy.ExecutionRoleArn``.
        :param policy_details: ``AWS::DLM::LifecyclePolicy.PolicyDetails``.
        :param state: ``AWS::DLM::LifecyclePolicy.State``.
        :param tags: ``AWS::DLM::LifecyclePolicy.Tags``.
        '''
        props = CfnLifecyclePolicyProps(
            description=description,
            execution_role_arn=execution_role_arn,
            policy_details=policy_details,
            state=state,
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
        '''``AWS::DLM::LifecyclePolicy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::DLM::LifecyclePolicy.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::DLM::LifecyclePolicy.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-executionrolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "executionRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="policyDetails")
    def policy_details(
        self,
    ) -> typing.Optional[typing.Union["CfnLifecyclePolicy.PolicyDetailsProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::DLM::LifecyclePolicy.PolicyDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-policydetails
        '''
        return typing.cast(typing.Optional[typing.Union["CfnLifecyclePolicy.PolicyDetailsProperty", aws_cdk.core.IResolvable]], jsii.get(self, "policyDetails"))

    @policy_details.setter
    def policy_details(
        self,
        value: typing.Optional[typing.Union["CfnLifecyclePolicy.PolicyDetailsProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "policyDetails", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''``AWS::DLM::LifecyclePolicy.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-state
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "state", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"cross_region_copy": "crossRegionCopy", "name": "name"},
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            cross_region_copy: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyActionProperty"]]],
            name: builtins.str,
        ) -> None:
            '''
            :param cross_region_copy: ``CfnLifecyclePolicy.ActionProperty.CrossRegionCopy``.
            :param name: ``CfnLifecyclePolicy.ActionProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cross_region_copy": cross_region_copy,
                "name": name,
            }

        @builtins.property
        def cross_region_copy(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyActionProperty"]]]:
            '''``CfnLifecyclePolicy.ActionProperty.CrossRegionCopy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html#cfn-dlm-lifecyclepolicy-action-crossregioncopy
            '''
            result = self._values.get("cross_region_copy")
            assert result is not None, "Required property 'cross_region_copy' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyActionProperty"]]], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnLifecyclePolicy.ActionProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html#cfn-dlm-lifecyclepolicy-action-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.CreateRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cron_expression": "cronExpression",
            "interval": "interval",
            "interval_unit": "intervalUnit",
            "location": "location",
            "times": "times",
        },
    )
    class CreateRuleProperty:
        def __init__(
            self,
            *,
            cron_expression: typing.Optional[builtins.str] = None,
            interval: typing.Optional[jsii.Number] = None,
            interval_unit: typing.Optional[builtins.str] = None,
            location: typing.Optional[builtins.str] = None,
            times: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param cron_expression: ``CfnLifecyclePolicy.CreateRuleProperty.CronExpression``.
            :param interval: ``CfnLifecyclePolicy.CreateRuleProperty.Interval``.
            :param interval_unit: ``CfnLifecyclePolicy.CreateRuleProperty.IntervalUnit``.
            :param location: ``CfnLifecyclePolicy.CreateRuleProperty.Location``.
            :param times: ``CfnLifecyclePolicy.CreateRuleProperty.Times``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cron_expression is not None:
                self._values["cron_expression"] = cron_expression
            if interval is not None:
                self._values["interval"] = interval
            if interval_unit is not None:
                self._values["interval_unit"] = interval_unit
            if location is not None:
                self._values["location"] = location
            if times is not None:
                self._values["times"] = times

        @builtins.property
        def cron_expression(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.CreateRuleProperty.CronExpression``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-cronexpression
            '''
            result = self._values.get("cron_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnLifecyclePolicy.CreateRuleProperty.Interval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval_unit(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.CreateRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-intervalunit
            '''
            result = self._values.get("interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def location(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.CreateRuleProperty.Location``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-location
            '''
            result = self._values.get("location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def times(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnLifecyclePolicy.CreateRuleProperty.Times``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-times
            '''
            result = self._values.get("times")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreateRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.CrossRegionCopyActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_configuration": "encryptionConfiguration",
            "target": "target",
            "retain_rule": "retainRule",
        },
    )
    class CrossRegionCopyActionProperty:
        def __init__(
            self,
            *,
            encryption_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.EncryptionConfigurationProperty"],
            target: builtins.str,
            retain_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty"]] = None,
        ) -> None:
            '''
            :param encryption_configuration: ``CfnLifecyclePolicy.CrossRegionCopyActionProperty.EncryptionConfiguration``.
            :param target: ``CfnLifecyclePolicy.CrossRegionCopyActionProperty.Target``.
            :param retain_rule: ``CfnLifecyclePolicy.CrossRegionCopyActionProperty.RetainRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "encryption_configuration": encryption_configuration,
                "target": target,
            }
            if retain_rule is not None:
                self._values["retain_rule"] = retain_rule

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.EncryptionConfigurationProperty"]:
            '''``CfnLifecyclePolicy.CrossRegionCopyActionProperty.EncryptionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            assert result is not None, "Required property 'encryption_configuration' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.EncryptionConfigurationProperty"], result)

        @builtins.property
        def target(self) -> builtins.str:
            '''``CfnLifecyclePolicy.CrossRegionCopyActionProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def retain_rule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty"]]:
            '''``CfnLifecyclePolicy.CrossRegionCopyActionProperty.RetainRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-retainrule
            '''
            result = self._values.get("retain_rule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrossRegionCopyActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"interval": "interval", "interval_unit": "intervalUnit"},
    )
    class CrossRegionCopyDeprecateRuleProperty:
        def __init__(
            self,
            *,
            interval: jsii.Number,
            interval_unit: builtins.str,
        ) -> None:
            '''
            :param interval: ``CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty.Interval``.
            :param interval_unit: ``CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "interval": interval,
                "interval_unit": interval_unit,
            }

        @builtins.property
        def interval(self) -> jsii.Number:
            '''``CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty.Interval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-interval
            '''
            result = self._values.get("interval")
            assert result is not None, "Required property 'interval' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def interval_unit(self) -> builtins.str:
            '''``CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-intervalunit
            '''
            result = self._values.get("interval_unit")
            assert result is not None, "Required property 'interval_unit' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrossRegionCopyDeprecateRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"interval": "interval", "interval_unit": "intervalUnit"},
    )
    class CrossRegionCopyRetainRuleProperty:
        def __init__(
            self,
            *,
            interval: jsii.Number,
            interval_unit: builtins.str,
        ) -> None:
            '''
            :param interval: ``CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty.Interval``.
            :param interval_unit: ``CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "interval": interval,
                "interval_unit": interval_unit,
            }

        @builtins.property
        def interval(self) -> jsii.Number:
            '''``CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty.Interval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyretainrule-interval
            '''
            result = self._values.get("interval")
            assert result is not None, "Required property 'interval' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def interval_unit(self) -> builtins.str:
            '''``CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyretainrule-intervalunit
            '''
            result = self._values.get("interval_unit")
            assert result is not None, "Required property 'interval_unit' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrossRegionCopyRetainRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.CrossRegionCopyRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encrypted": "encrypted",
            "cmk_arn": "cmkArn",
            "copy_tags": "copyTags",
            "deprecate_rule": "deprecateRule",
            "retain_rule": "retainRule",
            "target": "target",
            "target_region": "targetRegion",
        },
    )
    class CrossRegionCopyRuleProperty:
        def __init__(
            self,
            *,
            encrypted: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            cmk_arn: typing.Optional[builtins.str] = None,
            copy_tags: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            deprecate_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty"]] = None,
            retain_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty"]] = None,
            target: typing.Optional[builtins.str] = None,
            target_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param encrypted: ``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.Encrypted``.
            :param cmk_arn: ``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.CmkArn``.
            :param copy_tags: ``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.CopyTags``.
            :param deprecate_rule: ``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.DeprecateRule``.
            :param retain_rule: ``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.RetainRule``.
            :param target: ``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.Target``.
            :param target_region: ``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.TargetRegion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "encrypted": encrypted,
            }
            if cmk_arn is not None:
                self._values["cmk_arn"] = cmk_arn
            if copy_tags is not None:
                self._values["copy_tags"] = copy_tags
            if deprecate_rule is not None:
                self._values["deprecate_rule"] = deprecate_rule
            if retain_rule is not None:
                self._values["retain_rule"] = retain_rule
            if target is not None:
                self._values["target"] = target
            if target_region is not None:
                self._values["target_region"] = target_region

        @builtins.property
        def encrypted(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.Encrypted``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-encrypted
            '''
            result = self._values.get("encrypted")
            assert result is not None, "Required property 'encrypted' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        @builtins.property
        def cmk_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.CmkArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-cmkarn
            '''
            result = self._values.get("cmk_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def copy_tags(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.CopyTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-copytags
            '''
            result = self._values.get("copy_tags")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def deprecate_rule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty"]]:
            '''``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.DeprecateRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-deprecaterule
            '''
            result = self._values.get("deprecate_rule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty"]], result)

        @builtins.property
        def retain_rule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty"]]:
            '''``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.RetainRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-retainrule
            '''
            result = self._values.get("retain_rule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty"]], result)

        @builtins.property
        def target(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.Target``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_region(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.CrossRegionCopyRuleProperty.TargetRegion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-targetregion
            '''
            result = self._values.get("target_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrossRegionCopyRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.DeprecateRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "count": "count",
            "interval": "interval",
            "interval_unit": "intervalUnit",
        },
    )
    class DeprecateRuleProperty:
        def __init__(
            self,
            *,
            count: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            interval_unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param count: ``CfnLifecyclePolicy.DeprecateRuleProperty.Count``.
            :param interval: ``CfnLifecyclePolicy.DeprecateRuleProperty.Interval``.
            :param interval_unit: ``CfnLifecyclePolicy.DeprecateRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if count is not None:
                self._values["count"] = count
            if interval is not None:
                self._values["interval"] = interval
            if interval_unit is not None:
                self._values["interval_unit"] = interval_unit

        @builtins.property
        def count(self) -> typing.Optional[jsii.Number]:
            '''``CfnLifecyclePolicy.DeprecateRuleProperty.Count``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnLifecyclePolicy.DeprecateRuleProperty.Interval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval_unit(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.DeprecateRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-intervalunit
            '''
            result = self._values.get("interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeprecateRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"encrypted": "encrypted", "cmk_arn": "cmkArn"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encrypted: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            cmk_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param encrypted: ``CfnLifecyclePolicy.EncryptionConfigurationProperty.Encrypted``.
            :param cmk_arn: ``CfnLifecyclePolicy.EncryptionConfigurationProperty.CmkArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "encrypted": encrypted,
            }
            if cmk_arn is not None:
                self._values["cmk_arn"] = cmk_arn

        @builtins.property
        def encrypted(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnLifecyclePolicy.EncryptionConfigurationProperty.Encrypted``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html#cfn-dlm-lifecyclepolicy-encryptionconfiguration-encrypted
            '''
            result = self._values.get("encrypted")
            assert result is not None, "Required property 'encrypted' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        @builtins.property
        def cmk_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.EncryptionConfigurationProperty.CmkArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html#cfn-dlm-lifecyclepolicy-encryptionconfiguration-cmkarn
            '''
            result = self._values.get("cmk_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.EventParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_type": "eventType",
            "snapshot_owner": "snapshotOwner",
            "description_regex": "descriptionRegex",
        },
    )
    class EventParametersProperty:
        def __init__(
            self,
            *,
            event_type: builtins.str,
            snapshot_owner: typing.Sequence[builtins.str],
            description_regex: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param event_type: ``CfnLifecyclePolicy.EventParametersProperty.EventType``.
            :param snapshot_owner: ``CfnLifecyclePolicy.EventParametersProperty.SnapshotOwner``.
            :param description_regex: ``CfnLifecyclePolicy.EventParametersProperty.DescriptionRegex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "event_type": event_type,
                "snapshot_owner": snapshot_owner,
            }
            if description_regex is not None:
                self._values["description_regex"] = description_regex

        @builtins.property
        def event_type(self) -> builtins.str:
            '''``CfnLifecyclePolicy.EventParametersProperty.EventType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-eventtype
            '''
            result = self._values.get("event_type")
            assert result is not None, "Required property 'event_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def snapshot_owner(self) -> typing.List[builtins.str]:
            '''``CfnLifecyclePolicy.EventParametersProperty.SnapshotOwner``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-snapshotowner
            '''
            result = self._values.get("snapshot_owner")
            assert result is not None, "Required property 'snapshot_owner' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def description_regex(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.EventParametersProperty.DescriptionRegex``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-descriptionregex
            '''
            result = self._values.get("description_regex")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.EventSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "parameters": "parameters"},
    )
    class EventSourceProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.EventParametersProperty"]] = None,
        ) -> None:
            '''
            :param type: ``CfnLifecyclePolicy.EventSourceProperty.Type``.
            :param parameters: ``CfnLifecyclePolicy.EventSourceProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnLifecyclePolicy.EventSourceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html#cfn-dlm-lifecyclepolicy-eventsource-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.EventParametersProperty"]]:
            '''``CfnLifecyclePolicy.EventSourceProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html#cfn-dlm-lifecyclepolicy-eventsource-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.EventParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.FastRestoreRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zones": "availabilityZones",
            "count": "count",
            "interval": "interval",
            "interval_unit": "intervalUnit",
        },
    )
    class FastRestoreRuleProperty:
        def __init__(
            self,
            *,
            availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
            count: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            interval_unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param availability_zones: ``CfnLifecyclePolicy.FastRestoreRuleProperty.AvailabilityZones``.
            :param count: ``CfnLifecyclePolicy.FastRestoreRuleProperty.Count``.
            :param interval: ``CfnLifecyclePolicy.FastRestoreRuleProperty.Interval``.
            :param interval_unit: ``CfnLifecyclePolicy.FastRestoreRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if availability_zones is not None:
                self._values["availability_zones"] = availability_zones
            if count is not None:
                self._values["count"] = count
            if interval is not None:
                self._values["interval"] = interval
            if interval_unit is not None:
                self._values["interval_unit"] = interval_unit

        @builtins.property
        def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnLifecyclePolicy.FastRestoreRuleProperty.AvailabilityZones``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzones
            '''
            result = self._values.get("availability_zones")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def count(self) -> typing.Optional[jsii.Number]:
            '''``CfnLifecyclePolicy.FastRestoreRuleProperty.Count``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnLifecyclePolicy.FastRestoreRuleProperty.Interval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval_unit(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.FastRestoreRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-intervalunit
            '''
            result = self._values.get("interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FastRestoreRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.ParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exclude_boot_volume": "excludeBootVolume",
            "no_reboot": "noReboot",
        },
    )
    class ParametersProperty:
        def __init__(
            self,
            *,
            exclude_boot_volume: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            no_reboot: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param exclude_boot_volume: ``CfnLifecyclePolicy.ParametersProperty.ExcludeBootVolume``.
            :param no_reboot: ``CfnLifecyclePolicy.ParametersProperty.NoReboot``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if exclude_boot_volume is not None:
                self._values["exclude_boot_volume"] = exclude_boot_volume
            if no_reboot is not None:
                self._values["no_reboot"] = no_reboot

        @builtins.property
        def exclude_boot_volume(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnLifecyclePolicy.ParametersProperty.ExcludeBootVolume``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-excludebootvolume
            '''
            result = self._values.get("exclude_boot_volume")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def no_reboot(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnLifecyclePolicy.ParametersProperty.NoReboot``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-noreboot
            '''
            result = self._values.get("no_reboot")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.PolicyDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actions": "actions",
            "event_source": "eventSource",
            "parameters": "parameters",
            "policy_type": "policyType",
            "resource_locations": "resourceLocations",
            "resource_types": "resourceTypes",
            "schedules": "schedules",
            "target_tags": "targetTags",
        },
    )
    class PolicyDetailsProperty:
        def __init__(
            self,
            *,
            actions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ActionProperty"]]]] = None,
            event_source: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.EventSourceProperty"]] = None,
            parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ParametersProperty"]] = None,
            policy_type: typing.Optional[builtins.str] = None,
            resource_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            schedules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ScheduleProperty"]]]] = None,
            target_tags: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]] = None,
        ) -> None:
            '''
            :param actions: ``CfnLifecyclePolicy.PolicyDetailsProperty.Actions``.
            :param event_source: ``CfnLifecyclePolicy.PolicyDetailsProperty.EventSource``.
            :param parameters: ``CfnLifecyclePolicy.PolicyDetailsProperty.Parameters``.
            :param policy_type: ``CfnLifecyclePolicy.PolicyDetailsProperty.PolicyType``.
            :param resource_locations: ``CfnLifecyclePolicy.PolicyDetailsProperty.ResourceLocations``.
            :param resource_types: ``CfnLifecyclePolicy.PolicyDetailsProperty.ResourceTypes``.
            :param schedules: ``CfnLifecyclePolicy.PolicyDetailsProperty.Schedules``.
            :param target_tags: ``CfnLifecyclePolicy.PolicyDetailsProperty.TargetTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if actions is not None:
                self._values["actions"] = actions
            if event_source is not None:
                self._values["event_source"] = event_source
            if parameters is not None:
                self._values["parameters"] = parameters
            if policy_type is not None:
                self._values["policy_type"] = policy_type
            if resource_locations is not None:
                self._values["resource_locations"] = resource_locations
            if resource_types is not None:
                self._values["resource_types"] = resource_types
            if schedules is not None:
                self._values["schedules"] = schedules
            if target_tags is not None:
                self._values["target_tags"] = target_tags

        @builtins.property
        def actions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ActionProperty"]]]]:
            '''``CfnLifecyclePolicy.PolicyDetailsProperty.Actions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-actions
            '''
            result = self._values.get("actions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ActionProperty"]]]], result)

        @builtins.property
        def event_source(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.EventSourceProperty"]]:
            '''``CfnLifecyclePolicy.PolicyDetailsProperty.EventSource``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-eventsource
            '''
            result = self._values.get("event_source")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.EventSourceProperty"]], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ParametersProperty"]]:
            '''``CfnLifecyclePolicy.PolicyDetailsProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ParametersProperty"]], result)

        @builtins.property
        def policy_type(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.PolicyDetailsProperty.PolicyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-policytype
            '''
            result = self._values.get("policy_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_locations(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnLifecyclePolicy.PolicyDetailsProperty.ResourceLocations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcelocations
            '''
            result = self._values.get("resource_locations")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnLifecyclePolicy.PolicyDetailsProperty.ResourceTypes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcetypes
            '''
            result = self._values.get("resource_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def schedules(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ScheduleProperty"]]]]:
            '''``CfnLifecyclePolicy.PolicyDetailsProperty.Schedules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-schedules
            '''
            result = self._values.get("schedules")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ScheduleProperty"]]]], result)

        @builtins.property
        def target_tags(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]:
            '''``CfnLifecyclePolicy.PolicyDetailsProperty.TargetTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-targettags
            '''
            result = self._values.get("target_tags")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.RetainRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "count": "count",
            "interval": "interval",
            "interval_unit": "intervalUnit",
        },
    )
    class RetainRuleProperty:
        def __init__(
            self,
            *,
            count: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            interval_unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param count: ``CfnLifecyclePolicy.RetainRuleProperty.Count``.
            :param interval: ``CfnLifecyclePolicy.RetainRuleProperty.Interval``.
            :param interval_unit: ``CfnLifecyclePolicy.RetainRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if count is not None:
                self._values["count"] = count
            if interval is not None:
                self._values["interval"] = interval
            if interval_unit is not None:
                self._values["interval_unit"] = interval_unit

        @builtins.property
        def count(self) -> typing.Optional[jsii.Number]:
            '''``CfnLifecyclePolicy.RetainRuleProperty.Count``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnLifecyclePolicy.RetainRuleProperty.Interval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval_unit(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.RetainRuleProperty.IntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-intervalunit
            '''
            result = self._values.get("interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetainRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "copy_tags": "copyTags",
            "create_rule": "createRule",
            "cross_region_copy_rules": "crossRegionCopyRules",
            "deprecate_rule": "deprecateRule",
            "fast_restore_rule": "fastRestoreRule",
            "name": "name",
            "retain_rule": "retainRule",
            "share_rules": "shareRules",
            "tags_to_add": "tagsToAdd",
            "variable_tags": "variableTags",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            copy_tags: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            create_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CreateRuleProperty"]] = None,
            cross_region_copy_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyRuleProperty"]]]] = None,
            deprecate_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.DeprecateRuleProperty"]] = None,
            fast_restore_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.FastRestoreRuleProperty"]] = None,
            name: typing.Optional[builtins.str] = None,
            retain_rule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.RetainRuleProperty"]] = None,
            share_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ShareRuleProperty"]]]] = None,
            tags_to_add: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]] = None,
            variable_tags: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]] = None,
        ) -> None:
            '''
            :param copy_tags: ``CfnLifecyclePolicy.ScheduleProperty.CopyTags``.
            :param create_rule: ``CfnLifecyclePolicy.ScheduleProperty.CreateRule``.
            :param cross_region_copy_rules: ``CfnLifecyclePolicy.ScheduleProperty.CrossRegionCopyRules``.
            :param deprecate_rule: ``CfnLifecyclePolicy.ScheduleProperty.DeprecateRule``.
            :param fast_restore_rule: ``CfnLifecyclePolicy.ScheduleProperty.FastRestoreRule``.
            :param name: ``CfnLifecyclePolicy.ScheduleProperty.Name``.
            :param retain_rule: ``CfnLifecyclePolicy.ScheduleProperty.RetainRule``.
            :param share_rules: ``CfnLifecyclePolicy.ScheduleProperty.ShareRules``.
            :param tags_to_add: ``CfnLifecyclePolicy.ScheduleProperty.TagsToAdd``.
            :param variable_tags: ``CfnLifecyclePolicy.ScheduleProperty.VariableTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if copy_tags is not None:
                self._values["copy_tags"] = copy_tags
            if create_rule is not None:
                self._values["create_rule"] = create_rule
            if cross_region_copy_rules is not None:
                self._values["cross_region_copy_rules"] = cross_region_copy_rules
            if deprecate_rule is not None:
                self._values["deprecate_rule"] = deprecate_rule
            if fast_restore_rule is not None:
                self._values["fast_restore_rule"] = fast_restore_rule
            if name is not None:
                self._values["name"] = name
            if retain_rule is not None:
                self._values["retain_rule"] = retain_rule
            if share_rules is not None:
                self._values["share_rules"] = share_rules
            if tags_to_add is not None:
                self._values["tags_to_add"] = tags_to_add
            if variable_tags is not None:
                self._values["variable_tags"] = variable_tags

        @builtins.property
        def copy_tags(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnLifecyclePolicy.ScheduleProperty.CopyTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-copytags
            '''
            result = self._values.get("copy_tags")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def create_rule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CreateRuleProperty"]]:
            '''``CfnLifecyclePolicy.ScheduleProperty.CreateRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-createrule
            '''
            result = self._values.get("create_rule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CreateRuleProperty"]], result)

        @builtins.property
        def cross_region_copy_rules(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyRuleProperty"]]]]:
            '''``CfnLifecyclePolicy.ScheduleProperty.CrossRegionCopyRules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-crossregioncopyrules
            '''
            result = self._values.get("cross_region_copy_rules")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.CrossRegionCopyRuleProperty"]]]], result)

        @builtins.property
        def deprecate_rule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.DeprecateRuleProperty"]]:
            '''``CfnLifecyclePolicy.ScheduleProperty.DeprecateRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-deprecaterule
            '''
            result = self._values.get("deprecate_rule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.DeprecateRuleProperty"]], result)

        @builtins.property
        def fast_restore_rule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.FastRestoreRuleProperty"]]:
            '''``CfnLifecyclePolicy.ScheduleProperty.FastRestoreRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-fastrestorerule
            '''
            result = self._values.get("fast_restore_rule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.FastRestoreRuleProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.ScheduleProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def retain_rule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.RetainRuleProperty"]]:
            '''``CfnLifecyclePolicy.ScheduleProperty.RetainRule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-retainrule
            '''
            result = self._values.get("retain_rule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.RetainRuleProperty"]], result)

        @builtins.property
        def share_rules(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ShareRuleProperty"]]]]:
            '''``CfnLifecyclePolicy.ScheduleProperty.ShareRules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-sharerules
            '''
            result = self._values.get("share_rules")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLifecyclePolicy.ShareRuleProperty"]]]], result)

        @builtins.property
        def tags_to_add(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]:
            '''``CfnLifecyclePolicy.ScheduleProperty.TagsToAdd``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-tagstoadd
            '''
            result = self._values.get("tags_to_add")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]], result)

        @builtins.property
        def variable_tags(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]]:
            '''``CfnLifecyclePolicy.ScheduleProperty.VariableTags``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-variabletags
            '''
            result = self._values.get("variable_tags")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, aws_cdk.core.CfnTag]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicy.ShareRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_accounts": "targetAccounts",
            "unshare_interval": "unshareInterval",
            "unshare_interval_unit": "unshareIntervalUnit",
        },
    )
    class ShareRuleProperty:
        def __init__(
            self,
            *,
            target_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            unshare_interval: typing.Optional[jsii.Number] = None,
            unshare_interval_unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param target_accounts: ``CfnLifecyclePolicy.ShareRuleProperty.TargetAccounts``.
            :param unshare_interval: ``CfnLifecyclePolicy.ShareRuleProperty.UnshareInterval``.
            :param unshare_interval_unit: ``CfnLifecyclePolicy.ShareRuleProperty.UnshareIntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if target_accounts is not None:
                self._values["target_accounts"] = target_accounts
            if unshare_interval is not None:
                self._values["unshare_interval"] = unshare_interval
            if unshare_interval_unit is not None:
                self._values["unshare_interval_unit"] = unshare_interval_unit

        @builtins.property
        def target_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnLifecyclePolicy.ShareRuleProperty.TargetAccounts``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-targetaccounts
            '''
            result = self._values.get("target_accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def unshare_interval(self) -> typing.Optional[jsii.Number]:
            '''``CfnLifecyclePolicy.ShareRuleProperty.UnshareInterval``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-unshareinterval
            '''
            result = self._values.get("unshare_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unshare_interval_unit(self) -> typing.Optional[builtins.str]:
            '''``CfnLifecyclePolicy.ShareRuleProperty.UnshareIntervalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-unshareintervalunit
            '''
            result = self._values.get("unshare_interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ShareRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-dlm.CfnLifecyclePolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "execution_role_arn": "executionRoleArn",
        "policy_details": "policyDetails",
        "state": "state",
        "tags": "tags",
    },
)
class CfnLifecyclePolicyProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        policy_details: typing.Optional[typing.Union[CfnLifecyclePolicy.PolicyDetailsProperty, aws_cdk.core.IResolvable]] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::DLM::LifecyclePolicy``.

        :param description: ``AWS::DLM::LifecyclePolicy.Description``.
        :param execution_role_arn: ``AWS::DLM::LifecyclePolicy.ExecutionRoleArn``.
        :param policy_details: ``AWS::DLM::LifecyclePolicy.PolicyDetails``.
        :param state: ``AWS::DLM::LifecyclePolicy.State``.
        :param tags: ``AWS::DLM::LifecyclePolicy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if policy_details is not None:
            self._values["policy_details"] = policy_details
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::DLM::LifecyclePolicy.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::DLM::LifecyclePolicy.ExecutionRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_details(
        self,
    ) -> typing.Optional[typing.Union[CfnLifecyclePolicy.PolicyDetailsProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::DLM::LifecyclePolicy.PolicyDetails``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-policydetails
        '''
        result = self._values.get("policy_details")
        return typing.cast(typing.Optional[typing.Union[CfnLifecyclePolicy.PolicyDetailsProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''``AWS::DLM::LifecyclePolicy.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::DLM::LifecyclePolicy.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLifecyclePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLifecyclePolicy",
    "CfnLifecyclePolicyProps",
]

publication.publish()
