# -*- coding: utf-8 -*-
#
# test/test_metadata.py
# Part of ‘python-daemon’, an implementation of PEP 3143.
#
# This is free software, and you are welcome to redistribute it under
# certain conditions; see the end of this file for copyright
# information, grant of license, and disclaimer of warranty.

""" Unit test for ‘_metadata’ private module.
    """

from __future__ import (absolute_import, unicode_literals)

import collections
import errno
import functools
import json
import re
try:
    # Python 3 standard library.
    import urllib.parse as urlparse
except ImportError:
    # Python 2 standard library.
    import urlparse

import unittest.mock
import pkg_resources
import testtools.helpers
import testtools.matchers

from . import scaffold
from .scaffold import unicode

import daemon._metadata as metadata


class HasAttribute(testtools.matchers.Matcher):
    """ A matcher to assert an object has a named attribute. """

    def __init__(self, name):
        self.attribute_name = name

    def match(self, instance):
        """ Assert the object `instance` has an attribute named `name`. """
        result = None
        if not testtools.helpers.safe_hasattr(instance, self.attribute_name):
            result = AttributeNotFoundMismatch(instance, self.attribute_name)
        return result


class AttributeNotFoundMismatch(testtools.matchers.Mismatch):
    """ The specified instance does not have the named attribute. """

    def __init__(self, instance, name):
        self.instance = instance
        self.attribute_name = name

    def describe(self):
        """ Emit a text description of this mismatch. """
        text = (
                "{instance!r}"
                " has no attribute named {name!r}").format(
                    instance=self.instance, name=self.attribute_name)
        return text


class metadata_value_TestCase(scaffold.TestCaseWithScenarios):
    """ Test cases for metadata module values. """

    expected_str_attributes = set([
            'version_installed',
            'author',
            'copyright',
            'license',
            'url',
            ])

    scenarios = [
            (name, {'attribute_name': name})
            for name in expected_str_attributes]
    for (name, params) in scenarios:
        if name == 'version_installed':
            # No duck typing, this attribute might be None.
            params['ducktype_attribute_name'] = NotImplemented
            continue
        # Expect an attribute of ‘str’ to test this value.
        params['ducktype_attribute_name'] = 'isdigit'

    def test_module_has_attribute(self):
        """ Metadata should have expected value as a module attribute. """
        self.assertThat(
                metadata, HasAttribute(self.attribute_name))

    def test_module_attribute_has_duck_type(self):
        """ Metadata value should have expected duck-typing attribute. """
        if self.ducktype_attribute_name == NotImplemented:
            self.skipTest("Can't assert this attribute's type")
        instance = getattr(metadata, self.attribute_name)
        self.assertThat(
                instance, HasAttribute(self.ducktype_attribute_name))


class YearRange_TestCase(scaffold.TestCaseWithScenarios):
    """ Test cases for ‘YearRange’ class. """

    scenarios = [
            ('simple', {
                'begin_year': 1970,
                'end_year': 1979,
                'expected_text': "1970–1979",
                }),
            ('same year', {
                'begin_year': 1970,
                'end_year': 1970,
                'expected_text': "1970",
                }),
            ('no end year', {
                'begin_year': 1970,
                'end_year': None,
                'expected_text': "1970",
                }),
            ]

    def setUp(self):
        """ Set up test fixtures. """
        super().setUp()

        self.test_instance = metadata.YearRange(
                self.begin_year, self.end_year)

    def test_text_representation_as_expected(self):
        """ Text representation should be as expected. """
        result = unicode(self.test_instance)
        self.assertEqual(result, self.expected_text)


FakeYearRange = collections.namedtuple('FakeYearRange', ['begin', 'end'])


@unittest.mock.patch.object(metadata, 'YearRange', new=FakeYearRange)
class make_year_range_TestCase(scaffold.TestCaseWithScenarios):
    """ Test cases for ‘make_year_range’ function. """

    scenarios = [
            ('simple', {
                'begin_year': "1970",
                'end_date': "1979-01-01",
                'expected_range': FakeYearRange(begin=1970, end=1979),
                }),
            ('same year', {
                'begin_year': "1970",
                'end_date': "1970-01-01",
                'expected_range': FakeYearRange(begin=1970, end=1970),
                }),
            ('no end year', {
                'begin_year': "1970",
                'end_date': None,
                'expected_range': FakeYearRange(begin=1970, end=None),
                }),
            ('end date UNKNOWN token', {
                'begin_year': "1970",
                'end_date': "UNKNOWN",
                'expected_range': FakeYearRange(begin=1970, end=None),
                }),
            ('end date FUTURE token', {
                'begin_year': "1970",
                'end_date': "FUTURE",
                'expected_range': FakeYearRange(begin=1970, end=None),
                }),
            ]

    def test_result_matches_expected_range(self):
        """ Result should match expected YearRange. """
        result = metadata.make_year_range(self.begin_year, self.end_date)
        self.assertEqual(result, self.expected_range)


