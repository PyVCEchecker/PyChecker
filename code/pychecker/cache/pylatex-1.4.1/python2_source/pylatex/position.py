# -*- coding: utf-8 -*-
u"""
This module implements the classes that deal with positioning.

Positions various elements on the page.

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
from .base_classes import Environment, SpecialOptions, Command, CommandBase
from .package import Package
from .utils import NoEscape


class HorizontalSpace(CommandBase):
    u"""Add/remove the amount of horizontal space between elements."""

    _latex_name = u'hspace'

    _repr_attributes_mapping = {
        u"size": u"arguments"
    }

    def __init__(self, size, **_3to2kwargs):
        if 'star' in _3to2kwargs: star = _3to2kwargs['star']; del _3to2kwargs['star']
        else: star = True
        u"""
        Args
        ----
        size: str
            The amount of space to add
        star: bool
            Use the star variant of the command. Enabling this makes sure the
            space is also added where page breaking takes place.
        """

        if star:
            self.latex_name += u'*'

        super(HorizontalSpace, self).__init__(arguments=size)


class VerticalSpace(HorizontalSpace):
    u"""Add the user specified amount of vertical space to the document."""

    _latex_name = u'vspace'


class Center(Environment):
    ur"""Centered environment."""

    packages = [Package(u'ragged2e')]


class FlushLeft(Center):
    ur"""Left-aligned environment."""


class FlushRight(Center):
    ur"""Right-aligned environment."""


class MiniPage(Environment):
    ur"""A class that allows the creation of minipages within document pages."""

    packages = [Package(u'ragged2e')]

    _repr_attributes_mapping = {
        u"width": u"arguments",
        u"pos": u"options",
        u"height": u"options",
        u"content_pos": u"options",
        u"align": u"options"
    }

    def __init__(self, **_3to2kwargs):
        if 'data' in _3to2kwargs: data = _3to2kwargs['data']; del _3to2kwargs['data']
        else: data = None
        if 'fontsize' in _3to2kwargs: fontsize = _3to2kwargs['fontsize']; del _3to2kwargs['fontsize']
        else: fontsize = None
        if 'align' in _3to2kwargs: align = _3to2kwargs['align']; del _3to2kwargs['align']
        else: align = None
        if 'content_pos' in _3to2kwargs: content_pos = _3to2kwargs['content_pos']; del _3to2kwargs['content_pos']
        else: content_pos = None
        if 'height' in _3to2kwargs: height = _3to2kwargs['height']; del _3to2kwargs['height']
        else: height = None
        if 'pos' in _3to2kwargs: pos = _3to2kwargs['pos']; del _3to2kwargs['pos']
        else: pos = None
        if 'width' in _3to2kwargs: width = _3to2kwargs['width']; del _3to2kwargs['width']
        else: width = NoEscape(ur'\textwidth')
        ur"""
        Args
        ----
        width: str
            width of the minipage
        pos: str
            The vertical alignment of the minipage relative to the baseline
            (center(c), top(t), bottom(b))
        height: str
            height of the minipage
        content_pos: str
            The position of the content inside the minipage (center(c),
            bottom(b), top(t), spread(s))
        align: str
            alignment of the minibox
        fontsize: str
            The font size of the minipage
        data: str or `~.LatexObject`
            The data to place inside the MiniPage element
        """

        options = []

        if pos is not None:
            options.append(pos)

        if height is not None:
            options.append(NoEscape(height))

        if ((content_pos is not None) and (pos is not None) and
           (height is not None)):
            options.append(content_pos)

        options = SpecialOptions(*options)

        arguments = [NoEscape(unicode(width))]

        extra_data = []

        if align is not None:
            if align == u"l":
                extra_data.append(Command(command=u"flushleft"))
            elif align == u"c":
                extra_data.append(Command(command=u"centering"))
            elif align == u"r":
                extra_data.append(Command(command=u"flushright"))

        if fontsize is not None:
            extra_data.append(Command(command=fontsize))

        if data is not None:
            if isinstance(data, list):
                data = extra_data + data
            else:
                data = extra_data + [data]
        else:
            data = extra_data

        super(MiniPage, self).__init__(arguments=arguments, options=options, data=data)


class TextBlock(Environment):
    ur"""A class that represents a textblock environment.

    Make sure to set lengths of TPHorizModule and TPVertModule
    """

    _repr_attributes_mapping = {
        u"width": u"arguments"
    }

    packages = [Package(u'textpos')]

    def __init__(self, width, horizontal_pos, vertical_pos, **_3to2kwargs):
        if 'data' in _3to2kwargs: data = _3to2kwargs['data']; del _3to2kwargs['data']
        else: data = None
        if 'indent' in _3to2kwargs: indent = _3to2kwargs['indent']; del _3to2kwargs['indent']
        else: indent = False
        ur"""
        Args
        ----
        width: float
            Width of the text block in the units specified by TPHorizModule
        horizontal_pos: float
            Horizontal position in units specified by the TPHorizModule
        indent: bool
            Determines whether the text block has an indent before it
        vertical_pos: float
            Vertical position in units specified by the TPVertModule
        data: str or `~.LatexObject`
            The data to place inside the TextBlock element
        """

        arguments = width
        self.horizontal_pos = horizontal_pos
        self.vertical_pos = vertical_pos

        super(TextBlock, self).__init__(arguments=arguments)

        self.append(u"(%s, %s)" % (unicode(self.horizontal_pos),
                    unicode(self.vertical_pos)))

        if not indent:
            self.append(NoEscape(ur'\noindent'))
