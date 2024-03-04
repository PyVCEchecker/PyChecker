"""
Based entirely on Django's own ``setup.py``.
"""
from setuptools import find_packages
from setuptools import setup

import tagging

setup(
    name='django-tagging',
    version=tagging.__version__,

    description='Generic tagging application for Django',
    long_description='\n'.join([open('README.rst').read(),
                                open('CHANGELOG.txt').read()]),
    keywords='django, tag, tagging',

    author=tagging.__author__,
    author_email=tagging.__author_email__,
    maintainer=tagging.__maintainer__,
    maintainer_email=tagging.__maintainer_email__,
    url=tagging.__url__,
    license=tagging.__license__,

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    classifiers=[
        'Framework :: Django',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules']
)
