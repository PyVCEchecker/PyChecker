# -*- coding: utf-8 -*-
u"""
This module implements some simple utility functions.

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
import os.path
import shutil
import tempfile
import pylatex.base_classes

_latex_special_chars = {
    u'&': ur'\&',
    u'%': ur'\%',
    u'$': ur'\$',
    u'#': ur'\#',
    u'_': ur'\_',
    u'{': ur'\{',
    u'}': ur'\}',
    u'~': ur'\textasciitilde{}',
    u'^': ur'\^{}',
    u'\\': ur'\textbackslash{}',
    u'\n': u'\\newline%\n',
    u'-': ur'{-}',
    u'\xA0': u'~',  # Non-breaking space
    u'[': ur'{[}',
    u']': ur'{]}',
}

_tmp_path = None


def _is_iterable(element):
    return hasattr(element, u'__iter__') and not isinstance(element, unicode)


class NoEscape(unicode):
    u"""
    A simple string class that is not escaped.

    When a `.NoEscape` string is added to another `.NoEscape` string it will
    produce a `.NoEscape` string. If it is added to normal string it will
    produce a normal string.

    Args
    ----
    string: str
        The content of the `NoEscape` string.
    """

    def __repr__(self):
        return u'%s(%s)' % (self.__class__.__name__, self)

    def __add__(self, right):
        s = super(NoEscape, self).__add__(right)
        if isinstance(right, NoEscape):
            return NoEscape(s)
        return s


def escape_latex(s):
    ur"""Escape characters that are special in latex.

    Args
    ----
    s : `str`, `NoEscape` or anything that can be converted to string
        The string to be escaped. If this is not a string, it will be converted
        to a string using `str`. If it is a `NoEscape` string, it will pass
        through unchanged.

    Returns
    -------
    NoEscape
        The string, with special characters in latex escaped.

    Examples
    --------
    >>> escape_latex("Total cost: $30,000")
    'Total cost: \$30,000'
    >>> escape_latex("Issue #5 occurs in 30% of all cases")
    'Issue \#5 occurs in 30\% of all cases'
    >>> print(escape_latex("Total cost: $30,000"))

    References
    ----------
        * http://tex.stackexchange.com/a/34586/43228
        * http://stackoverflow.com/a/16264094/2570866
    """

    if isinstance(s, NoEscape):
        return s

    return NoEscape(u''.join(_latex_special_chars.get(c, c) for c in unicode(s)))


def fix_filename(path):
    ur"""Fix filenames for use in LaTeX.

    Latex has problems if there are one or more points in the filename, thus
    'abc.def.jpg' will be changed to '{abc.def}.jpg'

    Windows gets angry about the curly braces that resolve the above issue on
    linux Latex distributions. MikTeX however, has no qualms about multiple
    dots in the filename so the behavior is different for posix vs nt when the
    length of file_parts is greater than two.

    Args
    ----
    filename : str
        The file name to be changed.

    Returns
    -------
    str
        The new filename.

    Examples
    --------
    >>> fix_filename("foo.bar.pdf")
    '{foo.bar}.pdf'
    >>> fix_filename("/etc/local/foo.bar.pdf")
    '/etc/local/{foo.bar}.pdf'
    >>> fix_filename("/etc/local/foo.bar.baz/document.pdf")
    '/etc/local/foo.bar.baz/document.pdf'
    >>> fix_filename("/etc/local/foo.bar.baz/foo~1/document.pdf")
    '\detokenize{/etc/local/foo.bar.baz/foo~1/document.pdf}'
    """

    path_parts = path.split(u'/' if os.name == u'posix' else u'\\')
    dir_parts = path_parts[:-1]

    filename = path_parts[-1]
    file_parts = filename.split(u'.')

    if os.name == u'posix' and len(file_parts) > 2:
        filename = u'{' + u'.'.join(file_parts[0:-1]) + u'}.' + file_parts[-1]

    dir_parts.append(filename)
    fixed_path = u'/'.join(dir_parts)

    if u'~' in fixed_path:
        fixed_path = ur'\detokenize{' + fixed_path + u'}'

    return fixed_path


def dumps_list(l, **_3to2kwargs):
    if 'as_content' in _3to2kwargs: as_content = _3to2kwargs['as_content']; del _3to2kwargs['as_content']
    else: as_content = True
    if 'mapper' in _3to2kwargs: mapper = _3to2kwargs['mapper']; del _3to2kwargs['mapper']
    else: mapper = None
    if 'token' in _3to2kwargs: token = _3to2kwargs['token']; del _3to2kwargs['token']
    else: token = u'%\n'
    if 'escape' in _3to2kwargs: escape = _3to2kwargs['escape']; del _3to2kwargs['escape']
    else: escape = True
    ur"""Try to generate a LaTeX string of a list that can contain anything.

    Args
    ----
    l : list
        A list of objects to be converted into a single string.
    escape : bool
        Whether to escape special LaTeX characters in converted text.
    token : str
        The token (default is a newline) to separate objects in the list.
    mapper: callable or `list`
        A function, class or a list of functions/classes that should be called
        on all entries of the list after converting them to a string, for
        instance `~.bold` or `~.MediumText`.
    as_content: bool
        Indicates whether the items in the list should be dumped using
        `~.LatexObject.dumps_as_content`

    Returns
    -------
    NoEscape
        A single LaTeX string.

    Examples
    --------
    >>> dumps_list([r"\textbf{Test}", r"\nth{4}"])
    '\\textbf{Test}%\n\\nth{4}'
    >>> print(dumps_list([r"\textbf{Test}", r"\nth{4}"]))
    \textbf{Test}
    \nth{4}
    >>> print(pylatex.utils.dumps_list(["There are", 4, "lights!"]))
    There are
    4
    lights!
    >>> print(dumps_list(["$100%", "True"], escape=True))
    \$100\%
    True
    """
    strings = (_latex_item_to_string(i, escape=escape, as_content=as_content)
               for i in l)

    if mapper is not None:
        if not isinstance(mapper, list):
            mapper = [mapper]

        for m in mapper:
            strings = [m(s) for s in strings]
        strings = [_latex_item_to_string(s) for s in strings]

    return NoEscape(token.join(strings))


def _latex_item_to_string(item, **_3to2kwargs):
    if 'as_content' in _3to2kwargs: as_content = _3to2kwargs['as_content']; del _3to2kwargs['as_content']
    else: as_content = False
    if 'escape' in _3to2kwargs: escape = _3to2kwargs['escape']; del _3to2kwargs['escape']
    else: escape = False
    u"""Use the render method when possible, otherwise uses str.

    Args
    ----
    item: object
        An object that needs to be converted to a string
    escape: bool
        Flag that indicates if escaping is needed
    as_content: bool
        Indicates whether the item should be dumped using
        `~.LatexObject.dumps_as_content`

    Returns
    -------
    NoEscape
        Latex
    """

    if isinstance(item, pylatex.base_classes.LatexObject):
        if as_content:
            return item.dumps_as_content()
        else:
            return item.dumps()
    elif not isinstance(item, unicode):
        item = unicode(item)

    if escape:
        item = escape_latex(item)

    return item


def bold(s, **_3to2kwargs):
    if 'escape' in _3to2kwargs: escape = _3to2kwargs['escape']; del _3to2kwargs['escape']
    else: escape = True
    ur"""Make a string appear bold in LaTeX formatting.

    bold() wraps a given string in the LaTeX command \textbf{}.

    Args
    ----
    s : str
        The string to be formatted.
    escape: bool
        If true the bold text will be escaped

    Returns
    -------
    NoEscape
        The formatted string.

    Examples
    --------
    >>> bold("hello")
    '\\textbf{hello}'
    >>> print(bold("hello"))
    \textbf{hello}
    """

    if escape:
        s = escape_latex(s)

    return NoEscape(ur'\textbf{' + s + u'}')


def italic(s, **_3to2kwargs):
    if 'escape' in _3to2kwargs: escape = _3to2kwargs['escape']; del _3to2kwargs['escape']
    else: escape = True
    ur"""Make a string appear italicized in LaTeX formatting.

    italic() wraps a given string in the LaTeX command \textit{}.

    Args
    ----
    s : str
        The string to be formatted.
    escape: bool
        If true the italic text will be escaped

    Returns
    -------
    NoEscape
        The formatted string.

    Examples
    --------
    >>> italic("hello")
    '\\textit{hello}'
    >>> print(italic("hello"))
    \textit{hello}
    """
    if escape:
        s = escape_latex(s)

    return NoEscape(ur'\textit{' + s + u'}')


def verbatim(s, **_3to2kwargs):
    if 'delimiter' in _3to2kwargs: delimiter = _3to2kwargs['delimiter']; del _3to2kwargs['delimiter']
    else: delimiter = u'|'
    ur"""Make the string verbatim.

    Wraps the given string in a \verb LaTeX command.

    Args
    ----
    s : str
        The string to be formatted.
    delimiter : str
        How to designate the verbatim text (default is a pipe | )

    Returns
    -------
    NoEscape
        The formatted string.

    Examples
    --------
    >>> verbatim(r"\renewcommand{}")
    '\\verb|\\renewcommand{}|'
    >>> print(verbatim(r"\renewcommand{}"))
    \verb|\renewcommand{}|
    >>> print(verbatim('pi|pe', '!'))
    \verb!pi|pe!
    """

    return NoEscape(ur'\verb' + delimiter + s + delimiter)


def make_temp_dir():
    u"""Create a temporary directory if it doesn't exist.

    Returns
    -------
    str
        The absolute filepath to the created temporary directory.

    Examples
    --------
    >>> make_temp_dir()
    '/var/folders/g9/ct5f3_r52c37rbls5_9nc_qc0000gn/T/pylatex'
    """

    global _tmp_path
    if not _tmp_path:
        _tmp_path = tempfile.mkdtemp(prefix=u"pylatex-tmp.")
    return _tmp_path


def rm_temp_dir():
    u"""Remove the temporary directory specified in ``_tmp_path``."""

    global _tmp_path
    if _tmp_path:
        shutil.rmtree(_tmp_path)
        _tmp_path = None
