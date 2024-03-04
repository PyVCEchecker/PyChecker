import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-cdk.aws-dynamodb",
    "version": "1.129.0",
    "description": "The CDK Construct Library for AWS::DynamoDB",
    "license": "Apache-2.0",
    "url": "https://github.com/aws/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.aws_dynamodb",
        "aws_cdk.aws_dynamodb._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_dynamodb._jsii": [
            "aws-dynamodb@1.129.0.jsii.tgz"
        ],
        "aws_cdk.aws_dynamodb": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-applicationautoscaling==1.129.0",
        "aws-cdk.aws-cloudwatch==1.129.0",
        "aws-cdk.aws-iam==1.129.0",
        "aws-cdk.aws-kinesis==1.129.0",
        "aws-cdk.aws-kms==1.129.0",
        "aws-cdk.aws-lambda==1.129.0",
        "aws-cdk.core==1.129.0",
        "aws-cdk.custom-resources==1.129.0",
        "constructs>=3.3.69, <4.0.0",
        "jsii>=1.40.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved",
        "Framework :: AWS CDK",
        "Framework :: AWS CDK :: 1"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
