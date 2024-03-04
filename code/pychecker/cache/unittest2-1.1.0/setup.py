#! /usr/bin/env python
# setup.py
# Install script for unittest2
# Copyright (C) 2010 Michael Foord
# E-mail: fuzzyman AT voidspace DOT org DOT uk

# This software is licensed under the terms of the BSD license.
# http://www.voidspace.org.uk/python/license.shtml

import os
import sys

class late_version:
    def __str__(self):
        from unittest2 import __version__ as VERSION
        return VERSION
    def __add__(self, other):
        return str(self) + other
    def replace(self, old, new):
        return str(self).replace(old, new)
VERSION = late_version()

NAME = 'unittest2'

PACKAGES = ['unittest2', 'unittest2.test']

DESCRIPTION = ('The new features in unittest backported to '
               'Python 2.4+.')

URL = 'http://pypi.python.org/pypi/unittest2'

readme = os.path.join(os.path.dirname(__file__), 'README.txt')
LONG_DESCRIPTION = open(readme).read()

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.4',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Testing',
]

AUTHOR = 'Robert Collins'

AUTHOR_EMAIL = 'rbtcollins@hp.com'

KEYWORDS = "unittest testing tests".split(' ')

# Both install and setup requires - because we read VERSION from within the
# package, and the package also exports all the APIs.
# six for compat helpers
REQUIRES = ['argparse', 'six>=1.4', 'traceback2'],

params = dict(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=PACKAGES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=REQUIRES,
    setup_requires=REQUIRES,
)


from setuptools import setup
params['entry_points'] = {
    'console_scripts': [
        'unit2 = unittest2.__main__:main_',
    ],
}

params['test_suite'] = 'unittest2.collector'

setup(**params)
