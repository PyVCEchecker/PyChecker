.. image:: https://img.shields.io/pypi/v/jaraco.logging.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/jaraco.logging.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/jaraco.logging

.. image:: https://github.com/jaraco/jaraco.logging/workflows/Automated%20Tests/badge.svg
   :target: https://github.com/jaraco/jaraco.logging/actions?query=workflow%3A%22Automated+Tests%22
   :alt: Automated Tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. image:: https://readthedocs.org/projects/jaracologging/badge/?version=latest
   :target: https://jaracologging.readthedocs.io/en/latest/?badge=latest

Argument Parsing
================

Quickly solicit log level info from command-line parameters::

    parser = argparse.ArgumentParser()
    jaraco.logging.add_arguments(parser)
    args = parser.parse_args()
    jaraco.logging.setup(args)
