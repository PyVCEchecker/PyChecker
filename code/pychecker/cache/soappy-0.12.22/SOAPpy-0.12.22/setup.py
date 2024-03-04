#!/usr/bin/env python
#
# $Id: setup.py,v 1.11 2005/02/15 16:32:22 warnes Exp $

CVS=0

from setuptools import setup, find_packages
import os

def read(*rnames):
    return "\n"+ open(
        os.path.join('.', *rnames)
    ).read()
url="https://github.com/kiorky/SOAPpy.git"
long_description="SOAPpy provides tools for building SOAP clients and servers.  For more information see " + url\
    +'\n'+read('README.txt')\
    +'\n'+read('CHANGES.txt')
setup(
    name="SOAPpy",
    version='0.12.22',
    description="SOAP Services for Python",
    maintainer="Gregory Warnes, kiorky",
    maintainer_email="Gregory.R.Warnes@Pfizer.com, kiorky@cryptelium.net",
    url = url,
    long_description=long_description,
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    install_requires=[
        'wstools',
        'defusedxml',
    ]
)

