# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_spec', 'test', 'test.test_formats', 'test.test_results']

package_data = \
{'': ['*']}

install_requires = \
['six']

entry_points = \
{'pytest11': ['pytest_spec = pytest_spec.plugin']}

setup_kwargs = {
    'name': 'pytest-spec',
    'version': '3.2.0',
    'description': 'Library pytest-spec is a pytest plugin to display test execution output like a SPECIFICATION.',
    'long_description': '<p>\n    <h1 align="center">pytest-spec</h1>\n    <p align="center">\n        <img src="https://badgen.net/badge/python/2.7/green">\n        <img src="https://badgen.net/badge/python/3.5/green">\n        <img src="https://badgen.net/badge/python/3.6/green">\n        <img src="https://badgen.net/badge/python/3.7/green">\n        <img src="https://badgen.net/badge/python/3.8/green">\n        <img src="https://badgen.net/badge/python/3.9/green">\n    </p>\n    <p align="center">\n        <img src="https://badgen.net/badge/os/linux/blue">\n        <img src="https://badgen.net/badge/os/windows/blue">\n        <img src="https://badgen.net/badge/os/macos/blue">\n    </p>\n    <p align="center">\n        <img src="https://badgen.net/badge/pytest/3.9.3/purple">\n        <img src="https://badgen.net/badge/pytest/4.6.11/purple">\n        <img src="https://badgen.net/badge/pytest/5.4.3/purple">\n        <img src="https://badgen.net/badge/pytest/6.1.2/purple">\n    </p>\n    <p align="center">\n        Library pytest-spec is a pytest plugin to display test execution output like a SPECIFICATION.\n    </p>\n</p>\n\n\n## Available features\n\n* Format output to look like specification.\n* Group tests by classes and files\n* Failed, passed and skipped are marked and colored.\n* Remove test\\_ and underscores for every test.\n* It is possible to use docstring summary instead of test name.\n* Supports function based, class based test.\n* Supports describe like tests.\n\n\n## Output example\n\n![Example](https://github.com/pchomik/pytest-spec/raw/master/docs/output.gif)\n\n\n## Configuration\n\n### spec_header_format\n\nYou can configure the format of the test headers by specifying a [format string](https://docs.python.org/2/library/string.html#format-string-syntax) in your [ini-file](http://doc.pytest.org/en/latest/customize.html#inifiles):\n\n```ini\n    [tool:pytest]\n    spec_header_format = {module_path}:\n```\n\nIn addition to the ``{path}`` and ``{class_name}`` replacement fields, there is also ``{test_case}`` that holds a more human readable name.\n\n### spec_test_format\n\nYou can configure the format of the test results by specifying a [format string](https://docs.python.org/2/library/string.html#format-string-syntax) in your [ini-file](http://doc.pytest.org/en/latest/customize.html#inifiles):\n\n3 variables are available:\n* result - place for indicator\n* name - name of test\n* docstring_summary - first line from test docstring if available\n\n```ini\n    [tool:pytest]\n    spec_test_format = {result} {name}\n```\n\nor\n\n```ini\n    [tool:pytest]\n    spec_test_format = {result} {docstring_summary}\n```\n\nIn second example where docstring is not available the name will be added to spec output.\n\n### spec_success_indicator\n\nYou can configure the indicator displayed when test passed.\n\n```ini\n    [tool:pytest]\n    spec_success_indicator = ✓\n```\n\n### spec_failure_indicator\n\nYou can configure the indicator displated when test failed.\n\n```ini\n    [tool:pytest]\n    spec_failure_indicator = ✗\n```\n\n### spec_skipped_indicator\n\nYou can configure the indicator displated when test is skipped.\n\n```ini\n    [tool:pytest]\n    spec_skipped_indicator = ?\n```\n\n### spec_ignore\n\nComma-separated settings to ignore/hide some tests or output from from plugins like FLAKE8 or ISORT.\nAny test which contain provided string will be ignored in output spec.\n\n```ini\n    [tool:pytest]\n    spec_ignore = FLAKE8\n```\n\n### spec_indent\n\n```ini\n    [tool:pytest]\n    spec_indent = "   "\n```\n\n## Continuous Integration\n\n[![Tests](https://github.com/pchomik/pytest-spec/workflows/test/badge.svg)](https://github.com/pchomik/pytest-spec/actions)\n\n\n## Download\n\nAll versions of library are available on official [pypi server](https://pypi.org/project/pytest-spec/#history).\n\n## Install\n\n```sh\n    pip install pytest-spec\n```\n\n## Contribution\n\nPlease feel free to present your idea by code example (pull request) or reported issues.\n\n## Contributors\n\n* [@0x64746b](https://github.com/0x64746b)\n* [@lucasmarshall](https://github.com/lucasmarshall)\n* [@amcgregor](https://github.com/amcgregor)\n* [@jhermann](https://github.com/jhermann)\n* [@frenzymadness](https://github.com/frenzymadness)\n* [@chrischambers](https://github.com/chrischambers)\n* [@maxalbert](https://github.com/maxalbert)\n* [@jayvdb](https://github.com/jayvdb)\n\n## License\n\npytest-spec - pytest plugin to display test execution output like a SPECIFICATION.\n\nCopyright (C) 2014-2021 Pawel Chomicki\n\nThis program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n',
    'author': 'Pawel Chomicki',
    'author_email': 'pawel.chomicki@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pchomik/pytest-spec',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
}


setup(**setup_kwargs)
