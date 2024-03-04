'''
# Amazon Inspector Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.
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
class CfnAssessmentTarget(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-inspector.CfnAssessmentTarget",
):
    '''A CloudFormation ``AWS::Inspector::AssessmentTarget``.

    :cloudformationResource: AWS::Inspector::AssessmentTarget
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        assessment_target_name: typing.Optional[builtins.str] = None,
        resource_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Inspector::AssessmentTarget``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param assessment_target_name: ``AWS::Inspector::AssessmentTarget.AssessmentTargetName``.
        :param resource_group_arn: ``AWS::Inspector::AssessmentTarget.ResourceGroupArn``.
        '''
        props = CfnAssessmentTargetProps(
            assessment_target_name=assessment_target_name,
            resource_group_arn=resource_group_arn,
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
    @jsii.member(jsii_name="assessmentTargetName")
    def assessment_target_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Inspector::AssessmentTarget.AssessmentTargetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html#cfn-inspector-assessmenttarget-assessmenttargetname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assessmentTargetName"))

    @assessment_target_name.setter
    def assessment_target_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "assessmentTargetName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceGroupArn")
    def resource_group_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Inspector::AssessmentTarget.ResourceGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html#cfn-inspector-assessmenttarget-resourcegrouparn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupArn"))

    @resource_group_arn.setter
    def resource_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "resourceGroupArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-inspector.CfnAssessmentTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "assessment_target_name": "assessmentTargetName",
        "resource_group_arn": "resourceGroupArn",
    },
)
class CfnAssessmentTargetProps:
    def __init__(
        self,
        *,
        assessment_target_name: typing.Optional[builtins.str] = None,
        resource_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Inspector::AssessmentTarget``.

        :param assessment_target_name: ``AWS::Inspector::AssessmentTarget.AssessmentTargetName``.
        :param resource_group_arn: ``AWS::Inspector::AssessmentTarget.ResourceGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if assessment_target_name is not None:
            self._values["assessment_target_name"] = assessment_target_name
        if resource_group_arn is not None:
            self._values["resource_group_arn"] = resource_group_arn

    @builtins.property
    def assessment_target_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Inspector::AssessmentTarget.AssessmentTargetName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html#cfn-inspector-assessmenttarget-assessmenttargetname
        '''
        result = self._values.get("assessment_target_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_group_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Inspector::AssessmentTarget.ResourceGroupArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html#cfn-inspector-assessmenttarget-resourcegrouparn
        '''
        result = self._values.get("resource_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssessmentTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAssessmentTemplate(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-inspector.CfnAssessmentTemplate",
):
    '''A CloudFormation ``AWS::Inspector::AssessmentTemplate``.

    :cloudformationResource: AWS::Inspector::AssessmentTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        assessment_target_arn: builtins.str,
        duration_in_seconds: jsii.Number,
        rules_package_arns: typing.Sequence[builtins.str],
        assessment_template_name: typing.Optional[builtins.str] = None,
        user_attributes_for_findings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Inspector::AssessmentTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param assessment_target_arn: ``AWS::Inspector::AssessmentTemplate.AssessmentTargetArn``.
        :param duration_in_seconds: ``AWS::Inspector::AssessmentTemplate.DurationInSeconds``.
        :param rules_package_arns: ``AWS::Inspector::AssessmentTemplate.RulesPackageArns``.
        :param assessment_template_name: ``AWS::Inspector::AssessmentTemplate.AssessmentTemplateName``.
        :param user_attributes_for_findings: ``AWS::Inspector::AssessmentTemplate.UserAttributesForFindings``.
        '''
        props = CfnAssessmentTemplateProps(
            assessment_target_arn=assessment_target_arn,
            duration_in_seconds=duration_in_seconds,
            rules_package_arns=rules_package_arns,
            assessment_template_name=assessment_template_name,
            user_attributes_for_findings=user_attributes_for_findings,
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
    @jsii.member(jsii_name="assessmentTargetArn")
    def assessment_target_arn(self) -> builtins.str:
        '''``AWS::Inspector::AssessmentTemplate.AssessmentTargetArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-assessmenttargetarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "assessmentTargetArn"))

    @assessment_target_arn.setter
    def assessment_target_arn(self, value: builtins.str) -> None:
        jsii.set(self, "assessmentTargetArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="durationInSeconds")
    def duration_in_seconds(self) -> jsii.Number:
        '''``AWS::Inspector::AssessmentTemplate.DurationInSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-durationinseconds
        '''
        return typing.cast(jsii.Number, jsii.get(self, "durationInSeconds"))

    @duration_in_seconds.setter
    def duration_in_seconds(self, value: jsii.Number) -> None:
        jsii.set(self, "durationInSeconds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rulesPackageArns")
    def rules_package_arns(self) -> typing.List[builtins.str]:
        '''``AWS::Inspector::AssessmentTemplate.RulesPackageArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-rulespackagearns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rulesPackageArns"))

    @rules_package_arns.setter
    def rules_package_arns(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "rulesPackageArns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="assessmentTemplateName")
    def assessment_template_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Inspector::AssessmentTemplate.AssessmentTemplateName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-assessmenttemplatename
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assessmentTemplateName"))

    @assessment_template_name.setter
    def assessment_template_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "assessmentTemplateName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="userAttributesForFindings")
    def user_attributes_for_findings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]]]:
        '''``AWS::Inspector::AssessmentTemplate.UserAttributesForFindings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-userattributesforfindings
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]]], jsii.get(self, "userAttributesForFindings"))

    @user_attributes_for_findings.setter
    def user_attributes_for_findings(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "userAttributesForFindings", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-inspector.CfnAssessmentTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "assessment_target_arn": "assessmentTargetArn",
        "duration_in_seconds": "durationInSeconds",
        "rules_package_arns": "rulesPackageArns",
        "assessment_template_name": "assessmentTemplateName",
        "user_attributes_for_findings": "userAttributesForFindings",
    },
)
class CfnAssessmentTemplateProps:
    def __init__(
        self,
        *,
        assessment_target_arn: builtins.str,
        duration_in_seconds: jsii.Number,
        rules_package_arns: typing.Sequence[builtins.str],
        assessment_template_name: typing.Optional[builtins.str] = None,
        user_attributes_for_findings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Inspector::AssessmentTemplate``.

        :param assessment_target_arn: ``AWS::Inspector::AssessmentTemplate.AssessmentTargetArn``.
        :param duration_in_seconds: ``AWS::Inspector::AssessmentTemplate.DurationInSeconds``.
        :param rules_package_arns: ``AWS::Inspector::AssessmentTemplate.RulesPackageArns``.
        :param assessment_template_name: ``AWS::Inspector::AssessmentTemplate.AssessmentTemplateName``.
        :param user_attributes_for_findings: ``AWS::Inspector::AssessmentTemplate.UserAttributesForFindings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "assessment_target_arn": assessment_target_arn,
            "duration_in_seconds": duration_in_seconds,
            "rules_package_arns": rules_package_arns,
        }
        if assessment_template_name is not None:
            self._values["assessment_template_name"] = assessment_template_name
        if user_attributes_for_findings is not None:
            self._values["user_attributes_for_findings"] = user_attributes_for_findings

    @builtins.property
    def assessment_target_arn(self) -> builtins.str:
        '''``AWS::Inspector::AssessmentTemplate.AssessmentTargetArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-assessmenttargetarn
        '''
        result = self._values.get("assessment_target_arn")
        assert result is not None, "Required property 'assessment_target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration_in_seconds(self) -> jsii.Number:
        '''``AWS::Inspector::AssessmentTemplate.DurationInSeconds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-durationinseconds
        '''
        result = self._values.get("duration_in_seconds")
        assert result is not None, "Required property 'duration_in_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rules_package_arns(self) -> typing.List[builtins.str]:
        '''``AWS::Inspector::AssessmentTemplate.RulesPackageArns``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-rulespackagearns
        '''
        result = self._values.get("rules_package_arns")
        assert result is not None, "Required property 'rules_package_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def assessment_template_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Inspector::AssessmentTemplate.AssessmentTemplateName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-assessmenttemplatename
        '''
        result = self._values.get("assessment_template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_attributes_for_findings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]]]:
        '''``AWS::Inspector::AssessmentTemplate.UserAttributesForFindings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-userattributesforfindings
        '''
        result = self._values.get("user_attributes_for_findings")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssessmentTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnResourceGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-inspector.CfnResourceGroup",
):
    '''A CloudFormation ``AWS::Inspector::ResourceGroup``.

    :cloudformationResource: AWS::Inspector::ResourceGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resource_group_tags: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]],
    ) -> None:
        '''Create a new ``AWS::Inspector::ResourceGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_group_tags: ``AWS::Inspector::ResourceGroup.ResourceGroupTags``.
        '''
        props = CfnResourceGroupProps(resource_group_tags=resource_group_tags)

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
    @jsii.member(jsii_name="resourceGroupTags")
    def resource_group_tags(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]]:
        '''``AWS::Inspector::ResourceGroup.ResourceGroupTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html#cfn-inspector-resourcegroup-resourcegrouptags
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]], jsii.get(self, "resourceGroupTags"))

    @resource_group_tags.setter
    def resource_group_tags(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]],
    ) -> None:
        jsii.set(self, "resourceGroupTags", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-inspector.CfnResourceGroupProps",
    jsii_struct_bases=[],
    name_mapping={"resource_group_tags": "resourceGroupTags"},
)
class CfnResourceGroupProps:
    def __init__(
        self,
        *,
        resource_group_tags: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]],
    ) -> None:
        '''Properties for defining a ``AWS::Inspector::ResourceGroup``.

        :param resource_group_tags: ``AWS::Inspector::ResourceGroup.ResourceGroupTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource_group_tags": resource_group_tags,
        }

    @builtins.property
    def resource_group_tags(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]]:
        '''``AWS::Inspector::ResourceGroup.ResourceGroupTags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html#cfn-inspector-resourcegroup-resourcegrouptags
        '''
        result = self._values.get("resource_group_tags")
        assert result is not None, "Required property 'resource_group_tags' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.CfnTag, aws_cdk.core.IResolvable]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssessmentTarget",
    "CfnAssessmentTargetProps",
    "CfnAssessmentTemplate",
    "CfnAssessmentTemplateProps",
    "CfnResourceGroup",
    "CfnResourceGroupProps",
]

publication.publish()
