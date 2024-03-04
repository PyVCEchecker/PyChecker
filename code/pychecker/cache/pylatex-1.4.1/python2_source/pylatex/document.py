# -*- coding: utf-8 -*-
u"""
This module implements the class that deals with the full document.

..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from builtins import super
from future import standard_library
standard_library.install_aliases()
import os
import sys
import subprocess
import errno
from .base_classes import Environment, Command, Container, LatexObject, \
    UnsafeCommand, SpecialArguments
from .package import Package
from .errors import CompilerError
from .utils import dumps_list, rm_temp_dir, NoEscape
import pylatex.config as cf


class Document(Environment):
    ur"""
    A class that contains a full LaTeX document.

    If needed, you can append stuff to the preamble or the packages.
    For instance, if you need to use ``\maketitle`` you can add the title,
    author and date commands to the preamble to make it work.

    """

    def __init__(self, default_filepath=u'default_filepath', **_3to2kwargs):
        if 'data' in _3to2kwargs: data = _3to2kwargs['data']; del _3to2kwargs['data']
        else: data = None
        if 'geometry_options' in _3to2kwargs: geometry_options = _3to2kwargs['geometry_options']; del _3to2kwargs['geometry_options']
        else: geometry_options = None
        if 'indent' in _3to2kwargs: indent = _3to2kwargs['indent']; del _3to2kwargs['indent']
        else: indent = None
        if 'page_numbers' in _3to2kwargs: page_numbers = _3to2kwargs['page_numbers']; del _3to2kwargs['page_numbers']
        else: page_numbers = True
        if 'microtype' in _3to2kwargs: microtype = _3to2kwargs['microtype']; del _3to2kwargs['microtype']
        else: microtype = None
        if 'textcomp' in _3to2kwargs: textcomp = _3to2kwargs['textcomp']; del _3to2kwargs['textcomp']
        else: textcomp = True
        if 'lmodern' in _3to2kwargs: lmodern = _3to2kwargs['lmodern']; del _3to2kwargs['lmodern']
        else: lmodern = True
        if 'font_size' in _3to2kwargs: font_size = _3to2kwargs['font_size']; del _3to2kwargs['font_size']
        else: font_size = u"normalsize"
        if 'inputenc' in _3to2kwargs: inputenc = _3to2kwargs['inputenc']; del _3to2kwargs['inputenc']
        else: inputenc = u'utf8'
        if 'fontenc' in _3to2kwargs: fontenc = _3to2kwargs['fontenc']; del _3to2kwargs['fontenc']
        else: fontenc = u'T1'
        if 'document_options' in _3to2kwargs: document_options = _3to2kwargs['document_options']; del _3to2kwargs['document_options']
        else: document_options = None
        if 'documentclass' in _3to2kwargs: documentclass = _3to2kwargs['documentclass']; del _3to2kwargs['documentclass']
        else: documentclass = u'article'
        ur"""
        Args
        ----
        default_filepath: str
            The default path to save files.
        documentclass: str or `~.Command`
            The LaTeX class of the document.
        document_options: str or `list`
            The options to supply to the documentclass
        fontenc: str
            The option for the fontenc package. If it is `None`, the fontenc
            package will not be loaded at all.
        inputenc: str
            The option for the inputenc package. If it is `None`, the inputenc
            package will not be loaded at all.
        font_size: str
            The font size to declare as normalsize
        lmodern: bool
            Use the Latin Modern font. This is a font that contains more glyphs
            than the standard LaTeX font.
        textcomp: bool
            Adds even more glyphs, for instance the Euro (€) sign.
        page_numbers: bool
            Adds the ability to add the last page to the document.
        indent: bool
            Determines whether or not the document requires indentation. If it
            is `None` it will use the value from the active config. Which is
            `True` by default.
        geometry_options: dict
            The options to supply to the geometry package
        data: list
            Initial content of the document.
        """

        self.default_filepath = default_filepath

        if isinstance(documentclass, Command):
            self.documentclass = documentclass
        else:
            self.documentclass = Command(u'documentclass',
                                         arguments=documentclass,
                                         options=document_options)
        if indent is None:
            indent = cf.active.indent
        if microtype is None:
            microtype = cf.active.microtype

        # These variables are used by the __repr__ method
        self._fontenc = fontenc
        self._inputenc = inputenc
        self._lmodern = lmodern
        self._indent = indent
        self._microtype = microtype

        packages = []

        if fontenc is not None:
            packages.append(Package(u'fontenc', options=fontenc))
        if inputenc is not None:
            packages.append(Package(u'inputenc', options=inputenc))
        if lmodern:
            packages.append(Package(u'lmodern'))
        if textcomp:
            packages.append(Package(u'textcomp'))
        if page_numbers:
            packages.append(Package(u'lastpage'))
        if not indent:
            packages.append(Package(u'parskip'))
        if microtype:
            packages.append(Package(u'microtype'))

        if geometry_options is not None:
            packages.append(Package(u'geometry'))
            # Make sure we don't add this options command for an empty list,
            # because that breaks.
            if geometry_options:
                packages.append(Command(
                    u'geometry',
                    arguments=SpecialArguments(geometry_options),
                ))

        super(Document, self).__init__(data=data)

        # Usually the name is the class name, but if we create our own
        # document class, \begin{document} gets messed up.
        self._latex_name = u'document'

        self.packages |= packages
        self.variables = []

        self.preamble = []

        if not page_numbers:
            self.change_document_style(u"empty")

        # No colors have been added to the document yet
        self.color = False
        self.meta_data = False

        self.append(Command(command=font_size))

    def _propagate_packages(self):
        ur"""Propogate packages.

        Make sure that all the packages included in the previous containers
        are part of the full list of packages.
        """

        super(Document, self)._propagate_packages()

        for item in (self.preamble):
            if isinstance(item, LatexObject):
                if isinstance(item, Container):
                    item._propagate_packages()
                for p in item.packages:
                    self.packages.add(p)

    def dumps(self):
        u"""Represent the document as a string in LaTeX syntax.

        Returns
        -------
        str
        """

        head = self.documentclass.dumps() + u'%\n'
        head += self.dumps_packages() + u'%\n'
        head += dumps_list(self.variables) + u'%\n'
        head += dumps_list(self.preamble) + u'%\n'

        return head + u'%\n' + super(Document, self).dumps()

    def generate_tex(self, filepath=None):
        u"""Generate a .tex file for the document.

        Args
        ----
        filepath: str
            The name of the file (without .tex), if this is not supplied the
            default filepath attribute is used as the path.
        """

        super(Document, self).generate_tex(self._select_filepath(filepath))

    def generate_pdf(self, filepath=None, **_3to2kwargs):
        if 'silent' in _3to2kwargs: silent = _3to2kwargs['silent']; del _3to2kwargs['silent']
        else: silent = True
        if 'compiler_args' in _3to2kwargs: compiler_args = _3to2kwargs['compiler_args']; del _3to2kwargs['compiler_args']
        else: compiler_args = None
        if 'compiler' in _3to2kwargs: compiler = _3to2kwargs['compiler']; del _3to2kwargs['compiler']
        else: compiler = None
        if 'clean_tex' in _3to2kwargs: clean_tex = _3to2kwargs['clean_tex']; del _3to2kwargs['clean_tex']
        else: clean_tex = True
        if 'clean' in _3to2kwargs: clean = _3to2kwargs['clean']; del _3to2kwargs['clean']
        else: clean = True
        u"""Generate a pdf file from the document.

        Args
        ----
        filepath: str
            The name of the file (without .pdf), if it is `None` the
            ``default_filepath`` attribute will be used.
        clean: bool
            Whether non-pdf files created that are created during compilation
            should be removed.
        clean_tex: bool
            Also remove the generated tex file.
        compiler: `str` or `None`
            The name of the LaTeX compiler to use. If it is None, PyLaTeX will
            choose a fitting one on its own. Starting with ``latexmk`` and then
            ``pdflatex``.
        compiler_args: `list` or `None`
            Extra arguments that should be passed to the LaTeX compiler. If
            this is None it defaults to an empty list.
        silent: bool
            Whether to hide compiler output
        """

        if compiler_args is None:
            compiler_args = []

        # In case of newer python with the use of the cwd parameter
        # one can avoid to physically change the directory
        # to the destination folder
        python_cwd_available = sys.version_info >= (3, 6)

        filepath = self._select_filepath(filepath)
        if not os.path.basename(filepath):
            filepath = os.path.join(os.path.abspath(filepath),
                                    u'default_basename')
        else:
            filepath = os.path.abspath(filepath)

        cur_dir = os.getcwdu()
        dest_dir = os.path.dirname(filepath)

        if not python_cwd_available:
            os.chdir(dest_dir)

        self.generate_tex(filepath)

        if compiler is not None:
            compilers = ((compiler, []),)
        else:
            latexmk_args = [u'--pdf']

            compilers = (
                (u'latexmk', latexmk_args),
                (u'pdflatex', [])
            )

        main_arguments = [u'--interaction=nonstopmode', filepath + u'.tex']

        check_output_kwargs = {}
        if python_cwd_available:
            check_output_kwargs = {u'cwd': dest_dir}

        os_error = None

        for compiler, arguments in compilers:
            command = [compiler] + arguments + compiler_args + main_arguments

            try:
                output = subprocess.check_output(command,
                                                 stderr=subprocess.STDOUT,
                                                 **check_output_kwargs)
            except (OSError, IOError), e:
                # Use FileNotFoundError when python 2 is dropped
                os_error = e

                if os_error.errno == errno.ENOENT:
                    # If compiler does not exist, try next in the list
                    continue
                raise
            except subprocess.CalledProcessError, e:
                # For all other errors print the output and raise the error
                print(e.output.decode())
                raise
            else:
                if not silent:
                    print(output.decode())

            if clean:
                try:
                    # Try latexmk cleaning first
                    subprocess.check_output([u'latexmk', u'-c', filepath],
                                            stderr=subprocess.STDOUT,
                                            **check_output_kwargs)
                except (OSError, IOError, subprocess.CalledProcessError):
                    # Otherwise just remove some file extensions.
                    extensions = [u'aux', u'log', u'out', u'fls',
                                  u'fdb_latexmk']

                    for ext in extensions:
                        try:
                            os.remove(filepath + u'.' + ext)
                        except (OSError, IOError), e:
                            # Use FileNotFoundError when python 2 is dropped
                            if e.errno != errno.ENOENT:
                                raise
                rm_temp_dir()

            if clean_tex:
                os.remove(filepath + u'.tex')  # Remove generated tex file

            # Compilation has finished, so no further compilers have to be
            # tried
            break

        else:
            # Notify user that none of the compilers worked.
            raise(CompilerError(
                u'No LaTex compiler was found\n'
                u'Either specify a LaTex compiler '
                u'or make sure you have latexmk or pdfLaTex installed.'
            ))

        if not python_cwd_available:
            os.chdir(cur_dir)

    def _select_filepath(self, filepath):
        u"""Make a choice between ``filepath`` and ``self.default_filepath``.

        Args
        ----
        filepath: str
            the filepath to be compared with ``self.default_filepath``

        Returns
        -------
        str
            The selected filepath
        """

        if filepath is None:
            return self.default_filepath
        else:
            if os.path.basename(filepath) == u'':
                filepath = os.path.join(filepath, os.path.basename(
                    self.default_filepath))
            return filepath

    def change_page_style(self, style):
        ur"""Alternate page styles of the current page.

        Args
        ----
        style: str
            value to set for the page style of the current page
        """

        self.append(Command(u"thispagestyle", arguments=style))

    def change_document_style(self, style):
        ur"""Alternate page style for the entire document.

        Args
        ----
        style: str
            value to set for the document style
        """

        self.append(Command(u"pagestyle", arguments=style))

    def add_color(self, name, model, description):
        ur"""Add a color that can be used throughout the document.

        Args
        ----
        name: str
            Name to set for the color
        model: str
            The color model to use when defining the color
        description: str
            The values to use to define the color
        """

        if self.color is False:
            self.packages.append(Package(u"color"))
            self.color = True

        self.preamble.append(Command(u"definecolor", arguments=[name,
                                                               model,
                                                               description]))

    def change_length(self, parameter, value):
        ur"""Change the length of a certain parameter to a certain value.

        Args
        ----
        parameter: str
            The name of the parameter to change the length for
        value: str
            The value to set the parameter to
        """

        self.preamble.append(UnsafeCommand(u'setlength',
                                           arguments=[parameter, value]))

    def set_variable(self, name, value):
        ur"""Add a variable which can be used inside the document.

        Variables are defined before the preamble. If a variable with that name
        has already been set, the new value will override it for future uses.
        This is done by appending ``\renewcommand`` to the document.

        Args
        ----
        name: str
            The name to set for the variable
        value: str
            The value to set for the variable
        """

        name_arg = u"\\" + name
        variable_exists = False

        for variable in self.variables:
            if name_arg == variable.arguments._positional_args[0]:
                variable_exists = True
                break

        if variable_exists:
            renew = Command(command=u"renewcommand",
                            arguments=[NoEscape(name_arg), value])
            self.append(renew)
        else:
            new = Command(command=u"newcommand",
                          arguments=[NoEscape(name_arg), value])
            self.variables.append(new)
