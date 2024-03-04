# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['split_settings']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'django-split-settings',
    'version': '1.1.0',
    'description': 'Organize Django settings into multiple files and directories. Easily override and modify settings. Use wildcards and optional settings files.',
    'long_description': '<p align="center">\n  <img src="https://raw.githubusercontent.com/sobolevn/django-split-settings/master/docs/_static/logo-black.png"\n       alt="django-split-settings logo">\n</p>\n\n---\n\n[![wemake.services](https://img.shields.io/badge/%20-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services)\n[![test](https://github.com/sobolevn/django-split-settings/workflows/test/badge.svg)](https://github.com/sobolevn/django-split-settings/actions?query=workflow%3Atest)\n[![codecov](https://codecov.io/gh/sobolevn/django-split-settings/branch/master/graph/badge.svg)](https://codecov.io/gh/sobolevn/django-split-settings)\n[![Docs](https://readthedocs.org/projects/django-split-settings/badge/?version=latest)](http://django-split-settings.readthedocs.io/en/latest/?badge=latest)\n[![Python Version](https://img.shields.io/pypi/pyversions/django-split-settings.svg)](https://pypi.org/project/django-split-settings/)\n[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)\n\n\n\nOrganize Django settings into multiple files and directories. Easily\noverride and modify settings. Use wildcards in settings file paths\nand mark settings files as optional.\n\nRead [this blog post](https://sobolevn.me/2017/04/managing-djangos-settings)\nfor more information.\nAlso, check this [example project](https://github.com/wemake-services/wemake-django-template).\n\n\n## Requirements\n\nWhile this package will most likely work with the most versions of `django`, we [officially support](https://github.com/sobolevn/django-split-settings/blob/master/.travis.yml):\n\n- 1.11\n- 2.2\n- 3.0\n- 3.1\n\nThis package has no dependencies itself.\n\nIn case you need older `python` / `django` versions support,\nthen consider using older versions of `django-split-settings`.\n\n\n## Installation\n\n```bash\npip install django-split-settings\n```\n\n\n## Usage\n\nReplace your existing `settings.py` with a list of components that\nmake up your Django settings. Preferably create a settings package\nthat contains all the files.\n\nHere\'s a minimal example:\n\n```python\nfrom split_settings.tools import optional, include\n\ninclude(\n    \'components/base.py\',\n    \'components/database.py\',\n    optional(\'local_settings.py\')\n)\n```\n\nIn the example, the files `base.py` and `database.py` are included\nin that order from the subdirectory called `components/`.\n`local_settings.py` in the same directory is included if it exists.\n\n**Note:** The local context is passed on to each file, so each\nfollowing file can access and modify the settings declared in the\nprevious files.\n\nWe also made an in-depth [tutorial](https://sobolevn.me/2017/04/managing-djangos-settings).\n\n\n## Tips and tricks\n\nYou can use wildcards in file paths:\n\n```python\ninclude(\'components/my_app/*.py\')\n```\n\nNote that files are included in the order that `glob` returns them,\nprobably in the same order as what `ls -U` would list them. The\nfiles are NOT in alphabetical order.\n\nYou can modify common settings in environment settings simply importing them\n\n```python\n# local_settings.py\nfrom components.base import INSTALLED_APPS\n\nINSTALLED_APPS += (\n  \'raven.contrib.django.raven_compat\',\n)\n```\n\n\n## Do you want to contribute?\n\nRead the [CONTRIBUTING.md](https://github.com/sobolevn/django-split-settings/blob/master/CONTRIBUTING.md) file.\n\n\n## Version history\n\nSee [CHANGELOG.md](https://github.com/sobolevn/django-split-settings/blob/master/CHANGELOG.md) file.\n',
    'author': 'sobolevn',
    'author_email': 'mail@sobolevn.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://django-split-settings.readthedocs.io',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
