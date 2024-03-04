# -*- coding: utf-8 -*-
u"""
This module implements the section type classes.

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
from .base_classes import Container, Command
from .labelref import Marker, Label


class Section(Container):
    u"""A class that represents a section."""

    #: A section should normally start in its own paragraph
    end_paragraph = True

    #: Default prefix to use with Marker
    marker_prefix = u"sec"

    #: Number the sections when the section element is compatible,
    #: by changing the `~.Section` class default all
    #: subclasses will also have the new default.
    numbering = True

    def __init__(self, title, numbering=None, **kwargs):
        if 'label' in kwargs: label = kwargs['label']; del kwargs['label']
        else: label = True
        u"""
        Args
        ----
        title: str
            The section title.
        numbering: bool
            Add a number before the section title.
        label: Label or bool or str
            Can set a label manually or use a boolean to set
            preference between automatic or no label
        """

        self.title = title

        if numbering is not None:
            self.numbering = numbering
        if isinstance(label, Label):
            self.label = label
        elif isinstance(label, unicode):
            if u':' in label:
                label = label.split(u':', 1)
                self.label = Label(Marker(label[1], label[0]))
            else:
                self.label = Label(Marker(label, self.marker_prefix))
        elif label:
            self.label = Label(Marker(title, self.marker_prefix))
        else:
            self.label = None

        super(Section, self).__init__(**kwargs)

    def dumps(self):
        u"""Represent the section as a string in LaTeX syntax.

        Returns
        -------
        str

        """

        if not self.numbering:
            num = u'*'
        else:
            num = u''

        string = Command(self.latex_name + num, self.title).dumps()
        if self.label is not None:
            string += u'%\n' + self.label.dumps()
        string += u'%\n' + self.dumps_content()

        return string


class Part(Section):
    u"""A class that represents a part."""

    marker_prefix = u"part"


class Chapter(Section):
    u"""A class that represents a chapter."""

    marker_prefix = u"chap"


class Subsection(Section):
    u"""A class that represents a subsection."""

    marker_prefix = u"subsec"


class Subsubsection(Section):
    u"""A class that represents a subsubsection."""

    marker_prefix = u"ssubsec"


class Paragraph(Section):
    u"""A class that represents a paragraph."""

    marker_prefix = u"para"


class Subparagraph(Section):
    u"""A class that represents a subparagraph."""

    marker_prefix = u"subpara"
