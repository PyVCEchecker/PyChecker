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
