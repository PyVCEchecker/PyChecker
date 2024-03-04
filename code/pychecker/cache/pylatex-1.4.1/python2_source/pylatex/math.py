# -*- coding: utf-8 -*-
u"""
This module implements the classes that deal with math.

..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import super
from builtins import int
from future import standard_library
standard_library.install_aliases()
from .base_classes import Command, Container, Environment
from .package import Package


class Alignat(Environment):
    u"""Class that represents a aligned equation environment."""

    #: Alignat environment cause compile errors when they do not contain items.
    #: This is why it is omitted fully if they are empty.
    omit_if_empty = True
    packages = [Package(u'amsmath')]

    def __init__(self, aligns=2, numbering=True, escape=None):
        u"""
        Parameters
        ----------
        aligns : int
            number of alignments
        numbering : bool
            Whether to number equations
        escape : bool
            if True, will escape strings
        """
        self.aligns = aligns
        self.numbering = numbering
        self.escape = escape
        if not numbering:
            self._star_latex_name = True
        super(Alignat, self).__init__(start_arguments=[unicode(int(aligns))])


class Math(Container):
    u"""A class representing a math environment."""

    packages = [Package(u'amsmath')]

    content_separator = u' '

    def __init__(self, **_3to2kwargs):
        if 'escape' in _3to2kwargs: escape = _3to2kwargs['escape']; del _3to2kwargs['escape']
        else: escape = None
        if 'data' in _3to2kwargs: data = _3to2kwargs['data']; del _3to2kwargs['data']
        else: data = None
        if 'inline' in _3to2kwargs: inline = _3to2kwargs['inline']; del _3to2kwargs['inline']
        else: inline = False
        ur"""
        Args
        ----
        data: list
            Content of the math container.
        inline: bool
            If the math should be displayed inline or not.
        escape : bool
            if True, will escape strings
        """

        self.inline = inline
        self.escape = escape
        super(Math, self).__init__(data=data)

    def dumps(self):
        u"""Return a LaTeX formatted string representing the object.

        Returns
        -------
        str

        """
        if self.inline:
            return u'$' + self.dumps_content() + u'$'
        return u'\\[%\n' + self.dumps_content() + u'%\n\\]'


class VectorName(Command):
    u"""A class representing a named vector."""

    _repr_attributes_mapping = {
        u'name': u'arguments',
    }

    def __init__(self, name):
        u"""
        Args
        ----
        name: str
            Name of the vector
        """

        super(VectorName, self).__init__(u'mathbf', arguments=name)


class Matrix(Environment):
    u"""A class representing a matrix."""

    packages = [Package(u'amsmath')]

    _repr_attributes_mapping = {
        u'alignment': u'arguments',
    }

    def __init__(self, matrix, **_3to2kwargs):
        if 'alignment' in _3to2kwargs: alignment = _3to2kwargs['alignment']; del _3to2kwargs['alignment']
        else: alignment = None
        if 'mtype' in _3to2kwargs: mtype = _3to2kwargs['mtype']; del _3to2kwargs['mtype']
        else: mtype = u'p'
        ur"""
        Args
        ----
        matrix: `numpy.ndarray` instance
            The matrix to display
        mtype: str
            What kind of brackets are used around the matrix. The different
            options and their corresponding brackets are:
            p = ( ), b = [ ], B = { }, v = \| \|, V = \|\| \|\|
        alignment: str
            How to align the content of the cells in the matrix. This is ``c``
            by default.

        References
        ----------
        * https://en.wikibooks.org/wiki/LaTeX/Mathematics#Matrices_and_arrays
        """

        import numpy  # noqa, Sanity check if numpy is installed

        self.matrix = matrix

        self.latex_name = mtype + u'matrix'
        self._mtype = mtype
        if alignment is not None:
            self.latex_name += u'*'

        super(Matrix, self).__init__(arguments=alignment)

    def dumps_content(self):
        u"""Return a string representing the matrix in LaTeX syntax.

        Returns
        -------
        str
        """

        import numpy as np

        string = u''
        shape = self.matrix.shape

        for (y, x), value in np.ndenumerate(self.matrix):
            if x:
                string += u'&'
            string += unicode(value)

            if x == shape[1] - 1 and y != shape[0] - 1:
                string += ur'\\' + u'%\n'

        super(Matrix, self).dumps_content()

        return string
