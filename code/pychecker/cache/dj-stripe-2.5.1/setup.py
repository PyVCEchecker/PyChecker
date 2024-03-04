# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['djstripe',
 'djstripe.management',
 'djstripe.management.commands',
 'djstripe.migrations',
 'djstripe.models']

package_data = \
{'': ['*'],
 'djstripe': ['locale/fr/LC_MESSAGES/*',
              'locale/ru/LC_MESSAGES/*',
              'templates/djstripe/admin/*']}

install_requires = \
['Django>=2.2', 'jsonfield>=3.0', 'stripe>=2.48.0']

extras_require = \
{'docs': ['mkdocs>=1.1.2,<2.0.0', 'mkautodoc>=0.1.0,<0.2.0']}

setup_kwargs = {
    'name': 'dj-stripe',
    'version': '2.5.1',
    'description': 'Django + Stripe made easy',
    'long_description': '# dj-stripe\n\n[![Documentation](https://readthedocs.org/projects/dj-stripe/badge/)](https://dj-stripe.readthedocs.io/)\n[![Sponsor dj-stripe](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub)](https://github.com/sponsors/dj-stripe)\n\nStripe Models for Django.\n\n## Introduction\n\ndj-stripe implements all of the Stripe models, for Django. Set up your\nwebhook endpoint and start receiving model updates. You will then have\na copy of all the Stripe models available in Django models, as soon as\nthey are updated!\n\nThe full documentation is available [on Read the Docs](https://dj-stripe.readthedocs.io/).\n\n## Features\n\n-   Stripe Core\n-   Stripe Billing\n-   Stripe Cards (JS v2) and Sources (JS v3)\n-   Payment Methods and Payment Intents (SCA support)\n-   Support for multiple accounts and API keys\n-   Stripe Connect (partial support)\n-   Tested with Stripe API `2020-08-27` (see [API versions](https://dj-stripe.readthedocs.io/en/latest/api_versions.html))\n\n## Requirements\n\n-   Django 2.2+\n-   Python 3.6+\n-   PostgreSQL engine (recommended) 9.5+\n-   MySQL engine: MariaDB 10.2+ or MySQL 5.7+\n-   SQLite: Not recommended in production. Version 3.26+ required.\n\n## Quickstart\n\nInstall dj-stripe with pip:\n\n    pip install dj-stripe\n\nOr with [Poetry](https://python-poetry.org/) (recommended):\n\n    poetry add dj-stripe\n\nAdd `djstripe` to your `INSTALLED_APPS`:\n\n    INSTALLED_APPS =(\n        ...\n        "djstripe",\n        ...\n    )\n\nAdd to urls.py:\n\n    path("stripe/", include("djstripe.urls", namespace="djstripe")),\n\nTell Stripe about the webhook (Stripe webhook docs can be found\n[here](https://stripe.com/docs/webhooks)) using the full URL of your\nendpoint from the urls.py step above (e.g.\n`https://example.com/stripe/webhook`).\n\nAdd your Stripe keys and other settings:\n\n```py\nSTRIPE_LIVE_SECRET_KEY = os.environ.get("STRIPE_LIVE_SECRET_KEY", "<live secret key>")\nSTRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "<test secret key>")\nSTRIPE_LIVE_MODE = False  # Change to True in production\nDJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # Get it from the section in the Stripe dashboard where you added the webhook endpoint\nDJSTRIPE_USE_NATIVE_JSONFIELD = True  # We recommend setting to True for new installations\nDJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"  # Set to `"id"` for all new 2.4+ installations\n```\n\nAdd some payment plans via the Stripe.com dashboard.\n\nRun the commands:\n\n    python manage.py migrate\n\n    python manage.py djstripe_sync_models\n\nSee <https://dj-stripe.readthedocs.io/en/latest/stripe_elements_js.html>\nfor notes about usage of the Stripe Elements frontend JS library.\n\n## Running the Tests\n\nAssuming the tests are run against PostgreSQL:\n\n    createdb djstripe\n    pytest\n\n# Changelog\n\n[See release notes on Read the Docs](https://dj-stripe.readthedocs.io/en/latest/history/2_4_0/).\n\n# Funding this project\n\n[![Stripe Logo](./docs/logos/stripe_blurple.svg)](https://stripe.com)\n\nYou can now become a sponsor to dj-stripe with [GitHub Sponsors](https://github.com/sponsors/dj-stripe).\n\nWe\'ve been bringing dj-stripe to the world for over 7 years and are excited to be able to start\ndedicating some real resources to the project.\n\nYour sponsorship helps us keep a team of maintainers actively working to improve dj-stripe and\nensure it stays up-to-date with the latest Stripe changes. If you\'re using dj-stripe in a commercial\ncapacity and have the ability to start a sponsorship, we\'d greatly appreciate the contribution.\n\nAll contributions through GitHub sponsors flow into our [Open Collective](https://opencollective.com/dj-stripe),\nwhich holds our funds and keeps an open ledger on how donations are spent.\n\n## Similar libraries\n\n-   [dj-paypal](https://github.com/HearthSim/dj-paypal)\n    ([PayPal](https://www.paypal.com/))\n-   [dj-paddle](https://github.com/paddle-python/dj-paddle)\n    ([Paddle](https://paddle.com/))\n',
    'author': 'Alexander Kavanaugh',
    'author_email': 'alex@kavdev.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dj-stripe/dj-stripe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
