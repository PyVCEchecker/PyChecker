# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aldjemy']

package_data = \
{'': ['*']}

install_requires = \
['Django>=2.2', 'SQLAlchemy>=1.4']

setup_kwargs = {
    'name': 'aldjemy',
    'version': '2.5',
    'description': 'SQLAlchemy for your Django models',
    'long_description': '=======\nAldjemy\n=======\n\n.. image:: https://raw.githubusercontent.com/aldjemy/aldjemy/main/logo.png\n   :alt: Aldjemy Logo\n\n|pypi_version| |pypi_license| |ci-tests|\n\n\nAldjemy integrates SQLAlchemy into an existing Django project,\nto help you build complex queries that are difficult for the Django ORM.\n\nWhile other libraries use SQLAlchemy reflection to generate SQLAlchemy models,\nAldjemy generates the SQLAlchemy models by introspecting the Django models.\nThis allows you to better control what properties in a table are being accessed.\n\n\nInstallation\n------------\n\nAdd ``aldjemy`` to your ``INSTALLED_APPS``.\nAldjemy will automatically add an ``sa`` attribute to all models,\nwhich is an SQLAlchemy ``Model``.\n\nExample:\n\n.. code-block:: python\n\n    User.sa.query().filter(User.sa.username==\'Brubeck\')\n    User.sa.query().join(User.sa.groups).filter(Group.sa.name=="GROUP_NAME")\n\nExplicit joins are part of the SQLAlchemy philosophy,\nso don\'t expect Aldjemy to be a Django ORM drop-in replacement.\nInstead, you should use Aldjemy to help with special situations.\n\n\nSettings\n--------\n\nYou can add your own field types to map django types to sqlalchemy ones with\n``ALDJEMY_DATA_TYPES`` settings parameter.\nParameter must be a ``dict``, key is result of ``field.get_internal_type()``,\nvalue must be a one arg function. You can get idea from ``aldjemy.table``.\n\nAlso it is possible to extend/override list of supported SQLALCHEMY engines\nusing ``ALDJEMY_ENGINES`` settings parameter.\nParameter should be a ``dict``, key is substring after last dot from\nDjango database engine setting (e.g. ``sqlite3`` from ``django.db.backends.sqlite3``),\nvalue is SQLAlchemy driver which will be used for connection (e.g. ``sqlite``, ``sqlite+pysqlite``).\nIt could be helpful if you want to use ``django-postgrespool``.\n\n\nMixins\n------\n\nOften django models have helper function and properties that helps to\nrepresent the model\'s data (`__str__`), or represent some model based logic.\n\nTo integrate it with aldjemy models you can put these methods into a separate mixin:\n\n.. code-block:: python\n\n    class TaskMixin:\n        def __str__(self):\n            return self.code\n\n    class Task(TaskMixin, models.Model):\n        aldjemy_mixin = TaskMixin\n        code = models.CharField(_(\'code\'), max_length=32, unique=True)\n\nVoilà! You can use ``__str__`` on aldjemy classes, because this mixin will be\nmixed into generated aldjemy model.\n\nIf you want to expose all methods and properties without creating a\nseparate mixin class, you can use the `aldjemy.meta.AldjemyMeta`\nmetaclass:\n\n.. code-block:: python\n\n    class Task(models.Model, metaclass=AldjemyMeta):\n        code = models.CharField(_(\'code\'), max_length=32, unique=True)\n\n        def __str__(self):\n            return self.code\n\nThe result is same as with the example above, only you didn\'t need to\ncreate the mixin class at all.\n\nRelease Process\n\n---------------\n\n 1. Make a Pull Request with updated changelog and bumped version of the project\n\n    .. code-block:: bash\n\n       poetry version (major|minor|patch) # choose which version to bump\n\n 2. Once the pull request is merged, create a github release with the same version, on the web console or with github cli.\n\n    .. code-block:: bash\n\n       gh release create\n\n 3. Enjoy!\n\n.. |pypi_version| image:: https://img.shields.io/pypi/v/aldjemy.svg?style=flat-square\n    :target: https://pypi.python.org/pypi/aldjemy\n    :alt: Downloads\n\n.. |pypi_license| image:: https://img.shields.io/pypi/l/aldjemy.svg?style=flat-square\n    :target: https://pypi.python.org/pypi/aldjemy\n    :alt: License\n\n.. |ci-tests| image:: https://github.com/aldjemy/aldjemy/actions/workflows/build.yml/badge.svg\n   :target: https://github.com/aldjemy/aldjemy/actions/workflows/build.yml\n   :alt: Continuous Integration results\n',
    'author': 'Mikhail Krivushin',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aldjemy/aldjemy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
