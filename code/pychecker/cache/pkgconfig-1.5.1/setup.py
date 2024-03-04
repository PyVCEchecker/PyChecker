# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pkgconfig']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pkgconfig',
    'version': '1.5.1',
    'description': 'Interface Python with pkg-config',
    'long_description': "pkgconfig\n=========\n\n.. image:: https://travis-ci.org/matze/pkgconfig.png?branch=master\n    :target: https://travis-ci.org/matze/pkgconfig\n\n``pkgconfig`` is a Python module to interface with the ``pkg-config``\ncommand line tool and supports Python 2.6+ and 3.3+.\n\nIt can be used to\n\n-  find all pkg-config packages ::\n\n       >>> packages = pkgconfig.list_all()\n\n-  check if a package exists ::\n\n       >>> pkgconfig.exists('glib-2.0')\n       True\n\n-  check if a package meets certain version requirements ::\n\n       >>> pkgconfig.installed('glib-2.0', '< 2.26')\n       False\n\n-  return the version ::\n       >>> pkgconfig.modversion('glib-2.0')\n       '2.56.3'\n\n-  query CFLAGS and LDFLAGS ::\n\n       >>> pkgconfig.cflags('glib-2.0')\n       '-I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include'\n\n       >>> pkgconfig.libs('glib-2.0')\n       '-lglib-2.0'\n\n-  get all variables defined for a package::\n\n        >>> pkgconfig.variables('glib-2.0')\n        {u'exec_prefix': u'/usr'}\n\n-  parse the output to build extensions with setup.py ::\n\n       >>> d = pkgconfig.parse('glib-2.0 gtk+-2.0')\n       >>> d['libraries']\n       [u'gtk+-2.0', u'glib-2.0']\n\n   The ``pkgconfig.parse`` function returns a dictonary of lists.\n   The lists returned are accurate representations of the equivalent\n   ``pkg-config`` call's result, both in content and order.\n\nIf ``pkg-config`` is not on the path, raises ``EnvironmentError``.\n\nThe ``pkgconfig`` module is licensed under the MIT license.\n\n\nChangelog\n---------\n\nVersion 1.5.0\n~~~~~~~~~~~~~\n\n- Use poetry instead of setuptools directly\n- Fix #42: raise exception if package is missing\n- Fix version parsing for openssl-like version numbers, fixes #32\n- Fix #31: expose --modversion\n- Fix #30: strip whitespace from variable names\n\nVersion 1.4.0\n~~~~~~~~~~~~~\n\n- Add boolean ``static`` keyword to output private libraries as well\n- Raise original ``OSError`` as well\n\nVersion 1.3.1\n~~~~~~~~~~~~~\n\n- Fix compatibility problems with Python 2.6\n\nVersion 1.3.0\n~~~~~~~~~~~~~\n\n- Add variables() API to query defined variables\n- Disable Python 3.2 and enable Python 3.5 and 3.6 tests\n- Fix #16: handle spaces of values in .pc files correctly\n\nVersion 1.2.1 and 1.2.2\n~~~~~~~~~~~~~~~~~~~~~~~\n\nBug fix releases released on December 1st and 2nd 2016.\n\n- Include the ``data`` folder in the distribution in order to run tests\n- Improve the tests\n\n\nVersion 1.2.0\n~~~~~~~~~~~~~\n\nReleased on November 30th 2016.\n\n- Potential break: switch from result set to list\n- Expose --list-all query\n- Added support for PKG_CONFIG environment variable\n\n\nVersion 1.1.0\n~~~~~~~~~~~~~\n\nReleased on November 6th 2013.\n\n- Multiple packages can now be parsed with a single call to ``.parse``.\n\n\nVersion 1.0.0\n~~~~~~~~~~~~~\n\nFirst release on September 8th 2013.\n",
    'author': 'Matthias Vogelgesang',
    'author_email': 'matthias.vogelgesang@gmail.com',
    'url': 'https://github.com/matze/pkgconfig',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
}


setup(**setup_kwargs)
