# -*- coding: utf-8 -*-
u"""
This module implements LaTeX base classes that can be subclassed.

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
from collections import UserList
from pylatex.utils import dumps_list
from contextlib import contextmanager
from .latex_object import LatexObject
from .command import Command, Arguments


class Container(LatexObject, UserList):
    u"""A base class that groups multiple LaTeX classes.

    This class should be subclassed when a LaTeX class has content that is of
    variable length. It subclasses UserList, so it holds a list of elements
    that can simply be accessed by using normal list functionality, like
    indexing or appending.

    """

    content_separator = u'%\n'

    def __init__(self, **_3to2kwargs):
        if 'data' in _3to2kwargs: data = _3to2kwargs['data']; del _3to2kwargs['data']
        else: data = None
        ur"""
        Args
        ----
        data: list, `~.LatexObject` or something that can be converted to a \
                string
            The content with which the container is initialized
        """

        if data is None:
            data = []
        elif not isinstance(data, list):
            # If the data is not already a list make it a list, otherwise list
            # operations will not work
            data = [data]

        self.data = data
        self.real_data = data  # Always the data of this instance

        super(Container, self).__init__()

    @property
    def _repr_attributes(self):
        return super(Container, self)._repr_attributes + [u'real_data']

    def dumps_content(self, **kwargs):
        ur"""Represent the container as a string in LaTeX syntax.

        Args
        ----
        \*\*kwargs:
            Arguments that can be passed to `~.dumps_list`


        Returns
        -------
        string:
            A LaTeX string representing the container
        """

        return dumps_list(self, escape=self.escape,
                          token=self.content_separator, **kwargs)

    def _propagate_packages(self):
        u"""Make sure packages get propagated."""

        for item in self.data:
            if isinstance(item, LatexObject):
                if isinstance(item, Container):
                    item._propagate_packages()
                for p in item.packages:
                    self.packages.add(p)

    def dumps_packages(self):
        ur"""Represent the packages needed as a string in LaTeX syntax.

        Returns
        -------
        string:
            A LaTeX string representing the packages of the container
        """

        self._propagate_packages()

        return super(Container, self).dumps_packages()

    @contextmanager
    def create(self, child):
        u"""Add a LaTeX object to current container, context-manager style.

        Args
        ----
        child: `~.Container`
            An object to be added to the current container
        """

        prev_data = self.data
        self.data = child.data  # This way append works appends to the child

        yield child  # allows with ... as to be used as well

        self.data = prev_data
        self.append(child)


class Environment(Container):
    ur"""A base class for LaTeX environments.

    This class implements the basics of a LaTeX environment. A LaTeX
    environment looks like this:

    .. code-block:: latex

        \begin{environment_name}
            Some content that is in the environment
        \end{environment_name}

    The text that is used in the place of environment_name is by default the
    name of the class in lowercase.
    However, this default can be overridden in 2 ways:
    1. setting the _latex_name class variable when declaring the class
    2. setting the _latex_name attribute when initialising object
    """

    #: Set to true if this full container should be equivalent to an empty
    #: string if it has no content.
    omit_if_empty = False

    def __init__(self,
                 **kwargs):
        if 'start_arguments' in kwargs: start_arguments = kwargs['start_arguments']; del kwargs['start_arguments']
        else: start_arguments = None
        if 'arguments' in kwargs: arguments = kwargs['arguments']; del kwargs['arguments']
        else: arguments = None
        if 'options' in kwargs: options = kwargs['options']; del kwargs['options']
        else: options = None
        ur"""
        Args
        ----
        options: str or list or  `~.Options`
            Options to be added to the ``\begin`` command

        arguments: str or list or `~.Arguments`
            Arguments to be added to the ``\begin`` command

        start_arguments: str or list or `~.Arguments`
            Arguments to be added before the options
        """

        self.options = options
        self.arguments = arguments
        self.start_arguments = start_arguments

        super(Environment, self).__init__(**kwargs)

    def dumps(self):
        u"""Represent the environment as a string in LaTeX syntax.

        Returns
        -------
        str
            A LaTeX string representing the environment.
        """

        content = self.dumps_content()
        if not content.strip() and self.omit_if_empty:
            return u''

        string = u''

        # Something other than None needs to be used as extra arguments, that
        # way the options end up behind the latex_name argument.
        if self.arguments is None:
            extra_arguments = Arguments()
        else:
            extra_arguments = self.arguments

        begin = Command(u'begin', self.start_arguments, self.options,
                        extra_arguments=extra_arguments)
        begin.arguments._positional_args.insert(0, self.latex_name)
        string += begin.dumps() + self.content_separator

        string += content + self.content_separator

        string += Command(u'end', self.latex_name).dumps()

        return string


class Fragment(Container):
    ur"""A LaTeX fragment container class for fragmented document construction.

    This only provides logical wrapping of the items. The final document will
    look the same as if all items would not have been part of a container.

    A common usecase of this is to generate a .tex snippet containing more than
    one LaTeX item item without any extra container around it. This snippet can
    then be included in another ``.tex`` file using ``\input{snippet.tex}``
    """

    def __init__(self, **kwargs):
        u"""
        Args
        ----
        """

        super(Fragment, self).__init__(**kwargs)

    def dumps(self):
        u"""Represent the fragment as a string in LaTeX syntax.
        Returns
        -------
        str
        """

        return self.dumps_content()


class ContainerCommand(Container):
    ur"""A base class for a container command (A command which contains data).

    Container command example:

    .. code-block:: latex

        \CommandName[options]{arguments}{
            data
        }

    """

    omit_if_empty = False

    def __init__(self, arguments=None, options=None, **kwargs):
        if 'data' in kwargs: data = kwargs['data']; del kwargs['data']
        else: data = None
        ur"""
        Args
        ----
        arguments: str or `list`
            The arguments for the container command
        options: str, list or `~.Options`
            The options for the preamble command
        data: str or `~.LatexObject`
            The data to place inside the preamble command
        """

        self.arguments = arguments
        self.options = options

        super(ContainerCommand, self).__init__(data=data, **kwargs)

    def dumps(self):
        ur"""Convert the container to a string in latex syntax."""

        content = self.dumps_content()

        if not content.strip() and self.omit_if_empty:
            return u''

        string = u''

        start = Command(self.latex_name, arguments=self.arguments,
                        options=self.options)

        string += start.dumps() + u'{%\n'

        if content != u'':
            string += content + u'%\n}'
        else:
            string += u'}'

        return string
