'''
# AWS::AccessAnalyzer Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_accessanalyzer as accessanalyzer
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
class CfnAnalyzer(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-accessanalyzer.CfnAnalyzer",
):
    '''A CloudFormation ``AWS::AccessAnalyzer::Analyzer``.

    :cloudformationResource: AWS::AccessAnalyzer::Analyzer
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        type: builtins.str,
        analyzer_name: typing.Optional[builtins.str] = None,
        archive_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnAnalyzer.ArchiveRuleProperty", aws_cdk.core.IResolvable]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::AccessAnalyzer::Analyzer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param type: ``AWS::AccessAnalyzer::Analyzer.Type``.
        :param analyzer_name: ``AWS::AccessAnalyzer::Analyzer.AnalyzerName``.
        :param archive_rules: ``AWS::AccessAnalyzer::Analyzer.ArchiveRules``.
        :param tags: ``AWS::AccessAnalyzer::Analyzer.Tags``.
        '''
        props = CfnAnalyzerProps(
            type=type,
            analyzer_name=analyzer_name,
            archive_rules=archive_rules,
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
        '''``AWS::AccessAnalyzer::Analyzer.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::AccessAnalyzer::Analyzer.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="analyzerName")
    def analyzer_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AccessAnalyzer::Analyzer.AnalyzerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-analyzername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "analyzerName"))

    @analyzer_name.setter
    def analyzer_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "analyzerName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="archiveRules")
    def archive_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnAnalyzer.ArchiveRuleProperty", aws_cdk.core.IResolvable]]]]:
        '''``AWS::AccessAnalyzer::Analyzer.ArchiveRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-archiverules
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnAnalyzer.ArchiveRuleProperty", aws_cdk.core.IResolvable]]]], jsii.get(self, "archiveRules"))

    @archive_rules.setter
    def archive_rules(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnAnalyzer.ArchiveRuleProperty", aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "archiveRules", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-accessanalyzer.CfnAnalyzer.ArchiveRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"filter": "filter", "rule_name": "ruleName"},
    )
    class ArchiveRuleProperty:
        def __init__(
            self,
            *,
            filter: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnAnalyzer.FilterProperty"]]],
            rule_name: builtins.str,
        ) -> None:
            '''
            :param filter: ``CfnAnalyzer.ArchiveRuleProperty.Filter``.
            :param rule_name: ``CfnAnalyzer.ArchiveRuleProperty.RuleName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "filter": filter,
                "rule_name": rule_name,
            }

        @builtins.property
        def filter(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalyzer.FilterProperty"]]]:
            '''``CfnAnalyzer.ArchiveRuleProperty.Filter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html#cfn-accessanalyzer-analyzer-archiverule-filter
            '''
            result = self._values.get("filter")
            assert result is not None, "Required property 'filter' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAnalyzer.FilterProperty"]]], result)

        @builtins.property
        def rule_name(self) -> builtins.str:
            '''``CfnAnalyzer.ArchiveRuleProperty.RuleName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html#cfn-accessanalyzer-analyzer-archiverule-rulename
            '''
            result = self._values.get("rule_name")
            assert result is not None, "Required property 'rule_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-accessanalyzer.CfnAnalyzer.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "property": "property",
            "contains": "contains",
            "eq": "eq",
            "exists": "exists",
            "neq": "neq",
        },
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            property: builtins.str,
            contains: typing.Optional[typing.Sequence[builtins.str]] = None,
            eq: typing.Optional[typing.Sequence[builtins.str]] = None,
            exists: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            neq: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param property: ``CfnAnalyzer.FilterProperty.Property``.
            :param contains: ``CfnAnalyzer.FilterProperty.Contains``.
            :param eq: ``CfnAnalyzer.FilterProperty.Eq``.
            :param exists: ``CfnAnalyzer.FilterProperty.Exists``.
            :param neq: ``CfnAnalyzer.FilterProperty.Neq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "property": property,
            }
            if contains is not None:
                self._values["contains"] = contains
            if eq is not None:
                self._values["eq"] = eq
            if exists is not None:
                self._values["exists"] = exists
            if neq is not None:
                self._values["neq"] = neq

        @builtins.property
        def property(self) -> builtins.str:
            '''``CfnAnalyzer.FilterProperty.Property``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-property
            '''
            result = self._values.get("property")
            assert result is not None, "Required property 'property' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def contains(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnAnalyzer.FilterProperty.Contains``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-contains
            '''
            result = self._values.get("contains")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def eq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnAnalyzer.FilterProperty.Eq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-eq
            '''
            result = self._values.get("eq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def exists(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnAnalyzer.FilterProperty.Exists``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-exists
            '''
            result = self._values.get("exists")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def neq(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnAnalyzer.FilterProperty.Neq``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html#cfn-accessanalyzer-analyzer-filter-neq
            '''
            result = self._values.get("neq")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-accessanalyzer.CfnAnalyzerProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "analyzer_name": "analyzerName",
        "archive_rules": "archiveRules",
        "tags": "tags",
    },
)
class CfnAnalyzerProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        analyzer_name: typing.Optional[builtins.str] = None,
        archive_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnAnalyzer.ArchiveRuleProperty, aws_cdk.core.IResolvable]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::AccessAnalyzer::Analyzer``.

        :param type: ``AWS::AccessAnalyzer::Analyzer.Type``.
        :param analyzer_name: ``AWS::AccessAnalyzer::Analyzer.AnalyzerName``.
        :param archive_rules: ``AWS::AccessAnalyzer::Analyzer.ArchiveRules``.
        :param tags: ``AWS::AccessAnalyzer::Analyzer.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if analyzer_name is not None:
            self._values["analyzer_name"] = analyzer_name
        if archive_rules is not None:
            self._values["archive_rules"] = archive_rules
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::AccessAnalyzer::Analyzer.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def analyzer_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::AccessAnalyzer::Analyzer.AnalyzerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-analyzername
        '''
        result = self._values.get("analyzer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def archive_rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnAnalyzer.ArchiveRuleProperty, aws_cdk.core.IResolvable]]]]:
        '''``AWS::AccessAnalyzer::Analyzer.ArchiveRules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-archiverules
        '''
        result = self._values.get("archive_rules")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnAnalyzer.ArchiveRuleProperty, aws_cdk.core.IResolvable]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::AccessAnalyzer::Analyzer.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html#cfn-accessanalyzer-analyzer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnalyzerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAnalyzer",
    "CfnAnalyzerProps",
]

publication.publish()
