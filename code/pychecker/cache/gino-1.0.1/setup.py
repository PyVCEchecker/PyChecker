# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gino', 'gino.dialects', 'gino.ext']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.2.16,<1.4', 'asyncpg>=0.18,<1.0']

extras_require = \
{':python_version < "3.7"': ['contextvars>=2.4,<3.0'],
 ':python_version < "3.8"': ['importlib_metadata>=1.3.0,<2.0.0'],
 'aiohttp:python_version >= "3.5.3" and python_version < "4.0.0"': ['gino-aiohttp>=0.1.0,<0.2.0'],
 'quart:python_version >= "3.7" and python_version < "4.0"': ['gino-quart>=0.1.0,<0.2.0'],
 'sanic:python_version >= "3.6" and python_version < "4.0"': ['gino-sanic>=0.1.0,<0.2.0'],
 'starlette:python_version >= "3.6" and python_version < "4.0"': ['gino-starlette>=0.1.1,<0.2.0'],
 'tornado:python_version >= "3.5.2" and python_version < "4.0.0"': ['gino-tornado>=0.1.0,<0.2.0']}

entry_points = \
{'sqlalchemy.dialects': ['asyncpg = gino.dialects.asyncpg:AsyncpgDialect',
                         'postgresql.asyncpg = '
                         'gino.dialects.asyncpg:AsyncpgDialect']}

setup_kwargs = {
    'name': 'gino',
    'version': '1.0.1',
    'description': 'GINO Is Not ORM - a Python asyncio ORM on SQLAlchemy core.',
    'long_description': '======\n|GINO|\n======\n\n.. image:: https://img.shields.io/pypi/v/gino?logo=python&logoColor=white\n        :alt: PyPI Release Version\n        :target: https://pypi.python.org/pypi/gino\n\n.. image:: https://img.shields.io/github/workflow/status/python-gino/gino/test?label=test&logo=github\n        :alt: GitHub Workflow Status for tests\n        :target: https://github.com/python-gino/gino/actions?query=workflow%3Atest\n\n.. image:: https://img.shields.io/github/workflow/status/python-gino/gino/docs?label=docs&logo=github\n        :alt: GitHub Workflow Status for docs\n        :target: https://python-gino.org/docs/\n\n.. image:: https://img.shields.io/codacy/coverage/b6a59cdf5ca64eab9104928d4f9bbb97?logo=codacy\n        :alt: Codacy coverage\n        :target: https://app.codacy.com/gh/python-gino/gino/dashboard\n\n.. image:: https://img.shields.io/badge/Dependabot-active-brightgreen?logo=dependabot\n        :target: https://app.dependabot.com/accounts/python-gino/projects/129260\n        :alt: Dependabot\n\n.. image:: https://img.shields.io/gitter/room/python-gino/Lobby?logo=gitter\n        :target: https://gitter.im/python-gino/Lobby\n        :alt: Gitter chat\n\n\nGINO - GINO Is Not ORM - is a lightweight asynchronous ORM built on top of\nSQLAlchemy_ core for Python asyncio_. GINO 1.0 supports only PostgreSQL_ with asyncpg_.\n\n* Free software: BSD license\n* Requires: Python 3.5\n* GINO is developed proudly with |PyCharm|.\n\n\nHome\n----\n\n`python-gino.org <https://python-gino.org/>`__\n\n\nDocumentation\n-------------\n\n* English_\n* Chinese_\n\n\nInstallation\n------------\n\n.. code-block:: console\n\n    $ pip install gino\n\n\nFeatures\n--------\n\n* Robust SQLAlchemy-asyncpg bi-translator with no hard hack\n* Asynchronous SQLAlchemy-alike engine and connection\n* Asynchronous dialect API\n* Asynchronous-friendly CRUD objective models\n* Well-considered contextual connection and transaction management\n* Reusing native SQLAlchemy core to build queries with grammar sugars\n* Support SQLAlchemy ecosystem, e.g. Alembic_ for migration\n* `Community support <https://github.com/python-gino/>`_ for Starlette_/FastAPI_, aiohttp_, Sanic_, Tornado_ and Quart_\n* Rich PostgreSQL JSONB support\n\n\n.. _SQLAlchemy: https://www.sqlalchemy.org/\n.. _asyncpg: https://github.com/MagicStack/asyncpg\n.. _PostgreSQL: https://www.postgresql.org/\n.. _asyncio: https://docs.python.org/3/library/asyncio.html\n.. _Alembic: https://bitbucket.org/zzzeek/alembic\n.. _Sanic: https://github.com/channelcat/sanic\n.. _Tornado: http://www.tornadoweb.org/\n.. _Quart: https://gitlab.com/pgjones/quart/\n.. _English: https://python-gino.org/docs/en/\n.. _Chinese: https://python-gino.org/docs/zh/\n.. _aiohttp: https://github.com/aio-libs/aiohttp\n.. _Starlette: https://www.starlette.io/\n.. _FastAPI: https://fastapi.tiangolo.com/\n.. |PyCharm| image:: ./docs/images/pycharm.svg\n        :height: 20px\n        :target: https://www.jetbrains.com/?from=GINO\n\n.. |GINO| image:: ./docs/theme/static/logo.svg\n        :alt: GINO\n        :height: 64px\n        :target: https://python-gino.org/\n',
    'author': 'Fantix King',
    'author_email': 'fantix.king@gmail.com',
    'maintainer': 'Tony Wang',
    'maintainer_email': 'wwwjfy@gmail.com',
    'url': 'https://python-gino.org',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
