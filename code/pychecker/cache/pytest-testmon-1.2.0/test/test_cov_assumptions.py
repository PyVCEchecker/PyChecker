# #ifdef PYTEST_COV
import os

import pytest
from coverage import Coverage
from testmon_dev.testmon_core import Testmon as CoreTestmon, is_coverage5

pytest_plugins = ("pytester",)


class TestPytestCovAssumptions:
    class Plugin:
        def pytest_configure(self, config):
            cov_plugin = config.pluginmanager.get_plugin("_cov")
            self.cov_active = bool(cov_plugin and cov_plugin._started)

    def test_inactive(self, testdir):
        plugin = self.Plugin()
        testdir.runpytest_inprocess("", plugins=[plugin])
        assert plugin.cov_active == False

    @pytest.mark.filterwarnings("ignore:")
    def test_active(self, testdir):
        plugin = self.Plugin()

        testdir.runpytest_inprocess("--cov=.", plugins=[plugin])
        assert plugin.cov_active == True

    def test_specify_include(self, testdir):
        testdir.makepyfile(
            lib="""
        Ahoj
        bka
        # #
        """
        )

        cov = Coverage(data_file=None, config_file=False, include=["."])
        cov._warn_no_data = False
        cov.start()
        cov.stop()

        if is_coverage5():
            assert set() == cov.get_data().measured_files()
        else:
            assert [] == cov.get_data().measured_files()

    # specifying source=".", searches for all python files in that directory and adds them
    # to measured_files(), cov.get_data() calls cov._post_save_work() which searches all py files in the source dir
    def test_specify_source(self, testdir):
        testdir.makepyfile(lib="")

        cov = Coverage(data_file=None, config_file=False, source=["."])
        cov._warn_no_data = False
        cov.start()
        cov.stop()
        for mf in cov.get_data().measured_files():
            mf.endswith("lib.py")


# #endif

# #ifdef DOGFOODING
class TestCovAssumptions:
    def test_get_filter_method_based_on_cov_version(self):
        cov = Coverage()
        cov.start()
        cov.stop()
        assert CoreTestmon.get_file_filter_method_based_on_cov_version(cov)

    def test_check_include_omit_etc_internal_with_source(self, testdir):
        source = testdir.mkdir("source")
        cov = Coverage(source=[source], omit=[os.path.join(source, "omit/*")])
        cov.start()
        cov.stop()

        check_include_omit_etc = (
            CoreTestmon.get_file_filter_method_based_on_cov_version(cov)
        )
        assert not check_include_omit_etc(
            os.path.join(source, "a.py"), CoreTestmon.DummyFrame
        )
        assert check_include_omit_etc(
            os.path.join(source, "omit/c.py"), CoreTestmon.DummyFrame
        )
        assert check_include_omit_etc("lib/d.py", CoreTestmon.DummyFrame)

    def test_check_include_omit_etc_internal_with_include(self, testdir):
        include = testdir.mkdir("include")
        cov = Coverage(
            include=[os.path.join(include, "*")],
        )
        cov.start()
        cov.stop()

        check_include_omit_etc = (
            CoreTestmon.get_file_filter_method_based_on_cov_version(cov)
        )
        assert not check_include_omit_etc(
            os.path.join(include, "a.py"), CoreTestmon.DummyFrame
        )
        assert check_include_omit_etc(os.path.join("lib/b.py"), CoreTestmon.DummyFrame)


# #endif
