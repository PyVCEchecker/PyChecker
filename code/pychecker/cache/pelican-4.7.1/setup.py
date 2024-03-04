# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican',
 'pelican.plugins',
 'pelican.tests',
 'pelican.tests.dummy_plugins.namespace_plugin.pelican.plugins.ns_plugin',
 'pelican.tests.dummy_plugins.normal_plugin.normal_plugin',
 'pelican.tests.dummy_plugins.normal_plugin.normal_submodule_plugin',
 'pelican.tests.dummy_plugins.normal_plugin.normal_submodule_plugin.subpackage',
 'pelican.tools']

package_data = \
{'': ['*'],
 'pelican': ['themes/notmyidea/static/css/*',
             'themes/notmyidea/static/fonts/*',
             'themes/notmyidea/static/images/icons/*',
             'themes/notmyidea/templates/*',
             'themes/simple/templates/*'],
 'pelican.tests': ['TestPages/*',
                   'content/*',
                   'content/TestCategory/*',
                   'cyclic_intersite_links/*',
                   'mixed_content/*',
                   'mixed_content/subdir/*',
                   'nested_content/maindir/*',
                   'nested_content/maindir/subdir/*',
                   'output/basic/*',
                   'output/basic/author/*',
                   'output/basic/category/*',
                   'output/basic/drafts/*',
                   'output/basic/feeds/*',
                   'output/basic/override/*',
                   'output/basic/pages/*',
                   'output/basic/pictures/*',
                   'output/basic/tag/*',
                   'output/basic/theme/css/*',
                   'output/basic/theme/fonts/*',
                   'output/basic/theme/images/icons/*',
                   'output/custom/*',
                   'output/custom/author/*',
                   'output/custom/category/*',
                   'output/custom/drafts/*',
                   'output/custom/feeds/*',
                   'output/custom/override/*',
                   'output/custom/pages/*',
                   'output/custom/pictures/*',
                   'output/custom/tag/*',
                   'output/custom/theme/css/*',
                   'output/custom/theme/fonts/*',
                   'output/custom/theme/images/icons/*',
                   'output/custom_locale/*',
                   'output/custom_locale/author/*',
                   'output/custom_locale/category/*',
                   'output/custom_locale/drafts/*',
                   'output/custom_locale/feeds/*',
                   'output/custom_locale/override/*',
                   'output/custom_locale/pages/*',
                   'output/custom_locale/pictures/*',
                   'output/custom_locale/posts/2010/décembre/02/this-is-a-super-article/*',
                   'output/custom_locale/posts/2010/octobre/15/unbelievable/*',
                   'output/custom_locale/posts/2010/octobre/20/oh-yeah/*',
                   'output/custom_locale/posts/2011/avril/20/a-markdown-powered-article/*',
                   'output/custom_locale/posts/2011/février/17/article-1/*',
                   'output/custom_locale/posts/2011/février/17/article-2/*',
                   'output/custom_locale/posts/2011/février/17/article-3/*',
                   'output/custom_locale/posts/2012/février/29/second-article/*',
                   'output/custom_locale/posts/2012/novembre/30/filename_metadata-example/*',
                   'output/custom_locale/tag/*',
                   'output/custom_locale/theme/css/*',
                   'output/custom_locale/theme/fonts/*',
                   'output/custom_locale/theme/images/icons/*',
                   'parse_error/*',
                   'theme_overrides/level1/*',
                   'theme_overrides/level2/*'],
 'pelican.tools': ['templates/*']}

install_requires = \
['blinker>=1.4',
 'docutils>=0.16',
 'feedgenerator>=1.9',
 'jinja2>=2.7',
 'pygments>=2.6',
 'python-dateutil>=2.8',
 'pytz>=2020.1',
 'rich>=10.1',
 'unidecode>=1.1']

extras_require = \
{'markdown': ['markdown>=3.1']}

entry_points = \
{'console_scripts': ['pelican = pelican.__main__:main',
                     'pelican-import = pelican.tools.pelican_import:main',
                     'pelican-plugins = pelican.plugins._utils:list_plugins',
                     'pelican-quickstart = '
                     'pelican.tools.pelican_quickstart:main',
                     'pelican-themes = pelican.tools.pelican_themes:main']}

setup_kwargs = {
    'name': 'pelican',
    'version': '4.7.1',
    'description': 'Static site generator supporting Markdown and reStructuredText',
    'long_description': "Pelican |build-status| |pypi-version| |repology|\n================================================\n\nPelican is a static site generator, written in Python_.\n\n* Compose content in Markdown_ or reStructuredText_ using your editor of choice\n* Simple command-line tool (re)generates HTML, CSS, and JS from your source content\n* Easy to interface with version control systems and web hooks\n* Completely static output is simple to host anywhere\n\n\nFeatures\n--------\n\nPelican’s feature highlights include:\n\n* Chronological content (e.g., articles, blog posts) as well as static pages\n* Integration with external services\n* Site themes (created using Jinja2_ templates)\n* Publication of articles in multiple languages\n* Generation of Atom and RSS feeds\n* Code syntax highlighting via Pygments_\n* Import existing content from WordPress, Dotclear, or RSS feeds\n* Fast rebuild times due to content caching and selective output writing\n* Extensible via a rich plugin ecosystem: `Pelican Plugins`_\n\nCheck out the `Pelican documentation`_ for further information.\n\n\nHow to get help, contribute, or provide feedback\n------------------------------------------------\n\nSee our `contribution submission and feedback guidelines <CONTRIBUTING.rst>`_.\n\n\nSource code\n-----------\n\nPelican’s source code is `hosted on GitHub`_. For information on how it works,\nhave a look at `Pelican's internals`_.\n\n\nWhy the name “Pelican”?\n-----------------------\n\n“Pelican” is an anagram of *calepin*, which means “notebook” in French.\n\n\n.. Links\n\n.. _Python: https://www.python.org/\n.. _reStructuredText: http://docutils.sourceforge.net/rst.html\n.. _Markdown: https://daringfireball.net/projects/markdown/\n.. _Jinja2: https://palletsprojects.com/p/jinja/\n.. _Pygments: https://pygments.org/\n.. _`Pelican Plugins`: https://github.com/pelican-plugins\n.. _`Pelican documentation`: https://docs.getpelican.com/\n.. _`Pelican's internals`: https://docs.getpelican.com/en/latest/internals.html\n.. _`hosted on GitHub`: https://github.com/getpelican/pelican\n\n.. |build-status| image:: https://img.shields.io/github/workflow/status/getpelican/pelican/build\n   :target: https://github.com/getpelican/pelican/actions\n   :alt: GitHub Actions CI: continuous integration status\n.. |pypi-version| image:: https://img.shields.io/pypi/v/pelican.svg\n   :target: https://pypi.org/project/pelican/\n   :alt: PyPI: the Python Package Index\n.. |repology| image:: https://repology.org/badge/tiny-repos/pelican.svg\n   :target: https://repology.org/project/pelican/versions\n   :alt: Repology: the packaging hub\n",
    'author': 'Justin Mayer',
    'author_email': 'entrop@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://getpelican.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
