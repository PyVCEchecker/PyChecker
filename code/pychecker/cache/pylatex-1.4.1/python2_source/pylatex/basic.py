# -*- coding: utf-8 -*-
u"""
This module implements several classes that represent basic latex commands.

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
from .base_classes import CommandBase, Environment, ContainerCommand
from .package import Package


class NewPage(CommandBase):
    u"""A command that adds a new page to the document."""


class LineBreak(NewPage):
    u"""A command that adds a line break to the document."""


class NewLine(NewPage):
    u"""A command that adds a new line to the document."""


class HFill(NewPage):
    u"""A command that fills the current line in the document."""


class HugeText(Environment):
    u"""An environment which makes the text size 'Huge'."""

    _latex_name = u"Huge"

    def __init__(self, data=None):
        u"""
        Args
        ----
        data : str or `~.LatexObject`
            The string or LatexObject to be formatted.
        """

        super(HugeText, self).__init__(data=data)


class LargeText(HugeText):
    u"""An environment which makes the text size 'Large'."""

    _latex_name = u"Large"


class MediumText(HugeText):
    u"""An environment which makes the text size 'large'."""

    _latex_name = u"large"


class SmallText(HugeText):
    u"""An environment which makes the text size 'small'."""

    _latex_name = u"small"


class FootnoteText(HugeText):
    u"""An environment which makes the text size 'footnotesize'."""

    _latex_name = u"footnotesize"


class TextColor(ContainerCommand):
    u"""An environment which changes the text color of the data."""

    _repr_attributes_mapping = {
        u"color": u"arguments"
    }

    packages = [Package(u"xcolor")]

    def __init__(self, color, data):
        u"""
        Args
        ----
        color: str
            The color to set for the data inside of the environment.
        data: str or `~.LatexObject`
            The string or LatexObject to be formatted.
        """

        super(TextColor, self).__init__(arguments=color, data=data)
