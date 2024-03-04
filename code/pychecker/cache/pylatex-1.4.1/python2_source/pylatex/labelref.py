# -*- coding: utf-8 -*-
u"""This module implements the label command and reference."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import super
from future import standard_library
standard_library.install_aliases()
from .base_classes import CommandBase
from .package import Package
from .base_classes import LatexObject
from itertools import imap


def _remove_invalid_char(s):
    u"""Remove invalid and dangerous characters from a string."""

    s = u''.join([i if ord(i) >= 32 and ord(i) < 127 else u'' for i in s])
    s = s.translate(dict.fromkeys(imap(ord, u"&%$#_{}~^\\\n\xA0[]\":;' ")))
    return s


class Marker(LatexObject):
    u"""A class that represents a marker (label/ref parameter)."""

    _repr_attributes_override = [
        u'name',
        u'prefix',
    ]

    def __init__(self, name, prefix=u"", del_invalid_char=True):
        u"""
        Args
        ----
        name: str
            Name of the marker.
        prefix: str
            Prefix to add before the name (prefix:name).
        del_invalid_char: bool
            If True invalid and dangerous characters will be
            removed from the marker
        """

        if del_invalid_char:
            prefix = _remove_invalid_char(prefix)
            name = _remove_invalid_char(name)
        self.prefix = prefix
        self.name = name

    def __str__(self):
        return ((self.prefix + u":") if self.prefix != u"" else u"") + self.name

    def dumps(self):
        u"""Represent the Marker as a string in LaTeX syntax.

        Returns
        -------
        str

        """
        return unicode(self)


class RefLabelBase(CommandBase):
    u"""A class used as base for command that take a marker only."""

    _repr_attributes_mapping = {
        u'marker': u'arguments',
    }

    def __init__(self, marker):
        u"""
        Args
        ----
        marker: Marker
            The marker to use with the label/ref.
        """

        self.marker = marker
        super(RefLabelBase, self).__init__(arguments=(unicode(marker)))


class Label(RefLabelBase):
    u"""A class that represents a label."""


class Ref(RefLabelBase):
    u"""A class that represents a reference."""


class Pageref(RefLabelBase):
    u"""A class that represents a page reference."""


class Eqref(RefLabelBase):
    u"""A class that represent a ref to a formulae."""

    packages = [Package(u'amsmath')]


class Cref(RefLabelBase):
    u"""A class that represent a cref (not a Cref)."""

    packages = [Package(u'cleveref')]


class CrefUp(RefLabelBase):
    u"""A class that represent a Cref."""

    packages = [Package(u'cleveref')]
    latex_name = u'Cref'


class Autoref(RefLabelBase):
    u"""A class that represent an autoref."""

    packages = [Package(u'hyperref')]


class Hyperref(CommandBase):
    u"""A class that represents an hyperlink to a label."""

    _repr_attributes_mapping = {
        u'marker': u'options',
        u'text': u'arguments',
    }

    packages = [Package(u'hyperref')]

    def __init__(self, marker, text):
        u"""
        Args
        ----
        marker: Marker
            The marker to use with the label/ref.
        text: str
            The text that will be shown as a link
            to the label of the same marker.
        """

        self.marker = marker
        super(Hyperref, self).__init__(options=(unicode(marker)), arguments=text)
