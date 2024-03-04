# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry',
 'poetry.config',
 'poetry.console',
 'poetry.console.args',
 'poetry.console.commands',
 'poetry.console.commands.cache',
 'poetry.console.commands.debug',
 'poetry.console.commands.env',
 'poetry.console.commands.self',
 'poetry.console.config',
 'poetry.console.logging',
 'poetry.console.logging.formatters',
 'poetry.inspection',
 'poetry.installation',
 'poetry.installation.operations',
 'poetry.io',
 'poetry.json',
 'poetry.layouts',
 'poetry.masonry',
 'poetry.masonry.builders',
 'poetry.mixology',
 'poetry.mixology.solutions',
 'poetry.mixology.solutions.providers',
 'poetry.mixology.solutions.solutions',
 'poetry.packages',
 'poetry.publishing',
 'poetry.puzzle',
 'poetry.repositories',
 'poetry.utils',
 'poetry.version']

package_data = \
{'': ['*'], 'poetry': ['_vendor/*'], 'poetry.json': ['schemas/*']}

install_requires = \
['cachecontrol[filecache]>=0.12.4,<0.13.0',
 'cachy>=0.3.0,<0.4.0',
 'cleo>=0.8.1,<0.9.0',
 'clikit>=0.6.2,<0.7.0',
 'html5lib>=1.0,<2.0',
 'packaging>=20.4,<21.0',
 'pexpect>=4.7.0,<5.0.0',
 'pkginfo>=1.4,<2.0',
 'poetry-core>=1.0.0,<2.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.18,<3.0',
 'shellingham>=1.1,<2.0',
 'tomlkit>=0.7.0,<1.0.0',
 'virtualenv>=20.0.26,<21.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.6.0,<2.0.0'],
 ':python_version >= "2.7" and python_version < "2.8"': ['typing>=3.6,<4.0',
                                                         'pathlib2>=2.3,<3.0',
                                                         'futures>=3.3.0,<4.0.0',
                                                         'glob2>=0.6,<0.7',
                                                         'functools32>=3.2.3,<4.0.0',
                                                         'keyring>=18.0.1,<19.0.0',
                                                         'subprocess32>=3.5,<4.0'],
 ':python_version >= "3.5" and python_version < "3.6"': ['keyring>=20.0.1,<21.0.0'],
 ':python_version >= "3.6" and python_version < "4.0"': ['crashtest>=0.3.0,<0.4.0',
                                                         'keyring>=21.2.0,<22.0.0']}

entry_points = \
{'console_scripts': ['poetry = poetry.console:main']}

