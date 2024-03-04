# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nornir',
 'nornir.core',
 'nornir.core.helpers',
 'nornir.core.plugins',
 'nornir.plugins',
 'nornir.plugins.connections',
 'nornir.plugins.functions',
 'nornir.plugins.inventory',
 'nornir.plugins.processors',
 'nornir.plugins.runners',
 'nornir.plugins.tasks']

package_data = \
{'': ['*']}

install_requires = \
['mypy_extensions>=0.4.1,<0.5.0',
 'ruamel.yaml>=0.16,<0.17',
 'typing_extensions>=3.7,<4.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.7,<0.8'],
 'docs': ['sphinx>=1,<2',
          'sphinx_rtd_theme>=0.4,<0.5',
          'sphinxcontrib-napoleon>=0.7,<0.8',
          'jupyter>=1,<2',
          'nbsphinx>=0.5,<0.6',
          'pygments>=2,<3',
          'sphinx-issues>=1.2,<2.0']}

entry_points = \
{'nornir.plugins.inventory': ['SimpleInventory = '
                              'nornir.plugins.inventory.simple:SimpleInventory'],
 'nornir.plugins.runners': ['serial = nornir.plugins.runners:SerialRunner',
                            'threaded = nornir.plugins.runners:ThreadedRunner']}

setup_kwargs = {
    'name': 'nornir',
    'version': '3.1.1',
    'description': 'Pluggable multi-threaded framework with inventory management to help operate collections of devices',
    'long_description': '![Build Status](https://github.com/nornir-automation/nornir/workflows/test%20nornir/badge.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Coverage Status](https://coveralls.io/repos/github/nornir-automation/nornir/badge.svg?branch=develop)](https://coveralls.io/github/nornir-automation/nornir?branch=develop)\n\n\nNornir\n=======\n\n![logo][logo]\n\nNornir is a pure Python automation framework intented to be used directly from Python. While most automation frameworks use their own Domain Specific Language (DSL) which you use to describe what you want to have done, Nornir lets you control everything from Python.\n\nOne of the benefits we want to highlight with this approach is the ease of troubleshooting, if something goes wrong you can just use your existing debug tools directly from Python (just add a line of `import pdb` & `pdb.set_trace()` and you\'re good to go). Doing the same using a DSL can be quite time consuming.\n\nWhat Nornir brings to the table is that it takes care of dealing with your inventory and manages the job of dispatching the tasks you want to run against your nodes and devices. The framework provides a very simple way to write plugins if you aren\'t happy with the ones we ship. Of course if you have written a plugin you think can be useful to others, please send us your code and test cases as a [pull request](https://github.com/nornir-automation/nornir/pulls).\n\n\nInstall\n=======\n\nPlease note that Nornir requires Python 3.6.2 or higher. Install Nornir with pip.\n\n```\npip install nornir\n```\n\nPlugins\n-------\n\nSince version 3.0.0 nornir doesn\'t ship with plugins, instead you can rely on `pip` to install them for you. You can find a non-exhaustive list of plugins in the following URL:\n\nhttps://nornir.tech/nornir/plugins/\n\nIf you wrote a plugin and want to add it to the list don\'t hesitate to [add it yourself](https://github.com/nornir-automation/nornir.tech.src/blob/master/data/nornir/plugins.yaml)\n\nDevelopment version\n-------------------\n\nIf you want to clone the repo and install it from there you will need to use [poetry](https://github.com/sdispater/poetry).\n\nDocumentation\n=============\n\nRead the [Nornir documentation](https://nornir.readthedocs.io/) online or review it\'s [code here](https://github.com/nornir-automation/nornir/tree/develop/docs)\n\nExamples\n========\n\nYou can find some examples and already made tools [here](https://github.com/nornir-automation/nornir-tools/)\n\nExternal Resources\n==================\n\nBelow you can find links to talks, blog posts, podcasts and other resources:\n\n* April 2019 - Packet Pushers podcast - [Heavy Networking 445: An Introduction To The Nornir Automation Framework](https://packetpushers.net/podcast/heavy-networking-445-an-introduction-to-the-nornir-automation-framework/)\n* May 2018 - Software Gone Wild podcast - [IPSpace podcast about nornir](http://blog.ipspace.net/2018/05/network-automation-with-brigade-on.html)\n* Sep 2018 - IPSpace network automation solutions - [Nornir workshop](https://my.ipspace.net/bin/list?id=NetAutSol&module=9#NORNIR) ([slides](https://github.com/dravetech/nornir-workshop/blob/master/nornir-workshop.pdf))\n* May 2018 - Networklore - [Introducing Nornir - The Python automation framework](https://networklore.com/introducing-brigade/)\n* May 2018 - Cisco blogs - [Exploring Nornir, the Python Automation Framework](https://blogs.cisco.com/developer/nornir-python-automation-framework)\n\n\nBugs & New features\n===================\n\nIf you think you have bug or would like to request a new feature, please register a GitHub account and [open an issue](https://github.com/nornir-automation/nornir/issues).\n\n\nContact & Support\n=================\n\nOfficial channel for communicating issues is via [GitHub issues](https://github.com/nornir-automation/nornir/issues) and you can use [GitHub discussions](https://github.com/nornir-automation/nornir/discussions) for general discussions around nornir. In addition, you can join the community in our ``#nornir`` channel in the [networktoCode Slack team](https://networktocode.herokuapp.com/).\n\n\nContributing to Nornir\n=======================\n\nIf you want to help the project, the [Contribution Guidelines](https://nornir.readthedocs.io/en/develop/contributing/index.html) is the best place to start.\n\n[logo]: docs/_static/logo/nornir_logo_02.jpg "nornir logo"\n',
    'author': 'David Barroso',
    'author_email': 'dbarrosop@dravetech.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nornir-automation/nornir',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
