# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pykka']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=1.6']}

setup_kwargs = {
    'name': 'pykka',
    'version': '3.0.1',
    'description': 'Pykka is a Python implementation of the actor model',
    'long_description': '# &#x1F300; Pykka\n\n_Pykka makes it easier to build concurrent applications._\n\n[![CI](https://img.shields.io/github/workflow/status/jodal/pykka/CI)](https://github.com/jodal/pykka/actions?workflow=CI)\n[![Docs](https://img.shields.io/readthedocs/pykka)](https://pykka.readthedocs.io/en/latest/)\n[![Coverage](https://img.shields.io/codecov/c/gh/jodal/pykka)](https://codecov.io/gh/jodal/pykka)\n[![PyPI](https://img.shields.io/pypi/v/pykka)](https://pypi.org/project/pykka/)\n\n---\n\nPykka is a Python implementation of the\n[actor model](https://en.wikipedia.org/wiki/Actor_model).\nThe actor model introduces some simple rules to control\nthe sharing of state and cooperation between execution units,\nwhich makes it easier to build concurrent applications.\n\nFor a quickstart guide and a complete API reference,\nsee the [documentation](https://pykka.readthedocs.io/).\n\n## Installation\n\nPykka requires Python 3.6 or newer.\n\nPykka is available from [PyPI](https://pypi.org/project/pykka/):\n\n```\npython3 -m pip install pykka\n```\n\nIf you need support for Python 2.7 or 3.5, you can use Pykka 2.\n\n## License\n\nPykka is copyright 2010-2021 Stein Magnus Jodal and contributors.\nPykka is licensed under the\n[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).\n',
    'author': 'Stein Magnus Jodal',
    'author_email': 'stein.magnus@jodal.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jodal/pykka',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
