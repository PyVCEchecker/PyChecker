# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tinydb']

package_data = \
{'': ['*']}

extras_require = \
{':python_version <= "3.7"': ['typing-extensions>=3.10.0,<4.0.0']}

setup_kwargs = {
    'name': 'tinydb',
    'version': '4.5.2',
    'description': 'TinyDB is a tiny, document oriented database optimized for your happiness :)',
    'long_description': ".. image:: https://raw.githubusercontent.com/msiemens/tinydb/master/artwork/logo.png\n    :scale: 100%\n    :height: 150px\n\n|Build Status| |Coverage| |Version|\n\nQuick Links\n***********\n\n- `Example Code`_\n- `Supported Python Versions`_\n- `Documentation <http://tinydb.readthedocs.org/>`_\n- `Changelog <https://tinydb.readthedocs.io/en/latest/changelog.html>`_\n- `Extensions <https://tinydb.readthedocs.io/en/latest/extensions.html>`_\n- `Contributing`_\n\nIntroduction\n************\n\nTinyDB is a lightweight document oriented database optimized for your happiness :)\nIt's written in pure Python and has no external dependencies. The target are\nsmall apps that would be blown away by a SQL-DB or an external database server.\n\nTinyDB is:\n\n- **tiny:** The current source code has 1800 lines of code (with about 40%\n  documentation) and 1600 lines tests.\n\n- **document oriented:** Like MongoDB_, you can store any document\n  (represented as ``dict``) in TinyDB.\n\n- **optimized for your happiness:** TinyDB is designed to be simple and\n  fun to use by providing a simple and clean API.\n\n- **written in pure Python:** TinyDB neither needs an external server (as\n  e.g. `PyMongo <https://api.mongodb.org/python/current/>`_) nor any dependencies\n  from PyPI.\n\n- **works on Python 3.6+ and PyPy3:** TinyDB works on all modern versions of Python\n  and PyPy.\n\n- **powerfully extensible:** You can easily extend TinyDB by writing new\n  storages or modify the behaviour of storages with Middlewares.\n\n- **100% test coverage:** No explanation needed.\n\nTo dive straight into all the details, head over to the `TinyDB docs\n<https://tinydb.readthedocs.io/>`_. You can also discuss everything related\nto TinyDB like general development, extensions or showcase your TinyDB-based\nprojects on the `discussion forum <http://forum.m-siemens.de/.>`_.\n\nSupported Python Versions\n*************************\n\nTinyDB has been tested with Python 3.6 - 3.9 and PyPy3.\n\nExample Code\n************\n\n.. code-block:: python\n\n    >>> from tinydb import TinyDB, Query\n    >>> db = TinyDB('/path/to/db.json')\n    >>> db.insert({'int': 1, 'char': 'a'})\n    >>> db.insert({'int': 1, 'char': 'b'})\n\nQuery Language\n==============\n\n.. code-block:: python\n\n    >>> User = Query()\n    >>> # Search for a field value\n    >>> db.search(User.name == 'John')\n    [{'name': 'John', 'age': 22}, {'name': 'John', 'age': 37}]\n\n    >>> # Combine two queries with logical and\n    >>> db.search((User.name == 'John') & (User.age <= 30))\n    [{'name': 'John', 'age': 22}]\n\n    >>> # Combine two queries with logical or\n    >>> db.search((User.name == 'John') | (User.name == 'Bob'))\n    [{'name': 'John', 'age': 22}, {'name': 'John', 'age': 37}, {'name': 'Bob', 'age': 42}]\n\n    >>> # More possible comparisons:  !=  <  >  <=  >=\n    >>> # More possible checks: where(...).matches(regex), where(...).test(your_test_func)\n\nTables\n======\n\n.. code-block:: python\n\n    >>> table = db.table('name')\n    >>> table.insert({'value': True})\n    >>> table.all()\n    [{'value': True}]\n\nUsing Middlewares\n=================\n\n.. code-block:: python\n\n    >>> from tinydb.storages import JSONStorage\n    >>> from tinydb.middlewares import CachingMiddleware\n    >>> db = TinyDB('/path/to/db.json', storage=CachingMiddleware(JSONStorage))\n\n\nContributing\n************\n\nWhether reporting bugs, discussing improvements and new ideas or writing\nextensions: Contributions to TinyDB are welcome! Here's how to get started:\n\n1. Check for open issues or open a fresh issue to start a discussion around\n   a feature idea or a bug\n2. Fork `the repository <https://github.com/msiemens/tinydb/>`_ on Github,\n   create a new branch off the `master` branch and start making your changes\n   (known as `GitHub Flow <https://guides.github.com/introduction/flow/index.html>`_)\n3. Write a test which shows that the bug was fixed or that the feature works\n   as expected\n4. Send a pull request and bug the maintainer until it gets merged and\n   published ☺\n\n.. |Build Status| image:: https://img.shields.io/azure-devops/build/msiemens/3e5baa75-12ec-43ac-9728-89823ee8c7e2/2.svg?style=flat-square\n   :target: https://dev.azure.com/msiemens/github/_build?definitionId=2\n.. |Coverage| image:: http://img.shields.io/coveralls/msiemens/tinydb.svg?style=flat-square\n   :target: https://coveralls.io/r/msiemens/tinydb\n.. |Version| image:: http://img.shields.io/pypi/v/tinydb.svg?style=flat-square\n   :target: https://pypi.python.org/pypi/tinydb/\n.. _Buzhug: http://buzhug.sourceforge.net/\n.. _CodernityDB: https://github.com/perchouli/codernitydb\n.. _MongoDB: http://mongodb.org/\n",
    'author': 'Markus Siemens',
    'author_email': 'markus@m-siemens.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/msiemens/tinydb',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
