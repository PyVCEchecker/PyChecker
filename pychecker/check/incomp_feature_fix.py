import os
import re
import pychecker.config as config
from functools import cmp_to_key
from pychecker.utils import read_object_from_file
from pychecker.check.common import analysis_fix, ast_parse, parse_import_modules, get_func, parse_func_params, compare_version
from pychecker.check.Parser import ParserFactory


def reverse_std_modules(std_modules):
    # {pyver: [module1, module2, ...], ...} -> {module: [pyver1, pyver2, ...], ...}
    new_dict = dict()
    for pyver, modules in std_modules.items():
        for module in modules:
            if module not in new_dict:
                new_dict[module] = list()
            new_dict[module].append(pyver)
    return new_dict


std_modules = read_object_from_file(os.path.join(config.CACHE_DIR, "standard_top_level.json"))
std_modules = reverse_std_modules(std_modules)
syntax_features = read_object_from_file(os.path.join(config.CACHE_DIR, "python_features.json"))


def use_incomp_feature(path, **kwargs):
    # path: path of Python file
    # comp_info: declared compatible Python versions
    # local_modules: modules implement by the project itself
    comp_info = kwargs['comp_info'] if 'comp_info' in kwargs else config.PY_VERSIONS
    local_modules = kwargs['local_modules'] if 'local_modules' in kwargs else set()
    top_levels = extract_top_levels(path)  # module features
    top_levels -= local_modules
    features = extract_feature(path)  # syntax features
    comp_python = find_comp_pyvers(top_levels, features)  # Python vers contain all top_levels and support all features
    if use_open_encoding_kwarg(path):  # open(encoding=...) -> Python 3
        comp_python -= {"2.7"}
    difference = set(comp_info)-set(comp_python)
    if len(difference):
        return True, comp_python
    return False, comp_info


def fix_incomp_feature_usage(path, comp_info, local_modules):
    # path: path of setup.py
    # comp_info: declared compatible Python versions
    # local_modules: modules implement by the project itself
    # analysis: analyze setup.py first, and then analyze all local files whose modules are imported by setup.py
    res, comp_info = analysis_fix(path, use_incomp_feature, comp_info=comp_info, local_modules=local_modules)
    sorted_versions = sorted(comp_info, key=cmp_to_key(compare_version))
    expr = convert_range_to_expr(sorted_versions[0], sorted_versions[-1])
    return res, expr


def extract_feature(path):
    # match each line of code with regex
    matched_features = set()

    file = open(path)
    lines = file.readlines()
    file.close()
    for line in lines:
        if line.startswith("#"):
            continue
        for feature in syntax_features.keys():
            line = line.strip()
            if feature in matched_features:
                continue
            pattern = re.compile(syntax_features[feature]["regex"])
            if pattern.match(line):
                matched_features.add(feature)
                break
    return matched_features


def extract_top_levels(path):
    # TODO: unify ast parse
    parser = ParserFactory.make_parser("top_level")
    with open(path) as f:
        lines = f.readlines()
        code = "".join(lines)
        top_levels = parser.parse_modules(code)

    return top_levels


def find_comp_pyvers(modules, features):
    # find Python versions containing all standard modules and supporting all features
    comp_pyvers = set(config.PY_VERSIONS)
    for module in modules:
        if module not in std_modules:
            continue  # not a standard module, skip
        comp_pyvers = comp_pyvers.intersection(std_modules[module])

    for feature in features:
        comp_pyvers = comp_pyvers.intersection(syntax_features[feature]["pyver"])
    return comp_pyvers


def find_import_open_candidates(code):
    # analyze:
    # 1. if io.open or codecs.open is imported. if so, the original open function is replaced
    # 2. if io or codes is imported. if so, io.open or codecs.open may be used in the following code
    modules = parse_import_modules(code, True)
    modules = [module[0] for module in modules]
    candidates = [module for module in modules
                  if module == "io" or module == "io.open" or module == "codecs" or module == "codecs.open"]
    return candidates


def is_open_call(expr, this_ast, candidates):
    # judge whether a function is built-in open
    func_name = get_func(expr, this_ast)  # full function name, e.g. module.submodule.function
    for candidate in candidates:
        if candidate in func_name:
            return False  # io.open or codecs.open
    parts = func_name.split(".")
    if "open" in parts:
        # 'in parts' but not '==parts[-1]', because of the form like open(...).read()
        return True
    return False


def use_open_encoding_kwarg(path):
    file = open(path)
    code = "".join(file.readlines())
    file.close()
    body, this_ast = ast_parse(code)

    candidates = find_import_open_candidates(code)
    if "io.open" in candidates or "codecs.open" in candidates:
        # the original open function is replaced.
        # io.open(encoding=...) and codecs.open(encoding=...) are both compatible with Python 2 and 3.
        return False

    # 1. whether built-in open function is used; 2. if so, extract its keyword params.
    open_params = parse_func_params(body, this_ast, "open", is_open_call, candidates)
    if not open_params:
        return False  # built-in open is not used

    for param in open_params:
        if not param.arg:
            pass
        if param.arg == "encoding":
            return True
    return False


def convert_range_to_expr(lower, upper):
    # TODO: 3.10
    if lower == config.PY_VERSIONS[0] and upper == config.PY_VERSIONS[-2]:
        return ""
    if lower == config.PY_VERSIONS[0]:
        return f"<={upper}"
    if upper == config.PY_VERSIONS[-2]:
        return f">={lower}"
    return f">={lower}, <={upper}"


res = fix_incomp_feature_usage("/media/yhj/HDD/dataset/metadata-analysis/discord-1.7.3/setup.py", config.PY_VERSIONS, {"discord"})
print(res)
