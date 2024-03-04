'''
# AWS Web Application Firewall Construct Library

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
class CfnByteMatchSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-waf.CfnByteMatchSet",
):
    '''A CloudFormation ``AWS::WAF::ByteMatchSet``.

    :cloudformationResource: AWS::WAF::ByteMatchSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        byte_match_tuples: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnByteMatchSet.ByteMatchTupleProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::WAF::ByteMatchSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::WAF::ByteMatchSet.Name``.
        :param byte_match_tuples: ``AWS::WAF::ByteMatchSet.ByteMatchTuples``.
        '''
        props = CfnByteMatchSetProps(name=name, byte_match_tuples=byte_match_tuples)

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::WAF::ByteMatchSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="byteMatchTuples")
    def byte_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnByteMatchSet.ByteMatchTupleProperty"]]]]:
        '''``AWS::WAF::ByteMatchSet.ByteMatchTuples``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-bytematchtuples
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnByteMatchSet.ByteMatchTupleProperty"]]]], jsii.get(self, "byteMatchTuples"))

    @byte_match_tuples.setter
    def byte_match_tuples(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnByteMatchSet.ByteMatchTupleProperty"]]]],
    ) -> None:
        jsii.set(self, "byteMatchTuples", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnByteMatchSet.ByteMatchTupleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "positional_constraint": "positionalConstraint",
            "text_transformation": "textTransformation",
            "target_string": "targetString",
            "target_string_base64": "targetStringBase64",
        },
    )
    class ByteMatchTupleProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnByteMatchSet.FieldToMatchProperty"],
            positional_constraint: builtins.str,
            text_transformation: builtins.str,
            target_string: typing.Optional[builtins.str] = None,
            target_string_base64: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param field_to_match: ``CfnByteMatchSet.ByteMatchTupleProperty.FieldToMatch``.
            :param positional_constraint: ``CfnByteMatchSet.ByteMatchTupleProperty.PositionalConstraint``.
            :param text_transformation: ``CfnByteMatchSet.ByteMatchTupleProperty.TextTransformation``.
            :param target_string: ``CfnByteMatchSet.ByteMatchTupleProperty.TargetString``.
            :param target_string_base64: ``CfnByteMatchSet.ByteMatchTupleProperty.TargetStringBase64``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "field_to_match": field_to_match,
                "positional_constraint": positional_constraint,
                "text_transformation": text_transformation,
            }
            if target_string is not None:
                self._values["target_string"] = target_string
            if target_string_base64 is not None:
                self._values["target_string_base64"] = target_string_base64

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnByteMatchSet.FieldToMatchProperty"]:
            '''``CfnByteMatchSet.ByteMatchTupleProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnByteMatchSet.FieldToMatchProperty"], result)

        @builtins.property
        def positional_constraint(self) -> builtins.str:
            '''``CfnByteMatchSet.ByteMatchTupleProperty.PositionalConstraint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-positionalconstraint
            '''
            result = self._values.get("positional_constraint")
            assert result is not None, "Required property 'positional_constraint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def text_transformation(self) -> builtins.str:
            '''``CfnByteMatchSet.ByteMatchTupleProperty.TextTransformation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-texttransformation
            '''
            result = self._values.get("text_transformation")
            assert result is not None, "Required property 'text_transformation' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_string(self) -> typing.Optional[builtins.str]:
            '''``CfnByteMatchSet.ByteMatchTupleProperty.TargetString``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-targetstring
            '''
            result = self._values.get("target_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_string_base64(self) -> typing.Optional[builtins.str]:
            '''``CfnByteMatchSet.ByteMatchTupleProperty.TargetStringBase64``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-targetstringbase64
            '''
            result = self._values.get("target_string_base64")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ByteMatchTupleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnByteMatchSet.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "data": "data"},
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param type: ``CfnByteMatchSet.FieldToMatchProperty.Type``.
            :param data: ``CfnByteMatchSet.FieldToMatchProperty.Data``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if data is not None:
                self._values["data"] = data

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnByteMatchSet.FieldToMatchProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''``CfnByteMatchSet.FieldToMatchProperty.Data``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-waf.CfnByteMatchSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "byte_match_tuples": "byteMatchTuples"},
)
class CfnByteMatchSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        byte_match_tuples: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnByteMatchSet.ByteMatchTupleProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WAF::ByteMatchSet``.

        :param name: ``AWS::WAF::ByteMatchSet.Name``.
        :param byte_match_tuples: ``AWS::WAF::ByteMatchSet.ByteMatchTuples``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if byte_match_tuples is not None:
            self._values["byte_match_tuples"] = byte_match_tuples

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::WAF::ByteMatchSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def byte_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnByteMatchSet.ByteMatchTupleProperty]]]]:
        '''``AWS::WAF::ByteMatchSet.ByteMatchTuples``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-bytematchtuples
        '''
        result = self._values.get("byte_match_tuples")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnByteMatchSet.ByteMatchTupleProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnByteMatchSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnIPSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-waf.CfnIPSet",
):
    '''A CloudFormation ``AWS::WAF::IPSet``.

    :cloudformationResource: AWS::WAF::IPSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        ip_set_descriptors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnIPSet.IPSetDescriptorProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::WAF::IPSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::WAF::IPSet.Name``.
        :param ip_set_descriptors: ``AWS::WAF::IPSet.IPSetDescriptors``.
        '''
        props = CfnIPSetProps(name=name, ip_set_descriptors=ip_set_descriptors)

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::WAF::IPSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ipSetDescriptors")
    def ip_set_descriptors(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIPSet.IPSetDescriptorProperty"]]]]:
        '''``AWS::WAF::IPSet.IPSetDescriptors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-ipsetdescriptors
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIPSet.IPSetDescriptorProperty"]]]], jsii.get(self, "ipSetDescriptors"))

    @ip_set_descriptors.setter
    def ip_set_descriptors(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIPSet.IPSetDescriptorProperty"]]]],
    ) -> None:
        jsii.set(self, "ipSetDescriptors", value)

    @jsii.interface(jsii_type="@aws-cdk/aws-waf.CfnIPSet.IPSetDescriptorProperty")
    class IPSetDescriptorProperty(typing_extensions.Protocol):
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html
        '''

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="type")
        def type(self) -> builtins.str:
            '''``CfnIPSet.IPSetDescriptorProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-type
            '''
            ...

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="value")
        def value(self) -> builtins.str:
            '''``CfnIPSet.IPSetDescriptorProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-value
            '''
            ...


    class _IPSetDescriptorPropertyProxy:
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html
        '''

        __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-waf.CfnIPSet.IPSetDescriptorProperty"

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="type")
        def type(self) -> builtins.str:
            '''``CfnIPSet.IPSetDescriptorProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-type
            '''
            return typing.cast(builtins.str, jsii.get(self, "type"))

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="value")
        def value(self) -> builtins.str:
            '''``CfnIPSet.IPSetDescriptorProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-value
            '''
            return typing.cast(builtins.str, jsii.get(self, "value"))

    # Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
    typing.cast(typing.Any, IPSetDescriptorProperty).__jsii_proxy_class__ = lambda : _IPSetDescriptorPropertyProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-waf.CfnIPSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "ip_set_descriptors": "ipSetDescriptors"},
)
class CfnIPSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        ip_set_descriptors: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnIPSet.IPSetDescriptorProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WAF::IPSet``.

        :param name: ``AWS::WAF::IPSet.Name``.
        :param ip_set_descriptors: ``AWS::WAF::IPSet.IPSetDescriptors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if ip_set_descriptors is not None:
            self._values["ip_set_descriptors"] = ip_set_descriptors

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::WAF::IPSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_set_descriptors(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnIPSet.IPSetDescriptorProperty]]]]:
        '''``AWS::WAF::IPSet.IPSetDescriptors``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-ipsetdescriptors
        '''
        result = self._values.get("ip_set_descriptors")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnIPSet.IPSetDescriptorProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIPSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRule(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-waf.CfnRule",
):
    '''A CloudFormation ``AWS::WAF::Rule``.

    :cloudformationResource: AWS::WAF::Rule
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        metric_name: builtins.str,
        name: builtins.str,
        predicates: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRule.PredicateProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::WAF::Rule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param metric_name: ``AWS::WAF::Rule.MetricName``.
        :param name: ``AWS::WAF::Rule.Name``.
        :param predicates: ``AWS::WAF::Rule.Predicates``.
        '''
        props = CfnRuleProps(metric_name=metric_name, name=name, predicates=predicates)

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
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        '''``AWS::WAF::Rule.MetricName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-metricname
        '''
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        jsii.set(self, "metricName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::WAF::Rule.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="predicates")
    def predicates(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRule.PredicateProperty"]]]]:
        '''``AWS::WAF::Rule.Predicates``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-predicates
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRule.PredicateProperty"]]]], jsii.get(self, "predicates"))

    @predicates.setter
    def predicates(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRule.PredicateProperty"]]]],
    ) -> None:
        jsii.set(self, "predicates", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnRule.PredicateProperty",
        jsii_struct_bases=[],
        name_mapping={"data_id": "dataId", "negated": "negated", "type": "type"},
    )
    class PredicateProperty:
        def __init__(
            self,
            *,
            data_id: builtins.str,
            negated: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            type: builtins.str,
        ) -> None:
            '''
            :param data_id: ``CfnRule.PredicateProperty.DataId``.
            :param negated: ``CfnRule.PredicateProperty.Negated``.
            :param type: ``CfnRule.PredicateProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "data_id": data_id,
                "negated": negated,
                "type": type,
            }

        @builtins.property
        def data_id(self) -> builtins.str:
            '''``CfnRule.PredicateProperty.DataId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-dataid
            '''
            result = self._values.get("data_id")
            assert result is not None, "Required property 'data_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def negated(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnRule.PredicateProperty.Negated``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-negated
            '''
            result = self._values.get("negated")
            assert result is not None, "Required property 'negated' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnRule.PredicateProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PredicateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-waf.CfnRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "name": "name",
        "predicates": "predicates",
    },
)
class CfnRuleProps:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        name: builtins.str,
        predicates: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnRule.PredicateProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WAF::Rule``.

        :param metric_name: ``AWS::WAF::Rule.MetricName``.
        :param name: ``AWS::WAF::Rule.Name``.
        :param predicates: ``AWS::WAF::Rule.Predicates``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "metric_name": metric_name,
            "name": name,
        }
        if predicates is not None:
            self._values["predicates"] = predicates

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''``AWS::WAF::Rule.MetricName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-metricname
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::WAF::Rule.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def predicates(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnRule.PredicateProperty]]]]:
        '''``AWS::WAF::Rule.Predicates``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-predicates
        '''
        result = self._values.get("predicates")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnRule.PredicateProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSizeConstraintSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-waf.CfnSizeConstraintSet",
):
    '''A CloudFormation ``AWS::WAF::SizeConstraintSet``.

    :cloudformationResource: AWS::WAF::SizeConstraintSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        size_constraints: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnSizeConstraintSet.SizeConstraintProperty"]]],
    ) -> None:
        '''Create a new ``AWS::WAF::SizeConstraintSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::WAF::SizeConstraintSet.Name``.
        :param size_constraints: ``AWS::WAF::SizeConstraintSet.SizeConstraints``.
        '''
        props = CfnSizeConstraintSetProps(name=name, size_constraints=size_constraints)

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::WAF::SizeConstraintSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sizeConstraints")
    def size_constraints(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSizeConstraintSet.SizeConstraintProperty"]]]:
        '''``AWS::WAF::SizeConstraintSet.SizeConstraints``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-sizeconstraints
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSizeConstraintSet.SizeConstraintProperty"]]], jsii.get(self, "sizeConstraints"))

    @size_constraints.setter
    def size_constraints(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSizeConstraintSet.SizeConstraintProperty"]]],
    ) -> None:
        jsii.set(self, "sizeConstraints", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnSizeConstraintSet.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "data": "data"},
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param type: ``CfnSizeConstraintSet.FieldToMatchProperty.Type``.
            :param data: ``CfnSizeConstraintSet.FieldToMatchProperty.Data``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if data is not None:
                self._values["data"] = data

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnSizeConstraintSet.FieldToMatchProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''``CfnSizeConstraintSet.FieldToMatchProperty.Data``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnSizeConstraintSet.SizeConstraintProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "field_to_match": "fieldToMatch",
            "size": "size",
            "text_transformation": "textTransformation",
        },
    )
    class SizeConstraintProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnSizeConstraintSet.FieldToMatchProperty"],
            size: jsii.Number,
            text_transformation: builtins.str,
        ) -> None:
            '''
            :param comparison_operator: ``CfnSizeConstraintSet.SizeConstraintProperty.ComparisonOperator``.
            :param field_to_match: ``CfnSizeConstraintSet.SizeConstraintProperty.FieldToMatch``.
            :param size: ``CfnSizeConstraintSet.SizeConstraintProperty.Size``.
            :param text_transformation: ``CfnSizeConstraintSet.SizeConstraintProperty.TextTransformation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "field_to_match": field_to_match,
                "size": size,
                "text_transformation": text_transformation,
            }

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''``CfnSizeConstraintSet.SizeConstraintProperty.ComparisonOperator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnSizeConstraintSet.FieldToMatchProperty"]:
            '''``CfnSizeConstraintSet.SizeConstraintProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnSizeConstraintSet.FieldToMatchProperty"], result)

        @builtins.property
        def size(self) -> jsii.Number:
            '''``CfnSizeConstraintSet.SizeConstraintProperty.Size``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-size
            '''
            result = self._values.get("size")
            assert result is not None, "Required property 'size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def text_transformation(self) -> builtins.str:
            '''``CfnSizeConstraintSet.SizeConstraintProperty.TextTransformation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-texttransformation
            '''
            result = self._values.get("text_transformation")
            assert result is not None, "Required property 'text_transformation' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SizeConstraintProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-waf.CfnSizeConstraintSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "size_constraints": "sizeConstraints"},
)
class CfnSizeConstraintSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        size_constraints: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnSizeConstraintSet.SizeConstraintProperty]]],
    ) -> None:
        '''Properties for defining a ``AWS::WAF::SizeConstraintSet``.

        :param name: ``AWS::WAF::SizeConstraintSet.Name``.
        :param size_constraints: ``AWS::WAF::SizeConstraintSet.SizeConstraints``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "size_constraints": size_constraints,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::WAF::SizeConstraintSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size_constraints(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnSizeConstraintSet.SizeConstraintProperty]]]:
        '''``AWS::WAF::SizeConstraintSet.SizeConstraints``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-sizeconstraints
        '''
        result = self._values.get("size_constraints")
        assert result is not None, "Required property 'size_constraints' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnSizeConstraintSet.SizeConstraintProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSizeConstraintSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSqlInjectionMatchSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-waf.CfnSqlInjectionMatchSet",
):
    '''A CloudFormation ``AWS::WAF::SqlInjectionMatchSet``.

    :cloudformationResource: AWS::WAF::SqlInjectionMatchSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        sql_injection_match_tuples: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::WAF::SqlInjectionMatchSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::WAF::SqlInjectionMatchSet.Name``.
        :param sql_injection_match_tuples: ``AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuples``.
        '''
        props = CfnSqlInjectionMatchSetProps(
            name=name, sql_injection_match_tuples=sql_injection_match_tuples
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::WAF::SqlInjectionMatchSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sqlInjectionMatchTuples")
    def sql_injection_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty"]]]]:
        '''``AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuples``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty"]]]], jsii.get(self, "sqlInjectionMatchTuples"))

    @sql_injection_match_tuples.setter
    def sql_injection_match_tuples(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty"]]]],
    ) -> None:
        jsii.set(self, "sqlInjectionMatchTuples", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnSqlInjectionMatchSet.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "data": "data"},
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param type: ``CfnSqlInjectionMatchSet.FieldToMatchProperty.Type``.
            :param data: ``CfnSqlInjectionMatchSet.FieldToMatchProperty.Data``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if data is not None:
                self._values["data"] = data

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnSqlInjectionMatchSet.FieldToMatchProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''``CfnSqlInjectionMatchSet.FieldToMatchProperty.Data``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "text_transformation": "textTransformation",
        },
    )
    class SqlInjectionMatchTupleProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnSqlInjectionMatchSet.FieldToMatchProperty"],
            text_transformation: builtins.str,
        ) -> None:
            '''
            :param field_to_match: ``CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty.FieldToMatch``.
            :param text_transformation: ``CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty.TextTransformation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "field_to_match": field_to_match,
                "text_transformation": text_transformation,
            }

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnSqlInjectionMatchSet.FieldToMatchProperty"]:
            '''``CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnSqlInjectionMatchSet.FieldToMatchProperty"], result)

        @builtins.property
        def text_transformation(self) -> builtins.str:
            '''``CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty.TextTransformation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples-texttransformation
            '''
            result = self._values.get("text_transformation")
            assert result is not None, "Required property 'text_transformation' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqlInjectionMatchTupleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-waf.CfnSqlInjectionMatchSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "sql_injection_match_tuples": "sqlInjectionMatchTuples",
    },
)
class CfnSqlInjectionMatchSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        sql_injection_match_tuples: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WAF::SqlInjectionMatchSet``.

        :param name: ``AWS::WAF::SqlInjectionMatchSet.Name``.
        :param sql_injection_match_tuples: ``AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuples``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if sql_injection_match_tuples is not None:
            self._values["sql_injection_match_tuples"] = sql_injection_match_tuples

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::WAF::SqlInjectionMatchSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_injection_match_tuples(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty]]]]:
        '''``AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuples``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples
        '''
        result = self._values.get("sql_injection_match_tuples")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSqlInjectionMatchSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWebACL(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-waf.CfnWebACL",
):
    '''A CloudFormation ``AWS::WAF::WebACL``.

    :cloudformationResource: AWS::WAF::WebACL
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        default_action: typing.Union["CfnWebACL.WafActionProperty", aws_cdk.core.IResolvable],
        metric_name: builtins.str,
        name: builtins.str,
        rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ActivatedRuleProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::WAF::WebACL``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param default_action: ``AWS::WAF::WebACL.DefaultAction``.
        :param metric_name: ``AWS::WAF::WebACL.MetricName``.
        :param name: ``AWS::WAF::WebACL.Name``.
        :param rules: ``AWS::WAF::WebACL.Rules``.
        '''
        props = CfnWebACLProps(
            default_action=default_action,
            metric_name=metric_name,
            name=name,
            rules=rules,
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
    @jsii.member(jsii_name="defaultAction")
    def default_action(
        self,
    ) -> typing.Union["CfnWebACL.WafActionProperty", aws_cdk.core.IResolvable]:
        '''``AWS::WAF::WebACL.DefaultAction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-defaultaction
        '''
        return typing.cast(typing.Union["CfnWebACL.WafActionProperty", aws_cdk.core.IResolvable], jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(
        self,
        value: typing.Union["CfnWebACL.WafActionProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "defaultAction", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        '''``AWS::WAF::WebACL.MetricName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-metricname
        '''
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        jsii.set(self, "metricName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::WAF::WebACL.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ActivatedRuleProperty"]]]]:
        '''``AWS::WAF::WebACL.Rules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-rules
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ActivatedRuleProperty"]]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ActivatedRuleProperty"]]]],
    ) -> None:
        jsii.set(self, "rules", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnWebACL.ActivatedRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"priority": "priority", "rule_id": "ruleId", "action": "action"},
    )
    class ActivatedRuleProperty:
        def __init__(
            self,
            *,
            priority: jsii.Number,
            rule_id: builtins.str,
            action: typing.Optional[typing.Union["CfnWebACL.WafActionProperty", aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param priority: ``CfnWebACL.ActivatedRuleProperty.Priority``.
            :param rule_id: ``CfnWebACL.ActivatedRuleProperty.RuleId``.
            :param action: ``CfnWebACL.ActivatedRuleProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "priority": priority,
                "rule_id": rule_id,
            }
            if action is not None:
                self._values["action"] = action

        @builtins.property
        def priority(self) -> jsii.Number:
            '''``CfnWebACL.ActivatedRuleProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def rule_id(self) -> builtins.str:
            '''``CfnWebACL.ActivatedRuleProperty.RuleId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-ruleid
            '''
            result = self._values.get("rule_id")
            assert result is not None, "Required property 'rule_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def action(
            self,
        ) -> typing.Optional[typing.Union["CfnWebACL.WafActionProperty", aws_cdk.core.IResolvable]]:
            '''``CfnWebACL.ActivatedRuleProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[typing.Union["CfnWebACL.WafActionProperty", aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActivatedRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnWebACL.WafActionProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class WafActionProperty:
        def __init__(self, *, type: builtins.str) -> None:
            '''
            :param type: ``CfnWebACL.WafActionProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-action.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnWebACL.WafActionProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-action.html#cfn-waf-webacl-action-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WafActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-waf.CfnWebACLProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_action": "defaultAction",
        "metric_name": "metricName",
        "name": "name",
        "rules": "rules",
    },
)
class CfnWebACLProps:
    def __init__(
        self,
        *,
        default_action: typing.Union[CfnWebACL.WafActionProperty, aws_cdk.core.IResolvable],
        metric_name: builtins.str,
        name: builtins.str,
        rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnWebACL.ActivatedRuleProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WAF::WebACL``.

        :param default_action: ``AWS::WAF::WebACL.DefaultAction``.
        :param metric_name: ``AWS::WAF::WebACL.MetricName``.
        :param name: ``AWS::WAF::WebACL.Name``.
        :param rules: ``AWS::WAF::WebACL.Rules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "default_action": default_action,
            "metric_name": metric_name,
            "name": name,
        }
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def default_action(
        self,
    ) -> typing.Union[CfnWebACL.WafActionProperty, aws_cdk.core.IResolvable]:
        '''``AWS::WAF::WebACL.DefaultAction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-defaultaction
        '''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(typing.Union[CfnWebACL.WafActionProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''``AWS::WAF::WebACL.MetricName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-metricname
        '''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::WAF::WebACL.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnWebACL.ActivatedRuleProperty]]]]:
        '''``AWS::WAF::WebACL.Rules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-rules
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnWebACL.ActivatedRuleProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWebACLProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnXssMatchSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-waf.CfnXssMatchSet",
):
    '''A CloudFormation ``AWS::WAF::XssMatchSet``.

    :cloudformationResource: AWS::WAF::XssMatchSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        xss_match_tuples: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnXssMatchSet.XssMatchTupleProperty"]]],
    ) -> None:
        '''Create a new ``AWS::WAF::XssMatchSet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::WAF::XssMatchSet.Name``.
        :param xss_match_tuples: ``AWS::WAF::XssMatchSet.XssMatchTuples``.
        '''
        props = CfnXssMatchSetProps(name=name, xss_match_tuples=xss_match_tuples)

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::WAF::XssMatchSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="xssMatchTuples")
    def xss_match_tuples(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnXssMatchSet.XssMatchTupleProperty"]]]:
        '''``AWS::WAF::XssMatchSet.XssMatchTuples``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-xssmatchtuples
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnXssMatchSet.XssMatchTupleProperty"]]], jsii.get(self, "xssMatchTuples"))

    @xss_match_tuples.setter
    def xss_match_tuples(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnXssMatchSet.XssMatchTupleProperty"]]],
    ) -> None:
        jsii.set(self, "xssMatchTuples", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnXssMatchSet.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "data": "data"},
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param type: ``CfnXssMatchSet.FieldToMatchProperty.Type``.
            :param data: ``CfnXssMatchSet.FieldToMatchProperty.Data``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
            }
            if data is not None:
                self._values["data"] = data

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnXssMatchSet.FieldToMatchProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data(self) -> typing.Optional[builtins.str]:
            '''``CfnXssMatchSet.FieldToMatchProperty.Data``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch-data
            '''
            result = self._values.get("data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-waf.CfnXssMatchSet.XssMatchTupleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "text_transformation": "textTransformation",
        },
    )
    class XssMatchTupleProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnXssMatchSet.FieldToMatchProperty"],
            text_transformation: builtins.str,
        ) -> None:
            '''
            :param field_to_match: ``CfnXssMatchSet.XssMatchTupleProperty.FieldToMatch``.
            :param text_transformation: ``CfnXssMatchSet.XssMatchTupleProperty.TextTransformation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "field_to_match": field_to_match,
                "text_transformation": text_transformation,
            }

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnXssMatchSet.FieldToMatchProperty"]:
            '''``CfnXssMatchSet.XssMatchTupleProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnXssMatchSet.FieldToMatchProperty"], result)

        @builtins.property
        def text_transformation(self) -> builtins.str:
            '''``CfnXssMatchSet.XssMatchTupleProperty.TextTransformation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html#cfn-waf-xssmatchset-xssmatchtuple-texttransformation
            '''
            result = self._values.get("text_transformation")
            assert result is not None, "Required property 'text_transformation' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "XssMatchTupleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-waf.CfnXssMatchSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "xss_match_tuples": "xssMatchTuples"},
)
class CfnXssMatchSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        xss_match_tuples: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnXssMatchSet.XssMatchTupleProperty]]],
    ) -> None:
        '''Properties for defining a ``AWS::WAF::XssMatchSet``.

        :param name: ``AWS::WAF::XssMatchSet.Name``.
        :param xss_match_tuples: ``AWS::WAF::XssMatchSet.XssMatchTuples``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "xss_match_tuples": xss_match_tuples,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::WAF::XssMatchSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def xss_match_tuples(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnXssMatchSet.XssMatchTupleProperty]]]:
        '''``AWS::WAF::XssMatchSet.XssMatchTuples``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-xssmatchtuples
        '''
        result = self._values.get("xss_match_tuples")
        assert result is not None, "Required property 'xss_match_tuples' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnXssMatchSet.XssMatchTupleProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnXssMatchSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnByteMatchSet",
    "CfnByteMatchSetProps",
    "CfnIPSet",
    "CfnIPSetProps",
    "CfnRule",
    "CfnRuleProps",
    "CfnSizeConstraintSet",
    "CfnSizeConstraintSetProps",
    "CfnSqlInjectionMatchSet",
    "CfnSqlInjectionMatchSetProps",
    "CfnWebACL",
    "CfnWebACLProps",
    "CfnXssMatchSet",
    "CfnXssMatchSetProps",
]

publication.publish()
