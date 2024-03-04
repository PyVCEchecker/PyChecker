'''
# AWS::WAFv2 Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_wafv2 as wafv2
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
class CfnIPSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-wafv2.CfnIPSet",
):
    '''A CloudFormation ``AWS::WAFv2::IPSet``.

    :cloudformationResource: AWS::WAFv2::IPSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html
    '''

    def __init__(
        self,
        scope_: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        addresses: typing.Sequence[builtins.str],
        ip_address_version: builtins.str,
        scope: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::WAFv2::IPSet``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param addresses: ``AWS::WAFv2::IPSet.Addresses``.
        :param ip_address_version: ``AWS::WAFv2::IPSet.IPAddressVersion``.
        :param scope: ``AWS::WAFv2::IPSet.Scope``.
        :param description: ``AWS::WAFv2::IPSet.Description``.
        :param name: ``AWS::WAFv2::IPSet.Name``.
        :param tags: ``AWS::WAFv2::IPSet.Tags``.
        '''
        props = CfnIPSetProps(
            addresses=addresses,
            ip_address_version=ip_address_version,
            scope=scope,
            description=description,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::WAFv2::IPSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> typing.List[builtins.str]:
        '''``AWS::WAFv2::IPSet.Addresses``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-addresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addresses"))

    @addresses.setter
    def addresses(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "addresses", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ipAddressVersion")
    def ip_address_version(self) -> builtins.str:
        '''``AWS::WAFv2::IPSet.IPAddressVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-ipaddressversion
        '''
        return typing.cast(builtins.str, jsii.get(self, "ipAddressVersion"))

    @ip_address_version.setter
    def ip_address_version(self, value: builtins.str) -> None:
        jsii.set(self, "ipAddressVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        '''``AWS::WAFv2::IPSet.Scope``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-scope
        '''
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        jsii.set(self, "scope", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::IPSet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::IPSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-wafv2.CfnIPSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "addresses": "addresses",
        "ip_address_version": "ipAddressVersion",
        "scope": "scope",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnIPSetProps:
    def __init__(
        self,
        *,
        addresses: typing.Sequence[builtins.str],
        ip_address_version: builtins.str,
        scope: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WAFv2::IPSet``.

        :param addresses: ``AWS::WAFv2::IPSet.Addresses``.
        :param ip_address_version: ``AWS::WAFv2::IPSet.IPAddressVersion``.
        :param scope: ``AWS::WAFv2::IPSet.Scope``.
        :param description: ``AWS::WAFv2::IPSet.Description``.
        :param name: ``AWS::WAFv2::IPSet.Name``.
        :param tags: ``AWS::WAFv2::IPSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "addresses": addresses,
            "ip_address_version": ip_address_version,
            "scope": scope,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def addresses(self) -> typing.List[builtins.str]:
        '''``AWS::WAFv2::IPSet.Addresses``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-addresses
        '''
        result = self._values.get("addresses")
        assert result is not None, "Required property 'addresses' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def ip_address_version(self) -> builtins.str:
        '''``AWS::WAFv2::IPSet.IPAddressVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-ipaddressversion
        '''
        result = self._values.get("ip_address_version")
        assert result is not None, "Required property 'ip_address_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''``AWS::WAFv2::IPSet.Scope``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::IPSet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::IPSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::WAFv2::IPSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html#cfn-wafv2-ipset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIPSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLoggingConfiguration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-wafv2.CfnLoggingConfiguration",
):
    '''A CloudFormation ``AWS::WAFv2::LoggingConfiguration``.

    :cloudformationResource: AWS::WAFv2::LoggingConfiguration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        log_destination_configs: typing.Sequence[builtins.str],
        resource_arn: builtins.str,
        logging_filter: typing.Any = None,
        redacted_fields: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.FieldToMatchProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::WAFv2::LoggingConfiguration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param log_destination_configs: ``AWS::WAFv2::LoggingConfiguration.LogDestinationConfigs``.
        :param resource_arn: ``AWS::WAFv2::LoggingConfiguration.ResourceArn``.
        :param logging_filter: ``AWS::WAFv2::LoggingConfiguration.LoggingFilter``.
        :param redacted_fields: ``AWS::WAFv2::LoggingConfiguration.RedactedFields``.
        '''
        props = CfnLoggingConfigurationProps(
            log_destination_configs=log_destination_configs,
            resource_arn=resource_arn,
            logging_filter=logging_filter,
            redacted_fields=redacted_fields,
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
    @jsii.member(jsii_name="attrManagedByFirewallManager")
    def attr_managed_by_firewall_manager(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: ManagedByFirewallManager
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrManagedByFirewallManager"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="logDestinationConfigs")
    def log_destination_configs(self) -> typing.List[builtins.str]:
        '''``AWS::WAFv2::LoggingConfiguration.LogDestinationConfigs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-logdestinationconfigs
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "logDestinationConfigs"))

    @log_destination_configs.setter
    def log_destination_configs(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "logDestinationConfigs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loggingFilter")
    def logging_filter(self) -> typing.Any:
        '''``AWS::WAFv2::LoggingConfiguration.LoggingFilter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-loggingfilter
        '''
        return typing.cast(typing.Any, jsii.get(self, "loggingFilter"))

    @logging_filter.setter
    def logging_filter(self, value: typing.Any) -> None:
        jsii.set(self, "loggingFilter", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''``AWS::WAFv2::LoggingConfiguration.ResourceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-resourcearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        jsii.set(self, "resourceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="redactedFields")
    def redacted_fields(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.FieldToMatchProperty"]]]]:
        '''``AWS::WAFv2::LoggingConfiguration.RedactedFields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-redactedfields
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.FieldToMatchProperty"]]]], jsii.get(self, "redactedFields"))

    @redacted_fields.setter
    def redacted_fields(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLoggingConfiguration.FieldToMatchProperty"]]]],
    ) -> None:
        jsii.set(self, "redactedFields", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnLoggingConfiguration.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "json_body": "jsonBody",
            "method": "method",
            "query_string": "queryString",
            "single_header": "singleHeader",
            "uri_path": "uriPath",
        },
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            json_body: typing.Any = None,
            method: typing.Any = None,
            query_string: typing.Any = None,
            single_header: typing.Any = None,
            uri_path: typing.Any = None,
        ) -> None:
            '''
            :param json_body: ``CfnLoggingConfiguration.FieldToMatchProperty.JsonBody``.
            :param method: ``CfnLoggingConfiguration.FieldToMatchProperty.Method``.
            :param query_string: ``CfnLoggingConfiguration.FieldToMatchProperty.QueryString``.
            :param single_header: ``CfnLoggingConfiguration.FieldToMatchProperty.SingleHeader``.
            :param uri_path: ``CfnLoggingConfiguration.FieldToMatchProperty.UriPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if json_body is not None:
                self._values["json_body"] = json_body
            if method is not None:
                self._values["method"] = method
            if query_string is not None:
                self._values["query_string"] = query_string
            if single_header is not None:
                self._values["single_header"] = single_header
            if uri_path is not None:
                self._values["uri_path"] = uri_path

        @builtins.property
        def json_body(self) -> typing.Any:
            '''``CfnLoggingConfiguration.FieldToMatchProperty.JsonBody``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-jsonbody
            '''
            result = self._values.get("json_body")
            return typing.cast(typing.Any, result)

        @builtins.property
        def method(self) -> typing.Any:
            '''``CfnLoggingConfiguration.FieldToMatchProperty.Method``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Any, result)

        @builtins.property
        def query_string(self) -> typing.Any:
            '''``CfnLoggingConfiguration.FieldToMatchProperty.QueryString``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-querystring
            '''
            result = self._values.get("query_string")
            return typing.cast(typing.Any, result)

        @builtins.property
        def single_header(self) -> typing.Any:
            '''``CfnLoggingConfiguration.FieldToMatchProperty.SingleHeader``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-singleheader
            '''
            result = self._values.get("single_header")
            return typing.cast(typing.Any, result)

        @builtins.property
        def uri_path(self) -> typing.Any:
            '''``CfnLoggingConfiguration.FieldToMatchProperty.UriPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-loggingconfiguration-fieldtomatch.html#cfn-wafv2-loggingconfiguration-fieldtomatch-uripath
            '''
            result = self._values.get("uri_path")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-wafv2.CfnLoggingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_destination_configs": "logDestinationConfigs",
        "resource_arn": "resourceArn",
        "logging_filter": "loggingFilter",
        "redacted_fields": "redactedFields",
    },
)
class CfnLoggingConfigurationProps:
    def __init__(
        self,
        *,
        log_destination_configs: typing.Sequence[builtins.str],
        resource_arn: builtins.str,
        logging_filter: typing.Any = None,
        redacted_fields: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnLoggingConfiguration.FieldToMatchProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WAFv2::LoggingConfiguration``.

        :param log_destination_configs: ``AWS::WAFv2::LoggingConfiguration.LogDestinationConfigs``.
        :param resource_arn: ``AWS::WAFv2::LoggingConfiguration.ResourceArn``.
        :param logging_filter: ``AWS::WAFv2::LoggingConfiguration.LoggingFilter``.
        :param redacted_fields: ``AWS::WAFv2::LoggingConfiguration.RedactedFields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "log_destination_configs": log_destination_configs,
            "resource_arn": resource_arn,
        }
        if logging_filter is not None:
            self._values["logging_filter"] = logging_filter
        if redacted_fields is not None:
            self._values["redacted_fields"] = redacted_fields

    @builtins.property
    def log_destination_configs(self) -> typing.List[builtins.str]:
        '''``AWS::WAFv2::LoggingConfiguration.LogDestinationConfigs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-logdestinationconfigs
        '''
        result = self._values.get("log_destination_configs")
        assert result is not None, "Required property 'log_destination_configs' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''``AWS::WAFv2::LoggingConfiguration.ResourceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def logging_filter(self) -> typing.Any:
        '''``AWS::WAFv2::LoggingConfiguration.LoggingFilter``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-loggingfilter
        '''
        result = self._values.get("logging_filter")
        return typing.cast(typing.Any, result)

    @builtins.property
    def redacted_fields(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnLoggingConfiguration.FieldToMatchProperty]]]]:
        '''``AWS::WAFv2::LoggingConfiguration.RedactedFields``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-loggingconfiguration.html#cfn-wafv2-loggingconfiguration-redactedfields
        '''
        result = self._values.get("redacted_fields")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnLoggingConfiguration.FieldToMatchProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoggingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRegexPatternSet(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-wafv2.CfnRegexPatternSet",
):
    '''A CloudFormation ``AWS::WAFv2::RegexPatternSet``.

    :cloudformationResource: AWS::WAFv2::RegexPatternSet
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html
    '''

    def __init__(
        self,
        scope_: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        regular_expression_list: typing.Sequence[builtins.str],
        scope: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::WAFv2::RegexPatternSet``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param regular_expression_list: ``AWS::WAFv2::RegexPatternSet.RegularExpressionList``.
        :param scope: ``AWS::WAFv2::RegexPatternSet.Scope``.
        :param description: ``AWS::WAFv2::RegexPatternSet.Description``.
        :param name: ``AWS::WAFv2::RegexPatternSet.Name``.
        :param tags: ``AWS::WAFv2::RegexPatternSet.Tags``.
        '''
        props = CfnRegexPatternSetProps(
            regular_expression_list=regular_expression_list,
            scope=scope,
            description=description,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::WAFv2::RegexPatternSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="regularExpressionList")
    def regular_expression_list(self) -> typing.List[builtins.str]:
        '''``AWS::WAFv2::RegexPatternSet.RegularExpressionList``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-regularexpressionlist
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regularExpressionList"))

    @regular_expression_list.setter
    def regular_expression_list(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "regularExpressionList", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        '''``AWS::WAFv2::RegexPatternSet.Scope``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-scope
        '''
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        jsii.set(self, "scope", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::RegexPatternSet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::RegexPatternSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-wafv2.CfnRegexPatternSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "regular_expression_list": "regularExpressionList",
        "scope": "scope",
        "description": "description",
        "name": "name",
        "tags": "tags",
    },
)
class CfnRegexPatternSetProps:
    def __init__(
        self,
        *,
        regular_expression_list: typing.Sequence[builtins.str],
        scope: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WAFv2::RegexPatternSet``.

        :param regular_expression_list: ``AWS::WAFv2::RegexPatternSet.RegularExpressionList``.
        :param scope: ``AWS::WAFv2::RegexPatternSet.Scope``.
        :param description: ``AWS::WAFv2::RegexPatternSet.Description``.
        :param name: ``AWS::WAFv2::RegexPatternSet.Name``.
        :param tags: ``AWS::WAFv2::RegexPatternSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "regular_expression_list": regular_expression_list,
            "scope": scope,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def regular_expression_list(self) -> typing.List[builtins.str]:
        '''``AWS::WAFv2::RegexPatternSet.RegularExpressionList``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-regularexpressionlist
        '''
        result = self._values.get("regular_expression_list")
        assert result is not None, "Required property 'regular_expression_list' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''``AWS::WAFv2::RegexPatternSet.Scope``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::RegexPatternSet.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::RegexPatternSet.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::WAFv2::RegexPatternSet.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html#cfn-wafv2-regexpatternset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRegexPatternSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnRuleGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup",
):
    '''A CloudFormation ``AWS::WAFv2::RuleGroup``.

    :cloudformationResource: AWS::WAFv2::RuleGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html
    '''

    def __init__(
        self,
        scope_: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        capacity: jsii.Number,
        scope: builtins.str,
        visibility_config: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.VisibilityConfigProperty"],
        custom_response_bodies: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.CustomResponseBodyProperty"]]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleProperty"]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::WAFv2::RuleGroup``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param capacity: ``AWS::WAFv2::RuleGroup.Capacity``.
        :param scope: ``AWS::WAFv2::RuleGroup.Scope``.
        :param visibility_config: ``AWS::WAFv2::RuleGroup.VisibilityConfig``.
        :param custom_response_bodies: ``AWS::WAFv2::RuleGroup.CustomResponseBodies``.
        :param description: ``AWS::WAFv2::RuleGroup.Description``.
        :param name: ``AWS::WAFv2::RuleGroup.Name``.
        :param rules: ``AWS::WAFv2::RuleGroup.Rules``.
        :param tags: ``AWS::WAFv2::RuleGroup.Tags``.
        '''
        props = CfnRuleGroupProps(
            capacity=capacity,
            scope=scope,
            visibility_config=visibility_config,
            custom_response_bodies=custom_response_bodies,
            description=description,
            name=name,
            rules=rules,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

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
    @jsii.member(jsii_name="attrAvailableLabels")
    def attr_available_labels(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: AvailableLabels
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrAvailableLabels"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrConsumedLabels")
    def attr_consumed_labels(self) -> aws_cdk.core.IResolvable:
        '''
        :cloudformationAttribute: ConsumedLabels
        '''
        return typing.cast(aws_cdk.core.IResolvable, jsii.get(self, "attrConsumedLabels"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLabelNamespace")
    def attr_label_namespace(self) -> builtins.str:
        '''
        :cloudformationAttribute: LabelNamespace
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLabelNamespace"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::WAFv2::RuleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        '''``AWS::WAFv2::RuleGroup.Capacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-capacity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        jsii.set(self, "capacity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        '''``AWS::WAFv2::RuleGroup.Scope``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-scope
        '''
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        jsii.set(self, "scope", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="visibilityConfig")
    def visibility_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.VisibilityConfigProperty"]:
        '''``AWS::WAFv2::RuleGroup.VisibilityConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-visibilityconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.VisibilityConfigProperty"], jsii.get(self, "visibilityConfig"))

    @visibility_config.setter
    def visibility_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.VisibilityConfigProperty"],
    ) -> None:
        jsii.set(self, "visibilityConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customResponseBodies")
    def custom_response_bodies(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.CustomResponseBodyProperty"]]]]:
        '''``AWS::WAFv2::RuleGroup.CustomResponseBodies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-customresponsebodies
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.CustomResponseBodyProperty"]]]], jsii.get(self, "customResponseBodies"))

    @custom_response_bodies.setter
    def custom_response_bodies(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.CustomResponseBodyProperty"]]]],
    ) -> None:
        jsii.set(self, "customResponseBodies", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::RuleGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::RuleGroup.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleProperty"]]]]:
        '''``AWS::WAFv2::RuleGroup.Rules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-rules
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleProperty"]]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleProperty"]]]],
    ) -> None:
        jsii.set(self, "rules", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.AndStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"statements": "statements"},
    )
    class AndStatementProperty:
        def __init__(
            self,
            *,
            statements: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]]],
        ) -> None:
            '''
            :param statements: ``CfnRuleGroup.AndStatementProperty.Statements``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "statements": statements,
            }

        @builtins.property
        def statements(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]]]:
            '''``CfnRuleGroup.AndStatementProperty.Statements``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-andstatement.html#cfn-wafv2-rulegroup-andstatement-statements
            '''
            result = self._values.get("statements")
            assert result is not None, "Required property 'statements' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AndStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.ByteMatchStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "positional_constraint": "positionalConstraint",
            "text_transformations": "textTransformations",
            "search_string": "searchString",
            "search_string_base64": "searchStringBase64",
        },
    )
    class ByteMatchStatementProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"],
            positional_constraint: builtins.str,
            text_transformations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]],
            search_string: typing.Optional[builtins.str] = None,
            search_string_base64: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param field_to_match: ``CfnRuleGroup.ByteMatchStatementProperty.FieldToMatch``.
            :param positional_constraint: ``CfnRuleGroup.ByteMatchStatementProperty.PositionalConstraint``.
            :param text_transformations: ``CfnRuleGroup.ByteMatchStatementProperty.TextTransformations``.
            :param search_string: ``CfnRuleGroup.ByteMatchStatementProperty.SearchString``.
            :param search_string_base64: ``CfnRuleGroup.ByteMatchStatementProperty.SearchStringBase64``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "field_to_match": field_to_match,
                "positional_constraint": positional_constraint,
                "text_transformations": text_transformations,
            }
            if search_string is not None:
                self._values["search_string"] = search_string
            if search_string_base64 is not None:
                self._values["search_string_base64"] = search_string_base64

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"]:
            '''``CfnRuleGroup.ByteMatchStatementProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"], result)

        @builtins.property
        def positional_constraint(self) -> builtins.str:
            '''``CfnRuleGroup.ByteMatchStatementProperty.PositionalConstraint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-positionalconstraint
            '''
            result = self._values.get("positional_constraint")
            assert result is not None, "Required property 'positional_constraint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def text_transformations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]]:
            '''``CfnRuleGroup.ByteMatchStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-texttransformations
            '''
            result = self._values.get("text_transformations")
            assert result is not None, "Required property 'text_transformations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]], result)

        @builtins.property
        def search_string(self) -> typing.Optional[builtins.str]:
            '''``CfnRuleGroup.ByteMatchStatementProperty.SearchString``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstring
            '''
            result = self._values.get("search_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def search_string_base64(self) -> typing.Optional[builtins.str]:
            '''``CfnRuleGroup.ByteMatchStatementProperty.SearchStringBase64``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-bytematchstatement.html#cfn-wafv2-rulegroup-bytematchstatement-searchstringbase64
            '''
            result = self._values.get("search_string_base64")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ByteMatchStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.CustomResponseBodyProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content", "content_type": "contentType"},
    )
    class CustomResponseBodyProperty:
        def __init__(
            self,
            *,
            content: builtins.str,
            content_type: builtins.str,
        ) -> None:
            '''
            :param content: ``CfnRuleGroup.CustomResponseBodyProperty.Content``.
            :param content_type: ``CfnRuleGroup.CustomResponseBodyProperty.ContentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "content": content,
                "content_type": content_type,
            }

        @builtins.property
        def content(self) -> builtins.str:
            '''``CfnRuleGroup.CustomResponseBodyProperty.Content``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html#cfn-wafv2-rulegroup-customresponsebody-content
            '''
            result = self._values.get("content")
            assert result is not None, "Required property 'content' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def content_type(self) -> builtins.str:
            '''``CfnRuleGroup.CustomResponseBodyProperty.ContentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-customresponsebody.html#cfn-wafv2-rulegroup-customresponsebody-contenttype
            '''
            result = self._values.get("content_type")
            assert result is not None, "Required property 'content_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomResponseBodyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "all_query_arguments": "allQueryArguments",
            "body": "body",
            "json_body": "jsonBody",
            "method": "method",
            "query_string": "queryString",
            "single_header": "singleHeader",
            "single_query_argument": "singleQueryArgument",
            "uri_path": "uriPath",
        },
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            all_query_arguments: typing.Any = None,
            body: typing.Any = None,
            json_body: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.JsonBodyProperty"]] = None,
            method: typing.Any = None,
            query_string: typing.Any = None,
            single_header: typing.Any = None,
            single_query_argument: typing.Any = None,
            uri_path: typing.Any = None,
        ) -> None:
            '''
            :param all_query_arguments: ``CfnRuleGroup.FieldToMatchProperty.AllQueryArguments``.
            :param body: ``CfnRuleGroup.FieldToMatchProperty.Body``.
            :param json_body: ``CfnRuleGroup.FieldToMatchProperty.JsonBody``.
            :param method: ``CfnRuleGroup.FieldToMatchProperty.Method``.
            :param query_string: ``CfnRuleGroup.FieldToMatchProperty.QueryString``.
            :param single_header: ``CfnRuleGroup.FieldToMatchProperty.SingleHeader``.
            :param single_query_argument: ``CfnRuleGroup.FieldToMatchProperty.SingleQueryArgument``.
            :param uri_path: ``CfnRuleGroup.FieldToMatchProperty.UriPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if all_query_arguments is not None:
                self._values["all_query_arguments"] = all_query_arguments
            if body is not None:
                self._values["body"] = body
            if json_body is not None:
                self._values["json_body"] = json_body
            if method is not None:
                self._values["method"] = method
            if query_string is not None:
                self._values["query_string"] = query_string
            if single_header is not None:
                self._values["single_header"] = single_header
            if single_query_argument is not None:
                self._values["single_query_argument"] = single_query_argument
            if uri_path is not None:
                self._values["uri_path"] = uri_path

        @builtins.property
        def all_query_arguments(self) -> typing.Any:
            '''``CfnRuleGroup.FieldToMatchProperty.AllQueryArguments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-allqueryarguments
            '''
            result = self._values.get("all_query_arguments")
            return typing.cast(typing.Any, result)

        @builtins.property
        def body(self) -> typing.Any:
            '''``CfnRuleGroup.FieldToMatchProperty.Body``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Any, result)

        @builtins.property
        def json_body(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.JsonBodyProperty"]]:
            '''``CfnRuleGroup.FieldToMatchProperty.JsonBody``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-jsonbody
            '''
            result = self._values.get("json_body")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.JsonBodyProperty"]], result)

        @builtins.property
        def method(self) -> typing.Any:
            '''``CfnRuleGroup.FieldToMatchProperty.Method``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Any, result)

        @builtins.property
        def query_string(self) -> typing.Any:
            '''``CfnRuleGroup.FieldToMatchProperty.QueryString``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-querystring
            '''
            result = self._values.get("query_string")
            return typing.cast(typing.Any, result)

        @builtins.property
        def single_header(self) -> typing.Any:
            '''``CfnRuleGroup.FieldToMatchProperty.SingleHeader``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singleheader
            '''
            result = self._values.get("single_header")
            return typing.cast(typing.Any, result)

        @builtins.property
        def single_query_argument(self) -> typing.Any:
            '''``CfnRuleGroup.FieldToMatchProperty.SingleQueryArgument``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-singlequeryargument
            '''
            result = self._values.get("single_query_argument")
            return typing.cast(typing.Any, result)

        @builtins.property
        def uri_path(self) -> typing.Any:
            '''``CfnRuleGroup.FieldToMatchProperty.UriPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-fieldtomatch.html#cfn-wafv2-rulegroup-fieldtomatch-uripath
            '''
            result = self._values.get("uri_path")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.ForwardedIPConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fallback_behavior": "fallbackBehavior",
            "header_name": "headerName",
        },
    )
    class ForwardedIPConfigurationProperty:
        def __init__(
            self,
            *,
            fallback_behavior: builtins.str,
            header_name: builtins.str,
        ) -> None:
            '''
            :param fallback_behavior: ``CfnRuleGroup.ForwardedIPConfigurationProperty.FallbackBehavior``.
            :param header_name: ``CfnRuleGroup.ForwardedIPConfigurationProperty.HeaderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "fallback_behavior": fallback_behavior,
                "header_name": header_name,
            }

        @builtins.property
        def fallback_behavior(self) -> builtins.str:
            '''``CfnRuleGroup.ForwardedIPConfigurationProperty.FallbackBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html#cfn-wafv2-rulegroup-forwardedipconfiguration-fallbackbehavior
            '''
            result = self._values.get("fallback_behavior")
            assert result is not None, "Required property 'fallback_behavior' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def header_name(self) -> builtins.str:
            '''``CfnRuleGroup.ForwardedIPConfigurationProperty.HeaderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-forwardedipconfiguration.html#cfn-wafv2-rulegroup-forwardedipconfiguration-headername
            '''
            result = self._values.get("header_name")
            assert result is not None, "Required property 'header_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ForwardedIPConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.GeoMatchStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "country_codes": "countryCodes",
            "forwarded_ip_config": "forwardedIpConfig",
        },
    )
    class GeoMatchStatementProperty:
        def __init__(
            self,
            *,
            country_codes: typing.Optional[typing.Sequence[builtins.str]] = None,
            forwarded_ip_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ForwardedIPConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param country_codes: ``CfnRuleGroup.GeoMatchStatementProperty.CountryCodes``.
            :param forwarded_ip_config: ``CfnRuleGroup.GeoMatchStatementProperty.ForwardedIPConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if country_codes is not None:
                self._values["country_codes"] = country_codes
            if forwarded_ip_config is not None:
                self._values["forwarded_ip_config"] = forwarded_ip_config

        @builtins.property
        def country_codes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRuleGroup.GeoMatchStatementProperty.CountryCodes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html#cfn-wafv2-rulegroup-geomatchstatement-countrycodes
            '''
            result = self._values.get("country_codes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def forwarded_ip_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ForwardedIPConfigurationProperty"]]:
            '''``CfnRuleGroup.GeoMatchStatementProperty.ForwardedIPConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-geomatchstatement.html#cfn-wafv2-rulegroup-geomatchstatement-forwardedipconfig
            '''
            result = self._values.get("forwarded_ip_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ForwardedIPConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoMatchStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.interface(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.IPSetForwardedIPConfigurationProperty"
    )
    class IPSetForwardedIPConfigurationProperty(typing_extensions.Protocol):
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html
        '''

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="fallbackBehavior")
        def fallback_behavior(self) -> builtins.str:
            '''``CfnRuleGroup.IPSetForwardedIPConfigurationProperty.FallbackBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-fallbackbehavior
            '''
            ...

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="headerName")
        def header_name(self) -> builtins.str:
            '''``CfnRuleGroup.IPSetForwardedIPConfigurationProperty.HeaderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-headername
            '''
            ...

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="position")
        def position(self) -> builtins.str:
            '''``CfnRuleGroup.IPSetForwardedIPConfigurationProperty.Position``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-position
            '''
            ...


    class _IPSetForwardedIPConfigurationPropertyProxy:
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html
        '''

        __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-wafv2.CfnRuleGroup.IPSetForwardedIPConfigurationProperty"

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="fallbackBehavior")
        def fallback_behavior(self) -> builtins.str:
            '''``CfnRuleGroup.IPSetForwardedIPConfigurationProperty.FallbackBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-fallbackbehavior
            '''
            return typing.cast(builtins.str, jsii.get(self, "fallbackBehavior"))

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="headerName")
        def header_name(self) -> builtins.str:
            '''``CfnRuleGroup.IPSetForwardedIPConfigurationProperty.HeaderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-headername
            '''
            return typing.cast(builtins.str, jsii.get(self, "headerName"))

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="position")
        def position(self) -> builtins.str:
            '''``CfnRuleGroup.IPSetForwardedIPConfigurationProperty.Position``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetforwardedipconfiguration.html#cfn-wafv2-rulegroup-ipsetforwardedipconfiguration-position
            '''
            return typing.cast(builtins.str, jsii.get(self, "position"))

    # Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
    typing.cast(typing.Any, IPSetForwardedIPConfigurationProperty).__jsii_proxy_class__ = lambda : _IPSetForwardedIPConfigurationPropertyProxy

    @jsii.interface(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.IPSetReferenceStatementProperty"
    )
    class IPSetReferenceStatementProperty(typing_extensions.Protocol):
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html
        '''

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="arn")
        def arn(self) -> builtins.str:
            '''``CfnRuleGroup.IPSetReferenceStatementProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-arn
            '''
            ...

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="ipSetForwardedIpConfig")
        def ip_set_forwarded_ip_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.IPSetForwardedIPConfigurationProperty"]]:
            '''``CfnRuleGroup.IPSetReferenceStatementProperty.IPSetForwardedIPConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-ipsetforwardedipconfig
            '''
            ...


    class _IPSetReferenceStatementPropertyProxy:
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html
        '''

        __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-wafv2.CfnRuleGroup.IPSetReferenceStatementProperty"

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="arn")
        def arn(self) -> builtins.str:
            '''``CfnRuleGroup.IPSetReferenceStatementProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-arn
            '''
            return typing.cast(builtins.str, jsii.get(self, "arn"))

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="ipSetForwardedIpConfig")
        def ip_set_forwarded_ip_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.IPSetForwardedIPConfigurationProperty"]]:
            '''``CfnRuleGroup.IPSetReferenceStatementProperty.IPSetForwardedIPConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ipsetreferencestatement.html#cfn-wafv2-rulegroup-ipsetreferencestatement-ipsetforwardedipconfig
            '''
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.IPSetForwardedIPConfigurationProperty"]], jsii.get(self, "ipSetForwardedIpConfig"))

    # Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
    typing.cast(typing.Any, IPSetReferenceStatementProperty).__jsii_proxy_class__ = lambda : _IPSetReferenceStatementPropertyProxy

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.JsonBodyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "match_pattern": "matchPattern",
            "match_scope": "matchScope",
            "invalid_fallback_behavior": "invalidFallbackBehavior",
        },
    )
    class JsonBodyProperty:
        def __init__(
            self,
            *,
            match_pattern: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.JsonMatchPatternProperty"],
            match_scope: builtins.str,
            invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param match_pattern: ``CfnRuleGroup.JsonBodyProperty.MatchPattern``.
            :param match_scope: ``CfnRuleGroup.JsonBodyProperty.MatchScope``.
            :param invalid_fallback_behavior: ``CfnRuleGroup.JsonBodyProperty.InvalidFallbackBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "match_pattern": match_pattern,
                "match_scope": match_scope,
            }
            if invalid_fallback_behavior is not None:
                self._values["invalid_fallback_behavior"] = invalid_fallback_behavior

        @builtins.property
        def match_pattern(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.JsonMatchPatternProperty"]:
            '''``CfnRuleGroup.JsonBodyProperty.MatchPattern``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-matchpattern
            '''
            result = self._values.get("match_pattern")
            assert result is not None, "Required property 'match_pattern' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.JsonMatchPatternProperty"], result)

        @builtins.property
        def match_scope(self) -> builtins.str:
            '''``CfnRuleGroup.JsonBodyProperty.MatchScope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-matchscope
            '''
            result = self._values.get("match_scope")
            assert result is not None, "Required property 'match_scope' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invalid_fallback_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnRuleGroup.JsonBodyProperty.InvalidFallbackBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonbody.html#cfn-wafv2-rulegroup-jsonbody-invalidfallbackbehavior
            '''
            result = self._values.get("invalid_fallback_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonBodyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.JsonMatchPatternProperty",
        jsii_struct_bases=[],
        name_mapping={"all": "all", "included_paths": "includedPaths"},
    )
    class JsonMatchPatternProperty:
        def __init__(
            self,
            *,
            all: typing.Any = None,
            included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param all: ``CfnRuleGroup.JsonMatchPatternProperty.All``.
            :param included_paths: ``CfnRuleGroup.JsonMatchPatternProperty.IncludedPaths``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if all is not None:
                self._values["all"] = all
            if included_paths is not None:
                self._values["included_paths"] = included_paths

        @builtins.property
        def all(self) -> typing.Any:
            '''``CfnRuleGroup.JsonMatchPatternProperty.All``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html#cfn-wafv2-rulegroup-jsonmatchpattern-all
            '''
            result = self._values.get("all")
            return typing.cast(typing.Any, result)

        @builtins.property
        def included_paths(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnRuleGroup.JsonMatchPatternProperty.IncludedPaths``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-jsonmatchpattern.html#cfn-wafv2-rulegroup-jsonmatchpattern-includedpaths
            '''
            result = self._values.get("included_paths")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonMatchPatternProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.LabelMatchStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "scope": "scope"},
    )
    class LabelMatchStatementProperty:
        def __init__(self, *, key: builtins.str, scope: builtins.str) -> None:
            '''
            :param key: ``CfnRuleGroup.LabelMatchStatementProperty.Key``.
            :param scope: ``CfnRuleGroup.LabelMatchStatementProperty.Scope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "scope": scope,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnRuleGroup.LabelMatchStatementProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html#cfn-wafv2-rulegroup-labelmatchstatement-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scope(self) -> builtins.str:
            '''``CfnRuleGroup.LabelMatchStatementProperty.Scope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelmatchstatement.html#cfn-wafv2-rulegroup-labelmatchstatement-scope
            '''
            result = self._values.get("scope")
            assert result is not None, "Required property 'scope' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelMatchStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.LabelProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class LabelProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''
            :param name: ``CfnRuleGroup.LabelProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-label.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnRuleGroup.LabelProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-label.html#cfn-wafv2-rulegroup-label-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.LabelSummaryProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class LabelSummaryProperty:
        def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
            '''
            :param name: ``CfnRuleGroup.LabelSummaryProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelsummary.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnRuleGroup.LabelSummaryProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-labelsummary.html#cfn-wafv2-rulegroup-labelsummary-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelSummaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.NotStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"statement": "statement"},
    )
    class NotStatementProperty:
        def __init__(
            self,
            *,
            statement: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"],
        ) -> None:
            '''
            :param statement: ``CfnRuleGroup.NotStatementProperty.Statement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "statement": statement,
            }

        @builtins.property
        def statement(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]:
            '''``CfnRuleGroup.NotStatementProperty.Statement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-notstatement.html#cfn-wafv2-rulegroup-notstatement-statement
            '''
            result = self._values.get("statement")
            assert result is not None, "Required property 'statement' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.OrStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"statements": "statements"},
    )
    class OrStatementProperty:
        def __init__(
            self,
            *,
            statements: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]]],
        ) -> None:
            '''
            :param statements: ``CfnRuleGroup.OrStatementProperty.Statements``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "statements": statements,
            }

        @builtins.property
        def statements(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]]]:
            '''``CfnRuleGroup.OrStatementProperty.Statements``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-orstatement.html#cfn-wafv2-rulegroup-orstatement-statements
            '''
            result = self._values.get("statements")
            assert result is not None, "Required property 'statements' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.RateBasedStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregate_key_type": "aggregateKeyType",
            "limit": "limit",
            "forwarded_ip_config": "forwardedIpConfig",
            "scope_down_statement": "scopeDownStatement",
        },
    )
    class RateBasedStatementProperty:
        def __init__(
            self,
            *,
            aggregate_key_type: builtins.str,
            limit: jsii.Number,
            forwarded_ip_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ForwardedIPConfigurationProperty"]] = None,
            scope_down_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]] = None,
        ) -> None:
            '''
            :param aggregate_key_type: ``CfnRuleGroup.RateBasedStatementProperty.AggregateKeyType``.
            :param limit: ``CfnRuleGroup.RateBasedStatementProperty.Limit``.
            :param forwarded_ip_config: ``CfnRuleGroup.RateBasedStatementProperty.ForwardedIPConfig``.
            :param scope_down_statement: ``CfnRuleGroup.RateBasedStatementProperty.ScopeDownStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "aggregate_key_type": aggregate_key_type,
                "limit": limit,
            }
            if forwarded_ip_config is not None:
                self._values["forwarded_ip_config"] = forwarded_ip_config
            if scope_down_statement is not None:
                self._values["scope_down_statement"] = scope_down_statement

        @builtins.property
        def aggregate_key_type(self) -> builtins.str:
            '''``CfnRuleGroup.RateBasedStatementProperty.AggregateKeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-aggregatekeytype
            '''
            result = self._values.get("aggregate_key_type")
            assert result is not None, "Required property 'aggregate_key_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def limit(self) -> jsii.Number:
            '''``CfnRuleGroup.RateBasedStatementProperty.Limit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-limit
            '''
            result = self._values.get("limit")
            assert result is not None, "Required property 'limit' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def forwarded_ip_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ForwardedIPConfigurationProperty"]]:
            '''``CfnRuleGroup.RateBasedStatementProperty.ForwardedIPConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-forwardedipconfig
            '''
            result = self._values.get("forwarded_ip_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ForwardedIPConfigurationProperty"]], result)

        @builtins.property
        def scope_down_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]]:
            '''``CfnRuleGroup.RateBasedStatementProperty.ScopeDownStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ratebasedstatement.html#cfn-wafv2-rulegroup-ratebasedstatement-scopedownstatement
            '''
            result = self._values.get("scope_down_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RateBasedStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.RegexPatternSetReferenceStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "field_to_match": "fieldToMatch",
            "text_transformations": "textTransformations",
        },
    )
    class RegexPatternSetReferenceStatementProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"],
            text_transformations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]],
        ) -> None:
            '''
            :param arn: ``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.Arn``.
            :param field_to_match: ``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "field_to_match": field_to_match,
                "text_transformations": text_transformations,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"]:
            '''``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"], result)

        @builtins.property
        def text_transformations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]]:
            '''``CfnRuleGroup.RegexPatternSetReferenceStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-regexpatternsetreferencestatement.html#cfn-wafv2-rulegroup-regexpatternsetreferencestatement-texttransformations
            '''
            result = self._values.get("text_transformations")
            assert result is not None, "Required property 'text_transformations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegexPatternSetReferenceStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.RuleActionProperty",
        jsii_struct_bases=[],
        name_mapping={"allow": "allow", "block": "block", "count": "count"},
    )
    class RuleActionProperty:
        def __init__(
            self,
            *,
            allow: typing.Any = None,
            block: typing.Any = None,
            count: typing.Any = None,
        ) -> None:
            '''
            :param allow: ``CfnRuleGroup.RuleActionProperty.Allow``.
            :param block: ``CfnRuleGroup.RuleActionProperty.Block``.
            :param count: ``CfnRuleGroup.RuleActionProperty.Count``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if allow is not None:
                self._values["allow"] = allow
            if block is not None:
                self._values["block"] = block
            if count is not None:
                self._values["count"] = count

        @builtins.property
        def allow(self) -> typing.Any:
            '''``CfnRuleGroup.RuleActionProperty.Allow``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-allow
            '''
            result = self._values.get("allow")
            return typing.cast(typing.Any, result)

        @builtins.property
        def block(self) -> typing.Any:
            '''``CfnRuleGroup.RuleActionProperty.Block``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-block
            '''
            result = self._values.get("block")
            return typing.cast(typing.Any, result)

        @builtins.property
        def count(self) -> typing.Any:
            '''``CfnRuleGroup.RuleActionProperty.Count``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-ruleaction.html#cfn-wafv2-rulegroup-ruleaction-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "priority": "priority",
            "statement": "statement",
            "visibility_config": "visibilityConfig",
            "action": "action",
            "rule_labels": "ruleLabels",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            priority: jsii.Number,
            statement: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"],
            visibility_config: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.VisibilityConfigProperty"],
            action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleActionProperty"]] = None,
            rule_labels: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.LabelProperty"]]]] = None,
        ) -> None:
            '''
            :param name: ``CfnRuleGroup.RuleProperty.Name``.
            :param priority: ``CfnRuleGroup.RuleProperty.Priority``.
            :param statement: ``CfnRuleGroup.RuleProperty.Statement``.
            :param visibility_config: ``CfnRuleGroup.RuleProperty.VisibilityConfig``.
            :param action: ``CfnRuleGroup.RuleProperty.Action``.
            :param rule_labels: ``CfnRuleGroup.RuleProperty.RuleLabels``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "priority": priority,
                "statement": statement,
                "visibility_config": visibility_config,
            }
            if action is not None:
                self._values["action"] = action
            if rule_labels is not None:
                self._values["rule_labels"] = rule_labels

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnRuleGroup.RuleProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def priority(self) -> jsii.Number:
            '''``CfnRuleGroup.RuleProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def statement(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"]:
            '''``CfnRuleGroup.RuleProperty.Statement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-statement
            '''
            result = self._values.get("statement")
            assert result is not None, "Required property 'statement' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.StatementProperty"], result)

        @builtins.property
        def visibility_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.VisibilityConfigProperty"]:
            '''``CfnRuleGroup.RuleProperty.VisibilityConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-visibilityconfig
            '''
            result = self._values.get("visibility_config")
            assert result is not None, "Required property 'visibility_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.VisibilityConfigProperty"], result)

        @builtins.property
        def action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleActionProperty"]]:
            '''``CfnRuleGroup.RuleProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RuleActionProperty"]], result)

        @builtins.property
        def rule_labels(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.LabelProperty"]]]]:
            '''``CfnRuleGroup.RuleProperty.RuleLabels``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-rule.html#cfn-wafv2-rulegroup-rule-rulelabels
            '''
            result = self._values.get("rule_labels")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.LabelProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.SizeConstraintStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "field_to_match": "fieldToMatch",
            "size": "size",
            "text_transformations": "textTransformations",
        },
    )
    class SizeConstraintStatementProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"],
            size: jsii.Number,
            text_transformations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]],
        ) -> None:
            '''
            :param comparison_operator: ``CfnRuleGroup.SizeConstraintStatementProperty.ComparisonOperator``.
            :param field_to_match: ``CfnRuleGroup.SizeConstraintStatementProperty.FieldToMatch``.
            :param size: ``CfnRuleGroup.SizeConstraintStatementProperty.Size``.
            :param text_transformations: ``CfnRuleGroup.SizeConstraintStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "field_to_match": field_to_match,
                "size": size,
                "text_transformations": text_transformations,
            }

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''``CfnRuleGroup.SizeConstraintStatementProperty.ComparisonOperator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"]:
            '''``CfnRuleGroup.SizeConstraintStatementProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"], result)

        @builtins.property
        def size(self) -> jsii.Number:
            '''``CfnRuleGroup.SizeConstraintStatementProperty.Size``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-size
            '''
            result = self._values.get("size")
            assert result is not None, "Required property 'size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def text_transformations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]]:
            '''``CfnRuleGroup.SizeConstraintStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sizeconstraintstatement.html#cfn-wafv2-rulegroup-sizeconstraintstatement-texttransformations
            '''
            result = self._values.get("text_transformations")
            assert result is not None, "Required property 'text_transformations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SizeConstraintStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.SqliMatchStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "text_transformations": "textTransformations",
        },
    )
    class SqliMatchStatementProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"],
            text_transformations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]],
        ) -> None:
            '''
            :param field_to_match: ``CfnRuleGroup.SqliMatchStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnRuleGroup.SqliMatchStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "field_to_match": field_to_match,
                "text_transformations": text_transformations,
            }

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"]:
            '''``CfnRuleGroup.SqliMatchStatementProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"], result)

        @builtins.property
        def text_transformations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]]:
            '''``CfnRuleGroup.SqliMatchStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-sqlimatchstatement.html#cfn-wafv2-rulegroup-sqlimatchstatement-texttransformations
            '''
            result = self._values.get("text_transformations")
            assert result is not None, "Required property 'text_transformations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqliMatchStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.StatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_statement": "andStatement",
            "byte_match_statement": "byteMatchStatement",
            "geo_match_statement": "geoMatchStatement",
            "ip_set_reference_statement": "ipSetReferenceStatement",
            "label_match_statement": "labelMatchStatement",
            "not_statement": "notStatement",
            "or_statement": "orStatement",
            "rate_based_statement": "rateBasedStatement",
            "regex_pattern_set_reference_statement": "regexPatternSetReferenceStatement",
            "size_constraint_statement": "sizeConstraintStatement",
            "sqli_match_statement": "sqliMatchStatement",
            "xss_match_statement": "xssMatchStatement",
        },
    )
    class StatementProperty:
        def __init__(
            self,
            *,
            and_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.AndStatementProperty"]] = None,
            byte_match_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ByteMatchStatementProperty"]] = None,
            geo_match_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.GeoMatchStatementProperty"]] = None,
            ip_set_reference_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.IPSetReferenceStatementProperty"]] = None,
            label_match_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.LabelMatchStatementProperty"]] = None,
            not_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.NotStatementProperty"]] = None,
            or_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.OrStatementProperty"]] = None,
            rate_based_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RateBasedStatementProperty"]] = None,
            regex_pattern_set_reference_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RegexPatternSetReferenceStatementProperty"]] = None,
            size_constraint_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.SizeConstraintStatementProperty"]] = None,
            sqli_match_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.SqliMatchStatementProperty"]] = None,
            xss_match_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.XssMatchStatementProperty"]] = None,
        ) -> None:
            '''
            :param and_statement: ``CfnRuleGroup.StatementProperty.AndStatement``.
            :param byte_match_statement: ``CfnRuleGroup.StatementProperty.ByteMatchStatement``.
            :param geo_match_statement: ``CfnRuleGroup.StatementProperty.GeoMatchStatement``.
            :param ip_set_reference_statement: ``CfnRuleGroup.StatementProperty.IPSetReferenceStatement``.
            :param label_match_statement: ``CfnRuleGroup.StatementProperty.LabelMatchStatement``.
            :param not_statement: ``CfnRuleGroup.StatementProperty.NotStatement``.
            :param or_statement: ``CfnRuleGroup.StatementProperty.OrStatement``.
            :param rate_based_statement: ``CfnRuleGroup.StatementProperty.RateBasedStatement``.
            :param regex_pattern_set_reference_statement: ``CfnRuleGroup.StatementProperty.RegexPatternSetReferenceStatement``.
            :param size_constraint_statement: ``CfnRuleGroup.StatementProperty.SizeConstraintStatement``.
            :param sqli_match_statement: ``CfnRuleGroup.StatementProperty.SqliMatchStatement``.
            :param xss_match_statement: ``CfnRuleGroup.StatementProperty.XssMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if and_statement is not None:
                self._values["and_statement"] = and_statement
            if byte_match_statement is not None:
                self._values["byte_match_statement"] = byte_match_statement
            if geo_match_statement is not None:
                self._values["geo_match_statement"] = geo_match_statement
            if ip_set_reference_statement is not None:
                self._values["ip_set_reference_statement"] = ip_set_reference_statement
            if label_match_statement is not None:
                self._values["label_match_statement"] = label_match_statement
            if not_statement is not None:
                self._values["not_statement"] = not_statement
            if or_statement is not None:
                self._values["or_statement"] = or_statement
            if rate_based_statement is not None:
                self._values["rate_based_statement"] = rate_based_statement
            if regex_pattern_set_reference_statement is not None:
                self._values["regex_pattern_set_reference_statement"] = regex_pattern_set_reference_statement
            if size_constraint_statement is not None:
                self._values["size_constraint_statement"] = size_constraint_statement
            if sqli_match_statement is not None:
                self._values["sqli_match_statement"] = sqli_match_statement
            if xss_match_statement is not None:
                self._values["xss_match_statement"] = xss_match_statement

        @builtins.property
        def and_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.AndStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.AndStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-andstatement
            '''
            result = self._values.get("and_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.AndStatementProperty"]], result)

        @builtins.property
        def byte_match_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ByteMatchStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.ByteMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-bytematchstatement
            '''
            result = self._values.get("byte_match_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.ByteMatchStatementProperty"]], result)

        @builtins.property
        def geo_match_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.GeoMatchStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.GeoMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-geomatchstatement
            '''
            result = self._values.get("geo_match_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.GeoMatchStatementProperty"]], result)

        @builtins.property
        def ip_set_reference_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.IPSetReferenceStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.IPSetReferenceStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-ipsetreferencestatement
            '''
            result = self._values.get("ip_set_reference_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.IPSetReferenceStatementProperty"]], result)

        @builtins.property
        def label_match_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.LabelMatchStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.LabelMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-labelmatchstatement
            '''
            result = self._values.get("label_match_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.LabelMatchStatementProperty"]], result)

        @builtins.property
        def not_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.NotStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.NotStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-notstatement
            '''
            result = self._values.get("not_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.NotStatementProperty"]], result)

        @builtins.property
        def or_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.OrStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.OrStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-orstatement
            '''
            result = self._values.get("or_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.OrStatementProperty"]], result)

        @builtins.property
        def rate_based_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RateBasedStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.RateBasedStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-ratebasedstatement
            '''
            result = self._values.get("rate_based_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RateBasedStatementProperty"]], result)

        @builtins.property
        def regex_pattern_set_reference_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RegexPatternSetReferenceStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.RegexPatternSetReferenceStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-regexpatternsetreferencestatement
            '''
            result = self._values.get("regex_pattern_set_reference_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.RegexPatternSetReferenceStatementProperty"]], result)

        @builtins.property
        def size_constraint_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.SizeConstraintStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.SizeConstraintStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-sizeconstraintstatement
            '''
            result = self._values.get("size_constraint_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.SizeConstraintStatementProperty"]], result)

        @builtins.property
        def sqli_match_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.SqliMatchStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.SqliMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-sqlimatchstatement
            '''
            result = self._values.get("sqli_match_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.SqliMatchStatementProperty"]], result)

        @builtins.property
        def xss_match_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.XssMatchStatementProperty"]]:
            '''``CfnRuleGroup.StatementProperty.XssMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-statement.html#cfn-wafv2-rulegroup-statement-xssmatchstatement
            '''
            result = self._values.get("xss_match_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.XssMatchStatementProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.TextTransformationProperty",
        jsii_struct_bases=[],
        name_mapping={"priority": "priority", "type": "type"},
    )
    class TextTransformationProperty:
        def __init__(self, *, priority: jsii.Number, type: builtins.str) -> None:
            '''
            :param priority: ``CfnRuleGroup.TextTransformationProperty.Priority``.
            :param type: ``CfnRuleGroup.TextTransformationProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "priority": priority,
                "type": type,
            }

        @builtins.property
        def priority(self) -> jsii.Number:
            '''``CfnRuleGroup.TextTransformationProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html#cfn-wafv2-rulegroup-texttransformation-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnRuleGroup.TextTransformationProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-texttransformation.html#cfn-wafv2-rulegroup-texttransformation-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextTransformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.VisibilityConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_metrics_enabled": "cloudWatchMetricsEnabled",
            "metric_name": "metricName",
            "sampled_requests_enabled": "sampledRequestsEnabled",
        },
    )
    class VisibilityConfigProperty:
        def __init__(
            self,
            *,
            cloud_watch_metrics_enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            metric_name: builtins.str,
            sampled_requests_enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        ) -> None:
            '''
            :param cloud_watch_metrics_enabled: ``CfnRuleGroup.VisibilityConfigProperty.CloudWatchMetricsEnabled``.
            :param metric_name: ``CfnRuleGroup.VisibilityConfigProperty.MetricName``.
            :param sampled_requests_enabled: ``CfnRuleGroup.VisibilityConfigProperty.SampledRequestsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cloud_watch_metrics_enabled": cloud_watch_metrics_enabled,
                "metric_name": metric_name,
                "sampled_requests_enabled": sampled_requests_enabled,
            }

        @builtins.property
        def cloud_watch_metrics_enabled(
            self,
        ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnRuleGroup.VisibilityConfigProperty.CloudWatchMetricsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-cloudwatchmetricsenabled
            '''
            result = self._values.get("cloud_watch_metrics_enabled")
            assert result is not None, "Required property 'cloud_watch_metrics_enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''``CfnRuleGroup.VisibilityConfigProperty.MetricName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sampled_requests_enabled(
            self,
        ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnRuleGroup.VisibilityConfigProperty.SampledRequestsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-visibilityconfig.html#cfn-wafv2-rulegroup-visibilityconfig-sampledrequestsenabled
            '''
            result = self._values.get("sampled_requests_enabled")
            assert result is not None, "Required property 'sampled_requests_enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VisibilityConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroup.XssMatchStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "text_transformations": "textTransformations",
        },
    )
    class XssMatchStatementProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"],
            text_transformations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]],
        ) -> None:
            '''
            :param field_to_match: ``CfnRuleGroup.XssMatchStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnRuleGroup.XssMatchStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "field_to_match": field_to_match,
                "text_transformations": text_transformations,
            }

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"]:
            '''``CfnRuleGroup.XssMatchStatementProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html#cfn-wafv2-rulegroup-xssmatchstatement-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.FieldToMatchProperty"], result)

        @builtins.property
        def text_transformations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]]:
            '''``CfnRuleGroup.XssMatchStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-rulegroup-xssmatchstatement.html#cfn-wafv2-rulegroup-xssmatchstatement-texttransformations
            '''
            result = self._values.get("text_transformations")
            assert result is not None, "Required property 'text_transformations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRuleGroup.TextTransformationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "XssMatchStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-wafv2.CfnRuleGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "capacity": "capacity",
        "scope": "scope",
        "visibility_config": "visibilityConfig",
        "custom_response_bodies": "customResponseBodies",
        "description": "description",
        "name": "name",
        "rules": "rules",
        "tags": "tags",
    },
)
class CfnRuleGroupProps:
    def __init__(
        self,
        *,
        capacity: jsii.Number,
        scope: builtins.str,
        visibility_config: typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.VisibilityConfigProperty],
        custom_response_bodies: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.CustomResponseBodyProperty]]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.RuleProperty]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WAFv2::RuleGroup``.

        :param capacity: ``AWS::WAFv2::RuleGroup.Capacity``.
        :param scope: ``AWS::WAFv2::RuleGroup.Scope``.
        :param visibility_config: ``AWS::WAFv2::RuleGroup.VisibilityConfig``.
        :param custom_response_bodies: ``AWS::WAFv2::RuleGroup.CustomResponseBodies``.
        :param description: ``AWS::WAFv2::RuleGroup.Description``.
        :param name: ``AWS::WAFv2::RuleGroup.Name``.
        :param rules: ``AWS::WAFv2::RuleGroup.Rules``.
        :param tags: ``AWS::WAFv2::RuleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "capacity": capacity,
            "scope": scope,
            "visibility_config": visibility_config,
        }
        if custom_response_bodies is not None:
            self._values["custom_response_bodies"] = custom_response_bodies
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if rules is not None:
            self._values["rules"] = rules
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def capacity(self) -> jsii.Number:
        '''``AWS::WAFv2::RuleGroup.Capacity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-capacity
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''``AWS::WAFv2::RuleGroup.Scope``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def visibility_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.VisibilityConfigProperty]:
        '''``AWS::WAFv2::RuleGroup.VisibilityConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-visibilityconfig
        '''
        result = self._values.get("visibility_config")
        assert result is not None, "Required property 'visibility_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.VisibilityConfigProperty], result)

    @builtins.property
    def custom_response_bodies(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.CustomResponseBodyProperty]]]]:
        '''``AWS::WAFv2::RuleGroup.CustomResponseBodies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-customresponsebodies
        '''
        result = self._values.get("custom_response_bodies")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.CustomResponseBodyProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::RuleGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::RuleGroup.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.RuleProperty]]]]:
        '''``AWS::WAFv2::RuleGroup.Rules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-rules
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnRuleGroup.RuleProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::WAFv2::RuleGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html#cfn-wafv2-rulegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWebACL(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-wafv2.CfnWebACL",
):
    '''A CloudFormation ``AWS::WAFv2::WebACL``.

    :cloudformationResource: AWS::WAFv2::WebACL
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html
    '''

    def __init__(
        self,
        scope_: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        default_action: typing.Union["CfnWebACL.DefaultActionProperty", aws_cdk.core.IResolvable],
        scope: builtins.str,
        visibility_config: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.VisibilityConfigProperty"],
        custom_response_bodies: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomResponseBodyProperty"]]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleProperty"]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::WAFv2::WebACL``.

        :param scope_: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param default_action: ``AWS::WAFv2::WebACL.DefaultAction``.
        :param scope: ``AWS::WAFv2::WebACL.Scope``.
        :param visibility_config: ``AWS::WAFv2::WebACL.VisibilityConfig``.
        :param custom_response_bodies: ``AWS::WAFv2::WebACL.CustomResponseBodies``.
        :param description: ``AWS::WAFv2::WebACL.Description``.
        :param name: ``AWS::WAFv2::WebACL.Name``.
        :param rules: ``AWS::WAFv2::WebACL.Rules``.
        :param tags: ``AWS::WAFv2::WebACL.Tags``.
        '''
        props = CfnWebACLProps(
            default_action=default_action,
            scope=scope,
            visibility_config=visibility_config,
            custom_response_bodies=custom_response_bodies,
            description=description,
            name=name,
            rules=rules,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

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
    @jsii.member(jsii_name="attrCapacity")
    def attr_capacity(self) -> jsii.Number:
        '''
        :cloudformationAttribute: Capacity
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCapacity"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrLabelNamespace")
    def attr_label_namespace(self) -> builtins.str:
        '''
        :cloudformationAttribute: LabelNamespace
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLabelNamespace"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::WAFv2::WebACL.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultAction")
    def default_action(
        self,
    ) -> typing.Union["CfnWebACL.DefaultActionProperty", aws_cdk.core.IResolvable]:
        '''``AWS::WAFv2::WebACL.DefaultAction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-defaultaction
        '''
        return typing.cast(typing.Union["CfnWebACL.DefaultActionProperty", aws_cdk.core.IResolvable], jsii.get(self, "defaultAction"))

    @default_action.setter
    def default_action(
        self,
        value: typing.Union["CfnWebACL.DefaultActionProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "defaultAction", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        '''``AWS::WAFv2::WebACL.Scope``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-scope
        '''
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        jsii.set(self, "scope", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="visibilityConfig")
    def visibility_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.VisibilityConfigProperty"]:
        '''``AWS::WAFv2::WebACL.VisibilityConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-visibilityconfig
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.VisibilityConfigProperty"], jsii.get(self, "visibilityConfig"))

    @visibility_config.setter
    def visibility_config(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.VisibilityConfigProperty"],
    ) -> None:
        jsii.set(self, "visibilityConfig", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customResponseBodies")
    def custom_response_bodies(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomResponseBodyProperty"]]]]:
        '''``AWS::WAFv2::WebACL.CustomResponseBodies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-customresponsebodies
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomResponseBodyProperty"]]]], jsii.get(self, "customResponseBodies"))

    @custom_response_bodies.setter
    def custom_response_bodies(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomResponseBodyProperty"]]]],
    ) -> None:
        jsii.set(self, "customResponseBodies", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::WebACL.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::WebACL.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleProperty"]]]]:
        '''``AWS::WAFv2::WebACL.Rules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-rules
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleProperty"]]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleProperty"]]]],
    ) -> None:
        jsii.set(self, "rules", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.AllowActionProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_request_handling": "customRequestHandling"},
    )
    class AllowActionProperty:
        def __init__(
            self,
            *,
            custom_request_handling: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomRequestHandlingProperty"]] = None,
        ) -> None:
            '''
            :param custom_request_handling: ``CfnWebACL.AllowActionProperty.CustomRequestHandling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_request_handling is not None:
                self._values["custom_request_handling"] = custom_request_handling

        @builtins.property
        def custom_request_handling(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomRequestHandlingProperty"]]:
            '''``CfnWebACL.AllowActionProperty.CustomRequestHandling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-allowaction.html#cfn-wafv2-webacl-allowaction-customrequesthandling
            '''
            result = self._values.get("custom_request_handling")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomRequestHandlingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AllowActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.AndStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"statements": "statements"},
    )
    class AndStatementProperty:
        def __init__(
            self,
            *,
            statements: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]]],
        ) -> None:
            '''
            :param statements: ``CfnWebACL.AndStatementProperty.Statements``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "statements": statements,
            }

        @builtins.property
        def statements(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]]]:
            '''``CfnWebACL.AndStatementProperty.Statements``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-andstatement.html#cfn-wafv2-webacl-andstatement-statements
            '''
            result = self._values.get("statements")
            assert result is not None, "Required property 'statements' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AndStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.BlockActionProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_response": "customResponse"},
    )
    class BlockActionProperty:
        def __init__(
            self,
            *,
            custom_response: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomResponseProperty"]] = None,
        ) -> None:
            '''
            :param custom_response: ``CfnWebACL.BlockActionProperty.CustomResponse``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_response is not None:
                self._values["custom_response"] = custom_response

        @builtins.property
        def custom_response(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomResponseProperty"]]:
            '''``CfnWebACL.BlockActionProperty.CustomResponse``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-blockaction.html#cfn-wafv2-webacl-blockaction-customresponse
            '''
            result = self._values.get("custom_response")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomResponseProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlockActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.ByteMatchStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "positional_constraint": "positionalConstraint",
            "text_transformations": "textTransformations",
            "search_string": "searchString",
            "search_string_base64": "searchStringBase64",
        },
    )
    class ByteMatchStatementProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"],
            positional_constraint: builtins.str,
            text_transformations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]],
            search_string: typing.Optional[builtins.str] = None,
            search_string_base64: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param field_to_match: ``CfnWebACL.ByteMatchStatementProperty.FieldToMatch``.
            :param positional_constraint: ``CfnWebACL.ByteMatchStatementProperty.PositionalConstraint``.
            :param text_transformations: ``CfnWebACL.ByteMatchStatementProperty.TextTransformations``.
            :param search_string: ``CfnWebACL.ByteMatchStatementProperty.SearchString``.
            :param search_string_base64: ``CfnWebACL.ByteMatchStatementProperty.SearchStringBase64``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "field_to_match": field_to_match,
                "positional_constraint": positional_constraint,
                "text_transformations": text_transformations,
            }
            if search_string is not None:
                self._values["search_string"] = search_string
            if search_string_base64 is not None:
                self._values["search_string_base64"] = search_string_base64

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"]:
            '''``CfnWebACL.ByteMatchStatementProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"], result)

        @builtins.property
        def positional_constraint(self) -> builtins.str:
            '''``CfnWebACL.ByteMatchStatementProperty.PositionalConstraint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-positionalconstraint
            '''
            result = self._values.get("positional_constraint")
            assert result is not None, "Required property 'positional_constraint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def text_transformations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]]:
            '''``CfnWebACL.ByteMatchStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-texttransformations
            '''
            result = self._values.get("text_transformations")
            assert result is not None, "Required property 'text_transformations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]], result)

        @builtins.property
        def search_string(self) -> typing.Optional[builtins.str]:
            '''``CfnWebACL.ByteMatchStatementProperty.SearchString``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-searchstring
            '''
            result = self._values.get("search_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def search_string_base64(self) -> typing.Optional[builtins.str]:
            '''``CfnWebACL.ByteMatchStatementProperty.SearchStringBase64``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-bytematchstatement.html#cfn-wafv2-webacl-bytematchstatement-searchstringbase64
            '''
            result = self._values.get("search_string_base64")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ByteMatchStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.CountActionProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_request_handling": "customRequestHandling"},
    )
    class CountActionProperty:
        def __init__(
            self,
            *,
            custom_request_handling: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomRequestHandlingProperty"]] = None,
        ) -> None:
            '''
            :param custom_request_handling: ``CfnWebACL.CountActionProperty.CustomRequestHandling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_request_handling is not None:
                self._values["custom_request_handling"] = custom_request_handling

        @builtins.property
        def custom_request_handling(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomRequestHandlingProperty"]]:
            '''``CfnWebACL.CountActionProperty.CustomRequestHandling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-countaction.html#cfn-wafv2-webacl-countaction-customrequesthandling
            '''
            result = self._values.get("custom_request_handling")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomRequestHandlingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CountActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.CustomHTTPHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class CustomHTTPHeaderProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''
            :param name: ``CfnWebACL.CustomHTTPHeaderProperty.Name``.
            :param value: ``CfnWebACL.CustomHTTPHeaderProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnWebACL.CustomHTTPHeaderProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html#cfn-wafv2-webacl-customhttpheader-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnWebACL.CustomHTTPHeaderProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customhttpheader.html#cfn-wafv2-webacl-customhttpheader-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomHTTPHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.CustomRequestHandlingProperty",
        jsii_struct_bases=[],
        name_mapping={"insert_headers": "insertHeaders"},
    )
    class CustomRequestHandlingProperty:
        def __init__(
            self,
            *,
            insert_headers: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomHTTPHeaderProperty"]]],
        ) -> None:
            '''
            :param insert_headers: ``CfnWebACL.CustomRequestHandlingProperty.InsertHeaders``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "insert_headers": insert_headers,
            }

        @builtins.property
        def insert_headers(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomHTTPHeaderProperty"]]]:
            '''``CfnWebACL.CustomRequestHandlingProperty.InsertHeaders``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customrequesthandling.html#cfn-wafv2-webacl-customrequesthandling-insertheaders
            '''
            result = self._values.get("insert_headers")
            assert result is not None, "Required property 'insert_headers' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomHTTPHeaderProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomRequestHandlingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.CustomResponseBodyProperty",
        jsii_struct_bases=[],
        name_mapping={"content": "content", "content_type": "contentType"},
    )
    class CustomResponseBodyProperty:
        def __init__(
            self,
            *,
            content: builtins.str,
            content_type: builtins.str,
        ) -> None:
            '''
            :param content: ``CfnWebACL.CustomResponseBodyProperty.Content``.
            :param content_type: ``CfnWebACL.CustomResponseBodyProperty.ContentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "content": content,
                "content_type": content_type,
            }

        @builtins.property
        def content(self) -> builtins.str:
            '''``CfnWebACL.CustomResponseBodyProperty.Content``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html#cfn-wafv2-webacl-customresponsebody-content
            '''
            result = self._values.get("content")
            assert result is not None, "Required property 'content' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def content_type(self) -> builtins.str:
            '''``CfnWebACL.CustomResponseBodyProperty.ContentType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponsebody.html#cfn-wafv2-webacl-customresponsebody-contenttype
            '''
            result = self._values.get("content_type")
            assert result is not None, "Required property 'content_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomResponseBodyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.CustomResponseProperty",
        jsii_struct_bases=[],
        name_mapping={
            "response_code": "responseCode",
            "custom_response_body_key": "customResponseBodyKey",
            "response_headers": "responseHeaders",
        },
    )
    class CustomResponseProperty:
        def __init__(
            self,
            *,
            response_code: jsii.Number,
            custom_response_body_key: typing.Optional[builtins.str] = None,
            response_headers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomHTTPHeaderProperty"]]]] = None,
        ) -> None:
            '''
            :param response_code: ``CfnWebACL.CustomResponseProperty.ResponseCode``.
            :param custom_response_body_key: ``CfnWebACL.CustomResponseProperty.CustomResponseBodyKey``.
            :param response_headers: ``CfnWebACL.CustomResponseProperty.ResponseHeaders``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "response_code": response_code,
            }
            if custom_response_body_key is not None:
                self._values["custom_response_body_key"] = custom_response_body_key
            if response_headers is not None:
                self._values["response_headers"] = response_headers

        @builtins.property
        def response_code(self) -> jsii.Number:
            '''``CfnWebACL.CustomResponseProperty.ResponseCode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-responsecode
            '''
            result = self._values.get("response_code")
            assert result is not None, "Required property 'response_code' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def custom_response_body_key(self) -> typing.Optional[builtins.str]:
            '''``CfnWebACL.CustomResponseProperty.CustomResponseBodyKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-customresponsebodykey
            '''
            result = self._values.get("custom_response_body_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def response_headers(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomHTTPHeaderProperty"]]]]:
            '''``CfnWebACL.CustomResponseProperty.ResponseHeaders``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-customresponse.html#cfn-wafv2-webacl-customresponse-responseheaders
            '''
            result = self._values.get("response_headers")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CustomHTTPHeaderProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomResponseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.DefaultActionProperty",
        jsii_struct_bases=[],
        name_mapping={"allow": "allow", "block": "block"},
    )
    class DefaultActionProperty:
        def __init__(
            self,
            *,
            allow: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.AllowActionProperty"]] = None,
            block: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.BlockActionProperty"]] = None,
        ) -> None:
            '''
            :param allow: ``CfnWebACL.DefaultActionProperty.Allow``.
            :param block: ``CfnWebACL.DefaultActionProperty.Block``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if allow is not None:
                self._values["allow"] = allow
            if block is not None:
                self._values["block"] = block

        @builtins.property
        def allow(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.AllowActionProperty"]]:
            '''``CfnWebACL.DefaultActionProperty.Allow``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html#cfn-wafv2-webacl-defaultaction-allow
            '''
            result = self._values.get("allow")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.AllowActionProperty"]], result)

        @builtins.property
        def block(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.BlockActionProperty"]]:
            '''``CfnWebACL.DefaultActionProperty.Block``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-defaultaction.html#cfn-wafv2-webacl-defaultaction-block
            '''
            result = self._values.get("block")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.BlockActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.ExcludedRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class ExcludedRuleProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''
            :param name: ``CfnWebACL.ExcludedRuleProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnWebACL.ExcludedRuleProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-excludedrule.html#cfn-wafv2-webacl-excludedrule-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExcludedRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "all_query_arguments": "allQueryArguments",
            "body": "body",
            "json_body": "jsonBody",
            "method": "method",
            "query_string": "queryString",
            "single_header": "singleHeader",
            "single_query_argument": "singleQueryArgument",
            "uri_path": "uriPath",
        },
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            all_query_arguments: typing.Any = None,
            body: typing.Any = None,
            json_body: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.JsonBodyProperty"]] = None,
            method: typing.Any = None,
            query_string: typing.Any = None,
            single_header: typing.Any = None,
            single_query_argument: typing.Any = None,
            uri_path: typing.Any = None,
        ) -> None:
            '''
            :param all_query_arguments: ``CfnWebACL.FieldToMatchProperty.AllQueryArguments``.
            :param body: ``CfnWebACL.FieldToMatchProperty.Body``.
            :param json_body: ``CfnWebACL.FieldToMatchProperty.JsonBody``.
            :param method: ``CfnWebACL.FieldToMatchProperty.Method``.
            :param query_string: ``CfnWebACL.FieldToMatchProperty.QueryString``.
            :param single_header: ``CfnWebACL.FieldToMatchProperty.SingleHeader``.
            :param single_query_argument: ``CfnWebACL.FieldToMatchProperty.SingleQueryArgument``.
            :param uri_path: ``CfnWebACL.FieldToMatchProperty.UriPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if all_query_arguments is not None:
                self._values["all_query_arguments"] = all_query_arguments
            if body is not None:
                self._values["body"] = body
            if json_body is not None:
                self._values["json_body"] = json_body
            if method is not None:
                self._values["method"] = method
            if query_string is not None:
                self._values["query_string"] = query_string
            if single_header is not None:
                self._values["single_header"] = single_header
            if single_query_argument is not None:
                self._values["single_query_argument"] = single_query_argument
            if uri_path is not None:
                self._values["uri_path"] = uri_path

        @builtins.property
        def all_query_arguments(self) -> typing.Any:
            '''``CfnWebACL.FieldToMatchProperty.AllQueryArguments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-allqueryarguments
            '''
            result = self._values.get("all_query_arguments")
            return typing.cast(typing.Any, result)

        @builtins.property
        def body(self) -> typing.Any:
            '''``CfnWebACL.FieldToMatchProperty.Body``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Any, result)

        @builtins.property
        def json_body(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.JsonBodyProperty"]]:
            '''``CfnWebACL.FieldToMatchProperty.JsonBody``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-jsonbody
            '''
            result = self._values.get("json_body")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.JsonBodyProperty"]], result)

        @builtins.property
        def method(self) -> typing.Any:
            '''``CfnWebACL.FieldToMatchProperty.Method``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Any, result)

        @builtins.property
        def query_string(self) -> typing.Any:
            '''``CfnWebACL.FieldToMatchProperty.QueryString``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-querystring
            '''
            result = self._values.get("query_string")
            return typing.cast(typing.Any, result)

        @builtins.property
        def single_header(self) -> typing.Any:
            '''``CfnWebACL.FieldToMatchProperty.SingleHeader``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-singleheader
            '''
            result = self._values.get("single_header")
            return typing.cast(typing.Any, result)

        @builtins.property
        def single_query_argument(self) -> typing.Any:
            '''``CfnWebACL.FieldToMatchProperty.SingleQueryArgument``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-singlequeryargument
            '''
            result = self._values.get("single_query_argument")
            return typing.cast(typing.Any, result)

        @builtins.property
        def uri_path(self) -> typing.Any:
            '''``CfnWebACL.FieldToMatchProperty.UriPath``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-fieldtomatch.html#cfn-wafv2-webacl-fieldtomatch-uripath
            '''
            result = self._values.get("uri_path")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.ForwardedIPConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fallback_behavior": "fallbackBehavior",
            "header_name": "headerName",
        },
    )
    class ForwardedIPConfigurationProperty:
        def __init__(
            self,
            *,
            fallback_behavior: builtins.str,
            header_name: builtins.str,
        ) -> None:
            '''
            :param fallback_behavior: ``CfnWebACL.ForwardedIPConfigurationProperty.FallbackBehavior``.
            :param header_name: ``CfnWebACL.ForwardedIPConfigurationProperty.HeaderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "fallback_behavior": fallback_behavior,
                "header_name": header_name,
            }

        @builtins.property
        def fallback_behavior(self) -> builtins.str:
            '''``CfnWebACL.ForwardedIPConfigurationProperty.FallbackBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html#cfn-wafv2-webacl-forwardedipconfiguration-fallbackbehavior
            '''
            result = self._values.get("fallback_behavior")
            assert result is not None, "Required property 'fallback_behavior' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def header_name(self) -> builtins.str:
            '''``CfnWebACL.ForwardedIPConfigurationProperty.HeaderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-forwardedipconfiguration.html#cfn-wafv2-webacl-forwardedipconfiguration-headername
            '''
            result = self._values.get("header_name")
            assert result is not None, "Required property 'header_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ForwardedIPConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.GeoMatchStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "country_codes": "countryCodes",
            "forwarded_ip_config": "forwardedIpConfig",
        },
    )
    class GeoMatchStatementProperty:
        def __init__(
            self,
            *,
            country_codes: typing.Optional[typing.Sequence[builtins.str]] = None,
            forwarded_ip_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ForwardedIPConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param country_codes: ``CfnWebACL.GeoMatchStatementProperty.CountryCodes``.
            :param forwarded_ip_config: ``CfnWebACL.GeoMatchStatementProperty.ForwardedIPConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if country_codes is not None:
                self._values["country_codes"] = country_codes
            if forwarded_ip_config is not None:
                self._values["forwarded_ip_config"] = forwarded_ip_config

        @builtins.property
        def country_codes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnWebACL.GeoMatchStatementProperty.CountryCodes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html#cfn-wafv2-webacl-geomatchstatement-countrycodes
            '''
            result = self._values.get("country_codes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def forwarded_ip_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ForwardedIPConfigurationProperty"]]:
            '''``CfnWebACL.GeoMatchStatementProperty.ForwardedIPConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-geomatchstatement.html#cfn-wafv2-webacl-geomatchstatement-forwardedipconfig
            '''
            result = self._values.get("forwarded_ip_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ForwardedIPConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoMatchStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.interface(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.IPSetForwardedIPConfigurationProperty"
    )
    class IPSetForwardedIPConfigurationProperty(typing_extensions.Protocol):
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html
        '''

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="fallbackBehavior")
        def fallback_behavior(self) -> builtins.str:
            '''``CfnWebACL.IPSetForwardedIPConfigurationProperty.FallbackBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-fallbackbehavior
            '''
            ...

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="headerName")
        def header_name(self) -> builtins.str:
            '''``CfnWebACL.IPSetForwardedIPConfigurationProperty.HeaderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-headername
            '''
            ...

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="position")
        def position(self) -> builtins.str:
            '''``CfnWebACL.IPSetForwardedIPConfigurationProperty.Position``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-position
            '''
            ...


    class _IPSetForwardedIPConfigurationPropertyProxy:
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html
        '''

        __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-wafv2.CfnWebACL.IPSetForwardedIPConfigurationProperty"

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="fallbackBehavior")
        def fallback_behavior(self) -> builtins.str:
            '''``CfnWebACL.IPSetForwardedIPConfigurationProperty.FallbackBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-fallbackbehavior
            '''
            return typing.cast(builtins.str, jsii.get(self, "fallbackBehavior"))

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="headerName")
        def header_name(self) -> builtins.str:
            '''``CfnWebACL.IPSetForwardedIPConfigurationProperty.HeaderName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-headername
            '''
            return typing.cast(builtins.str, jsii.get(self, "headerName"))

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="position")
        def position(self) -> builtins.str:
            '''``CfnWebACL.IPSetForwardedIPConfigurationProperty.Position``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetforwardedipconfiguration.html#cfn-wafv2-webacl-ipsetforwardedipconfiguration-position
            '''
            return typing.cast(builtins.str, jsii.get(self, "position"))

    # Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
    typing.cast(typing.Any, IPSetForwardedIPConfigurationProperty).__jsii_proxy_class__ = lambda : _IPSetForwardedIPConfigurationPropertyProxy

    @jsii.interface(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.IPSetReferenceStatementProperty"
    )
    class IPSetReferenceStatementProperty(typing_extensions.Protocol):
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html
        '''

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="arn")
        def arn(self) -> builtins.str:
            '''``CfnWebACL.IPSetReferenceStatementProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-arn
            '''
            ...

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="ipSetForwardedIpConfig")
        def ip_set_forwarded_ip_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.IPSetForwardedIPConfigurationProperty"]]:
            '''``CfnWebACL.IPSetReferenceStatementProperty.IPSetForwardedIPConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-ipsetforwardedipconfig
            '''
            ...


    class _IPSetReferenceStatementPropertyProxy:
        '''
        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html
        '''

        __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-wafv2.CfnWebACL.IPSetReferenceStatementProperty"

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="arn")
        def arn(self) -> builtins.str:
            '''``CfnWebACL.IPSetReferenceStatementProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-arn
            '''
            return typing.cast(builtins.str, jsii.get(self, "arn"))

        @builtins.property # type: ignore[misc]
        @jsii.member(jsii_name="ipSetForwardedIpConfig")
        def ip_set_forwarded_ip_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.IPSetForwardedIPConfigurationProperty"]]:
            '''``CfnWebACL.IPSetReferenceStatementProperty.IPSetForwardedIPConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ipsetreferencestatement.html#cfn-wafv2-webacl-ipsetreferencestatement-ipsetforwardedipconfig
            '''
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.IPSetForwardedIPConfigurationProperty"]], jsii.get(self, "ipSetForwardedIpConfig"))

    # Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
    typing.cast(typing.Any, IPSetReferenceStatementProperty).__jsii_proxy_class__ = lambda : _IPSetReferenceStatementPropertyProxy

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.JsonBodyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "match_pattern": "matchPattern",
            "match_scope": "matchScope",
            "invalid_fallback_behavior": "invalidFallbackBehavior",
        },
    )
    class JsonBodyProperty:
        def __init__(
            self,
            *,
            match_pattern: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.JsonMatchPatternProperty"],
            match_scope: builtins.str,
            invalid_fallback_behavior: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param match_pattern: ``CfnWebACL.JsonBodyProperty.MatchPattern``.
            :param match_scope: ``CfnWebACL.JsonBodyProperty.MatchScope``.
            :param invalid_fallback_behavior: ``CfnWebACL.JsonBodyProperty.InvalidFallbackBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "match_pattern": match_pattern,
                "match_scope": match_scope,
            }
            if invalid_fallback_behavior is not None:
                self._values["invalid_fallback_behavior"] = invalid_fallback_behavior

        @builtins.property
        def match_pattern(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.JsonMatchPatternProperty"]:
            '''``CfnWebACL.JsonBodyProperty.MatchPattern``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-matchpattern
            '''
            result = self._values.get("match_pattern")
            assert result is not None, "Required property 'match_pattern' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.JsonMatchPatternProperty"], result)

        @builtins.property
        def match_scope(self) -> builtins.str:
            '''``CfnWebACL.JsonBodyProperty.MatchScope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-matchscope
            '''
            result = self._values.get("match_scope")
            assert result is not None, "Required property 'match_scope' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invalid_fallback_behavior(self) -> typing.Optional[builtins.str]:
            '''``CfnWebACL.JsonBodyProperty.InvalidFallbackBehavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonbody.html#cfn-wafv2-webacl-jsonbody-invalidfallbackbehavior
            '''
            result = self._values.get("invalid_fallback_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonBodyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.JsonMatchPatternProperty",
        jsii_struct_bases=[],
        name_mapping={"all": "all", "included_paths": "includedPaths"},
    )
    class JsonMatchPatternProperty:
        def __init__(
            self,
            *,
            all: typing.Any = None,
            included_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param all: ``CfnWebACL.JsonMatchPatternProperty.All``.
            :param included_paths: ``CfnWebACL.JsonMatchPatternProperty.IncludedPaths``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if all is not None:
                self._values["all"] = all
            if included_paths is not None:
                self._values["included_paths"] = included_paths

        @builtins.property
        def all(self) -> typing.Any:
            '''``CfnWebACL.JsonMatchPatternProperty.All``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html#cfn-wafv2-webacl-jsonmatchpattern-all
            '''
            result = self._values.get("all")
            return typing.cast(typing.Any, result)

        @builtins.property
        def included_paths(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnWebACL.JsonMatchPatternProperty.IncludedPaths``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-jsonmatchpattern.html#cfn-wafv2-webacl-jsonmatchpattern-includedpaths
            '''
            result = self._values.get("included_paths")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonMatchPatternProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.LabelMatchStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "scope": "scope"},
    )
    class LabelMatchStatementProperty:
        def __init__(self, *, key: builtins.str, scope: builtins.str) -> None:
            '''
            :param key: ``CfnWebACL.LabelMatchStatementProperty.Key``.
            :param scope: ``CfnWebACL.LabelMatchStatementProperty.Scope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "scope": scope,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnWebACL.LabelMatchStatementProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html#cfn-wafv2-webacl-labelmatchstatement-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scope(self) -> builtins.str:
            '''``CfnWebACL.LabelMatchStatementProperty.Scope``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-labelmatchstatement.html#cfn-wafv2-webacl-labelmatchstatement-scope
            '''
            result = self._values.get("scope")
            assert result is not None, "Required property 'scope' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelMatchStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.LabelProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class LabelProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''
            :param name: ``CfnWebACL.LabelProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-label.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnWebACL.LabelProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-label.html#cfn-wafv2-webacl-label-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.ManagedRuleGroupStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "vendor_name": "vendorName",
            "excluded_rules": "excludedRules",
            "scope_down_statement": "scopeDownStatement",
            "version": "version",
        },
    )
    class ManagedRuleGroupStatementProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            vendor_name: builtins.str,
            excluded_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ExcludedRuleProperty"]]]] = None,
            scope_down_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnWebACL.ManagedRuleGroupStatementProperty.Name``.
            :param vendor_name: ``CfnWebACL.ManagedRuleGroupStatementProperty.VendorName``.
            :param excluded_rules: ``CfnWebACL.ManagedRuleGroupStatementProperty.ExcludedRules``.
            :param scope_down_statement: ``CfnWebACL.ManagedRuleGroupStatementProperty.ScopeDownStatement``.
            :param version: ``CfnWebACL.ManagedRuleGroupStatementProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "vendor_name": vendor_name,
            }
            if excluded_rules is not None:
                self._values["excluded_rules"] = excluded_rules
            if scope_down_statement is not None:
                self._values["scope_down_statement"] = scope_down_statement
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnWebACL.ManagedRuleGroupStatementProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vendor_name(self) -> builtins.str:
            '''``CfnWebACL.ManagedRuleGroupStatementProperty.VendorName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-vendorname
            '''
            result = self._values.get("vendor_name")
            assert result is not None, "Required property 'vendor_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def excluded_rules(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ExcludedRuleProperty"]]]]:
            '''``CfnWebACL.ManagedRuleGroupStatementProperty.ExcludedRules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-excludedrules
            '''
            result = self._values.get("excluded_rules")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ExcludedRuleProperty"]]]], result)

        @builtins.property
        def scope_down_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]]:
            '''``CfnWebACL.ManagedRuleGroupStatementProperty.ScopeDownStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-scopedownstatement
            '''
            result = self._values.get("scope_down_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''``CfnWebACL.ManagedRuleGroupStatementProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-managedrulegroupstatement.html#cfn-wafv2-webacl-managedrulegroupstatement-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManagedRuleGroupStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.NotStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"statement": "statement"},
    )
    class NotStatementProperty:
        def __init__(
            self,
            *,
            statement: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"],
        ) -> None:
            '''
            :param statement: ``CfnWebACL.NotStatementProperty.Statement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "statement": statement,
            }

        @builtins.property
        def statement(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]:
            '''``CfnWebACL.NotStatementProperty.Statement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-notstatement.html#cfn-wafv2-webacl-notstatement-statement
            '''
            result = self._values.get("statement")
            assert result is not None, "Required property 'statement' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.OrStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"statements": "statements"},
    )
    class OrStatementProperty:
        def __init__(
            self,
            *,
            statements: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]]],
        ) -> None:
            '''
            :param statements: ``CfnWebACL.OrStatementProperty.Statements``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "statements": statements,
            }

        @builtins.property
        def statements(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]]]:
            '''``CfnWebACL.OrStatementProperty.Statements``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-orstatement.html#cfn-wafv2-webacl-orstatement-statements
            '''
            result = self._values.get("statements")
            assert result is not None, "Required property 'statements' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.OverrideActionProperty",
        jsii_struct_bases=[],
        name_mapping={"count": "count", "none": "none"},
    )
    class OverrideActionProperty:
        def __init__(
            self,
            *,
            count: typing.Any = None,
            none: typing.Any = None,
        ) -> None:
            '''
            :param count: ``CfnWebACL.OverrideActionProperty.Count``.
            :param none: ``CfnWebACL.OverrideActionProperty.None``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if count is not None:
                self._values["count"] = count
            if none is not None:
                self._values["none"] = none

        @builtins.property
        def count(self) -> typing.Any:
            '''``CfnWebACL.OverrideActionProperty.Count``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html#cfn-wafv2-webacl-overrideaction-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Any, result)

        @builtins.property
        def none(self) -> typing.Any:
            '''``CfnWebACL.OverrideActionProperty.None``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-overrideaction.html#cfn-wafv2-webacl-overrideaction-none
            '''
            result = self._values.get("none")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OverrideActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RateBasedStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregate_key_type": "aggregateKeyType",
            "limit": "limit",
            "forwarded_ip_config": "forwardedIpConfig",
            "scope_down_statement": "scopeDownStatement",
        },
    )
    class RateBasedStatementProperty:
        def __init__(
            self,
            *,
            aggregate_key_type: builtins.str,
            limit: jsii.Number,
            forwarded_ip_config: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ForwardedIPConfigurationProperty"]] = None,
            scope_down_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]] = None,
        ) -> None:
            '''
            :param aggregate_key_type: ``CfnWebACL.RateBasedStatementProperty.AggregateKeyType``.
            :param limit: ``CfnWebACL.RateBasedStatementProperty.Limit``.
            :param forwarded_ip_config: ``CfnWebACL.RateBasedStatementProperty.ForwardedIPConfig``.
            :param scope_down_statement: ``CfnWebACL.RateBasedStatementProperty.ScopeDownStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "aggregate_key_type": aggregate_key_type,
                "limit": limit,
            }
            if forwarded_ip_config is not None:
                self._values["forwarded_ip_config"] = forwarded_ip_config
            if scope_down_statement is not None:
                self._values["scope_down_statement"] = scope_down_statement

        @builtins.property
        def aggregate_key_type(self) -> builtins.str:
            '''``CfnWebACL.RateBasedStatementProperty.AggregateKeyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-aggregatekeytype
            '''
            result = self._values.get("aggregate_key_type")
            assert result is not None, "Required property 'aggregate_key_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def limit(self) -> jsii.Number:
            '''``CfnWebACL.RateBasedStatementProperty.Limit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-limit
            '''
            result = self._values.get("limit")
            assert result is not None, "Required property 'limit' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def forwarded_ip_config(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ForwardedIPConfigurationProperty"]]:
            '''``CfnWebACL.RateBasedStatementProperty.ForwardedIPConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-forwardedipconfig
            '''
            result = self._values.get("forwarded_ip_config")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ForwardedIPConfigurationProperty"]], result)

        @builtins.property
        def scope_down_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]]:
            '''``CfnWebACL.RateBasedStatementProperty.ScopeDownStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ratebasedstatement.html#cfn-wafv2-webacl-ratebasedstatement-scopedownstatement
            '''
            result = self._values.get("scope_down_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RateBasedStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RegexPatternSetReferenceStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "field_to_match": "fieldToMatch",
            "text_transformations": "textTransformations",
        },
    )
    class RegexPatternSetReferenceStatementProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"],
            text_transformations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]],
        ) -> None:
            '''
            :param arn: ``CfnWebACL.RegexPatternSetReferenceStatementProperty.Arn``.
            :param field_to_match: ``CfnWebACL.RegexPatternSetReferenceStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnWebACL.RegexPatternSetReferenceStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "field_to_match": field_to_match,
                "text_transformations": text_transformations,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''``CfnWebACL.RegexPatternSetReferenceStatementProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"]:
            '''``CfnWebACL.RegexPatternSetReferenceStatementProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"], result)

        @builtins.property
        def text_transformations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]]:
            '''``CfnWebACL.RegexPatternSetReferenceStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-regexpatternsetreferencestatement.html#cfn-wafv2-webacl-regexpatternsetreferencestatement-texttransformations
            '''
            result = self._values.get("text_transformations")
            assert result is not None, "Required property 'text_transformations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegexPatternSetReferenceStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RuleActionProperty",
        jsii_struct_bases=[],
        name_mapping={"allow": "allow", "block": "block", "count": "count"},
    )
    class RuleActionProperty:
        def __init__(
            self,
            *,
            allow: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.AllowActionProperty"]] = None,
            block: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.BlockActionProperty"]] = None,
            count: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CountActionProperty"]] = None,
        ) -> None:
            '''
            :param allow: ``CfnWebACL.RuleActionProperty.Allow``.
            :param block: ``CfnWebACL.RuleActionProperty.Block``.
            :param count: ``CfnWebACL.RuleActionProperty.Count``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if allow is not None:
                self._values["allow"] = allow
            if block is not None:
                self._values["block"] = block
            if count is not None:
                self._values["count"] = count

        @builtins.property
        def allow(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.AllowActionProperty"]]:
            '''``CfnWebACL.RuleActionProperty.Allow``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-allow
            '''
            result = self._values.get("allow")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.AllowActionProperty"]], result)

        @builtins.property
        def block(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.BlockActionProperty"]]:
            '''``CfnWebACL.RuleActionProperty.Block``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-block
            '''
            result = self._values.get("block")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.BlockActionProperty"]], result)

        @builtins.property
        def count(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CountActionProperty"]]:
            '''``CfnWebACL.RuleActionProperty.Count``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-ruleaction.html#cfn-wafv2-webacl-ruleaction-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.CountActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RuleGroupReferenceStatementProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "excluded_rules": "excludedRules"},
    )
    class RuleGroupReferenceStatementProperty:
        def __init__(
            self,
            *,
            arn: builtins.str,
            excluded_rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ExcludedRuleProperty"]]]] = None,
        ) -> None:
            '''
            :param arn: ``CfnWebACL.RuleGroupReferenceStatementProperty.Arn``.
            :param excluded_rules: ``CfnWebACL.RuleGroupReferenceStatementProperty.ExcludedRules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
            }
            if excluded_rules is not None:
                self._values["excluded_rules"] = excluded_rules

        @builtins.property
        def arn(self) -> builtins.str:
            '''``CfnWebACL.RuleGroupReferenceStatementProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def excluded_rules(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ExcludedRuleProperty"]]]]:
            '''``CfnWebACL.RuleGroupReferenceStatementProperty.ExcludedRules``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rulegroupreferencestatement.html#cfn-wafv2-webacl-rulegroupreferencestatement-excludedrules
            '''
            result = self._values.get("excluded_rules")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ExcludedRuleProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleGroupReferenceStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "priority": "priority",
            "statement": "statement",
            "visibility_config": "visibilityConfig",
            "action": "action",
            "override_action": "overrideAction",
            "rule_labels": "ruleLabels",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            priority: jsii.Number,
            statement: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"],
            visibility_config: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.VisibilityConfigProperty"],
            action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleActionProperty"]] = None,
            override_action: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.OverrideActionProperty"]] = None,
            rule_labels: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.LabelProperty"]]]] = None,
        ) -> None:
            '''
            :param name: ``CfnWebACL.RuleProperty.Name``.
            :param priority: ``CfnWebACL.RuleProperty.Priority``.
            :param statement: ``CfnWebACL.RuleProperty.Statement``.
            :param visibility_config: ``CfnWebACL.RuleProperty.VisibilityConfig``.
            :param action: ``CfnWebACL.RuleProperty.Action``.
            :param override_action: ``CfnWebACL.RuleProperty.OverrideAction``.
            :param rule_labels: ``CfnWebACL.RuleProperty.RuleLabels``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name": name,
                "priority": priority,
                "statement": statement,
                "visibility_config": visibility_config,
            }
            if action is not None:
                self._values["action"] = action
            if override_action is not None:
                self._values["override_action"] = override_action
            if rule_labels is not None:
                self._values["rule_labels"] = rule_labels

        @builtins.property
        def name(self) -> builtins.str:
            '''``CfnWebACL.RuleProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def priority(self) -> jsii.Number:
            '''``CfnWebACL.RuleProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def statement(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"]:
            '''``CfnWebACL.RuleProperty.Statement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-statement
            '''
            result = self._values.get("statement")
            assert result is not None, "Required property 'statement' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.StatementProperty"], result)

        @builtins.property
        def visibility_config(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.VisibilityConfigProperty"]:
            '''``CfnWebACL.RuleProperty.VisibilityConfig``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-visibilityconfig
            '''
            result = self._values.get("visibility_config")
            assert result is not None, "Required property 'visibility_config' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.VisibilityConfigProperty"], result)

        @builtins.property
        def action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleActionProperty"]]:
            '''``CfnWebACL.RuleProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleActionProperty"]], result)

        @builtins.property
        def override_action(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.OverrideActionProperty"]]:
            '''``CfnWebACL.RuleProperty.OverrideAction``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-overrideaction
            '''
            result = self._values.get("override_action")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.OverrideActionProperty"]], result)

        @builtins.property
        def rule_labels(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.LabelProperty"]]]]:
            '''``CfnWebACL.RuleProperty.RuleLabels``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-rule.html#cfn-wafv2-webacl-rule-rulelabels
            '''
            result = self._values.get("rule_labels")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.LabelProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.SizeConstraintStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "field_to_match": "fieldToMatch",
            "size": "size",
            "text_transformations": "textTransformations",
        },
    )
    class SizeConstraintStatementProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"],
            size: jsii.Number,
            text_transformations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]],
        ) -> None:
            '''
            :param comparison_operator: ``CfnWebACL.SizeConstraintStatementProperty.ComparisonOperator``.
            :param field_to_match: ``CfnWebACL.SizeConstraintStatementProperty.FieldToMatch``.
            :param size: ``CfnWebACL.SizeConstraintStatementProperty.Size``.
            :param text_transformations: ``CfnWebACL.SizeConstraintStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "field_to_match": field_to_match,
                "size": size,
                "text_transformations": text_transformations,
            }

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''``CfnWebACL.SizeConstraintStatementProperty.ComparisonOperator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"]:
            '''``CfnWebACL.SizeConstraintStatementProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"], result)

        @builtins.property
        def size(self) -> jsii.Number:
            '''``CfnWebACL.SizeConstraintStatementProperty.Size``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-size
            '''
            result = self._values.get("size")
            assert result is not None, "Required property 'size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def text_transformations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]]:
            '''``CfnWebACL.SizeConstraintStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sizeconstraintstatement.html#cfn-wafv2-webacl-sizeconstraintstatement-texttransformations
            '''
            result = self._values.get("text_transformations")
            assert result is not None, "Required property 'text_transformations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SizeConstraintStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.SqliMatchStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "text_transformations": "textTransformations",
        },
    )
    class SqliMatchStatementProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"],
            text_transformations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]],
        ) -> None:
            '''
            :param field_to_match: ``CfnWebACL.SqliMatchStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnWebACL.SqliMatchStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "field_to_match": field_to_match,
                "text_transformations": text_transformations,
            }

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"]:
            '''``CfnWebACL.SqliMatchStatementProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"], result)

        @builtins.property
        def text_transformations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]]:
            '''``CfnWebACL.SqliMatchStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-sqlimatchstatement.html#cfn-wafv2-webacl-sqlimatchstatement-texttransformations
            '''
            result = self._values.get("text_transformations")
            assert result is not None, "Required property 'text_transformations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SqliMatchStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.StatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "and_statement": "andStatement",
            "byte_match_statement": "byteMatchStatement",
            "geo_match_statement": "geoMatchStatement",
            "ip_set_reference_statement": "ipSetReferenceStatement",
            "label_match_statement": "labelMatchStatement",
            "managed_rule_group_statement": "managedRuleGroupStatement",
            "not_statement": "notStatement",
            "or_statement": "orStatement",
            "rate_based_statement": "rateBasedStatement",
            "regex_pattern_set_reference_statement": "regexPatternSetReferenceStatement",
            "rule_group_reference_statement": "ruleGroupReferenceStatement",
            "size_constraint_statement": "sizeConstraintStatement",
            "sqli_match_statement": "sqliMatchStatement",
            "xss_match_statement": "xssMatchStatement",
        },
    )
    class StatementProperty:
        def __init__(
            self,
            *,
            and_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.AndStatementProperty"]] = None,
            byte_match_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ByteMatchStatementProperty"]] = None,
            geo_match_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.GeoMatchStatementProperty"]] = None,
            ip_set_reference_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.IPSetReferenceStatementProperty"]] = None,
            label_match_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.LabelMatchStatementProperty"]] = None,
            managed_rule_group_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ManagedRuleGroupStatementProperty"]] = None,
            not_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.NotStatementProperty"]] = None,
            or_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.OrStatementProperty"]] = None,
            rate_based_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RateBasedStatementProperty"]] = None,
            regex_pattern_set_reference_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RegexPatternSetReferenceStatementProperty"]] = None,
            rule_group_reference_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleGroupReferenceStatementProperty"]] = None,
            size_constraint_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.SizeConstraintStatementProperty"]] = None,
            sqli_match_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.SqliMatchStatementProperty"]] = None,
            xss_match_statement: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.XssMatchStatementProperty"]] = None,
        ) -> None:
            '''
            :param and_statement: ``CfnWebACL.StatementProperty.AndStatement``.
            :param byte_match_statement: ``CfnWebACL.StatementProperty.ByteMatchStatement``.
            :param geo_match_statement: ``CfnWebACL.StatementProperty.GeoMatchStatement``.
            :param ip_set_reference_statement: ``CfnWebACL.StatementProperty.IPSetReferenceStatement``.
            :param label_match_statement: ``CfnWebACL.StatementProperty.LabelMatchStatement``.
            :param managed_rule_group_statement: ``CfnWebACL.StatementProperty.ManagedRuleGroupStatement``.
            :param not_statement: ``CfnWebACL.StatementProperty.NotStatement``.
            :param or_statement: ``CfnWebACL.StatementProperty.OrStatement``.
            :param rate_based_statement: ``CfnWebACL.StatementProperty.RateBasedStatement``.
            :param regex_pattern_set_reference_statement: ``CfnWebACL.StatementProperty.RegexPatternSetReferenceStatement``.
            :param rule_group_reference_statement: ``CfnWebACL.StatementProperty.RuleGroupReferenceStatement``.
            :param size_constraint_statement: ``CfnWebACL.StatementProperty.SizeConstraintStatement``.
            :param sqli_match_statement: ``CfnWebACL.StatementProperty.SqliMatchStatement``.
            :param xss_match_statement: ``CfnWebACL.StatementProperty.XssMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if and_statement is not None:
                self._values["and_statement"] = and_statement
            if byte_match_statement is not None:
                self._values["byte_match_statement"] = byte_match_statement
            if geo_match_statement is not None:
                self._values["geo_match_statement"] = geo_match_statement
            if ip_set_reference_statement is not None:
                self._values["ip_set_reference_statement"] = ip_set_reference_statement
            if label_match_statement is not None:
                self._values["label_match_statement"] = label_match_statement
            if managed_rule_group_statement is not None:
                self._values["managed_rule_group_statement"] = managed_rule_group_statement
            if not_statement is not None:
                self._values["not_statement"] = not_statement
            if or_statement is not None:
                self._values["or_statement"] = or_statement
            if rate_based_statement is not None:
                self._values["rate_based_statement"] = rate_based_statement
            if regex_pattern_set_reference_statement is not None:
                self._values["regex_pattern_set_reference_statement"] = regex_pattern_set_reference_statement
            if rule_group_reference_statement is not None:
                self._values["rule_group_reference_statement"] = rule_group_reference_statement
            if size_constraint_statement is not None:
                self._values["size_constraint_statement"] = size_constraint_statement
            if sqli_match_statement is not None:
                self._values["sqli_match_statement"] = sqli_match_statement
            if xss_match_statement is not None:
                self._values["xss_match_statement"] = xss_match_statement

        @builtins.property
        def and_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.AndStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.AndStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-andstatement
            '''
            result = self._values.get("and_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.AndStatementProperty"]], result)

        @builtins.property
        def byte_match_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ByteMatchStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.ByteMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-bytematchstatement
            '''
            result = self._values.get("byte_match_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ByteMatchStatementProperty"]], result)

        @builtins.property
        def geo_match_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.GeoMatchStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.GeoMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-geomatchstatement
            '''
            result = self._values.get("geo_match_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.GeoMatchStatementProperty"]], result)

        @builtins.property
        def ip_set_reference_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.IPSetReferenceStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.IPSetReferenceStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-ipsetreferencestatement
            '''
            result = self._values.get("ip_set_reference_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.IPSetReferenceStatementProperty"]], result)

        @builtins.property
        def label_match_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.LabelMatchStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.LabelMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-labelmatchstatement
            '''
            result = self._values.get("label_match_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.LabelMatchStatementProperty"]], result)

        @builtins.property
        def managed_rule_group_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ManagedRuleGroupStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.ManagedRuleGroupStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-managedrulegroupstatement
            '''
            result = self._values.get("managed_rule_group_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.ManagedRuleGroupStatementProperty"]], result)

        @builtins.property
        def not_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.NotStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.NotStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-notstatement
            '''
            result = self._values.get("not_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.NotStatementProperty"]], result)

        @builtins.property
        def or_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.OrStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.OrStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-orstatement
            '''
            result = self._values.get("or_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.OrStatementProperty"]], result)

        @builtins.property
        def rate_based_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RateBasedStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.RateBasedStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-ratebasedstatement
            '''
            result = self._values.get("rate_based_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RateBasedStatementProperty"]], result)

        @builtins.property
        def regex_pattern_set_reference_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RegexPatternSetReferenceStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.RegexPatternSetReferenceStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-regexpatternsetreferencestatement
            '''
            result = self._values.get("regex_pattern_set_reference_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RegexPatternSetReferenceStatementProperty"]], result)

        @builtins.property
        def rule_group_reference_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleGroupReferenceStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.RuleGroupReferenceStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-rulegroupreferencestatement
            '''
            result = self._values.get("rule_group_reference_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.RuleGroupReferenceStatementProperty"]], result)

        @builtins.property
        def size_constraint_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.SizeConstraintStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.SizeConstraintStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-sizeconstraintstatement
            '''
            result = self._values.get("size_constraint_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.SizeConstraintStatementProperty"]], result)

        @builtins.property
        def sqli_match_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.SqliMatchStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.SqliMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-sqlimatchstatement
            '''
            result = self._values.get("sqli_match_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.SqliMatchStatementProperty"]], result)

        @builtins.property
        def xss_match_statement(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.XssMatchStatementProperty"]]:
            '''``CfnWebACL.StatementProperty.XssMatchStatement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-statement.html#cfn-wafv2-webacl-statement-xssmatchstatement
            '''
            result = self._values.get("xss_match_statement")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.XssMatchStatementProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.TextTransformationProperty",
        jsii_struct_bases=[],
        name_mapping={"priority": "priority", "type": "type"},
    )
    class TextTransformationProperty:
        def __init__(self, *, priority: jsii.Number, type: builtins.str) -> None:
            '''
            :param priority: ``CfnWebACL.TextTransformationProperty.Priority``.
            :param type: ``CfnWebACL.TextTransformationProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "priority": priority,
                "type": type,
            }

        @builtins.property
        def priority(self) -> jsii.Number:
            '''``CfnWebACL.TextTransformationProperty.Priority``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html#cfn-wafv2-webacl-texttransformation-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnWebACL.TextTransformationProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-texttransformation.html#cfn-wafv2-webacl-texttransformation-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextTransformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.VisibilityConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_metrics_enabled": "cloudWatchMetricsEnabled",
            "metric_name": "metricName",
            "sampled_requests_enabled": "sampledRequestsEnabled",
        },
    )
    class VisibilityConfigProperty:
        def __init__(
            self,
            *,
            cloud_watch_metrics_enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            metric_name: builtins.str,
            sampled_requests_enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        ) -> None:
            '''
            :param cloud_watch_metrics_enabled: ``CfnWebACL.VisibilityConfigProperty.CloudWatchMetricsEnabled``.
            :param metric_name: ``CfnWebACL.VisibilityConfigProperty.MetricName``.
            :param sampled_requests_enabled: ``CfnWebACL.VisibilityConfigProperty.SampledRequestsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cloud_watch_metrics_enabled": cloud_watch_metrics_enabled,
                "metric_name": metric_name,
                "sampled_requests_enabled": sampled_requests_enabled,
            }

        @builtins.property
        def cloud_watch_metrics_enabled(
            self,
        ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnWebACL.VisibilityConfigProperty.CloudWatchMetricsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-cloudwatchmetricsenabled
            '''
            result = self._values.get("cloud_watch_metrics_enabled")
            assert result is not None, "Required property 'cloud_watch_metrics_enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''``CfnWebACL.VisibilityConfigProperty.MetricName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sampled_requests_enabled(
            self,
        ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''``CfnWebACL.VisibilityConfigProperty.SampledRequestsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-visibilityconfig.html#cfn-wafv2-webacl-visibilityconfig-sampledrequestsenabled
            '''
            result = self._values.get("sampled_requests_enabled")
            assert result is not None, "Required property 'sampled_requests_enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VisibilityConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-wafv2.CfnWebACL.XssMatchStatementProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_to_match": "fieldToMatch",
            "text_transformations": "textTransformations",
        },
    )
    class XssMatchStatementProperty:
        def __init__(
            self,
            *,
            field_to_match: typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"],
            text_transformations: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]],
        ) -> None:
            '''
            :param field_to_match: ``CfnWebACL.XssMatchStatementProperty.FieldToMatch``.
            :param text_transformations: ``CfnWebACL.XssMatchStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "field_to_match": field_to_match,
                "text_transformations": text_transformations,
            }

        @builtins.property
        def field_to_match(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"]:
            '''``CfnWebACL.XssMatchStatementProperty.FieldToMatch``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html#cfn-wafv2-webacl-xssmatchstatement-fieldtomatch
            '''
            result = self._values.get("field_to_match")
            assert result is not None, "Required property 'field_to_match' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.FieldToMatchProperty"], result)

        @builtins.property
        def text_transformations(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]]:
            '''``CfnWebACL.XssMatchStatementProperty.TextTransformations``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wafv2-webacl-xssmatchstatement.html#cfn-wafv2-webacl-xssmatchstatement-texttransformations
            '''
            result = self._values.get("text_transformations")
            assert result is not None, "Required property 'text_transformations' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnWebACL.TextTransformationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "XssMatchStatementProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWebACLAssociation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-wafv2.CfnWebACLAssociation",
):
    '''A CloudFormation ``AWS::WAFv2::WebACLAssociation``.

    :cloudformationResource: AWS::WAFv2::WebACLAssociation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        resource_arn: builtins.str,
        web_acl_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::WAFv2::WebACLAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param resource_arn: ``AWS::WAFv2::WebACLAssociation.ResourceArn``.
        :param web_acl_arn: ``AWS::WAFv2::WebACLAssociation.WebACLArn``.
        '''
        props = CfnWebACLAssociationProps(
            resource_arn=resource_arn, web_acl_arn=web_acl_arn
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
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''``AWS::WAFv2::WebACLAssociation.ResourceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-resourcearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        jsii.set(self, "resourceArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="webAclArn")
    def web_acl_arn(self) -> builtins.str:
        '''``AWS::WAFv2::WebACLAssociation.WebACLArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-webaclarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "webAclArn"))

    @web_acl_arn.setter
    def web_acl_arn(self, value: builtins.str) -> None:
        jsii.set(self, "webAclArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-wafv2.CfnWebACLAssociationProps",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "web_acl_arn": "webAclArn"},
)
class CfnWebACLAssociationProps:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        web_acl_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::WAFv2::WebACLAssociation``.

        :param resource_arn: ``AWS::WAFv2::WebACLAssociation.ResourceArn``.
        :param web_acl_arn: ``AWS::WAFv2::WebACLAssociation.WebACLArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "resource_arn": resource_arn,
            "web_acl_arn": web_acl_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''``AWS::WAFv2::WebACLAssociation.ResourceArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def web_acl_arn(self) -> builtins.str:
        '''``AWS::WAFv2::WebACLAssociation.WebACLArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html#cfn-wafv2-webaclassociation-webaclarn
        '''
        result = self._values.get("web_acl_arn")
        assert result is not None, "Required property 'web_acl_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWebACLAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-wafv2.CfnWebACLProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_action": "defaultAction",
        "scope": "scope",
        "visibility_config": "visibilityConfig",
        "custom_response_bodies": "customResponseBodies",
        "description": "description",
        "name": "name",
        "rules": "rules",
        "tags": "tags",
    },
)
class CfnWebACLProps:
    def __init__(
        self,
        *,
        default_action: typing.Union[CfnWebACL.DefaultActionProperty, aws_cdk.core.IResolvable],
        scope: builtins.str,
        visibility_config: typing.Union[aws_cdk.core.IResolvable, CfnWebACL.VisibilityConfigProperty],
        custom_response_bodies: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnWebACL.CustomResponseBodyProperty]]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnWebACL.RuleProperty]]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::WAFv2::WebACL``.

        :param default_action: ``AWS::WAFv2::WebACL.DefaultAction``.
        :param scope: ``AWS::WAFv2::WebACL.Scope``.
        :param visibility_config: ``AWS::WAFv2::WebACL.VisibilityConfig``.
        :param custom_response_bodies: ``AWS::WAFv2::WebACL.CustomResponseBodies``.
        :param description: ``AWS::WAFv2::WebACL.Description``.
        :param name: ``AWS::WAFv2::WebACL.Name``.
        :param rules: ``AWS::WAFv2::WebACL.Rules``.
        :param tags: ``AWS::WAFv2::WebACL.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "default_action": default_action,
            "scope": scope,
            "visibility_config": visibility_config,
        }
        if custom_response_bodies is not None:
            self._values["custom_response_bodies"] = custom_response_bodies
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if rules is not None:
            self._values["rules"] = rules
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def default_action(
        self,
    ) -> typing.Union[CfnWebACL.DefaultActionProperty, aws_cdk.core.IResolvable]:
        '''``AWS::WAFv2::WebACL.DefaultAction``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-defaultaction
        '''
        result = self._values.get("default_action")
        assert result is not None, "Required property 'default_action' is missing"
        return typing.cast(typing.Union[CfnWebACL.DefaultActionProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''``AWS::WAFv2::WebACL.Scope``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def visibility_config(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnWebACL.VisibilityConfigProperty]:
        '''``AWS::WAFv2::WebACL.VisibilityConfig``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-visibilityconfig
        '''
        result = self._values.get("visibility_config")
        assert result is not None, "Required property 'visibility_config' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnWebACL.VisibilityConfigProperty], result)

    @builtins.property
    def custom_response_bodies(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnWebACL.CustomResponseBodyProperty]]]]:
        '''``AWS::WAFv2::WebACL.CustomResponseBodies``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-customresponsebodies
        '''
        result = self._values.get("custom_response_bodies")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, typing.Union[aws_cdk.core.IResolvable, CfnWebACL.CustomResponseBodyProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::WebACL.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::WAFv2::WebACL.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnWebACL.RuleProperty]]]]:
        '''``AWS::WAFv2::WebACL.Rules``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-rules
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnWebACL.RuleProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::WAFv2::WebACL.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html#cfn-wafv2-webacl-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWebACLProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnIPSet",
    "CfnIPSetProps",
    "CfnLoggingConfiguration",
    "CfnLoggingConfigurationProps",
    "CfnRegexPatternSet",
    "CfnRegexPatternSetProps",
    "CfnRuleGroup",
    "CfnRuleGroupProps",
    "CfnWebACL",
    "CfnWebACLAssociation",
    "CfnWebACLAssociationProps",
    "CfnWebACLProps",
]

publication.publish()