class metadata_content_TestCase(scaffold.TestCase):
    """ Test cases for content of metadata. """

    def test_copyright_formatted_correctly(self):
        """ Copyright statement should be formatted correctly. """
        regex_pattern = (
                r"Copyright © "
                r"\d{4}"  # Four-digit year.
                r"(?:–\d{4})?"  # Optional range dash and four-digit year.
                )
        regex_flags = re.UNICODE
        self.assertThat(
                metadata.copyright,
                testtools.matchers.MatchesRegex(regex_pattern, regex_flags))

    def test_author_formatted_correctly(self):
        """ Author information should be formatted correctly. """
        regex_pattern = (
                r".+ "  # Name.
                r"<[^>]+>"  # Email address, in angle brackets.
                )
        regex_flags = re.UNICODE
        self.assertThat(
                metadata.author,
                testtools.matchers.MatchesRegex(regex_pattern, regex_flags))

    def test_copyright_contains_author(self):
        """ Copyright information should contain author information. """
        self.assertThat(
                metadata.copyright,
                testtools.matchers.Contains(metadata.author))

    def test_url_parses_correctly(self):
        """ Homepage URL should parse correctly. """
        result = urlparse.urlparse(metadata.url)
        self.assertIsInstance(
                result, urlparse.ParseResult,
                "URL value {url!r} did not parse correctly".format(
                    url=metadata.url))


try:
    FileNotFoundError
except NameError:
    # Python 2 uses IOError.
    FileNotFoundError = functools.partial(IOError, errno.ENOENT)

version_info_filename = "version_info.json"


def fake_func_has_metadata(name, *, resource_names):
    """ Fake the behaviour of ‘pkg_resources.Distribution.has_metadata’.

        :param name: The name of the resource to interrogate.
        :param resource_names: The known metadata resource names.
        :return: True iff `resource_name` is a known metadata resource.
        """
    result = (name in resource_names)
    return result


def fake_func_get_metadata(name, *, resources):
    """ Fake the behaviour of ‘pkg_resources.Distribution.get_metadata’.

        :param name: The name of the resource to interrogate.
        :param resources: Mapping {name: resource} of the known
            metadata resources.
        :return: The metadata resource as a string.
        """
    resource = NotImplemented
    if (
            hasattr(resources, '__getitem__')
            and name in resources):
        try:
            resource = resources[name]
        except KeyError:
            error = FileNotFoundError(name)
            raise error
    if resource is NotImplemented:
        error = FileNotFoundError(name)
        raise error
    return resource


def fake_func_get_distribution(
        testcase,
        name, *, fake_distribution=None):
    """ Fake the behaviour of ‘pkg_resources.get_distribution’. """
    if name != metadata.distribution_name:
        raise pkg_resources.DistributionNotFound
    if hasattr(testcase, 'get_distribution_error'):
        raise testcase.get_distribution_error
    if (fake_distribution is None):
        fake_resources = {}
        if hasattr(testcase, 'test_version_info'):
            fake_resources['version_info_filename'] = testcase.test_version_info
        fake_distribution = make_mock_distribution(
                name=name,
                metadata_resources=fake_resources)
    return fake_distribution


def make_mock_distribution(
        name,
        *,
        metadata_resources=None):
    """ Make a mock for a `pkg_resources.Distribution` object. """
    if metadata_resources is None:
        metadata_resources = {}
    mock_distribution = unittest.mock.MagicMock(name='Distribution')
    mock_distribution.has_metadata.side_effect = functools.partial(
            fake_func_has_metadata,
            resource_names=metadata_resources.keys(),
    )
    mock_distribution.get_metadata.side_effect = functools.partial(
            fake_func_get_metadata,
            resources=metadata_resources,
    )
    return mock_distribution


def patch_metadata_distribution_name(*, testcase, distribution_name=None):
    """ Patch `metadata.distribution_name` for the `testcase`. """
    if distribution_name is None:
        distribution_name = testcase.mock_distribution_name
    patcher_distribution_name = unittest.mock.patch.object(
            metadata, 'distribution_name',
            new=distribution_name)
    patcher_distribution_name.start()
    testcase.addCleanup(patcher_distribution_name.stop)


def patch_pkg_resources_get_distribution(
        *, testcase, mock_distribution=None):
    """
    Patch the `pkg_resources.get_distribution` function for `testcase`.
    """
    if mock_distribution is None:
        mock_distribution = testcase.mock_distribution
    func_patcher_get_distribution = unittest.mock.patch.object(
            pkg_resources, 'get_distribution')
    func_patcher_get_distribution.start()
    testcase.addCleanup(func_patcher_get_distribution.stop)
    pkg_resources.get_distribution.side_effect = functools.partial(
            fake_func_get_distribution,
            testcase,
            fake_distribution=mock_distribution)


