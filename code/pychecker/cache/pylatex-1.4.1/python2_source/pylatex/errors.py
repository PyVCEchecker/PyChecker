# -*- coding: utf-8 -*-
u"""
This module implements Error classes.

..  :copyright: (c) 2015 by Rene Beckmann.
    :license: MIT, see License for more details.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from future import standard_library
standard_library.install_aliases()
class PyLaTeXError(Exception):
    u"""A Base class for all PyLaTeX Exceptions."""


class CompilerError(PyLaTeXError):
    u"""A Base class for all PyLaTeX compiler related Exceptions."""


class TableError(PyLaTeXError):
    u"""A Base class for all errors concerning tables."""


class TableRowSizeError(TableError):
    u"""Error for wrong table row size."""
