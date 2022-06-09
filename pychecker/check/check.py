import os
import time
import pychecker.config as config
from pychecker.check.no_avl_resource_detection import detect_no_avl_resource_pkg, detect_no_avl_resource, parse_comp_expr
from pychecker.check.visit_pypi import parse_whl_comp, get_source_url, download_extract_source, get_metadata, COMP
from pychecker.check.incomp_feature_detection import detect_incomp_feature_usage
from pychecker.check.local_comp_detection import detect_local_comp_detection
from pychecker.check.common import find_custom_modules


def check_pkgver(pkg, ver, cache_path=config.CACHE_DIR, save_files=False):
    # pkg: package name
    # ver: version of the package
    # cache_path: path to download the package
    # save_files: save the package or not after checking
    results = [False, False, False]  # [FEATURE, LOCAL, RESOURCE]
    # check RESOURCE regardless of resource types
    metadata = get_metadata(pkg, ver)
    if not metadata:
        print(f"{pkg}-{ver} not found.")
        return results
    pyvers = set(parse_comp_expr(metadata[COMP], config.PY_VERSIONS))
    results[2] = detect_no_avl_resource_pkg(pkg, ver)

    # FEATURE & LOCAL occur in source code resources, filter Python versions only have source code resources.
    wheel_pyvers = parse_whl_comp(pkg, ver)
    no_wheel_pyvers = pyvers-wheel_pyvers-{"3.10"}  # TODO: 3.10
    if not no_wheel_pyvers:
        return results

    # download & extract resources
    path1 = os.path.join(cache_path, f"{pkg}-{ver}")
    path2 = os.path.join(cache_path, f"{pkg.replace('-', '_')}-{ver}")
    path = path1 if os.path.exists(path1) else path2
    zip_path = ""
    if not os.path.exists(path):
        source_url = get_source_url(pkg, ver)
        if not source_url:
            print(f"{pkg}-{ver}: Source code resources not found, "
                  "skip checking Use Incompatible Features & Check Compatibility Locally")
            return results
        _, zip_path = download_extract_source(source_url, path)
        time.sleep(5)
        path = path1 if os.path.exists(path1) else path2
    setup_path = os.path.join(path, "setup.py")
    if not os.path.exists(setup_path):
        print(f"{pkg}-{ver}: setup.py not found, "
              "skip checking Use Incompatible Features & Check Compatibility Locally")
        return results

    # check LOCAL for source code
    results[1] = detect_local_comp_detection(setup_path)

    # check FEATURE for source code
    custom_modules = find_custom_modules(path)
    if not custom_modules:
        print(f"{pkg}-{ver}: Source code of the package not found, skip checking Use Incompatible Features")
        return results
    results[0] = detect_incomp_feature_usage(setup_path, no_wheel_pyvers, custom_modules)

    # delete downloaded and extracted files if necessary
    if not save_files:
        if os.path.exists(path):
            os.rmdir(path)
        if os.path.exists(zip_path):
            os.rmdir(zip_path)
    return results


def check_project(path, python_requires):
    results = [False, False, False]
    pyvers = set(parse_comp_expr(python_requires, config.PY_VERSIONS))-{"3.10"}  # TODO: 3.10

    # check RESOURCE
    requirements = find_requirements_file(path)
    if not requirements:
        print("requirements.txt not found, skip checking No Available Resource")
    else:
        with open(requirements) as f:
            install_requires = f.readlines()
        results[2] = detect_no_avl_resource(python_requires, install_requires)

    # check LOCAL
    setup_path = os.path.join(path, "setup.py")
    if not os.path.exists(setup_path):
        print("setup.py not found, "
              "skip checking Use Incompatible Features & Check Compatibility Locally")
        return results
    results[1] = detect_local_comp_detection(setup_path)

    # check FEATURES
    custom_modules = find_custom_modules(path)
    if not custom_modules:
        print("Source code of the package not found, skip checking Use Incompatible Features")
        return results
    results[0] = detect_incomp_feature_usage(setup_path, pyvers, custom_modules)
    return results


def find_requirements_file(path):
    # find requirements.txt / requires.txt in the project
    requirements = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file == "requirements.txt" and not file == "requires.txt":
                continue
            requirements = os.path.join(root, file)
            break
        if requirements:
            break
    return requirements


def print_results(results):
    names = ["Use Incompatible Features",
             "Check Compatibility Locally",
             "No available resource"]
    for name, result in zip(names, results):
        color = "\033[31m" if result else "\033[32m"
        print(color, f"{name}: {result}")
