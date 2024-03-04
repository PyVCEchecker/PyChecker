# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prospector',
 'prospector.config',
 'prospector.formatters',
 'prospector.profiles',
 'prospector.tools',
 'prospector.tools.bandit',
 'prospector.tools.dodgy',
 'prospector.tools.frosted',
 'prospector.tools.mccabe',
 'prospector.tools.mypy',
 'prospector.tools.pep257',
 'prospector.tools.pep8',
 'prospector.tools.profile_validator',
 'prospector.tools.pyflakes',
 'prospector.tools.pylint',
 'prospector.tools.pyroma',
 'prospector.tools.vulture']

package_data = \
{'': ['*'], 'prospector.profiles': ['profiles/*']}

install_requires = \
['PyYAML',
 'dodgy>=0.2.1,<0.3.0',
 'mccabe>=0.6.0,<0.7.0',
 'pep8-naming>=0.3.3,<=0.10.0',
 'pycodestyle>=2.6.0,<2.9.0',
 'pydocstyle>=2.0.0',
 'pyflakes>=2.2.0,<2.4.0',
 'pylint-celery==0.3',
 'pylint-django>=2.4.4,<3.0.0',
 'pylint-flask==0.6',
 'pylint-plugin-utils>=0.6,<0.7',
 'pylint>=2.8.3,<3',
 'requirements-detector>=0.7,<0.8',
 'setoptconf-tmp>=0.3.1,<0.4.0',
 'toml>=0.10.2,<0.11.0']

extras_require = \
{'with_bandit': ['bandit>=1.5.1'],
 'with_everything': ['bandit>=1.5.1',
                     'frosted>=1.4.1',
                     'vulture>=1.5',
                     'mypy>=0.600',
                     'pyroma>=2.4'],
 'with_frosted': ['frosted>=1.4.1'],
 'with_mypy': ['mypy>=0.600'],
 'with_pyroma': ['pyroma>=2.4'],
 'with_vulture': ['vulture>=1.5']}

entry_points = \
{'console_scripts': ['prospector = prospector.run:main']}

