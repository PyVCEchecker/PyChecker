# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytzdata', 'pytzdata.commands']

package_data = \
{'': ['*'],
 'pytzdata': ['zoneinfo/*',
              'zoneinfo/Africa/*',
              'zoneinfo/America/*',
              'zoneinfo/America/Argentina/*',
              'zoneinfo/America/Indiana/*',
              'zoneinfo/America/Kentucky/*',
              'zoneinfo/America/North_Dakota/*',
              'zoneinfo/Antarctica/*',
              'zoneinfo/Arctic/*',
              'zoneinfo/Asia/*',
              'zoneinfo/Atlantic/*',
              'zoneinfo/Australia/*',
              'zoneinfo/Brazil/*',
              'zoneinfo/Canada/*',
              'zoneinfo/Chile/*',
              'zoneinfo/Etc/*',
              'zoneinfo/Europe/*',
              'zoneinfo/Indian/*',
              'zoneinfo/Mexico/*',
              'zoneinfo/Pacific/*',
              'zoneinfo/US/*']}

setup_kwargs = {
    'name': 'pytzdata',
    'version': '2020.1',
    'description': 'The Olson timezone database for Python.',
    'long_description': "Pytzdata\n########\n\n.. image:: https://travis-ci.org/sdispater/pytzdata.png\n   :alt: Pytzdata Build status\n   :target: https://travis-ci.org/sdispater/pytzdata\n\nThe Olson timezone database for Python.\n\nSupports Python **2.7+** and **3.5+**.\n\n\nInstallation\n============\n\n    pip install pytzdata\n\n\nUsage\n=====\n\nYou can access the content of a specific timezone file by using the `tz_file()` function:\n\n.. code-block:: python\n\n    from pytzdata import tz_file\n\n    with tz_file('Europe/Paris') as f:\n        # Do something with the file\n\nIf you just want to know the path to a specific timezone file, you may use the `tz_path()` function:\n\n.. code-block:: python\n\n    from pytzdata import tz_path\n\n    tz_path('Europe/Paris')\n\nBy default, ``pytzdata`` will use the bundled timezone database, however you can set\na custom directory that holds the timezone files using the ``set_directory`` function:\n\n.. code-block:: python\n\n    import pytzdata\n\n    pytzdata.set_directory('/custom/zoneinfo')\n\nYou can also set the ``PYTZDATA_TZDATADIR`` environment variable to set a custom directory.\n\n\nRelease\n=======\n\nTo make a new release just follow these steps:\n\n- ``make data``\n- Update version numbers in ``pytzdata/version.py`` and ``tests/test_version.py``\n- ``make tox``\n\n\nResources\n=========\n\n* `Issue Tracker <https://github.com/sdispater/pytzdata/issues>`_\n",
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sdispater/pytzdata',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
}


setup(**setup_kwargs)
