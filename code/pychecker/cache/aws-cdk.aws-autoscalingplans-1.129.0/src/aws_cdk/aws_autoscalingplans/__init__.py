'''
# AWS Auto Scaling Plans Construct Library

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
class CfnScalingPlan(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan",
):
    '''A CloudFormation ``AWS::AutoScalingPlans::ScalingPlan``.

    :cloudformationResource: AWS::AutoScalingPlans::ScalingPlan
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_source: typing.Union["CfnScalingPlan.ApplicationSourceProperty", aws_cdk.core.IResolvable],
        scaling_instructions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.ScalingInstructionProperty"]]],
    ) -> None:
        '''Create a new ``AWS::AutoScalingPlans::ScalingPlan``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_source: ``AWS::AutoScalingPlans::ScalingPlan.ApplicationSource``.
        :param scaling_instructions: ``AWS::AutoScalingPlans::ScalingPlan.ScalingInstructions``.
        '''
        props = CfnScalingPlanProps(
            application_source=application_source,
            scaling_instructions=scaling_instructions,
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
    @jsii.member(jsii_name="attrScalingPlanName")
    def attr_scaling_plan_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: ScalingPlanName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScalingPlanName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrScalingPlanVersion")
    def attr_scaling_plan_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: ScalingPlanVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScalingPlanVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationSource")
    def application_source(
        self,
    ) -> typing.Union["CfnScalingPlan.ApplicationSourceProperty", aws_cdk.core.IResolvable]:
        '''``AWS::AutoScalingPlans::ScalingPlan.ApplicationSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-applicationsource
        '''
        return typing.cast(typing.Union["CfnScalingPlan.ApplicationSourceProperty", aws_cdk.core.IResolvable], jsii.get(self, "applicationSource"))

    @application_source.setter
    def application_source(
        self,
        value: typing.Union["CfnScalingPlan.ApplicationSourceProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "applicationSource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scalingInstructions")
    def scaling_instructions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.ScalingInstructionProperty"]]]:
        '''``AWS::AutoScalingPlans::ScalingPlan.ScalingInstructions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-scalinginstructions
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.ScalingInstructionProperty"]]], jsii.get(self, "scalingInstructions"))

    @scaling_instructions.setter
    def scaling_instructions(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.ScalingInstructionProperty"]]],
    ) -> None:
        jsii.set(self, "scalingInstructions", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.ApplicationSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_formation_stack_arn": "cloudFormationStackArn",
            "tag_filters": "tagFilters",
        },
    )
    class ApplicationSourceProperty:
        def __init__(
            self,
            *,
            cloud_formation_stack_arn: typing.Optional[builtins.str] = None,
            tag_filters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.TagFilterProperty"]]]] = None,
        ) -> None:
            '''
            :param cloud_formation_stack_arn: ``CfnScalingPlan.ApplicationSourceProperty.CloudFormationStackARN``.
            :param tag_filters: ``CfnScalingPlan.ApplicationSourceProperty.TagFilters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_formation_stack_arn is not None:
                self._values["cloud_formation_stack_arn"] = cloud_formation_stack_arn
            if tag_filters is not None:
                self._values["tag_filters"] = tag_filters

        @builtins.property
        def cloud_formation_stack_arn(self) -> typing.Optional[builtins.str]:
            '''``CfnScalingPlan.ApplicationSourceProperty.CloudFormationStackARN``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html#cfn-autoscalingplans-scalingplan-applicationsource-cloudformationstackarn
            '''
            result = self._values.get("cloud_formation_stack_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_filters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.TagFilterProperty"]]]]:
            '''``CfnScalingPlan.ApplicationSourceProperty.TagFilters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html#cfn-autoscalingplans-scalingplan-applicationsource-tagfilters
            '''
            result = self._values.get("tag_filters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.TagFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.CustomizedLoadMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "namespace": "namespace",
            "statistic": "statistic",
            "dimensions": "dimensions",
            "unit": "unit",
        },
    )
    class CustomizedLoadMetricSpecificationProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            namespace: builtins.str,
            statistic: builtins.str,
            dimensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.MetricDimensionProperty"]]]] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param metric_name: ``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.MetricName``.
            :param namespace: ``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Namespace``.
            :param statistic: ``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Statistic``.
            :param dimensions: ``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Dimensions``.
            :param unit: ``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "metric_name": metric_name,
                "namespace": namespace,
                "statistic": statistic,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.MetricName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> builtins.str:
            '''``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def statistic(self) -> builtins.str:
            '''``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Statistic``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-statistic
            '''
            result = self._values.get("statistic")
            assert result is not None, "Required property 'statistic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.MetricDimensionProperty"]]]]:
            '''``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Dimensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.MetricDimensionProperty"]]]], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomizedLoadMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.CustomizedScalingMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "namespace": "namespace",
            "statistic": "statistic",
            "dimensions": "dimensions",
            "unit": "unit",
        },
    )
    class CustomizedScalingMetricSpecificationProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            namespace: builtins.str,
            statistic: builtins.str,
            dimensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.MetricDimensionProperty"]]]] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param metric_name: ``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.MetricName``.
            :param namespace: ``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Namespace``.
            :param statistic: ``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Statistic``.
            :param dimensions: ``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Dimensions``.
            :param unit: ``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "metric_name": metric_name,
                "namespace": namespace,
                "statistic": statistic,
            }
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.MetricName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> builtins.str:
            '''``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Namespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def statistic(self) -> builtins.str:
            '''``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Statistic``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-statistic
            '''
            result = self._values.get("statistic")
            assert result is not None, "Required property 'statistic' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.MetricDimensionProperty"]]]]:
            '''``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Dimensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.MetricDimensionProperty"]]]], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Unit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomizedScalingMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''
            :param name: ``CfnScalingPlan.MetricDimensionProperty.Name``.
            :param value: ``CfnScalingPlan.MetricDimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnScalingPlan.MetricDimensionProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html#cfn-autoscalingplans-scalingplan-metricdimension-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnScalingPlan.MetricDimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html#cfn-autoscalingplans-scalingplan-metricdimension-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.PredefinedLoadMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "predefined_load_metric_type": "predefinedLoadMetricType",
            "resource_label": "resourceLabel",
        },
    )
    class PredefinedLoadMetricSpecificationProperty:
        def __init__(
            self,
            *,
            predefined_load_metric_type: builtins.str,
            resource_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param predefined_load_metric_type: ``CfnScalingPlan.PredefinedLoadMetricSpecificationProperty.PredefinedLoadMetricType``.
            :param resource_label: ``CfnScalingPlan.PredefinedLoadMetricSpecificationProperty.ResourceLabel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "predefined_load_metric_type": predefined_load_metric_type,
            }
            if resource_label is not None:
                self._values["resource_label"] = resource_label

        @builtins.property
        def predefined_load_metric_type(self) -> builtins.str:
            '''``CfnScalingPlan.PredefinedLoadMetricSpecificationProperty.PredefinedLoadMetricType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedloadmetricspecification-predefinedloadmetrictype
            '''
            result = self._values.get("predefined_load_metric_type")
            assert result is not None, "Required property 'predefined_load_metric_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_label(self) -> typing.Optional[builtins.str]:
            '''``CfnScalingPlan.PredefinedLoadMetricSpecificationProperty.ResourceLabel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedloadmetricspecification-resourcelabel
            '''
            result = self._values.get("resource_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredefinedLoadMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.PredefinedScalingMetricSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "predefined_scaling_metric_type": "predefinedScalingMetricType",
            "resource_label": "resourceLabel",
        },
    )
    class PredefinedScalingMetricSpecificationProperty:
        def __init__(
            self,
            *,
            predefined_scaling_metric_type: builtins.str,
            resource_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param predefined_scaling_metric_type: ``CfnScalingPlan.PredefinedScalingMetricSpecificationProperty.PredefinedScalingMetricType``.
            :param resource_label: ``CfnScalingPlan.PredefinedScalingMetricSpecificationProperty.ResourceLabel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "predefined_scaling_metric_type": predefined_scaling_metric_type,
            }
            if resource_label is not None:
                self._values["resource_label"] = resource_label

        @builtins.property
        def predefined_scaling_metric_type(self) -> builtins.str:
            '''``CfnScalingPlan.PredefinedScalingMetricSpecificationProperty.PredefinedScalingMetricType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedscalingmetricspecification-predefinedscalingmetrictype
            '''
            result = self._values.get("predefined_scaling_metric_type")
            assert result is not None, "Required property 'predefined_scaling_metric_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_label(self) -> typing.Optional[builtins.str]:
            '''``CfnScalingPlan.PredefinedScalingMetricSpecificationProperty.ResourceLabel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedscalingmetricspecification-resourcelabel
            '''
            result = self._values.get("resource_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredefinedScalingMetricSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.ScalingInstructionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_capacity": "maxCapacity",
            "min_capacity": "minCapacity",
            "resource_id": "resourceId",
            "scalable_dimension": "scalableDimension",
            "service_namespace": "serviceNamespace",
            "target_tracking_configurations": "targetTrackingConfigurations",
            "customized_load_metric_specification": "customizedLoadMetricSpecification",
            "disable_dynamic_scaling": "disableDynamicScaling",
            "predefined_load_metric_specification": "predefinedLoadMetricSpecification",
            "predictive_scaling_max_capacity_behavior": "predictiveScalingMaxCapacityBehavior",
            "predictive_scaling_max_capacity_buffer": "predictiveScalingMaxCapacityBuffer",
            "predictive_scaling_mode": "predictiveScalingMode",
            "scaling_policy_update_behavior": "scalingPolicyUpdateBehavior",
            "scheduled_action_buffer_time": "scheduledActionBufferTime",
        },
    )
    class ScalingInstructionProperty:
        def __init__(
            self,
            *,
            max_capacity: jsii.Number,
            min_capacity: jsii.Number,
            resource_id: builtins.str,
            scalable_dimension: builtins.str,
            service_namespace: builtins.str,
            target_tracking_configurations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.TargetTrackingConfigurationProperty"]]],
            customized_load_metric_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.CustomizedLoadMetricSpecificationProperty"]] = None,
            disable_dynamic_scaling: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            predefined_load_metric_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.PredefinedLoadMetricSpecificationProperty"]] = None,
            predictive_scaling_max_capacity_behavior: typing.Optional[builtins.str] = None,
            predictive_scaling_max_capacity_buffer: typing.Optional[jsii.Number] = None,
            predictive_scaling_mode: typing.Optional[builtins.str] = None,
            scaling_policy_update_behavior: typing.Optional[builtins.str] = None,
            scheduled_action_buffer_time: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param max_capacity: ``CfnScalingPlan.ScalingInstructionProperty.MaxCapacity``.
            :param min_capacity: ``CfnScalingPlan.ScalingInstructionProperty.MinCapacity``.
            :param resource_id: ``CfnScalingPlan.ScalingInstructionProperty.ResourceId``.
            :param scalable_dimension: ``CfnScalingPlan.ScalingInstructionProperty.ScalableDimension``.
            :param service_namespace: ``CfnScalingPlan.ScalingInstructionProperty.ServiceNamespace``.
            :param target_tracking_configurations: ``CfnScalingPlan.ScalingInstructionProperty.TargetTrackingConfigurations``.
            :param customized_load_metric_specification: ``CfnScalingPlan.ScalingInstructionProperty.CustomizedLoadMetricSpecification``.
            :param disable_dynamic_scaling: ``CfnScalingPlan.ScalingInstructionProperty.DisableDynamicScaling``.
            :param predefined_load_metric_specification: ``CfnScalingPlan.ScalingInstructionProperty.PredefinedLoadMetricSpecification``.
            :param predictive_scaling_max_capacity_behavior: ``CfnScalingPlan.ScalingInstructionProperty.PredictiveScalingMaxCapacityBehavior``.
            :param predictive_scaling_max_capacity_buffer: ``CfnScalingPlan.ScalingInstructionProperty.PredictiveScalingMaxCapacityBuffer``.
            :param predictive_scaling_mode: ``CfnScalingPlan.ScalingInstructionProperty.PredictiveScalingMode``.
            :param scaling_policy_update_behavior: ``CfnScalingPlan.ScalingInstructionProperty.ScalingPolicyUpdateBehavior``.
            :param scheduled_action_buffer_time: ``CfnScalingPlan.ScalingInstructionProperty.ScheduledActionBufferTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "max_capacity": max_capacity,
                "min_capacity": min_capacity,
                "resource_id": resource_id,
                "scalable_dimension": scalable_dimension,
                "service_namespace": service_namespace,
                "target_tracking_configurations": target_tracking_configurations,
            }
            if customized_load_metric_specification is not None:
                self._values["customized_load_metric_specification"] = customized_load_metric_specification
            if disable_dynamic_scaling is not None:
                self._values["disable_dynamic_scaling"] = disable_dynamic_scaling
            if predefined_load_metric_specification is not None:
                self._values["predefined_load_metric_specification"] = predefined_load_metric_specification
            if predictive_scaling_max_capacity_behavior is not None:
                self._values["predictive_scaling_max_capacity_behavior"] = predictive_scaling_max_capacity_behavior
            if predictive_scaling_max_capacity_buffer is not None:
                self._values["predictive_scaling_max_capacity_buffer"] = predictive_scaling_max_capacity_buffer
            if predictive_scaling_mode is not None:
                self._values["predictive_scaling_mode"] = predictive_scaling_mode
            if scaling_policy_update_behavior is not None:
                self._values["scaling_policy_update_behavior"] = scaling_policy_update_behavior
            if scheduled_action_buffer_time is not None:
                self._values["scheduled_action_buffer_time"] = scheduled_action_buffer_time

        @builtins.property
        def max_capacity(self) -> jsii.Number:
            '''``CfnScalingPlan.ScalingInstructionProperty.MaxCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-maxcapacity
            '''
            result = self._values.get("max_capacity")
            assert result is not None, "Required property 'max_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_capacity(self) -> jsii.Number:
            '''``CfnScalingPlan.ScalingInstructionProperty.MinCapacity``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-mincapacity
            '''
            result = self._values.get("min_capacity")
            assert result is not None, "Required property 'min_capacity' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def resource_id(self) -> builtins.str:
            '''``CfnScalingPlan.ScalingInstructionProperty.ResourceId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-resourceid
            '''
            result = self._values.get("resource_id")
            assert result is not None, "Required property 'resource_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scalable_dimension(self) -> builtins.str:
            '''``CfnScalingPlan.ScalingInstructionProperty.ScalableDimension``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-scalabledimension
            '''
            result = self._values.get("scalable_dimension")
            assert result is not None, "Required property 'scalable_dimension' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_namespace(self) -> builtins.str:
            '''``CfnScalingPlan.ScalingInstructionProperty.ServiceNamespace``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-servicenamespace
            '''
            result = self._values.get("service_namespace")
            assert result is not None, "Required property 'service_namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_tracking_configurations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.TargetTrackingConfigurationProperty"]]]:
            '''``CfnScalingPlan.ScalingInstructionProperty.TargetTrackingConfigurations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-targettrackingconfigurations
            '''
            result = self._values.get("target_tracking_configurations")
            assert result is not None, "Required property 'target_tracking_configurations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.TargetTrackingConfigurationProperty"]]], result)

        @builtins.property
        def customized_load_metric_specification(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.CustomizedLoadMetricSpecificationProperty"]]:
            '''``CfnScalingPlan.ScalingInstructionProperty.CustomizedLoadMetricSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-customizedloadmetricspecification
            '''
            result = self._values.get("customized_load_metric_specification")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.CustomizedLoadMetricSpecificationProperty"]], result)

        @builtins.property
        def disable_dynamic_scaling(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnScalingPlan.ScalingInstructionProperty.DisableDynamicScaling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-disabledynamicscaling
            '''
            result = self._values.get("disable_dynamic_scaling")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def predefined_load_metric_specification(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.PredefinedLoadMetricSpecificationProperty"]]:
            '''``CfnScalingPlan.ScalingInstructionProperty.PredefinedLoadMetricSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predefinedloadmetricspecification
            '''
            result = self._values.get("predefined_load_metric_specification")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.PredefinedLoadMetricSpecificationProperty"]], result)

        @builtins.property
        def predictive_scaling_max_capacity_behavior(
            self,
        ) -> typing.Optional[builtins.str]:
            '''``CfnScalingPlan.ScalingInstructionProperty.PredictiveScalingMaxCapacityBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predictivescalingmaxcapacitybehavior
            '''
            result = self._values.get("predictive_scaling_max_capacity_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def predictive_scaling_max_capacity_buffer(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''``CfnScalingPlan.ScalingInstructionProperty.PredictiveScalingMaxCapacityBuffer``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predictivescalingmaxcapacitybuffer
            '''
            result = self._values.get("predictive_scaling_max_capacity_buffer")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def predictive_scaling_mode(self) -> typing.Optional[builtins.str]:
            '''``CfnScalingPlan.ScalingInstructionProperty.PredictiveScalingMode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predictivescalingmode
            '''
            result = self._values.get("predictive_scaling_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scaling_policy_update_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnScalingPlan.ScalingInstructionProperty.ScalingPolicyUpdateBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-scalingpolicyupdatebehavior
            '''
            result = self._values.get("scaling_policy_update_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scheduled_action_buffer_time(self) -> typing.Optional[jsii.Number]:
            '''``CfnScalingPlan.ScalingInstructionProperty.ScheduledActionBufferTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-scheduledactionbuffertime
            '''
            result = self._values.get("scheduled_action_buffer_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingInstructionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.TagFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TagFilterProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param key: ``CfnScalingPlan.TagFilterProperty.Key``.
            :param values: ``CfnScalingPlan.TagFilterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
            }
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnScalingPlan.TagFilterProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html#cfn-autoscalingplans-scalingplan-tagfilter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnScalingPlan.TagFilterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html#cfn-autoscalingplans-scalingplan-tagfilter-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.TargetTrackingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_value": "targetValue",
            "customized_scaling_metric_specification": "customizedScalingMetricSpecification",
            "disable_scale_in": "disableScaleIn",
            "estimated_instance_warmup": "estimatedInstanceWarmup",
            "predefined_scaling_metric_specification": "predefinedScalingMetricSpecification",
            "scale_in_cooldown": "scaleInCooldown",
            "scale_out_cooldown": "scaleOutCooldown",
        },
    )
    class TargetTrackingConfigurationProperty:
        def __init__(
            self,
            *,
            target_value: jsii.Number,
            customized_scaling_metric_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.CustomizedScalingMetricSpecificationProperty"]] = None,
            disable_scale_in: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            estimated_instance_warmup: typing.Optional[jsii.Number] = None,
            predefined_scaling_metric_specification: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.PredefinedScalingMetricSpecificationProperty"]] = None,
            scale_in_cooldown: typing.Optional[jsii.Number] = None,
            scale_out_cooldown: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param target_value: ``CfnScalingPlan.TargetTrackingConfigurationProperty.TargetValue``.
            :param customized_scaling_metric_specification: ``CfnScalingPlan.TargetTrackingConfigurationProperty.CustomizedScalingMetricSpecification``.
            :param disable_scale_in: ``CfnScalingPlan.TargetTrackingConfigurationProperty.DisableScaleIn``.
            :param estimated_instance_warmup: ``CfnScalingPlan.TargetTrackingConfigurationProperty.EstimatedInstanceWarmup``.
            :param predefined_scaling_metric_specification: ``CfnScalingPlan.TargetTrackingConfigurationProperty.PredefinedScalingMetricSpecification``.
            :param scale_in_cooldown: ``CfnScalingPlan.TargetTrackingConfigurationProperty.ScaleInCooldown``.
            :param scale_out_cooldown: ``CfnScalingPlan.TargetTrackingConfigurationProperty.ScaleOutCooldown``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "target_value": target_value,
            }
            if customized_scaling_metric_specification is not None:
                self._values["customized_scaling_metric_specification"] = customized_scaling_metric_specification
            if disable_scale_in is not None:
                self._values["disable_scale_in"] = disable_scale_in
            if estimated_instance_warmup is not None:
                self._values["estimated_instance_warmup"] = estimated_instance_warmup
            if predefined_scaling_metric_specification is not None:
                self._values["predefined_scaling_metric_specification"] = predefined_scaling_metric_specification
            if scale_in_cooldown is not None:
                self._values["scale_in_cooldown"] = scale_in_cooldown
            if scale_out_cooldown is not None:
                self._values["scale_out_cooldown"] = scale_out_cooldown

        @builtins.property
        def target_value(self) -> jsii.Number:
            '''``CfnScalingPlan.TargetTrackingConfigurationProperty.TargetValue``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-targetvalue
            '''
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def customized_scaling_metric_specification(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.CustomizedScalingMetricSpecificationProperty"]]:
            '''``CfnScalingPlan.TargetTrackingConfigurationProperty.CustomizedScalingMetricSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-customizedscalingmetricspecification
            '''
            result = self._values.get("customized_scaling_metric_specification")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.CustomizedScalingMetricSpecificationProperty"]], result)

        @builtins.property
        def disable_scale_in(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnScalingPlan.TargetTrackingConfigurationProperty.DisableScaleIn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-disablescalein
            '''
            result = self._values.get("disable_scale_in")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def estimated_instance_warmup(self) -> typing.Optional[jsii.Number]:
            '''``CfnScalingPlan.TargetTrackingConfigurationProperty.EstimatedInstanceWarmup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-estimatedinstancewarmup
            '''
            result = self._values.get("estimated_instance_warmup")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def predefined_scaling_metric_specification(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.PredefinedScalingMetricSpecificationProperty"]]:
            '''``CfnScalingPlan.TargetTrackingConfigurationProperty.PredefinedScalingMetricSpecification``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-predefinedscalingmetricspecification
            '''
            result = self._values.get("predefined_scaling_metric_specification")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPlan.PredefinedScalingMetricSpecificationProperty"]], result)

        @builtins.property
        def scale_in_cooldown(self) -> typing.Optional[jsii.Number]:
            '''``CfnScalingPlan.TargetTrackingConfigurationProperty.ScaleInCooldown``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-scaleincooldown
            '''
            result = self._values.get("scale_in_cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scale_out_cooldown(self) -> typing.Optional[jsii.Number]:
            '''``CfnScalingPlan.TargetTrackingConfigurationProperty.ScaleOutCooldown``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-scaleoutcooldown
            '''
            result = self._values.get("scale_out_cooldown")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_source": "applicationSource",
        "scaling_instructions": "scalingInstructions",
    },
)
class CfnScalingPlanProps:
    def __init__(
        self,
        *,
        application_source: typing.Union[CfnScalingPlan.ApplicationSourceProperty, aws_cdk.core.IResolvable],
        scaling_instructions: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnScalingPlan.ScalingInstructionProperty]]],
    ) -> None:
        '''Properties for defining a ``AWS::AutoScalingPlans::ScalingPlan``.

        :param application_source: ``AWS::AutoScalingPlans::ScalingPlan.ApplicationSource``.
        :param scaling_instructions: ``AWS::AutoScalingPlans::ScalingPlan.ScalingInstructions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_source": application_source,
            "scaling_instructions": scaling_instructions,
        }

    @builtins.property
    def application_source(
        self,
    ) -> typing.Union[CfnScalingPlan.ApplicationSourceProperty, aws_cdk.core.IResolvable]:
        '''``AWS::AutoScalingPlans::ScalingPlan.ApplicationSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-applicationsource
        '''
        result = self._values.get("application_source")
        assert result is not None, "Required property 'application_source' is missing"
        return typing.cast(typing.Union[CfnScalingPlan.ApplicationSourceProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def scaling_instructions(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnScalingPlan.ScalingInstructionProperty]]]:
        '''``AWS::AutoScalingPlans::ScalingPlan.ScalingInstructions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-scalinginstructions
        '''
        result = self._values.get("scaling_instructions")
        assert result is not None, "Required property 'scaling_instructions' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnScalingPlan.ScalingInstructionProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScalingPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnScalingPlan",
    "CfnScalingPlanProps",
]

publication.publish()
