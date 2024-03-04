# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_lambda_powertools',
 'aws_lambda_powertools.event_handler',
 'aws_lambda_powertools.exceptions',
 'aws_lambda_powertools.logging',
 'aws_lambda_powertools.metrics',
 'aws_lambda_powertools.middleware_factory',
 'aws_lambda_powertools.shared',
 'aws_lambda_powertools.tracing',
 'aws_lambda_powertools.utilities',
 'aws_lambda_powertools.utilities.batch',
 'aws_lambda_powertools.utilities.data_classes',
 'aws_lambda_powertools.utilities.data_classes.appsync',
 'aws_lambda_powertools.utilities.feature_flags',
 'aws_lambda_powertools.utilities.idempotency',
 'aws_lambda_powertools.utilities.idempotency.persistence',
 'aws_lambda_powertools.utilities.jmespath_utils',
 'aws_lambda_powertools.utilities.parameters',
 'aws_lambda_powertools.utilities.parser',
 'aws_lambda_powertools.utilities.parser.envelopes',
 'aws_lambda_powertools.utilities.parser.models',
 'aws_lambda_powertools.utilities.typing',
 'aws_lambda_powertools.utilities.validation']

package_data = \
{'': ['*']}

install_requires = \
['aws-xray-sdk>=2.8.0,<3.0.0',
 'boto3>=1.18,<2.0',
 'fastjsonschema>=2.14.5,<3.0.0',
 'jmespath>=0.10.0,<0.11.0']

extras_require = \
{'pydantic': ['pydantic>=1.8.2,<2.0.0', 'email-validator']}

setup_kwargs = {
    'name': 'aws-lambda-powertools',
    'version': '1.21.1',
    'description': 'A suite of utilities for AWS Lambda functions to ease adopting best practices such as tracing, structured logging, custom metrics, batching, idempotency, feature flags, and more.',
    'long_description': "# AWS Lambda Powertools (Python)\n\n![Build](https://github.com/awslabs/aws-lambda-powertools/workflows/Powertools%20Python/badge.svg?branch=master)\n[![codecov.io](https://codecov.io/github/awslabs/aws-lambda-powertools-python/branch/develop/graphs/badge.svg)](https://app.codecov.io/gh/awslabs/aws-lambda-powertools-python)\n![PythonSupport](https://img.shields.io/static/v1?label=python&message=3.6%20|%203.7|%203.8|%203.9&color=blue?style=flat-square&logo=python) ![PyPI version](https://badge.fury.io/py/aws-lambda-powertools.svg) ![PyPi monthly downloads](https://img.shields.io/pypi/dm/aws-lambda-powertools)\n\nA suite of Python utilities for AWS Lambda functions to ease adopting best practices such as tracing, structured logging, custom metrics, and more. ([AWS Lambda Powertools Java](https://github.com/awslabs/aws-lambda-powertools-java) is also available).\n\n\n\n**[📜Documentation](https://awslabs.github.io/aws-lambda-powertools-python/)** | **[🐍PyPi](https://pypi.org/project/aws-lambda-powertools/)** | **[Roadmap](https://github.com/awslabs/aws-lambda-powertools-roadmap/projects/1)** | **[Quick hello world example](https://github.com/aws-samples/cookiecutter-aws-sam-python)** | **[Detailed blog post](https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/)**\n\n> **An AWS Developer Acceleration (DevAx) initiative by Specialist Solution Architects | aws-devax-open-source@amazon.com**\n\n## Features\n\n* **[Tracing](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/tracer/)** - Decorators and utilities to trace Lambda function handlers, and both synchronous and asynchronous functions\n* **[Logging](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/logger/)** - Structured logging made easier, and decorator to enrich structured logging with key Lambda context details\n* **[Metrics](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/metrics/)** - Custom Metrics created asynchronously via CloudWatch Embedded Metric Format (EMF)\n* **[Event handler: AppSync](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/appsync/)** - AWS AppSync event handler for Lambda Direct Resolver and Amplify GraphQL Transformer function\n* **[Event handler: API Gateway and ALB](https://awslabs.github.io/aws-lambda-powertools-python/latest/core/event_handler/api_gateway/)** - Amazon API Gateway REST/HTTP API and ALB event handler for Lambda functions invoked using Proxy integration\n* **[Bring your own middleware](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/middleware_factory/)** - Decorator factory to create your own middleware to run logic before, and after each Lambda invocation\n* **[Parameters utility](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/parameters/)** - Retrieve and cache parameter values from Parameter Store, Secrets Manager, or DynamoDB\n* **[Batch processing](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/batch/)** - Handle partial failures for AWS SQS batch processing\n* **[Typing](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/typing/)** - Static typing classes to speedup development in your IDE\n* **[Validation](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/validation/)** - JSON Schema validator for inbound events and responses\n* **[Event source data classes](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/data_classes/)** - Data classes describing the schema of common Lambda event triggers\n* **[Parser](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/parser/)** - Data parsing and deep validation using Pydantic\n* **[Idempotency](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/idempotency/)** - Convert your Lambda functions into idempotent operations which are safe to retry\n* **[Feature Flags](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/feature_flags/)** - A simple rule engine to evaluate when one or multiple features should be enabled depending on the input\n\n### Installation\n\nWith [pip](https://pip.pypa.io/en/latest/index.html) installed, run: ``pip install aws-lambda-powertools``\n\n## Examples\n\n* [Serverless Shopping cart](https://github.com/aws-samples/aws-serverless-shopping-cart)\n* [Serverless Airline](https://github.com/aws-samples/aws-serverless-airline-booking)\n* [Serverless E-commerce platform](https://github.com/aws-samples/aws-serverless-ecommerce-platform)\n\n## Credits\n\n* Structured logging initial implementation from [aws-lambda-logging](https://gitlab.com/hadrien/aws_lambda_logging)\n* Powertools idea [DAZN Powertools](https://github.com/getndazn/dazn-lambda-powertools/)\n\n\n## Connect\n\n* **AWS Developers Slack**: `#lambda-powertools`** - **[Invite, if you don't have an account](https://join.slack.com/t/awsdevelopers/shared_invite/zt-gu30gquv-EhwIYq3kHhhysaZ2aIX7ew)**\n* **Email**: aws-lambda-powertools-feedback@amazon.com\n\n## License\n\nThis library is licensed under the MIT-0 License. See the LICENSE file.\n",
    'author': 'Amazon Web Services',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/awslabs/aws-lambda-powertools-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