class get_distribution_TestCase(scaffold.TestCaseWithScenarios):
    """ Test cases for ‘get_distribution’ function. """

    scenarios = [
            ('specified none', {
                'test_name': None,
                'expected_distribution': None,
                }),
            ('specified exist', {
                'test_name': 'mock-dist',
                }),
            ('specified not-exist', {
                'test_name': 'b0gUs',
                'expected_distribution': None,
                }),
            ]

    def setUp(self):
        """ Set up test fixtures. """
        super().setUp()

        if not hasattr(self, 'test_metadata_resources'):
            resources = {}
            if hasattr(self, 'test_version_info'):
                resources[self.version_info_filename] = (
                        self.test_version_info)
            self.test_metadata_resources = resources

        self.mock_distribution_name = "mock-dist"
        patch_metadata_distribution_name(testcase=self)
        self.mock_distribution = make_mock_distribution(
                metadata.distribution_name,
                metadata_resources=self.test_metadata_resources)
        patch_pkg_resources_get_distribution(
                testcase=self,
                mock_distribution=self.mock_distribution)

        self.test_args = {}
        if hasattr(self, 'test_name'):
            self.test_args['name'] = self.test_name

        if not hasattr(self, 'expected_distribution'):
            self.expected_distribution = self.mock_distribution

    def test_requests_installed_distribution(self):
        """ The package distribution should be retrieved. """
        if (getattr(self, 'test_name', None) is None):
            self.skipTest("no distribution name in this scenario")
        expected_distribution_name = self.test_name
        metadata.get_distribution(**self.test_args)
        pkg_resources.get_distribution.assert_called_with(
                expected_distribution_name)

    def test_returns_expected_result(self):
        """ Should return the expected result. """
        result = metadata.get_distribution(**self.test_args)
        self.assertIs(self.expected_distribution, result)


class get_distribution_version_info_TestCase(scaffold.TestCaseWithScenarios):
    """ Test cases for ‘get_distribution_version_info’ function. """

    default_version_info = {
            'release_date': "UNKNOWN",
            'version': "UNKNOWN",
            'maintainer': "UNKNOWN",
            }

    scenarios = [
            ('version 0.0', {
                'test_version_info': json.dumps({
                    'version': "0.0",
                    }),
                'expected_version_info': {'version': "0.0"},
                }),
            ('version 1.0', {
                'test_version_info': json.dumps({
                    'version': "1.0",
                    }),
                'expected_version_info': {'version': "1.0"},
                }),
            ('file lorem_ipsum.json', {
                'test_filename': "lorem_ipsum.json",
                'version_info_filename': "lorem_ipsum.json",
                'test_version_info': json.dumps({
                    'version': "1.0",
                    }),
                'expected_resource_name': "lorem_ipsum.json",
                'expected_version_info': {'version': "1.0"},
                }),
            ('not installed', {
                'get_distribution_error': pkg_resources.DistributionNotFound(),
                'expected_version_info': default_version_info,
                }),
            ('no version_info', {
                'expected_version_info': default_version_info,
                }),
            ('wrong filename', {
                'test_filename': "lorem_ipsum.json",
                'test_version_info': json.dumps({
                    'version': "1.0",
                    }),
                'expected_resource_name': "lorem_ipsum.json",
                'expected_version_info': default_version_info,
                }),
            ]

    def setUp(self):
        """ Set up test fixtures. """
        super().setUp()

        self.mock_distribution_name = "mock-dist"
        patch_metadata_distribution_name(testcase=self)
        self.mock_distribution = make_mock_distribution(
                metadata.distribution_name, metadata_resources=None)

        self.test_args = {}
        if hasattr(self, 'test_filename'):
            self.test_args['filename'] = self.test_filename

        if not hasattr(self, 'version_info_filename'):
            self.version_info_filename = version_info_filename

        if not hasattr(self, 'expected_resource_name'):
            self.expected_resource_name = version_info_filename

        if not hasattr(self, 'test_metadata_resources'):
            resources = {}
            if hasattr(self, 'test_version_info'):
                resources[self.version_info_filename] = (
                        self.test_version_info)
            self.test_metadata_resources = resources

        self.mock_distribution = make_mock_distribution(
                name=metadata.distribution_name,
                metadata_resources=self.test_metadata_resources)
        self.test_args['distribution'] = getattr(
                self, 'test_distribution', self.mock_distribution)

    def test_requests_specified_filename(self):
        """ The specified metadata resource name should be requested. """
        if hasattr(self, 'get_distribution_error'):
            self.skipTest("No access to distribution")
        metadata.get_distribution_version_info(**self.test_args)
        self.mock_distribution.has_metadata.assert_called_with(
                self.expected_resource_name)

    def test_result_matches_expected_items(self):
        """ The result should match the expected items. """
        version_info = metadata.get_distribution_version_info(**self.test_args)
        self.assertEqual(self.expected_version_info, version_info)


# Copyright © 2008–2019 Ben Finney <ben+python@benfinney.id.au>
#
# This is free software: you may copy, modify, and/or distribute this work
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 3 of that license or any later version.
# No warranty expressed or implied. See the file ‘LICENSE.GPL-3’ for details.


# Local variables:
# coding: utf-8
# mode: python
# End:
# vim: fileencoding=utf-8 filetype=python :
