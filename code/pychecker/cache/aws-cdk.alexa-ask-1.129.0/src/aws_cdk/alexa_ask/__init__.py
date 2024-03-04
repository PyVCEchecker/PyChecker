'''
# Alexa Skills Kit Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.alexa_ask as alexa_ask
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
class CfnSkill(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/alexa-ask.CfnSkill",
):
    '''A CloudFormation ``Alexa::ASK::Skill``.

    :cloudformationResource: Alexa::ASK::Skill
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        authentication_configuration: typing.Union["CfnSkill.AuthenticationConfigurationProperty", aws_cdk.core.IResolvable],
        skill_package: typing.Union[aws_cdk.core.IResolvable, "CfnSkill.SkillPackageProperty"],
        vendor_id: builtins.str,
    ) -> None:
        '''Create a new ``Alexa::ASK::Skill``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param authentication_configuration: ``Alexa::ASK::Skill.AuthenticationConfiguration``.
        :param skill_package: ``Alexa::ASK::Skill.SkillPackage``.
        :param vendor_id: ``Alexa::ASK::Skill.VendorId``.
        '''
        props = CfnSkillProps(
            authentication_configuration=authentication_configuration,
            skill_package=skill_package,
            vendor_id=vendor_id,
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
    @jsii.member(jsii_name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> typing.Union["CfnSkill.AuthenticationConfigurationProperty", aws_cdk.core.IResolvable]:
        '''``Alexa::ASK::Skill.AuthenticationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-authenticationconfiguration
        '''
        return typing.cast(typing.Union["CfnSkill.AuthenticationConfigurationProperty", aws_cdk.core.IResolvable], jsii.get(self, "authenticationConfiguration"))

    @authentication_configuration.setter
    def authentication_configuration(
        self,
        value: typing.Union["CfnSkill.AuthenticationConfigurationProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "authenticationConfiguration", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="skillPackage")
    def skill_package(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnSkill.SkillPackageProperty"]:
        '''``Alexa::ASK::Skill.SkillPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-skillpackage
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnSkill.SkillPackageProperty"], jsii.get(self, "skillPackage"))

    @skill_package.setter
    def skill_package(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnSkill.SkillPackageProperty"],
    ) -> None:
        jsii.set(self, "skillPackage", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="vendorId")
    def vendor_id(self) -> builtins.str:
        '''``Alexa::ASK::Skill.VendorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-vendorid
        '''
        return typing.cast(builtins.str, jsii.get(self, "vendorId"))

    @vendor_id.setter
    def vendor_id(self, value: builtins.str) -> None:
        jsii.set(self, "vendorId", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/alexa-ask.CfnSkill.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "refresh_token": "refreshToken",
        },
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            client_id: builtins.str,
            client_secret: builtins.str,
            refresh_token: builtins.str,
        ) -> None:
            '''
            :param client_id: ``CfnSkill.AuthenticationConfigurationProperty.ClientId``.
            :param client_secret: ``CfnSkill.AuthenticationConfigurationProperty.ClientSecret``.
            :param refresh_token: ``CfnSkill.AuthenticationConfigurationProperty.RefreshToken``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
            }

        @builtins.property
        def client_id(self) -> builtins.str:
            '''``CfnSkill.AuthenticationConfigurationProperty.ClientId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-clientid
            '''
            result = self._values.get("client_id")
            assert result is not None, "Required property 'client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_secret(self) -> builtins.str:
            '''``CfnSkill.AuthenticationConfigurationProperty.ClientSecret``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-clientsecret
            '''
            result = self._values.get("client_secret")
            assert result is not None, "Required property 'client_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def refresh_token(self) -> builtins.str:
            '''``CfnSkill.AuthenticationConfigurationProperty.RefreshToken``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-refreshtoken
            '''
            result = self._values.get("refresh_token")
            assert result is not None, "Required property 'refresh_token' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/alexa-ask.CfnSkill.OverridesProperty",
        jsii_struct_bases=[],
        name_mapping={"manifest": "manifest"},
    )
    class OverridesProperty:
        def __init__(self, *, manifest: typing.Any = None) -> None:
            '''
            :param manifest: ``CfnSkill.OverridesProperty.Manifest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if manifest is not None:
                self._values["manifest"] = manifest

        @builtins.property
        def manifest(self) -> typing.Any:
            '''``CfnSkill.OverridesProperty.Manifest``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html#cfn-ask-skill-overrides-manifest
            '''
            result = self._values.get("manifest")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/alexa-ask.CfnSkill.SkillPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket": "s3Bucket",
            "s3_key": "s3Key",
            "overrides": "overrides",
            "s3_bucket_role": "s3BucketRole",
            "s3_object_version": "s3ObjectVersion",
        },
    )
    class SkillPackageProperty:
        def __init__(
            self,
            *,
            s3_bucket: builtins.str,
            s3_key: builtins.str,
            overrides: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSkill.OverridesProperty"]] = None,
            s3_bucket_role: typing.Optional[builtins.str] = None,
            s3_object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param s3_bucket: ``CfnSkill.SkillPackageProperty.S3Bucket``.
            :param s3_key: ``CfnSkill.SkillPackageProperty.S3Key``.
            :param overrides: ``CfnSkill.SkillPackageProperty.Overrides``.
            :param s3_bucket_role: ``CfnSkill.SkillPackageProperty.S3BucketRole``.
            :param s3_object_version: ``CfnSkill.SkillPackageProperty.S3ObjectVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "s3_bucket": s3_bucket,
                "s3_key": s3_key,
            }
            if overrides is not None:
                self._values["overrides"] = overrides
            if s3_bucket_role is not None:
                self._values["s3_bucket_role"] = s3_bucket_role
            if s3_object_version is not None:
                self._values["s3_object_version"] = s3_object_version

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''``CfnSkill.SkillPackageProperty.S3Bucket``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key(self) -> builtins.str:
            '''``CfnSkill.SkillPackageProperty.S3Key``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3key
            '''
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def overrides(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSkill.OverridesProperty"]]:
            '''``CfnSkill.SkillPackageProperty.Overrides``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-overrides
            '''
            result = self._values.get("overrides")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnSkill.OverridesProperty"]], result)

        @builtins.property
        def s3_bucket_role(self) -> typing.Optional[builtins.str]:
            '''``CfnSkill.SkillPackageProperty.S3BucketRole``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3bucketrole
            '''
            result = self._values.get("s3_bucket_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_object_version(self) -> typing.Optional[builtins.str]:
            '''``CfnSkill.SkillPackageProperty.S3ObjectVersion``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3objectversion
            '''
            result = self._values.get("s3_object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SkillPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/alexa-ask.CfnSkillProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_configuration": "authenticationConfiguration",
        "skill_package": "skillPackage",
        "vendor_id": "vendorId",
    },
)
class CfnSkillProps:
    def __init__(
        self,
        *,
        authentication_configuration: typing.Union[CfnSkill.AuthenticationConfigurationProperty, aws_cdk.core.IResolvable],
        skill_package: typing.Union[aws_cdk.core.IResolvable, CfnSkill.SkillPackageProperty],
        vendor_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``Alexa::ASK::Skill``.

        :param authentication_configuration: ``Alexa::ASK::Skill.AuthenticationConfiguration``.
        :param skill_package: ``Alexa::ASK::Skill.SkillPackage``.
        :param vendor_id: ``Alexa::ASK::Skill.VendorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "authentication_configuration": authentication_configuration,
            "skill_package": skill_package,
            "vendor_id": vendor_id,
        }

    @builtins.property
    def authentication_configuration(
        self,
    ) -> typing.Union[CfnSkill.AuthenticationConfigurationProperty, aws_cdk.core.IResolvable]:
        '''``Alexa::ASK::Skill.AuthenticationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-authenticationconfiguration
        '''
        result = self._values.get("authentication_configuration")
        assert result is not None, "Required property 'authentication_configuration' is missing"
        return typing.cast(typing.Union[CfnSkill.AuthenticationConfigurationProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def skill_package(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnSkill.SkillPackageProperty]:
        '''``Alexa::ASK::Skill.SkillPackage``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-skillpackage
        '''
        result = self._values.get("skill_package")
        assert result is not None, "Required property 'skill_package' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnSkill.SkillPackageProperty], result)

    @builtins.property
    def vendor_id(self) -> builtins.str:
        '''``Alexa::ASK::Skill.VendorId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-vendorid
        '''
        result = self._values.get("vendor_id")
        assert result is not None, "Required property 'vendor_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSkillProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSkill",
    "CfnSkillProps",
]

publication.publish()
