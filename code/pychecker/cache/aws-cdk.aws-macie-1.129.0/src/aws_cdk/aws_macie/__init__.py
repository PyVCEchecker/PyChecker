'''
# AWS::Macie Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_macie as macie
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
class CfnCustomDataIdentifier(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-macie.CfnCustomDataIdentifier",
):
    '''A CloudFormation ``AWS::Macie::CustomDataIdentifier``.

    :cloudformationResource: AWS::Macie::CustomDataIdentifier
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        regex: builtins.str,
        description: typing.Optional[builtins.str] = None,
        ignore_words: typing.Optional[typing.Sequence[builtins.str]] = None,
        keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_match_distance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::Macie::CustomDataIdentifier``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Macie::CustomDataIdentifier.Name``.
        :param regex: ``AWS::Macie::CustomDataIdentifier.Regex``.
        :param description: ``AWS::Macie::CustomDataIdentifier.Description``.
        :param ignore_words: ``AWS::Macie::CustomDataIdentifier.IgnoreWords``.
        :param keywords: ``AWS::Macie::CustomDataIdentifier.Keywords``.
        :param maximum_match_distance: ``AWS::Macie::CustomDataIdentifier.MaximumMatchDistance``.
        '''
        props = CfnCustomDataIdentifierProps(
            name=name,
            regex=regex,
            description=description,
            ignore_words=ignore_words,
            keywords=keywords,
            maximum_match_distance=maximum_match_distance,
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Macie::CustomDataIdentifier.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        '''``AWS::Macie::CustomDataIdentifier.Regex``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-regex
        '''
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        jsii.set(self, "regex", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::CustomDataIdentifier.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ignoreWords")
    def ignore_words(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Macie::CustomDataIdentifier.IgnoreWords``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-ignorewords
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoreWords"))

    @ignore_words.setter
    def ignore_words(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "ignoreWords", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keywords")
    def keywords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Macie::CustomDataIdentifier.Keywords``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-keywords
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keywords"))

    @keywords.setter
    def keywords(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "keywords", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="maximumMatchDistance")
    def maximum_match_distance(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Macie::CustomDataIdentifier.MaximumMatchDistance``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-maximummatchdistance
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumMatchDistance"))

    @maximum_match_distance.setter
    def maximum_match_distance(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "maximumMatchDistance", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-macie.CfnCustomDataIdentifierProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "regex": "regex",
        "description": "description",
        "ignore_words": "ignoreWords",
        "keywords": "keywords",
        "maximum_match_distance": "maximumMatchDistance",
    },
)
class CfnCustomDataIdentifierProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        regex: builtins.str,
        description: typing.Optional[builtins.str] = None,
        ignore_words: typing.Optional[typing.Sequence[builtins.str]] = None,
        keywords: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_match_distance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Macie::CustomDataIdentifier``.

        :param name: ``AWS::Macie::CustomDataIdentifier.Name``.
        :param regex: ``AWS::Macie::CustomDataIdentifier.Regex``.
        :param description: ``AWS::Macie::CustomDataIdentifier.Description``.
        :param ignore_words: ``AWS::Macie::CustomDataIdentifier.IgnoreWords``.
        :param keywords: ``AWS::Macie::CustomDataIdentifier.Keywords``.
        :param maximum_match_distance: ``AWS::Macie::CustomDataIdentifier.MaximumMatchDistance``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "regex": regex,
        }
        if description is not None:
            self._values["description"] = description
        if ignore_words is not None:
            self._values["ignore_words"] = ignore_words
        if keywords is not None:
            self._values["keywords"] = keywords
        if maximum_match_distance is not None:
            self._values["maximum_match_distance"] = maximum_match_distance

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Macie::CustomDataIdentifier.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regex(self) -> builtins.str:
        '''``AWS::Macie::CustomDataIdentifier.Regex``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-regex
        '''
        result = self._values.get("regex")
        assert result is not None, "Required property 'regex' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::CustomDataIdentifier.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_words(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Macie::CustomDataIdentifier.IgnoreWords``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-ignorewords
        '''
        result = self._values.get("ignore_words")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def keywords(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::Macie::CustomDataIdentifier.Keywords``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-keywords
        '''
        result = self._values.get("keywords")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def maximum_match_distance(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Macie::CustomDataIdentifier.MaximumMatchDistance``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-customdataidentifier.html#cfn-macie-customdataidentifier-maximummatchdistance
        '''
        result = self._values.get("maximum_match_distance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomDataIdentifierProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnFindingsFilter(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-macie.CfnFindingsFilter",
):
    '''A CloudFormation ``AWS::Macie::FindingsFilter``.

    :cloudformationResource: AWS::Macie::FindingsFilter
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        finding_criteria: typing.Union["CfnFindingsFilter.FindingCriteriaProperty", aws_cdk.core.IResolvable],
        name: builtins.str,
        action: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new ``AWS::Macie::FindingsFilter``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param finding_criteria: ``AWS::Macie::FindingsFilter.FindingCriteria``.
        :param name: ``AWS::Macie::FindingsFilter.Name``.
        :param action: ``AWS::Macie::FindingsFilter.Action``.
        :param description: ``AWS::Macie::FindingsFilter.Description``.
        :param position: ``AWS::Macie::FindingsFilter.Position``.
        '''
        props = CfnFindingsFilterProps(
            finding_criteria=finding_criteria,
            name=name,
            action=action,
            description=description,
            position=position,
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
    @jsii.member(jsii_name="attrFindingsFilterListItems")
    def attr_findings_filter_list_items(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: FindingsFilterListItems
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrFindingsFilterListItems"))

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
    @jsii.member(jsii_name="findingCriteria")
    def finding_criteria(
        self,
    ) -> typing.Union["CfnFindingsFilter.FindingCriteriaProperty", aws_cdk.core.IResolvable]:
        '''``AWS::Macie::FindingsFilter.FindingCriteria``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-findingcriteria
        '''
        return typing.cast(typing.Union["CfnFindingsFilter.FindingCriteriaProperty", aws_cdk.core.IResolvable], jsii.get(self, "findingCriteria"))

    @finding_criteria.setter
    def finding_criteria(
        self,
        value: typing.Union["CfnFindingsFilter.FindingCriteriaProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "findingCriteria", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Macie::FindingsFilter.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="action")
    def action(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::FindingsFilter.Action``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-action
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "action"))

    @action.setter
    def action(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "action", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::FindingsFilter.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="position")
    def position(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Macie::FindingsFilter.Position``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-position
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "position"))

    @position.setter
    def position(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "position", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-macie.CfnFindingsFilter.CriterionProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class CriterionProperty:
        def __init__(self) -> None:
            '''
            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-criterion.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CriterionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-macie.CfnFindingsFilter.FindingCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={"criterion": "criterion"},
    )
    class FindingCriteriaProperty:
        def __init__(
            self,
            *,
            criterion: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFindingsFilter.CriterionProperty"]] = None,
        ) -> None:
            '''
            :param criterion: ``CfnFindingsFilter.FindingCriteriaProperty.Criterion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if criterion is not None:
                self._values["criterion"] = criterion

        @builtins.property
        def criterion(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFindingsFilter.CriterionProperty"]]:
            '''``CfnFindingsFilter.FindingCriteriaProperty.Criterion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingcriteria.html#cfn-macie-findingsfilter-findingcriteria-criterion
            '''
            result = self._values.get("criterion")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnFindingsFilter.CriterionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-macie.CfnFindingsFilter.FindingsFilterListItemProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "name": "name"},
    )
    class FindingsFilterListItemProperty:
        def __init__(
            self,
            *,
            id: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param id: ``CfnFindingsFilter.FindingsFilterListItemProperty.Id``.
            :param name: ``CfnFindingsFilter.FindingsFilterListItemProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if id is not None:
                self._values["id"] = id
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def id(self) -> typing.Optional[builtins.str]:
            '''``CfnFindingsFilter.FindingsFilterListItemProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnFindingsFilter.FindingsFilterListItemProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-macie-findingsfilter-findingsfilterlistitem.html#cfn-macie-findingsfilter-findingsfilterlistitem-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FindingsFilterListItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-macie.CfnFindingsFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "finding_criteria": "findingCriteria",
        "name": "name",
        "action": "action",
        "description": "description",
        "position": "position",
    },
)
class CfnFindingsFilterProps:
    def __init__(
        self,
        *,
        finding_criteria: typing.Union[CfnFindingsFilter.FindingCriteriaProperty, aws_cdk.core.IResolvable],
        name: builtins.str,
        action: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Macie::FindingsFilter``.

        :param finding_criteria: ``AWS::Macie::FindingsFilter.FindingCriteria``.
        :param name: ``AWS::Macie::FindingsFilter.Name``.
        :param action: ``AWS::Macie::FindingsFilter.Action``.
        :param description: ``AWS::Macie::FindingsFilter.Description``.
        :param position: ``AWS::Macie::FindingsFilter.Position``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "finding_criteria": finding_criteria,
            "name": name,
        }
        if action is not None:
            self._values["action"] = action
        if description is not None:
            self._values["description"] = description
        if position is not None:
            self._values["position"] = position

    @builtins.property
    def finding_criteria(
        self,
    ) -> typing.Union[CfnFindingsFilter.FindingCriteriaProperty, aws_cdk.core.IResolvable]:
        '''``AWS::Macie::FindingsFilter.FindingCriteria``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-findingcriteria
        '''
        result = self._values.get("finding_criteria")
        assert result is not None, "Required property 'finding_criteria' is missing"
        return typing.cast(typing.Union[CfnFindingsFilter.FindingCriteriaProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Macie::FindingsFilter.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::FindingsFilter.Action``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-action
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::FindingsFilter.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def position(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Macie::FindingsFilter.Position``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-findingsfilter.html#cfn-macie-findingsfilter-position
        '''
        result = self._values.get("position")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFindingsFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSession(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-macie.CfnSession",
):
    '''A CloudFormation ``AWS::Macie::Session``.

    :cloudformationResource: AWS::Macie::Session
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Macie::Session``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param finding_publishing_frequency: ``AWS::Macie::Session.FindingPublishingFrequency``.
        :param status: ``AWS::Macie::Session.Status``.
        '''
        props = CfnSessionProps(
            finding_publishing_frequency=finding_publishing_frequency, status=status
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
    @jsii.member(jsii_name="attrAwsAccountId")
    def attr_aws_account_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: AwsAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrServiceRole")
    def attr_service_role(self) -> builtins.str:
        '''
        :cloudformationAttribute: ServiceRole
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceRole"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::Session.FindingPublishingFrequency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-findingpublishingfrequency
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "findingPublishingFrequency"))

    @finding_publishing_frequency.setter
    def finding_publishing_frequency(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "findingPublishingFrequency", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::Session.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-macie.CfnSessionProps",
    jsii_struct_bases=[],
    name_mapping={
        "finding_publishing_frequency": "findingPublishingFrequency",
        "status": "status",
    },
)
class CfnSessionProps:
    def __init__(
        self,
        *,
        finding_publishing_frequency: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Macie::Session``.

        :param finding_publishing_frequency: ``AWS::Macie::Session.FindingPublishingFrequency``.
        :param status: ``AWS::Macie::Session.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html
        '''
        self._values: typing.Dict[str, typing.Any] = {}
        if finding_publishing_frequency is not None:
            self._values["finding_publishing_frequency"] = finding_publishing_frequency
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def finding_publishing_frequency(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::Session.FindingPublishingFrequency``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-findingpublishingfrequency
        '''
        result = self._values.get("finding_publishing_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::Macie::Session.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-macie-session.html#cfn-macie-session-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSessionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCustomDataIdentifier",
    "CfnCustomDataIdentifierProps",
    "CfnFindingsFilter",
    "CfnFindingsFilterProps",
    "CfnSession",
    "CfnSessionProps",
]

publication.publish()
