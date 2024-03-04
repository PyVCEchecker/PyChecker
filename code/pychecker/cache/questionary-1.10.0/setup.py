# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['questionary', 'questionary.prompts']

package_data = \
{'': ['*']}

install_requires = \
['prompt_toolkit>=2.0,<4.0']

extras_require = \
{'docs': ['Sphinx>=3.3,<4.0',
          'sphinx-rtd-theme>=0.5.0,<0.6.0',
          'sphinx-autobuild>=2020.9.1,<2021.0.0',
          'sphinx-copybutton>=0.3.1,<0.4.0',
          'sphinx-autodoc-typehints>=1.11.1,<2.0.0']}

setup_kwargs = {
    'name': 'questionary',
    'version': '1.10.0',
    'description': 'Python library to build pretty command line user prompts ⭐️',
    'long_description': '# Questionary\n\n[![Version](https://img.shields.io/pypi/v/questionary.svg)](https://pypi.org/project/questionary/)\n[![License](https://img.shields.io/pypi/l/questionary.svg)](#)\n[![Continuous Integration](https://github.com/tmbo/questionary/workflows/Continuous%20Integration/badge.svg)](#)\n[![Coverage](https://coveralls.io/repos/github/tmbo/questionary/badge.svg?branch=master)](https://coveralls.io/github/tmbo/questionary?branch=master)\n[![Supported Python Versions](https://img.shields.io/pypi/pyversions/questionary.svg)](https://pypi.python.org/pypi/questionary)\n[![Documentation](https://readthedocs.org/projects/questionary/badge/?version=latest)](https://questionary.readthedocs.io/en/latest/?badge=latest)\n\n✨ Questionary is a Python library for effortlessly building pretty command line interfaces ✨\n\n* [Features](#features)\n* [Installation](#installation)\n* [Usage](#usage)\n* [Documentation](#documentation)\n* [Support](#support)\n\n\n![Example](https://raw.githubusercontent.com/tmbo/questionary/master/docs/images/example.gif)\n\n```python3\nimport questionary\n\nquestionary.text("What\'s your first name").ask()\nquestionary.password("What\'s your secret?").ask()\nquestionary.confirm("Are you amazed?").ask()\n\nquestionary.select(\n    "What do you want to do?",\n    choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],\n).ask()\n\nquestionary.rawselect(\n    "What do you want to do?",\n    choices=["Order a pizza", "Make a reservation", "Ask for opening hours"],\n).ask()\n\nquestionary.checkbox(\n    "Select toppings", choices=["foo", "bar", "bazz"]\n).ask()\n\nquestionary.path("Path to the projects version file").ask()\n```\n\nUsed and supported by\n\n[<img src="https://raw.githubusercontent.com/tmbo/questionary/master/docs/images/rasa-logo.svg" width="200">](https://github.com/RasaHQ/rasa)\n\n## Features\n\nQuestionary supports the following input prompts:\n \n * [Text](https://questionary.readthedocs.io/en/stable/pages/types.html#text)\n * [Password](https://questionary.readthedocs.io/en/stable/pages/types.html#password)\n * [File Path](https://questionary.readthedocs.io/en/stable/pages/types.html#file-path)\n * [Confirmation](https://questionary.readthedocs.io/en/stable/pages/types.html#confirmation)\n * [Select](https://questionary.readthedocs.io/en/stable/pages/types.html#select)\n * [Raw select](https://questionary.readthedocs.io/en/stable/pages/types.html#raw-select)\n * [Checkbox](https://questionary.readthedocs.io/en/stable/pages/types.html#checkbox)\n * [Autocomplete](https://questionary.readthedocs.io/en/stable/pages/types.html#autocomplete)\n\nThere is also a helper to [print formatted text](https://questionary.readthedocs.io/en/stable/pages/types.html#printing-formatted-text)\nfor when you want to spice up your printed messages a bit.\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install Questionary:\n\n```bash\n$ pip install questionary\n✨🎂✨\n```\n\n## Usage\n\n```python\nimport questionary\n\nquestionary.select(\n    "What do you want to do?",\n    choices=[\n        \'Order a pizza\',\n        \'Make a reservation\',\n        \'Ask for opening hours\'\n    ]).ask()  # returns value of selection\n```\n\nThat\'s all it takes to create a prompt! Have a [look at the documentation](https://questionary.readthedocs.io/)\nfor some more examples.\n\n## Documentation\n\nDocumentation for Questionary is available [here](https://questionary.readthedocs.io/).\n\n## Support\n\nPlease [open an issue](https://github.com/tmbo/questionary/issues/new)\nwith enough information for us to reproduce your problem.\nA [minimal, reproducible example](https://stackoverflow.com/help/minimal-reproducible-example)\nwould be very helpful.\n\n## Contributing\n\nContributions are very much welcomed and appreciated. Head over to the documentation on [how to contribute](https://questionary.readthedocs.io/en/stable/pages/contributors.html#steps-for-submitting-code).\n\n## Authors and Acknowledgment\n\nQuestionary is written and maintained by Tom Bocklisch and Kian Cross.\n\nIt is based on the great work by [Oyetoke Toby](https://github.com/CITGuru/PyInquirer) \nand [Mark Fink](https://github.com/finklabs/whaaaaat).\n\n## License\nLicensed under the [MIT License](https://github.com/tmbo/questionary/blob/master/LICENSE). Copyright 2021 Tom Bocklisch.\n',
    'author': 'Tom Bocklisch',
    'author_email': 'tombocklisch@gmail.com',
    'maintainer': 'Tom Bocklisch',
    'maintainer_email': 'tombocklisch@gmail.com',
    'url': 'https://github.com/tmbo/questionary',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
