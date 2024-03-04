# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['libthumbor', 'libthumbor.django', 'libthumbor.url_signers']

package_data = \
{'': ['*']}

install_requires = \
['six>=1.14.0,<2.0.0']

setup_kwargs = {
    'name': 'libthumbor',
    'version': '2.0.1',
    'description': 'libthumbor is the python extension to generate thumbor URLs',
    'long_description': "[![Build Status](https://secure.travis-ci.org/thumbor/libthumbor.png)](http://travis-ci.org/thumbor/libthumbor) [![Coverage Status](https://coveralls.io/repos/github/thumbor/libthumbor/badge.svg?branch=master)](https://coveralls.io/github/thumbor/libthumbor?branch=master)\n\nlibthumbor allows easy usage of\n[thumbor](http://github.com/thumbor/thumbor) in Python. Check the docs for django integration.\n\nThis version is compliant with the new URL generation schema (thumbor 3.0.0 and up).\n\n## Using it\n\n```python\nfrom libthumbor import CryptoURL\n\ncrypto = CryptoURL(key='my-security-key')\n\nencrypted_url = crypto.generate(\n    width=300,\n    height=200,\n    smart=True,\n    image_url='/path/to/my/image.jpg'\n)\n```\n\n## Docs\n\nCheck the wiki for more information on using libthumbor.\n\n## Contributions\n\n### Bernardo Heynemann\n\n* Generic URL encryption\n\n### Rafael Caricio\n\n* Django Generic View and URL\n\n### Fábio Costa\n\n* Django Generic View and URL\n",
    'author': 'Bernardo Heynemann',
    'author_email': 'heynemann@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
