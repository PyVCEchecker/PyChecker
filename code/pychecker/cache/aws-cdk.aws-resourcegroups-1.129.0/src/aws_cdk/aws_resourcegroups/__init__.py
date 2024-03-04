'''
# AWS::ResourceGroups Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_resourcegroups as resourcegroups
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
class CfnGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-resourcegroups.CfnGroup",
):
    '''A CloudFormation ``AWS::ResourceGroups::Group``.

    :cloudformationResource: AWS::ResourceGroups::Group
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union["CfnGroup.ConfigurationItemProperty", aws_cdk.core.IResolvable]]]] = None,
        description: typing.Optional[builtins.str] = None,
        resource_query: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.ResourceQueryProperty"]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::ResourceGroups::Group``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::ResourceGroups::Group.Name``.
        :param configuration: ``AWS::ResourceGroups::Group.Configuration``.
        :param description: ``AWS::ResourceGroups::Group.Description``.
        :param resource_query: ``AWS::ResourceGroups::Group.ResourceQuery``.
        :param resources: ``AWS::ResourceGroups::Group.Resources``.
        :param tags: ``AWS::ResourceGroups::Group.Tags``.
        '''
        props = CfnGroupProps(
            name=name,
            configuration=configuration,
            description=description,
            resource_query=resource_query,
            resources=resources,
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
        '''``AWS::ResourceGroups::Group.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::ResourceGroups::Group.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnGroup.ConfigurationItemProperty", aws_cdk.core.IResolvable]]]]:
        '''``AWS::ResourceGroups::Group.Configuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-configuration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnGroup.ConfigurationItemProperty", aws_cdk.core.IResolvable]]]], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnGroup.ConfigurationItemProperty", aws_cdk.core.IResolvable]]]],
    ) -> None:
        jsii.set(self, "configuration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ResourceGroups::Group.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resourceQuery")
    def resource_query(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.ResourceQueryProperty"]]:
        '''``AWS::ResourceGroups::Group.ResourceQuery``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-resourcequery
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.ResourceQueryProperty"]], jsii.get(self, "resourceQuery"))

    @resource_query.setter
    def resource_query(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.ResourceQueryProperty"]],
    ) -> None:
        jsii.set(self, "resourceQuery", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ResourceGroups::Group.Resources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-resources
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "resources", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-resourcegroups.CfnGroup.ConfigurationItemProperty",
        jsii_struct_bases=[],
        name_mapping={"parameters": "parameters", "type": "type"},
    )
    class ConfigurationItemProperty:
        def __init__(
            self,
            *,
            parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.ConfigurationParameterProperty"]]]] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param parameters: ``CfnGroup.ConfigurationItemProperty.Parameters``.
            :param type: ``CfnGroup.ConfigurationItemProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-configurationitem.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if parameters is not None:
                self._values["parameters"] = parameters
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.ConfigurationParameterProperty"]]]]:
            '''``CfnGroup.ConfigurationItemProperty.Parameters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-configurationitem.html#cfn-resourcegroups-group-configurationitem-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.ConfigurationParameterProperty"]]]], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnGroup.ConfigurationItemProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-configurationitem.html#cfn-resourcegroups-group-configurationitem-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-resourcegroups.CfnGroup.ConfigurationParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "values": "values"},
    )
    class ConfigurationParameterProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param name: ``CfnGroup.ConfigurationParameterProperty.Name``.
            :param values: ``CfnGroup.ConfigurationParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-configurationparameter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnGroup.ConfigurationParameterProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-configurationparameter.html#cfn-resourcegroups-group-configurationparameter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnGroup.ConfigurationParameterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-configurationparameter.html#cfn-resourcegroups-group-configurationparameter-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-resourcegroups.CfnGroup.QueryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_type_filters": "resourceTypeFilters",
            "stack_identifier": "stackIdentifier",
            "tag_filters": "tagFilters",
        },
    )
    class QueryProperty:
        def __init__(
            self,
            *,
            resource_type_filters: typing.Optional[typing.Sequence[builtins.str]] = None,
            stack_identifier: typing.Optional[builtins.str] = None,
            tag_filters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.TagFilterProperty"]]]] = None,
        ) -> None:
            '''
            :param resource_type_filters: ``CfnGroup.QueryProperty.ResourceTypeFilters``.
            :param stack_identifier: ``CfnGroup.QueryProperty.StackIdentifier``.
            :param tag_filters: ``CfnGroup.QueryProperty.TagFilters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-query.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if resource_type_filters is not None:
                self._values["resource_type_filters"] = resource_type_filters
            if stack_identifier is not None:
                self._values["stack_identifier"] = stack_identifier
            if tag_filters is not None:
                self._values["tag_filters"] = tag_filters

        @builtins.property
        def resource_type_filters(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnGroup.QueryProperty.ResourceTypeFilters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-query.html#cfn-resourcegroups-group-query-resourcetypefilters
            '''
            result = self._values.get("resource_type_filters")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def stack_identifier(self) -> typing.Optional[builtins.str]:
            '''``CfnGroup.QueryProperty.StackIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-query.html#cfn-resourcegroups-group-query-stackidentifier
            '''
            result = self._values.get("stack_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_filters(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.TagFilterProperty"]]]]:
            '''``CfnGroup.QueryProperty.TagFilters``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-query.html#cfn-resourcegroups-group-query-tagfilters
            '''
            result = self._values.get("tag_filters")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.TagFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-resourcegroups.CfnGroup.ResourceQueryProperty",
        jsii_struct_bases=[],
        name_mapping={"query": "query", "type": "type"},
    )
    class ResourceQueryProperty:
        def __init__(
            self,
            *,
            query: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.QueryProperty"]] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param query: ``CfnGroup.ResourceQueryProperty.Query``.
            :param type: ``CfnGroup.ResourceQueryProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-resourcequery.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if query is not None:
                self._values["query"] = query
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def query(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.QueryProperty"]]:
            '''``CfnGroup.ResourceQueryProperty.Query``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-resourcequery.html#cfn-resourcegroups-group-resourcequery-query
            '''
            result = self._values.get("query")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnGroup.QueryProperty"]], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnGroup.ResourceQueryProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-resourcequery.html#cfn-resourcegroups-group-resourcequery-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceQueryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-resourcegroups.CfnGroup.TagFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "values": "values"},
    )
    class TagFilterProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param key: ``CfnGroup.TagFilterProperty.Key``.
            :param values: ``CfnGroup.TagFilterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-tagfilter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''``CfnGroup.TagFilterProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-tagfilter.html#cfn-resourcegroups-group-tagfilter-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnGroup.TagFilterProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resourcegroups-group-tagfilter.html#cfn-resourcegroups-group-tagfilter-values
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
    jsii_type="@aws-cdk/aws-resourcegroups.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "configuration": "configuration",
        "description": "description",
        "resource_query": "resourceQuery",
        "resources": "resources",
        "tags": "tags",
    },
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[CfnGroup.ConfigurationItemProperty, aws_cdk.core.IResolvable]]]] = None,
        description: typing.Optional[builtins.str] = None,
        resource_query: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnGroup.ResourceQueryProperty]] = None,
        resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ResourceGroups::Group``.

        :param name: ``AWS::ResourceGroups::Group.Name``.
        :param configuration: ``AWS::ResourceGroups::Group.Configuration``.
        :param description: ``AWS::ResourceGroups::Group.Description``.
        :param resource_query: ``AWS::ResourceGroups::Group.ResourceQuery``.
        :param resources: ``AWS::ResourceGroups::Group.Resources``.
        :param tags: ``AWS::ResourceGroups::Group.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if configuration is not None:
            self._values["configuration"] = configuration
        if description is not None:
            self._values["description"] = description
        if resource_query is not None:
            self._values["resource_query"] = resource_query
        if resources is not None:
            self._values["resources"] = resources
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::ResourceGroups::Group.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnGroup.ConfigurationItemProperty, aws_cdk.core.IResolvable]]]]:
        '''``AWS::ResourceGroups::Group.Configuration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[CfnGroup.ConfigurationItemProperty, aws_cdk.core.IResolvable]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::ResourceGroups::Group.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_query(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnGroup.ResourceQueryProperty]]:
        '''``AWS::ResourceGroups::Group.ResourceQuery``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-resourcequery
        '''
        result = self._values.get("resource_query")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnGroup.ResourceQueryProperty]], result)

    @builtins.property
    def resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::ResourceGroups::Group.Resources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-resources
        '''
        result = self._values.get("resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ResourceGroups::Group.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html#cfn-resourcegroups-group-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGroup",
    "CfnGroupProps",
]

publication.publish()
