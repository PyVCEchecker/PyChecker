# -*- coding: utf-8 -*-
u"""
This module implements the classes used to show plots.

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
from .base_classes import LatexObject, Environment, Command, Options, Container
from .package import Package
import re
import math
from itertools import izip


class TikZOptions(Options):
    u"""Options class, do not escape."""

    escape = False

    def append_positional(self, option):
        u"""Add a new positional option."""

        self._positional_args.append(option)


class TikZ(Environment):
    u"""Basic TikZ container class."""

    _latex_name = u'tikzpicture'
    packages = [Package(u'tikz')]


class Axis(Environment):
    u"""PGFPlots axis container class, this contains plots."""

    packages = [Package(u'pgfplots'), Command(u'pgfplotsset', u'compat=newest')]

    def __init__(self, options=None, **_3to2kwargs):
        if 'data' in _3to2kwargs: data = _3to2kwargs['data']; del _3to2kwargs['data']
        else: data = None
        u"""
        Args
        ----
        options: str, list or `~.Options`
            Options to format the axis environment.
        """

        super(Axis, self).__init__(options=options, data=data)


class TikZScope(Environment):
    u"""TikZ Scope Environment."""

    _latex_name = u'scope'


class TikZCoordinate(LatexObject):
    u"""A General Purpose Coordinate Class."""

    _coordinate_str_regex = re.compile(ur'(\+\+)?\(\s*(-?[0-9]+(\.[0-9]+)?)\s*'
                                       ur',\s*(-?[0-9]+(\.[0-9]+)?)\s*\)')

    def __init__(self, x, y, relative=False):
        u"""
        Args
        ----
        x: float or int
            X coordinate
        y: float or int
            Y coordinate
        relative: bool
            Coordinate is relative or absolute
        """
        self._x = float(x)
        self._y = float(y)
        self.relative = relative

    def __repr__(self):
        if self.relative:
            ret_str = u'++'
        else:
            ret_str = u''
        return ret_str + u'({},{})'.format(self._x, self._y)

    def dumps(self):
        u"""Return representation."""

        return self.__repr__()

    @classmethod
    def from_str(cls, coordinate):
        u"""Build a TikZCoordinate object from a string."""

        m = cls._coordinate_str_regex.match(coordinate)

        if m is None:
            raise ValueError(u'invalid coordinate string')

        if m.group(1) == u'++':
            relative = True
        else:
            relative = False

        return TikZCoordinate(
            float(m.group(2)), float(m.group(4)), relative=relative)

    def __eq__(self, other):
        if isinstance(other, tuple):
            # if comparing to a tuple, assume it to be an absolute coordinate.
            other_relative = False
            other_x = float(other[0])
            other_y = float(other[1])
        elif isinstance(other, TikZCoordinate):
            other_relative = other.relative
            other_x = other._x
            other_y = other._y
        else:
            raise TypeError(u'can only compare tuple and TiKZCoordinate types')

        # prevent comparison between relative and non relative
        # by returning False
        if (other_relative != self.relative):
            return False

        # return comparison result
        return (other_x == self._x and other_y == self._y)

    def _arith_check(self, other):
        if isinstance(other, tuple):
            other_coord = TikZCoordinate(*other)
        elif isinstance(other, TikZCoordinate):
            if other.relative is True or self.relative is True:
                raise ValueError(u'refusing to add relative coordinates')
            other_coord = other
        else:
            raise TypeError(u'can only add tuple or TiKZCoordinate types')

        return other_coord

    def __add__(self, other):
        other_coord = self._arith_check(other)
        return TikZCoordinate(self._x + other_coord._x,
                              self._y + other_coord._y)

    def __radd__(self, other):
        self.__add__(other)

    def __sub__(self, other):
        other_coord = self._arith_check(other)
        return TikZCoordinate(self._x - other_coord._y,
                              self._y - other_coord._y)

    def distance_to(self, other):
        u"""Euclidean distance between two coordinates."""

        other_coord = self._arith_check(other)
        return math.sqrt(math.pow(self._x - other_coord._x, 2) +
                         math.pow(self._y - other_coord._y, 2))


class TikZObject(Container):
    u"""Abstract Class that most TikZ Objects inherits from."""

    def __init__(self, options=None):
        u"""
        Args
        ----
        options: list
            Options pertaining to the object
        """

        super(TikZObject, self).__init__()
        self.options = options


class TikZNodeAnchor(LatexObject):
    u"""Representation of a node's anchor point."""

    def __init__(self, node_handle, anchor_name):
        u"""
        Args
        ----
        node_handle: str
            Node's identifier
        anchor_name: str
            Name of the anchor
        """

        self.handle = node_handle
        self.anchor = anchor_name

    def __repr__(self):
        return u'({}.{})'.format(self.handle, self.anchor)

    def dumps(self):
        u"""Return a representation. Alias for consistency."""

        return self.__repr__()


