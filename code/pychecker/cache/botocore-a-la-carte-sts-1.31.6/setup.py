#!/usr/bin/env python
from setuptools import setup

setup(
    name='botocore-a-la-carte-sts',
    version="1.31.6",
    description='sts data for botocore. See the `botocore-a-la-carte` package for more info.',
    author='Amazon Web Services',
    url='https://github.com/thejcannon/botocore-a-la-carte',
    scripts=[],
    packages=["botocore"],
    package_data={
        'botocore': ['data/sts/*/*.json'],
    },
    include_package_data=True,
    license="Apache License 2.0",
    python_requires=">= 3.7",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)
