# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vega', 'vega.tests']

package_data = \
{'': ['*'], 'vega': ['static/*']}

install_requires = \
['jupyter>=1.0.0,<2.0.0', 'pandas>=1.0.0,<2.0.0']

entry_points = \
{'altair.vega.v5.renderer': ['notebook = vega.vega:entry_point_renderer'],
 'altair.vegalite.v4.renderer': ['notebook = '
                                 'vega.vegalite:entry_point_renderer']}

setup_kwargs = {
    'name': 'vega',
    'version': '3.5.0',
    'description': 'A Jupyter widget for Vega 5 and Vega-Lite 4',
    'long_description': 'IPython Vega\n============\n\nIPython/Jupyter notebook module for `Vega <https://github.com/vega/vega/>`_\nand `Vega-Lite <https://github.com/vega/vega-lite/>`_.\nNotebooks with embedded visualizations can be viewed on GitHub and nbviewer.\n\nFor more information, see https://github.com/vega/ipyvega.\n\nInstallation Notes\n------------------\nWhen installing from PyPI, extra steps may be required to enable the Jupyter\nnotebook extension. For more information, see the\n`github page <https://github.com/vega/ipyvega>`_.\n',
    'author': 'Dominik Moritz',
    'author_email': 'domoritz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vega/ipyvega',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1',
}


setup(**setup_kwargs)
