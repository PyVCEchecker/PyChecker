# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stan']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6,<4.0',
 'clikit>=0.6,<0.7',
 'httpstan>=4.6,<4.7',
 'numpy>=1.7,<2.0',
 'pysimdjson>=3.2,<4.0']

setup_kwargs = {
    'name': 'pystan',
    'version': '3.3.0',
    'description': 'Python interface to Stan, a package for Bayesian inference',
    'long_description': '******\nPyStan\n******\n\n**PyStan** is a Python interface to Stan, a package for Bayesian inference.\n\nStan® is a state-of-the-art platform for statistical modeling and\nhigh-performance statistical computation. Thousands of users rely on Stan for\nstatistical modeling, data analysis, and prediction in the social, biological,\nand physical sciences, engineering, and business.\n\nNotable features of PyStan include:\n\n* Automatic caching of compiled Stan models\n* Automatic caching of samples from Stan models\n* An interface similar to that of RStan\n* Open source software: ISC License\n\nGetting started\n===============\n\nInstall PyStan with ``pip install pystan``. PyStan requires Python ≥3.7 running on Linux or macOS. You will also need a C++ compiler such as gcc ≥9.0 or clang ≥10.0.\n\nThe following block of code shows how to use PyStan with a model which studied coaching effects across eight schools (see Section 5.5 of Gelman et al (2003)). This hierarchical model is often called the "eight schools" model.\n\n.. code-block:: python\n\n    import stan\n\n    schools_code = """\n    data {\n      int<lower=0> J;         // number of schools\n      real y[J];              // estimated treatment effects\n      real<lower=0> sigma[J]; // standard error of effect estimates\n    }\n    parameters {\n      real mu;                // population treatment effect\n      real<lower=0> tau;      // standard deviation in treatment effects\n      vector[J] eta;          // unscaled deviation from mu by school\n    }\n    transformed parameters {\n      vector[J] theta = mu + tau * eta;        // school treatment effects\n    }\n    model {\n      target += normal_lpdf(eta | 0, 1);       // prior log-density\n      target += normal_lpdf(y | theta, sigma); // log-likelihood\n    }\n    """\n\n    schools_data = {"J": 8,\n                    "y": [28,  8, -3,  7, -1,  1, 18, 12],\n                    "sigma": [15, 10, 16, 11,  9, 11, 10, 18]}\n\n    posterior = stan.build(schools_code, data=schools_data)\n    fit = posterior.sample(num_chains=4, num_samples=1000)\n    eta = fit["eta"]  # array with shape (8, 4000)\n    df = fit.to_frame()  # pandas `DataFrame`\n\n\nCitation\n========\n\nWe appreciate citations as they let us discover what people have been doing\nwith the software. Citations also provide evidence of use which can help in\nobtaining grant funding.\n\nTo cite PyStan in publications use:\n\nRiddell, A., Hartikainen, A., & Carter, M. (2021). PyStan (3.0.0). https://pypi.org/project/pystan\n\nOr use the following BibTeX entry::\n\n    @misc{pystan,\n      title = {pystan (3.0.0)},\n      author = {Riddell, Allen and Hartikainen, Ari and Carter, Matthew},\n      year = {2021},\n      month = mar,\n      howpublished = {PyPI}\n    }\n\nPlease also cite Stan.\n',
    'author': 'Allen Riddell',
    'author_email': 'riddella@indiana.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://mc-stan.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
