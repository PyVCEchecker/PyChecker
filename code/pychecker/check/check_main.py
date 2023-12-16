import os
import time
import pychecker.config as config
from pychecker.check.root_cause_3_detection import detect_no_avl_resource_pkg, detect_no_avl_resource, parse_comp_expr
from pychecker.check.visit_pypi import parse_whl_comp, get_source_url, download_extract_source, get_metadata, COMP
from pychecker.check.root_cause_2_detection import detect_incomp_feature_usage,use_incomp_feature
from pychecker.check.root_cause_1_detection import detect_local_comp_detection
from pychecker.check.common import find_custom_modules,rich_console
import shutil

def check_pkgver(pkg, ver, cache_path=config.CACHE_DIR, save_files=False,detect_runtime_error=True):
    # pkg: package name
    # ver: version of the package
    # cache_path: path to download the package
    # save_files: save the package or not after checking
    # detect_runtime_error: if true ，functions's behaviors should be changed
    results = [False, False, False]  # [LOCAL,FEATURE, RESOURCE]
    # check RESOURCE regardless of resource types
    metadata = get_metadata(pkg, ver)# return {DEPS: metadata[DEPS], COMP: metadata[COMP]}
    if not metadata:
        print(f"{pkg}-{ver} not found.")
        return results
    pyvers = set(parse_comp_expr(metadata[COMP], config.PY_VERSIONS))
    results[2] = detect_no_avl_resource_pkg(pkg, ver)

    # FEATURE & LOCAL occur in source code resources, filter Python versions only have source code resources.
    wheel_pyvers = parse_whl_comp(pkg, ver)
    if wheel_pyvers:
        no_wheel_pyvers = pyvers - wheel_pyvers
    if not detect_runtime_error:
        if not no_wheel_pyvers:
            return results
    # download & extract resources
    path = os.path.join(cache_path, f"{pkg}-{ver}")
    '''
    ghc:
    I don't know why path2 is used, so I try to disuse it.
    '''
    # path2 = os.path.join(cache_path, f"{pkg.replace('-', '_')}-{ver}")
    # path = path1 if os.path.exists(path1) else path2

    zip_path = ""
    isWhl=False
    source_url = get_source_url(pkg, ver, detect_runtime_error)

    if not source_url:
        print(f"{pkg}-{ver}: Source code resources not found, "
              "skip checking Use Incompatible Features & Check Compatibility Locally")
        return results
    if source_url.endswith('.whl'):
        isWhl = True
    if not os.path.exists(path):
        _, zip_path = download_extract_source(source_url, path,cache_path=cache_path,detect_runtime_error=detect_runtime_error)
        time.sleep(0.1)
        # path = path1 if os.path.exists(path1) else path2

    if detect_runtime_error==True and isWhl==True:
        #if detect runtime error,skip check LOCAL
        #behaviors of check FEATURE will change
        custom_modules = find_custom_modules(path)
        if not custom_modules:
            print(f"{pkg}-{ver}: Source code of the package not found, skip checking Use Incompatible Features")
            return results

        # results[1]=detect_runtime_local_comp(path,  pyvers, custom_modules)
        results[1] = detect_incomp_feature_usage(path, metadata[COMP])


    else:
        setup_path = os.path.join(path, "setup.py")
        if not os.path.exists(setup_path):
            print(f"{pkg}-{ver}: setup.py not found, "
                  "skip checking Use Incompatible Features & Check Compatibility Locally")
            return results

        # check LOCAL for source code
        results[0] = detect_local_comp_detection(setup_path)

        # check FEATURE for source code
        custom_modules = find_custom_modules(path)
        if not custom_modules:
            print(f"{pkg}-{ver}: Source code of the package not found, skip checking Use Incompatible Features")
            return results
        if detect_runtime_error==False:
            results[1] = detect_incomp_feature_usage(setup_path, no_wheel_pyvers, custom_modules)
        if detect_runtime_error==True:
            # results[1] = detect_runtime_local_comp(path, pyvers, custom_modules)
            results[1] = detect_incomp_feature_usage(path,metadata[COMP])

    # delete downloaded and extracted files if necessary

    if not save_files:
        if os.path.exists(path):
            shutil.rmtree(path)
        if os.path.exists(zip_path):
            os.remove(zip_path)
    return results


def check_project(path, python_requires):
    results = [False, False, False]
    pyvers = set(parse_comp_expr(python_requires, config.PY_VERSIONS))

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
    results[0] = detect_local_comp_detection(setup_path)

    # check FEATURES
    custom_modules = find_custom_modules(path)
    if not custom_modules:
        print("Source code of the package not found, skip checking Use Incompatible Features")
        return results
    results[1] = detect_incomp_feature_usage(path, python_requires)
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
    names = ["Setup script issue",
             "using incompatible feature",
             "python version conflict"]
    console=rich_console()
    console.print('-'*50,style="grey53")
    for name, result in zip(names, results):
        if result:
            console.print(f"[red]{name}:{result}")
        else:
            console.print(f"[green]{name}:{result}")

if __name__ == '__main__':
    # result=check_project("/home/yhj/projects/PyVCEchecker/pychecker/cache/hydra-core-1.1.1",">=2.7")
    result=check_pkgver("cachier","1.5.0" ,save_files=True,detect_runtime_error=True)
    print_results(result)