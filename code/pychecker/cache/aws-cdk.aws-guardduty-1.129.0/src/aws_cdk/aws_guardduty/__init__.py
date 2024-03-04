'''
# Amazon GuardDuty Construct Library

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
class CfnDetector(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-guardduty.CfnDetector",
):
    '''A CloudFormation ``AWS::GuardDuty::Detector``.

    :cloudformationResource: AWS::GuardDuty::Detector
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        enable: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        data_sources: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.CFNDataSourceConfigurationsProperty"]] = None,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::Detector``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param enable: ``AWS::GuardDuty::Detector.Enable``.
        :param data_sources: ``AWS::GuardDuty::Detector.DataSources``.
        :param finding_publishing_frequency: ``AWS::GuardDuty::Detector.FindingPublishingFrequency``.
        '''
        props = CfnDetectorProps(
            enable=enable,
            data_sources=data_sources,
            finding_publishing_frequency=finding_publishing_frequency,
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
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::GuardDuty::Detector.Enable``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-enable
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "enable", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSources")
    def data_sources(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.CFNDataSourceConfigurationsProperty"]]:
        '''``AWS::GuardDuty::Detector.DataSources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-datasources
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.CFNDataSourceConfigurationsProperty"]], jsii.get(self, "dataSources"))

    @data_sources.setter
    def data_sources(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.CFNDataSourceConfigurationsProperty"]],
    ) -> None:
        jsii.set(self, "dataSources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::Detector.FindingPublishingFrequency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-findingpublishingfrequency
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "findingPublishingFrequency"))

    @finding_publishing_frequency.setter
    def finding_publishing_frequency(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "findingPublishingFrequency", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-guardduty.CfnDetector.CFNDataSourceConfigurationsProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_logs": "s3Logs"},
    )
    class CFNDataSourceConfigurationsProperty:
        def __init__(
            self,
            *,
            s3_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.CFNS3LogsConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param s3_logs: ``CfnDetector.CFNDataSourceConfigurationsProperty.S3Logs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if s3_logs is not None:
                self._values["s3_logs"] = s3_logs

        @builtins.property
        def s3_logs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.CFNS3LogsConfigurationProperty"]]:
            '''``CfnDetector.CFNDataSourceConfigurationsProperty.S3Logs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfndatasourceconfigurations.html#cfn-guardduty-detector-cfndatasourceconfigurations-s3logs
            '''
            result = self._values.get("s3_logs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnDetector.CFNS3LogsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNDataSourceConfigurationsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-guardduty.CfnDetector.CFNS3LogsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enable": "enable"},
    )
    class CFNS3LogsConfigurationProperty:
        def __init__(
            self,
            *,
            enable: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param enable: ``CfnDetector.CFNS3LogsConfigurationProperty.Enable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enable is not None:
                self._values["enable"] = enable

        @builtins.property
        def enable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnDetector.CFNS3LogsConfigurationProperty.Enable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-detector-cfns3logsconfiguration.html#cfn-guardduty-detector-cfns3logsconfiguration-enable
            '''
            result = self._values.get("enable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CFNS3LogsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-guardduty.CfnDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "enable": "enable",
        "data_sources": "dataSources",
        "finding_publishing_frequency": "findingPublishingFrequency",
    },
)
class CfnDetectorProps:
    def __init__(
        self,
        *,
        enable: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        data_sources: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDetector.CFNDataSourceConfigurationsProperty]] = None,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GuardDuty::Detector``.

        :param enable: ``AWS::GuardDuty::Detector.Enable``.
        :param data_sources: ``AWS::GuardDuty::Detector.DataSources``.
        :param finding_publishing_frequency: ``AWS::GuardDuty::Detector.FindingPublishingFrequency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "enable": enable,
        }
        if data_sources is not None:
            self._values["data_sources"] = data_sources
        if finding_publishing_frequency is not None:
            self._values["finding_publishing_frequency"] = finding_publishing_frequency

    @builtins.property
    def enable(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::GuardDuty::Detector.Enable``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-enable
        '''
        result = self._values.get("enable")
        assert result is not None, "Required property 'enable' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def data_sources(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDetector.CFNDataSourceConfigurationsProperty]]:
        '''``AWS::GuardDuty::Detector.DataSources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-datasources
        '''
        result = self._values.get("data_sources")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnDetector.CFNDataSourceConfigurationsProperty]], result)

    @builtins.property
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::Detector.FindingPublishingFrequency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-findingpublishingfrequency
        '''
        result = self._values.get("finding_publishing_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFilter(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-guardduty.CfnFilter",
):
    '''A CloudFormation ``AWS::GuardDuty::Filter``.

    :cloudformationResource: AWS::GuardDuty::Filter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        action: builtins.str,
        description: builtins.str,
        detector_id: builtins.str,
        finding_criteria: typing.Union[aws_cdk.core.IResolvable, "CfnFilter.FindingCriteriaProperty"],
        name: builtins.str,
        rank: jsii.Number,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::Filter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param action: ``AWS::GuardDuty::Filter.Action``.
        :param description: ``AWS::GuardDuty::Filter.Description``.
        :param detector_id: ``AWS::GuardDuty::Filter.DetectorId``.
        :param finding_criteria: ``AWS::GuardDuty::Filter.FindingCriteria``.
        :param name: ``AWS::GuardDuty::Filter.Name``.
        :param rank: ``AWS::GuardDuty::Filter.Rank``.
        '''
        props = CfnFilterProps(
            action=action,
            description=description,
            detector_id=detector_id,
            finding_criteria=finding_criteria,
            name=name,
            rank=rank,
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
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        '''``AWS::GuardDuty::Filter.Action``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-action
        '''
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        jsii.set(self, "action", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''``AWS::GuardDuty::Filter.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-description
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''``AWS::GuardDuty::Filter.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="findingCriteria")
    def finding_criteria(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnFilter.FindingCriteriaProperty"]:
        '''``AWS::GuardDuty::Filter.FindingCriteria``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-findingcriteria
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnFilter.FindingCriteriaProperty"], jsii.get(self, "findingCriteria"))

    @finding_criteria.setter
    def finding_criteria(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnFilter.FindingCriteriaProperty"],
    ) -> None:
        jsii.set(self, "findingCriteria", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::GuardDuty::Filter.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rank")
    def rank(self) -> jsii.Number:
        '''``AWS::GuardDuty::Filter.Rank``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-rank
        '''
        return typing.cast(jsii.Number, jsii.get(self, "rank"))

    @rank.setter
    def rank(self, value: jsii.Number) -> None:
        jsii.set(self, "rank", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-guardduty.CfnFilter.ConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "eq": "eq",
            "gte": "gte",
            "lt": "lt",
            "lte": "lte",
            "neq": "neq",
        },
    )
    class ConditionProperty:
        def __init__(
            self,
            *,
            eq: typing.Optional[typing.Sequence[builtins.str]] = None,
            gte: typing.Optional[jsii.Number] = None,
            lt: typing.Optional[jsii.Number] = None,
            lte: typing.Optional[jsii.Number] = None,
            neq: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param eq: ``CfnFilter.ConditionProperty.Eq``.
            :param gte: ``CfnFilter.ConditionProperty.Gte``.
            :param lt: ``CfnFilter.ConditionProperty.Lt``.
            :param lte: ``CfnFilter.ConditionProperty.Lte``.
            :param neq: ``CfnFilter.ConditionProperty.Neq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if eq is not None:
                self._values["eq"] = eq
            if gte is not None:
                self._values["gte"] = gte
            if lt is not None:
                self._values["lt"] = lt
            if lte is not None:
                self._values["lte"] = lte
            if neq is not None:
                self._values["neq"] = neq

        @builtins.property
        def eq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnFilter.ConditionProperty.Eq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-eq
            '''
            result = self._values.get("eq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def gte(self) -> typing.Optional[jsii.Number]:
            '''``CfnFilter.ConditionProperty.Gte``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-gte
            '''
            result = self._values.get("gte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lt(self) -> typing.Optional[jsii.Number]:
            '''``CfnFilter.ConditionProperty.Lt``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lt
            '''
            result = self._values.get("lt")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lte(self) -> typing.Optional[jsii.Number]:
            '''``CfnFilter.ConditionProperty.Lte``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lte
            '''
            result = self._values.get("lte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def neq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnFilter.ConditionProperty.Neq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-neq
            '''
            result = self._values.get("neq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-guardduty.CfnFilter.FindingCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"criterion": "criterion", "item_type": "itemType"},
    )
    class FindingCriteriaProperty:
        def __init__(
            self,
            *,
            criterion: typing.Any = None,
            item_type: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFilter.ConditionProperty"]] = None,
        ) -> None:
            '''
            :param criterion: ``CfnFilter.FindingCriteriaProperty.Criterion``.
            :param item_type: ``CfnFilter.FindingCriteriaProperty.ItemType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if criterion is not None:
                self._values["criterion"] = criterion
            if item_type is not None:
                self._values["item_type"] = item_type

        @builtins.property
        def criterion(self) -> typing.Any:
            '''``CfnFilter.FindingCriteriaProperty.Criterion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-criterion
            '''
            result = self._values.get("criterion")
            return typing.cast(typing.Any, result)

        @builtins.property
        def item_type(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFilter.ConditionProperty"]]:
            '''``CfnFilter.FindingCriteriaProperty.ItemType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-itemtype
            '''
            result = self._values.get("item_type")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFilter.ConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-guardduty.CfnFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "description": "description",
        "detector_id": "detectorId",
        "finding_criteria": "findingCriteria",
        "name": "name",
        "rank": "rank",
    },
)
class CfnFilterProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        description: builtins.str,
        detector_id: builtins.str,
        finding_criteria: typing.Union[aws_cdk.core.IResolvable, CfnFilter.FindingCriteriaProperty],
        name: builtins.str,
        rank: jsii.Number,
    ) -> None:
        '''Properties for defining a ``AWS::GuardDuty::Filter``.

        :param action: ``AWS::GuardDuty::Filter.Action``.
        :param description: ``AWS::GuardDuty::Filter.Description``.
        :param detector_id: ``AWS::GuardDuty::Filter.DetectorId``.
        :param finding_criteria: ``AWS::GuardDuty::Filter.FindingCriteria``.
        :param name: ``AWS::GuardDuty::Filter.Name``.
        :param rank: ``AWS::GuardDuty::Filter.Rank``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "description": description,
            "detector_id": detector_id,
            "finding_criteria": finding_criteria,
            "name": name,
            "rank": rank,
        }

    @builtins.property
    def action(self) -> builtins.str:
        '''``AWS::GuardDuty::Filter.Action``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''``AWS::GuardDuty::Filter.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''``AWS::GuardDuty::Filter.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def finding_criteria(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnFilter.FindingCriteriaProperty]:
        '''``AWS::GuardDuty::Filter.FindingCriteria``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-findingcriteria
        '''
        result = self._values.get("finding_criteria")
        assert result is not None, "Required property 'finding_criteria' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnFilter.FindingCriteriaProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::GuardDuty::Filter.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rank(self) -> jsii.Number:
        '''``AWS::GuardDuty::Filter.Rank``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-rank
        '''
        result = self._values.get("rank")
        assert result is not None, "Required property 'rank' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnIPSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-guardduty.CfnIPSet",
):
    '''A CloudFormation ``AWS::GuardDuty::IPSet``.

    :cloudformationResource: AWS::GuardDuty::IPSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        activate: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::IPSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param activate: ``AWS::GuardDuty::IPSet.Activate``.
        :param detector_id: ``AWS::GuardDuty::IPSet.DetectorId``.
        :param format: ``AWS::GuardDuty::IPSet.Format``.
        :param location: ``AWS::GuardDuty::IPSet.Location``.
        :param name: ``AWS::GuardDuty::IPSet.Name``.
        '''
        props = CfnIPSetProps(
            activate=activate,
            detector_id=detector_id,
            format=format,
            location=location,
            name=name,
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
    @jsii.member(jsii_name="activate")
    def activate(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::GuardDuty::IPSet.Activate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "activate"))

    @activate.setter
    def activate(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "activate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''``AWS::GuardDuty::IPSet.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        '''``AWS::GuardDuty::IPSet.Format``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format
        '''
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        jsii.set(self, "format", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        '''``AWS::GuardDuty::IPSet.Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location
        '''
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        jsii.set(self, "location", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::IPSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-guardduty.CfnIPSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "activate": "activate",
        "detector_id": "detectorId",
        "format": "format",
        "location": "location",
        "name": "name",
    },
)
class CfnIPSetProps:
    def __init__(
        self,
        *,
        activate: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GuardDuty::IPSet``.

        :param activate: ``AWS::GuardDuty::IPSet.Activate``.
        :param detector_id: ``AWS::GuardDuty::IPSet.DetectorId``.
        :param format: ``AWS::GuardDuty::IPSet.Format``.
        :param location: ``AWS::GuardDuty::IPSet.Location``.
        :param name: ``AWS::GuardDuty::IPSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "activate": activate,
            "detector_id": detector_id,
            "format": format,
            "location": location,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def activate(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::GuardDuty::IPSet.Activate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate
        '''
        result = self._values.get("activate")
        assert result is not None, "Required property 'activate' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''``AWS::GuardDuty::IPSet.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''``AWS::GuardDuty::IPSet.Format``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''``AWS::GuardDuty::IPSet.Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::IPSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIPSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMaster(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-guardduty.CfnMaster",
):
    '''A CloudFormation ``AWS::GuardDuty::Master``.

    :cloudformationResource: AWS::GuardDuty::Master
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        detector_id: builtins.str,
        master_id: builtins.str,
        invitation_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::Master``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param detector_id: ``AWS::GuardDuty::Master.DetectorId``.
        :param master_id: ``AWS::GuardDuty::Master.MasterId``.
        :param invitation_id: ``AWS::GuardDuty::Master.InvitationId``.
        '''
        props = CfnMasterProps(
            detector_id=detector_id, master_id=master_id, invitation_id=invitation_id
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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''``AWS::GuardDuty::Master.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="masterId")
    def master_id(self) -> builtins.str:
        '''``AWS::GuardDuty::Master.MasterId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-masterid
        '''
        return typing.cast(builtins.str, jsii.get(self, "masterId"))

    @master_id.setter
    def master_id(self, value: builtins.str) -> None:
        jsii.set(self, "masterId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="invitationId")
    def invitation_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::Master.InvitationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-invitationid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "invitationId"))

    @invitation_id.setter
    def invitation_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "invitationId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-guardduty.CfnMasterProps",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "master_id": "masterId",
        "invitation_id": "invitationId",
    },
)
class CfnMasterProps:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        master_id: builtins.str,
        invitation_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GuardDuty::Master``.

        :param detector_id: ``AWS::GuardDuty::Master.DetectorId``.
        :param master_id: ``AWS::GuardDuty::Master.MasterId``.
        :param invitation_id: ``AWS::GuardDuty::Master.InvitationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "detector_id": detector_id,
            "master_id": master_id,
        }
        if invitation_id is not None:
            self._values["invitation_id"] = invitation_id

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''``AWS::GuardDuty::Master.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_id(self) -> builtins.str:
        '''``AWS::GuardDuty::Master.MasterId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-masterid
        '''
        result = self._values.get("master_id")
        assert result is not None, "Required property 'master_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invitation_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::Master.InvitationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-invitationid
        '''
        result = self._values.get("invitation_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMasterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnMember(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-guardduty.CfnMember",
):
    '''A CloudFormation ``AWS::GuardDuty::Member``.

    :cloudformationResource: AWS::GuardDuty::Member
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        detector_id: builtins.str,
        email: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::Member``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param detector_id: ``AWS::GuardDuty::Member.DetectorId``.
        :param email: ``AWS::GuardDuty::Member.Email``.
        :param member_id: ``AWS::GuardDuty::Member.MemberId``.
        :param disable_email_notification: ``AWS::GuardDuty::Member.DisableEmailNotification``.
        :param message: ``AWS::GuardDuty::Member.Message``.
        :param status: ``AWS::GuardDuty::Member.Status``.
        '''
        props = CfnMemberProps(
            detector_id=detector_id,
            email=email,
            member_id=member_id,
            disable_email_notification=disable_email_notification,
            message=message,
            status=status,
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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''``AWS::GuardDuty::Member.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        '''``AWS::GuardDuty::Member.Email``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-email
        '''
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        jsii.set(self, "email", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="memberId")
    def member_id(self) -> builtins.str:
        '''``AWS::GuardDuty::Member.MemberId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-memberid
        '''
        return typing.cast(builtins.str, jsii.get(self, "memberId"))

    @member_id.setter
    def member_id(self, value: builtins.str) -> None:
        jsii.set(self, "memberId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="disableEmailNotification")
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::GuardDuty::Member.DisableEmailNotification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-disableemailnotification
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "disableEmailNotification"))

    @disable_email_notification.setter
    def disable_email_notification(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "disableEmailNotification", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="message")
    def message(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::Member.Message``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-message
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "message"))

    @message.setter
    def message(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "message", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::Member.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-guardduty.CfnMemberProps",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "email": "email",
        "member_id": "memberId",
        "disable_email_notification": "disableEmailNotification",
        "message": "message",
        "status": "status",
    },
)
class CfnMemberProps:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        email: builtins.str,
        member_id: builtins.str,
        disable_email_notification: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GuardDuty::Member``.

        :param detector_id: ``AWS::GuardDuty::Member.DetectorId``.
        :param email: ``AWS::GuardDuty::Member.Email``.
        :param member_id: ``AWS::GuardDuty::Member.MemberId``.
        :param disable_email_notification: ``AWS::GuardDuty::Member.DisableEmailNotification``.
        :param message: ``AWS::GuardDuty::Member.Message``.
        :param status: ``AWS::GuardDuty::Member.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "detector_id": detector_id,
            "email": email,
            "member_id": member_id,
        }
        if disable_email_notification is not None:
            self._values["disable_email_notification"] = disable_email_notification
        if message is not None:
            self._values["message"] = message
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''``AWS::GuardDuty::Member.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''``AWS::GuardDuty::Member.Email``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-email
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(self) -> builtins.str:
        '''``AWS::GuardDuty::Member.MemberId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-memberid
        '''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_email_notification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::GuardDuty::Member.DisableEmailNotification``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-disableemailnotification
        '''
        result = self._values.get("disable_email_notification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::Member.Message``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-message
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::Member.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMemberProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnThreatIntelSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-guardduty.CfnThreatIntelSet",
):
    '''A CloudFormation ``AWS::GuardDuty::ThreatIntelSet``.

    :cloudformationResource: AWS::GuardDuty::ThreatIntelSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        activate: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::GuardDuty::ThreatIntelSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param activate: ``AWS::GuardDuty::ThreatIntelSet.Activate``.
        :param detector_id: ``AWS::GuardDuty::ThreatIntelSet.DetectorId``.
        :param format: ``AWS::GuardDuty::ThreatIntelSet.Format``.
        :param location: ``AWS::GuardDuty::ThreatIntelSet.Location``.
        :param name: ``AWS::GuardDuty::ThreatIntelSet.Name``.
        '''
        props = CfnThreatIntelSetProps(
            activate=activate,
            detector_id=detector_id,
            format=format,
            location=location,
            name=name,
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
    @jsii.member(jsii_name="activate")
    def activate(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::GuardDuty::ThreatIntelSet.Activate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-activate
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "activate"))

    @activate.setter
    def activate(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "activate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''``AWS::GuardDuty::ThreatIntelSet.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-detectorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        jsii.set(self, "detectorId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        '''``AWS::GuardDuty::ThreatIntelSet.Format``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-format
        '''
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        jsii.set(self, "format", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        '''``AWS::GuardDuty::ThreatIntelSet.Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-location
        '''
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        jsii.set(self, "location", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::ThreatIntelSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-guardduty.CfnThreatIntelSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "activate": "activate",
        "detector_id": "detectorId",
        "format": "format",
        "location": "location",
        "name": "name",
    },
)
class CfnThreatIntelSetProps:
    def __init__(
        self,
        *,
        activate: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        detector_id: builtins.str,
        format: builtins.str,
        location: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::GuardDuty::ThreatIntelSet``.

        :param activate: ``AWS::GuardDuty::ThreatIntelSet.Activate``.
        :param detector_id: ``AWS::GuardDuty::ThreatIntelSet.DetectorId``.
        :param format: ``AWS::GuardDuty::ThreatIntelSet.Format``.
        :param location: ``AWS::GuardDuty::ThreatIntelSet.Location``.
        :param name: ``AWS::GuardDuty::ThreatIntelSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "activate": activate,
            "detector_id": detector_id,
            "format": format,
            "location": location,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def activate(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::GuardDuty::ThreatIntelSet.Activate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-activate
        '''
        result = self._values.get("activate")
        assert result is not None, "Required property 'activate' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''``AWS::GuardDuty::ThreatIntelSet.DetectorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''``AWS::GuardDuty::ThreatIntelSet.Format``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-format
        '''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''``AWS::GuardDuty::ThreatIntelSet.Location``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-location
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::GuardDuty::ThreatIntelSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnThreatIntelSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDetector",
    "CfnDetectorProps",
    "CfnFilter",
    "CfnFilterProps",
    "CfnIPSet",
    "CfnIPSetProps",
    "CfnMaster",
    "CfnMasterProps",
    "CfnMember",
    "CfnMemberProps",
    "CfnThreatIntelSet",
    "CfnThreatIntelSetProps",
]

publication.publish()
