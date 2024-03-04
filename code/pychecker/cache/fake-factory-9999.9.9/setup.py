#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


version = '9999.9.9'

package_name = 'fake-factory'

error = """ERROR:
    The `fake-factory` package was deprecated on December 15th, 2016.
    Use the `Faker` package instead."""

print(error)


setup(
    name=package_name,
    version=version,
    description="The `fake-factory` package was deprecated on December 15th, 2016. Use the `Faker` package instead.",
    long_description=error,
    classifiers=[
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 7 - Inactive',
        'License :: OSI Approved :: MIT License'
    ],
    author='joke2k',
    author_email='joke2k@gmail.com',
    url='https://github.com/joke2k/faker',
    license='MIT License',
    packages=find_packages(),
    platforms=["any"],
    zip_safe=True,
)