class TikZNode(TikZObject):
    u"""A class that represents a TiKZ node."""

    _possible_anchors = [u'north', u'south', u'east', u'west']

    def __init__(self, handle=None, options=None, at=None, text=None):
        u"""
        Args
        ----
        handle: str
            Node identifier
        options: list
            List of options
        at: TikZCoordinate
            Coordinate where node is placed
        text: str
            Body text of the node
        """
        super(TikZNode, self).__init__(options=options)

        self.handle = handle

        if isinstance(at, (TikZCoordinate, type(None))):
            self._node_position = at
        else:
            raise TypeError(
                u'at parameter must be an object of the'
                u'TikzCoordinate class')

        self._node_text = text

    def dumps(self):
        u"""Return string representation of the node."""

        ret_str = []
        ret_str.append(Command(u'node', options=self.options).dumps())

        if self.handle is not None:
            ret_str.append(u'({})'.format(self.handle))

        if self._node_position is not None:
            ret_str.append(u'at {}'.format(unicode(self._node_position)))

        if self._node_text is not None:
            ret_str.append(u'{{{text}}};'.format(text=self._node_text))
        else:
            ret_str.append(u'{};')

        return u' '.join(ret_str)

    def get_anchor_point(self, anchor_name):
        u"""Return an anchor point of the node, if it exists."""

        if anchor_name in self._possible_anchors:
            return TikZNodeAnchor(self.handle, anchor_name)
        else:
            try:
                anchor = int(anchor_name.split(u'_')[1])
            except:
                anchor = None

            if anchor is not None:
                return TikZNodeAnchor(self.handle, unicode(anchor))

        raise ValueError(u'Invalid anchor name: "{}"'.format(anchor_name))

    def __getattr__(self, attr_name):
        try:
            point = self.get_anchor_point(attr_name)
            return point
        except ValueError:
            pass

        # raise AttributeError(
        #    'Invalid attribute requested: "{}"'.format(attr_name))


class TikZUserPath(LatexObject):
    u"""Represents a possible TikZ path."""

    def __init__(self, path_type, options=None):
        u"""
        Args
        ----
        path_type: str
            Type of path used
        options: Options
            List of options to add
        """
        super(TikZUserPath, self).__init__()
        self.path_type = path_type
        self.options = options

    def dumps(self):
        u"""Return path command representation."""

        ret_str = self.path_type

        if self.options is not None:
            ret_str += self.options.dumps()

        return ret_str


class TikZPathList(LatexObject):
    u"""Represents a path drawing."""

    _legal_path_types = [u'--', u'-|', u'|-', u'to',
                         u'rectangle', u'circle',
                         u'arc', u'edge']

    def __init__(self, *args):
        u"""
        Args
        ----
        args: list
            A list of path elements
        """
        self._last_item_type = None
        self._arg_list = []

        # parse list and verify legality
        self._parse_arg_list(args)

    def append(self, item):
        u"""Add a new element to the current path."""
        self._parse_next_item(item)

    def _parse_next_item(self, item):

        # assume first item is a point
        if self._last_item_type is None:
            try:
                self._add_point(item)
            except (TypeError, ValueError):
                # not a point, do something
                raise TypeError(
                    u'First element of path list must be a node identifier'
                    u' or coordinate'
                )
        elif self._last_item_type == u'point':
            # point after point is permitted, doesnt draw
            try:
                self._add_point(item)
                return
            except (ValueError, TypeError):
                # not a point, try path
                pass

            # will raise typeerror if wrong
            self._add_path(item)
        elif self._last_item_type == u'path':
            # only point allowed after path
            original_exception = None
            try:
                self._add_point(item)
                return
            except (TypeError, ValueError), ex:
                # check if trying to insert path after path
                try:
                    self._add_path(item, parse_only=True)
                    not_a_path = False
                    original_exception = ex
                except (TypeError, ValueError), ex:
                    # not a path either!
                    not_a_path = True
                    original_exception = ex

            # disentangle exceptions
            if not_a_path is False:
                raise ValueError(u'only a point descriptor can come'
                                 u' after a path descriptor')

            if original_exception is not None:
                raise original_exception

    def _parse_arg_list(self, args):

        for item in args:
            self._parse_next_item(item)

    def _add_path(self, path, parse_only=False):
        if isinstance(path, unicode):
            if path in self._legal_path_types:
                _path = TikZUserPath(path)
            else:
                raise ValueError(u'Illegal user path type: "{}"'.format(path))
        elif isinstance(path, TikZUserPath):
            _path = path
        else:
            raise TypeError(u'Only string or TikZUserPath types are allowed')

        # add
        if parse_only is False:
            self._arg_list.append(_path)
            self._last_item_type = u'path'
        else:
            return _path

    def _add_point(self, point, parse_only=False):
        if isinstance(point, unicode):
            try:
                _item = TikZCoordinate.from_str(point)
            except ValueError:
                raise ValueError(u'Illegal point string: "{}"'.format(point))
        elif isinstance(point, TikZCoordinate):
            _item = point
        elif isinstance(point, tuple):
            _item = TikZCoordinate(*point)
        elif isinstance(point, TikZNode):
            _item = u'({})'.format(point.handle)
        elif isinstance(point, TikZNodeAnchor):
            _item = point.dumps()
        else:
            raise TypeError(u'Only str, tuple, TikZCoordinate,'
                            u'TikZNode or TikZNodeAnchor types are allowed,'
                            u' got: {}'.format(type(point)))
        # add, finally
        if parse_only is False:
            self._arg_list.append(_item)
            self._last_item_type = u'point'
        else:
            return _item

    def dumps(self):
        u"""Return representation of the path command."""

        ret_str = []
        for item in self._arg_list:
            if isinstance(item, TikZUserPath):
                ret_str.append(item.dumps())
            elif isinstance(item, TikZCoordinate):
                ret_str.append(item.dumps())
            elif isinstance(item, unicode):
                ret_str.append(item)

        return u' '.join(ret_str)


