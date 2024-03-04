'''
# AWS OpsWorks Construct Library

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
class CfnApp(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-opsworks.CfnApp",
):
    '''A CloudFormation ``AWS::OpsWorks::App``.

    :cloudformationResource: AWS::OpsWorks::App
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        stack_id: builtins.str,
        type: builtins.str,
        app_source: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.SourceProperty"]] = None,
        attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        data_sources: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnApp.DataSourceProperty"]]]] = None,
        description: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_ssl: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnApp.EnvironmentVariableProperty"]]]] = None,
        shortname: typing.Optional[builtins.str] = None,
        ssl_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.SslConfigurationProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::OpsWorks::App``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::OpsWorks::App.Name``.
        :param stack_id: ``AWS::OpsWorks::App.StackId``.
        :param type: ``AWS::OpsWorks::App.Type``.
        :param app_source: ``AWS::OpsWorks::App.AppSource``.
        :param attributes: ``AWS::OpsWorks::App.Attributes``.
        :param data_sources: ``AWS::OpsWorks::App.DataSources``.
        :param description: ``AWS::OpsWorks::App.Description``.
        :param domains: ``AWS::OpsWorks::App.Domains``.
        :param enable_ssl: ``AWS::OpsWorks::App.EnableSsl``.
        :param environment: ``AWS::OpsWorks::App.Environment``.
        :param shortname: ``AWS::OpsWorks::App.Shortname``.
        :param ssl_configuration: ``AWS::OpsWorks::App.SslConfiguration``.
        '''
        props = CfnAppProps(
            name=name,
            stack_id=stack_id,
            type=type,
            app_source=app_source,
            attributes=attributes,
            data_sources=data_sources,
            description=description,
            domains=domains,
            enable_ssl=enable_ssl,
            environment=environment,
            shortname=shortname,
            ssl_configuration=ssl_configuration,
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
        '''``AWS::OpsWorks::App.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        '''``AWS::OpsWorks::App.StackId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-stackid
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        jsii.set(self, "stackId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::OpsWorks::App.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="appSource")
    def app_source(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.SourceProperty"]]:
        '''``AWS::OpsWorks::App.AppSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-appsource
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.SourceProperty"]], jsii.get(self, "appSource"))

    @app_source.setter
    def app_source(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.SourceProperty"]],
    ) -> None:
        jsii.set(self, "appSource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::OpsWorks::App.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-attributes
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        jsii.set(self, "attributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dataSources")
    def data_sources(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.DataSourceProperty"]]]]:
        '''``AWS::OpsWorks::App.DataSources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-datasources
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.DataSourceProperty"]]]], jsii.get(self, "dataSources"))

    @data_sources.setter
    def data_sources(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.DataSourceProperty"]]]],
    ) -> None:
        jsii.set(self, "dataSources", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::App.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="domains")
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::App.Domains``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-domains
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "domains"))

    @domains.setter
    def domains(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "domains", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableSsl")
    def enable_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::App.EnableSsl``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-enablessl
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enableSsl"))

    @enable_ssl.setter
    def enable_ssl(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enableSsl", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="environment")
    def environment(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.EnvironmentVariableProperty"]]]]:
        '''``AWS::OpsWorks::App.Environment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-environment
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.EnvironmentVariableProperty"]]]], jsii.get(self, "environment"))

    @environment.setter
    def environment(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApp.EnvironmentVariableProperty"]]]],
    ) -> None:
        jsii.set(self, "environment", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="shortname")
    def shortname(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::App.Shortname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-shortname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortname"))

    @shortname.setter
    def shortname(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "shortname", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sslConfiguration")
    def ssl_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.SslConfigurationProperty"]]:
        '''``AWS::OpsWorks::App.SslConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-sslconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.SslConfigurationProperty"]], jsii.get(self, "sslConfiguration"))

    @ssl_configuration.setter
    def ssl_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApp.SslConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "sslConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnApp.DataSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "database_name": "databaseName", "type": "type"},
    )
    class DataSourceProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param arn: ``CfnApp.DataSourceProperty.Arn``.
            :param database_name: ``CfnApp.DataSourceProperty.DatabaseName``.
            :param type: ``CfnApp.DataSourceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if database_name is not None:
                self._values["database_name"] = database_name
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.DataSourceProperty.Arn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.DataSourceProperty.DatabaseName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.DataSourceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-datasource.html#cfn-opsworks-app-datasource-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnApp.EnvironmentVariableProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value", "secure": "secure"},
    )
    class EnvironmentVariableProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: builtins.str,
            secure: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param key: ``CfnApp.EnvironmentVariableProperty.Key``.
            :param value: ``CfnApp.EnvironmentVariableProperty.Value``.
            :param secure: ``CfnApp.EnvironmentVariableProperty.Secure``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "key": key,
                "value": value,
            }
            if secure is not None:
                self._values["secure"] = secure

        @builtins.property
        def key(self) -> builtins.str:
            '''``CfnApp.EnvironmentVariableProperty.Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#cfn-opsworks-app-environment-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnApp.EnvironmentVariableProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secure(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnApp.EnvironmentVariableProperty.Secure``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-environment.html#cfn-opsworks-app-environment-secure
            '''
            result = self._values.get("secure")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnvironmentVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnApp.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password": "password",
            "revision": "revision",
            "ssh_key": "sshKey",
            "type": "type",
            "url": "url",
            "username": "username",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            password: typing.Optional[builtins.str] = None,
            revision: typing.Optional[builtins.str] = None,
            ssh_key: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param password: ``CfnApp.SourceProperty.Password``.
            :param revision: ``CfnApp.SourceProperty.Revision``.
            :param ssh_key: ``CfnApp.SourceProperty.SshKey``.
            :param type: ``CfnApp.SourceProperty.Type``.
            :param url: ``CfnApp.SourceProperty.Url``.
            :param username: ``CfnApp.SourceProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if password is not None:
                self._values["password"] = password
            if revision is not None:
                self._values["revision"] = revision
            if ssh_key is not None:
                self._values["ssh_key"] = ssh_key
            if type is not None:
                self._values["type"] = type
            if url is not None:
                self._values["url"] = url
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.SourceProperty.Password``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-pw
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def revision(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.SourceProperty.Revision``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-revision
            '''
            result = self._values.get("revision")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssh_key(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.SourceProperty.SshKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-sshkey
            '''
            result = self._values.get("ssh_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.SourceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.SourceProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.SourceProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnApp.SslConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate": "certificate",
            "chain": "chain",
            "private_key": "privateKey",
        },
    )
    class SslConfigurationProperty:
        def __init__(
            self,
            *,
            certificate: typing.Optional[builtins.str] = None,
            chain: typing.Optional[builtins.str] = None,
            private_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param certificate: ``CfnApp.SslConfigurationProperty.Certificate``.
            :param chain: ``CfnApp.SslConfigurationProperty.Chain``.
            :param private_key: ``CfnApp.SslConfigurationProperty.PrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if certificate is not None:
                self._values["certificate"] = certificate
            if chain is not None:
                self._values["chain"] = chain
            if private_key is not None:
                self._values["private_key"] = private_key

        @builtins.property
        def certificate(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.SslConfigurationProperty.Certificate``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-certificate
            '''
            result = self._values.get("certificate")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def chain(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.SslConfigurationProperty.Chain``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-chain
            '''
            result = self._values.get("chain")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def private_key(self) -> typing.Optional[builtins.str]:
            '''``CfnApp.SslConfigurationProperty.PrivateKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-app-sslconfiguration.html#cfn-opsworks-app-sslconfig-privatekey
            '''
            result = self._values.get("private_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SslConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-opsworks.CfnAppProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "stack_id": "stackId",
        "type": "type",
        "app_source": "appSource",
        "attributes": "attributes",
        "data_sources": "dataSources",
        "description": "description",
        "domains": "domains",
        "enable_ssl": "enableSsl",
        "environment": "environment",
        "shortname": "shortname",
        "ssl_configuration": "sslConfiguration",
    },
)
class CfnAppProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        stack_id: builtins.str,
        type: builtins.str,
        app_source: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.SourceProperty]] = None,
        attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        data_sources: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnApp.DataSourceProperty]]]] = None,
        description: typing.Optional[builtins.str] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_ssl: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        environment: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnApp.EnvironmentVariableProperty]]]] = None,
        shortname: typing.Optional[builtins.str] = None,
        ssl_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.SslConfigurationProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::OpsWorks::App``.

        :param name: ``AWS::OpsWorks::App.Name``.
        :param stack_id: ``AWS::OpsWorks::App.StackId``.
        :param type: ``AWS::OpsWorks::App.Type``.
        :param app_source: ``AWS::OpsWorks::App.AppSource``.
        :param attributes: ``AWS::OpsWorks::App.Attributes``.
        :param data_sources: ``AWS::OpsWorks::App.DataSources``.
        :param description: ``AWS::OpsWorks::App.Description``.
        :param domains: ``AWS::OpsWorks::App.Domains``.
        :param enable_ssl: ``AWS::OpsWorks::App.EnableSsl``.
        :param environment: ``AWS::OpsWorks::App.Environment``.
        :param shortname: ``AWS::OpsWorks::App.Shortname``.
        :param ssl_configuration: ``AWS::OpsWorks::App.SslConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "stack_id": stack_id,
            "type": type,
        }
        if app_source is not None:
            self._values["app_source"] = app_source
        if attributes is not None:
            self._values["attributes"] = attributes
        if data_sources is not None:
            self._values["data_sources"] = data_sources
        if description is not None:
            self._values["description"] = description
        if domains is not None:
            self._values["domains"] = domains
        if enable_ssl is not None:
            self._values["enable_ssl"] = enable_ssl
        if environment is not None:
            self._values["environment"] = environment
        if shortname is not None:
            self._values["shortname"] = shortname
        if ssl_configuration is not None:
            self._values["ssl_configuration"] = ssl_configuration

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::OpsWorks::App.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''``AWS::OpsWorks::App.StackId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-stackid
        '''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::OpsWorks::App.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_source(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.SourceProperty]]:
        '''``AWS::OpsWorks::App.AppSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-appsource
        '''
        result = self._values.get("app_source")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.SourceProperty]], result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::OpsWorks::App.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def data_sources(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnApp.DataSourceProperty]]]]:
        '''``AWS::OpsWorks::App.DataSources``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-datasources
        '''
        result = self._values.get("data_sources")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnApp.DataSourceProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::App.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::App.Domains``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-domains
        '''
        result = self._values.get("domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::App.EnableSsl``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-enablessl
        '''
        result = self._values.get("enable_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnApp.EnvironmentVariableProperty]]]]:
        '''``AWS::OpsWorks::App.Environment``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-environment
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnApp.EnvironmentVariableProperty]]]], result)

    @builtins.property
    def shortname(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::App.Shortname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-shortname
        '''
        result = self._values.get("shortname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.SslConfigurationProperty]]:
        '''``AWS::OpsWorks::App.SslConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html#cfn-opsworks-app-sslconfiguration
        '''
        result = self._values.get("ssl_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApp.SslConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnElasticLoadBalancerAttachment(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-opsworks.CfnElasticLoadBalancerAttachment",
):
    '''A CloudFormation ``AWS::OpsWorks::ElasticLoadBalancerAttachment``.

    :cloudformationResource: AWS::OpsWorks::ElasticLoadBalancerAttachment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        elastic_load_balancer_name: builtins.str,
        layer_id: builtins.str,
    ) -> None:
        '''Create a new ``AWS::OpsWorks::ElasticLoadBalancerAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param elastic_load_balancer_name: ``AWS::OpsWorks::ElasticLoadBalancerAttachment.ElasticLoadBalancerName``.
        :param layer_id: ``AWS::OpsWorks::ElasticLoadBalancerAttachment.LayerId``.
        '''
        props = CfnElasticLoadBalancerAttachmentProps(
            elastic_load_balancer_name=elastic_load_balancer_name, layer_id=layer_id
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
    @jsii.member(jsii_name="elasticLoadBalancerName")
    def elastic_load_balancer_name(self) -> builtins.str:
        '''``AWS::OpsWorks::ElasticLoadBalancerAttachment.ElasticLoadBalancerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html#cfn-opsworks-elbattachment-elbname
        '''
        return typing.cast(builtins.str, jsii.get(self, "elasticLoadBalancerName"))

    @elastic_load_balancer_name.setter
    def elastic_load_balancer_name(self, value: builtins.str) -> None:
        jsii.set(self, "elasticLoadBalancerName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="layerId")
    def layer_id(self) -> builtins.str:
        '''``AWS::OpsWorks::ElasticLoadBalancerAttachment.LayerId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html#cfn-opsworks-elbattachment-layerid
        '''
        return typing.cast(builtins.str, jsii.get(self, "layerId"))

    @layer_id.setter
    def layer_id(self, value: builtins.str) -> None:
        jsii.set(self, "layerId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-opsworks.CfnElasticLoadBalancerAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "elastic_load_balancer_name": "elasticLoadBalancerName",
        "layer_id": "layerId",
    },
)
class CfnElasticLoadBalancerAttachmentProps:
    def __init__(
        self,
        *,
        elastic_load_balancer_name: builtins.str,
        layer_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::OpsWorks::ElasticLoadBalancerAttachment``.

        :param elastic_load_balancer_name: ``AWS::OpsWorks::ElasticLoadBalancerAttachment.ElasticLoadBalancerName``.
        :param layer_id: ``AWS::OpsWorks::ElasticLoadBalancerAttachment.LayerId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "elastic_load_balancer_name": elastic_load_balancer_name,
            "layer_id": layer_id,
        }

    @builtins.property
    def elastic_load_balancer_name(self) -> builtins.str:
        '''``AWS::OpsWorks::ElasticLoadBalancerAttachment.ElasticLoadBalancerName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html#cfn-opsworks-elbattachment-elbname
        '''
        result = self._values.get("elastic_load_balancer_name")
        assert result is not None, "Required property 'elastic_load_balancer_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def layer_id(self) -> builtins.str:
        '''``AWS::OpsWorks::ElasticLoadBalancerAttachment.LayerId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html#cfn-opsworks-elbattachment-layerid
        '''
        result = self._values.get("layer_id")
        assert result is not None, "Required property 'layer_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnElasticLoadBalancerAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnInstance(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-opsworks.CfnInstance",
):
    '''A CloudFormation ``AWS::OpsWorks::Instance``.

    :cloudformationResource: AWS::OpsWorks::Instance
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        instance_type: builtins.str,
        layer_ids: typing.Sequence[builtins.str],
        stack_id: builtins.str,
        agent_version: typing.Optional[builtins.str] = None,
        ami_id: typing.Optional[builtins.str] = None,
        architecture: typing.Optional[builtins.str] = None,
        auto_scaling_type: typing.Optional[builtins.str] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        block_device_mappings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.BlockDeviceMappingProperty"]]]] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        elastic_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        hostname: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        os: typing.Optional[builtins.str] = None,
        root_device_type: typing.Optional[builtins.str] = None,
        ssh_key_name: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tenancy: typing.Optional[builtins.str] = None,
        time_based_auto_scaling: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.TimeBasedAutoScalingProperty"]] = None,
        virtualization_type: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::OpsWorks::Instance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param instance_type: ``AWS::OpsWorks::Instance.InstanceType``.
        :param layer_ids: ``AWS::OpsWorks::Instance.LayerIds``.
        :param stack_id: ``AWS::OpsWorks::Instance.StackId``.
        :param agent_version: ``AWS::OpsWorks::Instance.AgentVersion``.
        :param ami_id: ``AWS::OpsWorks::Instance.AmiId``.
        :param architecture: ``AWS::OpsWorks::Instance.Architecture``.
        :param auto_scaling_type: ``AWS::OpsWorks::Instance.AutoScalingType``.
        :param availability_zone: ``AWS::OpsWorks::Instance.AvailabilityZone``.
        :param block_device_mappings: ``AWS::OpsWorks::Instance.BlockDeviceMappings``.
        :param ebs_optimized: ``AWS::OpsWorks::Instance.EbsOptimized``.
        :param elastic_ips: ``AWS::OpsWorks::Instance.ElasticIps``.
        :param hostname: ``AWS::OpsWorks::Instance.Hostname``.
        :param install_updates_on_boot: ``AWS::OpsWorks::Instance.InstallUpdatesOnBoot``.
        :param os: ``AWS::OpsWorks::Instance.Os``.
        :param root_device_type: ``AWS::OpsWorks::Instance.RootDeviceType``.
        :param ssh_key_name: ``AWS::OpsWorks::Instance.SshKeyName``.
        :param subnet_id: ``AWS::OpsWorks::Instance.SubnetId``.
        :param tenancy: ``AWS::OpsWorks::Instance.Tenancy``.
        :param time_based_auto_scaling: ``AWS::OpsWorks::Instance.TimeBasedAutoScaling``.
        :param virtualization_type: ``AWS::OpsWorks::Instance.VirtualizationType``.
        :param volumes: ``AWS::OpsWorks::Instance.Volumes``.
        '''
        props = CfnInstanceProps(
            instance_type=instance_type,
            layer_ids=layer_ids,
            stack_id=stack_id,
            agent_version=agent_version,
            ami_id=ami_id,
            architecture=architecture,
            auto_scaling_type=auto_scaling_type,
            availability_zone=availability_zone,
            block_device_mappings=block_device_mappings,
            ebs_optimized=ebs_optimized,
            elastic_ips=elastic_ips,
            hostname=hostname,
            install_updates_on_boot=install_updates_on_boot,
            os=os,
            root_device_type=root_device_type,
            ssh_key_name=ssh_key_name,
            subnet_id=subnet_id,
            tenancy=tenancy,
            time_based_auto_scaling=time_based_auto_scaling,
            virtualization_type=virtualization_type,
            volumes=volumes,
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
    @jsii.member(jsii_name="attrAvailabilityZone")
    def attr_availability_zone(self) -> builtins.str:
        '''
        :cloudformationAttribute: AvailabilityZone
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAvailabilityZone"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPrivateDnsName")
    def attr_private_dns_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: PrivateDnsName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrivateDnsName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPrivateIp")
    def attr_private_ip(self) -> builtins.str:
        '''
        :cloudformationAttribute: PrivateIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrivateIp"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublicDnsName")
    def attr_public_dns_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublicDnsName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublicDnsName"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attrPublicIp")
    def attr_public_ip(self) -> builtins.str:
        '''
        :cloudformationAttribute: PublicIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPublicIp"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        '''``AWS::OpsWorks::Instance.InstanceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-instancetype
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        jsii.set(self, "instanceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="layerIds")
    def layer_ids(self) -> typing.List[builtins.str]:
        '''``AWS::OpsWorks::Instance.LayerIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-layerids
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "layerIds"))

    @layer_ids.setter
    def layer_ids(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "layerIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        '''``AWS::OpsWorks::Instance.StackId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-stackid
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        jsii.set(self, "stackId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="agentVersion")
    def agent_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.AgentVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-agentversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentVersion"))

    @agent_version.setter
    def agent_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "agentVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="amiId")
    def ami_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.AmiId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-amiid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amiId"))

    @ami_id.setter
    def ami_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "amiId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="architecture")
    def architecture(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.Architecture``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-architecture
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "architecture"))

    @architecture.setter
    def architecture(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "architecture", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoScalingType")
    def auto_scaling_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.AutoScalingType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-autoscalingtype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingType"))

    @auto_scaling_type.setter
    def auto_scaling_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "autoScalingType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.AvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-availabilityzone
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "availabilityZone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.BlockDeviceMappingProperty"]]]]:
        '''``AWS::OpsWorks::Instance.BlockDeviceMappings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-blockdevicemappings
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.BlockDeviceMappingProperty"]]]], jsii.get(self, "blockDeviceMappings"))

    @block_device_mappings.setter
    def block_device_mappings(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.BlockDeviceMappingProperty"]]]],
    ) -> None:
        jsii.set(self, "blockDeviceMappings", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ebsOptimized")
    def ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Instance.EbsOptimized``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-ebsoptimized
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "ebsOptimized"))

    @ebs_optimized.setter
    def ebs_optimized(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "ebsOptimized", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="elasticIps")
    def elastic_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::Instance.ElasticIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-elasticips
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "elasticIps"))

    @elastic_ips.setter
    def elastic_ips(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "elasticIps", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.Hostname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-hostname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "hostname", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="installUpdatesOnBoot")
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Instance.InstallUpdatesOnBoot``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-installupdatesonboot
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "installUpdatesOnBoot"))

    @install_updates_on_boot.setter
    def install_updates_on_boot(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "installUpdatesOnBoot", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="os")
    def os(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.Os``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-os
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "os"))

    @os.setter
    def os(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "os", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rootDeviceType")
    def root_device_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.RootDeviceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-rootdevicetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rootDeviceType"))

    @root_device_type.setter
    def root_device_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "rootDeviceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sshKeyName")
    def ssh_key_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.SshKeyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-sshkeyname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshKeyName"))

    @ssh_key_name.setter
    def ssh_key_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sshKeyName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-subnetid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "subnetId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tenancy")
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.Tenancy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-tenancy
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenancy"))

    @tenancy.setter
    def tenancy(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tenancy", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="timeBasedAutoScaling")
    def time_based_auto_scaling(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.TimeBasedAutoScalingProperty"]]:
        '''``AWS::OpsWorks::Instance.TimeBasedAutoScaling``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-timebasedautoscaling
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.TimeBasedAutoScalingProperty"]], jsii.get(self, "timeBasedAutoScaling"))

    @time_based_auto_scaling.setter
    def time_based_auto_scaling(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.TimeBasedAutoScalingProperty"]],
    ) -> None:
        jsii.set(self, "timeBasedAutoScaling", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="virtualizationType")
    def virtualization_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.VirtualizationType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-virtualizationtype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualizationType"))

    @virtualization_type.setter
    def virtualization_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "virtualizationType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::Instance.Volumes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-volumes
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "volumes"))

    @volumes.setter
    def volumes(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "volumes", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnInstance.BlockDeviceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "ebs": "ebs",
            "no_device": "noDevice",
            "virtual_name": "virtualName",
        },
    )
    class BlockDeviceMappingProperty:
        def __init__(
            self,
            *,
            device_name: typing.Optional[builtins.str] = None,
            ebs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.EbsBlockDeviceProperty"]] = None,
            no_device: typing.Optional[builtins.str] = None,
            virtual_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param device_name: ``CfnInstance.BlockDeviceMappingProperty.DeviceName``.
            :param ebs: ``CfnInstance.BlockDeviceMappingProperty.Ebs``.
            :param no_device: ``CfnInstance.BlockDeviceMappingProperty.NoDevice``.
            :param virtual_name: ``CfnInstance.BlockDeviceMappingProperty.VirtualName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if device_name is not None:
                self._values["device_name"] = device_name
            if ebs is not None:
                self._values["ebs"] = ebs
            if no_device is not None:
                self._values["no_device"] = no_device
            if virtual_name is not None:
                self._values["virtual_name"] = virtual_name

        @builtins.property
        def device_name(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.BlockDeviceMappingProperty.DeviceName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-devicename
            '''
            result = self._values.get("device_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.EbsBlockDeviceProperty"]]:
            '''``CfnInstance.BlockDeviceMappingProperty.Ebs``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-ebs
            '''
            result = self._values.get("ebs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.EbsBlockDeviceProperty"]], result)

        @builtins.property
        def no_device(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.BlockDeviceMappingProperty.NoDevice``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-nodevice
            '''
            result = self._values.get("no_device")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def virtual_name(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.BlockDeviceMappingProperty.VirtualName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-blockdevicemapping.html#cfn-opsworks-instance-blockdevicemapping-virtualname
            '''
            result = self._values.get("virtual_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlockDeviceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnInstance.EbsBlockDeviceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_on_termination": "deleteOnTermination",
            "iops": "iops",
            "snapshot_id": "snapshotId",
            "volume_size": "volumeSize",
            "volume_type": "volumeType",
        },
    )
    class EbsBlockDeviceProperty:
        def __init__(
            self,
            *,
            delete_on_termination: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            iops: typing.Optional[jsii.Number] = None,
            snapshot_id: typing.Optional[builtins.str] = None,
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param delete_on_termination: ``CfnInstance.EbsBlockDeviceProperty.DeleteOnTermination``.
            :param iops: ``CfnInstance.EbsBlockDeviceProperty.Iops``.
            :param snapshot_id: ``CfnInstance.EbsBlockDeviceProperty.SnapshotId``.
            :param volume_size: ``CfnInstance.EbsBlockDeviceProperty.VolumeSize``.
            :param volume_type: ``CfnInstance.EbsBlockDeviceProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if delete_on_termination is not None:
                self._values["delete_on_termination"] = delete_on_termination
            if iops is not None:
                self._values["iops"] = iops
            if snapshot_id is not None:
                self._values["snapshot_id"] = snapshot_id
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def delete_on_termination(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnInstance.EbsBlockDeviceProperty.DeleteOnTermination``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-deleteontermination
            '''
            result = self._values.get("delete_on_termination")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstance.EbsBlockDeviceProperty.Iops``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def snapshot_id(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.EbsBlockDeviceProperty.SnapshotId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-snapshotid
            '''
            result = self._values.get("snapshot_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''``CfnInstance.EbsBlockDeviceProperty.VolumeSize``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''``CfnInstance.EbsBlockDeviceProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-ebsblockdevice.html#cfn-opsworks-instance-ebsblockdevice-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsBlockDeviceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnInstance.TimeBasedAutoScalingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "friday": "friday",
            "monday": "monday",
            "saturday": "saturday",
            "sunday": "sunday",
            "thursday": "thursday",
            "tuesday": "tuesday",
            "wednesday": "wednesday",
        },
    )
    class TimeBasedAutoScalingProperty:
        def __init__(
            self,
            *,
            friday: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            monday: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            saturday: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            sunday: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            thursday: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            tuesday: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            wednesday: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''
            :param friday: ``CfnInstance.TimeBasedAutoScalingProperty.Friday``.
            :param monday: ``CfnInstance.TimeBasedAutoScalingProperty.Monday``.
            :param saturday: ``CfnInstance.TimeBasedAutoScalingProperty.Saturday``.
            :param sunday: ``CfnInstance.TimeBasedAutoScalingProperty.Sunday``.
            :param thursday: ``CfnInstance.TimeBasedAutoScalingProperty.Thursday``.
            :param tuesday: ``CfnInstance.TimeBasedAutoScalingProperty.Tuesday``.
            :param wednesday: ``CfnInstance.TimeBasedAutoScalingProperty.Wednesday``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if friday is not None:
                self._values["friday"] = friday
            if monday is not None:
                self._values["monday"] = monday
            if saturday is not None:
                self._values["saturday"] = saturday
            if sunday is not None:
                self._values["sunday"] = sunday
            if thursday is not None:
                self._values["thursday"] = thursday
            if tuesday is not None:
                self._values["tuesday"] = tuesday
            if wednesday is not None:
                self._values["wednesday"] = wednesday

        @builtins.property
        def friday(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnInstance.TimeBasedAutoScalingProperty.Friday``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-friday
            '''
            result = self._values.get("friday")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def monday(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnInstance.TimeBasedAutoScalingProperty.Monday``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-monday
            '''
            result = self._values.get("monday")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def saturday(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnInstance.TimeBasedAutoScalingProperty.Saturday``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-saturday
            '''
            result = self._values.get("saturday")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def sunday(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnInstance.TimeBasedAutoScalingProperty.Sunday``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-sunday
            '''
            result = self._values.get("sunday")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def thursday(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnInstance.TimeBasedAutoScalingProperty.Thursday``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-thursday
            '''
            result = self._values.get("thursday")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def tuesday(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnInstance.TimeBasedAutoScalingProperty.Tuesday``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-tuesday
            '''
            result = self._values.get("tuesday")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def wednesday(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''``CfnInstance.TimeBasedAutoScalingProperty.Wednesday``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-instance-timebasedautoscaling.html#cfn-opsworks-instance-timebasedautoscaling-wednesday
            '''
            result = self._values.get("wednesday")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeBasedAutoScalingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-opsworks.CfnInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "layer_ids": "layerIds",
        "stack_id": "stackId",
        "agent_version": "agentVersion",
        "ami_id": "amiId",
        "architecture": "architecture",
        "auto_scaling_type": "autoScalingType",
        "availability_zone": "availabilityZone",
        "block_device_mappings": "blockDeviceMappings",
        "ebs_optimized": "ebsOptimized",
        "elastic_ips": "elasticIps",
        "hostname": "hostname",
        "install_updates_on_boot": "installUpdatesOnBoot",
        "os": "os",
        "root_device_type": "rootDeviceType",
        "ssh_key_name": "sshKeyName",
        "subnet_id": "subnetId",
        "tenancy": "tenancy",
        "time_based_auto_scaling": "timeBasedAutoScaling",
        "virtualization_type": "virtualizationType",
        "volumes": "volumes",
    },
)
class CfnInstanceProps:
    def __init__(
        self,
        *,
        instance_type: builtins.str,
        layer_ids: typing.Sequence[builtins.str],
        stack_id: builtins.str,
        agent_version: typing.Optional[builtins.str] = None,
        ami_id: typing.Optional[builtins.str] = None,
        architecture: typing.Optional[builtins.str] = None,
        auto_scaling_type: typing.Optional[builtins.str] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        block_device_mappings: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnInstance.BlockDeviceMappingProperty]]]] = None,
        ebs_optimized: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        elastic_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
        hostname: typing.Optional[builtins.str] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        os: typing.Optional[builtins.str] = None,
        root_device_type: typing.Optional[builtins.str] = None,
        ssh_key_name: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tenancy: typing.Optional[builtins.str] = None,
        time_based_auto_scaling: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.TimeBasedAutoScalingProperty]] = None,
        virtualization_type: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::OpsWorks::Instance``.

        :param instance_type: ``AWS::OpsWorks::Instance.InstanceType``.
        :param layer_ids: ``AWS::OpsWorks::Instance.LayerIds``.
        :param stack_id: ``AWS::OpsWorks::Instance.StackId``.
        :param agent_version: ``AWS::OpsWorks::Instance.AgentVersion``.
        :param ami_id: ``AWS::OpsWorks::Instance.AmiId``.
        :param architecture: ``AWS::OpsWorks::Instance.Architecture``.
        :param auto_scaling_type: ``AWS::OpsWorks::Instance.AutoScalingType``.
        :param availability_zone: ``AWS::OpsWorks::Instance.AvailabilityZone``.
        :param block_device_mappings: ``AWS::OpsWorks::Instance.BlockDeviceMappings``.
        :param ebs_optimized: ``AWS::OpsWorks::Instance.EbsOptimized``.
        :param elastic_ips: ``AWS::OpsWorks::Instance.ElasticIps``.
        :param hostname: ``AWS::OpsWorks::Instance.Hostname``.
        :param install_updates_on_boot: ``AWS::OpsWorks::Instance.InstallUpdatesOnBoot``.
        :param os: ``AWS::OpsWorks::Instance.Os``.
        :param root_device_type: ``AWS::OpsWorks::Instance.RootDeviceType``.
        :param ssh_key_name: ``AWS::OpsWorks::Instance.SshKeyName``.
        :param subnet_id: ``AWS::OpsWorks::Instance.SubnetId``.
        :param tenancy: ``AWS::OpsWorks::Instance.Tenancy``.
        :param time_based_auto_scaling: ``AWS::OpsWorks::Instance.TimeBasedAutoScaling``.
        :param virtualization_type: ``AWS::OpsWorks::Instance.VirtualizationType``.
        :param volumes: ``AWS::OpsWorks::Instance.Volumes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
            "layer_ids": layer_ids,
            "stack_id": stack_id,
        }
        if agent_version is not None:
            self._values["agent_version"] = agent_version
        if ami_id is not None:
            self._values["ami_id"] = ami_id
        if architecture is not None:
            self._values["architecture"] = architecture
        if auto_scaling_type is not None:
            self._values["auto_scaling_type"] = auto_scaling_type
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if ebs_optimized is not None:
            self._values["ebs_optimized"] = ebs_optimized
        if elastic_ips is not None:
            self._values["elastic_ips"] = elastic_ips
        if hostname is not None:
            self._values["hostname"] = hostname
        if install_updates_on_boot is not None:
            self._values["install_updates_on_boot"] = install_updates_on_boot
        if os is not None:
            self._values["os"] = os
        if root_device_type is not None:
            self._values["root_device_type"] = root_device_type
        if ssh_key_name is not None:
            self._values["ssh_key_name"] = ssh_key_name
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tenancy is not None:
            self._values["tenancy"] = tenancy
        if time_based_auto_scaling is not None:
            self._values["time_based_auto_scaling"] = time_based_auto_scaling
        if virtualization_type is not None:
            self._values["virtualization_type"] = virtualization_type
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def instance_type(self) -> builtins.str:
        '''``AWS::OpsWorks::Instance.InstanceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-instancetype
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def layer_ids(self) -> typing.List[builtins.str]:
        '''``AWS::OpsWorks::Instance.LayerIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-layerids
        '''
        result = self._values.get("layer_ids")
        assert result is not None, "Required property 'layer_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''``AWS::OpsWorks::Instance.StackId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-stackid
        '''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.AgentVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-agentversion
        '''
        result = self._values.get("agent_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ami_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.AmiId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-amiid
        '''
        result = self._values.get("ami_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def architecture(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.Architecture``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-architecture
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_scaling_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.AutoScalingType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-autoscalingtype
        '''
        result = self._values.get("auto_scaling_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.AvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInstance.BlockDeviceMappingProperty]]]]:
        '''``AWS::OpsWorks::Instance.BlockDeviceMappings``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-blockdevicemappings
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnInstance.BlockDeviceMappingProperty]]]], result)

    @builtins.property
    def ebs_optimized(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Instance.EbsOptimized``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-ebsoptimized
        '''
        result = self._values.get("ebs_optimized")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def elastic_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::Instance.ElasticIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-elasticips
        '''
        result = self._values.get("elastic_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.Hostname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-hostname
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Instance.InstallUpdatesOnBoot``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-installupdatesonboot
        '''
        result = self._values.get("install_updates_on_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def os(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.Os``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-os
        '''
        result = self._values.get("os")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_device_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.RootDeviceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-rootdevicetype
        '''
        result = self._values.get("root_device_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_key_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.SshKeyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-sshkeyname
        '''
        result = self._values.get("ssh_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.SubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-subnetid
        '''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenancy(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.Tenancy``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-tenancy
        '''
        result = self._values.get("tenancy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_based_auto_scaling(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.TimeBasedAutoScalingProperty]]:
        '''``AWS::OpsWorks::Instance.TimeBasedAutoScaling``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-timebasedautoscaling
        '''
        result = self._values.get("time_based_auto_scaling")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnInstance.TimeBasedAutoScalingProperty]], result)

    @builtins.property
    def virtualization_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Instance.VirtualizationType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-virtualizationtype
        '''
        result = self._values.get("virtualization_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::Instance.Volumes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html#cfn-opsworks-instance-volumes
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnLayer(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-opsworks.CfnLayer",
):
    '''A CloudFormation ``AWS::OpsWorks::Layer``.

    :cloudformationResource: AWS::OpsWorks::Layer
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        auto_assign_elastic_ips: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        auto_assign_public_ips: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        enable_auto_healing: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        name: builtins.str,
        shortname: builtins.str,
        stack_id: builtins.str,
        type: builtins.str,
        attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Any = None,
        custom_recipes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.RecipesProperty"]] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        lifecycle_event_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.LifecycleEventConfigurationProperty"]] = None,
        load_based_auto_scaling: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.LoadBasedAutoScalingProperty"]] = None,
        packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        volume_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.VolumeConfigurationProperty"]]]] = None,
    ) -> None:
        '''Create a new ``AWS::OpsWorks::Layer``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param auto_assign_elastic_ips: ``AWS::OpsWorks::Layer.AutoAssignElasticIps``.
        :param auto_assign_public_ips: ``AWS::OpsWorks::Layer.AutoAssignPublicIps``.
        :param enable_auto_healing: ``AWS::OpsWorks::Layer.EnableAutoHealing``.
        :param name: ``AWS::OpsWorks::Layer.Name``.
        :param shortname: ``AWS::OpsWorks::Layer.Shortname``.
        :param stack_id: ``AWS::OpsWorks::Layer.StackId``.
        :param type: ``AWS::OpsWorks::Layer.Type``.
        :param attributes: ``AWS::OpsWorks::Layer.Attributes``.
        :param custom_instance_profile_arn: ``AWS::OpsWorks::Layer.CustomInstanceProfileArn``.
        :param custom_json: ``AWS::OpsWorks::Layer.CustomJson``.
        :param custom_recipes: ``AWS::OpsWorks::Layer.CustomRecipes``.
        :param custom_security_group_ids: ``AWS::OpsWorks::Layer.CustomSecurityGroupIds``.
        :param install_updates_on_boot: ``AWS::OpsWorks::Layer.InstallUpdatesOnBoot``.
        :param lifecycle_event_configuration: ``AWS::OpsWorks::Layer.LifecycleEventConfiguration``.
        :param load_based_auto_scaling: ``AWS::OpsWorks::Layer.LoadBasedAutoScaling``.
        :param packages: ``AWS::OpsWorks::Layer.Packages``.
        :param tags: ``AWS::OpsWorks::Layer.Tags``.
        :param use_ebs_optimized_instances: ``AWS::OpsWorks::Layer.UseEbsOptimizedInstances``.
        :param volume_configurations: ``AWS::OpsWorks::Layer.VolumeConfigurations``.
        '''
        props = CfnLayerProps(
            auto_assign_elastic_ips=auto_assign_elastic_ips,
            auto_assign_public_ips=auto_assign_public_ips,
            enable_auto_healing=enable_auto_healing,
            name=name,
            shortname=shortname,
            stack_id=stack_id,
            type=type,
            attributes=attributes,
            custom_instance_profile_arn=custom_instance_profile_arn,
            custom_json=custom_json,
            custom_recipes=custom_recipes,
            custom_security_group_ids=custom_security_group_ids,
            install_updates_on_boot=install_updates_on_boot,
            lifecycle_event_configuration=lifecycle_event_configuration,
            load_based_auto_scaling=load_based_auto_scaling,
            packages=packages,
            tags=tags,
            use_ebs_optimized_instances=use_ebs_optimized_instances,
            volume_configurations=volume_configurations,
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
        '''``AWS::OpsWorks::Layer.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoAssignElasticIps")
    def auto_assign_elastic_ips(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::OpsWorks::Layer.AutoAssignElasticIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignelasticips
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "autoAssignElasticIps"))

    @auto_assign_elastic_ips.setter
    def auto_assign_elastic_ips(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "autoAssignElasticIps", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="autoAssignPublicIps")
    def auto_assign_public_ips(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::OpsWorks::Layer.AutoAssignPublicIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignpublicips
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "autoAssignPublicIps"))

    @auto_assign_public_ips.setter
    def auto_assign_public_ips(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "autoAssignPublicIps", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customJson")
    def custom_json(self) -> typing.Any:
        '''``AWS::OpsWorks::Layer.CustomJson``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customjson
        '''
        return typing.cast(typing.Any, jsii.get(self, "customJson"))

    @custom_json.setter
    def custom_json(self, value: typing.Any) -> None:
        jsii.set(self, "customJson", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enableAutoHealing")
    def enable_auto_healing(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::OpsWorks::Layer.EnableAutoHealing``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-enableautohealing
        '''
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], jsii.get(self, "enableAutoHealing"))

    @enable_auto_healing.setter
    def enable_auto_healing(
        self,
        value: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "enableAutoHealing", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::OpsWorks::Layer.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="shortname")
    def shortname(self) -> builtins.str:
        '''``AWS::OpsWorks::Layer.Shortname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-shortname
        '''
        return typing.cast(builtins.str, jsii.get(self, "shortname"))

    @shortname.setter
    def shortname(self, value: builtins.str) -> None:
        jsii.set(self, "shortname", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        '''``AWS::OpsWorks::Layer.StackId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-stackid
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        jsii.set(self, "stackId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::OpsWorks::Layer.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::OpsWorks::Layer.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-attributes
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        jsii.set(self, "attributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customInstanceProfileArn")
    def custom_instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Layer.CustomInstanceProfileArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-custominstanceprofilearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customInstanceProfileArn"))

    @custom_instance_profile_arn.setter
    def custom_instance_profile_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "customInstanceProfileArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customRecipes")
    def custom_recipes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.RecipesProperty"]]:
        '''``AWS::OpsWorks::Layer.CustomRecipes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customrecipes
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.RecipesProperty"]], jsii.get(self, "customRecipes"))

    @custom_recipes.setter
    def custom_recipes(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.RecipesProperty"]],
    ) -> None:
        jsii.set(self, "customRecipes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customSecurityGroupIds")
    def custom_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::Layer.CustomSecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customsecuritygroupids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customSecurityGroupIds"))

    @custom_security_group_ids.setter
    def custom_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        jsii.set(self, "customSecurityGroupIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="installUpdatesOnBoot")
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Layer.InstallUpdatesOnBoot``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-installupdatesonboot
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "installUpdatesOnBoot"))

    @install_updates_on_boot.setter
    def install_updates_on_boot(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "installUpdatesOnBoot", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="lifecycleEventConfiguration")
    def lifecycle_event_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.LifecycleEventConfigurationProperty"]]:
        '''``AWS::OpsWorks::Layer.LifecycleEventConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-lifecycleeventconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.LifecycleEventConfigurationProperty"]], jsii.get(self, "lifecycleEventConfiguration"))

    @lifecycle_event_configuration.setter
    def lifecycle_event_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.LifecycleEventConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "lifecycleEventConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="loadBasedAutoScaling")
    def load_based_auto_scaling(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.LoadBasedAutoScalingProperty"]]:
        '''``AWS::OpsWorks::Layer.LoadBasedAutoScaling``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-loadbasedautoscaling
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.LoadBasedAutoScalingProperty"]], jsii.get(self, "loadBasedAutoScaling"))

    @load_based_auto_scaling.setter
    def load_based_auto_scaling(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.LoadBasedAutoScalingProperty"]],
    ) -> None:
        jsii.set(self, "loadBasedAutoScaling", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="packages")
    def packages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::Layer.Packages``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-packages
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "packages"))

    @packages.setter
    def packages(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "packages", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="useEbsOptimizedInstances")
    def use_ebs_optimized_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Layer.UseEbsOptimizedInstances``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-useebsoptimizedinstances
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "useEbsOptimizedInstances"))

    @use_ebs_optimized_instances.setter
    def use_ebs_optimized_instances(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "useEbsOptimizedInstances", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="volumeConfigurations")
    def volume_configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.VolumeConfigurationProperty"]]]]:
        '''``AWS::OpsWorks::Layer.VolumeConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-volumeconfigurations
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.VolumeConfigurationProperty"]]]], jsii.get(self, "volumeConfigurations"))

    @volume_configurations.setter
    def volume_configurations(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.VolumeConfigurationProperty"]]]],
    ) -> None:
        jsii.set(self, "volumeConfigurations", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnLayer.AutoScalingThresholdsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu_threshold": "cpuThreshold",
            "ignore_metrics_time": "ignoreMetricsTime",
            "instance_count": "instanceCount",
            "load_threshold": "loadThreshold",
            "memory_threshold": "memoryThreshold",
            "thresholds_wait_time": "thresholdsWaitTime",
        },
    )
    class AutoScalingThresholdsProperty:
        def __init__(
            self,
            *,
            cpu_threshold: typing.Optional[jsii.Number] = None,
            ignore_metrics_time: typing.Optional[jsii.Number] = None,
            instance_count: typing.Optional[jsii.Number] = None,
            load_threshold: typing.Optional[jsii.Number] = None,
            memory_threshold: typing.Optional[jsii.Number] = None,
            thresholds_wait_time: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param cpu_threshold: ``CfnLayer.AutoScalingThresholdsProperty.CpuThreshold``.
            :param ignore_metrics_time: ``CfnLayer.AutoScalingThresholdsProperty.IgnoreMetricsTime``.
            :param instance_count: ``CfnLayer.AutoScalingThresholdsProperty.InstanceCount``.
            :param load_threshold: ``CfnLayer.AutoScalingThresholdsProperty.LoadThreshold``.
            :param memory_threshold: ``CfnLayer.AutoScalingThresholdsProperty.MemoryThreshold``.
            :param thresholds_wait_time: ``CfnLayer.AutoScalingThresholdsProperty.ThresholdsWaitTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if cpu_threshold is not None:
                self._values["cpu_threshold"] = cpu_threshold
            if ignore_metrics_time is not None:
                self._values["ignore_metrics_time"] = ignore_metrics_time
            if instance_count is not None:
                self._values["instance_count"] = instance_count
            if load_threshold is not None:
                self._values["load_threshold"] = load_threshold
            if memory_threshold is not None:
                self._values["memory_threshold"] = memory_threshold
            if thresholds_wait_time is not None:
                self._values["thresholds_wait_time"] = thresholds_wait_time

        @builtins.property
        def cpu_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.AutoScalingThresholdsProperty.CpuThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-cputhreshold
            '''
            result = self._values.get("cpu_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ignore_metrics_time(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.AutoScalingThresholdsProperty.IgnoreMetricsTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-ignoremetricstime
            '''
            result = self._values.get("ignore_metrics_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def instance_count(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.AutoScalingThresholdsProperty.InstanceCount``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-instancecount
            '''
            result = self._values.get("instance_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def load_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.AutoScalingThresholdsProperty.LoadThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-loadthreshold
            '''
            result = self._values.get("load_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def memory_threshold(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.AutoScalingThresholdsProperty.MemoryThreshold``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-memorythreshold
            '''
            result = self._values.get("memory_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def thresholds_wait_time(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.AutoScalingThresholdsProperty.ThresholdsWaitTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling-autoscalingthresholds.html#cfn-opsworks-layer-loadbasedautoscaling-autoscalingthresholds-thresholdwaittime
            '''
            result = self._values.get("thresholds_wait_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingThresholdsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnLayer.LifecycleEventConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"shutdown_event_configuration": "shutdownEventConfiguration"},
    )
    class LifecycleEventConfigurationProperty:
        def __init__(
            self,
            *,
            shutdown_event_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.ShutdownEventConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param shutdown_event_configuration: ``CfnLayer.LifecycleEventConfigurationProperty.ShutdownEventConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if shutdown_event_configuration is not None:
                self._values["shutdown_event_configuration"] = shutdown_event_configuration

        @builtins.property
        def shutdown_event_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.ShutdownEventConfigurationProperty"]]:
            '''``CfnLayer.LifecycleEventConfigurationProperty.ShutdownEventConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration
            '''
            result = self._values.get("shutdown_event_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.ShutdownEventConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecycleEventConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnLayer.LoadBasedAutoScalingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "down_scaling": "downScaling",
            "enable": "enable",
            "up_scaling": "upScaling",
        },
    )
    class LoadBasedAutoScalingProperty:
        def __init__(
            self,
            *,
            down_scaling: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.AutoScalingThresholdsProperty"]] = None,
            enable: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            up_scaling: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.AutoScalingThresholdsProperty"]] = None,
        ) -> None:
            '''
            :param down_scaling: ``CfnLayer.LoadBasedAutoScalingProperty.DownScaling``.
            :param enable: ``CfnLayer.LoadBasedAutoScalingProperty.Enable``.
            :param up_scaling: ``CfnLayer.LoadBasedAutoScalingProperty.UpScaling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if down_scaling is not None:
                self._values["down_scaling"] = down_scaling
            if enable is not None:
                self._values["enable"] = enable
            if up_scaling is not None:
                self._values["up_scaling"] = up_scaling

        @builtins.property
        def down_scaling(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.AutoScalingThresholdsProperty"]]:
            '''``CfnLayer.LoadBasedAutoScalingProperty.DownScaling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-downscaling
            '''
            result = self._values.get("down_scaling")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.AutoScalingThresholdsProperty"]], result)

        @builtins.property
        def enable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnLayer.LoadBasedAutoScalingProperty.Enable``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-enable
            '''
            result = self._values.get("enable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def up_scaling(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.AutoScalingThresholdsProperty"]]:
            '''``CfnLayer.LoadBasedAutoScalingProperty.UpScaling``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-loadbasedautoscaling.html#cfn-opsworks-layer-loadbasedautoscaling-upscaling
            '''
            result = self._values.get("up_scaling")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnLayer.AutoScalingThresholdsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoadBasedAutoScalingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnLayer.RecipesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configure": "configure",
            "deploy": "deploy",
            "setup": "setup",
            "shutdown": "shutdown",
            "undeploy": "undeploy",
        },
    )
    class RecipesProperty:
        def __init__(
            self,
            *,
            configure: typing.Optional[typing.Sequence[builtins.str]] = None,
            deploy: typing.Optional[typing.Sequence[builtins.str]] = None,
            setup: typing.Optional[typing.Sequence[builtins.str]] = None,
            shutdown: typing.Optional[typing.Sequence[builtins.str]] = None,
            undeploy: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param configure: ``CfnLayer.RecipesProperty.Configure``.
            :param deploy: ``CfnLayer.RecipesProperty.Deploy``.
            :param setup: ``CfnLayer.RecipesProperty.Setup``.
            :param shutdown: ``CfnLayer.RecipesProperty.Shutdown``.
            :param undeploy: ``CfnLayer.RecipesProperty.Undeploy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if configure is not None:
                self._values["configure"] = configure
            if deploy is not None:
                self._values["deploy"] = deploy
            if setup is not None:
                self._values["setup"] = setup
            if shutdown is not None:
                self._values["shutdown"] = shutdown
            if undeploy is not None:
                self._values["undeploy"] = undeploy

        @builtins.property
        def configure(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnLayer.RecipesProperty.Configure``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-configure
            '''
            result = self._values.get("configure")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def deploy(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnLayer.RecipesProperty.Deploy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-deploy
            '''
            result = self._values.get("deploy")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def setup(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnLayer.RecipesProperty.Setup``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-setup
            '''
            result = self._values.get("setup")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def shutdown(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnLayer.RecipesProperty.Shutdown``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-shutdown
            '''
            result = self._values.get("shutdown")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def undeploy(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnLayer.RecipesProperty.Undeploy``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-recipes.html#cfn-opsworks-layer-customrecipes-undeploy
            '''
            result = self._values.get("undeploy")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecipesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnLayer.ShutdownEventConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delay_until_elb_connections_drained": "delayUntilElbConnectionsDrained",
            "execution_timeout": "executionTimeout",
        },
    )
    class ShutdownEventConfigurationProperty:
        def __init__(
            self,
            *,
            delay_until_elb_connections_drained: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            execution_timeout: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param delay_until_elb_connections_drained: ``CfnLayer.ShutdownEventConfigurationProperty.DelayUntilElbConnectionsDrained``.
            :param execution_timeout: ``CfnLayer.ShutdownEventConfigurationProperty.ExecutionTimeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if delay_until_elb_connections_drained is not None:
                self._values["delay_until_elb_connections_drained"] = delay_until_elb_connections_drained
            if execution_timeout is not None:
                self._values["execution_timeout"] = execution_timeout

        @builtins.property
        def delay_until_elb_connections_drained(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnLayer.ShutdownEventConfigurationProperty.DelayUntilElbConnectionsDrained``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration-delayuntilelbconnectionsdrained
            '''
            result = self._values.get("delay_until_elb_connections_drained")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def execution_timeout(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.ShutdownEventConfigurationProperty.ExecutionTimeout``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-lifecycleeventconfiguration-shutdowneventconfiguration.html#cfn-opsworks-layer-lifecycleconfiguration-shutdowneventconfiguration-executiontimeout
            '''
            result = self._values.get("execution_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ShutdownEventConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnLayer.VolumeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encrypted": "encrypted",
            "iops": "iops",
            "mount_point": "mountPoint",
            "number_of_disks": "numberOfDisks",
            "raid_level": "raidLevel",
            "size": "size",
            "volume_type": "volumeType",
        },
    )
    class VolumeConfigurationProperty:
        def __init__(
            self,
            *,
            encrypted: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            iops: typing.Optional[jsii.Number] = None,
            mount_point: typing.Optional[builtins.str] = None,
            number_of_disks: typing.Optional[jsii.Number] = None,
            raid_level: typing.Optional[jsii.Number] = None,
            size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param encrypted: ``CfnLayer.VolumeConfigurationProperty.Encrypted``.
            :param iops: ``CfnLayer.VolumeConfigurationProperty.Iops``.
            :param mount_point: ``CfnLayer.VolumeConfigurationProperty.MountPoint``.
            :param number_of_disks: ``CfnLayer.VolumeConfigurationProperty.NumberOfDisks``.
            :param raid_level: ``CfnLayer.VolumeConfigurationProperty.RaidLevel``.
            :param size: ``CfnLayer.VolumeConfigurationProperty.Size``.
            :param volume_type: ``CfnLayer.VolumeConfigurationProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if encrypted is not None:
                self._values["encrypted"] = encrypted
            if iops is not None:
                self._values["iops"] = iops
            if mount_point is not None:
                self._values["mount_point"] = mount_point
            if number_of_disks is not None:
                self._values["number_of_disks"] = number_of_disks
            if raid_level is not None:
                self._values["raid_level"] = raid_level
            if size is not None:
                self._values["size"] = size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def encrypted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnLayer.VolumeConfigurationProperty.Encrypted``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volumeconfiguration-encrypted
            '''
            result = self._values.get("encrypted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.VolumeConfigurationProperty.Iops``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def mount_point(self) -> typing.Optional[builtins.str]:
            '''``CfnLayer.VolumeConfigurationProperty.MountPoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-mountpoint
            '''
            result = self._values.get("mount_point")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def number_of_disks(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.VolumeConfigurationProperty.NumberOfDisks``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-numberofdisks
            '''
            result = self._values.get("number_of_disks")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def raid_level(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.VolumeConfigurationProperty.RaidLevel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-raidlevel
            '''
            result = self._values.get("raid_level")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size(self) -> typing.Optional[jsii.Number]:
            '''``CfnLayer.VolumeConfigurationProperty.Size``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-size
            '''
            result = self._values.get("size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''``CfnLayer.VolumeConfigurationProperty.VolumeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-layer-volumeconfiguration.html#cfn-opsworks-layer-volconfig-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VolumeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-opsworks.CfnLayerProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_assign_elastic_ips": "autoAssignElasticIps",
        "auto_assign_public_ips": "autoAssignPublicIps",
        "enable_auto_healing": "enableAutoHealing",
        "name": "name",
        "shortname": "shortname",
        "stack_id": "stackId",
        "type": "type",
        "attributes": "attributes",
        "custom_instance_profile_arn": "customInstanceProfileArn",
        "custom_json": "customJson",
        "custom_recipes": "customRecipes",
        "custom_security_group_ids": "customSecurityGroupIds",
        "install_updates_on_boot": "installUpdatesOnBoot",
        "lifecycle_event_configuration": "lifecycleEventConfiguration",
        "load_based_auto_scaling": "loadBasedAutoScaling",
        "packages": "packages",
        "tags": "tags",
        "use_ebs_optimized_instances": "useEbsOptimizedInstances",
        "volume_configurations": "volumeConfigurations",
    },
)
class CfnLayerProps:
    def __init__(
        self,
        *,
        auto_assign_elastic_ips: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        auto_assign_public_ips: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        enable_auto_healing: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        name: builtins.str,
        shortname: builtins.str,
        stack_id: builtins.str,
        type: builtins.str,
        attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        custom_instance_profile_arn: typing.Optional[builtins.str] = None,
        custom_json: typing.Any = None,
        custom_recipes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLayer.RecipesProperty]] = None,
        custom_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        install_updates_on_boot: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        lifecycle_event_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLayer.LifecycleEventConfigurationProperty]] = None,
        load_based_auto_scaling: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLayer.LoadBasedAutoScalingProperty]] = None,
        packages: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        use_ebs_optimized_instances: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        volume_configurations: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnLayer.VolumeConfigurationProperty]]]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::OpsWorks::Layer``.

        :param auto_assign_elastic_ips: ``AWS::OpsWorks::Layer.AutoAssignElasticIps``.
        :param auto_assign_public_ips: ``AWS::OpsWorks::Layer.AutoAssignPublicIps``.
        :param enable_auto_healing: ``AWS::OpsWorks::Layer.EnableAutoHealing``.
        :param name: ``AWS::OpsWorks::Layer.Name``.
        :param shortname: ``AWS::OpsWorks::Layer.Shortname``.
        :param stack_id: ``AWS::OpsWorks::Layer.StackId``.
        :param type: ``AWS::OpsWorks::Layer.Type``.
        :param attributes: ``AWS::OpsWorks::Layer.Attributes``.
        :param custom_instance_profile_arn: ``AWS::OpsWorks::Layer.CustomInstanceProfileArn``.
        :param custom_json: ``AWS::OpsWorks::Layer.CustomJson``.
        :param custom_recipes: ``AWS::OpsWorks::Layer.CustomRecipes``.
        :param custom_security_group_ids: ``AWS::OpsWorks::Layer.CustomSecurityGroupIds``.
        :param install_updates_on_boot: ``AWS::OpsWorks::Layer.InstallUpdatesOnBoot``.
        :param lifecycle_event_configuration: ``AWS::OpsWorks::Layer.LifecycleEventConfiguration``.
        :param load_based_auto_scaling: ``AWS::OpsWorks::Layer.LoadBasedAutoScaling``.
        :param packages: ``AWS::OpsWorks::Layer.Packages``.
        :param tags: ``AWS::OpsWorks::Layer.Tags``.
        :param use_ebs_optimized_instances: ``AWS::OpsWorks::Layer.UseEbsOptimizedInstances``.
        :param volume_configurations: ``AWS::OpsWorks::Layer.VolumeConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "auto_assign_elastic_ips": auto_assign_elastic_ips,
            "auto_assign_public_ips": auto_assign_public_ips,
            "enable_auto_healing": enable_auto_healing,
            "name": name,
            "shortname": shortname,
            "stack_id": stack_id,
            "type": type,
        }
        if attributes is not None:
            self._values["attributes"] = attributes
        if custom_instance_profile_arn is not None:
            self._values["custom_instance_profile_arn"] = custom_instance_profile_arn
        if custom_json is not None:
            self._values["custom_json"] = custom_json
        if custom_recipes is not None:
            self._values["custom_recipes"] = custom_recipes
        if custom_security_group_ids is not None:
            self._values["custom_security_group_ids"] = custom_security_group_ids
        if install_updates_on_boot is not None:
            self._values["install_updates_on_boot"] = install_updates_on_boot
        if lifecycle_event_configuration is not None:
            self._values["lifecycle_event_configuration"] = lifecycle_event_configuration
        if load_based_auto_scaling is not None:
            self._values["load_based_auto_scaling"] = load_based_auto_scaling
        if packages is not None:
            self._values["packages"] = packages
        if tags is not None:
            self._values["tags"] = tags
        if use_ebs_optimized_instances is not None:
            self._values["use_ebs_optimized_instances"] = use_ebs_optimized_instances
        if volume_configurations is not None:
            self._values["volume_configurations"] = volume_configurations

    @builtins.property
    def auto_assign_elastic_ips(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::OpsWorks::Layer.AutoAssignElasticIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignelasticips
        '''
        result = self._values.get("auto_assign_elastic_ips")
        assert result is not None, "Required property 'auto_assign_elastic_ips' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def auto_assign_public_ips(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::OpsWorks::Layer.AutoAssignPublicIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-autoassignpublicips
        '''
        result = self._values.get("auto_assign_public_ips")
        assert result is not None, "Required property 'auto_assign_public_ips' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def enable_auto_healing(
        self,
    ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
        '''``AWS::OpsWorks::Layer.EnableAutoHealing``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-enableautohealing
        '''
        result = self._values.get("enable_auto_healing")
        assert result is not None, "Required property 'enable_auto_healing' is missing"
        return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::OpsWorks::Layer.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shortname(self) -> builtins.str:
        '''``AWS::OpsWorks::Layer.Shortname``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-shortname
        '''
        result = self._values.get("shortname")
        assert result is not None, "Required property 'shortname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''``AWS::OpsWorks::Layer.StackId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-stackid
        '''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::OpsWorks::Layer.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::OpsWorks::Layer.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def custom_instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Layer.CustomInstanceProfileArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-custominstanceprofilearn
        '''
        result = self._values.get("custom_instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_json(self) -> typing.Any:
        '''``AWS::OpsWorks::Layer.CustomJson``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customjson
        '''
        result = self._values.get("custom_json")
        return typing.cast(typing.Any, result)

    @builtins.property
    def custom_recipes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLayer.RecipesProperty]]:
        '''``AWS::OpsWorks::Layer.CustomRecipes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customrecipes
        '''
        result = self._values.get("custom_recipes")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLayer.RecipesProperty]], result)

    @builtins.property
    def custom_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::Layer.CustomSecurityGroupIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-customsecuritygroupids
        '''
        result = self._values.get("custom_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def install_updates_on_boot(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Layer.InstallUpdatesOnBoot``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-installupdatesonboot
        '''
        result = self._values.get("install_updates_on_boot")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def lifecycle_event_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLayer.LifecycleEventConfigurationProperty]]:
        '''``AWS::OpsWorks::Layer.LifecycleEventConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-lifecycleeventconfiguration
        '''
        result = self._values.get("lifecycle_event_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLayer.LifecycleEventConfigurationProperty]], result)

    @builtins.property
    def load_based_auto_scaling(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLayer.LoadBasedAutoScalingProperty]]:
        '''``AWS::OpsWorks::Layer.LoadBasedAutoScaling``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-loadbasedautoscaling
        '''
        result = self._values.get("load_based_auto_scaling")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnLayer.LoadBasedAutoScalingProperty]], result)

    @builtins.property
    def packages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::Layer.Packages``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-packages
        '''
        result = self._values.get("packages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::OpsWorks::Layer.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def use_ebs_optimized_instances(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Layer.UseEbsOptimizedInstances``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-useebsoptimizedinstances
        '''
        result = self._values.get("use_ebs_optimized_instances")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def volume_configurations(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnLayer.VolumeConfigurationProperty]]]]:
        '''``AWS::OpsWorks::Layer.VolumeConfigurations``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html#cfn-opsworks-layer-volumeconfigurations
        '''
        result = self._values.get("volume_configurations")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnLayer.VolumeConfigurationProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLayerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnStack(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-opsworks.CfnStack",
):
    '''A CloudFormation ``AWS::OpsWorks::Stack``.

    :cloudformationResource: AWS::OpsWorks::Stack
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        default_instance_profile_arn: builtins.str,
        name: builtins.str,
        service_role_arn: builtins.str,
        agent_version: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        chef_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.ChefConfigurationProperty"]] = None,
        clone_app_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        clone_permissions: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        configuration_manager: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.StackConfigurationManagerProperty"]] = None,
        custom_cookbooks_source: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.SourceProperty"]] = None,
        custom_json: typing.Any = None,
        default_availability_zone: typing.Optional[builtins.str] = None,
        default_os: typing.Optional[builtins.str] = None,
        default_root_device_type: typing.Optional[builtins.str] = None,
        default_ssh_key_name: typing.Optional[builtins.str] = None,
        default_subnet_id: typing.Optional[builtins.str] = None,
        ecs_cluster_arn: typing.Optional[builtins.str] = None,
        elastic_ips: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnStack.ElasticIpProperty"]]]] = None,
        hostname_theme: typing.Optional[builtins.str] = None,
        rds_db_instances: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnStack.RdsDbInstanceProperty"]]]] = None,
        source_stack_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        use_custom_cookbooks: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        use_opsworks_security_groups: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::OpsWorks::Stack``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param default_instance_profile_arn: ``AWS::OpsWorks::Stack.DefaultInstanceProfileArn``.
        :param name: ``AWS::OpsWorks::Stack.Name``.
        :param service_role_arn: ``AWS::OpsWorks::Stack.ServiceRoleArn``.
        :param agent_version: ``AWS::OpsWorks::Stack.AgentVersion``.
        :param attributes: ``AWS::OpsWorks::Stack.Attributes``.
        :param chef_configuration: ``AWS::OpsWorks::Stack.ChefConfiguration``.
        :param clone_app_ids: ``AWS::OpsWorks::Stack.CloneAppIds``.
        :param clone_permissions: ``AWS::OpsWorks::Stack.ClonePermissions``.
        :param configuration_manager: ``AWS::OpsWorks::Stack.ConfigurationManager``.
        :param custom_cookbooks_source: ``AWS::OpsWorks::Stack.CustomCookbooksSource``.
        :param custom_json: ``AWS::OpsWorks::Stack.CustomJson``.
        :param default_availability_zone: ``AWS::OpsWorks::Stack.DefaultAvailabilityZone``.
        :param default_os: ``AWS::OpsWorks::Stack.DefaultOs``.
        :param default_root_device_type: ``AWS::OpsWorks::Stack.DefaultRootDeviceType``.
        :param default_ssh_key_name: ``AWS::OpsWorks::Stack.DefaultSshKeyName``.
        :param default_subnet_id: ``AWS::OpsWorks::Stack.DefaultSubnetId``.
        :param ecs_cluster_arn: ``AWS::OpsWorks::Stack.EcsClusterArn``.
        :param elastic_ips: ``AWS::OpsWorks::Stack.ElasticIps``.
        :param hostname_theme: ``AWS::OpsWorks::Stack.HostnameTheme``.
        :param rds_db_instances: ``AWS::OpsWorks::Stack.RdsDbInstances``.
        :param source_stack_id: ``AWS::OpsWorks::Stack.SourceStackId``.
        :param tags: ``AWS::OpsWorks::Stack.Tags``.
        :param use_custom_cookbooks: ``AWS::OpsWorks::Stack.UseCustomCookbooks``.
        :param use_opsworks_security_groups: ``AWS::OpsWorks::Stack.UseOpsworksSecurityGroups``.
        :param vpc_id: ``AWS::OpsWorks::Stack.VpcId``.
        '''
        props = CfnStackProps(
            default_instance_profile_arn=default_instance_profile_arn,
            name=name,
            service_role_arn=service_role_arn,
            agent_version=agent_version,
            attributes=attributes,
            chef_configuration=chef_configuration,
            clone_app_ids=clone_app_ids,
            clone_permissions=clone_permissions,
            configuration_manager=configuration_manager,
            custom_cookbooks_source=custom_cookbooks_source,
            custom_json=custom_json,
            default_availability_zone=default_availability_zone,
            default_os=default_os,
            default_root_device_type=default_root_device_type,
            default_ssh_key_name=default_ssh_key_name,
            default_subnet_id=default_subnet_id,
            ecs_cluster_arn=ecs_cluster_arn,
            elastic_ips=elastic_ips,
            hostname_theme=hostname_theme,
            rds_db_instances=rds_db_instances,
            source_stack_id=source_stack_id,
            tags=tags,
            use_custom_cookbooks=use_custom_cookbooks,
            use_opsworks_security_groups=use_opsworks_security_groups,
            vpc_id=vpc_id,
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
        '''``AWS::OpsWorks::Stack.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customJson")
    def custom_json(self) -> typing.Any:
        '''``AWS::OpsWorks::Stack.CustomJson``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-custjson
        '''
        return typing.cast(typing.Any, jsii.get(self, "customJson"))

    @custom_json.setter
    def custom_json(self, value: typing.Any) -> None:
        jsii.set(self, "customJson", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultInstanceProfileArn")
    def default_instance_profile_arn(self) -> builtins.str:
        '''``AWS::OpsWorks::Stack.DefaultInstanceProfileArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultinstanceprof
        '''
        return typing.cast(builtins.str, jsii.get(self, "defaultInstanceProfileArn"))

    @default_instance_profile_arn.setter
    def default_instance_profile_arn(self, value: builtins.str) -> None:
        jsii.set(self, "defaultInstanceProfileArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::OpsWorks::Stack.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        '''``AWS::OpsWorks::Stack.ServiceRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-servicerolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="agentVersion")
    def agent_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.AgentVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-agentversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentVersion"))

    @agent_version.setter
    def agent_version(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "agentVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::OpsWorks::Stack.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-attributes
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        jsii.set(self, "attributes", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="chefConfiguration")
    def chef_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.ChefConfigurationProperty"]]:
        '''``AWS::OpsWorks::Stack.ChefConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-chefconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.ChefConfigurationProperty"]], jsii.get(self, "chefConfiguration"))

    @chef_configuration.setter
    def chef_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.ChefConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "chefConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cloneAppIds")
    def clone_app_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::Stack.CloneAppIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-cloneappids
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cloneAppIds"))

    @clone_app_ids.setter
    def clone_app_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        jsii.set(self, "cloneAppIds", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clonePermissions")
    def clone_permissions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Stack.ClonePermissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-clonepermissions
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "clonePermissions"))

    @clone_permissions.setter
    def clone_permissions(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "clonePermissions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationManager")
    def configuration_manager(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.StackConfigurationManagerProperty"]]:
        '''``AWS::OpsWorks::Stack.ConfigurationManager``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-configmanager
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.StackConfigurationManagerProperty"]], jsii.get(self, "configurationManager"))

    @configuration_manager.setter
    def configuration_manager(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.StackConfigurationManagerProperty"]],
    ) -> None:
        jsii.set(self, "configurationManager", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="customCookbooksSource")
    def custom_cookbooks_source(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.SourceProperty"]]:
        '''``AWS::OpsWorks::Stack.CustomCookbooksSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-custcookbooksource
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.SourceProperty"]], jsii.get(self, "customCookbooksSource"))

    @custom_cookbooks_source.setter
    def custom_cookbooks_source(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnStack.SourceProperty"]],
    ) -> None:
        jsii.set(self, "customCookbooksSource", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultAvailabilityZone")
    def default_availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.DefaultAvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultaz
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAvailabilityZone"))

    @default_availability_zone.setter
    def default_availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultAvailabilityZone", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultOs")
    def default_os(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.DefaultOs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultos
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultOs"))

    @default_os.setter
    def default_os(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultOs", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultRootDeviceType")
    def default_root_device_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.DefaultRootDeviceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultrootdevicetype
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRootDeviceType"))

    @default_root_device_type.setter
    def default_root_device_type(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultRootDeviceType", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultSshKeyName")
    def default_ssh_key_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.DefaultSshKeyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultsshkeyname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSshKeyName"))

    @default_ssh_key_name.setter
    def default_ssh_key_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultSshKeyName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultSubnetId")
    def default_subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.DefaultSubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#defaultsubnet
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSubnetId"))

    @default_subnet_id.setter
    def default_subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultSubnetId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="ecsClusterArn")
    def ecs_cluster_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.EcsClusterArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-ecsclusterarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ecsClusterArn"))

    @ecs_cluster_arn.setter
    def ecs_cluster_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "ecsClusterArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="elasticIps")
    def elastic_ips(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStack.ElasticIpProperty"]]]]:
        '''``AWS::OpsWorks::Stack.ElasticIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-elasticips
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStack.ElasticIpProperty"]]]], jsii.get(self, "elasticIps"))

    @elastic_ips.setter
    def elastic_ips(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStack.ElasticIpProperty"]]]],
    ) -> None:
        jsii.set(self, "elasticIps", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="hostnameTheme")
    def hostname_theme(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.HostnameTheme``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-hostnametheme
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameTheme"))

    @hostname_theme.setter
    def hostname_theme(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "hostnameTheme", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="rdsDbInstances")
    def rds_db_instances(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStack.RdsDbInstanceProperty"]]]]:
        '''``AWS::OpsWorks::Stack.RdsDbInstances``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-rdsdbinstances
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStack.RdsDbInstanceProperty"]]]], jsii.get(self, "rdsDbInstances"))

    @rds_db_instances.setter
    def rds_db_instances(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnStack.RdsDbInstanceProperty"]]]],
    ) -> None:
        jsii.set(self, "rdsDbInstances", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceStackId")
    def source_stack_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.SourceStackId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-sourcestackid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceStackId"))

    @source_stack_id.setter
    def source_stack_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sourceStackId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="useCustomCookbooks")
    def use_custom_cookbooks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Stack.UseCustomCookbooks``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#usecustcookbooks
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "useCustomCookbooks"))

    @use_custom_cookbooks.setter
    def use_custom_cookbooks(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "useCustomCookbooks", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="useOpsworksSecurityGroups")
    def use_opsworks_security_groups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Stack.UseOpsworksSecurityGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-useopsworkssecuritygroups
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "useOpsworksSecurityGroups"))

    @use_opsworks_security_groups.setter
    def use_opsworks_security_groups(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "useOpsworksSecurityGroups", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-vpcid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "vpcId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnStack.ChefConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "berkshelf_version": "berkshelfVersion",
            "manage_berkshelf": "manageBerkshelf",
        },
    )
    class ChefConfigurationProperty:
        def __init__(
            self,
            *,
            berkshelf_version: typing.Optional[builtins.str] = None,
            manage_berkshelf: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param berkshelf_version: ``CfnStack.ChefConfigurationProperty.BerkshelfVersion``.
            :param manage_berkshelf: ``CfnStack.ChefConfigurationProperty.ManageBerkshelf``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if berkshelf_version is not None:
                self._values["berkshelf_version"] = berkshelf_version
            if manage_berkshelf is not None:
                self._values["manage_berkshelf"] = manage_berkshelf

        @builtins.property
        def berkshelf_version(self) -> typing.Optional[builtins.str]:
            '''``CfnStack.ChefConfigurationProperty.BerkshelfVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html#cfn-opsworks-chefconfiguration-berkshelfversion
            '''
            result = self._values.get("berkshelf_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manage_berkshelf(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnStack.ChefConfigurationProperty.ManageBerkshelf``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-chefconfiguration.html#cfn-opsworks-chefconfiguration-berkshelfversion
            '''
            result = self._values.get("manage_berkshelf")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChefConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnStack.ElasticIpProperty",
        jsii_struct_bases=[],
        name_mapping={"ip": "ip", "name": "name"},
    )
    class ElasticIpProperty:
        def __init__(
            self,
            *,
            ip: builtins.str,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param ip: ``CfnStack.ElasticIpProperty.Ip``.
            :param name: ``CfnStack.ElasticIpProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "ip": ip,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def ip(self) -> builtins.str:
            '''``CfnStack.ElasticIpProperty.Ip``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html#cfn-opsworks-stack-elasticip-ip
            '''
            result = self._values.get("ip")
            assert result is not None, "Required property 'ip' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnStack.ElasticIpProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-elasticip.html#cfn-opsworks-stack-elasticip-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticIpProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnStack.RdsDbInstanceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "db_password": "dbPassword",
            "db_user": "dbUser",
            "rds_db_instance_arn": "rdsDbInstanceArn",
        },
    )
    class RdsDbInstanceProperty:
        def __init__(
            self,
            *,
            db_password: builtins.str,
            db_user: builtins.str,
            rds_db_instance_arn: builtins.str,
        ) -> None:
            '''
            :param db_password: ``CfnStack.RdsDbInstanceProperty.DbPassword``.
            :param db_user: ``CfnStack.RdsDbInstanceProperty.DbUser``.
            :param rds_db_instance_arn: ``CfnStack.RdsDbInstanceProperty.RdsDbInstanceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "db_password": db_password,
                "db_user": db_user,
                "rds_db_instance_arn": rds_db_instance_arn,
            }

        @builtins.property
        def db_password(self) -> builtins.str:
            '''``CfnStack.RdsDbInstanceProperty.DbPassword``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-dbpassword
            '''
            result = self._values.get("db_password")
            assert result is not None, "Required property 'db_password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def db_user(self) -> builtins.str:
            '''``CfnStack.RdsDbInstanceProperty.DbUser``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-dbuser
            '''
            result = self._values.get("db_user")
            assert result is not None, "Required property 'db_user' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rds_db_instance_arn(self) -> builtins.str:
            '''``CfnStack.RdsDbInstanceProperty.RdsDbInstanceArn``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-rdsdbinstance.html#cfn-opsworks-stack-rdsdbinstance-rdsdbinstancearn
            '''
            result = self._values.get("rds_db_instance_arn")
            assert result is not None, "Required property 'rds_db_instance_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RdsDbInstanceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnStack.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "password": "password",
            "revision": "revision",
            "ssh_key": "sshKey",
            "type": "type",
            "url": "url",
            "username": "username",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            password: typing.Optional[builtins.str] = None,
            revision: typing.Optional[builtins.str] = None,
            ssh_key: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param password: ``CfnStack.SourceProperty.Password``.
            :param revision: ``CfnStack.SourceProperty.Revision``.
            :param ssh_key: ``CfnStack.SourceProperty.SshKey``.
            :param type: ``CfnStack.SourceProperty.Type``.
            :param url: ``CfnStack.SourceProperty.Url``.
            :param username: ``CfnStack.SourceProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if password is not None:
                self._values["password"] = password
            if revision is not None:
                self._values["revision"] = revision
            if ssh_key is not None:
                self._values["ssh_key"] = ssh_key
            if type is not None:
                self._values["type"] = type
            if url is not None:
                self._values["url"] = url
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''``CfnStack.SourceProperty.Password``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def revision(self) -> typing.Optional[builtins.str]:
            '''``CfnStack.SourceProperty.Revision``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-revision
            '''
            result = self._values.get("revision")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssh_key(self) -> typing.Optional[builtins.str]:
            '''``CfnStack.SourceProperty.SshKey``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-sshkey
            '''
            result = self._values.get("ssh_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnStack.SourceProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnStack.SourceProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''``CfnStack.SourceProperty.Username``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-source.html#cfn-opsworks-custcookbooksource-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-opsworks.CfnStack.StackConfigurationManagerProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "version": "version"},
    )
    class StackConfigurationManagerProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: ``CfnStack.StackConfigurationManagerProperty.Name``.
            :param version: ``CfnStack.StackConfigurationManagerProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''``CfnStack.StackConfigurationManagerProperty.Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html#cfn-opsworks-configmanager-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''``CfnStack.StackConfigurationManagerProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-opsworks-stack-stackconfigmanager.html#cfn-opsworks-configmanager-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StackConfigurationManagerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-opsworks.CfnStackProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_instance_profile_arn": "defaultInstanceProfileArn",
        "name": "name",
        "service_role_arn": "serviceRoleArn",
        "agent_version": "agentVersion",
        "attributes": "attributes",
        "chef_configuration": "chefConfiguration",
        "clone_app_ids": "cloneAppIds",
        "clone_permissions": "clonePermissions",
        "configuration_manager": "configurationManager",
        "custom_cookbooks_source": "customCookbooksSource",
        "custom_json": "customJson",
        "default_availability_zone": "defaultAvailabilityZone",
        "default_os": "defaultOs",
        "default_root_device_type": "defaultRootDeviceType",
        "default_ssh_key_name": "defaultSshKeyName",
        "default_subnet_id": "defaultSubnetId",
        "ecs_cluster_arn": "ecsClusterArn",
        "elastic_ips": "elasticIps",
        "hostname_theme": "hostnameTheme",
        "rds_db_instances": "rdsDbInstances",
        "source_stack_id": "sourceStackId",
        "tags": "tags",
        "use_custom_cookbooks": "useCustomCookbooks",
        "use_opsworks_security_groups": "useOpsworksSecurityGroups",
        "vpc_id": "vpcId",
    },
)
class CfnStackProps:
    def __init__(
        self,
        *,
        default_instance_profile_arn: builtins.str,
        name: builtins.str,
        service_role_arn: builtins.str,
        agent_version: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        chef_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStack.ChefConfigurationProperty]] = None,
        clone_app_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        clone_permissions: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        configuration_manager: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStack.StackConfigurationManagerProperty]] = None,
        custom_cookbooks_source: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStack.SourceProperty]] = None,
        custom_json: typing.Any = None,
        default_availability_zone: typing.Optional[builtins.str] = None,
        default_os: typing.Optional[builtins.str] = None,
        default_root_device_type: typing.Optional[builtins.str] = None,
        default_ssh_key_name: typing.Optional[builtins.str] = None,
        default_subnet_id: typing.Optional[builtins.str] = None,
        ecs_cluster_arn: typing.Optional[builtins.str] = None,
        elastic_ips: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnStack.ElasticIpProperty]]]] = None,
        hostname_theme: typing.Optional[builtins.str] = None,
        rds_db_instances: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnStack.RdsDbInstanceProperty]]]] = None,
        source_stack_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
        use_custom_cookbooks: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        use_opsworks_security_groups: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::OpsWorks::Stack``.

        :param default_instance_profile_arn: ``AWS::OpsWorks::Stack.DefaultInstanceProfileArn``.
        :param name: ``AWS::OpsWorks::Stack.Name``.
        :param service_role_arn: ``AWS::OpsWorks::Stack.ServiceRoleArn``.
        :param agent_version: ``AWS::OpsWorks::Stack.AgentVersion``.
        :param attributes: ``AWS::OpsWorks::Stack.Attributes``.
        :param chef_configuration: ``AWS::OpsWorks::Stack.ChefConfiguration``.
        :param clone_app_ids: ``AWS::OpsWorks::Stack.CloneAppIds``.
        :param clone_permissions: ``AWS::OpsWorks::Stack.ClonePermissions``.
        :param configuration_manager: ``AWS::OpsWorks::Stack.ConfigurationManager``.
        :param custom_cookbooks_source: ``AWS::OpsWorks::Stack.CustomCookbooksSource``.
        :param custom_json: ``AWS::OpsWorks::Stack.CustomJson``.
        :param default_availability_zone: ``AWS::OpsWorks::Stack.DefaultAvailabilityZone``.
        :param default_os: ``AWS::OpsWorks::Stack.DefaultOs``.
        :param default_root_device_type: ``AWS::OpsWorks::Stack.DefaultRootDeviceType``.
        :param default_ssh_key_name: ``AWS::OpsWorks::Stack.DefaultSshKeyName``.
        :param default_subnet_id: ``AWS::OpsWorks::Stack.DefaultSubnetId``.
        :param ecs_cluster_arn: ``AWS::OpsWorks::Stack.EcsClusterArn``.
        :param elastic_ips: ``AWS::OpsWorks::Stack.ElasticIps``.
        :param hostname_theme: ``AWS::OpsWorks::Stack.HostnameTheme``.
        :param rds_db_instances: ``AWS::OpsWorks::Stack.RdsDbInstances``.
        :param source_stack_id: ``AWS::OpsWorks::Stack.SourceStackId``.
        :param tags: ``AWS::OpsWorks::Stack.Tags``.
        :param use_custom_cookbooks: ``AWS::OpsWorks::Stack.UseCustomCookbooks``.
        :param use_opsworks_security_groups: ``AWS::OpsWorks::Stack.UseOpsworksSecurityGroups``.
        :param vpc_id: ``AWS::OpsWorks::Stack.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "default_instance_profile_arn": default_instance_profile_arn,
            "name": name,
            "service_role_arn": service_role_arn,
        }
        if agent_version is not None:
            self._values["agent_version"] = agent_version
        if attributes is not None:
            self._values["attributes"] = attributes
        if chef_configuration is not None:
            self._values["chef_configuration"] = chef_configuration
        if clone_app_ids is not None:
            self._values["clone_app_ids"] = clone_app_ids
        if clone_permissions is not None:
            self._values["clone_permissions"] = clone_permissions
        if configuration_manager is not None:
            self._values["configuration_manager"] = configuration_manager
        if custom_cookbooks_source is not None:
            self._values["custom_cookbooks_source"] = custom_cookbooks_source
        if custom_json is not None:
            self._values["custom_json"] = custom_json
        if default_availability_zone is not None:
            self._values["default_availability_zone"] = default_availability_zone
        if default_os is not None:
            self._values["default_os"] = default_os
        if default_root_device_type is not None:
            self._values["default_root_device_type"] = default_root_device_type
        if default_ssh_key_name is not None:
            self._values["default_ssh_key_name"] = default_ssh_key_name
        if default_subnet_id is not None:
            self._values["default_subnet_id"] = default_subnet_id
        if ecs_cluster_arn is not None:
            self._values["ecs_cluster_arn"] = ecs_cluster_arn
        if elastic_ips is not None:
            self._values["elastic_ips"] = elastic_ips
        if hostname_theme is not None:
            self._values["hostname_theme"] = hostname_theme
        if rds_db_instances is not None:
            self._values["rds_db_instances"] = rds_db_instances
        if source_stack_id is not None:
            self._values["source_stack_id"] = source_stack_id
        if tags is not None:
            self._values["tags"] = tags
        if use_custom_cookbooks is not None:
            self._values["use_custom_cookbooks"] = use_custom_cookbooks
        if use_opsworks_security_groups is not None:
            self._values["use_opsworks_security_groups"] = use_opsworks_security_groups
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def default_instance_profile_arn(self) -> builtins.str:
        '''``AWS::OpsWorks::Stack.DefaultInstanceProfileArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultinstanceprof
        '''
        result = self._values.get("default_instance_profile_arn")
        assert result is not None, "Required property 'default_instance_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::OpsWorks::Stack.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role_arn(self) -> builtins.str:
        '''``AWS::OpsWorks::Stack.ServiceRoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-servicerolearn
        '''
        result = self._values.get("service_role_arn")
        assert result is not None, "Required property 'service_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_version(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.AgentVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-agentversion
        '''
        result = self._values.get("agent_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''``AWS::OpsWorks::Stack.Attributes``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def chef_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStack.ChefConfigurationProperty]]:
        '''``AWS::OpsWorks::Stack.ChefConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-chefconfiguration
        '''
        result = self._values.get("chef_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStack.ChefConfigurationProperty]], result)

    @builtins.property
    def clone_app_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''``AWS::OpsWorks::Stack.CloneAppIds``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-cloneappids
        '''
        result = self._values.get("clone_app_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def clone_permissions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Stack.ClonePermissions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-clonepermissions
        '''
        result = self._values.get("clone_permissions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def configuration_manager(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStack.StackConfigurationManagerProperty]]:
        '''``AWS::OpsWorks::Stack.ConfigurationManager``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-configmanager
        '''
        result = self._values.get("configuration_manager")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStack.StackConfigurationManagerProperty]], result)

    @builtins.property
    def custom_cookbooks_source(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStack.SourceProperty]]:
        '''``AWS::OpsWorks::Stack.CustomCookbooksSource``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-custcookbooksource
        '''
        result = self._values.get("custom_cookbooks_source")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnStack.SourceProperty]], result)

    @builtins.property
    def custom_json(self) -> typing.Any:
        '''``AWS::OpsWorks::Stack.CustomJson``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-custjson
        '''
        result = self._values.get("custom_json")
        return typing.cast(typing.Any, result)

    @builtins.property
    def default_availability_zone(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.DefaultAvailabilityZone``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultaz
        '''
        result = self._values.get("default_availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_os(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.DefaultOs``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultos
        '''
        result = self._values.get("default_os")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_root_device_type(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.DefaultRootDeviceType``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultrootdevicetype
        '''
        result = self._values.get("default_root_device_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_ssh_key_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.DefaultSshKeyName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-defaultsshkeyname
        '''
        result = self._values.get("default_ssh_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_subnet_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.DefaultSubnetId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#defaultsubnet
        '''
        result = self._values.get("default_subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ecs_cluster_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.EcsClusterArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-ecsclusterarn
        '''
        result = self._values.get("ecs_cluster_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elastic_ips(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnStack.ElasticIpProperty]]]]:
        '''``AWS::OpsWorks::Stack.ElasticIps``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-elasticips
        '''
        result = self._values.get("elastic_ips")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnStack.ElasticIpProperty]]]], result)

    @builtins.property
    def hostname_theme(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.HostnameTheme``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-hostnametheme
        '''
        result = self._values.get("hostname_theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rds_db_instances(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnStack.RdsDbInstanceProperty]]]]:
        '''``AWS::OpsWorks::Stack.RdsDbInstances``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-rdsdbinstances
        '''
        result = self._values.get("rds_db_instances")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnStack.RdsDbInstanceProperty]]]], result)

    @builtins.property
    def source_stack_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.SourceStackId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-sourcestackid
        '''
        result = self._values.get("source_stack_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::OpsWorks::Stack.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    @builtins.property
    def use_custom_cookbooks(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Stack.UseCustomCookbooks``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#usecustcookbooks
        '''
        result = self._values.get("use_custom_cookbooks")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def use_opsworks_security_groups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::Stack.UseOpsworksSecurityGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-useopsworkssecuritygroups
        '''
        result = self._values.get("use_opsworks_security_groups")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Stack.VpcId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html#cfn-opsworks-stack-vpcid
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnUserProfile(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-opsworks.CfnUserProfile",
):
    '''A CloudFormation ``AWS::OpsWorks::UserProfile``.

    :cloudformationResource: AWS::OpsWorks::UserProfile
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        iam_user_arn: builtins.str,
        allow_self_management: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ssh_public_key: typing.Optional[builtins.str] = None,
        ssh_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::OpsWorks::UserProfile``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param iam_user_arn: ``AWS::OpsWorks::UserProfile.IamUserArn``.
        :param allow_self_management: ``AWS::OpsWorks::UserProfile.AllowSelfManagement``.
        :param ssh_public_key: ``AWS::OpsWorks::UserProfile.SshPublicKey``.
        :param ssh_username: ``AWS::OpsWorks::UserProfile.SshUsername``.
        '''
        props = CfnUserProfileProps(
            iam_user_arn=iam_user_arn,
            allow_self_management=allow_self_management,
            ssh_public_key=ssh_public_key,
            ssh_username=ssh_username,
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
    @jsii.member(jsii_name="attrSshUsername")
    def attr_ssh_username(self) -> builtins.str:
        '''
        :cloudformationAttribute: SshUsername
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSshUsername"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="iamUserArn")
    def iam_user_arn(self) -> builtins.str:
        '''``AWS::OpsWorks::UserProfile.IamUserArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-iamuserarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "iamUserArn"))

    @iam_user_arn.setter
    def iam_user_arn(self, value: builtins.str) -> None:
        jsii.set(self, "iamUserArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="allowSelfManagement")
    def allow_self_management(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::UserProfile.AllowSelfManagement``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-allowselfmanagement
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "allowSelfManagement"))

    @allow_self_management.setter
    def allow_self_management(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "allowSelfManagement", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sshPublicKey")
    def ssh_public_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::UserProfile.SshPublicKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshpublickey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshPublicKey"))

    @ssh_public_key.setter
    def ssh_public_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sshPublicKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sshUsername")
    def ssh_username(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::UserProfile.SshUsername``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshusername
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshUsername"))

    @ssh_username.setter
    def ssh_username(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sshUsername", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-opsworks.CfnUserProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "iam_user_arn": "iamUserArn",
        "allow_self_management": "allowSelfManagement",
        "ssh_public_key": "sshPublicKey",
        "ssh_username": "sshUsername",
    },
)
class CfnUserProfileProps:
    def __init__(
        self,
        *,
        iam_user_arn: builtins.str,
        allow_self_management: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ssh_public_key: typing.Optional[builtins.str] = None,
        ssh_username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::OpsWorks::UserProfile``.

        :param iam_user_arn: ``AWS::OpsWorks::UserProfile.IamUserArn``.
        :param allow_self_management: ``AWS::OpsWorks::UserProfile.AllowSelfManagement``.
        :param ssh_public_key: ``AWS::OpsWorks::UserProfile.SshPublicKey``.
        :param ssh_username: ``AWS::OpsWorks::UserProfile.SshUsername``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "iam_user_arn": iam_user_arn,
        }
        if allow_self_management is not None:
            self._values["allow_self_management"] = allow_self_management
        if ssh_public_key is not None:
            self._values["ssh_public_key"] = ssh_public_key
        if ssh_username is not None:
            self._values["ssh_username"] = ssh_username

    @builtins.property
    def iam_user_arn(self) -> builtins.str:
        '''``AWS::OpsWorks::UserProfile.IamUserArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-iamuserarn
        '''
        result = self._values.get("iam_user_arn")
        assert result is not None, "Required property 'iam_user_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_self_management(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::OpsWorks::UserProfile.AllowSelfManagement``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-allowselfmanagement
        '''
        result = self._values.get("allow_self_management")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def ssh_public_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::UserProfile.SshPublicKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshpublickey
        '''
        result = self._values.get("ssh_public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssh_username(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::UserProfile.SshUsername``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html#cfn-opsworks-userprofile-sshusername
        '''
        result = self._values.get("ssh_username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnVolume(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-opsworks.CfnVolume",
):
    '''A CloudFormation ``AWS::OpsWorks::Volume``.

    :cloudformationResource: AWS::OpsWorks::Volume
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        ec2_volume_id: builtins.str,
        stack_id: builtins.str,
        mount_point: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::OpsWorks::Volume``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param ec2_volume_id: ``AWS::OpsWorks::Volume.Ec2VolumeId``.
        :param stack_id: ``AWS::OpsWorks::Volume.StackId``.
        :param mount_point: ``AWS::OpsWorks::Volume.MountPoint``.
        :param name: ``AWS::OpsWorks::Volume.Name``.
        '''
        props = CfnVolumeProps(
            ec2_volume_id=ec2_volume_id,
            stack_id=stack_id,
            mount_point=mount_point,
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
    @jsii.member(jsii_name="ec2VolumeId")
    def ec2_volume_id(self) -> builtins.str:
        '''``AWS::OpsWorks::Volume.Ec2VolumeId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-ec2volumeid
        '''
        return typing.cast(builtins.str, jsii.get(self, "ec2VolumeId"))

    @ec2_volume_id.setter
    def ec2_volume_id(self, value: builtins.str) -> None:
        jsii.set(self, "ec2VolumeId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> builtins.str:
        '''``AWS::OpsWorks::Volume.StackId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-stackid
        '''
        return typing.cast(builtins.str, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: builtins.str) -> None:
        jsii.set(self, "stackId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="mountPoint")
    def mount_point(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Volume.MountPoint``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-mountpoint
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountPoint"))

    @mount_point.setter
    def mount_point(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "mountPoint", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Volume.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-name
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-opsworks.CfnVolumeProps",
    jsii_struct_bases=[],
    name_mapping={
        "ec2_volume_id": "ec2VolumeId",
        "stack_id": "stackId",
        "mount_point": "mountPoint",
        "name": "name",
    },
)
class CfnVolumeProps:
    def __init__(
        self,
        *,
        ec2_volume_id: builtins.str,
        stack_id: builtins.str,
        mount_point: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::OpsWorks::Volume``.

        :param ec2_volume_id: ``AWS::OpsWorks::Volume.Ec2VolumeId``.
        :param stack_id: ``AWS::OpsWorks::Volume.StackId``.
        :param mount_point: ``AWS::OpsWorks::Volume.MountPoint``.
        :param name: ``AWS::OpsWorks::Volume.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "ec2_volume_id": ec2_volume_id,
            "stack_id": stack_id,
        }
        if mount_point is not None:
            self._values["mount_point"] = mount_point
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def ec2_volume_id(self) -> builtins.str:
        '''``AWS::OpsWorks::Volume.Ec2VolumeId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-ec2volumeid
        '''
        result = self._values.get("ec2_volume_id")
        assert result is not None, "Required property 'ec2_volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''``AWS::OpsWorks::Volume.StackId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-stackid
        '''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_point(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Volume.MountPoint``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-mountpoint
        '''
        result = self._values.get("mount_point")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''``AWS::OpsWorks::Volume.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html#cfn-opsworks-volume-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVolumeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApp",
    "CfnAppProps",
    "CfnElasticLoadBalancerAttachment",
    "CfnElasticLoadBalancerAttachmentProps",
    "CfnInstance",
    "CfnInstanceProps",
    "CfnLayer",
    "CfnLayerProps",
    "CfnStack",
    "CfnStackProps",
    "CfnUserProfile",
    "CfnUserProfileProps",
    "CfnVolume",
    "CfnVolumeProps",
]

publication.publish()