setup_kwargs = {
    'name': 'prospector',
    'version': '1.5.1',
    'description': '',
    'long_description': 'prospector\n==========\n\n.. image:: https://img.shields.io/pypi/v/prospector.svg\n   :target: https://pypi.python.org/pypi/prospector\n   :alt: Latest Version of Prospector\n.. image:: https://travis-ci.org/PyCQA/prospector.svg?branch=master\n   :target: https://travis-ci.org/PyCQA/prospector\n   :alt: Build Status\n.. image:: https://landscape.io/github/landscapeio/prospector/master/landscape.svg?style=flat\n   :target: https://landscape.io/github/landscapeio/prospector/master\n   :alt: Code Health\n.. image:: https://img.shields.io/coveralls/PyCQA/prospector.svg?style=flat\n   :target: https://coveralls.io/r/PyCQA/prospector\n   :alt: Test Coverage\n.. image:: https://readthedocs.org/projects/prospector/badge/?version=latest\n   :target: http://prospector.readthedocs.io/\n   :alt: Documentation\n\n\nAbout\n-----\n\nProspector is a tool to analyse Python code and output information about\nerrors, potential problems, convention violations and complexity.\n\nIt brings together the functionality of other Python analysis tools such as\n`Pylint <http://docs.pylint.org/>`_,\n`pep8 <http://pep8.readthedocs.org/en/latest/>`_,\nand `McCabe complexity <https://pypi.python.org/pypi/mccabe>`_.\nSee the `Supported Tools <http://prospector.readthedocs.io/en/latest/supported_tools.html>`_\ndocumentation section for a complete list.\n\nThe primary aim of Prospector is to be useful \'out of the box\'. A common complaint of other\nPython analysis tools is that it takes a long time to filter through which errors are relevant\nor interesting to your own coding style. Prospector provides some default profiles, which\nhopefully will provide a good starting point and will be useful straight away, and adapts\nthe output depending on the libraries your project uses.\n\nInstallation\n------------\n\nProspector can be installed from PyPI using ``pip`` by running the following command::\n\n    pip install prospector\n\nOptional dependencies for Prospector, such as ``pyroma`` can also be installed by running::\n\n    pip install prospector[with_pyroma]\n\nSome shells (such as ``Zsh``, the default shell of macOS Catalina) require brackets to be escaped::\n\n    pip install prospector\\[with_pyroma\\]\n\nFor a list of all of the optional dependencies, see the optional extras section on the ReadTheDocs\npage on `Supported Tools Extras <https://prospector.readthedocs.io/en/latest/supported_tools.html#optional-extras>`_.\n\nFor local development, [poetry](https://python-poetry.org/) is used. Check out the code, then run::\n\n    poetry install\n\nAnd for extras::\n\n    poetry install -E with_everything\n\nFor more detailed information on installing the tool, see the\n`installation section <http://prospector.readthedocs.io/en/latest/#installation>`_ of the tool\'s main page\non ReadTheDocs.\n\nDocumentation\n-------------\n\nFull `documentation is available at ReadTheDocs <http://prospector.readthedocs.io>`_.\n\nUsage\n-----\n\nSimply run prospector from the root of your project::\n\n    prospector\n\nThis will output a list of messages pointing out potential problems or errors, for example::\n\n    prospector.tools.base (prospector/tools/base.py):\n        L5:0 ToolBase: pylint - R0922\n        Abstract class is only referenced 1 times\n\nOptions\n```````\n\nRun ``prospector --help`` for a full list of options and their effects.\n\nOutput Format\n~~~~~~~~~~~~~\n\nThe default output format of ``prospector`` is designed to be human readable. For parsing\n(for example, for reporting), you can use the ``--output-format json`` flag to get JSON-formatted\noutput.\n\nProfiles\n~~~~~~~~\n\nProspector is configurable using "profiles". These are composable YAML files with directives to\ndisable or enable tools or messages. For more information, read\n`the documentation about profiles <http://prospector.readthedocs.io/en/latest/profiles.html>`_.\n\nIf your code uses frameworks and libraries\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nOften tools such as pylint find errors in code which is not an error, for example due to attributes of classes being\ncreated at run time by a library or framework used by your project.\nFor example, by default, pylint will generate an error for Django models when accessing ``objects``, as the\n``objects`` attribute is not part of the ``Model`` class definition.\n\nProspector mitigates this by providing an understanding of these frameworks to the underlying tools.\n\nProspector will try to intuit which libraries your project uses by\n`detecting dependencies <https://github.com/landscapeio/requirements-detector>`_ and automatically turning on\nsupport for the requisite libraries. You can see which adaptors were run in the metadata section of the report.\n\nIf Prospector does not correctly detect your project\'s dependencies, you can specify them manually from the commandline::\n\n    prospector --uses django celery\n\nAdditionally, if Prospector is automatically detecting a library that you do not in fact use, you can turn\noff autodetection completely::\n\n    prospector --no-autodetect\n\nNote that as far as possible, these adaptors have been written as plugins or augmentations for the underlying\ntools so that they can be used without requiring Prospector. For example, the Django support is available as a pylint plugin.\n\nStrictness\n~~~~~~~~~~\n\nProspector has a configurable \'strictness\' level which will determine how harshly it searches for errors::\n\n    prospector --strictness high\n\nPossible values are ``verylow``, ``low``, ``medium``, ``high``, ``veryhigh``.\n\nProspector does not include documentation warnings by default, but you can turn\nthis on using the ``--doc-warnings`` flag.\n\npre-commit\n----------\n\nIf you\'d like Prospector to be run automatically when making changes to files in your Git\nrepository, you can install `pre-commit <https://pre-commit.com/>`_ and add the following\ntext to your repositories\' ``.pre-commit-config.yaml``::\n\n    repos:\n    -   repo: https://github.com/PyCQA/prospector\n        rev: 1.1.7 # The version of Prospector to use, at least 1.1.7\n        hooks:\n        -   id: prospector\n\nLicense\n-------\n\nProspector is available under the GPLv2 License.\n',
    'author': 'Carl Crowder',
    'author_email': 'git@carlcrowder.com',
    'maintainer': 'Carl Crowder',
    'maintainer_email': 'git@carlcrowder.com',
    'url': 'http://prospector.readthedocs.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
