# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bareasgi',
 'bareasgi.basic_router',
 'bareasgi.http',
 'bareasgi.lifespan',
 'bareasgi.middlewares',
 'bareasgi.websockets']

package_data = \
{'': ['*']}

install_requires = \
['bareutils>=4.0.0,<5.0.0', 'jetblack-asgi-typing>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'bareasgi',
    'version': '4.0.1',
    'description': 'A lightweight ASGI framework',
    'long_description': "# bareASGI\n\nA lightweight Python [ASGI](user-guide/asgi) web server framework\n(read the [docs](https://rob-blackbourn.github.io/bareASGI/)).\n\n## Overview\n\nThis is a _bare_ ASGI web server framework. The goal is to provide\na minimal implementation, with other facilities (serving static files, CORS,\nsessions, etc.) being implemented by optional packages.\n\nThe framework is targeted at micro-services which require a light footprint, or\nas a base for larger frameworks.\n\nPython 3.8+ is required.\n\n## Optional Packages\n\n- [bareASGI-cors](https://github.com/rob-blackbourn/bareASGI-cors) for cross origin resource sharing,\n- [bareASGI-static](https://github.com/rob-blackbourn/bareASGI-static) for serving static files,\n- [bareASGI-jinja2](https://github.com/rob-blackbourn/bareASGI-jinja2) for [Jinja2](https://github.com/pallets/jinja) template rendering,\n- [bareASGI-graphql-next](https://github.com/rob-blackbourn/bareASGI-graphql-next) for [GraphQL](https://github.com/graphql-python/graphql-core) and [grapehene](https://github.com/graphql-python/graphene),\n- [bareASGI-rest](https://github.com/rob-blackbourn/bareASGI-rest) for REST support,\n- [bareASGI-prometheus](https://github.com/rob-blackbourn/bareASGI-prometheus) for [prometheus](https://prometheus.io/) metrics,\n- [bareASGI-session](https://github.com/rob-blackbourn/bareASGI-session) for sessions.\n\n## Functionality\n\nWhile lightweight, the framework contains all the functionality required for\ndeveloping sophisticated web applications including:\n\n- Http (1.0, 1.1, 2, 3),\n- WebSockets,\n- A method and path based router,\n- Middleware,\n- Http 2 push,\n- Streaming requests and responses.\n\n## Simple Server\n\nHere is a simple server with a request handler that returns some text.\n\n```python\nimport uvicorn\nfrom bareasgi import Application, text_writer\n\nasync def http_request_callback(request):\n    return HttpResponse(200, [(b'content-type', b'text/plain')], text_writer('This is not a test'))\n\napp = Application()\napp.http_router.add({'GET'}, '/', http_request_callback)\n\nuvicorn.run(app, port=9009)\n```\n",
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareasgi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
