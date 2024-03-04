##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.i18nmessageid package
"""
from __future__ import print_function

import os
import sys

from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError
from distutils.errors import DistutilsExecError
from distutils.errors import DistutilsPlatformError
import platform

from setuptools import setup, find_packages, Extension

py_impl = getattr(platform, 'python_implementation', lambda: None)
is_pypy = py_impl() == 'PyPy'
is_jython = 'java' in sys.platform

codeoptimization_c = os.path.join('src', 'zope', 'i18nmessageid',
                                  "_zope_i18nmessageid_message.c")
codeoptimization = [
    Extension(
        "zope.i18nmessageid._zope_i18nmessageid_message",
        [os.path.normcase(codeoptimization_c)]
    ),
]

ext_modules = []
if not is_pypy and not is_jython:
    # Jython cannot build the C optimizations, while on PyPy they are
    # anti-optimizations (the C extension compatibility layer is known-slow,
    # and defeats JIT opportunities).
    ext_modules = codeoptimization


tests_require = [
    'zope.testrunner',
    'coverage',
]

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as stream:
        return stream.read()


class optional_build_ext(build_ext):
    """This class subclasses build_ext and allows
       the building of C extensions to fail.
    """
    def run(self):
        try:
            build_ext.run(self)
        except DistutilsPlatformError as e:
            self._unavailable(e)

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, DistutilsExecError) as e:
            self._unavailable(e)

    def _unavailable(self, e):
        print('*' * 80, file=sys.stderr)
        print("""WARNING:

        An optional code optimization (C extension) could not be compiled.

        Optimizations for this package will not be available!

        """, file=sys.stderr)
        print(str(e), file=sys.stderr)
        print('*' * 80, file=sys.stderr)



setup(
    name='zope.i18nmessageid',
    version='5.0.1',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    description='Message Identifiers for internationalization',
    long_description=(
        read('README.rst')
        + '\n\n' +
        read('CHANGES.rst')
        ),
    keywords="zope i18n message factory",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope :: 3',
    ],
    license='ZPL 2.1',
    url='https://github.com/zopefoundation/zope.i18nmessageid',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['zope'],
    install_requires=['setuptools', 'six'],
    include_package_data=True,
    test_suite='zope.i18nmessageid.tests.test_suite',
    zip_safe=False,
    cmdclass={'build_ext': optional_build_ext},
    ext_modules=ext_modules,
    tests_require=tests_require,
    extras_require={
        'testing': tests_require,
        'test': tests_require,
        'docs': ['Sphinx'],
    },
)
