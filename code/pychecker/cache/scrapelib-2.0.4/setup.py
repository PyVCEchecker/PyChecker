# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scrapelib', 'scrapelib.tests']

package_data = \
{'': ['*']}

install_requires = \
['requests[security]>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['scrapeshell = scrapelib.__main__:scrapeshell']}

setup_kwargs = {
    'name': 'scrapelib',
    'version': '2.0.4',
    'description': '',
    'long_description': "=========\nscrapelib\n=========\n\n.. image:: https://github.com/jamesturk/scrapelib/workflows/Test/badge.svg\n    :target: https://github.com/jamesturk/scrapelib/actions\n\n.. image:: https://coveralls.io/repos/jamesturk/scrapelib/badge.png?branch=master\n    :target: https://coveralls.io/r/jamesturk/scrapelib\n\n.. image:: https://img.shields.io/pypi/v/scrapelib.svg\n    :target: https://pypi.python.org/pypi/scrapelib\n\n.. image:: https://readthedocs.org/projects/scrapelib/badge/?version=latest\n    :target: https://readthedocs.org/projects/scrapelib/?badge=latest\n    :alt: Documentation Status\n\nscrapelib is a library for making requests to less-than-reliable websites, it is implemented\n(as of 0.7) as a wrapper around `requests <http://python-requests.org>`_.\n\nscrapelib originated as part of the `Open States <http://openstates.org/>`_\nproject to scrape the websites of all 50 state legislatures and as a result\nwas therefore designed with features desirable when dealing with sites that\nhave intermittent errors or require rate-limiting.\n\nAdvantages of using scrapelib over alternatives like httplib2 simply using\nrequests as-is:\n\n* All of the power of the suberb `requests <http://python-requests.org>`_ library.\n* HTTP, HTTPS, and FTP requests via an identical API\n* support for simple caching with pluggable cache backends\n* request throttling\n* configurable retries for non-permanent site failures\n\nWritten by James Turk <dev@jamesturk.net>, thanks to Michael Stephens for\ninitial urllib2/httplib2 version\n\nSee https://github.com/jamesturk/scrapelib/graphs/contributors for contributors.\n\nRequirements\n============\n\n* python >=3.7\n* requests >= 2.0\n\n\nExample Usage\n=============\n\nDocumentation: http://scrapelib.readthedocs.org/en/latest/\n\n::\n\n  import scrapelib\n  s = scrapelib.Scraper(requests_per_minute=10)\n\n  # Grab Google front page\n  s.get('http://google.com')\n\n  # Will be throttled to 10 HTTP requests per minute\n  while True:\n      s.get('http://example.com')\n",
    'author': 'James Turk',
    'author_email': 'dev@jamesturk.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jamesturk/scrapelib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
