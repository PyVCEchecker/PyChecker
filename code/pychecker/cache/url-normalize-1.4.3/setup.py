# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['url_normalize']

package_data = \
{'': ['*']}

install_requires = \
['six']

setup_kwargs = {
    'name': 'url-normalize',
    'version': '1.4.3',
    'description': 'URL normalization for Python',
    'long_description': 'url-normalize\n=============\n\n[![Build Status](https://travis-ci.org/niksite/url-normalize.svg?branch=master)](https://travis-ci.org/niksite/url-normalize)\n[![Coverage Status](https://coveralls.io/repos/github/niksite/url-normalize/badge.svg?branch=master)](https://coveralls.io/github/niksite/url-normalize?branch=master)\n\nURI Normalization function:\n\n* Take care of IDN domains.\n* Always provide the URI scheme in lowercase characters.\n* Always provide the host, if any, in lowercase characters.\n* Only perform percent-encoding where it is essential.\n* Always use uppercase A-through-F characters when percent-encoding.\n* Prevent dot-segments appearing in non-relative URI paths.\n* For schemes that define a default authority, use an empty authority if the default is desired.\n* For schemes that define an empty path to be equivalent to a path of "/", use "/".\n* For schemes that define a port, use an empty port if the default is desired\n* All portions of the URI must be utf-8 encoded NFC from Unicode strings\n\nInspired by Sam Ruby\'s [urlnorm.py](http://intertwingly.net/blog/2004/08/04/Urlnorm)\n\nExample:\n\n```sh\n$ pip install url-normalize\nCollecting url-normalize\n...\nSuccessfully installed future-0.16.0 url-normalize-1.3.3\n$ python\nPython 3.6.1 (default, Jul  8 2017, 05:00:20)\n[GCC 4.9.2] on linux\nType "help", "copyright", "credits" or "license" for more information.\n> from url_normalize import url_normalize\n> print(url_normalize(\'www.foo.com:80/foo\'))\n> https://www.foo.com/foo\n```\n\nHistory:\n\n* 1.4.3: Added LICENSE file\n* 1.4.2: Added an optional param sort_query_params (True by default)\n* 1.4.1: Added an optional param default_scheme to the url_normalize (\'https\' by default)\n* 1.4.0: A bit of code refactoring and cleanup\n* 1.3.3: Support empty string and double slash urls (//domain.tld)\n* 1.3.2: Same code support both Python 3 and Python 2.\n* 1.3.1: Python 3 compatibility\n* 1.2.1: PEP8, setup.py\n* 1.1.2: support for shebang (#!) urls\n* 1.1.1: using \'http\' schema by default when appropriate\n* 1.1.0: added handling of IDN domains\n* 1.0.0: code pep8\n* 0.1.0: forked from Sam Ruby\'s urlnorm.py\n\nLicense: MIT License\n',
    'author': 'Nikolay Panov',
    'author_email': 'github@npanov.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/niksite/url-normalize',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
}


setup(**setup_kwargs)
