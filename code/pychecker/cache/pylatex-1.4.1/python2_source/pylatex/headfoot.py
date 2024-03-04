# -*- coding: utf-8 -*-
u"""
This module implements the classes that deal with creating headers and footers.

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
from .base_classes import ContainerCommand, Command
from .package import Package
from .utils import NoEscape


class PageStyle(ContainerCommand):
    ur"""Allows the creation of new page styles."""

    _latex_name = u"fancypagestyle"

    packages = [Package(u'fancyhdr')]

    def __init__(self, name, **_3to2kwargs):
        if 'data' in _3to2kwargs: data = _3to2kwargs['data']; del _3to2kwargs['data']
        else: data = None
        if 'footer_thickness' in _3to2kwargs: footer_thickness = _3to2kwargs['footer_thickness']; del _3to2kwargs['footer_thickness']
        else: footer_thickness = 0
        if 'header_thickness' in _3to2kwargs: header_thickness = _3to2kwargs['header_thickness']; del _3to2kwargs['header_thickness']
        else: header_thickness = 0
        ur"""
        Args
        ----
        name: str
            The name of the page style
        header_thickness: float
            Value to set for the line under the header
        footer_thickness: float
            Value to set for the line over the footer
        data: str or `~.LatexObject`
            The data to place inside the PageStyle
        """

        self.name = name

        super(PageStyle, self).__init__(data=data, arguments=self.name)

        self.change_thickness(element=u"header", thickness=header_thickness)
        self.change_thickness(element=u"footer", thickness=footer_thickness)

        # Clear the current header and footer
        self.append(Head())
        self.append(Foot())

    def change_thickness(self, element, thickness):
        ur"""Change line thickness.

        Changes the thickness of the line under/over the header/footer
        to the specified thickness.

        Args
        ----
        element: str
            the name of the element to change thickness for: header, footer
        thickness: float
            the thickness to set the line to
        """

        if element == u"header":
            self.data.append(Command(u"renewcommand",
                             arguments=[NoEscape(ur"\headrulewidth"),
                                        unicode(thickness) + u'pt']))
        elif element == u"footer":
            self.data.append(Command(u"renewcommand", arguments=[
                NoEscape(ur"\footrulewidth"), unicode(thickness) + u'pt']))


def simple_page_number():
    u"""Get a string containing commands to display the page number.

    Returns
    -------
    str
        The latex string that displays the page number
    """

    return NoEscape(ur'Page \thepage\ of \pageref{LastPage}')


class Head(ContainerCommand):
    ur"""Allows the creation of headers."""

    _latex_name = u"fancyhead"

    def __init__(self, position=None, **_3to2kwargs):
        if 'data' in _3to2kwargs: data = _3to2kwargs['data']; del _3to2kwargs['data']
        else: data = None
        ur"""
        Args
        ----
        position: str
            the headers position: L, C, R
        data: str or `~.LatexObject`
            The data to place inside the Head element
        """

        self.position = position

        super(Head, self).__init__(data=data, options=position)


class Foot(Head):
    ur"""Allows the creation of footers."""

    _latex_name = u"fancyfoot"
