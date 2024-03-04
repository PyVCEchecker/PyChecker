# -*- coding: utf-8 -*-
u"""
This module implements the classes that deal with adding frames.

..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from .base_classes import Environment, ContainerCommand
from .package import Package


class MdFramed(Environment):
    u"""A class that defines an mdframed environment."""

    packages = [Package(u'mdframed')]


class FBox(ContainerCommand):
    u"""A class that defines an fbox ContainerCommand."""
