# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['checksumdir']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['checksumdir = checksumdir.cli:main']}

setup_kwargs = {
    'name': 'checksumdir',
    'version': '1.2.0',
    'description': 'Compute a single hash of the file contents of a directory.',
    'long_description': "***********\nChecksumdir\n***********\n\n|badge1| |badge2|\n\n\n.. |badge1| image:: https://img.shields.io/pypi/dm/checksumdir   \n    :alt: PyPI - Downloads\n    :target: https://pypi.org/project/checksumdir/\n\n.. |badge2| image:: https://badge.fury.io/py/checksumdir.svg\n    :target: https://pypi.org/project/checksumdir/\n\nA simple module for creating a single hash for a directory of files, with file contents;\nignoring any metadata such as file name.  Options exist to also exclude specific files\nor files with specific extensions.\n\n=====\nUsage\n=====\n\n.. code-block:: python\n\n    from checksumdir import dirhash\n\n    directory  = '/path/to/directory/'\n    md5hash    = dirhash(directory, 'md5')\n    sha1hash   = dirhash(directory, 'sha1', excluded_files=['package.json'])\n    sha256hash = dirhash(directory, 'sha256', excluded_extensions=['pyc'])\n\n\nOr to use the CLI:\n\n.. code-block:: bash\n\n    # Defaults to md5.\n    $ checksumdir /path/to/directory\n\n    # Create sha1 hash:\n    $ checksumdir -a sha1 /path/to/directory\n\n    # Exclude files:\n    $ checksumdir -e <files> /path/to/directory\n\n    # Exclude files with specific extensions:\n    $ checksumdir -x <extensions> /path/to/directory\n\n    # Follow soft links:\n    $ checksumdir --follow-links /path/to/directory\n",
    'author': 'Tom McCarthy',
    'author_email': 'tmac.se@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://github.com/cakepietoast/checksumdir',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
