# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tinydb_smartcache']

package_data = \
{'': ['*']}

install_requires = \
['tinydb>=4.0,<5.0']

setup_kwargs = {
    'name': 'tinydb-smartcache',
    'version': '2.0.0',
    'description': 'A smarter query cache for TinyDB',
    'long_description': "tinydb-smartcache\n^^^^^^^^^^^^^^^^^\n\n|Build Status| |Coverage| |Version|\n\n``tinydb-smartcache`` provides a smart query cache for TinyDB. It updates the\nquery cache when inserting/removing/updating elements so the cache doesn't get\ninvalidated. It's useful if you perform lots of queries while the data changes\nonly a little.\n\nInstallation\n************\n\n.. code-block:: bash\n\n    $ pip install tinydb_smartcache\n\nUsage\n*****\n\n.. code-block:: python\n\n    >>> from tinydb import TinyDB\n    >>> from tinydb_smartcache import SmartCacheTable\n    >>> db = TinyDB('db.json')\n    >>> db.table_class = SmartCacheTable\n    >>> db.table('foo')\n    >>> # foo will now use the smart query cache\n\nIf you want to enable TinyDB for all databases in a session, run:\n\n.. code-block:: python\n\n    >>> from tinydb import TinyDB\n    >>> from tinydb_smartcache import SmartCacheTable\n    >>> TinyDB.table_class = SmartCacheTable\n    >>> # All databases/tables will now use the smart query cache\n\nChangelog\n*********\n\n**v2.0.0** (2020-08-25)\n-----------------------\n\n- Add support for TinyDB v4. Drops support for TinyDB <= 3 and Python 2.\n\n**v1.0.3** (2019-10-26)\n-----------------------\n\n- Make ``SmartCacheTable`` work again after breakage with TinyDB v3.12.0\n\n**v1.0.2** (2015-11-17)\n-----------------------\n\n- Account for changes in TinyDB 3.0\n\n**v1.0.1** (2015-11-17)\n-----------------------\n\n- Fix installation via pip\n\n**v1.0.0** (2015-09-17)\n-----------------------\n\n- Initial release on PyPI\n\n.. |Build Status| image:: https://img.shields.io/github/workflow/status/msiemens/tinydb-smartcache/Python%20CI?style=flat-square\n   :target: https://github.com/msiemens/tinydb-smartcache/actions?query=workflow%3A%22Python+CI%22\n.. |Coverage| image:: http://img.shields.io/coveralls/msiemens/tinydb-smartcache.svg?style=flat-square\n   :target: https://coveralls.io/r/msiemens/tinydb-smartcache\n.. |Version| image:: http://img.shields.io/pypi/v/tinydb-smartcache.svg?style=flat-square\n   :target: https://pypi.python.org/pypi/tinydb-smartcache/\n",
    'author': 'Markus Siemens',
    'author_email': 'markus@m-siemens.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
