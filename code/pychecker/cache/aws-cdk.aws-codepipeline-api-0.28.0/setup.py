import json
import setuptools

kwargs = json.loads("""
{
    "name": "aws-cdk.aws-codepipeline-api",
    "version": "0.28.0",
    "description": "Actions API for AWS Code Pipeline",
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
        "aws_cdk.aws_codepipeline_api._jsii"
    ],
    "package_data": {
        "aws_cdk.aws_codepipeline_api._jsii": [
            "aws-codepipeline-api@0.28.0.jsii.tgz"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii",
        "publication>=0.0.3"
    ]
}
""")

with open('README.md') as fp:
    kwargs['long_description'] = fp.read()


setuptools.setup(**kwargs)
