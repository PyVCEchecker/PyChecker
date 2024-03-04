'''
# Amazon Athena Construct Library

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
class CfnDataCatalog(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-athena.CfnDataCatalog",
):
    '''A CloudFormation ``AWS::Athena::DataCatalog``.

    :cloudformationResource: AWS::Athena::DataCatalog
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::Athena::DataCatalog``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Athena::DataCatalog.Name``.
        :param type: ``AWS::Athena::DataCatalog.Type``.
        :param description: ``AWS::Athena::DataCatalog.Description``.
        :param parameters: ``AWS::Athena::DataCatalog.Parameters``.
        :param tags: ``AWS::Athena::DataCatalog.Tags``.
        '''
        props = CfnDataCatalogProps(
            name=name,
            type=type,
            description=description,
            parameters=parameters,
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Athena::DataCatalog.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Athena::DataCatalog.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::Athena::DataCatalog.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::DataCatalog.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::Athena::DataCatalog.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-parameters
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        jsii.set(self, "parameters", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-athena.CfnDataCatalogProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "description": "description",
        "parameters": "parameters",
        "tags": "tags",
    },
)
class CfnDataCatalogProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Athena::DataCatalog``.

        :param name: ``AWS::Athena::DataCatalog.Name``.
        :param type: ``AWS::Athena::DataCatalog.Type``.
        :param description: ``AWS::Athena::DataCatalog.Description``.
        :param parameters: ``AWS::Athena::DataCatalog.Parameters``.
        :param tags: ``AWS::Athena::DataCatalog.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Athena::DataCatalog.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::Athena::DataCatalog.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::DataCatalog.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::Athena::DataCatalog.Parameters``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Athena::DataCatalog.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-datacatalog.html#cfn-athena-datacatalog-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataCatalogProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnNamedQuery(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-athena.CfnNamedQuery",
):
    '''A CloudFormation ``AWS::Athena::NamedQuery``.

    :cloudformationResource: AWS::Athena::NamedQuery
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        database: builtins.str,
        query_string: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        work_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Athena::NamedQuery``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param database: ``AWS::Athena::NamedQuery.Database``.
        :param query_string: ``AWS::Athena::NamedQuery.QueryString``.
        :param description: ``AWS::Athena::NamedQuery.Description``.
        :param name: ``AWS::Athena::NamedQuery.Name``.
        :param work_group: ``AWS::Athena::NamedQuery.WorkGroup``.
        '''
        props = CfnNamedQueryProps(
            database=database,
            query_string=query_string,
            description=description,
            name=name,
            work_group=work_group,
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
    @jsii.member(jsii_name="attrNamedQueryId")
    def attr_named_query_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: NamedQueryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamedQueryId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        '''``AWS::Athena::NamedQuery.Database``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-database
        '''
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        jsii.set(self, "database", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> builtins.str:
        '''``AWS::Athena::NamedQuery.QueryString``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-querystring
        '''
        return typing.cast(builtins.str, jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: builtins.str) -> None:
        jsii.set(self, "queryString", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::NamedQuery.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::NamedQuery.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workGroup")
    def work_group(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::NamedQuery.WorkGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-workgroup
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workGroup"))

    @work_group.setter
    def work_group(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "workGroup", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-athena.CfnNamedQueryProps",
    jsii_struct_bases=[],
    name_mapping={
        "database": "database",
        "query_string": "queryString",
        "description": "description",
        "name": "name",
        "work_group": "workGroup",
    },
)
class CfnNamedQueryProps:
    def __init__(
        self,
        *,
        database: builtins.str,
        query_string: builtins.str,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        work_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Athena::NamedQuery``.

        :param database: ``AWS::Athena::NamedQuery.Database``.
        :param query_string: ``AWS::Athena::NamedQuery.QueryString``.
        :param description: ``AWS::Athena::NamedQuery.Description``.
        :param name: ``AWS::Athena::NamedQuery.Name``.
        :param work_group: ``AWS::Athena::NamedQuery.WorkGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "query_string": query_string,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if work_group is not None:
            self._values["work_group"] = work_group

    @builtins.property
    def database(self) -> builtins.str:
        '''``AWS::Athena::NamedQuery.Database``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-database
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_string(self) -> builtins.str:
        '''``AWS::Athena::NamedQuery.QueryString``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-querystring
        '''
        result = self._values.get("query_string")
        assert result is not None, "Required property 'query_string' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::NamedQuery.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::NamedQuery.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def work_group(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::NamedQuery.WorkGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-workgroup
        '''
        result = self._values.get("work_group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNamedQueryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPreparedStatement(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-athena.CfnPreparedStatement",
):
    '''A CloudFormation ``AWS::Athena::PreparedStatement``.

    :cloudformationResource: AWS::Athena::PreparedStatement
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        query_statement: builtins.str,
        statement_name: builtins.str,
        work_group: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Athena::PreparedStatement``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param query_statement: ``AWS::Athena::PreparedStatement.QueryStatement``.
        :param statement_name: ``AWS::Athena::PreparedStatement.StatementName``.
        :param work_group: ``AWS::Athena::PreparedStatement.WorkGroup``.
        :param description: ``AWS::Athena::PreparedStatement.Description``.
        '''
        props = CfnPreparedStatementProps(
            query_statement=query_statement,
            statement_name=statement_name,
            work_group=work_group,
            description=description,
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
    @jsii.member(jsii_name="queryStatement")
    def query_statement(self) -> builtins.str:
        '''``AWS::Athena::PreparedStatement.QueryStatement``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-querystatement
        '''
        return typing.cast(builtins.str, jsii.get(self, "queryStatement"))

    @query_statement.setter
    def query_statement(self, value: builtins.str) -> None:
        jsii.set(self, "queryStatement", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="statementName")
    def statement_name(self) -> builtins.str:
        '''``AWS::Athena::PreparedStatement.StatementName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-statementname
        '''
        return typing.cast(builtins.str, jsii.get(self, "statementName"))

    @statement_name.setter
    def statement_name(self, value: builtins.str) -> None:
        jsii.set(self, "statementName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workGroup")
    def work_group(self) -> builtins.str:
        '''``AWS::Athena::PreparedStatement.WorkGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-workgroup
        '''
        return typing.cast(builtins.str, jsii.get(self, "workGroup"))

    @work_group.setter
    def work_group(self, value: builtins.str) -> None:
        jsii.set(self, "workGroup", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::PreparedStatement.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-athena.CfnPreparedStatementProps",
    jsii_struct_bases=[],
    name_mapping={
        "query_statement": "queryStatement",
        "statement_name": "statementName",
        "work_group": "workGroup",
        "description": "description",
    },
)
class CfnPreparedStatementProps:
    def __init__(
        self,
        *,
        query_statement: builtins.str,
        statement_name: builtins.str,
        work_group: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Athena::PreparedStatement``.

        :param query_statement: ``AWS::Athena::PreparedStatement.QueryStatement``.
        :param statement_name: ``AWS::Athena::PreparedStatement.StatementName``.
        :param work_group: ``AWS::Athena::PreparedStatement.WorkGroup``.
        :param description: ``AWS::Athena::PreparedStatement.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "query_statement": query_statement,
            "statement_name": statement_name,
            "work_group": work_group,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def query_statement(self) -> builtins.str:
        '''``AWS::Athena::PreparedStatement.QueryStatement``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-querystatement
        '''
        result = self._values.get("query_statement")
        assert result is not None, "Required property 'query_statement' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statement_name(self) -> builtins.str:
        '''``AWS::Athena::PreparedStatement.StatementName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-statementname
        '''
        result = self._values.get("statement_name")
        assert result is not None, "Required property 'statement_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def work_group(self) -> builtins.str:
        '''``AWS::Athena::PreparedStatement.WorkGroup``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-workgroup
        '''
        result = self._values.get("work_group")
        assert result is not None, "Required property 'work_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::PreparedStatement.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-preparedstatement.html#cfn-athena-preparedstatement-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPreparedStatementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnWorkGroup(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-athena.CfnWorkGroup",
):
    '''A CloudFormation ``AWS::Athena::WorkGroup``.

    :cloudformationResource: AWS::Athena::WorkGroup
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        recursive_delete_option: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        work_group_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.WorkGroupConfigurationProperty"]] = None,
        work_group_configuration_updates: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.WorkGroupConfigurationUpdatesProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::Athena::WorkGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Athena::WorkGroup.Name``.
        :param description: ``AWS::Athena::WorkGroup.Description``.
        :param recursive_delete_option: ``AWS::Athena::WorkGroup.RecursiveDeleteOption``.
        :param state: ``AWS::Athena::WorkGroup.State``.
        :param tags: ``AWS::Athena::WorkGroup.Tags``.
        :param work_group_configuration: ``AWS::Athena::WorkGroup.WorkGroupConfiguration``.
        :param work_group_configuration_updates: ``AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates``.
        '''
        props = CfnWorkGroupProps(
            name=name,
            description=description,
            recursive_delete_option=recursive_delete_option,
            state=state,
            tags=tags,
            work_group_configuration=work_group_configuration,
            work_group_configuration_updates=work_group_configuration_updates,
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
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrWorkGroupConfigurationEngineVersionEffectiveEngineVersion")
    def attr_work_group_configuration_engine_version_effective_engine_version(
        self,
    ) -> builtins.str:
        '''
        :cloudformationAttribute: WorkGroupConfiguration.EngineVersion.EffectiveEngineVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkGroupConfigurationEngineVersionEffectiveEngineVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrWorkGroupConfigurationUpdatesEngineVersionEffectiveEngineVersion")
    def attr_work_group_configuration_updates_engine_version_effective_engine_version(
        self,
    ) -> builtins.str:
        '''
        :cloudformationAttribute: WorkGroupConfigurationUpdates.EngineVersion.EffectiveEngineVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkGroupConfigurationUpdatesEngineVersionEffectiveEngineVersion"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Athena::WorkGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Athena::WorkGroup.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::WorkGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="recursiveDeleteOption")
    def recursive_delete_option(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Athena::WorkGroup.RecursiveDeleteOption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "recursiveDeleteOption"))

    @recursive_delete_option.setter
    def recursive_delete_option(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "recursiveDeleteOption", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::WorkGroup.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "state", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workGroupConfiguration")
    def work_group_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.WorkGroupConfigurationProperty"]]:
        '''``AWS::Athena::WorkGroup.WorkGroupConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.WorkGroupConfigurationProperty"]], jsii.get(self, "workGroupConfiguration"))

    @work_group_configuration.setter
    def work_group_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.WorkGroupConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "workGroupConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="workGroupConfigurationUpdates")
    def work_group_configuration_updates(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.WorkGroupConfigurationUpdatesProperty"]]:
        '''``AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.WorkGroupConfigurationUpdatesProperty"]], jsii.get(self, "workGroupConfigurationUpdates"))

    @work_group_configuration_updates.setter
    def work_group_configuration_updates(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.WorkGroupConfigurationUpdatesProperty"]],
    ) -> None:
        jsii.set(self, "workGroupConfigurationUpdates", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-athena.CfnWorkGroup.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_option": "encryptionOption", "kms_key": "kmsKey"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_option: builtins.str,
            kms_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param encryption_option: ``CfnWorkGroup.EncryptionConfigurationProperty.EncryptionOption``.
            :param kms_key: ``CfnWorkGroup.EncryptionConfigurationProperty.KmsKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "encryption_option": encryption_option,
            }
            if kms_key is not None:
                self._values["kms_key"] = kms_key

        @builtins.property
        def encryption_option(self) -> builtins.str:
            '''``CfnWorkGroup.EncryptionConfigurationProperty.EncryptionOption``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-encryptionoption
            '''
            result = self._values.get("encryption_option")
            assert result is not None, "Required property 'encryption_option' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkGroup.EncryptionConfigurationProperty.KmsKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-encryptionconfiguration.html#cfn-athena-workgroup-encryptionconfiguration-kmskey
            '''
            result = self._values.get("kms_key")
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
        jsii_type="@aws-cdk/aws-athena.CfnWorkGroup.EngineVersionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "effective_engine_version": "effectiveEngineVersion",
            "selected_engine_version": "selectedEngineVersion",
        },
    )
    class EngineVersionProperty:
        def __init__(
            self,
            *,
            effective_engine_version: typing.Optional[builtins.str] = None,
            selected_engine_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param effective_engine_version: ``CfnWorkGroup.EngineVersionProperty.EffectiveEngineVersion``.
            :param selected_engine_version: ``CfnWorkGroup.EngineVersionProperty.SelectedEngineVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if effective_engine_version is not None:
                self._values["effective_engine_version"] = effective_engine_version
            if selected_engine_version is not None:
                self._values["selected_engine_version"] = selected_engine_version

        @builtins.property
        def effective_engine_version(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkGroup.EngineVersionProperty.EffectiveEngineVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html#cfn-athena-workgroup-engineversion-effectiveengineversion
            '''
            result = self._values.get("effective_engine_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def selected_engine_version(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkGroup.EngineVersionProperty.SelectedEngineVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-engineversion.html#cfn-athena-workgroup-engineversion-selectedengineversion
            '''
            result = self._values.get("selected_engine_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EngineVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-athena.CfnWorkGroup.ResultConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_configuration": "encryptionConfiguration",
            "output_location": "outputLocation",
        },
    )
    class ResultConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EncryptionConfigurationProperty"]] = None,
            output_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param encryption_configuration: ``CfnWorkGroup.ResultConfigurationProperty.EncryptionConfiguration``.
            :param output_location: ``CfnWorkGroup.ResultConfigurationProperty.OutputLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if output_location is not None:
                self._values["output_location"] = output_location

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EncryptionConfigurationProperty"]]:
            '''``CfnWorkGroup.ResultConfigurationProperty.EncryptionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EncryptionConfigurationProperty"]], result)

        @builtins.property
        def output_location(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkGroup.ResultConfigurationProperty.OutputLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfiguration.html#cfn-athena-workgroup-resultconfiguration-outputlocation
            '''
            result = self._values.get("output_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResultConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-athena.CfnWorkGroup.ResultConfigurationUpdatesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_configuration": "encryptionConfiguration",
            "output_location": "outputLocation",
            "remove_encryption_configuration": "removeEncryptionConfiguration",
            "remove_output_location": "removeOutputLocation",
        },
    )
    class ResultConfigurationUpdatesProperty:
        def __init__(
            self,
            *,
            encryption_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EncryptionConfigurationProperty"]] = None,
            output_location: typing.Optional[builtins.str] = None,
            remove_encryption_configuration: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            remove_output_location: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param encryption_configuration: ``CfnWorkGroup.ResultConfigurationUpdatesProperty.EncryptionConfiguration``.
            :param output_location: ``CfnWorkGroup.ResultConfigurationUpdatesProperty.OutputLocation``.
            :param remove_encryption_configuration: ``CfnWorkGroup.ResultConfigurationUpdatesProperty.RemoveEncryptionConfiguration``.
            :param remove_output_location: ``CfnWorkGroup.ResultConfigurationUpdatesProperty.RemoveOutputLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if output_location is not None:
                self._values["output_location"] = output_location
            if remove_encryption_configuration is not None:
                self._values["remove_encryption_configuration"] = remove_encryption_configuration
            if remove_output_location is not None:
                self._values["remove_output_location"] = remove_output_location

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EncryptionConfigurationProperty"]]:
            '''``CfnWorkGroup.ResultConfigurationUpdatesProperty.EncryptionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EncryptionConfigurationProperty"]], result)

        @builtins.property
        def output_location(self) -> typing.Optional[builtins.str]:
            '''``CfnWorkGroup.ResultConfigurationUpdatesProperty.OutputLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-outputlocation
            '''
            result = self._values.get("output_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def remove_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnWorkGroup.ResultConfigurationUpdatesProperty.RemoveEncryptionConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeencryptionconfiguration
            '''
            result = self._values.get("remove_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def remove_output_location(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnWorkGroup.ResultConfigurationUpdatesProperty.RemoveOutputLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-resultconfigurationupdates.html#cfn-athena-workgroup-resultconfigurationupdates-removeoutputlocation
            '''
            result = self._values.get("remove_output_location")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResultConfigurationUpdatesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-athena.CfnWorkGroup.WorkGroupConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bytes_scanned_cutoff_per_query": "bytesScannedCutoffPerQuery",
            "enforce_work_group_configuration": "enforceWorkGroupConfiguration",
            "engine_version": "engineVersion",
            "publish_cloud_watch_metrics_enabled": "publishCloudWatchMetricsEnabled",
            "requester_pays_enabled": "requesterPaysEnabled",
            "result_configuration": "resultConfiguration",
        },
    )
    class WorkGroupConfigurationProperty:
        def __init__(
            self,
            *,
            bytes_scanned_cutoff_per_query: typing.Optional[jsii.Number] = None,
            enforce_work_group_configuration: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            engine_version: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EngineVersionProperty"]] = None,
            publish_cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            requester_pays_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            result_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.ResultConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param bytes_scanned_cutoff_per_query: ``CfnWorkGroup.WorkGroupConfigurationProperty.BytesScannedCutoffPerQuery``.
            :param enforce_work_group_configuration: ``CfnWorkGroup.WorkGroupConfigurationProperty.EnforceWorkGroupConfiguration``.
            :param engine_version: ``CfnWorkGroup.WorkGroupConfigurationProperty.EngineVersion``.
            :param publish_cloud_watch_metrics_enabled: ``CfnWorkGroup.WorkGroupConfigurationProperty.PublishCloudWatchMetricsEnabled``.
            :param requester_pays_enabled: ``CfnWorkGroup.WorkGroupConfigurationProperty.RequesterPaysEnabled``.
            :param result_configuration: ``CfnWorkGroup.WorkGroupConfigurationProperty.ResultConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if bytes_scanned_cutoff_per_query is not None:
                self._values["bytes_scanned_cutoff_per_query"] = bytes_scanned_cutoff_per_query
            if enforce_work_group_configuration is not None:
                self._values["enforce_work_group_configuration"] = enforce_work_group_configuration
            if engine_version is not None:
                self._values["engine_version"] = engine_version
            if publish_cloud_watch_metrics_enabled is not None:
                self._values["publish_cloud_watch_metrics_enabled"] = publish_cloud_watch_metrics_enabled
            if requester_pays_enabled is not None:
                self._values["requester_pays_enabled"] = requester_pays_enabled
            if result_configuration is not None:
                self._values["result_configuration"] = result_configuration

        @builtins.property
        def bytes_scanned_cutoff_per_query(self) -> typing.Optional[jsii.Number]:
            '''``CfnWorkGroup.WorkGroupConfigurationProperty.BytesScannedCutoffPerQuery``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-bytesscannedcutoffperquery
            '''
            result = self._values.get("bytes_scanned_cutoff_per_query")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def enforce_work_group_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnWorkGroup.WorkGroupConfigurationProperty.EnforceWorkGroupConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-enforceworkgroupconfiguration
            '''
            result = self._values.get("enforce_work_group_configuration")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def engine_version(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EngineVersionProperty"]]:
            '''``CfnWorkGroup.WorkGroupConfigurationProperty.EngineVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-engineversion
            '''
            result = self._values.get("engine_version")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EngineVersionProperty"]], result)

        @builtins.property
        def publish_cloud_watch_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnWorkGroup.WorkGroupConfigurationProperty.PublishCloudWatchMetricsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-publishcloudwatchmetricsenabled
            '''
            result = self._values.get("publish_cloud_watch_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def requester_pays_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnWorkGroup.WorkGroupConfigurationProperty.RequesterPaysEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-requesterpaysenabled
            '''
            result = self._values.get("requester_pays_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def result_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.ResultConfigurationProperty"]]:
            '''``CfnWorkGroup.WorkGroupConfigurationProperty.ResultConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfiguration.html#cfn-athena-workgroup-workgroupconfiguration-resultconfiguration
            '''
            result = self._values.get("result_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.ResultConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkGroupConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-athena.CfnWorkGroup.WorkGroupConfigurationUpdatesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bytes_scanned_cutoff_per_query": "bytesScannedCutoffPerQuery",
            "enforce_work_group_configuration": "enforceWorkGroupConfiguration",
            "engine_version": "engineVersion",
            "publish_cloud_watch_metrics_enabled": "publishCloudWatchMetricsEnabled",
            "remove_bytes_scanned_cutoff_per_query": "removeBytesScannedCutoffPerQuery",
            "requester_pays_enabled": "requesterPaysEnabled",
            "result_configuration_updates": "resultConfigurationUpdates",
        },
    )
    class WorkGroupConfigurationUpdatesProperty:
        def __init__(
            self,
            *,
            bytes_scanned_cutoff_per_query: typing.Optional[jsii.Number] = None,
            enforce_work_group_configuration: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            engine_version: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EngineVersionProperty"]] = None,
            publish_cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            remove_bytes_scanned_cutoff_per_query: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            requester_pays_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            result_configuration_updates: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.ResultConfigurationUpdatesProperty"]] = None,
        ) -> None:
            '''
            :param bytes_scanned_cutoff_per_query: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.BytesScannedCutoffPerQuery``.
            :param enforce_work_group_configuration: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.EnforceWorkGroupConfiguration``.
            :param engine_version: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.EngineVersion``.
            :param publish_cloud_watch_metrics_enabled: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.PublishCloudWatchMetricsEnabled``.
            :param remove_bytes_scanned_cutoff_per_query: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.RemoveBytesScannedCutoffPerQuery``.
            :param requester_pays_enabled: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.RequesterPaysEnabled``.
            :param result_configuration_updates: ``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.ResultConfigurationUpdates``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if bytes_scanned_cutoff_per_query is not None:
                self._values["bytes_scanned_cutoff_per_query"] = bytes_scanned_cutoff_per_query
            if enforce_work_group_configuration is not None:
                self._values["enforce_work_group_configuration"] = enforce_work_group_configuration
            if engine_version is not None:
                self._values["engine_version"] = engine_version
            if publish_cloud_watch_metrics_enabled is not None:
                self._values["publish_cloud_watch_metrics_enabled"] = publish_cloud_watch_metrics_enabled
            if remove_bytes_scanned_cutoff_per_query is not None:
                self._values["remove_bytes_scanned_cutoff_per_query"] = remove_bytes_scanned_cutoff_per_query
            if requester_pays_enabled is not None:
                self._values["requester_pays_enabled"] = requester_pays_enabled
            if result_configuration_updates is not None:
                self._values["result_configuration_updates"] = result_configuration_updates

        @builtins.property
        def bytes_scanned_cutoff_per_query(self) -> typing.Optional[jsii.Number]:
            '''``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.BytesScannedCutoffPerQuery``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-bytesscannedcutoffperquery
            '''
            result = self._values.get("bytes_scanned_cutoff_per_query")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def enforce_work_group_configuration(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.EnforceWorkGroupConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-enforceworkgroupconfiguration
            '''
            result = self._values.get("enforce_work_group_configuration")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def engine_version(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EngineVersionProperty"]]:
            '''``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.EngineVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-engineversion
            '''
            result = self._values.get("engine_version")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.EngineVersionProperty"]], result)

        @builtins.property
        def publish_cloud_watch_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.PublishCloudWatchMetricsEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-publishcloudwatchmetricsenabled
            '''
            result = self._values.get("publish_cloud_watch_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def remove_bytes_scanned_cutoff_per_query(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.RemoveBytesScannedCutoffPerQuery``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-removebytesscannedcutoffperquery
            '''
            result = self._values.get("remove_bytes_scanned_cutoff_per_query")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def requester_pays_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.RequesterPaysEnabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-requesterpaysenabled
            '''
            result = self._values.get("requester_pays_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def result_configuration_updates(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.ResultConfigurationUpdatesProperty"]]:
            '''``CfnWorkGroup.WorkGroupConfigurationUpdatesProperty.ResultConfigurationUpdates``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-athena-workgroup-workgroupconfigurationupdates.html#cfn-athena-workgroup-workgroupconfigurationupdates-resultconfigurationupdates
            '''
            result = self._values.get("result_configuration_updates")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnWorkGroup.ResultConfigurationUpdatesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkGroupConfigurationUpdatesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-athena.CfnWorkGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "recursive_delete_option": "recursiveDeleteOption",
        "state": "state",
        "tags": "tags",
        "work_group_configuration": "workGroupConfiguration",
        "work_group_configuration_updates": "workGroupConfigurationUpdates",
    },
)
class CfnWorkGroupProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        recursive_delete_option: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        work_group_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkGroup.WorkGroupConfigurationProperty]] = None,
        work_group_configuration_updates: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkGroup.WorkGroupConfigurationUpdatesProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Athena::WorkGroup``.

        :param name: ``AWS::Athena::WorkGroup.Name``.
        :param description: ``AWS::Athena::WorkGroup.Description``.
        :param recursive_delete_option: ``AWS::Athena::WorkGroup.RecursiveDeleteOption``.
        :param state: ``AWS::Athena::WorkGroup.State``.
        :param tags: ``AWS::Athena::WorkGroup.Tags``.
        :param work_group_configuration: ``AWS::Athena::WorkGroup.WorkGroupConfiguration``.
        :param work_group_configuration_updates: ``AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if recursive_delete_option is not None:
            self._values["recursive_delete_option"] = recursive_delete_option
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags
        if work_group_configuration is not None:
            self._values["work_group_configuration"] = work_group_configuration
        if work_group_configuration_updates is not None:
            self._values["work_group_configuration_updates"] = work_group_configuration_updates

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Athena::WorkGroup.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::WorkGroup.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recursive_delete_option(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Athena::WorkGroup.RecursiveDeleteOption``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-recursivedeleteoption
        '''
        result = self._values.get("recursive_delete_option")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''``AWS::Athena::WorkGroup.State``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::Athena::WorkGroup.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def work_group_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkGroup.WorkGroupConfigurationProperty]]:
        '''``AWS::Athena::WorkGroup.WorkGroupConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfiguration
        '''
        result = self._values.get("work_group_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkGroup.WorkGroupConfigurationProperty]], result)

    @builtins.property
    def work_group_configuration_updates(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkGroup.WorkGroupConfigurationUpdatesProperty]]:
        '''``AWS::Athena::WorkGroup.WorkGroupConfigurationUpdates``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html#cfn-athena-workgroup-workgroupconfigurationupdates
        '''
        result = self._values.get("work_group_configuration_updates")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnWorkGroup.WorkGroupConfigurationUpdatesProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataCatalog",
    "CfnDataCatalogProps",
    "CfnNamedQuery",
    "CfnNamedQueryProps",
    "CfnPreparedStatement",
    "CfnPreparedStatementProps",
    "CfnWorkGroup",
    "CfnWorkGroupProps",
]

publication.publish()
