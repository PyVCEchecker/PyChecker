# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['xdg']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xdg',
    'version': '5.1.1',
    'description': 'Variables defined by the XDG Base Directory Specification',
    'long_description': '# xdg\n\n[![Licence](https://img.shields.io/github/license/srstevenson/xdg?label=Licence&color=blue)](https://github.com/srstevenson/xdg/blob/main/LICENCE)\n[![GitHub release](https://img.shields.io/github/v/release/srstevenson/xdg?label=GitHub)](https://github.com/srstevenson/xdg)\n[![PyPI version](https://img.shields.io/pypi/v/xdg?label=PyPI)](https://pypi.org/project/xdg/)\n[![Python versions](https://img.shields.io/pypi/pyversions/xdg?label=Python)](https://pypi.org/project/xdg/)\n[![CI status](https://github.com/srstevenson/xdg/workflows/CI/badge.svg)](https://github.com/srstevenson/xdg/actions)\n[![Coverage](https://img.shields.io/codecov/c/gh/srstevenson/xdg?label=Coverage)](https://codecov.io/gh/srstevenson/xdg)\n\n`xdg` is a Python module which provides functions to return paths to the\ndirectories defined by the [XDG Base Directory Specification][spec], to save you\nfrom duplicating the same snippet of logic in every Python utility you write\nthat deals with user cache, configuration, or data files. It has no external\ndependencies.\n\n## Installation\n\nTo install the latest release from [PyPI], use [pip]:\n\n```bash\npython3 -m pip install xdg\n```\n\nThe latest release of `xdg` currently implements version 0.8 of the\nspecification, released on 8th May 2021.\n\nIn Python projects using [Poetry] or [Pipenv] for dependency management, add\n`xdg` as a dependency with `poetry add xdg` or `pipenv install xdg`.\nAlternatively, since `xdg` is only a single file you may prefer to just copy\n`src/xdg/__init__.py` from the source distribution into your project.\n\n## Usage\n\n```python\nfrom xdg import (\n    xdg_cache_home,\n    xdg_config_dirs,\n    xdg_config_home,\n    xdg_data_dirs,\n    xdg_data_home,\n    xdg_runtime_dir,\n    xdg_state_home,\n)\n```\n\n`xdg_cache_home()`, `xdg_config_home()`, `xdg_data_home()`, and\n`xdg_state_home()` return [`pathlib.Path` objects][path] containing the value of\nthe environment variable named `XDG_CACHE_HOME`, `XDG_CONFIG_HOME`,\n`XDG_DATA_HOME`, and `XDG_STATE_HOME` respectively, or the default defined in\nthe specification if the environment variable is unset, empty, or contains a\nrelative path rather than absolute path.\n\n`xdg_config_dirs()` and `xdg_data_dirs()` return a list of `pathlib.Path`\nobjects containing the value, split on colons, of the environment variable named\n`XDG_CONFIG_DIRS` and `XDG_DATA_DIRS` respectively, or the default defined in\nthe specification if the environment variable is unset or empty. Relative paths\nare ignored, as per the specification.\n\n`xdg_runtime_dir()` returns a `pathlib.Path` object containing the value of the\n`XDG_RUNTIME_DIR` environment variable, or `None` if the environment variable is\nnot set, or contains a relative path rather than absolute path.\n\n## Copyright\n\nCopyright © 2016-2021 [Scott Stevenson].\n\n`xdg` is distributed under the terms of the [ISC licence].\n\n[isc licence]: https://opensource.org/licenses/ISC\n[path]: https://docs.python.org/3/library/pathlib.html#pathlib.Path\n[pip]: https://pip.pypa.io/en/stable/\n[pipenv]: https://docs.pipenv.org/\n[poetry]: https://python-poetry.org/\n[pypi]: https://pypi.org/project/xdg/\n[scott stevenson]: https://scott.stevenson.io\n[spec]:\n  https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html\n',
    'author': 'Scott Stevenson',
    'author_email': 'scott@stevenson.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/srstevenson/xdg',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
