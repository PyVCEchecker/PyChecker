# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sphinxarg', 'test']

package_data = \
{'': ['*']}

install_requires = \
['sphinx>=1.2.0']

extras_require = \
{'markdown': ['CommonMark>=0.5.6']}

setup_kwargs = {
    'name': 'sphinx-argparse',
    'version': '0.3.1',
    'description': 'A sphinx extension that automatically documents argparse commands and options',
    'long_description': None,
    'author': 'Ash Berlin-Taylor',
    'author_email': 'ash_github@firemirror.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
