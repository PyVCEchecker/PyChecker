# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['flake8_print']
install_requires = \
['flake8>=3.0', 'pycodestyle', 'six']

entry_points = \
{'flake8.extension': ['T00 = flake8_print:PrintChecker']}

setup_kwargs = {
    'name': 'flake8-print',
    'version': '4.0.0',
    'description': 'print statement checker plugin for flake8',
    'long_description': "Flake8 print plugin\n===================\n\nCheck for Print statements in python files.\n\nThis module provides a plugin for ``flake8``, the Python code checker.\n\n\nInstallation\n------------\n\nYou can install or upgrade ``flake8-print`` with these commands::\n\n  $ pip install flake8-print\n  $ pip install --upgrade flake8-print\n\n\nPlugin for Flake8\n-----------------\n\nWhen both ``flake8 2.4.1`` and ``flake8-print`` are installed, the plugin is\navailable in ``flake8``::\n\n    $ flake8 --version\n    2.4.1 (pep8: 1.5.7, flake8-print: 2.0.0, mccabe: 0.3.1, pyflakes: 0.8.1)\n\nError codes\n-----------\n\n| Error Code  | Description                          |\n| ----------- | ------------------------------------ |\n| T001        | print found                          |\n| T002        | Python 2.x reserved word print used  |\n| T003        | pprint found                         |\n| T004        | pprint declared                      |\n\n\nChanges\n-------\n\n##### 4.0.0 - 2020-11-29\n\n* Opted back into using Poetry now that the existing issues have been fixed.\n* Python 2.7 support was no officially dropped.\n\n##### 3.1.4 - 2019-1-11\n\n* Fix bug introduced in 3.1.3\n* Support for `nopep8` comments\n\n##### 3.1.3 - 2019-31-10\n\n* Swapped back from poetry to setup.py :(....python ecosystem issues....\n* single function refactor code\n\n##### 3.1.1 - 2019-03-12\n\n* Fix reading from stdin when it is closed (requires flake8 > 2.1).\n* Add error codes to ReadMe.\n* Swapped to poetry from setup.py\n* Ran black on the repository\n\n##### 3.1.0 - 2018-02-11\n* Add a framework classifier for use in pypi.org\n* Fix entry_point in setup.py leaving it off by default again.\n\n##### 3.0.1 - 2017-11-06\n* Fix conflict in setup.py leaving it off by default again.\n* Fix bug in name code.\n\n##### 3.0.0 - 2017-11-05\n* Remove some of the python 2/3 message differentiation.\n* Use an AST rather than a logical line checker with a regex.\n* pprint support.\n* Loss of multiline noqa support, until there is a way to use both the AST and have flake8 provide the noqa lines.\n\n\n##### 2.0.2 - 2016-02-29\n* Fix ReadMe for pipy\n* Refactor, DRY it up.\n* Update python 2 vs python 3 print statement styles.\n\n##### 2.0.1 - 2015-11-21\n* Add back the decorator to fix the `flake8 --version` call.\n\n##### 2.0 - 2015-11-10\n* Support noqa at end of multiline print statement\n* Performance improvements\n* Removed PrintStatementChecker class and other functions\n* Added T101 for 'Python 2.x reserved word print used.'\n* Added testing for Python 3.3 and 3.5, and different flake8 versions\n\n##### 1.6.1 - 2015-05-22\n* Fix bug introduced in 1.6.\n\n##### 1.6 - 2015-05-18\n* Added proper support for python3 and testing for python 2.6, 2.7 and 3.4\n\n##### 1.5 - 2014-11-04\n* Added python2.6 support. Thanks @zoidbergwill\n\n##### 1.4 - 2014-10-06\n* Apped noqa support\n\n##### 1.3 - 2014-09-27\n* Dropped noqa support\n* Support for multiline comments and less false positives\n\n##### 1.2 - 2014-06-30\n* Does not catch the word print in single line strings\n* Does not catch inline comments with print in it\n* Added tests\n\n##### 1.1 - 2014-06-30\n* First release\n\n##### 1.0 - 2014-06-30\n* Whoops\n",
    'author': 'Joseph Kahn',
    'author_email': 'josephbkahn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jbkahn/flake8-print',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
