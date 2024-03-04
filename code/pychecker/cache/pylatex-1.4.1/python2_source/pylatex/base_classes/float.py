# -*- coding: utf-8 -*-
u"""
This module implements the classes that deal with floating environments.

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
from . import Environment, Command


class Float(Environment):
    u"""A class that represents a floating environment."""

    #: By default floats are positioned inside a separate paragraph.
    #: Setting this to option to `False` will change that.
    separate_paragraph = True

    _repr_attributes_mapping = {
        u'position': u'options',
    }

    def __init__(self, **kwargs):
        if 'position' in kwargs: position = kwargs['position']; del kwargs['position']
        else: position = None
        u"""
        Args
        ----
        position: str
            Define the positioning of a floating environment, for instance
            ``'h'``. See the references for more information.

        References
        ----------
            * https://www.sharelatex.com/learn/Positioning_of_Figures
        """

        super(Float, self).__init__(options=position, **kwargs)

    def add_caption(self, caption):
        u"""Add a caption to the float.

        Args
        ----
        caption: str
            The text of the caption.
        """

        self.append(Command(u'caption', caption))
