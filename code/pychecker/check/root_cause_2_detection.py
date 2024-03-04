import os
import re
import pychecker.config as config
from pychecker.utils import read_object_from_file
from pychecker.check.common import  ast_parse, parse_import_modules, get_func, parse_func_params,find_custom_modules,parse_all_pyfiles,suggest_pyver,sorted_pyver_list,rich_console
from pychecker.check.Parser import ParserFactory
from pychecker.check.root_cause_3_detection import parse_comp_expr
from pychecker.check.py_syntax_rule.parse_file_rule import file_rule
from packaging.specifiers import SpecifierSet
from packaging.version import Version
import tokenize
from io import BytesIO
# import vermin as V

incomp_feature_dict=dict()
incomp_feature_dict["cause"]="using incompatible feature"
incomp_feature_dict["current-python_requires"]=""
incomp_feature_dict["position"]=[]
incomp_feature_dict["specific"]=[]
incomp_feature_dict["suggest-python_requires"]=""

has_inf=False

def detect_incomp_feature_usage(root_path,comp_expr=">=2.7"):

    # root_path: project root path
    # comp_expr: project original python_requires
    global incomp_feature_dict,has_inf
    has_inf = False
    incomp_feature_dict = dict()
    incomp_feature_dict["cause"] = "using incompatible feature"
    incomp_feature_dict["current-python_requires"] = ""
    incomp_feature_dict["position"] = []
    incomp_feature_dict["specific"] = []
    incomp_feature_dict["suggest-python_requires"] = ""
    incomp_feature_dict["current-python_requires"] = comp_expr
    if not comp_expr:
        # set default python_requires
        comp_expr = ">=2.7"
        incomp_feature_dict["current-python_requires"] = "Not Set (default >=2.7)"
    pyvers = set(parse_comp_expr(comp_expr, config.PY_VERSIONS))

    custom_modules = find_custom_modules(root_path)

    if not custom_modules:
        print(f"Source code of the package not found, skip checking Use Incompatible Features")

    final_pyvers=detect_all_local_comp(root_path,comp_info=pyvers,local_modules=custom_modules)
    if final_pyvers:
        final_pyvers=sorted_pyver_list(final_pyvers)
        suggestion=suggest_pyver(final_pyvers)
        incomp_feature_dict["suggest-python_requires"]=suggestion+"----origin"

    if has_inf:
        print_incompFeature(incomp_feature_dict)
        return True
    return False

# def detect_incomp_feature_usage_vermin(root_path,comp_expr=">=2.7"):
#     # root_path: project root path
#     # comp_expr: project original python_requires
#     global incomp_feature_dict
#     incomp_feature_dict["current-python_requires"] = comp_expr
#     if not comp_expr:
#         # set default python_requires
#         comp_expr = ">=2.7"
#         incomp_feature_dict["current-python_requires"] = "Not Set (default >=2.7)"
#     pyvers = set(parse_comp_expr(comp_expr, config.PY_VERSIONS))
#     minVers=get_minimum_versions(root_path)
#     final_pyvers=remove_versions(pyvers,minVers)
#     if len(final_pyvers)==len(pyvers):
#         return False
#     final_pyvers=sorted_pyver_list(final_pyvers)
#     if len(final_pyvers)>0:
#         suggestion=suggest_pyver(final_pyvers)
#         incomp_feature_dict["suggest-python_requires"] = suggestion+"----vermin"
#         print_incompFeature(incomp_feature_dict)
#     return True
#
#
# def detect_incomp_feature_usage_syntax_rule(root_path,comp_expr=">=2.7"):
#     # root_path: project root path
#     # comp_expr: project original python_requires
#     global incomp_feature_dict
#     incomp_feature_dict["current-python_requires"] = comp_expr
#     if not comp_expr:
#         # set default python_requires
#         comp_expr = ">=2.7"
#         incomp_feature_dict["current-python_requires"] = "Not Set (default >=2.7)"
#     pyvers = set(parse_comp_expr(comp_expr, config.PY_VERSIONS))
#     contraints=file_rule(root_path)
#     print(contraints)
#     final_pyvers=version_intersection(pyvers,contraints)
#     if len(final_pyvers)==len(pyvers):
#         return False
#     final_pyvers=sorted_pyver_list(final_pyvers)
#
#     if len(final_pyvers)>0:
#         suggestion=suggest_pyver(final_pyvers)
#         incomp_feature_dict["suggest-python_requires"] = suggestion+"----syntax_rule"
#         print_incompFeature(incomp_feature_dict)
#
#     return True
#


def detect_all_local_comp(root_path ,comp_info, local_modules):
    # path: root path of project
    # comp_info: declared compatible Python versions
    # local_modules: modules implement by the project itself
    # analysis: analyze setup.py first, and then analyze all local files whose modules are imported by setup.py

    pyfiles = list()
    parse_all_pyfiles(root_path, pyfiles)
    for pyfile in pyfiles:
        comp_info=use_incomp_feature(pyfile,root_path=root_path, comp_info=comp_info, local_modules=local_modules)
    return comp_info


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



