# -*- coding: utf-8 -*-
u"""
This module implements the class that deals with packages.

..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import super
from future import standard_library
standard_library.install_aliases()
from .base_classes import CommandBase


class Package(CommandBase):
    u"""A class that represents a package."""

    _latex_name = u'usepackage'

    _repr_attributes_mapping = {
        u'name': u'arguments',
    }

    def __init__(self, name, options=None):
        u"""
        Args
        ----
        name: str
            Name of the package.
        options: `str`, `list` or `~.Options`
            Options of the package.

        """

        super(Package, self).__init__(arguments=name, options=options)
