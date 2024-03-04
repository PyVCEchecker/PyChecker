'''
# Amazon Pinpoint Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_pinpoint as pinpoint
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
class CfnADMChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnADMChannel",
):
    '''A CloudFormation ``AWS::Pinpoint::ADMChannel``.

    :cloudformationResource: AWS::Pinpoint::ADMChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        client_id: builtins.str,
        client_secret: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::ADMChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::ADMChannel.ApplicationId``.
        :param client_id: ``AWS::Pinpoint::ADMChannel.ClientId``.
        :param client_secret: ``AWS::Pinpoint::ADMChannel.ClientSecret``.
        :param enabled: ``AWS::Pinpoint::ADMChannel.Enabled``.
        '''
        props = CfnADMChannelProps(
            application_id=application_id,
            client_id=client_id,
            client_secret=client_secret,
            enabled=enabled,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::ADMChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        '''``AWS::Pinpoint::ADMChannel.ClientId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientid
        '''
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        jsii.set(self, "clientId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        '''``AWS::Pinpoint::ADMChannel.ClientSecret``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientsecret
        '''
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        jsii.set(self, "clientSecret", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::ADMChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enabled", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnADMChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "enabled": "enabled",
    },
)
class CfnADMChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        client_id: builtins.str,
        client_secret: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::ADMChannel``.

        :param application_id: ``AWS::Pinpoint::ADMChannel.ApplicationId``.
        :param client_id: ``AWS::Pinpoint::ADMChannel.ClientId``.
        :param client_secret: ``AWS::Pinpoint::ADMChannel.ClientSecret``.
        :param enabled: ``AWS::Pinpoint::ADMChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "client_id": client_id,
            "client_secret": client_secret,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::ADMChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_id(self) -> builtins.str:
        '''``AWS::Pinpoint::ADMChannel.ClientId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientid
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''``AWS::Pinpoint::ADMChannel.ClientSecret``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-clientsecret
        '''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::ADMChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html#cfn-pinpoint-admchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnADMChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAPNSChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnAPNSChannel",
):
    '''A CloudFormation ``AWS::Pinpoint::APNSChannel``.

    :cloudformationResource: AWS::Pinpoint::APNSChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::APNSChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::APNSChannel.ApplicationId``.
        :param bundle_id: ``AWS::Pinpoint::APNSChannel.BundleId``.
        :param certificate: ``AWS::Pinpoint::APNSChannel.Certificate``.
        :param default_authentication_method: ``AWS::Pinpoint::APNSChannel.DefaultAuthenticationMethod``.
        :param enabled: ``AWS::Pinpoint::APNSChannel.Enabled``.
        :param private_key: ``AWS::Pinpoint::APNSChannel.PrivateKey``.
        :param team_id: ``AWS::Pinpoint::APNSChannel.TeamId``.
        :param token_key: ``AWS::Pinpoint::APNSChannel.TokenKey``.
        :param token_key_id: ``AWS::Pinpoint::APNSChannel.TokenKeyId``.
        '''
        props = CfnAPNSChannelProps(
            application_id=application_id,
            bundle_id=bundle_id,
            certificate=certificate,
            default_authentication_method=default_authentication_method,
            enabled=enabled,
            private_key=private_key,
            team_id=team_id,
            token_key=token_key,
            token_key_id=token_key_id,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::APNSChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-bundleid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bundleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-certificate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "certificate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.DefaultAuthenticationMethod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-defaultauthenticationmethod
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAuthenticationMethod"))

    @default_authentication_method.setter
    def default_authentication_method(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "defaultAuthenticationMethod", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::APNSChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.PrivateKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-privatekey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "privateKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.TeamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-teamid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "teamId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tokenKey")
    def token_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.TokenKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKey"))

    @token_key.setter
    def token_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tokenKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tokenKeyId")
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKeyId"))

    @token_key_id.setter
    def token_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tokenKeyId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnAPNSChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "bundle_id": "bundleId",
        "certificate": "certificate",
        "default_authentication_method": "defaultAuthenticationMethod",
        "enabled": "enabled",
        "private_key": "privateKey",
        "team_id": "teamId",
        "token_key": "tokenKey",
        "token_key_id": "tokenKeyId",
    },
)
class CfnAPNSChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::APNSChannel``.

        :param application_id: ``AWS::Pinpoint::APNSChannel.ApplicationId``.
        :param bundle_id: ``AWS::Pinpoint::APNSChannel.BundleId``.
        :param certificate: ``AWS::Pinpoint::APNSChannel.Certificate``.
        :param default_authentication_method: ``AWS::Pinpoint::APNSChannel.DefaultAuthenticationMethod``.
        :param enabled: ``AWS::Pinpoint::APNSChannel.Enabled``.
        :param private_key: ``AWS::Pinpoint::APNSChannel.PrivateKey``.
        :param team_id: ``AWS::Pinpoint::APNSChannel.TeamId``.
        :param token_key: ``AWS::Pinpoint::APNSChannel.TokenKey``.
        :param token_key_id: ``AWS::Pinpoint::APNSChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
        }
        if bundle_id is not None:
            self._values["bundle_id"] = bundle_id
        if certificate is not None:
            self._values["certificate"] = certificate
        if default_authentication_method is not None:
            self._values["default_authentication_method"] = default_authentication_method
        if enabled is not None:
            self._values["enabled"] = enabled
        if private_key is not None:
            self._values["private_key"] = private_key
        if team_id is not None:
            self._values["team_id"] = team_id
        if token_key is not None:
            self._values["token_key"] = token_key
        if token_key_id is not None:
            self._values["token_key_id"] = token_key_id

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::APNSChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-bundleid
        '''
        result = self._values.get("bundle_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.DefaultAuthenticationMethod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-defaultauthenticationmethod
        '''
        result = self._values.get("default_authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::APNSChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.PrivateKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-privatekey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.TeamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-teamid
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.TokenKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkey
        '''
        result = self._values.get("token_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html#cfn-pinpoint-apnschannel-tokenkeyid
        '''
        result = self._values.get("token_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAPNSChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAPNSSandboxChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnAPNSSandboxChannel",
):
    '''A CloudFormation ``AWS::Pinpoint::APNSSandboxChannel``.

    :cloudformationResource: AWS::Pinpoint::APNSSandboxChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::APNSSandboxChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::APNSSandboxChannel.ApplicationId``.
        :param bundle_id: ``AWS::Pinpoint::APNSSandboxChannel.BundleId``.
        :param certificate: ``AWS::Pinpoint::APNSSandboxChannel.Certificate``.
        :param default_authentication_method: ``AWS::Pinpoint::APNSSandboxChannel.DefaultAuthenticationMethod``.
        :param enabled: ``AWS::Pinpoint::APNSSandboxChannel.Enabled``.
        :param private_key: ``AWS::Pinpoint::APNSSandboxChannel.PrivateKey``.
        :param team_id: ``AWS::Pinpoint::APNSSandboxChannel.TeamId``.
        :param token_key: ``AWS::Pinpoint::APNSSandboxChannel.TokenKey``.
        :param token_key_id: ``AWS::Pinpoint::APNSSandboxChannel.TokenKeyId``.
        '''
        props = CfnAPNSSandboxChannelProps(
            application_id=application_id,
            bundle_id=bundle_id,
            certificate=certificate,
            default_authentication_method=default_authentication_method,
            enabled=enabled,
            private_key=private_key,
            team_id=team_id,
            token_key=token_key,
            token_key_id=token_key_id,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::APNSSandboxChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-bundleid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bundleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-certificate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "certificate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.DefaultAuthenticationMethod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-defaultauthenticationmethod
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAuthenticationMethod"))

    @default_authentication_method.setter
    def default_authentication_method(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "defaultAuthenticationMethod", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::APNSSandboxChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.PrivateKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-privatekey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "privateKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.TeamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-teamid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "teamId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tokenKey")
    def token_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.TokenKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKey"))

    @token_key.setter
    def token_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tokenKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tokenKeyId")
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKeyId"))

    @token_key_id.setter
    def token_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tokenKeyId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnAPNSSandboxChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "bundle_id": "bundleId",
        "certificate": "certificate",
        "default_authentication_method": "defaultAuthenticationMethod",
        "enabled": "enabled",
        "private_key": "privateKey",
        "team_id": "teamId",
        "token_key": "tokenKey",
        "token_key_id": "tokenKeyId",
    },
)
class CfnAPNSSandboxChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::APNSSandboxChannel``.

        :param application_id: ``AWS::Pinpoint::APNSSandboxChannel.ApplicationId``.
        :param bundle_id: ``AWS::Pinpoint::APNSSandboxChannel.BundleId``.
        :param certificate: ``AWS::Pinpoint::APNSSandboxChannel.Certificate``.
        :param default_authentication_method: ``AWS::Pinpoint::APNSSandboxChannel.DefaultAuthenticationMethod``.
        :param enabled: ``AWS::Pinpoint::APNSSandboxChannel.Enabled``.
        :param private_key: ``AWS::Pinpoint::APNSSandboxChannel.PrivateKey``.
        :param team_id: ``AWS::Pinpoint::APNSSandboxChannel.TeamId``.
        :param token_key: ``AWS::Pinpoint::APNSSandboxChannel.TokenKey``.
        :param token_key_id: ``AWS::Pinpoint::APNSSandboxChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
        }
        if bundle_id is not None:
            self._values["bundle_id"] = bundle_id
        if certificate is not None:
            self._values["certificate"] = certificate
        if default_authentication_method is not None:
            self._values["default_authentication_method"] = default_authentication_method
        if enabled is not None:
            self._values["enabled"] = enabled
        if private_key is not None:
            self._values["private_key"] = private_key
        if team_id is not None:
            self._values["team_id"] = team_id
        if token_key is not None:
            self._values["token_key"] = token_key
        if token_key_id is not None:
            self._values["token_key_id"] = token_key_id

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::APNSSandboxChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-bundleid
        '''
        result = self._values.get("bundle_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.DefaultAuthenticationMethod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-defaultauthenticationmethod
        '''
        result = self._values.get("default_authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::APNSSandboxChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.PrivateKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-privatekey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.TeamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-teamid
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.TokenKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkey
        '''
        result = self._values.get("token_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSSandboxChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html#cfn-pinpoint-apnssandboxchannel-tokenkeyid
        '''
        result = self._values.get("token_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAPNSSandboxChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAPNSVoipChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnAPNSVoipChannel",
):
    '''A CloudFormation ``AWS::Pinpoint::APNSVoipChannel``.

    :cloudformationResource: AWS::Pinpoint::APNSVoipChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::APNSVoipChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::APNSVoipChannel.ApplicationId``.
        :param bundle_id: ``AWS::Pinpoint::APNSVoipChannel.BundleId``.
        :param certificate: ``AWS::Pinpoint::APNSVoipChannel.Certificate``.
        :param default_authentication_method: ``AWS::Pinpoint::APNSVoipChannel.DefaultAuthenticationMethod``.
        :param enabled: ``AWS::Pinpoint::APNSVoipChannel.Enabled``.
        :param private_key: ``AWS::Pinpoint::APNSVoipChannel.PrivateKey``.
        :param team_id: ``AWS::Pinpoint::APNSVoipChannel.TeamId``.
        :param token_key: ``AWS::Pinpoint::APNSVoipChannel.TokenKey``.
        :param token_key_id: ``AWS::Pinpoint::APNSVoipChannel.TokenKeyId``.
        '''
        props = CfnAPNSVoipChannelProps(
            application_id=application_id,
            bundle_id=bundle_id,
            certificate=certificate,
            default_authentication_method=default_authentication_method,
            enabled=enabled,
            private_key=private_key,
            team_id=team_id,
            token_key=token_key,
            token_key_id=token_key_id,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::APNSVoipChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-bundleid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bundleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-certificate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "certificate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.DefaultAuthenticationMethod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-defaultauthenticationmethod
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAuthenticationMethod"))

    @default_authentication_method.setter
    def default_authentication_method(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "defaultAuthenticationMethod", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::APNSVoipChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.PrivateKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-privatekey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "privateKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.TeamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-teamid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "teamId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tokenKey")
    def token_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.TokenKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKey"))

    @token_key.setter
    def token_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tokenKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tokenKeyId")
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKeyId"))

    @token_key_id.setter
    def token_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tokenKeyId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnAPNSVoipChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "bundle_id": "bundleId",
        "certificate": "certificate",
        "default_authentication_method": "defaultAuthenticationMethod",
        "enabled": "enabled",
        "private_key": "privateKey",
        "team_id": "teamId",
        "token_key": "tokenKey",
        "token_key_id": "tokenKeyId",
    },
)
class CfnAPNSVoipChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::APNSVoipChannel``.

        :param application_id: ``AWS::Pinpoint::APNSVoipChannel.ApplicationId``.
        :param bundle_id: ``AWS::Pinpoint::APNSVoipChannel.BundleId``.
        :param certificate: ``AWS::Pinpoint::APNSVoipChannel.Certificate``.
        :param default_authentication_method: ``AWS::Pinpoint::APNSVoipChannel.DefaultAuthenticationMethod``.
        :param enabled: ``AWS::Pinpoint::APNSVoipChannel.Enabled``.
        :param private_key: ``AWS::Pinpoint::APNSVoipChannel.PrivateKey``.
        :param team_id: ``AWS::Pinpoint::APNSVoipChannel.TeamId``.
        :param token_key: ``AWS::Pinpoint::APNSVoipChannel.TokenKey``.
        :param token_key_id: ``AWS::Pinpoint::APNSVoipChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
        }
        if bundle_id is not None:
            self._values["bundle_id"] = bundle_id
        if certificate is not None:
            self._values["certificate"] = certificate
        if default_authentication_method is not None:
            self._values["default_authentication_method"] = default_authentication_method
        if enabled is not None:
            self._values["enabled"] = enabled
        if private_key is not None:
            self._values["private_key"] = private_key
        if team_id is not None:
            self._values["team_id"] = team_id
        if token_key is not None:
            self._values["token_key"] = token_key
        if token_key_id is not None:
            self._values["token_key_id"] = token_key_id

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::APNSVoipChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-bundleid
        '''
        result = self._values.get("bundle_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.DefaultAuthenticationMethod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-defaultauthenticationmethod
        '''
        result = self._values.get("default_authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::APNSVoipChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.PrivateKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-privatekey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.TeamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-teamid
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.TokenKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkey
        '''
        result = self._values.get("token_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html#cfn-pinpoint-apnsvoipchannel-tokenkeyid
        '''
        result = self._values.get("token_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAPNSVoipChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnAPNSVoipSandboxChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnAPNSVoipSandboxChannel",
):
    '''A CloudFormation ``AWS::Pinpoint::APNSVoipSandboxChannel``.

    :cloudformationResource: AWS::Pinpoint::APNSVoipSandboxChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::APNSVoipSandboxChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::APNSVoipSandboxChannel.ApplicationId``.
        :param bundle_id: ``AWS::Pinpoint::APNSVoipSandboxChannel.BundleId``.
        :param certificate: ``AWS::Pinpoint::APNSVoipSandboxChannel.Certificate``.
        :param default_authentication_method: ``AWS::Pinpoint::APNSVoipSandboxChannel.DefaultAuthenticationMethod``.
        :param enabled: ``AWS::Pinpoint::APNSVoipSandboxChannel.Enabled``.
        :param private_key: ``AWS::Pinpoint::APNSVoipSandboxChannel.PrivateKey``.
        :param team_id: ``AWS::Pinpoint::APNSVoipSandboxChannel.TeamId``.
        :param token_key: ``AWS::Pinpoint::APNSVoipSandboxChannel.TokenKey``.
        :param token_key_id: ``AWS::Pinpoint::APNSVoipSandboxChannel.TokenKeyId``.
        '''
        props = CfnAPNSVoipSandboxChannelProps(
            application_id=application_id,
            bundle_id=bundle_id,
            certificate=certificate,
            default_authentication_method=default_authentication_method,
            enabled=enabled,
            private_key=private_key,
            team_id=team_id,
            token_key=token_key,
            token_key_id=token_key_id,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="bundleId")
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-bundleid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bundleId"))

    @bundle_id.setter
    def bundle_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "bundleId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-certificate
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "certificate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultAuthenticationMethod")
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.DefaultAuthenticationMethod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-defaultauthenticationmethod
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultAuthenticationMethod"))

    @default_authentication_method.setter
    def default_authentication_method(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "defaultAuthenticationMethod", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.PrivateKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-privatekey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "privateKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.TeamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-teamid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "teamId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tokenKey")
    def token_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.TokenKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkey
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKey"))

    @token_key.setter
    def token_key(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tokenKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tokenKeyId")
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkeyid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenKeyId"))

    @token_key_id.setter
    def token_key_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "tokenKeyId", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnAPNSVoipSandboxChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "bundle_id": "bundleId",
        "certificate": "certificate",
        "default_authentication_method": "defaultAuthenticationMethod",
        "enabled": "enabled",
        "private_key": "privateKey",
        "team_id": "teamId",
        "token_key": "tokenKey",
        "token_key_id": "tokenKeyId",
    },
)
class CfnAPNSVoipSandboxChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        bundle_id: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        default_authentication_method: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        private_key: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        token_key: typing.Optional[builtins.str] = None,
        token_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::APNSVoipSandboxChannel``.

        :param application_id: ``AWS::Pinpoint::APNSVoipSandboxChannel.ApplicationId``.
        :param bundle_id: ``AWS::Pinpoint::APNSVoipSandboxChannel.BundleId``.
        :param certificate: ``AWS::Pinpoint::APNSVoipSandboxChannel.Certificate``.
        :param default_authentication_method: ``AWS::Pinpoint::APNSVoipSandboxChannel.DefaultAuthenticationMethod``.
        :param enabled: ``AWS::Pinpoint::APNSVoipSandboxChannel.Enabled``.
        :param private_key: ``AWS::Pinpoint::APNSVoipSandboxChannel.PrivateKey``.
        :param team_id: ``AWS::Pinpoint::APNSVoipSandboxChannel.TeamId``.
        :param token_key: ``AWS::Pinpoint::APNSVoipSandboxChannel.TokenKey``.
        :param token_key_id: ``AWS::Pinpoint::APNSVoipSandboxChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
        }
        if bundle_id is not None:
            self._values["bundle_id"] = bundle_id
        if certificate is not None:
            self._values["certificate"] = certificate
        if default_authentication_method is not None:
            self._values["default_authentication_method"] = default_authentication_method
        if enabled is not None:
            self._values["enabled"] = enabled
        if private_key is not None:
            self._values["private_key"] = private_key
        if team_id is not None:
            self._values["team_id"] = team_id
        if token_key is not None:
            self._values["token_key"] = token_key
        if token_key_id is not None:
            self._values["token_key_id"] = token_key_id

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bundle_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.BundleId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-bundleid
        '''
        result = self._values.get("bundle_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_authentication_method(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.DefaultAuthenticationMethod``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-defaultauthenticationmethod
        '''
        result = self._values.get("default_authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.PrivateKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-privatekey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.TeamId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-teamid
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.TokenKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkey
        '''
        result = self._values.get("token_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_key_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::APNSVoipSandboxChannel.TokenKeyId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html#cfn-pinpoint-apnsvoipsandboxchannel-tokenkeyid
        '''
        result = self._values.get("token_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAPNSVoipSandboxChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnApp(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnApp",
):
    '''A CloudFormation ``AWS::Pinpoint::App``.

    :cloudformationResource: AWS::Pinpoint::App
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        tags: typing.Any = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::App``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: ``AWS::Pinpoint::App.Name``.
        :param tags: ``AWS::Pinpoint::App.Tags``.
        '''
        props = CfnAppProps(name=name, tags=tags)

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
        '''``AWS::Pinpoint::App.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Pinpoint::App.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnAppProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags"},
)
class CfnAppProps:
    def __init__(self, *, name: builtins.str, tags: typing.Any = None) -> None:
        '''Properties for defining a ``AWS::Pinpoint::App``.

        :param name: ``AWS::Pinpoint::App.Name``.
        :param tags: ``AWS::Pinpoint::App.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Pinpoint::App.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::Pinpoint::App.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html#cfn-pinpoint-app-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnApplicationSettings(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnApplicationSettings",
):
    '''A CloudFormation ``AWS::Pinpoint::ApplicationSettings``.

    :cloudformationResource: AWS::Pinpoint::ApplicationSettings
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        campaign_hook: typing.Optional[typing.Union["CfnApplicationSettings.CampaignHookProperty", aws_cdk.core.IResolvable]] = None,
        cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        limits: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationSettings.LimitsProperty"]] = None,
        quiet_time: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationSettings.QuietTimeProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::ApplicationSettings``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::ApplicationSettings.ApplicationId``.
        :param campaign_hook: ``AWS::Pinpoint::ApplicationSettings.CampaignHook``.
        :param cloud_watch_metrics_enabled: ``AWS::Pinpoint::ApplicationSettings.CloudWatchMetricsEnabled``.
        :param limits: ``AWS::Pinpoint::ApplicationSettings.Limits``.
        :param quiet_time: ``AWS::Pinpoint::ApplicationSettings.QuietTime``.
        '''
        props = CfnApplicationSettingsProps(
            application_id=application_id,
            campaign_hook=campaign_hook,
            cloud_watch_metrics_enabled=cloud_watch_metrics_enabled,
            limits=limits,
            quiet_time=quiet_time,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::ApplicationSettings.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="campaignHook")
    def campaign_hook(
        self,
    ) -> typing.Optional[typing.Union["CfnApplicationSettings.CampaignHookProperty", aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::ApplicationSettings.CampaignHook``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-campaignhook
        '''
        return typing.cast(typing.Optional[typing.Union["CfnApplicationSettings.CampaignHookProperty", aws_cdk.core.IResolvable]], jsii.get(self, "campaignHook"))

    @campaign_hook.setter
    def campaign_hook(
        self,
        value: typing.Optional[typing.Union["CfnApplicationSettings.CampaignHookProperty", aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "campaignHook", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cloudWatchMetricsEnabled")
    def cloud_watch_metrics_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::ApplicationSettings.CloudWatchMetricsEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-cloudwatchmetricsenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "cloudWatchMetricsEnabled"))

    @cloud_watch_metrics_enabled.setter
    def cloud_watch_metrics_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "cloudWatchMetricsEnabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="limits")
    def limits(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationSettings.LimitsProperty"]]:
        '''``AWS::Pinpoint::ApplicationSettings.Limits``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-limits
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationSettings.LimitsProperty"]], jsii.get(self, "limits"))

    @limits.setter
    def limits(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationSettings.LimitsProperty"]],
    ) -> None:
        jsii.set(self, "limits", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="quietTime")
    def quiet_time(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationSettings.QuietTimeProperty"]]:
        '''``AWS::Pinpoint::ApplicationSettings.QuietTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-quiettime
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationSettings.QuietTimeProperty"]], jsii.get(self, "quietTime"))

    @quiet_time.setter
    def quiet_time(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationSettings.QuietTimeProperty"]],
    ) -> None:
        jsii.set(self, "quietTime", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnApplicationSettings.CampaignHookProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_function_name": "lambdaFunctionName",
            "mode": "mode",
            "web_url": "webUrl",
        },
    )
    class CampaignHookProperty:
        def __init__(
            self,
            *,
            lambda_function_name: typing.Optional[builtins.str] = None,
            mode: typing.Optional[builtins.str] = None,
            web_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param lambda_function_name: ``CfnApplicationSettings.CampaignHookProperty.LambdaFunctionName``.
            :param mode: ``CfnApplicationSettings.CampaignHookProperty.Mode``.
            :param web_url: ``CfnApplicationSettings.CampaignHookProperty.WebUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if lambda_function_name is not None:
                self._values["lambda_function_name"] = lambda_function_name
            if mode is not None:
                self._values["mode"] = mode
            if web_url is not None:
                self._values["web_url"] = web_url

        @builtins.property
        def lambda_function_name(self) -> typing.Optional[builtins.str]:
            '''``CfnApplicationSettings.CampaignHookProperty.LambdaFunctionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-lambdafunctionname
            '''
            result = self._values.get("lambda_function_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''``CfnApplicationSettings.CampaignHookProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def web_url(self) -> typing.Optional[builtins.str]:
            '''``CfnApplicationSettings.CampaignHookProperty.WebUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-campaignhook.html#cfn-pinpoint-applicationsettings-campaignhook-weburl
            '''
            result = self._values.get("web_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnApplicationSettings.LimitsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "daily": "daily",
            "maximum_duration": "maximumDuration",
            "messages_per_second": "messagesPerSecond",
            "total": "total",
        },
    )
    class LimitsProperty:
        def __init__(
            self,
            *,
            daily: typing.Optional[jsii.Number] = None,
            maximum_duration: typing.Optional[jsii.Number] = None,
            messages_per_second: typing.Optional[jsii.Number] = None,
            total: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param daily: ``CfnApplicationSettings.LimitsProperty.Daily``.
            :param maximum_duration: ``CfnApplicationSettings.LimitsProperty.MaximumDuration``.
            :param messages_per_second: ``CfnApplicationSettings.LimitsProperty.MessagesPerSecond``.
            :param total: ``CfnApplicationSettings.LimitsProperty.Total``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if daily is not None:
                self._values["daily"] = daily
            if maximum_duration is not None:
                self._values["maximum_duration"] = maximum_duration
            if messages_per_second is not None:
                self._values["messages_per_second"] = messages_per_second
            if total is not None:
                self._values["total"] = total

        @builtins.property
        def daily(self) -> typing.Optional[jsii.Number]:
            '''``CfnApplicationSettings.LimitsProperty.Daily``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-daily
            '''
            result = self._values.get("daily")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_duration(self) -> typing.Optional[jsii.Number]:
            '''``CfnApplicationSettings.LimitsProperty.MaximumDuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-maximumduration
            '''
            result = self._values.get("maximum_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def messages_per_second(self) -> typing.Optional[jsii.Number]:
            '''``CfnApplicationSettings.LimitsProperty.MessagesPerSecond``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-messagespersecond
            '''
            result = self._values.get("messages_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total(self) -> typing.Optional[jsii.Number]:
            '''``CfnApplicationSettings.LimitsProperty.Total``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-limits.html#cfn-pinpoint-applicationsettings-limits-total
            '''
            result = self._values.get("total")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnApplicationSettings.QuietTimeProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class QuietTimeProperty:
        def __init__(self, *, end: builtins.str, start: builtins.str) -> None:
            '''
            :param end: ``CfnApplicationSettings.QuietTimeProperty.End``.
            :param start: ``CfnApplicationSettings.QuietTimeProperty.Start``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "end": end,
                "start": start,
            }

        @builtins.property
        def end(self) -> builtins.str:
            '''``CfnApplicationSettings.QuietTimeProperty.End``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html#cfn-pinpoint-applicationsettings-quiettime-end
            '''
            result = self._values.get("end")
            assert result is not None, "Required property 'end' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start(self) -> builtins.str:
            '''``CfnApplicationSettings.QuietTimeProperty.Start``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-applicationsettings-quiettime.html#cfn-pinpoint-applicationsettings-quiettime-start
            '''
            result = self._values.get("start")
            assert result is not None, "Required property 'start' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuietTimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnApplicationSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "campaign_hook": "campaignHook",
        "cloud_watch_metrics_enabled": "cloudWatchMetricsEnabled",
        "limits": "limits",
        "quiet_time": "quietTime",
    },
)
class CfnApplicationSettingsProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        campaign_hook: typing.Optional[typing.Union[CfnApplicationSettings.CampaignHookProperty, aws_cdk.core.IResolvable]] = None,
        cloud_watch_metrics_enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        limits: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApplicationSettings.LimitsProperty]] = None,
        quiet_time: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApplicationSettings.QuietTimeProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::ApplicationSettings``.

        :param application_id: ``AWS::Pinpoint::ApplicationSettings.ApplicationId``.
        :param campaign_hook: ``AWS::Pinpoint::ApplicationSettings.CampaignHook``.
        :param cloud_watch_metrics_enabled: ``AWS::Pinpoint::ApplicationSettings.CloudWatchMetricsEnabled``.
        :param limits: ``AWS::Pinpoint::ApplicationSettings.Limits``.
        :param quiet_time: ``AWS::Pinpoint::ApplicationSettings.QuietTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
        }
        if campaign_hook is not None:
            self._values["campaign_hook"] = campaign_hook
        if cloud_watch_metrics_enabled is not None:
            self._values["cloud_watch_metrics_enabled"] = cloud_watch_metrics_enabled
        if limits is not None:
            self._values["limits"] = limits
        if quiet_time is not None:
            self._values["quiet_time"] = quiet_time

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::ApplicationSettings.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def campaign_hook(
        self,
    ) -> typing.Optional[typing.Union[CfnApplicationSettings.CampaignHookProperty, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::ApplicationSettings.CampaignHook``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-campaignhook
        '''
        result = self._values.get("campaign_hook")
        return typing.cast(typing.Optional[typing.Union[CfnApplicationSettings.CampaignHookProperty, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def cloud_watch_metrics_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::ApplicationSettings.CloudWatchMetricsEnabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-cloudwatchmetricsenabled
        '''
        result = self._values.get("cloud_watch_metrics_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def limits(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApplicationSettings.LimitsProperty]]:
        '''``AWS::Pinpoint::ApplicationSettings.Limits``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-limits
        '''
        result = self._values.get("limits")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApplicationSettings.LimitsProperty]], result)

    @builtins.property
    def quiet_time(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApplicationSettings.QuietTimeProperty]]:
        '''``AWS::Pinpoint::ApplicationSettings.QuietTime``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html#cfn-pinpoint-applicationsettings-quiettime
        '''
        result = self._values.get("quiet_time")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnApplicationSettings.QuietTimeProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnBaiduChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnBaiduChannel",
):
    '''A CloudFormation ``AWS::Pinpoint::BaiduChannel``.

    :cloudformationResource: AWS::Pinpoint::BaiduChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        api_key: builtins.str,
        application_id: builtins.str,
        secret_key: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::BaiduChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_key: ``AWS::Pinpoint::BaiduChannel.ApiKey``.
        :param application_id: ``AWS::Pinpoint::BaiduChannel.ApplicationId``.
        :param secret_key: ``AWS::Pinpoint::BaiduChannel.SecretKey``.
        :param enabled: ``AWS::Pinpoint::BaiduChannel.Enabled``.
        '''
        props = CfnBaiduChannelProps(
            api_key=api_key,
            application_id=application_id,
            secret_key=secret_key,
            enabled=enabled,
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
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        '''``AWS::Pinpoint::BaiduChannel.ApiKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-apikey
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        jsii.set(self, "apiKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::BaiduChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> builtins.str:
        '''``AWS::Pinpoint::BaiduChannel.SecretKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-secretkey
        '''
        return typing.cast(builtins.str, jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: builtins.str) -> None:
        jsii.set(self, "secretKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::BaiduChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enabled", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnBaiduChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "application_id": "applicationId",
        "secret_key": "secretKey",
        "enabled": "enabled",
    },
)
class CfnBaiduChannelProps:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        application_id: builtins.str,
        secret_key: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::BaiduChannel``.

        :param api_key: ``AWS::Pinpoint::BaiduChannel.ApiKey``.
        :param application_id: ``AWS::Pinpoint::BaiduChannel.ApplicationId``.
        :param secret_key: ``AWS::Pinpoint::BaiduChannel.SecretKey``.
        :param enabled: ``AWS::Pinpoint::BaiduChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
            "application_id": application_id,
            "secret_key": secret_key,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def api_key(self) -> builtins.str:
        '''``AWS::Pinpoint::BaiduChannel.ApiKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-apikey
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::BaiduChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_key(self) -> builtins.str:
        '''``AWS::Pinpoint::BaiduChannel.SecretKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-secretkey
        '''
        result = self._values.get("secret_key")
        assert result is not None, "Required property 'secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::BaiduChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html#cfn-pinpoint-baiduchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBaiduChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCampaign(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign",
):
    '''A CloudFormation ``AWS::Pinpoint::Campaign``.

    :cloudformationResource: AWS::Pinpoint::Campaign
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        message_configuration: typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageConfigurationProperty"],
        name: builtins.str,
        schedule: typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.ScheduleProperty"],
        segment_id: builtins.str,
        additional_treatments: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.WriteTreatmentResourceProperty"]]]] = None,
        campaign_hook: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignHookProperty"]] = None,
        description: typing.Optional[builtins.str] = None,
        holdout_percent: typing.Optional[jsii.Number] = None,
        is_paused: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        limits: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.LimitsProperty"]] = None,
        segment_version: typing.Optional[jsii.Number] = None,
        tags: typing.Any = None,
        treatment_description: typing.Optional[builtins.str] = None,
        treatment_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::Campaign``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::Campaign.ApplicationId``.
        :param message_configuration: ``AWS::Pinpoint::Campaign.MessageConfiguration``.
        :param name: ``AWS::Pinpoint::Campaign.Name``.
        :param schedule: ``AWS::Pinpoint::Campaign.Schedule``.
        :param segment_id: ``AWS::Pinpoint::Campaign.SegmentId``.
        :param additional_treatments: ``AWS::Pinpoint::Campaign.AdditionalTreatments``.
        :param campaign_hook: ``AWS::Pinpoint::Campaign.CampaignHook``.
        :param description: ``AWS::Pinpoint::Campaign.Description``.
        :param holdout_percent: ``AWS::Pinpoint::Campaign.HoldoutPercent``.
        :param is_paused: ``AWS::Pinpoint::Campaign.IsPaused``.
        :param limits: ``AWS::Pinpoint::Campaign.Limits``.
        :param segment_version: ``AWS::Pinpoint::Campaign.SegmentVersion``.
        :param tags: ``AWS::Pinpoint::Campaign.Tags``.
        :param treatment_description: ``AWS::Pinpoint::Campaign.TreatmentDescription``.
        :param treatment_name: ``AWS::Pinpoint::Campaign.TreatmentName``.
        '''
        props = CfnCampaignProps(
            application_id=application_id,
            message_configuration=message_configuration,
            name=name,
            schedule=schedule,
            segment_id=segment_id,
            additional_treatments=additional_treatments,
            campaign_hook=campaign_hook,
            description=description,
            holdout_percent=holdout_percent,
            is_paused=is_paused,
            limits=limits,
            segment_version=segment_version,
            tags=tags,
            treatment_description=treatment_description,
            treatment_name=treatment_name,
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
    @jsii.member(jsii_name="attrCampaignId")
    def attr_campaign_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: CampaignId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCampaignId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Pinpoint::Campaign.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::Campaign.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="messageConfiguration")
    def message_configuration(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageConfigurationProperty"]:
        '''``AWS::Pinpoint::Campaign.MessageConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-messageconfiguration
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageConfigurationProperty"], jsii.get(self, "messageConfiguration"))

    @message_configuration.setter
    def message_configuration(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageConfigurationProperty"],
    ) -> None:
        jsii.set(self, "messageConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Pinpoint::Campaign.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.ScheduleProperty"]:
        '''``AWS::Pinpoint::Campaign.Schedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-schedule
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.ScheduleProperty"], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.ScheduleProperty"],
    ) -> None:
        jsii.set(self, "schedule", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="segmentId")
    def segment_id(self) -> builtins.str:
        '''``AWS::Pinpoint::Campaign.SegmentId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentid
        '''
        return typing.cast(builtins.str, jsii.get(self, "segmentId"))

    @segment_id.setter
    def segment_id(self, value: builtins.str) -> None:
        jsii.set(self, "segmentId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="additionalTreatments")
    def additional_treatments(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.WriteTreatmentResourceProperty"]]]]:
        '''``AWS::Pinpoint::Campaign.AdditionalTreatments``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-additionaltreatments
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.WriteTreatmentResourceProperty"]]]], jsii.get(self, "additionalTreatments"))

    @additional_treatments.setter
    def additional_treatments(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.WriteTreatmentResourceProperty"]]]],
    ) -> None:
        jsii.set(self, "additionalTreatments", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="campaignHook")
    def campaign_hook(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignHookProperty"]]:
        '''``AWS::Pinpoint::Campaign.CampaignHook``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-campaignhook
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignHookProperty"]], jsii.get(self, "campaignHook"))

    @campaign_hook.setter
    def campaign_hook(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignHookProperty"]],
    ) -> None:
        jsii.set(self, "campaignHook", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::Campaign.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "description", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="holdoutPercent")
    def holdout_percent(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Pinpoint::Campaign.HoldoutPercent``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-holdoutpercent
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "holdoutPercent"))

    @holdout_percent.setter
    def holdout_percent(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "holdoutPercent", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="isPaused")
    def is_paused(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::Campaign.IsPaused``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-ispaused
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "isPaused"))

    @is_paused.setter
    def is_paused(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "isPaused", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="limits")
    def limits(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.LimitsProperty"]]:
        '''``AWS::Pinpoint::Campaign.Limits``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-limits
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.LimitsProperty"]], jsii.get(self, "limits"))

    @limits.setter
    def limits(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.LimitsProperty"]],
    ) -> None:
        jsii.set(self, "limits", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="segmentVersion")
    def segment_version(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Pinpoint::Campaign.SegmentVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentversion
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "segmentVersion"))

    @segment_version.setter
    def segment_version(self, value: typing.Optional[jsii.Number]) -> None:
        jsii.set(self, "segmentVersion", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="treatmentDescription")
    def treatment_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::Campaign.TreatmentDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "treatmentDescription"))

    @treatment_description.setter
    def treatment_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "treatmentDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="treatmentName")
    def treatment_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::Campaign.TreatmentName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "treatmentName"))

    @treatment_name.setter
    def treatment_name(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "treatmentName", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.AttributeDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"attribute_type": "attributeType", "values": "values"},
    )
    class AttributeDimensionProperty:
        def __init__(
            self,
            *,
            attribute_type: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param attribute_type: ``CfnCampaign.AttributeDimensionProperty.AttributeType``.
            :param values: ``CfnCampaign.AttributeDimensionProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attribute_type is not None:
                self._values["attribute_type"] = attribute_type
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def attribute_type(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.AttributeDimensionProperty.AttributeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html#cfn-pinpoint-campaign-attributedimension-attributetype
            '''
            result = self._values.get("attribute_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnCampaign.AttributeDimensionProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-attributedimension.html#cfn-pinpoint-campaign-attributedimension-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.CampaignEmailMessageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "body": "body",
            "from_address": "fromAddress",
            "html_body": "htmlBody",
            "title": "title",
        },
    )
    class CampaignEmailMessageProperty:
        def __init__(
            self,
            *,
            body: typing.Optional[builtins.str] = None,
            from_address: typing.Optional[builtins.str] = None,
            html_body: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param body: ``CfnCampaign.CampaignEmailMessageProperty.Body``.
            :param from_address: ``CfnCampaign.CampaignEmailMessageProperty.FromAddress``.
            :param html_body: ``CfnCampaign.CampaignEmailMessageProperty.HtmlBody``.
            :param title: ``CfnCampaign.CampaignEmailMessageProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if body is not None:
                self._values["body"] = body
            if from_address is not None:
                self._values["from_address"] = from_address
            if html_body is not None:
                self._values["html_body"] = html_body
            if title is not None:
                self._values["title"] = title

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignEmailMessageProperty.Body``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def from_address(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignEmailMessageProperty.FromAddress``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-fromaddress
            '''
            result = self._values.get("from_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def html_body(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignEmailMessageProperty.HtmlBody``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-htmlbody
            '''
            result = self._values.get("html_body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignEmailMessageProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignemailmessage.html#cfn-pinpoint-campaign-campaignemailmessage-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignEmailMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.CampaignEventFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"dimensions": "dimensions", "filter_type": "filterType"},
    )
    class CampaignEventFilterProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.EventDimensionsProperty"]] = None,
            filter_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param dimensions: ``CfnCampaign.CampaignEventFilterProperty.Dimensions``.
            :param filter_type: ``CfnCampaign.CampaignEventFilterProperty.FilterType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if filter_type is not None:
                self._values["filter_type"] = filter_type

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.EventDimensionsProperty"]]:
            '''``CfnCampaign.CampaignEventFilterProperty.Dimensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html#cfn-pinpoint-campaign-campaigneventfilter-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.EventDimensionsProperty"]], result)

        @builtins.property
        def filter_type(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignEventFilterProperty.FilterType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaigneventfilter.html#cfn-pinpoint-campaign-campaigneventfilter-filtertype
            '''
            result = self._values.get("filter_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignEventFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.CampaignHookProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_function_name": "lambdaFunctionName",
            "mode": "mode",
            "web_url": "webUrl",
        },
    )
    class CampaignHookProperty:
        def __init__(
            self,
            *,
            lambda_function_name: typing.Optional[builtins.str] = None,
            mode: typing.Optional[builtins.str] = None,
            web_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param lambda_function_name: ``CfnCampaign.CampaignHookProperty.LambdaFunctionName``.
            :param mode: ``CfnCampaign.CampaignHookProperty.Mode``.
            :param web_url: ``CfnCampaign.CampaignHookProperty.WebUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if lambda_function_name is not None:
                self._values["lambda_function_name"] = lambda_function_name
            if mode is not None:
                self._values["mode"] = mode
            if web_url is not None:
                self._values["web_url"] = web_url

        @builtins.property
        def lambda_function_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignHookProperty.LambdaFunctionName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-lambdafunctionname
            '''
            result = self._values.get("lambda_function_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignHookProperty.Mode``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def web_url(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignHookProperty.WebUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignhook.html#cfn-pinpoint-campaign-campaignhook-weburl
            '''
            result = self._values.get("web_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.CampaignSmsMessageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "body": "body",
            "entity_id": "entityId",
            "message_type": "messageType",
            "origination_number": "originationNumber",
            "sender_id": "senderId",
            "template_id": "templateId",
        },
    )
    class CampaignSmsMessageProperty:
        def __init__(
            self,
            *,
            body: typing.Optional[builtins.str] = None,
            entity_id: typing.Optional[builtins.str] = None,
            message_type: typing.Optional[builtins.str] = None,
            origination_number: typing.Optional[builtins.str] = None,
            sender_id: typing.Optional[builtins.str] = None,
            template_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param body: ``CfnCampaign.CampaignSmsMessageProperty.Body``.
            :param entity_id: ``CfnCampaign.CampaignSmsMessageProperty.EntityId``.
            :param message_type: ``CfnCampaign.CampaignSmsMessageProperty.MessageType``.
            :param origination_number: ``CfnCampaign.CampaignSmsMessageProperty.OriginationNumber``.
            :param sender_id: ``CfnCampaign.CampaignSmsMessageProperty.SenderId``.
            :param template_id: ``CfnCampaign.CampaignSmsMessageProperty.TemplateId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if body is not None:
                self._values["body"] = body
            if entity_id is not None:
                self._values["entity_id"] = entity_id
            if message_type is not None:
                self._values["message_type"] = message_type
            if origination_number is not None:
                self._values["origination_number"] = origination_number
            if sender_id is not None:
                self._values["sender_id"] = sender_id
            if template_id is not None:
                self._values["template_id"] = template_id

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignSmsMessageProperty.Body``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entity_id(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignSmsMessageProperty.EntityId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-entityid
            '''
            result = self._values.get("entity_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message_type(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignSmsMessageProperty.MessageType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-messagetype
            '''
            result = self._values.get("message_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def origination_number(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignSmsMessageProperty.OriginationNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-originationnumber
            '''
            result = self._values.get("origination_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sender_id(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignSmsMessageProperty.SenderId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-senderid
            '''
            result = self._values.get("sender_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def template_id(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.CampaignSmsMessageProperty.TemplateId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-campaignsmsmessage.html#cfn-pinpoint-campaign-campaignsmsmessage-templateid
            '''
            result = self._values.get("template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CampaignSmsMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.EventDimensionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attributes": "attributes",
            "event_type": "eventType",
            "metrics": "metrics",
        },
    )
    class EventDimensionsProperty:
        def __init__(
            self,
            *,
            attributes: typing.Any = None,
            event_type: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.SetDimensionProperty"]] = None,
            metrics: typing.Any = None,
        ) -> None:
            '''
            :param attributes: ``CfnCampaign.EventDimensionsProperty.Attributes``.
            :param event_type: ``CfnCampaign.EventDimensionsProperty.EventType``.
            :param metrics: ``CfnCampaign.EventDimensionsProperty.Metrics``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if event_type is not None:
                self._values["event_type"] = event_type
            if metrics is not None:
                self._values["metrics"] = metrics

        @builtins.property
        def attributes(self) -> typing.Any:
            '''``CfnCampaign.EventDimensionsProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Any, result)

        @builtins.property
        def event_type(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.SetDimensionProperty"]]:
            '''``CfnCampaign.EventDimensionsProperty.EventType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-eventtype
            '''
            result = self._values.get("event_type")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.SetDimensionProperty"]], result)

        @builtins.property
        def metrics(self) -> typing.Any:
            '''``CfnCampaign.EventDimensionsProperty.Metrics``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-eventdimensions.html#cfn-pinpoint-campaign-eventdimensions-metrics
            '''
            result = self._values.get("metrics")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventDimensionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.LimitsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "daily": "daily",
            "maximum_duration": "maximumDuration",
            "messages_per_second": "messagesPerSecond",
            "total": "total",
        },
    )
    class LimitsProperty:
        def __init__(
            self,
            *,
            daily: typing.Optional[jsii.Number] = None,
            maximum_duration: typing.Optional[jsii.Number] = None,
            messages_per_second: typing.Optional[jsii.Number] = None,
            total: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param daily: ``CfnCampaign.LimitsProperty.Daily``.
            :param maximum_duration: ``CfnCampaign.LimitsProperty.MaximumDuration``.
            :param messages_per_second: ``CfnCampaign.LimitsProperty.MessagesPerSecond``.
            :param total: ``CfnCampaign.LimitsProperty.Total``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if daily is not None:
                self._values["daily"] = daily
            if maximum_duration is not None:
                self._values["maximum_duration"] = maximum_duration
            if messages_per_second is not None:
                self._values["messages_per_second"] = messages_per_second
            if total is not None:
                self._values["total"] = total

        @builtins.property
        def daily(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.LimitsProperty.Daily``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-daily
            '''
            result = self._values.get("daily")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_duration(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.LimitsProperty.MaximumDuration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-maximumduration
            '''
            result = self._values.get("maximum_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def messages_per_second(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.LimitsProperty.MessagesPerSecond``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-messagespersecond
            '''
            result = self._values.get("messages_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.LimitsProperty.Total``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-limits.html#cfn-pinpoint-campaign-limits-total
            '''
            result = self._values.get("total")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.MessageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "adm_message": "admMessage",
            "apns_message": "apnsMessage",
            "baidu_message": "baiduMessage",
            "default_message": "defaultMessage",
            "email_message": "emailMessage",
            "gcm_message": "gcmMessage",
            "sms_message": "smsMessage",
        },
    )
    class MessageConfigurationProperty:
        def __init__(
            self,
            *,
            adm_message: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]] = None,
            apns_message: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]] = None,
            baidu_message: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]] = None,
            default_message: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]] = None,
            email_message: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignEmailMessageProperty"]] = None,
            gcm_message: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]] = None,
            sms_message: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignSmsMessageProperty"]] = None,
        ) -> None:
            '''
            :param adm_message: ``CfnCampaign.MessageConfigurationProperty.ADMMessage``.
            :param apns_message: ``CfnCampaign.MessageConfigurationProperty.APNSMessage``.
            :param baidu_message: ``CfnCampaign.MessageConfigurationProperty.BaiduMessage``.
            :param default_message: ``CfnCampaign.MessageConfigurationProperty.DefaultMessage``.
            :param email_message: ``CfnCampaign.MessageConfigurationProperty.EmailMessage``.
            :param gcm_message: ``CfnCampaign.MessageConfigurationProperty.GCMMessage``.
            :param sms_message: ``CfnCampaign.MessageConfigurationProperty.SMSMessage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if adm_message is not None:
                self._values["adm_message"] = adm_message
            if apns_message is not None:
                self._values["apns_message"] = apns_message
            if baidu_message is not None:
                self._values["baidu_message"] = baidu_message
            if default_message is not None:
                self._values["default_message"] = default_message
            if email_message is not None:
                self._values["email_message"] = email_message
            if gcm_message is not None:
                self._values["gcm_message"] = gcm_message
            if sms_message is not None:
                self._values["sms_message"] = sms_message

        @builtins.property
        def adm_message(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]]:
            '''``CfnCampaign.MessageConfigurationProperty.ADMMessage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-admmessage
            '''
            result = self._values.get("adm_message")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]], result)

        @builtins.property
        def apns_message(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]]:
            '''``CfnCampaign.MessageConfigurationProperty.APNSMessage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-apnsmessage
            '''
            result = self._values.get("apns_message")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]], result)

        @builtins.property
        def baidu_message(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]]:
            '''``CfnCampaign.MessageConfigurationProperty.BaiduMessage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-baidumessage
            '''
            result = self._values.get("baidu_message")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]], result)

        @builtins.property
        def default_message(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]]:
            '''``CfnCampaign.MessageConfigurationProperty.DefaultMessage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-defaultmessage
            '''
            result = self._values.get("default_message")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]], result)

        @builtins.property
        def email_message(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignEmailMessageProperty"]]:
            '''``CfnCampaign.MessageConfigurationProperty.EmailMessage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-emailmessage
            '''
            result = self._values.get("email_message")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignEmailMessageProperty"]], result)

        @builtins.property
        def gcm_message(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]]:
            '''``CfnCampaign.MessageConfigurationProperty.GCMMessage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-gcmmessage
            '''
            result = self._values.get("gcm_message")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageProperty"]], result)

        @builtins.property
        def sms_message(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignSmsMessageProperty"]]:
            '''``CfnCampaign.MessageConfigurationProperty.SMSMessage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-smsmessage
            '''
            result = self._values.get("sms_message")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignSmsMessageProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.MessageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "body": "body",
            "image_icon_url": "imageIconUrl",
            "image_small_icon_url": "imageSmallIconUrl",
            "image_url": "imageUrl",
            "json_body": "jsonBody",
            "media_url": "mediaUrl",
            "raw_content": "rawContent",
            "silent_push": "silentPush",
            "time_to_live": "timeToLive",
            "title": "title",
            "url": "url",
        },
    )
    class MessageProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            body: typing.Optional[builtins.str] = None,
            image_icon_url: typing.Optional[builtins.str] = None,
            image_small_icon_url: typing.Optional[builtins.str] = None,
            image_url: typing.Optional[builtins.str] = None,
            json_body: typing.Optional[builtins.str] = None,
            media_url: typing.Optional[builtins.str] = None,
            raw_content: typing.Optional[builtins.str] = None,
            silent_push: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            time_to_live: typing.Optional[jsii.Number] = None,
            title: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param action: ``CfnCampaign.MessageProperty.Action``.
            :param body: ``CfnCampaign.MessageProperty.Body``.
            :param image_icon_url: ``CfnCampaign.MessageProperty.ImageIconUrl``.
            :param image_small_icon_url: ``CfnCampaign.MessageProperty.ImageSmallIconUrl``.
            :param image_url: ``CfnCampaign.MessageProperty.ImageUrl``.
            :param json_body: ``CfnCampaign.MessageProperty.JsonBody``.
            :param media_url: ``CfnCampaign.MessageProperty.MediaUrl``.
            :param raw_content: ``CfnCampaign.MessageProperty.RawContent``.
            :param silent_push: ``CfnCampaign.MessageProperty.SilentPush``.
            :param time_to_live: ``CfnCampaign.MessageProperty.TimeToLive``.
            :param title: ``CfnCampaign.MessageProperty.Title``.
            :param url: ``CfnCampaign.MessageProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if body is not None:
                self._values["body"] = body
            if image_icon_url is not None:
                self._values["image_icon_url"] = image_icon_url
            if image_small_icon_url is not None:
                self._values["image_small_icon_url"] = image_small_icon_url
            if image_url is not None:
                self._values["image_url"] = image_url
            if json_body is not None:
                self._values["json_body"] = json_body
            if media_url is not None:
                self._values["media_url"] = media_url
            if raw_content is not None:
                self._values["raw_content"] = raw_content
            if silent_push is not None:
                self._values["silent_push"] = silent_push
            if time_to_live is not None:
                self._values["time_to_live"] = time_to_live
            if title is not None:
                self._values["title"] = title
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MessageProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MessageProperty.Body``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_icon_url(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MessageProperty.ImageIconUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imageiconurl
            '''
            result = self._values.get("image_icon_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_small_icon_url(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MessageProperty.ImageSmallIconUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imagesmalliconurl
            '''
            result = self._values.get("image_small_icon_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_url(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MessageProperty.ImageUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-imageurl
            '''
            result = self._values.get("image_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def json_body(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MessageProperty.JsonBody``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-jsonbody
            '''
            result = self._values.get("json_body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def media_url(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MessageProperty.MediaUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-mediaurl
            '''
            result = self._values.get("media_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def raw_content(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MessageProperty.RawContent``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-rawcontent
            '''
            result = self._values.get("raw_content")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def silent_push(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCampaign.MessageProperty.SilentPush``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-silentpush
            '''
            result = self._values.get("silent_push")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def time_to_live(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.MessageProperty.TimeToLive``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-timetolive
            '''
            result = self._values.get("time_to_live")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MessageProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MessageProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-message.html#cfn-pinpoint-campaign-message-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.MetricDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison_operator": "comparisonOperator", "value": "value"},
    )
    class MetricDimensionProperty:
        def __init__(
            self,
            *,
            comparison_operator: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param comparison_operator: ``CfnCampaign.MetricDimensionProperty.ComparisonOperator``.
            :param value: ``CfnCampaign.MetricDimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if comparison_operator is not None:
                self._values["comparison_operator"] = comparison_operator
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def comparison_operator(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.MetricDimensionProperty.ComparisonOperator``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html#cfn-pinpoint-campaign-metricdimension-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.MetricDimensionProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-metricdimension.html#cfn-pinpoint-campaign-metricdimension-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.QuietTimeProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class QuietTimeProperty:
        def __init__(self, *, end: builtins.str, start: builtins.str) -> None:
            '''
            :param end: ``CfnCampaign.QuietTimeProperty.End``.
            :param start: ``CfnCampaign.QuietTimeProperty.Start``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "end": end,
                "start": start,
            }

        @builtins.property
        def end(self) -> builtins.str:
            '''``CfnCampaign.QuietTimeProperty.End``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html#cfn-pinpoint-campaign-schedule-quiettime-end
            '''
            result = self._values.get("end")
            assert result is not None, "Required property 'end' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start(self) -> builtins.str:
            '''``CfnCampaign.QuietTimeProperty.Start``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule-quiettime.html#cfn-pinpoint-campaign-schedule-quiettime-start
            '''
            result = self._values.get("start")
            assert result is not None, "Required property 'start' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuietTimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_time": "endTime",
            "event_filter": "eventFilter",
            "frequency": "frequency",
            "is_local_time": "isLocalTime",
            "quiet_time": "quietTime",
            "start_time": "startTime",
            "time_zone": "timeZone",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            end_time: typing.Optional[builtins.str] = None,
            event_filter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignEventFilterProperty"]] = None,
            frequency: typing.Optional[builtins.str] = None,
            is_local_time: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            quiet_time: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.QuietTimeProperty"]] = None,
            start_time: typing.Optional[builtins.str] = None,
            time_zone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param end_time: ``CfnCampaign.ScheduleProperty.EndTime``.
            :param event_filter: ``CfnCampaign.ScheduleProperty.EventFilter``.
            :param frequency: ``CfnCampaign.ScheduleProperty.Frequency``.
            :param is_local_time: ``CfnCampaign.ScheduleProperty.IsLocalTime``.
            :param quiet_time: ``CfnCampaign.ScheduleProperty.QuietTime``.
            :param start_time: ``CfnCampaign.ScheduleProperty.StartTime``.
            :param time_zone: ``CfnCampaign.ScheduleProperty.TimeZone``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if end_time is not None:
                self._values["end_time"] = end_time
            if event_filter is not None:
                self._values["event_filter"] = event_filter
            if frequency is not None:
                self._values["frequency"] = frequency
            if is_local_time is not None:
                self._values["is_local_time"] = is_local_time
            if quiet_time is not None:
                self._values["quiet_time"] = quiet_time
            if start_time is not None:
                self._values["start_time"] = start_time
            if time_zone is not None:
                self._values["time_zone"] = time_zone

        @builtins.property
        def end_time(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.ScheduleProperty.EndTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-endtime
            '''
            result = self._values.get("end_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def event_filter(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignEventFilterProperty"]]:
            '''``CfnCampaign.ScheduleProperty.EventFilter``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-eventfilter
            '''
            result = self._values.get("event_filter")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.CampaignEventFilterProperty"]], result)

        @builtins.property
        def frequency(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.ScheduleProperty.Frequency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-frequency
            '''
            result = self._values.get("frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def is_local_time(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCampaign.ScheduleProperty.IsLocalTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-islocaltime
            '''
            result = self._values.get("is_local_time")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def quiet_time(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.QuietTimeProperty"]]:
            '''``CfnCampaign.ScheduleProperty.QuietTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-quiettime
            '''
            result = self._values.get("quiet_time")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.QuietTimeProperty"]], result)

        @builtins.property
        def start_time(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.ScheduleProperty.StartTime``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-starttime
            '''
            result = self._values.get("start_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def time_zone(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.ScheduleProperty.TimeZone``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-schedule.html#cfn-pinpoint-campaign-schedule-timezone
            '''
            result = self._values.get("time_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.SetDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_type": "dimensionType", "values": "values"},
    )
    class SetDimensionProperty:
        def __init__(
            self,
            *,
            dimension_type: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param dimension_type: ``CfnCampaign.SetDimensionProperty.DimensionType``.
            :param values: ``CfnCampaign.SetDimensionProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dimension_type is not None:
                self._values["dimension_type"] = dimension_type
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def dimension_type(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.SetDimensionProperty.DimensionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html#cfn-pinpoint-campaign-setdimension-dimensiontype
            '''
            result = self._values.get("dimension_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnCampaign.SetDimensionProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-setdimension.html#cfn-pinpoint-campaign-setdimension-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SetDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnCampaign.WriteTreatmentResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "message_configuration": "messageConfiguration",
            "schedule": "schedule",
            "size_percent": "sizePercent",
            "treatment_description": "treatmentDescription",
            "treatment_name": "treatmentName",
        },
    )
    class WriteTreatmentResourceProperty:
        def __init__(
            self,
            *,
            message_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageConfigurationProperty"]] = None,
            schedule: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.ScheduleProperty"]] = None,
            size_percent: typing.Optional[jsii.Number] = None,
            treatment_description: typing.Optional[builtins.str] = None,
            treatment_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param message_configuration: ``CfnCampaign.WriteTreatmentResourceProperty.MessageConfiguration``.
            :param schedule: ``CfnCampaign.WriteTreatmentResourceProperty.Schedule``.
            :param size_percent: ``CfnCampaign.WriteTreatmentResourceProperty.SizePercent``.
            :param treatment_description: ``CfnCampaign.WriteTreatmentResourceProperty.TreatmentDescription``.
            :param treatment_name: ``CfnCampaign.WriteTreatmentResourceProperty.TreatmentName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if message_configuration is not None:
                self._values["message_configuration"] = message_configuration
            if schedule is not None:
                self._values["schedule"] = schedule
            if size_percent is not None:
                self._values["size_percent"] = size_percent
            if treatment_description is not None:
                self._values["treatment_description"] = treatment_description
            if treatment_name is not None:
                self._values["treatment_name"] = treatment_name

        @builtins.property
        def message_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageConfigurationProperty"]]:
            '''``CfnCampaign.WriteTreatmentResourceProperty.MessageConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-messageconfiguration
            '''
            result = self._values.get("message_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.MessageConfigurationProperty"]], result)

        @builtins.property
        def schedule(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.ScheduleProperty"]]:
            '''``CfnCampaign.WriteTreatmentResourceProperty.Schedule``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-schedule
            '''
            result = self._values.get("schedule")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCampaign.ScheduleProperty"]], result)

        @builtins.property
        def size_percent(self) -> typing.Optional[jsii.Number]:
            '''``CfnCampaign.WriteTreatmentResourceProperty.SizePercent``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-sizepercent
            '''
            result = self._values.get("size_percent")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def treatment_description(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.WriteTreatmentResourceProperty.TreatmentDescription``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-treatmentdescription
            '''
            result = self._values.get("treatment_description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def treatment_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCampaign.WriteTreatmentResourceProperty.TreatmentName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-writetreatmentresource.html#cfn-pinpoint-campaign-writetreatmentresource-treatmentname
            '''
            result = self._values.get("treatment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WriteTreatmentResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnCampaignProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "message_configuration": "messageConfiguration",
        "name": "name",
        "schedule": "schedule",
        "segment_id": "segmentId",
        "additional_treatments": "additionalTreatments",
        "campaign_hook": "campaignHook",
        "description": "description",
        "holdout_percent": "holdoutPercent",
        "is_paused": "isPaused",
        "limits": "limits",
        "segment_version": "segmentVersion",
        "tags": "tags",
        "treatment_description": "treatmentDescription",
        "treatment_name": "treatmentName",
    },
)
class CfnCampaignProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        message_configuration: typing.Union[aws_cdk.core.IResolvable, CfnCampaign.MessageConfigurationProperty],
        name: builtins.str,
        schedule: typing.Union[aws_cdk.core.IResolvable, CfnCampaign.ScheduleProperty],
        segment_id: builtins.str,
        additional_treatments: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.WriteTreatmentResourceProperty]]]] = None,
        campaign_hook: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.CampaignHookProperty]] = None,
        description: typing.Optional[builtins.str] = None,
        holdout_percent: typing.Optional[jsii.Number] = None,
        is_paused: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        limits: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.LimitsProperty]] = None,
        segment_version: typing.Optional[jsii.Number] = None,
        tags: typing.Any = None,
        treatment_description: typing.Optional[builtins.str] = None,
        treatment_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::Campaign``.

        :param application_id: ``AWS::Pinpoint::Campaign.ApplicationId``.
        :param message_configuration: ``AWS::Pinpoint::Campaign.MessageConfiguration``.
        :param name: ``AWS::Pinpoint::Campaign.Name``.
        :param schedule: ``AWS::Pinpoint::Campaign.Schedule``.
        :param segment_id: ``AWS::Pinpoint::Campaign.SegmentId``.
        :param additional_treatments: ``AWS::Pinpoint::Campaign.AdditionalTreatments``.
        :param campaign_hook: ``AWS::Pinpoint::Campaign.CampaignHook``.
        :param description: ``AWS::Pinpoint::Campaign.Description``.
        :param holdout_percent: ``AWS::Pinpoint::Campaign.HoldoutPercent``.
        :param is_paused: ``AWS::Pinpoint::Campaign.IsPaused``.
        :param limits: ``AWS::Pinpoint::Campaign.Limits``.
        :param segment_version: ``AWS::Pinpoint::Campaign.SegmentVersion``.
        :param tags: ``AWS::Pinpoint::Campaign.Tags``.
        :param treatment_description: ``AWS::Pinpoint::Campaign.TreatmentDescription``.
        :param treatment_name: ``AWS::Pinpoint::Campaign.TreatmentName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "message_configuration": message_configuration,
            "name": name,
            "schedule": schedule,
            "segment_id": segment_id,
        }
        if additional_treatments is not None:
            self._values["additional_treatments"] = additional_treatments
        if campaign_hook is not None:
            self._values["campaign_hook"] = campaign_hook
        if description is not None:
            self._values["description"] = description
        if holdout_percent is not None:
            self._values["holdout_percent"] = holdout_percent
        if is_paused is not None:
            self._values["is_paused"] = is_paused
        if limits is not None:
            self._values["limits"] = limits
        if segment_version is not None:
            self._values["segment_version"] = segment_version
        if tags is not None:
            self._values["tags"] = tags
        if treatment_description is not None:
            self._values["treatment_description"] = treatment_description
        if treatment_name is not None:
            self._values["treatment_name"] = treatment_name

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::Campaign.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def message_configuration(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnCampaign.MessageConfigurationProperty]:
        '''``AWS::Pinpoint::Campaign.MessageConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-messageconfiguration
        '''
        result = self._values.get("message_configuration")
        assert result is not None, "Required property 'message_configuration' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnCampaign.MessageConfigurationProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Pinpoint::Campaign.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnCampaign.ScheduleProperty]:
        '''``AWS::Pinpoint::Campaign.Schedule``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-schedule
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnCampaign.ScheduleProperty], result)

    @builtins.property
    def segment_id(self) -> builtins.str:
        '''``AWS::Pinpoint::Campaign.SegmentId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentid
        '''
        result = self._values.get("segment_id")
        assert result is not None, "Required property 'segment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_treatments(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.WriteTreatmentResourceProperty]]]]:
        '''``AWS::Pinpoint::Campaign.AdditionalTreatments``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-additionaltreatments
        '''
        result = self._values.get("additional_treatments")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.WriteTreatmentResourceProperty]]]], result)

    @builtins.property
    def campaign_hook(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.CampaignHookProperty]]:
        '''``AWS::Pinpoint::Campaign.CampaignHook``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-campaignhook
        '''
        result = self._values.get("campaign_hook")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.CampaignHookProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::Campaign.Description``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def holdout_percent(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Pinpoint::Campaign.HoldoutPercent``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-holdoutpercent
        '''
        result = self._values.get("holdout_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def is_paused(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::Campaign.IsPaused``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-ispaused
        '''
        result = self._values.get("is_paused")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def limits(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.LimitsProperty]]:
        '''``AWS::Pinpoint::Campaign.Limits``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-limits
        '''
        result = self._values.get("limits")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCampaign.LimitsProperty]], result)

    @builtins.property
    def segment_version(self) -> typing.Optional[jsii.Number]:
        '''``AWS::Pinpoint::Campaign.SegmentVersion``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-segmentversion
        '''
        result = self._values.get("segment_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::Pinpoint::Campaign.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def treatment_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::Campaign.TreatmentDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentdescription
        '''
        result = self._values.get("treatment_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def treatment_name(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::Campaign.TreatmentName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html#cfn-pinpoint-campaign-treatmentname
        '''
        result = self._values.get("treatment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCampaignProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEmailChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnEmailChannel",
):
    '''A CloudFormation ``AWS::Pinpoint::EmailChannel``.

    :cloudformationResource: AWS::Pinpoint::EmailChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        from_address: builtins.str,
        identity: builtins.str,
        configuration_set: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::EmailChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::EmailChannel.ApplicationId``.
        :param from_address: ``AWS::Pinpoint::EmailChannel.FromAddress``.
        :param identity: ``AWS::Pinpoint::EmailChannel.Identity``.
        :param configuration_set: ``AWS::Pinpoint::EmailChannel.ConfigurationSet``.
        :param enabled: ``AWS::Pinpoint::EmailChannel.Enabled``.
        :param role_arn: ``AWS::Pinpoint::EmailChannel.RoleArn``.
        '''
        props = CfnEmailChannelProps(
            application_id=application_id,
            from_address=from_address,
            identity=identity,
            configuration_set=configuration_set,
            enabled=enabled,
            role_arn=role_arn,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::EmailChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="fromAddress")
    def from_address(self) -> builtins.str:
        '''``AWS::Pinpoint::EmailChannel.FromAddress``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-fromaddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "fromAddress"))

    @from_address.setter
    def from_address(self, value: builtins.str) -> None:
        jsii.set(self, "fromAddress", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="identity")
    def identity(self) -> builtins.str:
        '''``AWS::Pinpoint::EmailChannel.Identity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-identity
        '''
        return typing.cast(builtins.str, jsii.get(self, "identity"))

    @identity.setter
    def identity(self, value: builtins.str) -> None:
        jsii.set(self, "identity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="configurationSet")
    def configuration_set(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailChannel.ConfigurationSet``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-configurationset
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationSet"))

    @configuration_set.setter
    def configuration_set(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "configurationSet", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::EmailChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailChannel.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-rolearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnEmailChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "from_address": "fromAddress",
        "identity": "identity",
        "configuration_set": "configurationSet",
        "enabled": "enabled",
        "role_arn": "roleArn",
    },
)
class CfnEmailChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        from_address: builtins.str,
        identity: builtins.str,
        configuration_set: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::EmailChannel``.

        :param application_id: ``AWS::Pinpoint::EmailChannel.ApplicationId``.
        :param from_address: ``AWS::Pinpoint::EmailChannel.FromAddress``.
        :param identity: ``AWS::Pinpoint::EmailChannel.Identity``.
        :param configuration_set: ``AWS::Pinpoint::EmailChannel.ConfigurationSet``.
        :param enabled: ``AWS::Pinpoint::EmailChannel.Enabled``.
        :param role_arn: ``AWS::Pinpoint::EmailChannel.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "from_address": from_address,
            "identity": identity,
        }
        if configuration_set is not None:
            self._values["configuration_set"] = configuration_set
        if enabled is not None:
            self._values["enabled"] = enabled
        if role_arn is not None:
            self._values["role_arn"] = role_arn

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::EmailChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def from_address(self) -> builtins.str:
        '''``AWS::Pinpoint::EmailChannel.FromAddress``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-fromaddress
        '''
        result = self._values.get("from_address")
        assert result is not None, "Required property 'from_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity(self) -> builtins.str:
        '''``AWS::Pinpoint::EmailChannel.Identity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-identity
        '''
        result = self._values.get("identity")
        assert result is not None, "Required property 'identity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_set(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailChannel.ConfigurationSet``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-configurationset
        '''
        result = self._values.get("configuration_set")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::EmailChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailChannel.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html#cfn-pinpoint-emailchannel-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEmailChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEmailTemplate(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnEmailTemplate",
):
    '''A CloudFormation ``AWS::Pinpoint::EmailTemplate``.

    :cloudformationResource: AWS::Pinpoint::EmailTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        subject: builtins.str,
        template_name: builtins.str,
        default_substitutions: typing.Optional[builtins.str] = None,
        html_part: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
        text_part: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::EmailTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param subject: ``AWS::Pinpoint::EmailTemplate.Subject``.
        :param template_name: ``AWS::Pinpoint::EmailTemplate.TemplateName``.
        :param default_substitutions: ``AWS::Pinpoint::EmailTemplate.DefaultSubstitutions``.
        :param html_part: ``AWS::Pinpoint::EmailTemplate.HtmlPart``.
        :param tags: ``AWS::Pinpoint::EmailTemplate.Tags``.
        :param template_description: ``AWS::Pinpoint::EmailTemplate.TemplateDescription``.
        :param text_part: ``AWS::Pinpoint::EmailTemplate.TextPart``.
        '''
        props = CfnEmailTemplateProps(
            subject=subject,
            template_name=template_name,
            default_substitutions=default_substitutions,
            html_part=html_part,
            tags=tags,
            template_description=template_description,
            text_part=text_part,
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
        '''``AWS::Pinpoint::EmailTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        '''``AWS::Pinpoint::EmailTemplate.Subject``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-subject
        '''
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        jsii.set(self, "subject", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> builtins.str:
        '''``AWS::Pinpoint::EmailTemplate.TemplateName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatename
        '''
        return typing.cast(builtins.str, jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: builtins.str) -> None:
        jsii.set(self, "templateName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultSubstitutions")
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailTemplate.DefaultSubstitutions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-defaultsubstitutions
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSubstitutions"))

    @default_substitutions.setter
    def default_substitutions(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultSubstitutions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="htmlPart")
    def html_part(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailTemplate.HtmlPart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-htmlpart
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "htmlPart"))

    @html_part.setter
    def html_part(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "htmlPart", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateDescription")
    def template_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailTemplate.TemplateDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatedescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateDescription"))

    @template_description.setter
    def template_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateDescription", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="textPart")
    def text_part(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailTemplate.TextPart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-textpart
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textPart"))

    @text_part.setter
    def text_part(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "textPart", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnEmailTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "subject": "subject",
        "template_name": "templateName",
        "default_substitutions": "defaultSubstitutions",
        "html_part": "htmlPart",
        "tags": "tags",
        "template_description": "templateDescription",
        "text_part": "textPart",
    },
)
class CfnEmailTemplateProps:
    def __init__(
        self,
        *,
        subject: builtins.str,
        template_name: builtins.str,
        default_substitutions: typing.Optional[builtins.str] = None,
        html_part: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
        text_part: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::EmailTemplate``.

        :param subject: ``AWS::Pinpoint::EmailTemplate.Subject``.
        :param template_name: ``AWS::Pinpoint::EmailTemplate.TemplateName``.
        :param default_substitutions: ``AWS::Pinpoint::EmailTemplate.DefaultSubstitutions``.
        :param html_part: ``AWS::Pinpoint::EmailTemplate.HtmlPart``.
        :param tags: ``AWS::Pinpoint::EmailTemplate.Tags``.
        :param template_description: ``AWS::Pinpoint::EmailTemplate.TemplateDescription``.
        :param text_part: ``AWS::Pinpoint::EmailTemplate.TextPart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "subject": subject,
            "template_name": template_name,
        }
        if default_substitutions is not None:
            self._values["default_substitutions"] = default_substitutions
        if html_part is not None:
            self._values["html_part"] = html_part
        if tags is not None:
            self._values["tags"] = tags
        if template_description is not None:
            self._values["template_description"] = template_description
        if text_part is not None:
            self._values["text_part"] = text_part

    @builtins.property
    def subject(self) -> builtins.str:
        '''``AWS::Pinpoint::EmailTemplate.Subject``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-subject
        '''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_name(self) -> builtins.str:
        '''``AWS::Pinpoint::EmailTemplate.TemplateName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatename
        '''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailTemplate.DefaultSubstitutions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-defaultsubstitutions
        '''
        result = self._values.get("default_substitutions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def html_part(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailTemplate.HtmlPart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-htmlpart
        '''
        result = self._values.get("html_part")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::Pinpoint::EmailTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def template_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailTemplate.TemplateDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-templatedescription
        '''
        result = self._values.get("template_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def text_part(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::EmailTemplate.TextPart``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html#cfn-pinpoint-emailtemplate-textpart
        '''
        result = self._values.get("text_part")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEmailTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnEventStream(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnEventStream",
):
    '''A CloudFormation ``AWS::Pinpoint::EventStream``.

    :cloudformationResource: AWS::Pinpoint::EventStream
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        destination_stream_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::EventStream``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::EventStream.ApplicationId``.
        :param destination_stream_arn: ``AWS::Pinpoint::EventStream.DestinationStreamArn``.
        :param role_arn: ``AWS::Pinpoint::EventStream.RoleArn``.
        '''
        props = CfnEventStreamProps(
            application_id=application_id,
            destination_stream_arn=destination_stream_arn,
            role_arn=role_arn,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::EventStream.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="destinationStreamArn")
    def destination_stream_arn(self) -> builtins.str:
        '''``AWS::Pinpoint::EventStream.DestinationStreamArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-destinationstreamarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "destinationStreamArn"))

    @destination_stream_arn.setter
    def destination_stream_arn(self, value: builtins.str) -> None:
        jsii.set(self, "destinationStreamArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''``AWS::Pinpoint::EventStream.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-rolearn
        '''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        jsii.set(self, "roleArn", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnEventStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "destination_stream_arn": "destinationStreamArn",
        "role_arn": "roleArn",
    },
)
class CfnEventStreamProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        destination_stream_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::EventStream``.

        :param application_id: ``AWS::Pinpoint::EventStream.ApplicationId``.
        :param destination_stream_arn: ``AWS::Pinpoint::EventStream.DestinationStreamArn``.
        :param role_arn: ``AWS::Pinpoint::EventStream.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "destination_stream_arn": destination_stream_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::EventStream.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_stream_arn(self) -> builtins.str:
        '''``AWS::Pinpoint::EventStream.DestinationStreamArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-destinationstreamarn
        '''
        result = self._values.get("destination_stream_arn")
        assert result is not None, "Required property 'destination_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''``AWS::Pinpoint::EventStream.RoleArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html#cfn-pinpoint-eventstream-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnGCMChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnGCMChannel",
):
    '''A CloudFormation ``AWS::Pinpoint::GCMChannel``.

    :cloudformationResource: AWS::Pinpoint::GCMChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        api_key: builtins.str,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::GCMChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param api_key: ``AWS::Pinpoint::GCMChannel.ApiKey``.
        :param application_id: ``AWS::Pinpoint::GCMChannel.ApplicationId``.
        :param enabled: ``AWS::Pinpoint::GCMChannel.Enabled``.
        '''
        props = CfnGCMChannelProps(
            api_key=api_key, application_id=application_id, enabled=enabled
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
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        '''``AWS::Pinpoint::GCMChannel.ApiKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-apikey
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        jsii.set(self, "apiKey", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::GCMChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::GCMChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enabled", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnGCMChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "application_id": "applicationId",
        "enabled": "enabled",
    },
)
class CfnGCMChannelProps:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::GCMChannel``.

        :param api_key: ``AWS::Pinpoint::GCMChannel.ApiKey``.
        :param application_id: ``AWS::Pinpoint::GCMChannel.ApplicationId``.
        :param enabled: ``AWS::Pinpoint::GCMChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
            "application_id": application_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def api_key(self) -> builtins.str:
        '''``AWS::Pinpoint::GCMChannel.ApiKey``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-apikey
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::GCMChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::GCMChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html#cfn-pinpoint-gcmchannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGCMChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPushTemplate(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnPushTemplate",
):
    '''A CloudFormation ``AWS::Pinpoint::PushTemplate``.

    :cloudformationResource: AWS::Pinpoint::PushTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        template_name: builtins.str,
        adm: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]] = None,
        apns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.APNSPushNotificationTemplateProperty"]] = None,
        baidu: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]] = None,
        default: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.DefaultPushNotificationTemplateProperty"]] = None,
        default_substitutions: typing.Optional[builtins.str] = None,
        gcm: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::PushTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param template_name: ``AWS::Pinpoint::PushTemplate.TemplateName``.
        :param adm: ``AWS::Pinpoint::PushTemplate.ADM``.
        :param apns: ``AWS::Pinpoint::PushTemplate.APNS``.
        :param baidu: ``AWS::Pinpoint::PushTemplate.Baidu``.
        :param default: ``AWS::Pinpoint::PushTemplate.Default``.
        :param default_substitutions: ``AWS::Pinpoint::PushTemplate.DefaultSubstitutions``.
        :param gcm: ``AWS::Pinpoint::PushTemplate.GCM``.
        :param tags: ``AWS::Pinpoint::PushTemplate.Tags``.
        :param template_description: ``AWS::Pinpoint::PushTemplate.TemplateDescription``.
        '''
        props = CfnPushTemplateProps(
            template_name=template_name,
            adm=adm,
            apns=apns,
            baidu=baidu,
            default=default,
            default_substitutions=default_substitutions,
            gcm=gcm,
            tags=tags,
            template_description=template_description,
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
        '''``AWS::Pinpoint::PushTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> builtins.str:
        '''``AWS::Pinpoint::PushTemplate.TemplateName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatename
        '''
        return typing.cast(builtins.str, jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: builtins.str) -> None:
        jsii.set(self, "templateName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="adm")
    def adm(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]]:
        '''``AWS::Pinpoint::PushTemplate.ADM``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-adm
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]], jsii.get(self, "adm"))

    @adm.setter
    def adm(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]],
    ) -> None:
        jsii.set(self, "adm", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apns")
    def apns(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.APNSPushNotificationTemplateProperty"]]:
        '''``AWS::Pinpoint::PushTemplate.APNS``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-apns
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.APNSPushNotificationTemplateProperty"]], jsii.get(self, "apns"))

    @apns.setter
    def apns(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.APNSPushNotificationTemplateProperty"]],
    ) -> None:
        jsii.set(self, "apns", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="baidu")
    def baidu(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]]:
        '''``AWS::Pinpoint::PushTemplate.Baidu``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-baidu
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]], jsii.get(self, "baidu"))

    @baidu.setter
    def baidu(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]],
    ) -> None:
        jsii.set(self, "baidu", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="default")
    def default(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.DefaultPushNotificationTemplateProperty"]]:
        '''``AWS::Pinpoint::PushTemplate.Default``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-default
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.DefaultPushNotificationTemplateProperty"]], jsii.get(self, "default"))

    @default.setter
    def default(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.DefaultPushNotificationTemplateProperty"]],
    ) -> None:
        jsii.set(self, "default", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultSubstitutions")
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::PushTemplate.DefaultSubstitutions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-defaultsubstitutions
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSubstitutions"))

    @default_substitutions.setter
    def default_substitutions(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultSubstitutions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="gcm")
    def gcm(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]]:
        '''``AWS::Pinpoint::PushTemplate.GCM``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-gcm
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]], jsii.get(self, "gcm"))

    @gcm.setter
    def gcm(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnPushTemplate.AndroidPushNotificationTemplateProperty"]],
    ) -> None:
        jsii.set(self, "gcm", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateDescription")
    def template_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::PushTemplate.TemplateDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatedescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateDescription"))

    @template_description.setter
    def template_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateDescription", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnPushTemplate.APNSPushNotificationTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "body": "body",
            "media_url": "mediaUrl",
            "sound": "sound",
            "title": "title",
            "url": "url",
        },
    )
    class APNSPushNotificationTemplateProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            body: typing.Optional[builtins.str] = None,
            media_url: typing.Optional[builtins.str] = None,
            sound: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param action: ``CfnPushTemplate.APNSPushNotificationTemplateProperty.Action``.
            :param body: ``CfnPushTemplate.APNSPushNotificationTemplateProperty.Body``.
            :param media_url: ``CfnPushTemplate.APNSPushNotificationTemplateProperty.MediaUrl``.
            :param sound: ``CfnPushTemplate.APNSPushNotificationTemplateProperty.Sound``.
            :param title: ``CfnPushTemplate.APNSPushNotificationTemplateProperty.Title``.
            :param url: ``CfnPushTemplate.APNSPushNotificationTemplateProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if body is not None:
                self._values["body"] = body
            if media_url is not None:
                self._values["media_url"] = media_url
            if sound is not None:
                self._values["sound"] = sound
            if title is not None:
                self._values["title"] = title
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.APNSPushNotificationTemplateProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.APNSPushNotificationTemplateProperty.Body``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def media_url(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.APNSPushNotificationTemplateProperty.MediaUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-mediaurl
            '''
            result = self._values.get("media_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sound(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.APNSPushNotificationTemplateProperty.Sound``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-sound
            '''
            result = self._values.get("sound")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.APNSPushNotificationTemplateProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.APNSPushNotificationTemplateProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-apnspushnotificationtemplate.html#cfn-pinpoint-pushtemplate-apnspushnotificationtemplate-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "APNSPushNotificationTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnPushTemplate.AndroidPushNotificationTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "body": "body",
            "image_icon_url": "imageIconUrl",
            "image_url": "imageUrl",
            "small_image_icon_url": "smallImageIconUrl",
            "sound": "sound",
            "title": "title",
            "url": "url",
        },
    )
    class AndroidPushNotificationTemplateProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            body: typing.Optional[builtins.str] = None,
            image_icon_url: typing.Optional[builtins.str] = None,
            image_url: typing.Optional[builtins.str] = None,
            small_image_icon_url: typing.Optional[builtins.str] = None,
            sound: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param action: ``CfnPushTemplate.AndroidPushNotificationTemplateProperty.Action``.
            :param body: ``CfnPushTemplate.AndroidPushNotificationTemplateProperty.Body``.
            :param image_icon_url: ``CfnPushTemplate.AndroidPushNotificationTemplateProperty.ImageIconUrl``.
            :param image_url: ``CfnPushTemplate.AndroidPushNotificationTemplateProperty.ImageUrl``.
            :param small_image_icon_url: ``CfnPushTemplate.AndroidPushNotificationTemplateProperty.SmallImageIconUrl``.
            :param sound: ``CfnPushTemplate.AndroidPushNotificationTemplateProperty.Sound``.
            :param title: ``CfnPushTemplate.AndroidPushNotificationTemplateProperty.Title``.
            :param url: ``CfnPushTemplate.AndroidPushNotificationTemplateProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if body is not None:
                self._values["body"] = body
            if image_icon_url is not None:
                self._values["image_icon_url"] = image_icon_url
            if image_url is not None:
                self._values["image_url"] = image_url
            if small_image_icon_url is not None:
                self._values["small_image_icon_url"] = small_image_icon_url
            if sound is not None:
                self._values["sound"] = sound
            if title is not None:
                self._values["title"] = title
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.AndroidPushNotificationTemplateProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.AndroidPushNotificationTemplateProperty.Body``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_icon_url(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.AndroidPushNotificationTemplateProperty.ImageIconUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-imageiconurl
            '''
            result = self._values.get("image_icon_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def image_url(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.AndroidPushNotificationTemplateProperty.ImageUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-imageurl
            '''
            result = self._values.get("image_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def small_image_icon_url(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.AndroidPushNotificationTemplateProperty.SmallImageIconUrl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-smallimageiconurl
            '''
            result = self._values.get("small_image_icon_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sound(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.AndroidPushNotificationTemplateProperty.Sound``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-sound
            '''
            result = self._values.get("sound")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.AndroidPushNotificationTemplateProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.AndroidPushNotificationTemplateProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-androidpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-androidpushnotificationtemplate-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AndroidPushNotificationTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnPushTemplate.DefaultPushNotificationTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "body": "body",
            "sound": "sound",
            "title": "title",
            "url": "url",
        },
    )
    class DefaultPushNotificationTemplateProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            body: typing.Optional[builtins.str] = None,
            sound: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param action: ``CfnPushTemplate.DefaultPushNotificationTemplateProperty.Action``.
            :param body: ``CfnPushTemplate.DefaultPushNotificationTemplateProperty.Body``.
            :param sound: ``CfnPushTemplate.DefaultPushNotificationTemplateProperty.Sound``.
            :param title: ``CfnPushTemplate.DefaultPushNotificationTemplateProperty.Title``.
            :param url: ``CfnPushTemplate.DefaultPushNotificationTemplateProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if body is not None:
                self._values["body"] = body
            if sound is not None:
                self._values["sound"] = sound
            if title is not None:
                self._values["title"] = title
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.DefaultPushNotificationTemplateProperty.Action``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def body(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.DefaultPushNotificationTemplateProperty.Body``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-body
            '''
            result = self._values.get("body")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sound(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.DefaultPushNotificationTemplateProperty.Sound``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-sound
            '''
            result = self._values.get("sound")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.DefaultPushNotificationTemplateProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''``CfnPushTemplate.DefaultPushNotificationTemplateProperty.Url``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-pushtemplate-defaultpushnotificationtemplate.html#cfn-pinpoint-pushtemplate-defaultpushnotificationtemplate-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultPushNotificationTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnPushTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "template_name": "templateName",
        "adm": "adm",
        "apns": "apns",
        "baidu": "baidu",
        "default": "default",
        "default_substitutions": "defaultSubstitutions",
        "gcm": "gcm",
        "tags": "tags",
        "template_description": "templateDescription",
    },
)
class CfnPushTemplateProps:
    def __init__(
        self,
        *,
        template_name: builtins.str,
        adm: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.AndroidPushNotificationTemplateProperty]] = None,
        apns: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.APNSPushNotificationTemplateProperty]] = None,
        baidu: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.AndroidPushNotificationTemplateProperty]] = None,
        default: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.DefaultPushNotificationTemplateProperty]] = None,
        default_substitutions: typing.Optional[builtins.str] = None,
        gcm: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.AndroidPushNotificationTemplateProperty]] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::PushTemplate``.

        :param template_name: ``AWS::Pinpoint::PushTemplate.TemplateName``.
        :param adm: ``AWS::Pinpoint::PushTemplate.ADM``.
        :param apns: ``AWS::Pinpoint::PushTemplate.APNS``.
        :param baidu: ``AWS::Pinpoint::PushTemplate.Baidu``.
        :param default: ``AWS::Pinpoint::PushTemplate.Default``.
        :param default_substitutions: ``AWS::Pinpoint::PushTemplate.DefaultSubstitutions``.
        :param gcm: ``AWS::Pinpoint::PushTemplate.GCM``.
        :param tags: ``AWS::Pinpoint::PushTemplate.Tags``.
        :param template_description: ``AWS::Pinpoint::PushTemplate.TemplateDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "template_name": template_name,
        }
        if adm is not None:
            self._values["adm"] = adm
        if apns is not None:
            self._values["apns"] = apns
        if baidu is not None:
            self._values["baidu"] = baidu
        if default is not None:
            self._values["default"] = default
        if default_substitutions is not None:
            self._values["default_substitutions"] = default_substitutions
        if gcm is not None:
            self._values["gcm"] = gcm
        if tags is not None:
            self._values["tags"] = tags
        if template_description is not None:
            self._values["template_description"] = template_description

    @builtins.property
    def template_name(self) -> builtins.str:
        '''``AWS::Pinpoint::PushTemplate.TemplateName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatename
        '''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def adm(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.AndroidPushNotificationTemplateProperty]]:
        '''``AWS::Pinpoint::PushTemplate.ADM``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-adm
        '''
        result = self._values.get("adm")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.AndroidPushNotificationTemplateProperty]], result)

    @builtins.property
    def apns(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.APNSPushNotificationTemplateProperty]]:
        '''``AWS::Pinpoint::PushTemplate.APNS``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-apns
        '''
        result = self._values.get("apns")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.APNSPushNotificationTemplateProperty]], result)

    @builtins.property
    def baidu(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.AndroidPushNotificationTemplateProperty]]:
        '''``AWS::Pinpoint::PushTemplate.Baidu``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-baidu
        '''
        result = self._values.get("baidu")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.AndroidPushNotificationTemplateProperty]], result)

    @builtins.property
    def default(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.DefaultPushNotificationTemplateProperty]]:
        '''``AWS::Pinpoint::PushTemplate.Default``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-default
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.DefaultPushNotificationTemplateProperty]], result)

    @builtins.property
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::PushTemplate.DefaultSubstitutions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-defaultsubstitutions
        '''
        result = self._values.get("default_substitutions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gcm(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.AndroidPushNotificationTemplateProperty]]:
        '''``AWS::Pinpoint::PushTemplate.GCM``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-gcm
        '''
        result = self._values.get("gcm")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnPushTemplate.AndroidPushNotificationTemplateProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::Pinpoint::PushTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def template_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::PushTemplate.TemplateDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html#cfn-pinpoint-pushtemplate-templatedescription
        '''
        result = self._values.get("template_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPushTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSMSChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnSMSChannel",
):
    '''A CloudFormation ``AWS::Pinpoint::SMSChannel``.

    :cloudformationResource: AWS::Pinpoint::SMSChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        sender_id: typing.Optional[builtins.str] = None,
        short_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::SMSChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::SMSChannel.ApplicationId``.
        :param enabled: ``AWS::Pinpoint::SMSChannel.Enabled``.
        :param sender_id: ``AWS::Pinpoint::SMSChannel.SenderId``.
        :param short_code: ``AWS::Pinpoint::SMSChannel.ShortCode``.
        '''
        props = CfnSMSChannelProps(
            application_id=application_id,
            enabled=enabled,
            sender_id=sender_id,
            short_code=short_code,
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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::SMSChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::SMSChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enabled", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="senderId")
    def sender_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::SMSChannel.SenderId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-senderid
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "senderId"))

    @sender_id.setter
    def sender_id(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "senderId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="shortCode")
    def short_code(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::SMSChannel.ShortCode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-shortcode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shortCode"))

    @short_code.setter
    def short_code(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "shortCode", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnSMSChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "enabled": "enabled",
        "sender_id": "senderId",
        "short_code": "shortCode",
    },
)
class CfnSMSChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        sender_id: typing.Optional[builtins.str] = None,
        short_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::SMSChannel``.

        :param application_id: ``AWS::Pinpoint::SMSChannel.ApplicationId``.
        :param enabled: ``AWS::Pinpoint::SMSChannel.Enabled``.
        :param sender_id: ``AWS::Pinpoint::SMSChannel.SenderId``.
        :param short_code: ``AWS::Pinpoint::SMSChannel.ShortCode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if sender_id is not None:
            self._values["sender_id"] = sender_id
        if short_code is not None:
            self._values["short_code"] = short_code

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::SMSChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::SMSChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    @builtins.property
    def sender_id(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::SMSChannel.SenderId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-senderid
        '''
        result = self._values.get("sender_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def short_code(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::SMSChannel.ShortCode``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-shortcode
        '''
        result = self._values.get("short_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSMSChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSegment(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnSegment",
):
    '''A CloudFormation ``AWS::Pinpoint::Segment``.

    :cloudformationResource: AWS::Pinpoint::Segment
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        name: builtins.str,
        dimensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentDimensionsProperty"]] = None,
        segment_groups: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentGroupsProperty"]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::Segment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::Segment.ApplicationId``.
        :param name: ``AWS::Pinpoint::Segment.Name``.
        :param dimensions: ``AWS::Pinpoint::Segment.Dimensions``.
        :param segment_groups: ``AWS::Pinpoint::Segment.SegmentGroups``.
        :param tags: ``AWS::Pinpoint::Segment.Tags``.
        '''
        props = CfnSegmentProps(
            application_id=application_id,
            name=name,
            dimensions=dimensions,
            segment_groups=segment_groups,
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
    @jsii.member(jsii_name="attrSegmentId")
    def attr_segment_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: SegmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSegmentId"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::Pinpoint::Segment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::Segment.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''``AWS::Pinpoint::Segment.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        jsii.set(self, "name", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="dimensions")
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentDimensionsProperty"]]:
        '''``AWS::Pinpoint::Segment.Dimensions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-dimensions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentDimensionsProperty"]], jsii.get(self, "dimensions"))

    @dimensions.setter
    def dimensions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentDimensionsProperty"]],
    ) -> None:
        jsii.set(self, "dimensions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="segmentGroups")
    def segment_groups(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentGroupsProperty"]]:
        '''``AWS::Pinpoint::Segment.SegmentGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-segmentgroups
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentGroupsProperty"]], jsii.get(self, "segmentGroups"))

    @segment_groups.setter
    def segment_groups(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentGroupsProperty"]],
    ) -> None:
        jsii.set(self, "segmentGroups", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.AttributeDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"attribute_type": "attributeType", "values": "values"},
    )
    class AttributeDimensionProperty:
        def __init__(
            self,
            *,
            attribute_type: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param attribute_type: ``CfnSegment.AttributeDimensionProperty.AttributeType``.
            :param values: ``CfnSegment.AttributeDimensionProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attribute_type is not None:
                self._values["attribute_type"] = attribute_type
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def attribute_type(self) -> typing.Optional[builtins.str]:
            '''``CfnSegment.AttributeDimensionProperty.AttributeType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html#cfn-pinpoint-segment-attributedimension-attributetype
            '''
            result = self._values.get("attribute_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnSegment.AttributeDimensionProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-attributedimension.html#cfn-pinpoint-segment-attributedimension-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.BehaviorProperty",
        jsii_struct_bases=[],
        name_mapping={"recency": "recency"},
    )
    class BehaviorProperty:
        def __init__(
            self,
            *,
            recency: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.RecencyProperty"]] = None,
        ) -> None:
            '''
            :param recency: ``CfnSegment.BehaviorProperty.Recency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if recency is not None:
                self._values["recency"] = recency

        @builtins.property
        def recency(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.RecencyProperty"]]:
            '''``CfnSegment.BehaviorProperty.Recency``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency
            '''
            result = self._values.get("recency")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.RecencyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BehaviorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.CoordinatesProperty",
        jsii_struct_bases=[],
        name_mapping={"latitude": "latitude", "longitude": "longitude"},
    )
    class CoordinatesProperty:
        def __init__(self, *, latitude: jsii.Number, longitude: jsii.Number) -> None:
            '''
            :param latitude: ``CfnSegment.CoordinatesProperty.Latitude``.
            :param longitude: ``CfnSegment.CoordinatesProperty.Longitude``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "latitude": latitude,
                "longitude": longitude,
            }

        @builtins.property
        def latitude(self) -> jsii.Number:
            '''``CfnSegment.CoordinatesProperty.Latitude``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates-latitude
            '''
            result = self._values.get("latitude")
            assert result is not None, "Required property 'latitude' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def longitude(self) -> jsii.Number:
            '''``CfnSegment.CoordinatesProperty.Longitude``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates-longitude
            '''
            result = self._values.get("longitude")
            assert result is not None, "Required property 'longitude' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoordinatesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.DemographicProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_version": "appVersion",
            "channel": "channel",
            "device_type": "deviceType",
            "make": "make",
            "model": "model",
            "platform": "platform",
        },
    )
    class DemographicProperty:
        def __init__(
            self,
            *,
            app_version: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]] = None,
            channel: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]] = None,
            device_type: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]] = None,
            make: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]] = None,
            model: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]] = None,
            platform: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]] = None,
        ) -> None:
            '''
            :param app_version: ``CfnSegment.DemographicProperty.AppVersion``.
            :param channel: ``CfnSegment.DemographicProperty.Channel``.
            :param device_type: ``CfnSegment.DemographicProperty.DeviceType``.
            :param make: ``CfnSegment.DemographicProperty.Make``.
            :param model: ``CfnSegment.DemographicProperty.Model``.
            :param platform: ``CfnSegment.DemographicProperty.Platform``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if app_version is not None:
                self._values["app_version"] = app_version
            if channel is not None:
                self._values["channel"] = channel
            if device_type is not None:
                self._values["device_type"] = device_type
            if make is not None:
                self._values["make"] = make
            if model is not None:
                self._values["model"] = model
            if platform is not None:
                self._values["platform"] = platform

        @builtins.property
        def app_version(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]]:
            '''``CfnSegment.DemographicProperty.AppVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-appversion
            '''
            result = self._values.get("app_version")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def channel(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]]:
            '''``CfnSegment.DemographicProperty.Channel``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-channel
            '''
            result = self._values.get("channel")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def device_type(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]]:
            '''``CfnSegment.DemographicProperty.DeviceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-devicetype
            '''
            result = self._values.get("device_type")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def make(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]]:
            '''``CfnSegment.DemographicProperty.Make``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-make
            '''
            result = self._values.get("make")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def model(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]]:
            '''``CfnSegment.DemographicProperty.Model``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-model
            '''
            result = self._values.get("model")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def platform(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]]:
            '''``CfnSegment.DemographicProperty.Platform``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-demographic.html#cfn-pinpoint-segment-segmentdimensions-demographic-platform
            '''
            result = self._values.get("platform")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DemographicProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.GPSPointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "coordinates": "coordinates",
            "range_in_kilometers": "rangeInKilometers",
        },
    )
    class GPSPointProperty:
        def __init__(
            self,
            *,
            coordinates: typing.Union[aws_cdk.core.IResolvable, "CfnSegment.CoordinatesProperty"],
            range_in_kilometers: jsii.Number,
        ) -> None:
            '''
            :param coordinates: ``CfnSegment.GPSPointProperty.Coordinates``.
            :param range_in_kilometers: ``CfnSegment.GPSPointProperty.RangeInKilometers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "coordinates": coordinates,
                "range_in_kilometers": range_in_kilometers,
            }

        @builtins.property
        def coordinates(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnSegment.CoordinatesProperty"]:
            '''``CfnSegment.GPSPointProperty.Coordinates``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-coordinates
            '''
            result = self._values.get("coordinates")
            assert result is not None, "Required property 'coordinates' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnSegment.CoordinatesProperty"], result)

        @builtins.property
        def range_in_kilometers(self) -> jsii.Number:
            '''``CfnSegment.GPSPointProperty.RangeInKilometers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location-gpspoint.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint-rangeinkilometers
            '''
            result = self._values.get("range_in_kilometers")
            assert result is not None, "Required property 'range_in_kilometers' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GPSPointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.GroupsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dimensions": "dimensions",
            "source_segments": "sourceSegments",
            "source_type": "sourceType",
            "type": "type",
        },
    )
    class GroupsProperty:
        def __init__(
            self,
            *,
            dimensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentDimensionsProperty"]]]] = None,
            source_segments: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SourceSegmentsProperty"]]]] = None,
            source_type: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param dimensions: ``CfnSegment.GroupsProperty.Dimensions``.
            :param source_segments: ``CfnSegment.GroupsProperty.SourceSegments``.
            :param source_type: ``CfnSegment.GroupsProperty.SourceType``.
            :param type: ``CfnSegment.GroupsProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dimensions is not None:
                self._values["dimensions"] = dimensions
            if source_segments is not None:
                self._values["source_segments"] = source_segments
            if source_type is not None:
                self._values["source_type"] = source_type
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def dimensions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentDimensionsProperty"]]]]:
            '''``CfnSegment.GroupsProperty.Dimensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-dimensions
            '''
            result = self._values.get("dimensions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SegmentDimensionsProperty"]]]], result)

        @builtins.property
        def source_segments(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SourceSegmentsProperty"]]]]:
            '''``CfnSegment.GroupsProperty.SourceSegments``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments
            '''
            result = self._values.get("source_segments")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SourceSegmentsProperty"]]]], result)

        @builtins.property
        def source_type(self) -> typing.Optional[builtins.str]:
            '''``CfnSegment.GroupsProperty.SourceType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-sourcetype
            '''
            result = self._values.get("source_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''``CfnSegment.GroupsProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups.html#cfn-pinpoint-segment-segmentgroups-groups-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GroupsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"country": "country", "gps_point": "gpsPoint"},
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            country: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]] = None,
            gps_point: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.GPSPointProperty"]] = None,
        ) -> None:
            '''
            :param country: ``CfnSegment.LocationProperty.Country``.
            :param gps_point: ``CfnSegment.LocationProperty.GPSPoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if country is not None:
                self._values["country"] = country
            if gps_point is not None:
                self._values["gps_point"] = gps_point

        @builtins.property
        def country(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]]:
            '''``CfnSegment.LocationProperty.Country``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html#cfn-pinpoint-segment-segmentdimensions-location-country
            '''
            result = self._values.get("country")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.SetDimensionProperty"]], result)

        @builtins.property
        def gps_point(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.GPSPointProperty"]]:
            '''``CfnSegment.LocationProperty.GPSPoint``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-location.html#cfn-pinpoint-segment-segmentdimensions-location-gpspoint
            '''
            result = self._values.get("gps_point")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.GPSPointProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.RecencyProperty",
        jsii_struct_bases=[],
        name_mapping={"duration": "duration", "recency_type": "recencyType"},
    )
    class RecencyProperty:
        def __init__(
            self,
            *,
            duration: builtins.str,
            recency_type: builtins.str,
        ) -> None:
            '''
            :param duration: ``CfnSegment.RecencyProperty.Duration``.
            :param recency_type: ``CfnSegment.RecencyProperty.RecencyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "duration": duration,
                "recency_type": recency_type,
            }

        @builtins.property
        def duration(self) -> builtins.str:
            '''``CfnSegment.RecencyProperty.Duration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency-duration
            '''
            result = self._values.get("duration")
            assert result is not None, "Required property 'duration' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def recency_type(self) -> builtins.str:
            '''``CfnSegment.RecencyProperty.RecencyType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions-behavior-recency.html#cfn-pinpoint-segment-segmentdimensions-behavior-recency-recencytype
            '''
            result = self._values.get("recency_type")
            assert result is not None, "Required property 'recency_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.SegmentDimensionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attributes": "attributes",
            "behavior": "behavior",
            "demographic": "demographic",
            "location": "location",
            "metrics": "metrics",
            "user_attributes": "userAttributes",
        },
    )
    class SegmentDimensionsProperty:
        def __init__(
            self,
            *,
            attributes: typing.Any = None,
            behavior: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.BehaviorProperty"]] = None,
            demographic: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.DemographicProperty"]] = None,
            location: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.LocationProperty"]] = None,
            metrics: typing.Any = None,
            user_attributes: typing.Any = None,
        ) -> None:
            '''
            :param attributes: ``CfnSegment.SegmentDimensionsProperty.Attributes``.
            :param behavior: ``CfnSegment.SegmentDimensionsProperty.Behavior``.
            :param demographic: ``CfnSegment.SegmentDimensionsProperty.Demographic``.
            :param location: ``CfnSegment.SegmentDimensionsProperty.Location``.
            :param metrics: ``CfnSegment.SegmentDimensionsProperty.Metrics``.
            :param user_attributes: ``CfnSegment.SegmentDimensionsProperty.UserAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if attributes is not None:
                self._values["attributes"] = attributes
            if behavior is not None:
                self._values["behavior"] = behavior
            if demographic is not None:
                self._values["demographic"] = demographic
            if location is not None:
                self._values["location"] = location
            if metrics is not None:
                self._values["metrics"] = metrics
            if user_attributes is not None:
                self._values["user_attributes"] = user_attributes

        @builtins.property
        def attributes(self) -> typing.Any:
            '''``CfnSegment.SegmentDimensionsProperty.Attributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Any, result)

        @builtins.property
        def behavior(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.BehaviorProperty"]]:
            '''``CfnSegment.SegmentDimensionsProperty.Behavior``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-behavior
            '''
            result = self._values.get("behavior")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.BehaviorProperty"]], result)

        @builtins.property
        def demographic(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.DemographicProperty"]]:
            '''``CfnSegment.SegmentDimensionsProperty.Demographic``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-demographic
            '''
            result = self._values.get("demographic")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.DemographicProperty"]], result)

        @builtins.property
        def location(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.LocationProperty"]]:
            '''``CfnSegment.SegmentDimensionsProperty.Location``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-location
            '''
            result = self._values.get("location")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.LocationProperty"]], result)

        @builtins.property
        def metrics(self) -> typing.Any:
            '''``CfnSegment.SegmentDimensionsProperty.Metrics``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-metrics
            '''
            result = self._values.get("metrics")
            return typing.cast(typing.Any, result)

        @builtins.property
        def user_attributes(self) -> typing.Any:
            '''``CfnSegment.SegmentDimensionsProperty.UserAttributes``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentdimensions.html#cfn-pinpoint-segment-segmentdimensions-userattributes
            '''
            result = self._values.get("user_attributes")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SegmentDimensionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.SegmentGroupsProperty",
        jsii_struct_bases=[],
        name_mapping={"groups": "groups", "include": "include"},
    )
    class SegmentGroupsProperty:
        def __init__(
            self,
            *,
            groups: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.GroupsProperty"]]]] = None,
            include: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param groups: ``CfnSegment.SegmentGroupsProperty.Groups``.
            :param include: ``CfnSegment.SegmentGroupsProperty.Include``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if groups is not None:
                self._values["groups"] = groups
            if include is not None:
                self._values["include"] = include

        @builtins.property
        def groups(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.GroupsProperty"]]]]:
            '''``CfnSegment.SegmentGroupsProperty.Groups``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html#cfn-pinpoint-segment-segmentgroups-groups
            '''
            result = self._values.get("groups")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSegment.GroupsProperty"]]]], result)

        @builtins.property
        def include(self) -> typing.Optional[builtins.str]:
            '''``CfnSegment.SegmentGroupsProperty.Include``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups.html#cfn-pinpoint-segment-segmentgroups-include
            '''
            result = self._values.get("include")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SegmentGroupsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.SetDimensionProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_type": "dimensionType", "values": "values"},
    )
    class SetDimensionProperty:
        def __init__(
            self,
            *,
            dimension_type: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param dimension_type: ``CfnSegment.SetDimensionProperty.DimensionType``.
            :param values: ``CfnSegment.SetDimensionProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if dimension_type is not None:
                self._values["dimension_type"] = dimension_type
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def dimension_type(self) -> typing.Optional[builtins.str]:
            '''``CfnSegment.SetDimensionProperty.DimensionType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html#cfn-pinpoint-segment-setdimension-dimensiontype
            '''
            result = self._values.get("dimension_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''``CfnSegment.SetDimensionProperty.Values``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-setdimension.html#cfn-pinpoint-segment-setdimension-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SetDimensionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-pinpoint.CfnSegment.SourceSegmentsProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "version": "version"},
    )
    class SourceSegmentsProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            version: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param id: ``CfnSegment.SourceSegmentsProperty.Id``.
            :param version: ``CfnSegment.SourceSegmentsProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "id": id,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def id(self) -> builtins.str:
            '''``CfnSegment.SourceSegmentsProperty.Id``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> typing.Optional[jsii.Number]:
            '''``CfnSegment.SourceSegmentsProperty.Version``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-segment-segmentgroups-groups-sourcesegments.html#cfn-pinpoint-segment-segmentgroups-groups-sourcesegments-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceSegmentsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnSegmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "name": "name",
        "dimensions": "dimensions",
        "segment_groups": "segmentGroups",
        "tags": "tags",
    },
)
class CfnSegmentProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        name: builtins.str,
        dimensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSegment.SegmentDimensionsProperty]] = None,
        segment_groups: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSegment.SegmentGroupsProperty]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::Segment``.

        :param application_id: ``AWS::Pinpoint::Segment.ApplicationId``.
        :param name: ``AWS::Pinpoint::Segment.Name``.
        :param dimensions: ``AWS::Pinpoint::Segment.Dimensions``.
        :param segment_groups: ``AWS::Pinpoint::Segment.SegmentGroups``.
        :param tags: ``AWS::Pinpoint::Segment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "name": name,
        }
        if dimensions is not None:
            self._values["dimensions"] = dimensions
        if segment_groups is not None:
            self._values["segment_groups"] = segment_groups
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::Segment.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''``AWS::Pinpoint::Segment.Name``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimensions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSegment.SegmentDimensionsProperty]]:
        '''``AWS::Pinpoint::Segment.Dimensions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-dimensions
        '''
        result = self._values.get("dimensions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSegment.SegmentDimensionsProperty]], result)

    @builtins.property
    def segment_groups(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSegment.SegmentGroupsProperty]]:
        '''``AWS::Pinpoint::Segment.SegmentGroups``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-segmentgroups
        '''
        result = self._values.get("segment_groups")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnSegment.SegmentGroupsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::Pinpoint::Segment.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html#cfn-pinpoint-segment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSegmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnSmsTemplate(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnSmsTemplate",
):
    '''A CloudFormation ``AWS::Pinpoint::SmsTemplate``.

    :cloudformationResource: AWS::Pinpoint::SmsTemplate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        body: builtins.str,
        template_name: builtins.str,
        default_substitutions: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::SmsTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param body: ``AWS::Pinpoint::SmsTemplate.Body``.
        :param template_name: ``AWS::Pinpoint::SmsTemplate.TemplateName``.
        :param default_substitutions: ``AWS::Pinpoint::SmsTemplate.DefaultSubstitutions``.
        :param tags: ``AWS::Pinpoint::SmsTemplate.Tags``.
        :param template_description: ``AWS::Pinpoint::SmsTemplate.TemplateDescription``.
        '''
        props = CfnSmsTemplateProps(
            body=body,
            template_name=template_name,
            default_substitutions=default_substitutions,
            tags=tags,
            template_description=template_description,
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
        '''``AWS::Pinpoint::SmsTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        '''``AWS::Pinpoint::SmsTemplate.Body``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-body
        '''
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        jsii.set(self, "body", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> builtins.str:
        '''``AWS::Pinpoint::SmsTemplate.TemplateName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatename
        '''
        return typing.cast(builtins.str, jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: builtins.str) -> None:
        jsii.set(self, "templateName", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="defaultSubstitutions")
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::SmsTemplate.DefaultSubstitutions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-defaultsubstitutions
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSubstitutions"))

    @default_substitutions.setter
    def default_substitutions(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "defaultSubstitutions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateDescription")
    def template_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::SmsTemplate.TemplateDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatedescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateDescription"))

    @template_description.setter
    def template_description(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateDescription", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnSmsTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "body": "body",
        "template_name": "templateName",
        "default_substitutions": "defaultSubstitutions",
        "tags": "tags",
        "template_description": "templateDescription",
    },
)
class CfnSmsTemplateProps:
    def __init__(
        self,
        *,
        body: builtins.str,
        template_name: builtins.str,
        default_substitutions: typing.Optional[builtins.str] = None,
        tags: typing.Any = None,
        template_description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::SmsTemplate``.

        :param body: ``AWS::Pinpoint::SmsTemplate.Body``.
        :param template_name: ``AWS::Pinpoint::SmsTemplate.TemplateName``.
        :param default_substitutions: ``AWS::Pinpoint::SmsTemplate.DefaultSubstitutions``.
        :param tags: ``AWS::Pinpoint::SmsTemplate.Tags``.
        :param template_description: ``AWS::Pinpoint::SmsTemplate.TemplateDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "body": body,
            "template_name": template_name,
        }
        if default_substitutions is not None:
            self._values["default_substitutions"] = default_substitutions
        if tags is not None:
            self._values["tags"] = tags
        if template_description is not None:
            self._values["template_description"] = template_description

    @builtins.property
    def body(self) -> builtins.str:
        '''``AWS::Pinpoint::SmsTemplate.Body``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-body
        '''
        result = self._values.get("body")
        assert result is not None, "Required property 'body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_name(self) -> builtins.str:
        '''``AWS::Pinpoint::SmsTemplate.TemplateName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatename
        '''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_substitutions(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::SmsTemplate.DefaultSubstitutions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-defaultsubstitutions
        '''
        result = self._values.get("default_substitutions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''``AWS::Pinpoint::SmsTemplate.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    @builtins.property
    def template_description(self) -> typing.Optional[builtins.str]:
        '''``AWS::Pinpoint::SmsTemplate.TemplateDescription``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html#cfn-pinpoint-smstemplate-templatedescription
        '''
        result = self._values.get("template_description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSmsTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnVoiceChannel(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-pinpoint.CfnVoiceChannel",
):
    '''A CloudFormation ``AWS::Pinpoint::VoiceChannel``.

    :cloudformationResource: AWS::Pinpoint::VoiceChannel
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Create a new ``AWS::Pinpoint::VoiceChannel``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param application_id: ``AWS::Pinpoint::VoiceChannel.ApplicationId``.
        :param enabled: ``AWS::Pinpoint::VoiceChannel.Enabled``.
        '''
        props = CfnVoiceChannelProps(application_id=application_id, enabled=enabled)

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
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::VoiceChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-applicationid
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        jsii.set(self, "applicationId", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::VoiceChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-enabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]],
    ) -> None:
        jsii.set(self, "enabled", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-pinpoint.CfnVoiceChannelProps",
    jsii_struct_bases=[],
    name_mapping={"application_id": "applicationId", "enabled": "enabled"},
)
class CfnVoiceChannelProps:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::Pinpoint::VoiceChannel``.

        :param application_id: ``AWS::Pinpoint::VoiceChannel.ApplicationId``.
        :param enabled: ``AWS::Pinpoint::VoiceChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def application_id(self) -> builtins.str:
        '''``AWS::Pinpoint::VoiceChannel.ApplicationId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-applicationid
        '''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
        '''``AWS::Pinpoint::VoiceChannel.Enabled``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html#cfn-pinpoint-voicechannel-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVoiceChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnADMChannel",
    "CfnADMChannelProps",
    "CfnAPNSChannel",
    "CfnAPNSChannelProps",
    "CfnAPNSSandboxChannel",
    "CfnAPNSSandboxChannelProps",
    "CfnAPNSVoipChannel",
    "CfnAPNSVoipChannelProps",
    "CfnAPNSVoipSandboxChannel",
    "CfnAPNSVoipSandboxChannelProps",
    "CfnApp",
    "CfnAppProps",
    "CfnApplicationSettings",
    "CfnApplicationSettingsProps",
    "CfnBaiduChannel",
    "CfnBaiduChannelProps",
    "CfnCampaign",
    "CfnCampaignProps",
    "CfnEmailChannel",
    "CfnEmailChannelProps",
    "CfnEmailTemplate",
    "CfnEmailTemplateProps",
    "CfnEventStream",
    "CfnEventStreamProps",
    "CfnGCMChannel",
    "CfnGCMChannelProps",
    "CfnPushTemplate",
    "CfnPushTemplateProps",
    "CfnSMSChannel",
    "CfnSMSChannelProps",
    "CfnSegment",
    "CfnSegmentProps",
    "CfnSmsTemplate",
    "CfnSmsTemplateProps",
    "CfnVoiceChannel",
    "CfnVoiceChannelProps",
]

publication.publish()
