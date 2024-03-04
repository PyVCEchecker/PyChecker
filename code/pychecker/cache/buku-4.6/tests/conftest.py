#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pytest_configure(config):
    # plugin = config.pluginmanager.getplugin('mypy')
    # plugin.mypy_argv.append('--check-untyped-defs')
    config.addinivalue_line(
        "markers", "non_tox: mark test to not run on tox"
    )
