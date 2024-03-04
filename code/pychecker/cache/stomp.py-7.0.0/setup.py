# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stomp', 'stomp.adapter']

package_data = \
{'': ['*']}

install_requires = \
['docopt>=0.6.2,<0.7.0']

entry_points = \
{'console_scripts': ['stomp = stomp.__main__:main']}

setup_kwargs = {
    'name': 'stomp.py',
    'version': '7.0.0',
    'description': 'Python STOMP client, supporting versions 1.0, 1.1 and 1.2 of the protocol',
    'long_description': '========\nstomp.py\n========\n\n.. image:: https://badge.fury.io/py/stomp.py.svg\n    :target: https://badge.fury.io/py/stomp.py\n    :alt: PyPI version\n\n.. image:: https://travis-ci.org/jasonrbriggs/stomp.py.svg\n    :target: https://travis-ci.org/jasonrbriggs/stomp.py\n    :alt: Build Status\n\n"stomp.py" is a Python client library for accessing messaging servers (such as ActiveMQ_, Artemis_ or RabbitMQ_) using the STOMP_ protocol (`STOMP v1.0`_, `STOMP v1.1`_ and `STOMP v1.2`_). It can also be run as a standalone, command-line client for testing.  NOTE: Stomp.py has officially ended support for Python2.x. See `python3statement.org`_ for more information. \n\n**If you find this project useful, why not** `buy me a coffee`_.\n\n.. contents:: \\ \n    :depth: 1\n\n\nQuick Start\n===========\n\nYou can connect to a message broker running on the local machine, and send a message using the following example.\n\n.. code-block:: python\n\n  import stomp\n\n  conn = stomp.Connection()\n  conn.connect(\'admin\', \'password\', wait=True)\n  conn.send(body=\' \'.join(sys.argv[1:]), destination=\'/queue/test\')\n  conn.disconnect()\n\n\nDocumentation and Resources\n===========================\n\n- `Main documentation`_\n- `API documentation`_ (see `stomp.github.io`_ for details on the STOMP protocol itself)\n- A basic example of using stomp.py with a message listener can be found in the `quick start`_ section of the main documentation\n- Description of the `command-line interface`_\n- `Travis`_ for continuous integration builds\n- Current `test coverage report`_\n- `PyPi stomp.py page`_\n\nThe current version of stomp.py supports:\n\n- Python 3.x (Python2 support ended as of Jan 2020)\n- STOMP version 1.0, 1.1 and 1.2\n\nThere is also legacy 3.1.7 version using the old 3-series code (see `3.1.7 on PyPi`_ and `3.1.7 on GitHub`_). This is no longer supported, but (at least as of 2018) there were still a couple of reports of this version still being used in the wild.\n\nNote: stomp.py now follows `semantic versioning`_:\n\n- MAJOR version for incompatible API changes,\n- MINOR version for functionality added in a backwards compatible manner, and\n- PATCH version for backwards compatible bug fixes.\n\n\n\nTesting\n=======\n\nstomp.py has been perfunctorily tested on:\n\n- Pivotal `RabbitMQ`_   (`test_rabbitmq.py <https://github.com/jasonrbriggs/stomp.py/blob/dev/tests/test_rabbitmq.py>`_)\n- Apache `ActiveMQ`_   (`test_activemq.py <https://github.com/jasonrbriggs/stomp.py/blob/dev/tests/test_activemq.py>`_)\n- Apache ActiveMQ `Artemis`_  (`test_artemis.py <https://github.com/jasonrbriggs/stomp.py/blob/dev/tests/test_artemis.py>`_)\n- `stompserver`_  (`test_stompserver.py <https://github.com/jasonrbriggs/stomp.py/blob/dev/tests/test_stompserver.py>`_)\n\nFor testing locally, you\'ll need to install docker. Once installed:\n\n#. Create the docker image:\n        make docker-image\n#. Run the container:\n        make run-docker\n#. Run stomp.py unit tests:\n        make test\n#. Cleanup the container afterwards if you don\'t need it any more:\n        make remove-docker\n\n\n.. _`STOMP`: http://stomp.github.io\n.. _`STOMP v1.0`: http://stomp.github.io/stomp-specification-1.0.html\n.. _`STOMP v1.1`: http://stomp.github.io/stomp-specification-1.1.html\n.. _`STOMP v1.2`: http://stomp.github.io/stomp-specification-1.2.html\n.. _`python3statement.org`: http://python3statement.org/\n\n.. _`Main documentation`: http://jasonrbriggs.github.io/stomp.py/index.html\n.. _`stomp.github.io`: http://stomp.github.io/\n.. _`quick start`: http://jasonrbriggs.github.io/stomp.py/quickstart.html\n.. _`command-line interface`: http://jasonrbriggs.github.io/stomp.py/commandline.html\n.. _`PyPi stomp.py page`: https://pypi.org/project/stomp.py/\n.. _`API documentation`: http://jasonrbriggs.github.io/stomp.py/api.html\n.. _`test coverage report`: http://jasonrbriggs.github.io/stomp.py/htmlcov/\n.. _`Travis`: https://travis-ci.org/jasonrbriggs/stomp.py\n\n.. _`3.1.7 on PyPi`: https://pypi.org/project/stomp.py/3.1.7/\n.. _`3.1.7 on GitHub`: https://github.com/jasonrbriggs/stomp.py/tree/stomppy-3series\n\n.. _`ActiveMQ`:  http://activemq.apache.org/\n.. _`Artemis`: https://activemq.apache.org/components/artemis/\n.. _`RabbitMQ`: http://www.rabbitmq.com\n.. _`stompserver`: http://stompserver.rubyforge.org\n\n.. _`buy me a coffee`: https://www.paypal.me/jasonrbriggs\n\n.. _`semantic versioning`: https://semver.org/\n',
    'author': 'Jason R Briggs',
    'author_email': 'jasonrbriggs@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jasonrbriggs/stomp.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
