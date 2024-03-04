from datetime import datetime as dt
from setuptools import find_packages, setup

PROJECT_NAME = "robomotion"
PROJECT_PACKAGE_NAME = "robomotion"
PROJECT_LICENSE = "Apache License 2.0"
PROJECT_AUTHOR = "Robomotion IO"
PROJECT_COPYRIGHT = f" 2020-{dt.now().year}, {PROJECT_AUTHOR}"
PROJECT_URL = "https://robomotion.io/"
PROJECT_EMAIL = "support@robomotion.io"

PROJECT_GITHUB_USERNAME = "robomotionio"
PROJECT_GITHUB_REPOSITORY = "python-lib"

PYPI_URL = f"https://pypi.org/project/{PROJECT_PACKAGE_NAME}"
GITHUB_PATH = f"{PROJECT_GITHUB_USERNAME}/{PROJECT_GITHUB_REPOSITORY}"
GITHUB_URL = f"https://github.com/{GITHUB_PATH}"

PROJECT_URLS = {
    "Bug Reports": f"{GITHUB_URL}/issues",
    "Dev Docs": "https://docs.robomotion.io/",
    "Slack": "https://slack.robomotion.io",
    "Forum": "https://forum.robomotion.io/",
}

PACKAGES = find_packages(exclude=["tests", "tests.*"])

REQUIRES = [
    "protobuf==3.8.0",
    "grpcio==1.27.2",
    "grpcio-tools==1.27.2",
    "zipp==3.1.0"
]

setup(
    name=PROJECT_PACKAGE_NAME,
    version="1.4.0",
    url=PROJECT_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires='>=3.6',
    test_suite="tests",
)