#!/usr/bin/env python
"""metapackage to express dependency on pyzmq"""
from __future__ import print_function
import sys

from setuptools import setup

print("You probably meant 'pyzmq' not 'zmq'", file=sys.stderr)

setup(
    name='zmq',
    install_requires=['pyzmq'],
    version='0.0.0',
    description="You are probably looking for pyzmq.",
    long_description="PyZMQ provides Python bindings for libzmq.",
    author="Min RK",
    author_email="benjaminrk@gmail.com",
    url="https://github.com/zeromq/pyzmq",
    license="BSD",
)
