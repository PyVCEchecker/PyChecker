# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pastel', 'tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pastel',
    'version': '0.2.1',
    'description': 'Bring colors to your terminal.',
    'long_description': "Pastel: Bring colors to your terminal\n#####################################\n\nPastel is a simple library to help you colorize strings in your terminal.\n\nIt comes bundled with predefined styles:\n\n* ``info``: green\n* ``comment``: yellow\n* ``question``: black on cyan\n* ``error``: white on red\n\n.. image:: https://raw.githubusercontent.com/sdispater/pastel/master/assets/screenshot.png\n\n\nFeatures\n========\n\n* Use predefined styles or add you own.\n* Disable colors all together by calling ``with_colors(False)``.\n* Automatically disables colors if the output is not a TTY.\n* Used in `cleo <https://github.com/sdispater/cleo>`_.\n* Supports Python **2.7+**, **3.5+** and **PyPy**.\n\n\nUsage\n=====\n\n.. code-block:: python\n\n    >>> import pastel\n    >>> print(pastel.colorize('<info>Information</info>'))\n    'Information'  # Green string by default\n    >>> print(pastel.colorize('<fg=red;options=bold>This is bold red</>'))\n    'This is bold red'\n\n\nInstallation\n============\n\n.. code-block::\n\n    pip install pastel\n",
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sdispater/pastel',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
}


setup(**setup_kwargs)
