# doc/sphinx.mk
# Part of ‘python-daemon’, an implementation of PEP 3143.
#
# This is free software, and you are welcome to redistribute it under
# certain conditions; see the end of this file for copyright
# information, grant of license, and disclaimer of warranty.

# Makefile module for Sphinx documentation.

SPHINX_BUILD = $(PYTHON) -m sphinx
SPHINX_BUILD_OPTS =

PAPER =
SPHINX_SOURCE_DIR = ${DOC_DIR}/source
SPHINX_BUILD_DIR = ${DOC_DIR}/build
SPHINX_CACHE_DIR = ${SPHINX_BUILD_DIR}/.cache

GENERATED_FILES += ${SPHINX_BUILD_DIR}

PAPEROPT_a4 = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
SPHINX_BUILD_NOCACHE_OPTS = ${PAPEROPT_${PAPER}} ${SPHINX_BUILD_OPTS} ${SPHINX_SOURCE_DIR}
SPHINX_BUILD_ALL_OPTS = -d ${SPHINX_CACHE_DIR} ${SPHINX_BUILD_NOCACHE_OPTS}

.PHONY: sphinx-html
sphinx-html:
	$(SPHINX_BUILD) -b html ${SPHINX_BUILD_ALL_OPTS} ${SPHINX_BUILD_DIR}/html

.PHONY: sphinx-dirhtml
sphinx-dirhtml:
	$(SPHINX_BUILD) -b dirhtml ${SPHINX_BUILD_ALL_OPTS} ${SPHINX_BUILD_DIR}/dirhtml

.PHONY: sphinx-singlehtml
sphinx-singlehtml:
	$(SPHINX_BUILD) -b singlehtml ${SPHINX_BUILD_ALL_OPTS} ${SPHINX_BUILD_DIR}/singlehtml

.PHONY: sphinx-text
sphinx-text:
	$(SPHINX_BUILD) -b text ${SPHINX_BUILD_ALL_OPTS} ${SPHINX_BUILD_DIR}/text

.PHONY: sphinx-gettext
sphinx-gettext:
	$(SPHINX_BUILD) -b gettext ${SPHINX_BUILD_NOCACHE_OPTS} ${SPHINX_BUILD_DIR}/locale

.PHONY: sphinx-linkcheck
sphinx-linkcheck:
	$(SPHINX_BUILD) -b linkcheck ${SPHINX_BUILD_ALL_OPTS} ${SPHINX_BUILD_DIR}/linkcheck

.PHONY: sphinx-doctest
sphinx-doctest:
	$(SPHINX_BUILD) -b doctest ${SPHINX_BUILD_ALL_OPTS} ${SPHINX_BUILD_DIR}/doctest

.PHONY: sphinx-coverage
sphinx-coverage:
	$(SPHINX_BUILD) -b coverage ${SPHINX_BUILD_ALL_OPTS} ${SPHINX_BUILD_DIR}/coverage


# Copyright © 2006–2019 Ben Finney <ben+python@benfinney.id.au>
#
# This is free software: you may copy, modify, and/or distribute this work
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 3 of that license or any later version.
# No warranty expressed or implied. See the file ‘LICENSE.GPL-3’ for details.


# Local Variables:
# coding: utf-8
# mode: makefile
# End:
# vim: fileencoding=utf-8 filetype=make :
