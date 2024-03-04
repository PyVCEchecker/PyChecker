#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

import virus_total_apis

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

version = virus_total_apis.__version__

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='virustotal-api',
    version=virus_total_apis.__version__,
    description='Virus Total Public/Private/Intel API',
    long_description=readme + '\n\n' + history,
    url='https://github.com/blacktop/virustotal-api',
    author='blacktop',
    author_email='dev@blacktop.io',
    license=virus_total_apis.__license__,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite="tests",
    packages=['virus_total_apis'],
    package_data={'': ['LICENSE', 'NOTICE']},
    package_dir={'virus_total_apis': 'virus_total_apis'},
    include_package_data=True,
    install_requires=["requests >= 2.22.0"])
