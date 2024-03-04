# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['djoser',
 'djoser.social',
 'djoser.social.backends',
 'djoser.social.token',
 'djoser.urls']

package_data = \
{'': ['*'],
 'djoser': ['locale/de/LC_MESSAGES/django.po',
            'locale/es/LC_MESSAGES/django.po',
            'locale/fr/LC_MESSAGES/django.po',
            'locale/ka/LC_MESSAGES/django.po',
            'locale/pl/LC_MESSAGES/django.po',
            'locale/pt_BR/LC_MESSAGES/django.po',
            'locale/ru_RU/LC_MESSAGES/django.po',
            'templates/email/*']}

install_requires = \
['asgiref>=3.2.10,<4.0.0',
 'coreapi>=2.3.3,<3.0.0',
 'django-templated-mail>=1.1.1,<2.0.0',
 'djangorestframework-simplejwt>=4.3.0,<5.0.0',
 'social-auth-app-django>=4.0.0,<5.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0'],
 'test': ['pytest>=6.0.2,<7.0.0',
          'codecov>=2.0.16,<3.0.0',
          'coverage>=5.3,<6.0',
          'pytest-cov>=2.10.1,<3.0.0',
          'pytest-django>=3.10.0,<4.0.0',
          'pytest-pythonpath>=0.7.3,<0.8.0',
          'djet>=0.2.2,<0.3.0']}

setup_kwargs = {
    'name': 'djoser',
    'version': '2.1.0',
    'description': 'REST implementation of Django authentication system.',
    'long_description': '======\ndjoser\n======\n\n.. image:: https://img.shields.io/pypi/v/djoser.svg\n   :target: https://pypi.org/project/djoser\n\n.. image:: https://img.shields.io/travis/sunscrapers/djoser/master.svg\n   :target: https://travis-ci.org/sunscrapers/djoser\n\n.. image:: https://img.shields.io/codecov/c/github/sunscrapers/djoser.svg\n   :target: https://codecov.io/gh/sunscrapers/djoser\n\n.. image:: https://api.codacy.com/project/badge/Grade/c9bf80318d2741e5bb63912a5e0b32dc\n   :alt: Codacy Badge\n   :target: https://app.codacy.com/app/dekoza/djoser?utm_source=github.com&utm_medium=referral&utm_content=sunscrapers/djoser&utm_campaign=Badge_Grade_Dashboard\n\n.. image:: https://img.shields.io/pypi/dm/djoser\n   :target: https://img.shields.io/pypi/dm/djoser\n\n\nREST implementation of `Django <https://www.djangoproject.com/>`_ authentication\nsystem. **djoser** library provides a set of `Django Rest Framework <https://www.django-rest-framework.org/>`_\nviews to handle basic actions such as registration, login, logout, password\nreset and account activation. It works with\n`custom user model <https://docs.djangoproject.com/en/dev/topics/auth/customizing/>`_.\n\nInstead of reusing Django code (e.g. ``PasswordResetForm``), we reimplemented\nfew things to fit better into `Single Page App <https://en.wikipedia.org/wiki/Single-page_application>`_\narchitecture.\n\nDeveloped by `SUNSCRAPERS <http://sunscrapers.com/>`_ with passion & patience.\n\n.. image:: https://asciinema.org/a/94J4eG2tSBD2iEfF30a6vGtXw.png\n  :target: https://asciinema.org/a/94J4eG2tSBD2iEfF30a6vGtXw\n\nRequirements\n============\n\nTo be able to run **djoser** you have to meet following requirements:\n\n- Python (3.6, 3.7, 3.8, 3.9)\n- Django (2.2, 3.1)\n- Django REST Framework 3.11.1\n\nIf you need to support other versions, please use djoser<2.\n\nInstallation\n============\n\nSimply install using ``pip``:\n\n.. code-block:: bash\n\n    $ pip install djoser\n\nAnd continue with the steps described at\n`configuration <https://djoser.readthedocs.io/en/latest/getting_started.html#configuration>`_\nguide.\n\nDocumentation\n=============\n\nDocumentation is available to study at\n`https://djoser.readthedocs.io <https://djoser.readthedocs.io>`_\nand in ``docs`` directory.\n\nContributing and development\n============================\n\nTo start developing on **djoser**, clone the repository:\n\n.. code-block:: bash\n\n    $ git clone git@github.com:sunscrapers/djoser.git\n\nWe use `poetry <https://python-poetry.org/>`_ as dependency management and packaging tool.\n\n.. code-block:: bash\n\n    $ cd djoser\n    $ poetry install -E test\n\nThis will create a virtualenv with all development dependencies.\n\nTo run the test just type:\n\n.. code-block:: bash\n\n    $ poetry run py.test testproject\n\nWe also preapred a convenient ``Makefile`` to automate commands above:\n\n.. code-block:: bash\n\n    $ make init\n    $ make test\n\nTo activate the virtual environment run\n\n.. code-block:: bash\n\n    $ poetry shell\n\nWithout poetry\n--------------\n\nNew versions of ``pip`` can use ``pyproject.toml`` to build the package and install its dependencies.\n\n.. code-block:: bash\n\n    $ pip install .[test]\n\n.. code-block:: bash\n\n    $ cd testproject\n    $ ./manage.py test\n\nTox\n---\n\nIf you need to run tests against all supported Python and Django versions then invoke:\n\n.. code-block:: bash\n\n    $ poetry run tox -p all\n\nExample project\n---------------\n\nYou can also play with test project by running following commands:\n\n.. code-block:: bash\n\n    $ make migrate\n    $ make runserver\n\nCommiting your code\n-------------------\n\nBefore sending patches please make sure you have `pre-commit <https://pre-commit.com/>`_ activated in your local git repository:\n\n.. code-block:: bash\n\n    $ pre-commit install\n\nThis will ensure that your code is cleaned before you commit it.\nSome steps (like black) automatically fix issues but the show their status as FAILED.\nJust inspect if eveything is OK, git-add the files and retry the commit.\nOther tools (like flake8) require you to manually fix the issues.\n\n\nSimilar projects\n================\n\nList of projects related to Django, REST and authentication:\n\n- `django-rest-framework-simplejwt <https://github.com/davesque/django-rest-framework-simplejwt>`_\n- `django-oauth-toolkit <https://github.com/evonove/django-oauth-toolkit>`_\n- `django-rest-auth <https://github.com/Tivix/django-rest-auth>`_ (not maintained)\n- `django-rest-framework-digestauth <https://github.com/juanriaza/django-rest-framework-digestauth>`_ (not maintained)\n\nPlease, keep in mind that while using custom authentication and TokenCreateSerializer\nvalidation, there is a path that **ignores intentional return of None** from authenticate()\nand try to find User using parameters. Probably, that will be changed in the future.\n',
    'author': 'Sunscrapers',
    'author_email': 'info@sunscrapers.com',
    'maintainer': 'Tomasz Wójcik',
    'maintainer_email': 't.wojcik@sunscrapers.com',
    'url': 'https://github.com/sunscrapers/djoser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
