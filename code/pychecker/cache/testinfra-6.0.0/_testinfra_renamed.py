import warnings


def pytest_configure(config):
    warnings.warn((
        "testinfra package has been renamed to pytest-testinfra. "
        "Please `pip install pytest-testinfra` and "
        "`pip uninstall testinfra` and "
        "update your package requirements to avoid this message"
    ), DeprecationWarning)
