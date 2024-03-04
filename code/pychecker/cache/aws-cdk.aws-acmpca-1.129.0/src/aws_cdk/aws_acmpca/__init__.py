'''
# AWS::ACMPCA Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
# Example automatically generated. See https://github.com/aws/jsii/issues/826
import aws_cdk.aws_acmpca as acmpca
```

## Certificate Authority

This package contains a `CertificateAuthority` class.
At the moment, you cannot create new Authorities using it,
but you can import existing ones using the `fromCertificateAuthorityArn` static method:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
certificate_authority = acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CA", "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/023077d8-2bfa-4eb0-8f22-05c96deade77")
```

## Low-level `Cfn*` classes

You can always use the low-level classes
(starting with `Cfn*`) to create resources like the Certificate Authority:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
cfn_certificate_authority = acmpca.CfnCertificateAuthority(self, "CA",
    type="ROOT",
    key_algorithm="RSA_2048",
    signing_algorithm="SHA256WITHRSA",
    subject={
        "country": "US",
        "organization": "string",
        "organizational_unit": "string",
        "distinguished_name_qualifier": "string",
        "state": "string",
        "common_name": "123",
        "serial_number": "string",
        "locality": "string",
        "title": "string",
        "surname": "string",
        "given_name": "string",
        "initials": "DG",
        "pseudonym": "string",
        "generation_qualifier": "DBG"
    }
)
```

If you need to pass the higher-level `ICertificateAuthority` somewhere,
you can get it from the lower-level `CfnCertificateAuthority` using the same `fromCertificateAuthorityArn` method:

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
certificate_authority = acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CertificateAuthority", cfn_certificate_authority.attr_arn)
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
import constructs


class CertificateAuthority(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-acmpca.CertificateAuthority",
):
    '''Defines a Certificate for ACMPCA.

    :resource: AWS::ACMPCA::CertificateAuthority
    '''

    @jsii.member(jsii_name="fromCertificateAuthorityArn") # type: ignore[misc]
    @builtins.classmethod
    def from_certificate_authority_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        certificate_authority_arn: builtins.str,
    ) -> "ICertificateAuthority":
        '''Import an existing Certificate given an ARN.

        :param scope: -
        :param id: -
        :param certificate_authority_arn: -
        '''
        return typing.cast("ICertificateAuthority", jsii.sinvoke(cls, "fromCertificateAuthorityArn", [scope, id, certificate_authority_arn]))


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCertificate(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-acmpca.CfnCertificate",
):
    '''A CloudFormation ``AWS::ACMPCA::Certificate``.

    :cloudformationResource: AWS::ACMPCA::Certificate
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        certificate_authority_arn: builtins.str,
        certificate_signing_request: builtins.str,
        signing_algorithm: builtins.str,
        validity: typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ValidityProperty"],
        api_passthrough: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ApiPassthroughProperty"]] = None,
        template_arn: typing.Optional[builtins.str] = None,
        validity_not_before: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ValidityProperty"]] = None,
    ) -> None:
        '''Create a new ``AWS::ACMPCA::Certificate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param certificate_authority_arn: ``AWS::ACMPCA::Certificate.CertificateAuthorityArn``.
        :param certificate_signing_request: ``AWS::ACMPCA::Certificate.CertificateSigningRequest``.
        :param signing_algorithm: ``AWS::ACMPCA::Certificate.SigningAlgorithm``.
        :param validity: ``AWS::ACMPCA::Certificate.Validity``.
        :param api_passthrough: ``AWS::ACMPCA::Certificate.ApiPassthrough``.
        :param template_arn: ``AWS::ACMPCA::Certificate.TemplateArn``.
        :param validity_not_before: ``AWS::ACMPCA::Certificate.ValidityNotBefore``.
        '''
        props = CfnCertificateProps(
            certificate_authority_arn=certificate_authority_arn,
            certificate_signing_request=certificate_signing_request,
            signing_algorithm=signing_algorithm,
            validity=validity,
            api_passthrough=api_passthrough,
            template_arn=template_arn,
            validity_not_before=validity_not_before,
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
    @jsii.member(jsii_name="attrCertificate")
    def attr_certificate(self) -> builtins.str:
        '''
        :cloudformationAttribute: Certificate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCertificate"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''``AWS::ACMPCA::Certificate.CertificateAuthorityArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-certificateauthorityarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: builtins.str) -> None:
        jsii.set(self, "certificateAuthorityArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificateSigningRequest")
    def certificate_signing_request(self) -> builtins.str:
        '''``AWS::ACMPCA::Certificate.CertificateSigningRequest``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-certificatesigningrequest
        '''
        return typing.cast(builtins.str, jsii.get(self, "certificateSigningRequest"))

    @certificate_signing_request.setter
    def certificate_signing_request(self, value: builtins.str) -> None:
        jsii.set(self, "certificateSigningRequest", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="signingAlgorithm")
    def signing_algorithm(self) -> builtins.str:
        '''``AWS::ACMPCA::Certificate.SigningAlgorithm``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-signingalgorithm
        '''
        return typing.cast(builtins.str, jsii.get(self, "signingAlgorithm"))

    @signing_algorithm.setter
    def signing_algorithm(self, value: builtins.str) -> None:
        jsii.set(self, "signingAlgorithm", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="validity")
    def validity(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ValidityProperty"]:
        '''``AWS::ACMPCA::Certificate.Validity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-validity
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ValidityProperty"], jsii.get(self, "validity"))

    @validity.setter
    def validity(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ValidityProperty"],
    ) -> None:
        jsii.set(self, "validity", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="apiPassthrough")
    def api_passthrough(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ApiPassthroughProperty"]]:
        '''``AWS::ACMPCA::Certificate.ApiPassthrough``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-apipassthrough
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ApiPassthroughProperty"]], jsii.get(self, "apiPassthrough"))

    @api_passthrough.setter
    def api_passthrough(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ApiPassthroughProperty"]],
    ) -> None:
        jsii.set(self, "apiPassthrough", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="templateArn")
    def template_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ACMPCA::Certificate.TemplateArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-templatearn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateArn"))

    @template_arn.setter
    def template_arn(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "templateArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="validityNotBefore")
    def validity_not_before(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ValidityProperty"]]:
        '''``AWS::ACMPCA::Certificate.ValidityNotBefore``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-validitynotbefore
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ValidityProperty"]], jsii.get(self, "validityNotBefore"))

    @validity_not_before.setter
    def validity_not_before(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ValidityProperty"]],
    ) -> None:
        jsii.set(self, "validityNotBefore", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.ApiPassthroughProperty",
        jsii_struct_bases=[],
        name_mapping={"extensions": "extensions", "subject": "subject"},
    )
    class ApiPassthroughProperty:
        def __init__(
            self,
            *,
            extensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ExtensionsProperty"]] = None,
            subject: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.SubjectProperty"]] = None,
        ) -> None:
            '''
            :param extensions: ``CfnCertificate.ApiPassthroughProperty.Extensions``.
            :param subject: ``CfnCertificate.ApiPassthroughProperty.Subject``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if extensions is not None:
                self._values["extensions"] = extensions
            if subject is not None:
                self._values["subject"] = subject

        @builtins.property
        def extensions(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ExtensionsProperty"]]:
            '''``CfnCertificate.ApiPassthroughProperty.Extensions``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html#cfn-acmpca-certificate-apipassthrough-extensions
            '''
            result = self._values.get("extensions")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ExtensionsProperty"]], result)

        @builtins.property
        def subject(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.SubjectProperty"]]:
            '''``CfnCertificate.ApiPassthroughProperty.Subject``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-apipassthrough.html#cfn-acmpca-certificate-apipassthrough-subject
            '''
            result = self._values.get("subject")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.SubjectProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiPassthroughProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.EdiPartyNameProperty",
        jsii_struct_bases=[],
        name_mapping={"name_assigner": "nameAssigner", "party_name": "partyName"},
    )
    class EdiPartyNameProperty:
        def __init__(
            self,
            *,
            name_assigner: builtins.str,
            party_name: builtins.str,
        ) -> None:
            '''
            :param name_assigner: ``CfnCertificate.EdiPartyNameProperty.NameAssigner``.
            :param party_name: ``CfnCertificate.EdiPartyNameProperty.PartyName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-edipartyname.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name_assigner": name_assigner,
                "party_name": party_name,
            }

        @builtins.property
        def name_assigner(self) -> builtins.str:
            '''``CfnCertificate.EdiPartyNameProperty.NameAssigner``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-edipartyname.html#cfn-acmpca-certificate-edipartyname-nameassigner
            '''
            result = self._values.get("name_assigner")
            assert result is not None, "Required property 'name_assigner' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def party_name(self) -> builtins.str:
            '''``CfnCertificate.EdiPartyNameProperty.PartyName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-edipartyname.html#cfn-acmpca-certificate-edipartyname-partyname
            '''
            result = self._values.get("party_name")
            assert result is not None, "Required property 'party_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdiPartyNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.ExtendedKeyUsageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "extended_key_usage_object_identifier": "extendedKeyUsageObjectIdentifier",
            "extended_key_usage_type": "extendedKeyUsageType",
        },
    )
    class ExtendedKeyUsageProperty:
        def __init__(
            self,
            *,
            extended_key_usage_object_identifier: typing.Optional[builtins.str] = None,
            extended_key_usage_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param extended_key_usage_object_identifier: ``CfnCertificate.ExtendedKeyUsageProperty.ExtendedKeyUsageObjectIdentifier``.
            :param extended_key_usage_type: ``CfnCertificate.ExtendedKeyUsageProperty.ExtendedKeyUsageType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if extended_key_usage_object_identifier is not None:
                self._values["extended_key_usage_object_identifier"] = extended_key_usage_object_identifier
            if extended_key_usage_type is not None:
                self._values["extended_key_usage_type"] = extended_key_usage_type

        @builtins.property
        def extended_key_usage_object_identifier(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.ExtendedKeyUsageProperty.ExtendedKeyUsageObjectIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html#cfn-acmpca-certificate-extendedkeyusage-extendedkeyusageobjectidentifier
            '''
            result = self._values.get("extended_key_usage_object_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def extended_key_usage_type(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.ExtendedKeyUsageProperty.ExtendedKeyUsageType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extendedkeyusage.html#cfn-acmpca-certificate-extendedkeyusage-extendedkeyusagetype
            '''
            result = self._values.get("extended_key_usage_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtendedKeyUsageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.ExtensionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_policies": "certificatePolicies",
            "extended_key_usage": "extendedKeyUsage",
            "key_usage": "keyUsage",
            "subject_alternative_names": "subjectAlternativeNames",
        },
    )
    class ExtensionsProperty:
        def __init__(
            self,
            *,
            certificate_policies: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.PolicyInformationProperty"]]]] = None,
            extended_key_usage: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ExtendedKeyUsageProperty"]]]] = None,
            key_usage: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.KeyUsageProperty"]] = None,
            subject_alternative_names: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.GeneralNameProperty"]]]] = None,
        ) -> None:
            '''
            :param certificate_policies: ``CfnCertificate.ExtensionsProperty.CertificatePolicies``.
            :param extended_key_usage: ``CfnCertificate.ExtensionsProperty.ExtendedKeyUsage``.
            :param key_usage: ``CfnCertificate.ExtensionsProperty.KeyUsage``.
            :param subject_alternative_names: ``CfnCertificate.ExtensionsProperty.SubjectAlternativeNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if certificate_policies is not None:
                self._values["certificate_policies"] = certificate_policies
            if extended_key_usage is not None:
                self._values["extended_key_usage"] = extended_key_usage
            if key_usage is not None:
                self._values["key_usage"] = key_usage
            if subject_alternative_names is not None:
                self._values["subject_alternative_names"] = subject_alternative_names

        @builtins.property
        def certificate_policies(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.PolicyInformationProperty"]]]]:
            '''``CfnCertificate.ExtensionsProperty.CertificatePolicies``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-certificatepolicies
            '''
            result = self._values.get("certificate_policies")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.PolicyInformationProperty"]]]], result)

        @builtins.property
        def extended_key_usage(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ExtendedKeyUsageProperty"]]]]:
            '''``CfnCertificate.ExtensionsProperty.ExtendedKeyUsage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-extendedkeyusage
            '''
            result = self._values.get("extended_key_usage")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.ExtendedKeyUsageProperty"]]]], result)

        @builtins.property
        def key_usage(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.KeyUsageProperty"]]:
            '''``CfnCertificate.ExtensionsProperty.KeyUsage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-keyusage
            '''
            result = self._values.get("key_usage")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.KeyUsageProperty"]], result)

        @builtins.property
        def subject_alternative_names(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.GeneralNameProperty"]]]]:
            '''``CfnCertificate.ExtensionsProperty.SubjectAlternativeNames``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-extensions.html#cfn-acmpca-certificate-extensions-subjectalternativenames
            '''
            result = self._values.get("subject_alternative_names")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.GeneralNameProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtensionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.GeneralNameProperty",
        jsii_struct_bases=[],
        name_mapping={
            "directory_name": "directoryName",
            "dns_name": "dnsName",
            "edi_party_name": "ediPartyName",
            "ip_address": "ipAddress",
            "other_name": "otherName",
            "registered_id": "registeredId",
            "rfc822_name": "rfc822Name",
            "uniform_resource_identifier": "uniformResourceIdentifier",
        },
    )
    class GeneralNameProperty:
        def __init__(
            self,
            *,
            directory_name: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.SubjectProperty"]] = None,
            dns_name: typing.Optional[builtins.str] = None,
            edi_party_name: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.EdiPartyNameProperty"]] = None,
            ip_address: typing.Optional[builtins.str] = None,
            other_name: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.OtherNameProperty"]] = None,
            registered_id: typing.Optional[builtins.str] = None,
            rfc822_name: typing.Optional[builtins.str] = None,
            uniform_resource_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param directory_name: ``CfnCertificate.GeneralNameProperty.DirectoryName``.
            :param dns_name: ``CfnCertificate.GeneralNameProperty.DnsName``.
            :param edi_party_name: ``CfnCertificate.GeneralNameProperty.EdiPartyName``.
            :param ip_address: ``CfnCertificate.GeneralNameProperty.IpAddress``.
            :param other_name: ``CfnCertificate.GeneralNameProperty.OtherName``.
            :param registered_id: ``CfnCertificate.GeneralNameProperty.RegisteredId``.
            :param rfc822_name: ``CfnCertificate.GeneralNameProperty.Rfc822Name``.
            :param uniform_resource_identifier: ``CfnCertificate.GeneralNameProperty.UniformResourceIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if directory_name is not None:
                self._values["directory_name"] = directory_name
            if dns_name is not None:
                self._values["dns_name"] = dns_name
            if edi_party_name is not None:
                self._values["edi_party_name"] = edi_party_name
            if ip_address is not None:
                self._values["ip_address"] = ip_address
            if other_name is not None:
                self._values["other_name"] = other_name
            if registered_id is not None:
                self._values["registered_id"] = registered_id
            if rfc822_name is not None:
                self._values["rfc822_name"] = rfc822_name
            if uniform_resource_identifier is not None:
                self._values["uniform_resource_identifier"] = uniform_resource_identifier

        @builtins.property
        def directory_name(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.SubjectProperty"]]:
            '''``CfnCertificate.GeneralNameProperty.DirectoryName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-directoryname
            '''
            result = self._values.get("directory_name")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.SubjectProperty"]], result)

        @builtins.property
        def dns_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.GeneralNameProperty.DnsName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-dnsname
            '''
            result = self._values.get("dns_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def edi_party_name(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.EdiPartyNameProperty"]]:
            '''``CfnCertificate.GeneralNameProperty.EdiPartyName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-edipartyname
            '''
            result = self._values.get("edi_party_name")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.EdiPartyNameProperty"]], result)

        @builtins.property
        def ip_address(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.GeneralNameProperty.IpAddress``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-ipaddress
            '''
            result = self._values.get("ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def other_name(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.OtherNameProperty"]]:
            '''``CfnCertificate.GeneralNameProperty.OtherName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-othername
            '''
            result = self._values.get("other_name")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.OtherNameProperty"]], result)

        @builtins.property
        def registered_id(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.GeneralNameProperty.RegisteredId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-registeredid
            '''
            result = self._values.get("registered_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rfc822_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.GeneralNameProperty.Rfc822Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-rfc822name
            '''
            result = self._values.get("rfc822_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uniform_resource_identifier(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.GeneralNameProperty.UniformResourceIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-generalname.html#cfn-acmpca-certificate-generalname-uniformresourceidentifier
            '''
            result = self._values.get("uniform_resource_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeneralNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.KeyUsageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crl_sign": "crlSign",
            "data_encipherment": "dataEncipherment",
            "decipher_only": "decipherOnly",
            "digital_signature": "digitalSignature",
            "encipher_only": "encipherOnly",
            "key_agreement": "keyAgreement",
            "key_cert_sign": "keyCertSign",
            "key_encipherment": "keyEncipherment",
            "non_repudiation": "nonRepudiation",
        },
    )
    class KeyUsageProperty:
        def __init__(
            self,
            *,
            crl_sign: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            data_encipherment: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            decipher_only: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            digital_signature: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            encipher_only: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            key_agreement: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            key_cert_sign: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            key_encipherment: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            non_repudiation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param crl_sign: ``CfnCertificate.KeyUsageProperty.CRLSign``.
            :param data_encipherment: ``CfnCertificate.KeyUsageProperty.DataEncipherment``.
            :param decipher_only: ``CfnCertificate.KeyUsageProperty.DecipherOnly``.
            :param digital_signature: ``CfnCertificate.KeyUsageProperty.DigitalSignature``.
            :param encipher_only: ``CfnCertificate.KeyUsageProperty.EncipherOnly``.
            :param key_agreement: ``CfnCertificate.KeyUsageProperty.KeyAgreement``.
            :param key_cert_sign: ``CfnCertificate.KeyUsageProperty.KeyCertSign``.
            :param key_encipherment: ``CfnCertificate.KeyUsageProperty.KeyEncipherment``.
            :param non_repudiation: ``CfnCertificate.KeyUsageProperty.NonRepudiation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if crl_sign is not None:
                self._values["crl_sign"] = crl_sign
            if data_encipherment is not None:
                self._values["data_encipherment"] = data_encipherment
            if decipher_only is not None:
                self._values["decipher_only"] = decipher_only
            if digital_signature is not None:
                self._values["digital_signature"] = digital_signature
            if encipher_only is not None:
                self._values["encipher_only"] = encipher_only
            if key_agreement is not None:
                self._values["key_agreement"] = key_agreement
            if key_cert_sign is not None:
                self._values["key_cert_sign"] = key_cert_sign
            if key_encipherment is not None:
                self._values["key_encipherment"] = key_encipherment
            if non_repudiation is not None:
                self._values["non_repudiation"] = non_repudiation

        @builtins.property
        def crl_sign(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificate.KeyUsageProperty.CRLSign``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-crlsign
            '''
            result = self._values.get("crl_sign")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def data_encipherment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificate.KeyUsageProperty.DataEncipherment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-dataencipherment
            '''
            result = self._values.get("data_encipherment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def decipher_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificate.KeyUsageProperty.DecipherOnly``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-decipheronly
            '''
            result = self._values.get("decipher_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def digital_signature(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificate.KeyUsageProperty.DigitalSignature``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-digitalsignature
            '''
            result = self._values.get("digital_signature")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def encipher_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificate.KeyUsageProperty.EncipherOnly``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-encipheronly
            '''
            result = self._values.get("encipher_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def key_agreement(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificate.KeyUsageProperty.KeyAgreement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-keyagreement
            '''
            result = self._values.get("key_agreement")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def key_cert_sign(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificate.KeyUsageProperty.KeyCertSign``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-keycertsign
            '''
            result = self._values.get("key_cert_sign")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def key_encipherment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificate.KeyUsageProperty.KeyEncipherment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-keyencipherment
            '''
            result = self._values.get("key_encipherment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def non_repudiation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificate.KeyUsageProperty.NonRepudiation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-keyusage.html#cfn-acmpca-certificate-keyusage-nonrepudiation
            '''
            result = self._values.get("non_repudiation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyUsageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.OtherNameProperty",
        jsii_struct_bases=[],
        name_mapping={"type_id": "typeId", "value": "value"},
    )
    class OtherNameProperty:
        def __init__(self, *, type_id: builtins.str, value: builtins.str) -> None:
            '''
            :param type_id: ``CfnCertificate.OtherNameProperty.TypeId``.
            :param value: ``CfnCertificate.OtherNameProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-othername.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type_id": type_id,
                "value": value,
            }

        @builtins.property
        def type_id(self) -> builtins.str:
            '''``CfnCertificate.OtherNameProperty.TypeId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-othername.html#cfn-acmpca-certificate-othername-typeid
            '''
            result = self._values.get("type_id")
            assert result is not None, "Required property 'type_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnCertificate.OtherNameProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-othername.html#cfn-acmpca-certificate-othername-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtherNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.PolicyInformationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cert_policy_id": "certPolicyId",
            "policy_qualifiers": "policyQualifiers",
        },
    )
    class PolicyInformationProperty:
        def __init__(
            self,
            *,
            cert_policy_id: builtins.str,
            policy_qualifiers: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.PolicyQualifierInfoProperty"]]]] = None,
        ) -> None:
            '''
            :param cert_policy_id: ``CfnCertificate.PolicyInformationProperty.CertPolicyId``.
            :param policy_qualifiers: ``CfnCertificate.PolicyInformationProperty.PolicyQualifiers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cert_policy_id": cert_policy_id,
            }
            if policy_qualifiers is not None:
                self._values["policy_qualifiers"] = policy_qualifiers

        @builtins.property
        def cert_policy_id(self) -> builtins.str:
            '''``CfnCertificate.PolicyInformationProperty.CertPolicyId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html#cfn-acmpca-certificate-policyinformation-certpolicyid
            '''
            result = self._values.get("cert_policy_id")
            assert result is not None, "Required property 'cert_policy_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def policy_qualifiers(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.PolicyQualifierInfoProperty"]]]]:
            '''``CfnCertificate.PolicyInformationProperty.PolicyQualifiers``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyinformation.html#cfn-acmpca-certificate-policyinformation-policyqualifiers
            '''
            result = self._values.get("policy_qualifiers")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.PolicyQualifierInfoProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyInformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.PolicyQualifierInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_qualifier_id": "policyQualifierId",
            "qualifier": "qualifier",
        },
    )
    class PolicyQualifierInfoProperty:
        def __init__(
            self,
            *,
            policy_qualifier_id: builtins.str,
            qualifier: typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.QualifierProperty"],
        ) -> None:
            '''
            :param policy_qualifier_id: ``CfnCertificate.PolicyQualifierInfoProperty.PolicyQualifierId``.
            :param qualifier: ``CfnCertificate.PolicyQualifierInfoProperty.Qualifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "policy_qualifier_id": policy_qualifier_id,
                "qualifier": qualifier,
            }

        @builtins.property
        def policy_qualifier_id(self) -> builtins.str:
            '''``CfnCertificate.PolicyQualifierInfoProperty.PolicyQualifierId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html#cfn-acmpca-certificate-policyqualifierinfo-policyqualifierid
            '''
            result = self._values.get("policy_qualifier_id")
            assert result is not None, "Required property 'policy_qualifier_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def qualifier(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.QualifierProperty"]:
            '''``CfnCertificate.PolicyQualifierInfoProperty.Qualifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-policyqualifierinfo.html#cfn-acmpca-certificate-policyqualifierinfo-qualifier
            '''
            result = self._values.get("qualifier")
            assert result is not None, "Required property 'qualifier' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCertificate.QualifierProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyQualifierInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.QualifierProperty",
        jsii_struct_bases=[],
        name_mapping={"cps_uri": "cpsUri"},
    )
    class QualifierProperty:
        def __init__(self, *, cps_uri: builtins.str) -> None:
            '''
            :param cps_uri: ``CfnCertificate.QualifierProperty.CpsUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-qualifier.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "cps_uri": cps_uri,
            }

        @builtins.property
        def cps_uri(self) -> builtins.str:
            '''``CfnCertificate.QualifierProperty.CpsUri``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-qualifier.html#cfn-acmpca-certificate-qualifier-cpsuri
            '''
            result = self._values.get("cps_uri")
            assert result is not None, "Required property 'cps_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QualifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.SubjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "common_name": "commonName",
            "country": "country",
            "distinguished_name_qualifier": "distinguishedNameQualifier",
            "generation_qualifier": "generationQualifier",
            "given_name": "givenName",
            "initials": "initials",
            "locality": "locality",
            "organization": "organization",
            "organizational_unit": "organizationalUnit",
            "pseudonym": "pseudonym",
            "serial_number": "serialNumber",
            "state": "state",
            "surname": "surname",
            "title": "title",
        },
    )
    class SubjectProperty:
        def __init__(
            self,
            *,
            common_name: typing.Optional[builtins.str] = None,
            country: typing.Optional[builtins.str] = None,
            distinguished_name_qualifier: typing.Optional[builtins.str] = None,
            generation_qualifier: typing.Optional[builtins.str] = None,
            given_name: typing.Optional[builtins.str] = None,
            initials: typing.Optional[builtins.str] = None,
            locality: typing.Optional[builtins.str] = None,
            organization: typing.Optional[builtins.str] = None,
            organizational_unit: typing.Optional[builtins.str] = None,
            pseudonym: typing.Optional[builtins.str] = None,
            serial_number: typing.Optional[builtins.str] = None,
            state: typing.Optional[builtins.str] = None,
            surname: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param common_name: ``CfnCertificate.SubjectProperty.CommonName``.
            :param country: ``CfnCertificate.SubjectProperty.Country``.
            :param distinguished_name_qualifier: ``CfnCertificate.SubjectProperty.DistinguishedNameQualifier``.
            :param generation_qualifier: ``CfnCertificate.SubjectProperty.GenerationQualifier``.
            :param given_name: ``CfnCertificate.SubjectProperty.GivenName``.
            :param initials: ``CfnCertificate.SubjectProperty.Initials``.
            :param locality: ``CfnCertificate.SubjectProperty.Locality``.
            :param organization: ``CfnCertificate.SubjectProperty.Organization``.
            :param organizational_unit: ``CfnCertificate.SubjectProperty.OrganizationalUnit``.
            :param pseudonym: ``CfnCertificate.SubjectProperty.Pseudonym``.
            :param serial_number: ``CfnCertificate.SubjectProperty.SerialNumber``.
            :param state: ``CfnCertificate.SubjectProperty.State``.
            :param surname: ``CfnCertificate.SubjectProperty.Surname``.
            :param title: ``CfnCertificate.SubjectProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if common_name is not None:
                self._values["common_name"] = common_name
            if country is not None:
                self._values["country"] = country
            if distinguished_name_qualifier is not None:
                self._values["distinguished_name_qualifier"] = distinguished_name_qualifier
            if generation_qualifier is not None:
                self._values["generation_qualifier"] = generation_qualifier
            if given_name is not None:
                self._values["given_name"] = given_name
            if initials is not None:
                self._values["initials"] = initials
            if locality is not None:
                self._values["locality"] = locality
            if organization is not None:
                self._values["organization"] = organization
            if organizational_unit is not None:
                self._values["organizational_unit"] = organizational_unit
            if pseudonym is not None:
                self._values["pseudonym"] = pseudonym
            if serial_number is not None:
                self._values["serial_number"] = serial_number
            if state is not None:
                self._values["state"] = state
            if surname is not None:
                self._values["surname"] = surname
            if title is not None:
                self._values["title"] = title

        @builtins.property
        def common_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.CommonName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-commonname
            '''
            result = self._values.get("common_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def country(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.Country``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-country
            '''
            result = self._values.get("country")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def distinguished_name_qualifier(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.DistinguishedNameQualifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-distinguishednamequalifier
            '''
            result = self._values.get("distinguished_name_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def generation_qualifier(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.GenerationQualifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-generationqualifier
            '''
            result = self._values.get("generation_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def given_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.GivenName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-givenname
            '''
            result = self._values.get("given_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def initials(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.Initials``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-initials
            '''
            result = self._values.get("initials")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def locality(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.Locality``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-locality
            '''
            result = self._values.get("locality")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organization(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.Organization``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-organization
            '''
            result = self._values.get("organization")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.OrganizationalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-organizationalunit
            '''
            result = self._values.get("organizational_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pseudonym(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.Pseudonym``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-pseudonym
            '''
            result = self._values.get("pseudonym")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def serial_number(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.SerialNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-serialnumber
            '''
            result = self._values.get("serial_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.State``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def surname(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.Surname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-surname
            '''
            result = self._values.get("surname")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificate.SubjectProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-subject.html#cfn-acmpca-certificate-subject-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificate.ValidityProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class ValidityProperty:
        def __init__(self, *, type: builtins.str, value: jsii.Number) -> None:
            '''
            :param type: ``CfnCertificate.ValidityProperty.Type``.
            :param value: ``CfnCertificate.ValidityProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''``CfnCertificate.ValidityProperty.Type``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html#cfn-acmpca-certificate-validity-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''``CfnCertificate.ValidityProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificate-validity.html#cfn-acmpca-certificate-validity-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCertificateAuthority(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority",
):
    '''A CloudFormation ``AWS::ACMPCA::CertificateAuthority``.

    :cloudformationResource: AWS::ACMPCA::CertificateAuthority
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        key_algorithm: builtins.str,
        signing_algorithm: builtins.str,
        subject: typing.Union["CfnCertificateAuthority.SubjectProperty", aws_cdk.core.IResolvable],
        type: builtins.str,
        csr_extensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.CsrExtensionsProperty"]] = None,
        key_storage_security_standard: typing.Optional[builtins.str] = None,
        revocation_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.RevocationConfigurationProperty"]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Create a new ``AWS::ACMPCA::CertificateAuthority``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param key_algorithm: ``AWS::ACMPCA::CertificateAuthority.KeyAlgorithm``.
        :param signing_algorithm: ``AWS::ACMPCA::CertificateAuthority.SigningAlgorithm``.
        :param subject: ``AWS::ACMPCA::CertificateAuthority.Subject``.
        :param type: ``AWS::ACMPCA::CertificateAuthority.Type``.
        :param csr_extensions: ``AWS::ACMPCA::CertificateAuthority.CsrExtensions``.
        :param key_storage_security_standard: ``AWS::ACMPCA::CertificateAuthority.KeyStorageSecurityStandard``.
        :param revocation_configuration: ``AWS::ACMPCA::CertificateAuthority.RevocationConfiguration``.
        :param tags: ``AWS::ACMPCA::CertificateAuthority.Tags``.
        '''
        props = CfnCertificateAuthorityProps(
            key_algorithm=key_algorithm,
            signing_algorithm=signing_algorithm,
            subject=subject,
            type=type,
            csr_extensions=csr_extensions,
            key_storage_security_standard=key_storage_security_standard,
            revocation_configuration=revocation_configuration,
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
    @jsii.member(jsii_name="attrCertificateSigningRequest")
    def attr_certificate_signing_request(self) -> builtins.str:
        '''
        :cloudformationAttribute: CertificateSigningRequest
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCertificateSigningRequest"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''``AWS::ACMPCA::CertificateAuthority.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keyAlgorithm")
    def key_algorithm(self) -> builtins.str:
        '''``AWS::ACMPCA::CertificateAuthority.KeyAlgorithm``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-keyalgorithm
        '''
        return typing.cast(builtins.str, jsii.get(self, "keyAlgorithm"))

    @key_algorithm.setter
    def key_algorithm(self, value: builtins.str) -> None:
        jsii.set(self, "keyAlgorithm", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="signingAlgorithm")
    def signing_algorithm(self) -> builtins.str:
        '''``AWS::ACMPCA::CertificateAuthority.SigningAlgorithm``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-signingalgorithm
        '''
        return typing.cast(builtins.str, jsii.get(self, "signingAlgorithm"))

    @signing_algorithm.setter
    def signing_algorithm(self, value: builtins.str) -> None:
        jsii.set(self, "signingAlgorithm", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="subject")
    def subject(
        self,
    ) -> typing.Union["CfnCertificateAuthority.SubjectProperty", aws_cdk.core.IResolvable]:
        '''``AWS::ACMPCA::CertificateAuthority.Subject``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-subject
        '''
        return typing.cast(typing.Union["CfnCertificateAuthority.SubjectProperty", aws_cdk.core.IResolvable], jsii.get(self, "subject"))

    @subject.setter
    def subject(
        self,
        value: typing.Union["CfnCertificateAuthority.SubjectProperty", aws_cdk.core.IResolvable],
    ) -> None:
        jsii.set(self, "subject", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''``AWS::ACMPCA::CertificateAuthority.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-type
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        jsii.set(self, "type", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="csrExtensions")
    def csr_extensions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.CsrExtensionsProperty"]]:
        '''``AWS::ACMPCA::CertificateAuthority.CsrExtensions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-csrextensions
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.CsrExtensionsProperty"]], jsii.get(self, "csrExtensions"))

    @csr_extensions.setter
    def csr_extensions(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.CsrExtensionsProperty"]],
    ) -> None:
        jsii.set(self, "csrExtensions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="keyStorageSecurityStandard")
    def key_storage_security_standard(self) -> typing.Optional[builtins.str]:
        '''``AWS::ACMPCA::CertificateAuthority.KeyStorageSecurityStandard``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-keystoragesecuritystandard
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyStorageSecurityStandard"))

    @key_storage_security_standard.setter
    def key_storage_security_standard(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        jsii.set(self, "keyStorageSecurityStandard", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="revocationConfiguration")
    def revocation_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.RevocationConfigurationProperty"]]:
        '''``AWS::ACMPCA::CertificateAuthority.RevocationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-revocationconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.RevocationConfigurationProperty"]], jsii.get(self, "revocationConfiguration"))

    @revocation_configuration.setter
    def revocation_configuration(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.RevocationConfigurationProperty"]],
    ) -> None:
        jsii.set(self, "revocationConfiguration", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.AccessDescriptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_location": "accessLocation",
            "access_method": "accessMethod",
        },
    )
    class AccessDescriptionProperty:
        def __init__(
            self,
            *,
            access_location: typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.GeneralNameProperty"],
            access_method: typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.AccessMethodProperty"],
        ) -> None:
            '''
            :param access_location: ``CfnCertificateAuthority.AccessDescriptionProperty.AccessLocation``.
            :param access_method: ``CfnCertificateAuthority.AccessDescriptionProperty.AccessMethod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "access_location": access_location,
                "access_method": access_method,
            }

        @builtins.property
        def access_location(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.GeneralNameProperty"]:
            '''``CfnCertificateAuthority.AccessDescriptionProperty.AccessLocation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html#cfn-acmpca-certificateauthority-accessdescription-accesslocation
            '''
            result = self._values.get("access_location")
            assert result is not None, "Required property 'access_location' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.GeneralNameProperty"], result)

        @builtins.property
        def access_method(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.AccessMethodProperty"]:
            '''``CfnCertificateAuthority.AccessDescriptionProperty.AccessMethod``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessdescription.html#cfn-acmpca-certificateauthority-accessdescription-accessmethod
            '''
            result = self._values.get("access_method")
            assert result is not None, "Required property 'access_method' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.AccessMethodProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessDescriptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.AccessMethodProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_method_type": "accessMethodType",
            "custom_object_identifier": "customObjectIdentifier",
        },
    )
    class AccessMethodProperty:
        def __init__(
            self,
            *,
            access_method_type: typing.Optional[builtins.str] = None,
            custom_object_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param access_method_type: ``CfnCertificateAuthority.AccessMethodProperty.AccessMethodType``.
            :param custom_object_identifier: ``CfnCertificateAuthority.AccessMethodProperty.CustomObjectIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if access_method_type is not None:
                self._values["access_method_type"] = access_method_type
            if custom_object_identifier is not None:
                self._values["custom_object_identifier"] = custom_object_identifier

        @builtins.property
        def access_method_type(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.AccessMethodProperty.AccessMethodType``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html#cfn-acmpca-certificateauthority-accessmethod-accessmethodtype
            '''
            result = self._values.get("access_method_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_object_identifier(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.AccessMethodProperty.CustomObjectIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-accessmethod.html#cfn-acmpca-certificateauthority-accessmethod-customobjectidentifier
            '''
            result = self._values.get("custom_object_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessMethodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.CrlConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_cname": "customCname",
            "enabled": "enabled",
            "expiration_in_days": "expirationInDays",
            "s3_bucket_name": "s3BucketName",
            "s3_object_acl": "s3ObjectAcl",
        },
    )
    class CrlConfigurationProperty:
        def __init__(
            self,
            *,
            custom_cname: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            expiration_in_days: typing.Optional[jsii.Number] = None,
            s3_bucket_name: typing.Optional[builtins.str] = None,
            s3_object_acl: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param custom_cname: ``CfnCertificateAuthority.CrlConfigurationProperty.CustomCname``.
            :param enabled: ``CfnCertificateAuthority.CrlConfigurationProperty.Enabled``.
            :param expiration_in_days: ``CfnCertificateAuthority.CrlConfigurationProperty.ExpirationInDays``.
            :param s3_bucket_name: ``CfnCertificateAuthority.CrlConfigurationProperty.S3BucketName``.
            :param s3_object_acl: ``CfnCertificateAuthority.CrlConfigurationProperty.S3ObjectAcl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if custom_cname is not None:
                self._values["custom_cname"] = custom_cname
            if enabled is not None:
                self._values["enabled"] = enabled
            if expiration_in_days is not None:
                self._values["expiration_in_days"] = expiration_in_days
            if s3_bucket_name is not None:
                self._values["s3_bucket_name"] = s3_bucket_name
            if s3_object_acl is not None:
                self._values["s3_object_acl"] = s3_object_acl

        @builtins.property
        def custom_cname(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.CrlConfigurationProperty.CustomCname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-customcname
            '''
            result = self._values.get("custom_cname")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.CrlConfigurationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def expiration_in_days(self) -> typing.Optional[jsii.Number]:
            '''``CfnCertificateAuthority.CrlConfigurationProperty.ExpirationInDays``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-expirationindays
            '''
            result = self._values.get("expiration_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.CrlConfigurationProperty.S3BucketName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_object_acl(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.CrlConfigurationProperty.S3ObjectAcl``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-crlconfiguration.html#cfn-acmpca-certificateauthority-crlconfiguration-s3objectacl
            '''
            result = self._values.get("s3_object_acl")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrlConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.CsrExtensionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key_usage": "keyUsage",
            "subject_information_access": "subjectInformationAccess",
        },
    )
    class CsrExtensionsProperty:
        def __init__(
            self,
            *,
            key_usage: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.KeyUsageProperty"]] = None,
            subject_information_access: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.AccessDescriptionProperty"]]]] = None,
        ) -> None:
            '''
            :param key_usage: ``CfnCertificateAuthority.CsrExtensionsProperty.KeyUsage``.
            :param subject_information_access: ``CfnCertificateAuthority.CsrExtensionsProperty.SubjectInformationAccess``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if key_usage is not None:
                self._values["key_usage"] = key_usage
            if subject_information_access is not None:
                self._values["subject_information_access"] = subject_information_access

        @builtins.property
        def key_usage(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.KeyUsageProperty"]]:
            '''``CfnCertificateAuthority.CsrExtensionsProperty.KeyUsage``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html#cfn-acmpca-certificateauthority-csrextensions-keyusage
            '''
            result = self._values.get("key_usage")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.KeyUsageProperty"]], result)

        @builtins.property
        def subject_information_access(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.AccessDescriptionProperty"]]]]:
            '''``CfnCertificateAuthority.CsrExtensionsProperty.SubjectInformationAccess``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-csrextensions.html#cfn-acmpca-certificateauthority-csrextensions-subjectinformationaccess
            '''
            result = self._values.get("subject_information_access")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.AccessDescriptionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CsrExtensionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.EdiPartyNameProperty",
        jsii_struct_bases=[],
        name_mapping={"name_assigner": "nameAssigner", "party_name": "partyName"},
    )
    class EdiPartyNameProperty:
        def __init__(
            self,
            *,
            name_assigner: builtins.str,
            party_name: builtins.str,
        ) -> None:
            '''
            :param name_assigner: ``CfnCertificateAuthority.EdiPartyNameProperty.NameAssigner``.
            :param party_name: ``CfnCertificateAuthority.EdiPartyNameProperty.PartyName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "name_assigner": name_assigner,
                "party_name": party_name,
            }

        @builtins.property
        def name_assigner(self) -> builtins.str:
            '''``CfnCertificateAuthority.EdiPartyNameProperty.NameAssigner``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html#cfn-acmpca-certificateauthority-edipartyname-nameassigner
            '''
            result = self._values.get("name_assigner")
            assert result is not None, "Required property 'name_assigner' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def party_name(self) -> builtins.str:
            '''``CfnCertificateAuthority.EdiPartyNameProperty.PartyName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-edipartyname.html#cfn-acmpca-certificateauthority-edipartyname-partyname
            '''
            result = self._values.get("party_name")
            assert result is not None, "Required property 'party_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdiPartyNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.GeneralNameProperty",
        jsii_struct_bases=[],
        name_mapping={
            "directory_name": "directoryName",
            "dns_name": "dnsName",
            "edi_party_name": "ediPartyName",
            "ip_address": "ipAddress",
            "other_name": "otherName",
            "registered_id": "registeredId",
            "rfc822_name": "rfc822Name",
            "uniform_resource_identifier": "uniformResourceIdentifier",
        },
    )
    class GeneralNameProperty:
        def __init__(
            self,
            *,
            directory_name: typing.Optional[typing.Union["CfnCertificateAuthority.SubjectProperty", aws_cdk.core.IResolvable]] = None,
            dns_name: typing.Optional[builtins.str] = None,
            edi_party_name: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.EdiPartyNameProperty"]] = None,
            ip_address: typing.Optional[builtins.str] = None,
            other_name: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.OtherNameProperty"]] = None,
            registered_id: typing.Optional[builtins.str] = None,
            rfc822_name: typing.Optional[builtins.str] = None,
            uniform_resource_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param directory_name: ``CfnCertificateAuthority.GeneralNameProperty.DirectoryName``.
            :param dns_name: ``CfnCertificateAuthority.GeneralNameProperty.DnsName``.
            :param edi_party_name: ``CfnCertificateAuthority.GeneralNameProperty.EdiPartyName``.
            :param ip_address: ``CfnCertificateAuthority.GeneralNameProperty.IpAddress``.
            :param other_name: ``CfnCertificateAuthority.GeneralNameProperty.OtherName``.
            :param registered_id: ``CfnCertificateAuthority.GeneralNameProperty.RegisteredId``.
            :param rfc822_name: ``CfnCertificateAuthority.GeneralNameProperty.Rfc822Name``.
            :param uniform_resource_identifier: ``CfnCertificateAuthority.GeneralNameProperty.UniformResourceIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if directory_name is not None:
                self._values["directory_name"] = directory_name
            if dns_name is not None:
                self._values["dns_name"] = dns_name
            if edi_party_name is not None:
                self._values["edi_party_name"] = edi_party_name
            if ip_address is not None:
                self._values["ip_address"] = ip_address
            if other_name is not None:
                self._values["other_name"] = other_name
            if registered_id is not None:
                self._values["registered_id"] = registered_id
            if rfc822_name is not None:
                self._values["rfc822_name"] = rfc822_name
            if uniform_resource_identifier is not None:
                self._values["uniform_resource_identifier"] = uniform_resource_identifier

        @builtins.property
        def directory_name(
            self,
        ) -> typing.Optional[typing.Union["CfnCertificateAuthority.SubjectProperty", aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.GeneralNameProperty.DirectoryName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-directoryname
            '''
            result = self._values.get("directory_name")
            return typing.cast(typing.Optional[typing.Union["CfnCertificateAuthority.SubjectProperty", aws_cdk.core.IResolvable]], result)

        @builtins.property
        def dns_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.GeneralNameProperty.DnsName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-dnsname
            '''
            result = self._values.get("dns_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def edi_party_name(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.EdiPartyNameProperty"]]:
            '''``CfnCertificateAuthority.GeneralNameProperty.EdiPartyName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-edipartyname
            '''
            result = self._values.get("edi_party_name")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.EdiPartyNameProperty"]], result)

        @builtins.property
        def ip_address(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.GeneralNameProperty.IpAddress``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-ipaddress
            '''
            result = self._values.get("ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def other_name(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.OtherNameProperty"]]:
            '''``CfnCertificateAuthority.GeneralNameProperty.OtherName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-othername
            '''
            result = self._values.get("other_name")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.OtherNameProperty"]], result)

        @builtins.property
        def registered_id(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.GeneralNameProperty.RegisteredId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-registeredid
            '''
            result = self._values.get("registered_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rfc822_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.GeneralNameProperty.Rfc822Name``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-rfc822name
            '''
            result = self._values.get("rfc822_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uniform_resource_identifier(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.GeneralNameProperty.UniformResourceIdentifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-generalname.html#cfn-acmpca-certificateauthority-generalname-uniformresourceidentifier
            '''
            result = self._values.get("uniform_resource_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeneralNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.KeyUsageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crl_sign": "crlSign",
            "data_encipherment": "dataEncipherment",
            "decipher_only": "decipherOnly",
            "digital_signature": "digitalSignature",
            "encipher_only": "encipherOnly",
            "key_agreement": "keyAgreement",
            "key_cert_sign": "keyCertSign",
            "key_encipherment": "keyEncipherment",
            "non_repudiation": "nonRepudiation",
        },
    )
    class KeyUsageProperty:
        def __init__(
            self,
            *,
            crl_sign: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            data_encipherment: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            decipher_only: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            digital_signature: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            encipher_only: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            key_agreement: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            key_cert_sign: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            key_encipherment: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            non_repudiation: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''
            :param crl_sign: ``CfnCertificateAuthority.KeyUsageProperty.CRLSign``.
            :param data_encipherment: ``CfnCertificateAuthority.KeyUsageProperty.DataEncipherment``.
            :param decipher_only: ``CfnCertificateAuthority.KeyUsageProperty.DecipherOnly``.
            :param digital_signature: ``CfnCertificateAuthority.KeyUsageProperty.DigitalSignature``.
            :param encipher_only: ``CfnCertificateAuthority.KeyUsageProperty.EncipherOnly``.
            :param key_agreement: ``CfnCertificateAuthority.KeyUsageProperty.KeyAgreement``.
            :param key_cert_sign: ``CfnCertificateAuthority.KeyUsageProperty.KeyCertSign``.
            :param key_encipherment: ``CfnCertificateAuthority.KeyUsageProperty.KeyEncipherment``.
            :param non_repudiation: ``CfnCertificateAuthority.KeyUsageProperty.NonRepudiation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if crl_sign is not None:
                self._values["crl_sign"] = crl_sign
            if data_encipherment is not None:
                self._values["data_encipherment"] = data_encipherment
            if decipher_only is not None:
                self._values["decipher_only"] = decipher_only
            if digital_signature is not None:
                self._values["digital_signature"] = digital_signature
            if encipher_only is not None:
                self._values["encipher_only"] = encipher_only
            if key_agreement is not None:
                self._values["key_agreement"] = key_agreement
            if key_cert_sign is not None:
                self._values["key_cert_sign"] = key_cert_sign
            if key_encipherment is not None:
                self._values["key_encipherment"] = key_encipherment
            if non_repudiation is not None:
                self._values["non_repudiation"] = non_repudiation

        @builtins.property
        def crl_sign(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.KeyUsageProperty.CRLSign``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-crlsign
            '''
            result = self._values.get("crl_sign")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def data_encipherment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.KeyUsageProperty.DataEncipherment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-dataencipherment
            '''
            result = self._values.get("data_encipherment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def decipher_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.KeyUsageProperty.DecipherOnly``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-decipheronly
            '''
            result = self._values.get("decipher_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def digital_signature(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.KeyUsageProperty.DigitalSignature``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-digitalsignature
            '''
            result = self._values.get("digital_signature")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def encipher_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.KeyUsageProperty.EncipherOnly``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-encipheronly
            '''
            result = self._values.get("encipher_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def key_agreement(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.KeyUsageProperty.KeyAgreement``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-keyagreement
            '''
            result = self._values.get("key_agreement")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def key_cert_sign(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.KeyUsageProperty.KeyCertSign``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-keycertsign
            '''
            result = self._values.get("key_cert_sign")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def key_encipherment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.KeyUsageProperty.KeyEncipherment``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-keyencipherment
            '''
            result = self._values.get("key_encipherment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def non_repudiation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.KeyUsageProperty.NonRepudiation``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-keyusage.html#cfn-acmpca-certificateauthority-keyusage-nonrepudiation
            '''
            result = self._values.get("non_repudiation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyUsageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.OcspConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "ocsp_custom_cname": "ocspCustomCname"},
    )
    class OcspConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            ocsp_custom_cname: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param enabled: ``CfnCertificateAuthority.OcspConfigurationProperty.Enabled``.
            :param ocsp_custom_cname: ``CfnCertificateAuthority.OcspConfigurationProperty.OcspCustomCname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if ocsp_custom_cname is not None:
                self._values["ocsp_custom_cname"] = ocsp_custom_cname

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''``CfnCertificateAuthority.OcspConfigurationProperty.Enabled``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html#cfn-acmpca-certificateauthority-ocspconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def ocsp_custom_cname(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.OcspConfigurationProperty.OcspCustomCname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-ocspconfiguration.html#cfn-acmpca-certificateauthority-ocspconfiguration-ocspcustomcname
            '''
            result = self._values.get("ocsp_custom_cname")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OcspConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.OtherNameProperty",
        jsii_struct_bases=[],
        name_mapping={"type_id": "typeId", "value": "value"},
    )
    class OtherNameProperty:
        def __init__(self, *, type_id: builtins.str, value: builtins.str) -> None:
            '''
            :param type_id: ``CfnCertificateAuthority.OtherNameProperty.TypeId``.
            :param value: ``CfnCertificateAuthority.OtherNameProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html
            '''
            self._values: typing.Dict[str, typing.Any] = {
                "type_id": type_id,
                "value": value,
            }

        @builtins.property
        def type_id(self) -> builtins.str:
            '''``CfnCertificateAuthority.OtherNameProperty.TypeId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html#cfn-acmpca-certificateauthority-othername-typeid
            '''
            result = self._values.get("type_id")
            assert result is not None, "Required property 'type_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''``CfnCertificateAuthority.OtherNameProperty.Value``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-othername.html#cfn-acmpca-certificateauthority-othername-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OtherNameProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.RevocationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "crl_configuration": "crlConfiguration",
            "ocsp_configuration": "ocspConfiguration",
        },
    )
    class RevocationConfigurationProperty:
        def __init__(
            self,
            *,
            crl_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.CrlConfigurationProperty"]] = None,
            ocsp_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.OcspConfigurationProperty"]] = None,
        ) -> None:
            '''
            :param crl_configuration: ``CfnCertificateAuthority.RevocationConfigurationProperty.CrlConfiguration``.
            :param ocsp_configuration: ``CfnCertificateAuthority.RevocationConfigurationProperty.OcspConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if crl_configuration is not None:
                self._values["crl_configuration"] = crl_configuration
            if ocsp_configuration is not None:
                self._values["ocsp_configuration"] = ocsp_configuration

        @builtins.property
        def crl_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.CrlConfigurationProperty"]]:
            '''``CfnCertificateAuthority.RevocationConfigurationProperty.CrlConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html#cfn-acmpca-certificateauthority-revocationconfiguration-crlconfiguration
            '''
            result = self._values.get("crl_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.CrlConfigurationProperty"]], result)

        @builtins.property
        def ocsp_configuration(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.OcspConfigurationProperty"]]:
            '''``CfnCertificateAuthority.RevocationConfigurationProperty.OcspConfiguration``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-revocationconfiguration.html#cfn-acmpca-certificateauthority-revocationconfiguration-ocspconfiguration
            '''
            result = self._values.get("ocsp_configuration")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCertificateAuthority.OcspConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RevocationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthority.SubjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "common_name": "commonName",
            "country": "country",
            "distinguished_name_qualifier": "distinguishedNameQualifier",
            "generation_qualifier": "generationQualifier",
            "given_name": "givenName",
            "initials": "initials",
            "locality": "locality",
            "organization": "organization",
            "organizational_unit": "organizationalUnit",
            "pseudonym": "pseudonym",
            "serial_number": "serialNumber",
            "state": "state",
            "surname": "surname",
            "title": "title",
        },
    )
    class SubjectProperty:
        def __init__(
            self,
            *,
            common_name: typing.Optional[builtins.str] = None,
            country: typing.Optional[builtins.str] = None,
            distinguished_name_qualifier: typing.Optional[builtins.str] = None,
            generation_qualifier: typing.Optional[builtins.str] = None,
            given_name: typing.Optional[builtins.str] = None,
            initials: typing.Optional[builtins.str] = None,
            locality: typing.Optional[builtins.str] = None,
            organization: typing.Optional[builtins.str] = None,
            organizational_unit: typing.Optional[builtins.str] = None,
            pseudonym: typing.Optional[builtins.str] = None,
            serial_number: typing.Optional[builtins.str] = None,
            state: typing.Optional[builtins.str] = None,
            surname: typing.Optional[builtins.str] = None,
            title: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param common_name: ``CfnCertificateAuthority.SubjectProperty.CommonName``.
            :param country: ``CfnCertificateAuthority.SubjectProperty.Country``.
            :param distinguished_name_qualifier: ``CfnCertificateAuthority.SubjectProperty.DistinguishedNameQualifier``.
            :param generation_qualifier: ``CfnCertificateAuthority.SubjectProperty.GenerationQualifier``.
            :param given_name: ``CfnCertificateAuthority.SubjectProperty.GivenName``.
            :param initials: ``CfnCertificateAuthority.SubjectProperty.Initials``.
            :param locality: ``CfnCertificateAuthority.SubjectProperty.Locality``.
            :param organization: ``CfnCertificateAuthority.SubjectProperty.Organization``.
            :param organizational_unit: ``CfnCertificateAuthority.SubjectProperty.OrganizationalUnit``.
            :param pseudonym: ``CfnCertificateAuthority.SubjectProperty.Pseudonym``.
            :param serial_number: ``CfnCertificateAuthority.SubjectProperty.SerialNumber``.
            :param state: ``CfnCertificateAuthority.SubjectProperty.State``.
            :param surname: ``CfnCertificateAuthority.SubjectProperty.Surname``.
            :param title: ``CfnCertificateAuthority.SubjectProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html
            '''
            self._values: typing.Dict[str, typing.Any] = {}
            if common_name is not None:
                self._values["common_name"] = common_name
            if country is not None:
                self._values["country"] = country
            if distinguished_name_qualifier is not None:
                self._values["distinguished_name_qualifier"] = distinguished_name_qualifier
            if generation_qualifier is not None:
                self._values["generation_qualifier"] = generation_qualifier
            if given_name is not None:
                self._values["given_name"] = given_name
            if initials is not None:
                self._values["initials"] = initials
            if locality is not None:
                self._values["locality"] = locality
            if organization is not None:
                self._values["organization"] = organization
            if organizational_unit is not None:
                self._values["organizational_unit"] = organizational_unit
            if pseudonym is not None:
                self._values["pseudonym"] = pseudonym
            if serial_number is not None:
                self._values["serial_number"] = serial_number
            if state is not None:
                self._values["state"] = state
            if surname is not None:
                self._values["surname"] = surname
            if title is not None:
                self._values["title"] = title

        @builtins.property
        def common_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.CommonName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-commonname
            '''
            result = self._values.get("common_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def country(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.Country``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-country
            '''
            result = self._values.get("country")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def distinguished_name_qualifier(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.DistinguishedNameQualifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-distinguishednamequalifier
            '''
            result = self._values.get("distinguished_name_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def generation_qualifier(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.GenerationQualifier``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-generationqualifier
            '''
            result = self._values.get("generation_qualifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def given_name(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.GivenName``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-givenname
            '''
            result = self._values.get("given_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def initials(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.Initials``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-initials
            '''
            result = self._values.get("initials")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def locality(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.Locality``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-locality
            '''
            result = self._values.get("locality")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organization(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.Organization``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-organization
            '''
            result = self._values.get("organization")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organizational_unit(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.OrganizationalUnit``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-organizationalunit
            '''
            result = self._values.get("organizational_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pseudonym(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.Pseudonym``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-pseudonym
            '''
            result = self._values.get("pseudonym")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def serial_number(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.SerialNumber``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-serialnumber
            '''
            result = self._values.get("serial_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.State``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def surname(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.Surname``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-surname
            '''
            result = self._values.get("surname")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def title(self) -> typing.Optional[builtins.str]:
            '''``CfnCertificateAuthority.SubjectProperty.Title``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-acmpca-certificateauthority-subject.html#cfn-acmpca-certificateauthority-subject-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCertificateAuthorityActivation(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthorityActivation",
):
    '''A CloudFormation ``AWS::ACMPCA::CertificateAuthorityActivation``.

    :cloudformationResource: AWS::ACMPCA::CertificateAuthorityActivation
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        certificate: builtins.str,
        certificate_authority_arn: builtins.str,
        certificate_chain: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ACMPCA::CertificateAuthorityActivation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param certificate: ``AWS::ACMPCA::CertificateAuthorityActivation.Certificate``.
        :param certificate_authority_arn: ``AWS::ACMPCA::CertificateAuthorityActivation.CertificateAuthorityArn``.
        :param certificate_chain: ``AWS::ACMPCA::CertificateAuthorityActivation.CertificateChain``.
        :param status: ``AWS::ACMPCA::CertificateAuthorityActivation.Status``.
        '''
        props = CfnCertificateAuthorityActivationProps(
            certificate=certificate,
            certificate_authority_arn=certificate_authority_arn,
            certificate_chain=certificate_chain,
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
    @jsii.member(jsii_name="attrCompleteCertificateChain")
    def attr_complete_certificate_chain(self) -> builtins.str:
        '''
        :cloudformationAttribute: CompleteCertificateChain
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCompleteCertificateChain"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        '''``AWS::ACMPCA::CertificateAuthorityActivation.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificate
        '''
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        jsii.set(self, "certificate", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''``AWS::ACMPCA::CertificateAuthorityActivation.CertificateAuthorityArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificateauthorityarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: builtins.str) -> None:
        jsii.set(self, "certificateAuthorityArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> typing.Optional[builtins.str]:
        '''``AWS::ACMPCA::CertificateAuthorityActivation.CertificateChain``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificatechain
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "certificateChain", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::ACMPCA::CertificateAuthorityActivation.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-status
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthorityActivationProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "certificate_authority_arn": "certificateAuthorityArn",
        "certificate_chain": "certificateChain",
        "status": "status",
    },
)
class CfnCertificateAuthorityActivationProps:
    def __init__(
        self,
        *,
        certificate: builtins.str,
        certificate_authority_arn: builtins.str,
        certificate_chain: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ACMPCA::CertificateAuthorityActivation``.

        :param certificate: ``AWS::ACMPCA::CertificateAuthorityActivation.Certificate``.
        :param certificate_authority_arn: ``AWS::ACMPCA::CertificateAuthorityActivation.CertificateAuthorityArn``.
        :param certificate_chain: ``AWS::ACMPCA::CertificateAuthorityActivation.CertificateChain``.
        :param status: ``AWS::ACMPCA::CertificateAuthorityActivation.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "certificate": certificate,
            "certificate_authority_arn": certificate_authority_arn,
        }
        if certificate_chain is not None:
            self._values["certificate_chain"] = certificate_chain
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def certificate(self) -> builtins.str:
        '''``AWS::ACMPCA::CertificateAuthorityActivation.Certificate``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificate
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''``AWS::ACMPCA::CertificateAuthorityActivation.CertificateAuthorityArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificateauthorityarn
        '''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_chain(self) -> typing.Optional[builtins.str]:
        '''``AWS::ACMPCA::CertificateAuthorityActivation.CertificateChain``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-certificatechain
        '''
        result = self._values.get("certificate_chain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''``AWS::ACMPCA::CertificateAuthorityActivation.Status``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html#cfn-acmpca-certificateauthorityactivation-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateAuthorityActivationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-acmpca.CfnCertificateAuthorityProps",
    jsii_struct_bases=[],
    name_mapping={
        "key_algorithm": "keyAlgorithm",
        "signing_algorithm": "signingAlgorithm",
        "subject": "subject",
        "type": "type",
        "csr_extensions": "csrExtensions",
        "key_storage_security_standard": "keyStorageSecurityStandard",
        "revocation_configuration": "revocationConfiguration",
        "tags": "tags",
    },
)
class CfnCertificateAuthorityProps:
    def __init__(
        self,
        *,
        key_algorithm: builtins.str,
        signing_algorithm: builtins.str,
        subject: typing.Union[CfnCertificateAuthority.SubjectProperty, aws_cdk.core.IResolvable],
        type: builtins.str,
        csr_extensions: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificateAuthority.CsrExtensionsProperty]] = None,
        key_storage_security_standard: typing.Optional[builtins.str] = None,
        revocation_configuration: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificateAuthority.RevocationConfigurationProperty]] = None,
        tags: typing.Optional[typing.Sequence[aws_cdk.core.CfnTag]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ACMPCA::CertificateAuthority``.

        :param key_algorithm: ``AWS::ACMPCA::CertificateAuthority.KeyAlgorithm``.
        :param signing_algorithm: ``AWS::ACMPCA::CertificateAuthority.SigningAlgorithm``.
        :param subject: ``AWS::ACMPCA::CertificateAuthority.Subject``.
        :param type: ``AWS::ACMPCA::CertificateAuthority.Type``.
        :param csr_extensions: ``AWS::ACMPCA::CertificateAuthority.CsrExtensions``.
        :param key_storage_security_standard: ``AWS::ACMPCA::CertificateAuthority.KeyStorageSecurityStandard``.
        :param revocation_configuration: ``AWS::ACMPCA::CertificateAuthority.RevocationConfiguration``.
        :param tags: ``AWS::ACMPCA::CertificateAuthority.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "key_algorithm": key_algorithm,
            "signing_algorithm": signing_algorithm,
            "subject": subject,
            "type": type,
        }
        if csr_extensions is not None:
            self._values["csr_extensions"] = csr_extensions
        if key_storage_security_standard is not None:
            self._values["key_storage_security_standard"] = key_storage_security_standard
        if revocation_configuration is not None:
            self._values["revocation_configuration"] = revocation_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def key_algorithm(self) -> builtins.str:
        '''``AWS::ACMPCA::CertificateAuthority.KeyAlgorithm``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-keyalgorithm
        '''
        result = self._values.get("key_algorithm")
        assert result is not None, "Required property 'key_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signing_algorithm(self) -> builtins.str:
        '''``AWS::ACMPCA::CertificateAuthority.SigningAlgorithm``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-signingalgorithm
        '''
        result = self._values.get("signing_algorithm")
        assert result is not None, "Required property 'signing_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject(
        self,
    ) -> typing.Union[CfnCertificateAuthority.SubjectProperty, aws_cdk.core.IResolvable]:
        '''``AWS::ACMPCA::CertificateAuthority.Subject``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-subject
        '''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(typing.Union[CfnCertificateAuthority.SubjectProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''``AWS::ACMPCA::CertificateAuthority.Type``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def csr_extensions(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificateAuthority.CsrExtensionsProperty]]:
        '''``AWS::ACMPCA::CertificateAuthority.CsrExtensions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-csrextensions
        '''
        result = self._values.get("csr_extensions")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificateAuthority.CsrExtensionsProperty]], result)

    @builtins.property
    def key_storage_security_standard(self) -> typing.Optional[builtins.str]:
        '''``AWS::ACMPCA::CertificateAuthority.KeyStorageSecurityStandard``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-keystoragesecuritystandard
        '''
        result = self._values.get("key_storage_security_standard")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revocation_configuration(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificateAuthority.RevocationConfigurationProperty]]:
        '''``AWS::ACMPCA::CertificateAuthority.RevocationConfiguration``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-revocationconfiguration
        '''
        result = self._values.get("revocation_configuration")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificateAuthority.RevocationConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        '''``AWS::ACMPCA::CertificateAuthority.Tags``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html#cfn-acmpca-certificateauthority-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[aws_cdk.core.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateAuthorityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-acmpca.CfnCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_authority_arn": "certificateAuthorityArn",
        "certificate_signing_request": "certificateSigningRequest",
        "signing_algorithm": "signingAlgorithm",
        "validity": "validity",
        "api_passthrough": "apiPassthrough",
        "template_arn": "templateArn",
        "validity_not_before": "validityNotBefore",
    },
)
class CfnCertificateProps:
    def __init__(
        self,
        *,
        certificate_authority_arn: builtins.str,
        certificate_signing_request: builtins.str,
        signing_algorithm: builtins.str,
        validity: typing.Union[aws_cdk.core.IResolvable, CfnCertificate.ValidityProperty],
        api_passthrough: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificate.ApiPassthroughProperty]] = None,
        template_arn: typing.Optional[builtins.str] = None,
        validity_not_before: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificate.ValidityProperty]] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ACMPCA::Certificate``.

        :param certificate_authority_arn: ``AWS::ACMPCA::Certificate.CertificateAuthorityArn``.
        :param certificate_signing_request: ``AWS::ACMPCA::Certificate.CertificateSigningRequest``.
        :param signing_algorithm: ``AWS::ACMPCA::Certificate.SigningAlgorithm``.
        :param validity: ``AWS::ACMPCA::Certificate.Validity``.
        :param api_passthrough: ``AWS::ACMPCA::Certificate.ApiPassthrough``.
        :param template_arn: ``AWS::ACMPCA::Certificate.TemplateArn``.
        :param validity_not_before: ``AWS::ACMPCA::Certificate.ValidityNotBefore``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_authority_arn": certificate_authority_arn,
            "certificate_signing_request": certificate_signing_request,
            "signing_algorithm": signing_algorithm,
            "validity": validity,
        }
        if api_passthrough is not None:
            self._values["api_passthrough"] = api_passthrough
        if template_arn is not None:
            self._values["template_arn"] = template_arn
        if validity_not_before is not None:
            self._values["validity_not_before"] = validity_not_before

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''``AWS::ACMPCA::Certificate.CertificateAuthorityArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-certificateauthorityarn
        '''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_signing_request(self) -> builtins.str:
        '''``AWS::ACMPCA::Certificate.CertificateSigningRequest``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-certificatesigningrequest
        '''
        result = self._values.get("certificate_signing_request")
        assert result is not None, "Required property 'certificate_signing_request' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signing_algorithm(self) -> builtins.str:
        '''``AWS::ACMPCA::Certificate.SigningAlgorithm``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-signingalgorithm
        '''
        result = self._values.get("signing_algorithm")
        assert result is not None, "Required property 'signing_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validity(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnCertificate.ValidityProperty]:
        '''``AWS::ACMPCA::Certificate.Validity``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-validity
        '''
        result = self._values.get("validity")
        assert result is not None, "Required property 'validity' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnCertificate.ValidityProperty], result)

    @builtins.property
    def api_passthrough(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificate.ApiPassthroughProperty]]:
        '''``AWS::ACMPCA::Certificate.ApiPassthrough``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-apipassthrough
        '''
        result = self._values.get("api_passthrough")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificate.ApiPassthroughProperty]], result)

    @builtins.property
    def template_arn(self) -> typing.Optional[builtins.str]:
        '''``AWS::ACMPCA::Certificate.TemplateArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-templatearn
        '''
        result = self._values.get("template_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validity_not_before(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificate.ValidityProperty]]:
        '''``AWS::ACMPCA::Certificate.ValidityNotBefore``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html#cfn-acmpca-certificate-validitynotbefore
        '''
        result = self._values.get("validity_not_before")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCertificate.ValidityProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnPermission(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-acmpca.CfnPermission",
):
    '''A CloudFormation ``AWS::ACMPCA::Permission``.

    :cloudformationResource: AWS::ACMPCA::Permission
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        actions: typing.Sequence[builtins.str],
        certificate_authority_arn: builtins.str,
        principal: builtins.str,
        source_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::ACMPCA::Permission``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param actions: ``AWS::ACMPCA::Permission.Actions``.
        :param certificate_authority_arn: ``AWS::ACMPCA::Permission.CertificateAuthorityArn``.
        :param principal: ``AWS::ACMPCA::Permission.Principal``.
        :param source_account: ``AWS::ACMPCA::Permission.SourceAccount``.
        '''
        props = CfnPermissionProps(
            actions=actions,
            certificate_authority_arn=certificate_authority_arn,
            principal=principal,
            source_account=source_account,
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
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.List[builtins.str]:
        '''``AWS::ACMPCA::Permission.Actions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-actions
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actions"))

    @actions.setter
    def actions(self, value: typing.List[builtins.str]) -> None:
        jsii.set(self, "actions", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''``AWS::ACMPCA::Permission.CertificateAuthorityArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-certificateauthorityarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: builtins.str) -> None:
        jsii.set(self, "certificateAuthorityArn", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        '''``AWS::ACMPCA::Permission.Principal``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-principal
        '''
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        jsii.set(self, "principal", value)

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="sourceAccount")
    def source_account(self) -> typing.Optional[builtins.str]:
        '''``AWS::ACMPCA::Permission.SourceAccount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-sourceaccount
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceAccount"))

    @source_account.setter
    def source_account(self, value: typing.Optional[builtins.str]) -> None:
        jsii.set(self, "sourceAccount", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-acmpca.CfnPermissionProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "certificate_authority_arn": "certificateAuthorityArn",
        "principal": "principal",
        "source_account": "sourceAccount",
    },
)
class CfnPermissionProps:
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        certificate_authority_arn: builtins.str,
        principal: builtins.str,
        source_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``AWS::ACMPCA::Permission``.

        :param actions: ``AWS::ACMPCA::Permission.Actions``.
        :param certificate_authority_arn: ``AWS::ACMPCA::Permission.CertificateAuthorityArn``.
        :param principal: ``AWS::ACMPCA::Permission.Principal``.
        :param source_account: ``AWS::ACMPCA::Permission.SourceAccount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html
        '''
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "certificate_authority_arn": certificate_authority_arn,
            "principal": principal,
        }
        if source_account is not None:
            self._values["source_account"] = source_account

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''``AWS::ACMPCA::Permission.Actions``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-actions
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''``AWS::ACMPCA::Permission.CertificateAuthorityArn``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-certificateauthorityarn
        '''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''``AWS::ACMPCA::Permission.Principal``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_account(self) -> typing.Optional[builtins.str]:
        '''``AWS::ACMPCA::Permission.SourceAccount``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-permission.html#cfn-acmpca-permission-sourceaccount
        '''
        result = self._values.get("source_account")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-acmpca.ICertificateAuthority")
class ICertificateAuthority(aws_cdk.core.IResource, typing_extensions.Protocol):
    '''Interface which all CertificateAuthority based class must implement.'''

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name of the Certificate.

        :attribute: true
        '''
        ...


class _ICertificateAuthorityProxy(
    jsii.proxy_for(aws_cdk.core.IResource) # type: ignore[misc]
):
    '''Interface which all CertificateAuthority based class must implement.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-acmpca.ICertificateAuthority"

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name of the Certificate.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateAuthority).__jsii_proxy_class__ = lambda : _ICertificateAuthorityProxy


__all__ = [
    "CertificateAuthority",
    "CfnCertificate",
    "CfnCertificateAuthority",
    "CfnCertificateAuthorityActivation",
    "CfnCertificateAuthorityActivationProps",
    "CfnCertificateAuthorityProps",
    "CfnCertificateProps",
    "CfnPermission",
    "CfnPermissionProps",
    "ICertificateAuthority",
]

publication.publish()
