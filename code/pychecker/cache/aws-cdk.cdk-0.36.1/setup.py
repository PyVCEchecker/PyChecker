import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.cdk",
    "version": "0.36.1",
    "description": "Deprecated: this module ha been renamed to @aws-cdk/core",
    "url": "https://github.com/awslabs/aws-cdk",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "project_urls": {
        "Source": "https://github.com/awslabs/aws-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.cdk._jsii"
    ],
    "package_data": {
        "aws_cdk.cdk._jsii": [
            "cdk@0.36.1.jsii.tgz"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii~=0.13.2",
        "publication>=0.0.3"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