setup_kwargs = {
    'name': 'poetry',
    'version': '1.1.4',
    'description': 'Python dependency management and packaging made easy.',
    'long_description': '# Poetry: Dependency Management for Python\n\nPoetry helps you declare, manage and install dependencies of Python projects,\nensuring you have the right stack everywhere.\n\n![Poetry Install](https://raw.githubusercontent.com/python-poetry/poetry/master/assets/install.gif)\n\nIt supports Python 2.7 and 3.5+.\n\n**Note**: Python 2.7 and 3.5 will no longer be supported in the next feature release (1.2).\nYou should consider updating your Python version to a supported one.\n\n[![Tests Status](https://github.com/python-poetry/poetry/workflows/Tests/badge.svg?branch=master&event=push)](https://github.com/python-poetry/poetry/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush)\n\nThe [complete documentation](https://python-poetry.org/docs/) is available on the [official website](https://python-poetry.org).\n\n## Installation\n\nPoetry provides a custom installer that will install `poetry` isolated\nfrom the rest of your system by vendorizing its dependencies. This is the\nrecommended way of installing `poetry`.\n\n```bash\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python\n```\n\nAlternatively, you can download the `get-poetry.py` file and execute it separately.\n\nThe setup script must be able to find one of following executables in your shell\'s path environment:\n\n- `python` (which can be a py3 or py2 interpreter)\n- `python3`\n- `py.exe -3` (Windows)\n- `py.exe -2` (Windows)\n\nIf you want to install prerelease versions, you can do so by passing `--preview` to `get-poetry.py`:\n\n```bash\npython get-poetry.py --preview\n```\n\nSimilarly, if you want to install a specific version, you can use `--version`:\n\n```bash\npython get-poetry.py --version 0.7.0\n```\n\nUsing `pip` to install `poetry` is also possible.\n\n```bash\npip install --user poetry\n```\n\nBe aware, however, that it will also install poetry\'s dependencies\nwhich might cause conflicts.\n\n## Updating `poetry`\n\nUpdating poetry to the latest stable version is as simple as calling the `self update` command.\n\n```bash\npoetry self update\n```\n\nIf you want to install prerelease versions, you can use the `--preview` option.\n\n```bash\npoetry self update --preview\n```\n\nAnd finally, if you want to install a specific version you can pass it as an argument\nto `self update`.\n\n```bash\npoetry self update 1.0.0\n```\n\n*Note:*\n\n    If you are still on poetry version < 1.0 use `poetry self:update` instead.\n\n\n## Enable tab completion for Bash, Fish, or Zsh\n\n`poetry` supports generating completion scripts for Bash, Fish, and Zsh.\nSee `poetry help completions` for full details, but the gist is as simple as using one of the following:\n\n```bash\n# Bash\npoetry completions bash > /etc/bash_completion.d/poetry.bash-completion\n\n# Bash (Homebrew)\npoetry completions bash > $(brew --prefix)/etc/bash_completion.d/poetry.bash-completion\n\n# Fish\npoetry completions fish > ~/.config/fish/completions/poetry.fish\n\n# Fish (Homebrew)\npoetry completions fish > (brew --prefix)/share/fish/vendor_completions.d/poetry.fish\n\n# Zsh\npoetry completions zsh > ~/.zfunc/_poetry\n\n# Zsh (Homebrew)\npoetry completions zsh > $(brew --prefix)/share/zsh/site-functions/_poetry\n\n# Zsh (Oh-My-Zsh)\nmkdir $ZSH_CUSTOM/plugins/poetry\npoetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry\n\n# Zsh (prezto)\npoetry completions zsh > ~/.zprezto/modules/completion/external/src/_poetry\n```\n\n*Note:* you may need to restart your shell in order for the changes to take\neffect.\n\nFor `zsh`, you must then add the following line in your `~/.zshrc` before\n`compinit` (not for homebrew setup):\n\n```zsh\nfpath+=~/.zfunc\n```\n\n\n## Introduction\n\n`poetry` is a tool to handle dependency installation as well as building and packaging of Python packages.\nIt only needs one file to do all of that: the new, [standardized](https://www.python.org/dev/peps/pep-0518/) `pyproject.toml`.\n\nIn other words, poetry uses `pyproject.toml` to replace `setup.py`, `requirements.txt`, `setup.cfg`, `MANIFEST.in` and the newly added `Pipfile`.\n\n```toml\n[tool.poetry]\nname = "my-package"\nversion = "0.1.0"\ndescription = "The description of the package"\n\nlicense = "MIT"\n\nauthors = [\n    "Sébastien Eustace <sebastien@eustace.io>"\n]\n\nreadme = \'README.md\'  # Markdown files are supported\n\nrepository = "https://github.com/python-poetry/poetry"\nhomepage = "https://github.com/python-poetry/poetry"\n\nkeywords = [\'packaging\', \'poetry\']\n\n[tool.poetry.dependencies]\npython = "~2.7 || ^3.2"  # Compatible python versions must be declared here\ntoml = "^0.9"\n# Dependencies with extras\nrequests = { version = "^2.13", extras = [ "security" ] }\n# Python specific dependencies with prereleases allowed\npathlib2 = { version = "^2.2", python = "~2.7", allow-prereleases = true }\n# Git dependencies\ncleo = { git = "https://github.com/sdispater/cleo.git", branch = "master" }\n\n# Optional dependencies (extras)\npendulum = { version = "^1.4", optional = true }\n\n[tool.poetry.dev-dependencies]\npytest = "^3.0"\npytest-cov = "^2.4"\n\n[tool.poetry.scripts]\nmy-script = \'my_package:main\'\n```\n\nThere are some things we can notice here:\n\n* It will try to enforce [semantic versioning](<http://semver.org>) as the best practice in version naming.\n* You can specify the readme, included and excluded files: no more `MANIFEST.in`.\n`poetry` will also use VCS ignore files (like `.gitignore`) to populate the `exclude` section.\n* Keywords (up to 5) can be specified and will act as tags on the packaging site.\n* The dependencies sections support caret, tilde, wildcard, inequality and multiple requirements.\n* You must specify the python versions for which your package is compatible.\n\n`poetry` will also detect if you are inside a virtualenv and install the packages accordingly.\nSo, `poetry` can be installed globally and used everywhere.\n\n`poetry` also comes with a full fledged dependency resolution library.\n\n## Why?\n\nPackaging systems and dependency management in Python are rather convoluted and hard to understand for newcomers.\nEven for seasoned developers it might be cumbersome at times to create all files needed in a Python project: `setup.py`,\n`requirements.txt`, `setup.cfg`, `MANIFEST.in` and the newly added `Pipfile`.\n\nSo I wanted a tool that would limit everything to a single configuration file to do:\ndependency management, packaging and publishing.\n\nIt takes inspiration in tools that exist in other languages, like `composer` (PHP) or `cargo` (Rust).\n\nAnd, finally, there is no reliable tool to properly resolve dependencies in Python, so I started `poetry`\nto bring an exhaustive dependency resolver to the Python community.\n\n### What about Pipenv?\n\nIn short: I do not like the CLI it provides, or some of the decisions made,\nand I think we can make a better and more intuitive one. Here are a few things\nthat I don\'t like.\n\n#### Dependency resolution\n\nThe dependency resolution is erratic and will fail even if there is a solution. Let\'s take an example:\n\n```bash\npipenv install oslo.utils==1.4.0\n```\n\nwill fail with this error:\n\n```text\nCould not find a version that matches pbr!=0.7,!=2.1.0,<1.0,>=0.6,>=2.0.0\n```\n\nwhile Poetry will get you the right set of packages:\n\n```bash\npoetry add oslo.utils=1.4.0\n```\n\nresults in :\n\n```text\n  - Installing pytz (2018.3)\n  - Installing netifaces (0.10.6)\n  - Installing netaddr (0.7.19)\n  - Installing oslo.i18n (2.1.0)\n  - Installing iso8601 (0.1.12)\n  - Installing six (1.11.0)\n  - Installing babel (2.5.3)\n  - Installing pbr (0.11.1)\n  - Installing oslo.utils (1.4.0)\n```\n\nThis is possible thanks to the efficient dependency resolver at the heart of Poetry.\n\nHere is a breakdown of what exactly happens here:\n\n`oslo.utils (1.4.0)` depends on:\n\n- `pbr (>=0.6,!=0.7,<1.0)`\n- `Babel (>=1.3)`\n- `six (>=1.9.0)`\n- `iso8601 (>=0.1.9)`\n- `oslo.i18n (>=1.3.0)`\n- `netaddr (>=0.7.12)`\n- `netifaces (>=0.10.4)`\n\nWhat interests us is `pbr (>=0.6,!=0.7,<1.0)`.\n\nAt this point, poetry will choose `pbr==0.11.1` which is the latest version that matches the constraint.\n\nNext it will try to select `oslo.i18n==3.20.0` which is the latest version that matches `oslo.i18n (>=1.3.0)`.\n\nHowever this version requires `pbr (!=2.1.0,>=2.0.0)` which is incompatible with `pbr==0.11.1`,\nso `poetry` will try to find a version of `oslo.i18n` that satisfies `pbr (>=0.6,!=0.7,<1.0)`.\n\nBy analyzing the releases of `oslo.i18n`, it will find `oslo.i18n==2.1.0` which requires `pbr (>=0.11,<2.0)`.\nAt this point the rest of the resolution is straightforward since there is no more conflict.\n\n## Resources\n\n* [Official Website](https://python-poetry.org)\n* [Issue Tracker](https://github.com/python-poetry/poetry/issues)\n* [Discord](https://discordapp.com/invite/awxPgve)\n',
    'author': 'Sébastien Eustace',
    'author_email': 'sebastien@eustace.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://python-poetry.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
