# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyppeteer']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.3,<2.0.0',
 'pyee>=7.0.1,<8.0.0',
 'tqdm>=4.42.1,<5.0.0',
 'urllib3>=1.25.8,<2.0.0',
 'websockets>=8.1,<9.0']

entry_points = \
{'console_scripts': ['pyppeteer-install = pyppeteer.command:install']}

setup_kwargs = {
    'name': 'pyppeteer',
    'version': '0.2.2',
    'description': 'Headless chrome/chromium automation library (unofficial port of puppeteer)',
    'long_description': "pyppeteer\n==========\n\n[![PyPI](https://img.shields.io/pypi/v/pyppeteer.svg)](https://pypi.python.org/pypi/pyppeteer)\n[![PyPI version](https://img.shields.io/pypi/pyversions/pyppeteer.svg)](https://pypi.python.org/pypi/pyppeteer)\n[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://pyppeteer.github.io/pyppeteer/)\n[![CircleCI](https://circleci.com/gh/pyppeteer/pyppeteer.svg?style=shield)](https://circleci.com/gh/circleci/circleci-docs)\n[![codecov](https://codecov.io/gh/pyppeteer/pyppeteer/branch/dev/graph/badge.svg)](https://codecov.io/gh/pyppeteer/pyppeteer)\n\n_Note: this is a continuation of the original, apparently abandoned [pyppeteer project](https://github.com/miyakogi/pyppeteer)_\n\nUnofficial Python port of [puppeteer](https://github.com/GoogleChrome/puppeteer) JavaScript (headless) chrome/chromium browser automation library.\n\n* Free software: MIT license (including the work distributed under the Apache 2.0 license)\n* Documentation: https://pyppeteer.github.io/pyppeteer/\n\n## Installation\n\npyppeteer requires Python >= 3.6\n\nInstall with `pip` from PyPI:\n\n```\npip install pyppeteer\n```\n\nOr install the latest version from [this github repo](https://github.com/pyppeteer/pyppeteer/):\n\n```\npip install -U git+https://github.com/pyppeteer/pyppeteer@dev\n```\n\n## Usage\n\n> **Note**: When you run pyppeteer for the first time, it downloads the latest version of Chromium (~150MB) if it is not found on your system. If you don't prefer this behavior, ensure that a suitable Chrome binary is installed. One way to do this is to run `pyppeteer-install` command before prior to using this library.\n\nFull documentation can be found [here](https://pyppeteer.github.io/pyppeteer/reference.html). [Puppeteer's documentation](https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md#) and [its troubleshooting guide](https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md) are also great resources for puppeteer2 users.\n\n### Examples\n\nOpen web page and take a screenshot:\n```py\nimport asyncio\nfrom pyppeteer import launch\n\nasync def main():\n    browser = await launch()\n    page = await browser.newPage()\n    await page.goto('https://example.com')\n    await page.screenshot({'path': 'example.png'})\n    await browser.close()\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\nEvaluate javascript on a page:\n```py\nimport asyncio\nfrom pyppeteer import launch\n\nasync def main():\n    browser = await launch()\n    page = await browser.newPage()\n    await page.goto('https://example.com')\n    await page.screenshot({'path': 'example.png'})\n\n    dimensions = await page.evaluate('''() => {\n        return {\n            width: document.documentElement.clientWidth,\n            height: document.documentElement.clientHeight,\n            deviceScaleFactor: window.devicePixelRatio,\n        }\n    }''')\n\n    print(dimensions)\n    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}\n    await browser.close()\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\n## Differences between puppeteer and pyppeteer\n\npyppeteer strives to replicate the puppeteer API as close as possible, however, fundamental differences between Javascript and Python make this difficult to do precisely. More information on specifics can be found in the [documentation](https://pyppeteer.github.io/pyppeteer/reference.html).\n\n### Keyword arguments for options\n\npuppeteer uses an object for passing options to functions/methods. pyppeteer methods/functions accept both dictionary (python equivalent to JavaScript's objects) and keyword arguments for options.\n\nDictionary style options (similar to puppeteer):\n\n```python\nbrowser = await launch({'headless': True})\n```\n\nKeyword argument style options (more pythonic, isn't it?):\n\n```python\nbrowser = await launch(headless=True)\n```\n\n### Element selector method names\n\nIn python, `$` is not a valid identifier. The equivalent methods to Puppeteer's `$`, `$$`, and `$x` methods are listed below, along with some shorthand methods for your convenience:\n\n| puppeteer | pyppeteer              | pyppeteer shorthand |\n|-----------|-------------------------|----------------------|\n| Page.$()  | Page.querySelector()    | Page.J()             |\n| Page.$$() | Page.querySelectorAll() | Page.JJ()            |\n| Page.$x() | Page.xpath()            | Page.Jx()            |\n\n### Arguments of `Page.evaluate()` and `Page.querySelectorEval()`\n\npuppeteer's version of `evaluate()` takes a JavaScript function or a string representation of a JavaScript expression. pyppeteer takes string representation of JavaScript expression or function. pyppeteer will try to automatically detect if the string is function or expression, but it will fail sometimes. If an expression is erroneously treated as function and an error is raised, try setting `force_expr` to `True`, to force pyppeteer to treat the string as expression.\n\n### Examples:\n\nGet a page's `textContent`:\n\n```python\ncontent = await page.evaluate('document.body.textContent', force_expr=True)\n```\n\nGet an element's `textContent`:\n\n```python\nelement = await page.querySelector('h1')\ntitle = await page.evaluate('(element) => element.textContent', element)\n```\n\n## Roadmap\n\nSee [projects](https://github.com/pyppeteer/pyppeteer/projects)\n\n## Credits\n\n###### This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.\n",
    'author': 'pyppeteer',
    'author_email': 'pyppeteer@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pyppeteer/pyppeteer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
