import os

import pytest
import time
from test.test_core import CoreTestmonDataForTest

from testmon_dev.db import DB
from testmon_dev.process_code import encode_lines

pytest_plugins = ("pytester",)


@pytest.fixture
def tmdata(testdir):
    return CoreTestmonDataForTest(rootdir="")


class TestFileSystem(object):
    def test_filesystem_time_fractions(self):
        assert os.path.getmtime("setup.py") % 1 != 0

    @pytest.mark.xfail
    def test_mtime_difference(self, testdir, tmdata):
        file_a = testdir.makepyfile(test_a="1")
        # let's execute some minimal but realistic work which should happen between executions
        tmdata.write("test_a.py::n1", {"test_a.py": encode_lines(["1"])})
        CoreTestmonDataForTest(rootdir="")
        file_b = testdir.makepyfile(file_b="print('hello')")
        assert (file_b.mtime() - file_a.mtime()) == 0