def use_incomp_feature(path, root_path,**kwargs):
    # path: path of Python file
    # comp_info: declared compatible Python versions
    # local_modules: modules implement by the project itself
    global incomp_feature_dict,has_inf
    relative_path = path.replace(root_path, '.')
    comp_info = kwargs['comp_info'] if 'comp_info' in kwargs else config.PY_VERSIONS
    new_set = set()
    for version in comp_info:
        parts = version.split('.')
        new_version = '.'.join(parts[:2])
        new_set.add(new_version)
    comp_info=new_set

    local_modules = kwargs['local_modules'] if 'local_modules' in kwargs else set()
    top_levels = extract_top_levels(path)  # module features
    top_levels -= local_modules
    features = extract_feature(path)  # syntax features
    comp_info = find_comp_pyvers(top_levels, features,comp_info,relative_path)  # Python vers contain all top_levels and support all features
    if use_open_encoding_kwarg(path):  # open(encoding=...) -> Python 3
        if "2.7" in comp_info:
            incomp_feature_dict["position"].append(relative_path)
            incomp_feature_dict["specific"].append(f"feature: open(encoding=...) do not support python [2.7]")
            has_inf=True
    return comp_info
    #     comp_python -= {"2.7"}
    # difference = set(comp_info)-set(comp_python)
    # if len(difference):
    #     return True





def extract_feature(path):
    # match each line of code with regex
    matched_features = set()
    lines=preprocess_file(path)
    for line in lines:
        for feature in syntax_features.keys():
            line = line.strip()
            if feature in matched_features:
                continue
            pattern = re.compile(syntax_features[feature]["regex"])
            if pattern.search(line):
                matched_features.add(feature)
                break
    return matched_features


def extract_top_levels(path):
    # TODO: unify ast parse
    parser = ParserFactory.make_parser("top_level")
    with open(path , encoding="ISO-8859-1") as f:
        lines = f.readlines()
        code = "".join(lines)
        top_levels = parser.parse_modules_only_top(code)

    return top_levels


def find_comp_pyvers(modules, features,orig_comp_pyvers,path):
    # find Python versions containing all standard modules and supporting all features
    global incomp_feature_dict,has_inf
    comp_pyvers = set(config.PY_VERSIONS)
    for module in modules:
        if module not in std_modules:
            continue  # not a standard module, skip
        comp_pyvers = comp_pyvers.intersection(std_modules[module])
        difference = set(orig_comp_pyvers) - set(comp_pyvers)
        if len(difference):
            if orig_comp_pyvers-difference:
                #Todo : standard modules do not whole
                orig_comp_pyvers=orig_comp_pyvers-difference
                incomp_feature_dict["position"].append(path)
                incomp_feature_dict["specific"].append(f"module: <{module}> do not support python {[i for i in difference]}")
                has_inf = True
    for feature in features:
        comp_pyvers = comp_pyvers.intersection(syntax_features[feature]["pyver"])
        difference = set(orig_comp_pyvers) - set(comp_pyvers)
        if len(difference):
            orig_comp_pyvers = orig_comp_pyvers - difference
            incomp_feature_dict["position"].append(path)
            incomp_feature_dict["specific"].append(f"feature: <{feature}> do not support python {[i for i in difference]}")
            has_inf = True
    return orig_comp_pyvers


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
    try:
        func_name = get_func(expr, this_ast)  # full function name, e.g. module.submodule.function
        for candidate in candidates:
            if candidate in func_name:
                return False  # io.open or codecs.open
        if not func_name:
            return False
        parts = func_name.split(".")
        if "open" in parts:
            # 'in parts' but not '==parts[-1]', because of the form like open(...).read()
            return True
        return False
    except:
        return False

def use_open_encoding_kwarg(path):
    file = open(path , encoding="ISO-8859-1")
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

def remove_annotation_and_quotation(lines):

    in_annotation = False
    new_lines=list()
    for line in lines:
        # consider annotation
        if in_annotation==True:
            if '"""' in line:
                ind = line.index('"""')
                line = line[ind + 3:]
                in_annotation = False
            else:
                continue
        if len(line)>=6 and line.startswith('"""') and line.endswith('"""'):
            continue
        if '"""'in line:
            ind=line.index('"""')
            line=line[:ind]
            in_annotation = True
        if line.startswith('#'):
            continue
        # consider quotation
        # line = remove_quotation(line)
        if '#' in line:
            ind=line.index('#')
            line=line[:ind]

        if line == '':
            continue
        new_lines.append(line)

    return new_lines

def remove_quotation(line):
    temp = re.sub("\"([^\"]*)\"", '""', line)
    temp = re.sub("\'([^\']*)\'", '""', temp)
    return temp

