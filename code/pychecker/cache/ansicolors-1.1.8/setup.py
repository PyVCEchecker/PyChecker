#!/usr/bin/env python

from setuptools import setup

import colors


setup(
    name='ansicolors',
    version='1.1.8',
    description='ANSI colors for Python',
    long_description=open('README.rst').read(),
    author='Giorgos Verigakis',
    author_email='verigak@gmail.com',
    maintainer='Jonathan Eunice',
    maintainer_email='jonathan.eunice@gmail.com',
    url='http://github.com/jonathaneunice/colors/',
    license='ISC',
    packages=['colors'],
    install_requires=[],
    test_requore=['tox', 'pytest', 'coverage', 'pytest-cov'],
    test_suite="test",
    zip_safe=False,
    keywords='ASNI color style console',

    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
