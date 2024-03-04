u"""
Baseclasses that can be used to create classes representing LaTeX objects.

..  :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from .latex_object import LatexObject
from .containers import Container, Environment, ContainerCommand
from .command import CommandBase, Command, UnsafeCommand, Options, \
    SpecialOptions, Arguments, SpecialArguments
from .float import Float

# Old names of the base classes for backwards compatibility
BaseLaTeXClass = LatexObject
BaseLaTeXContainer = Container
BaseLaTeXNamedContainer = Environment