def read_file_and_remove_strip(file_path):
    with open(file_path, 'r', encoding="ISO-8859-1") as f:
        lines = f.readlines()
        lines = ''.join(lines).strip('\n').splitlines()
        # remove blank lines
        lines = [l.strip() for l in lines if l != '']
        return lines

# def preprocess_file(file_path):
#     lines=read_file_and_remove_strip(file_path)
#     new_lines=remove_annotation_and_quotation(lines)
#     return new_lines
def preprocess_file(file_path):
    with open(file_path, 'r', encoding="ISO-8859-1") as f:
        code = f.read()

    tokens = tokenize.tokenize(BytesIO(code.encode('utf-8')).readline)

    new_code = []
    current_line = []

    last_lineno = -1
    for toktype, tokstring, start, end, _ in tokens:
        if toktype != tokenize.COMMENT:
            if start[0] != last_lineno:  # new line
                if current_line:  # if there are any tokens accumulated for previous line
                    new_code.append(" ".join(current_line))  # join them into a line and add to new_code
                current_line = []  # start a new line
            current_line.append(tokstring)  # add the token to current line
            last_lineno = start[0]  # update last_lineno

    if current_line:  # add the last line if it's not empty
        new_code.append(" ".join(current_line))

    return new_code

def print_incompFeature(results):
    console=rich_console()

    console.rule(f"[bold yellow]root cause 2: {results['cause']}")

    console.print("cause : ",results["cause"])
    console.print("current python_requires :",results["current-python_requires"])

    for i in range(len(results["position"])):
        console.print("-"*40,style="grey53")
        console.print("error file :",results['position'][i])
        console.print("specific cause :",results["specific"][i])

    console.print("-"*40,style="grey53")
    console.print(f"suggest python_requires : {results['suggest-python_requires']}")


def remove_versions(versions, version_to_compare):
    # 将版本号字符串转换为元组，以便进行比较
    versions = {tuple(map(int, version.split('.'))) for version in versions}
    version_to_compare = tuple(map(int, version_to_compare.split('.')))

    # 仅保留大于或等于指定版本号的版本
    versions = {version for version in versions if version >= version_to_compare}

    # 将版本号元组转换回字符串
    versions = {'.'.join(map(str, version)) for version in versions}

    return versions

import subprocess

def run_vermin(package_name):
    command = ["vermin", package_name]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def get_minimum_versions(root_path):
    output = run_vermin(root_path)
    match = re.search(r'Minimum required versions: (\d+\.\d+)', output)
    if match:
        version = match.group(1)
    else:
        version=2.7
    return str(version)

def version_intersection(versions, constraints):
    # 转换版本号为Version对象
    versions = {Version(v) for v in versions}
    # 初始化结果为所有版本
    intersected_versions = set(versions)

    for constraint in constraints:
        # 对于排除特定版本的情况，我们直接在结果中去掉对应的版本
        if constraint.startswith('!='):
            exclude_versions = constraint[2:].split(',')
            for v in exclude_versions:
                major, minor = v.split('.')[:2]
                # 处理通配符
                if minor.endswith('*'):
                    minor = minor[:-1]
                for version in versions:
                    if str(version.major) == major and str(version.minor).startswith(minor):
                        if version in intersected_versions:
                            intersected_versions.remove(version)
        # 对于其它情况，我们使用SpecifierSet进行过滤
        else:
            specifier_set = SpecifierSet(constraint)
            intersected_versions &= set(specifier_set.filter(versions))

    # 返回结果
    return {str(v) for v in intersected_versions}




if __name__ == '__main__':
    # rst=preprocess_file("/home/yhj/projects/PyChecker/code/pychecker/cache/amcrest-1.9.6/src/amcrest/utils.py")
    # for i in rst:
    #     print(i)
    # detect_incomp_feature_usage("/home/yhj/projects/PyChecker/code/pychecker/cache/amcrest-1.9.6")
    # 调用 vermin 命令并获取输出结果
    root_path="/home/yhj/projects/PyChecker/code/pychecker/cache/amcrest-1.9.6"
    # root_path="/home/yhj/projects/PyChecker/code/pychecker/cache/django-hijack-3.2.6"
    root_path="/home/yhj/projects/PyChecker/code/pychecker/cache/datadog-checks-dev-17.8.1"
    # root_path="/home/yhj/projects/PyChecker/code/pychecker/cache/zappa-0.54.0"
    # root_path="/home/yhj/projects/PyChecker/code/pychecker/cache/dask-jobqueue-0.7.2"
    file_path="/home/yhj/projects/PyChecker/code/pychecker/cache/amcrest-1.9.6/src/amcrest/utils.py"
    # detect_incomp_feature_usage(root_path)
    detect_incomp_feature_usage_vermin(root_path)
    detect_incomp_feature_usage_syntax_rule(root_path)
    # info=file_rule(root_path)
    # print(info)