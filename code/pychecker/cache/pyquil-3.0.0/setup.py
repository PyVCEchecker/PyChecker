# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyquil',
 'pyquil._parser',
 'pyquil.api',
 'pyquil.compatibility',
 'pyquil.compatibility.v2',
 'pyquil.compatibility.v2.api',
 'pyquil.experiment',
 'pyquil.external',
 'pyquil.latex',
 'pyquil.quantum_processor',
 'pyquil.quantum_processor.transformers',
 'pyquil.simulation']

package_data = \
{'': ['*']}

install_requires = \
['lark>=0.11.1,<0.12.0',
 'networkx>=2.5,<3.0',
 'numpy>=1.20,<2.0',
 'qcs-api-client>=0.8.0,<0.9.0',
 'retry>=0.9.2,<0.10.0',
 'rpcq>=3.6.0,<4.0.0',
 'scipy>=1.6.1,<2.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=3.7.3,<4.0.0'],
 'docs': ['Sphinx>=4.0.2,<5.0.0',
          'sphinx-rtd-theme>=0.5.2,<0.6.0',
          'nbsphinx>=0.8.6,<0.9.0',
          'recommonmark>=0.7.1,<0.8.0'],
 'latex': ['ipython>=7.21.0,<8.0.0']}

setup_kwargs = {
    'name': 'pyquil',
    'version': '3.0.0',
    'description': 'A Python library for creating Quantum Instruction Language (Quil) programs.',
    'long_description': 'PyQuil: Quantum programming in Python\n=====================================\n\n[![binder](https://mybinder.org/badge_logo.svg)][binder]\n[![docs][docs-badge]][docs-repo]\n[![coverage][coverage-badge]][coverage-repo]\n[![docker][docker-badge]][docker-repo]\n[![pepy][pepy-badge]][pepy-repo]\n[![pypi][pypi-badge]][pypi-repo]\n[![slack][slack-badge]][slack-invite]\n\nPyQuil is a Python library for quantum programming using [Quil](https://arxiv.org/abs/1608.03355),\nthe quantum instruction language developed at [Rigetti Computing](https://www.rigetti.com/).\nPyQuil serves three main functions:\n\n- Easily generating Quil programs from quantum gates and classical operations\n- Compiling and simulating Quil programs using the [Quil Compiler](https://github.com/rigetti/quilc)\n  (quilc) and the [Quantum Virtual Machine](https://github.com/rigetti/qvm) (QVM)\n- Executing Quil programs on real quantum processors (QPUs) using\n  [Quantum Cloud Services][qcs-paper] (QCS)\n\nPyQuil has a ton of other features, which you can learn more about in the\n[docs](http://pyquil.readthedocs.io/en/latest/). However, you can also keep reading\nbelow to get started with running your first quantum program!\n\nQuickstart with interactive tutorial notebooks\n----------------------------------------------\n\nWithout installing anything, you can quickly get started with quantum programming by exploring\nour interactive [Jupyter][jupyter] notebook tutorials and examples. To run them in a preconfigured\nexecution environment on [Binder][mybinder], click the "launch binder" badge at the top of the\nREADME or the link [here][binder]! To learn more about the tutorials and how you can add your own,\nvisit the [rigetti/forest-tutorials][forest-tutorials] repository. If you\'d rather set everything\nup locally, or are interested in contributing to pyQuil, continue onto the next section for\ninstructions on installing pyQuil and the Forest SDK.\n\nInstalling pyQuil and the Forest SDK\n------------------------------------\n\n[![pypi][pypi-badge]][pypi-repo]\n[![conda-forge][conda-forge-badge]][conda-forge-badge]\n[![conda-rigetti][conda-rigetti-badge]][conda-rigetti-repo]\n\nPyQuil can be installed using `conda`, `pip`, or from source. To install it from PyPI (via `pip`),\ndo the following:\n\n```bash\npip install pyquil\n```\n\nTo instead install pyQuil from source, do the following from within the repository after cloning it:\n\n```bash\npip install -e .\n```\n\nIf you choose to use `pip`, we highly recommend installing pyQuil within a virtual environment.\n\nPyQuil, along with quilc, the QVM, and other libraries, make up what is called the Forest\nSDK. To make full use of pyQuil, you will need to additionally have installed\n[quilc](https://github.com/quil-lang/quilc) and the [QVM](https://github.com/quil-lang/qvm).\nFor more information, check out the docs!\n\nRunning your first quantum program\n----------------------------------\n\nIn just a few lines, we can use pyQuil with the Forest SDK to simulate a Bell state!\n\n```python\nfrom pyquil import get_qc, Program\nfrom pyquil.gates import CNOT, H, MEASURE\n \nqvm = get_qc(\'2q-qvm\')\n \np = Program()\np += H(0)\np += CNOT(0, 1)\nro = p.declare(\'ro\', \'BIT\', 2)\np += MEASURE(0, ro[0])\np += MEASURE(1, ro[1])\np.wrap_in_numshots_loop(10)\n\nqvm.run(p).readout_data[\'ro\'].tolist()\n```\n\nThe output of the above program should look something like the following,\nthe statistics of which are consistent with a two-qubit entangled state.\n\n```\n[[0, 0],\n [1, 1],\n [1, 1],\n [1, 1],\n [1, 1],\n [0, 0],\n [0, 0],\n [1, 1],\n [0, 0],\n [0, 0]]\n```\n\nUsing the Forest SDK, you can simulate the operation of a real quantum processor (QPU). If you\nwould like to run on the real QPUs in our lab in Berkeley, you can sign up for an account\non [Quantum Cloud Services][qcs-request-access] (QCS)!\n\nJoining the Forest community\n----------------------------\n\nIf you\'d like to get involved with pyQuil and Forest, joining the\n[Rigetti Forest Slack Workspace][slack-invite] is a great place to start! You can do so by\nclicking the invite link in the previous sentence, or in the badge at the top of this README.\nThe Slack Workspace is a great place to ask general questions, join high-level design discussions,\nand hear about updates to pyQuil and the Forest SDK.\n\nTo go a step further and start contributing to the development of pyQuil, good first steps are\n[reporting a bug][bug], [requesting a feature][feature], or picking up one of the issues with the\n[good first issue][first] or [help wanted][help] labels. Once you find an issue to work\non, make sure to [fork this repository][fork] and then [open a pull request][pr] once your changes\nare ready. For more information on all the ways you can contribute to pyQuil (along with\nsome helpful tips for developers and maintainers) check out our\n[Contributing Guide](CONTRIBUTING.md)!\n\nTo see what people have contributed in the past, check out the [Changelog](CHANGELOG.md) for\na detailed list of all announcements, improvements, changes, and bugfixes. The\n[Releases](https://github.com/rigetti/pyquil/releases) page for pyQuil contains similar\ninformation, but with links to the pull request for each change and its corresponding author.\nThanks for contributing to pyQuil! 🙂\n\nCiting pyQuil, Forest, and Quantum Cloud Services\n-------------------------------------------------\n\n[![zenodo][zenodo-badge]][zenodo-doi]\n\nIf you use pyQuil, Grove, or other parts of the Forest SDK in your research, please cite\nthe [Quil specification][quil-paper] using the following BibTeX snippet:\n\n```bibtex\n@misc{smith2016practical,\n    title={A Practical Quantum Instruction Set Architecture},\n    author={Robert S. Smith and Michael J. Curtis and William J. Zeng},\n    year={2016},\n    eprint={1608.03355},\n    archivePrefix={arXiv},\n    primaryClass={quant-ph}\n}\n```\n\nAdditionally, if your research involves taking data on Rigetti quantum processors (QPUs) via\nthe Quantum Cloud Services (QCS) platform, please reference the [QCS paper][qcs-paper] using the\nfollowing BibTeX snippet:\n\n```bibtex\n@article{Karalekas_2020,\n    title = {A quantum-classical cloud platform optimized for variational hybrid algorithms},\n    author = {Peter J Karalekas and Nikolas A Tezak and Eric C Peterson\n              and Colm A Ryan and Marcus P da Silva and Robert S Smith},\n    year = 2020,\n    month = {apr},\n    publisher = {{IOP} Publishing},\n    journal = {Quantum Science and Technology},\n    volume = {5},\n    number = {2},\n    pages = {024003},\n    doi = {10.1088/2058-9565/ab7559},\n    url = {https://doi.org/10.1088%2F2058-9565%2Fab7559},\n}\n```\n\nThe preprint of the QCS paper is available on [arXiv][qcs-arxiv], and the supplementary\ninteractive notebooks and datasets for the paper can be found in the [rigetti/qcs-paper][qcs-repo]\nrepository.\n\nLicense\n-------\n\nPyQuil is licensed under the\n[Apache License 2.0](https://github.com/rigetti/pyQuil/blob/master/LICENSE).\n\n[binder]: https://mybinder.org/v2/gh/rigetti/forest-tutorials/master?urlpath=lab/tree/Welcome.ipynb\n[conda-forge-badge]: https://img.shields.io/conda/vn/conda-forge/pyquil.svg\n[conda-forge-repo]: https://anaconda.org/conda-forge/pyquil\n[conda-rigetti-badge]: https://img.shields.io/conda/vn/rigetti/pyquil?label=conda-rigetti\n[conda-rigetti-repo]: https://anaconda.org/rigetti/pyquil\n[coverage-badge]: https://coveralls.io/repos/github/rigetti/pyquil/badge.svg?branch=more-badges\n[coverage-repo]: https://coveralls.io/github/rigetti/pyquil?branch=more-badges\n[docker-badge]: https://img.shields.io/docker/pulls/rigetti/forest\n[docker-repo]: https://hub.docker.com/r/rigetti/forest\n[docs-badge]: https://readthedocs.org/projects/pyquil/badge/?version=latest\n[docs-repo]: http://pyquil.readthedocs.io/en/latest/?badge=latest\n[forest-tutorials]: https://github.com/rigetti/forest-tutorials\n[jupyter]: https://jupyter.org/\n[mybinder]: https://mybinder.org\n[pepy-badge]: https://pepy.tech/badge/pyquil\n[pepy-repo]: https://pepy.tech/project/pyquil\n[pypi-badge]: https://img.shields.io/pypi/v/pyquil.svg\n[pypi-repo]: https://pypi.org/project/pyquil/\n[qcs-request-access]: https://qcs.rigetti.com/request-access\n[slack-badge]: https://img.shields.io/badge/slack-rigetti--forest-812f82.svg?\n[zenodo-badge]: https://zenodo.org/badge/DOI/10.5281/zenodo.3553165.svg\n[zenodo-doi]: https://doi.org/10.5281/zenodo.3553165\n\n[qcs-arxiv]: https://arxiv.org/abs/2001.04449\n[qcs-paper]: https://dx.doi.org/10.1088/2058-9565/ab7559\n[qcs-repo]: https://github.com/rigetti/qcs-paper\n[quil-paper]: https://arxiv.org/abs/1608.03355\n\n[bug]: https://github.com/rigetti/pyquil/issues/new?assignees=&labels=bug+%3Abug%3A&template=BUG_REPORT.md&title=\n[feature]: https://github.com/rigetti/pyquil/issues/new?assignees=&labels=enhancement+%3Asparkles%3A&template=FEATURE_REQUEST.md&title=\n[first]: https://github.com/rigetti/pyquil/labels/good%20first%20issue%20%3Ababy%3A\n[help]: https://github.com/rigetti/pyquil/labels/help%20wanted%20%3Awave%3A\n[fork]: https://github.com/rigetti/pyquil/fork\n[pr]: https://github.com/rigetti/pyquil/compare\n[slack-invite]: https://join.slack.com/t/rigetti-forest/shared_invite/enQtNTUyNTE1ODg3MzE2LWQwNzBlMjZlMmNlN2M5MzQyZDlmOGViODQ5ODI0NWMwNmYzODY4YTc2ZjdjOTNmNzhiYTk2YjVhNTE2NTRkODY\n',
    'author': 'Rigetti Computing',
    'author_email': 'softapps@rigetti.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rigetti/pyquil.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