class TikZPath(TikZObject):
    ur"""The TikZ \path command."""

    def __init__(self, path=None, options=None):
        u"""
        Args
        ----
        path: TikZPathList
            A list of the nodes, path types in the path
        options: TikZOptions
            A list of options for the command
        """

        super(TikZPath, self).__init__(options=options)

        if isinstance(path, TikZPathList):
            self.path = path
        elif isinstance(path, list):
            self.path = TikZPathList(*path)
        elif path is None:
            self.path = TikZPathList()
        else:
            raise TypeError(
                u'argument "path" can only be of types list or TikZPathList')

    def append(self, element):
        u"""Append a path element to the current list."""
        self.path.append(element)

    def dumps(self):
        u"""Return a representation for the command."""

        ret_str = [Command(u'path', options=self.options).dumps()]

        ret_str.append(self.path.dumps())

        return u' '.join(ret_str) + u';'


class TikZDraw(TikZPath):
    u"""A draw command is just a path command with the draw option."""

    def __init__(self, path=None, options=None):
        u"""
        Args
        ----
        path: TikZPathList
            A list of the nodes, path types in the path
        options: TikZOptions
            A list of options for the command
        """
        super(TikZDraw, self).__init__(path=path, options=options)

        # append option
        if self.options is not None:
            self.options.append_positional(u'draw')
        else:
            self.options = TikZOptions(u'draw')


class Plot(LatexObject):
    u"""A class representing a PGFPlot."""

    packages = [Package(u'pgfplots'), Command(u'pgfplotsset', u'compat=newest')]

    def __init__(self,
                 name=None,
                 func=None,
                 coordinates=None,
                 error_bar=None,
                 options=None):
        u"""
        Args
        ----
        name: str
            Name of the plot.
        func: str
            A function that should be plotted.
        coordinates: list
            A list of exact coordinates tat should be plotted.

        options: str, list or `~.Options`
        """

        self.name = name
        self.func = func
        self.coordinates = coordinates
        self.error_bar = error_bar
        self.options = options

        super(Plot, self).__init__()

    def dumps(self):
        u"""Represent the plot as a string in LaTeX syntax.

        Returns
        -------
        str
        """

        string = Command(u'addplot', options=self.options).dumps()

        if self.coordinates is not None:
            string += u' coordinates {%\n'

            if self.error_bar is None:
                for x, y in self.coordinates:
                    # ie: "(x,y)"
                    string += u'(' + unicode(x) + u',' + unicode(y) + u')%\n'

            else:
                for (x, y), (e_x, e_y) in izip(self.coordinates,
                                              self.error_bar):
                    # ie: "(x,y) +- (e_x,e_y)"
                    string += u'(' + unicode(x) + u',' + unicode(y) + \
                        u') +- (' + unicode(e_x) + u',' + unicode(e_y) + u')%\n'

            string += u'};%\n%\n'

        elif self.func is not None:
            string += u'{' + self.func + u'};%\n%\n'

        if self.name is not None:
            string += Command(u'addlegendentry', self.name).dumps()

        super(Plot, self).dumps()

        return string
