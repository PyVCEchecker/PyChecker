# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['flake8_debugger']
install_requires = \
['flake8>=3.0', 'pycodestyle', 'six']

entry_points = \
{'flake8.extension': ['T100 = flake8_debugger:DebuggerChecker']}

setup_kwargs = {
    'name': 'flake8-debugger',
    'version': '4.0.0',
    'description': 'ipdb/pdb statement checker plugin for flake8',
    'long_description': 'Flake8 debugger plugin\n======================\n\nCheck for pdb;idbp imports and set traces, as well as `from IPython.terminal.embed import InteractiveShellEmbed` and `InteractiveShellEmbed()()`.\n\nThis module provides a plugin for ``flake8``, the Python code checker.\n\n\nInstallation\n------------\n\nYou can install or upgrade ``flake8-debugger`` with these commands::\n\n    $ pip install flake8-debugger\n    $ pip install --upgrade flake8-debugger\n\n\nPlugin for Flake8\n-----------------\n\nWhen both ``flake8 2.2`` and ``flake8-debugger`` are installed, the plugin is\navailable in ``flake8``::\n\n    $ flake8 --version\n    2.0 (pep8: 1.4.5, flake8-debugger: 1.0, pyflakes: 0.6.1)\n\n\nChanges\n-------\n\n##### 4.0.0 - 2020-11-29\n\n* Opted back into using Poetry now that the existing issues have been fixed.\n* Python 2.7 support was no officially dropped.\n\n##### 3.2.1 - 2019-10-31\n\n* Swapped back from poetry to setup.py :(....python ecosystem issues....\n\n##### 3.2.0 - 2019-10-15\n\n* Forgot to add `breakpoint` support to the last changelog entry as well as fixing a bug introduced into that version that flagged `import builtins` as noteworthy.\n\n\n##### 3.1.1 - 2019-10-12\n\n* Fix reading from stdin when it is closed (requires flake8 > 2.1).\n* Swapped to poetry from setup.py\n* Ran black on the repository\n\n##### 3.1.0 - 2018-02-11\n* Add a framework classifier for use in pypi.org\n* Fix entry_point in setup.py leaving it off by default again\n* Detect __import__ debugger statements\n* Add support for `pudb` detection\n\n##### 3.0.0 - 2017-05-11\n* fix the refactor of the detector in 2.0.0 that was removed from pypi.\n* fix a flake8 issue that had it turned off by default.\n\n\n##### 2.0.0 - 2016-09-19\n* refactor detector\n* drop official support for python 2.6 and 3.3\n\n\n##### 1.4.0 - 2015-05-18\n* refactor detector, run tests in python 2.6, 2.7 and 3.4 as well as adding a check for InteractiveShellEmbed.\n\n##### 1.3.2 - 2014-11-04\n* more tests, fix edge case and debugger identification.\n\n##### 1.3.1 - 2014-11-04\n* more tests, a little refactoring and improvements in catching.\n\n##### 1.3 - 2014-11-04\n* using ast instead of regular expressions\n\n##### 1.2 - 2014-06-30\n* Added a few simple tests\n\n##### 1.1 - 2014-06-30\n* First release\n\n##### 1.0 - 2014-06-30\n* Whoops\n',
    'author': 'Joseph Kahn',
    'author_email': 'josephbkahn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jbkahn/flake8-debugger',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
