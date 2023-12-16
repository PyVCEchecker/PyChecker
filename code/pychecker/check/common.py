import os
import ast as ast39
import time
from typed_ast import ast27
from collections import deque
from urllib import request
from compare_string_version import compareVersion
from pychecker import config
from rich.console import Console


def ast_parse(code):
    # ast related: refer to Python doc >> ast
    try:
        body = ast39.parse(code).body
        this_ast = ast39
    except SyntaxError:
        try:
            body = ast27.parse(code).body
            this_ast = ast27
        except SyntaxError:
            return None, None
    return body, this_ast


def parse_custom_modules(path):
    # extract modules implement by the project itself
    modules = list()
    filenames = os.listdir(path)
    for filename in filenames:
        fullpath = os.path.join(path, filename)
        if os.path.isdir(fullpath):
            subs = os.listdir(fullpath)
            if "__init__.py" not in subs:
                continue
            modules.append(filename)  # folder is a module
        elif filename.endswith(".py") or filename.endswith(".so"):
            if filename == "setup.py" or filename.startswith("__"):
                continue
            modules.append(filename.split(".")[0])  # py file or so file is a module

    return set(modules)


def parse_body(body, this_ast, local_modules, need_parse_func):
    for stmt in body:
        if stmt.__class__ == this_ast.Import:
            for alias in stmt.names:
                name = alias.name
                local_modules.add((name, 0))  # abs import, level=0
        elif stmt.__class__ == this_ast.ImportFrom:
            module = stmt.module
            names = {(f"{module}.{name.name}", stmt.level) for name in stmt.names}
            local_modules = local_modules.union(names)
        elif stmt.__class__ in [this_ast.For, this_ast.While, ast39.AsyncFor, this_ast.With, ast39.AsyncWith]:
            local_modules = parse_body(stmt.body, this_ast, local_modules, False)
        elif stmt.__class__ in [this_ast.FunctionDef, this_ast.ClassDef, ast39.AsyncFunctionDef] and need_parse_func:
            local_modules = parse_body(stmt.body, this_ast, local_modules, False)
        elif stmt.__class__ == this_ast.If:
            local_modules = parse_body(stmt.body, this_ast, local_modules, False)
            local_modules = parse_body(stmt.orelse, this_ast, local_modules, False)
        elif isinstance(stmt, ast39.Try) or isinstance(stmt, ast27.TryExcept):
            local_modules = parse_body(stmt.body, this_ast, local_modules, False)
            for handler in stmt.handlers:
                local_modules = parse_body(handler.body, this_ast, local_modules, False)
    return local_modules


def parse_local_import(code, local_tops, need_parse_func):
    modules = parse_import_modules(code, need_parse_func)
    # local_modules = {module for module in modules if module[0].split(".")[0] in local_tops}
    local_modules=list()
    for module in modules:
        if module[0].split(".")[0] in local_tops and module[1]==0:
            local_modules.append(module)
        elif module[1]>0:
            local_modules.append(module)



    return list(local_modules)


def parse_import_modules(code, need_parse_func):
    # extract all imported modules
    modules = set()  # {(module name, level), ...}
    body, this_ast = ast_parse(code)
    if not body:
        return set()
    modules = parse_body(body, this_ast, modules, need_parse_func)
    return modules


def parse_relative_import(modules, path, root):
    # modules: (name, level)
    imported_modules = set()
    for module, level in modules:
        if level == 0:
            imported_modules.add(module)
            continue
        while level > 0:
            temp_path = os.path.dirname(path)
            level-=1
        parent_path = temp_path.removeprefix(root)
        parent_module = parent_path.replace(os.sep, "")
        module = f"{parent_module}.{module}"
        imported_modules.add(module)

    return list(imported_modules)


def parse_local_path(modules, root, pyver=3.9):
    paths = set()
    for item in modules:
        module_path = os.sep.join(item.split("."))
        module_path = os.path.join(root, module_path)
        while module_path != root:
            if os.path.exists(module_path) and os.path.isdir(module_path):
                init_file_path = os.path.join(module_path, "__init__.py")
                if os.path.exists(init_file_path):
                    paths.add(init_file_path)
            else:
                module_path = module_path + ".py"
                if os.path.exists(module_path):
                    paths.add(module_path)
            if pyver < 3.3:
                break
            # Changed in Python 3.3: Parent packages are automatically imported.
            module_path = os.path.dirname(module_path)

    return paths

def parse_all_pyfiles(path,pyfiles):
    #obtain all python files in a project
    #path : top directory of project
    #pyfiles :an empty list at the first time.it will be a list of all python files in the end
    filenames=os.listdir(path)

    if "__init__.py" in filenames:
        for fname in filenames:
            if fname.endswith('.py'):
                fullpath=os.path.join(path,fname)
                pyfiles.append(fullpath)
    for filename in filenames:
        if "test" in filename:
            continue
        fullpath = os.path.join(path, filename)
        if filename=="setup.py":
            pyfiles.append(fullpath)
        elif os.path.isdir(fullpath):
            parse_all_pyfiles(fullpath,pyfiles)

def analysis(path, func, **kwargs):
    # path: path of "setup.py"
    # if the file<path> satisfies some attributes<func>, return True immediately
    # else visit its imported local files, and check the attributes
    root = os.path.dirname(path)
    local_tops = parse_custom_modules(root)
    targets = deque([path])
    is_setup = True
    visited = set()
    while targets:
        kwargs |= {"is_setup": is_setup}  # is_setup = True only at the first time (parse setup.py)
        path = targets.popleft()
        visited.add(path)
        file = open(path , encoding="ISO-8859-1")
        code = "".join(file.readlines())
        file.close()
        if func(path, **kwargs):  # analyze current file
            return True,path
        # analyze imported local modules
        imported_local_modules = parse_local_import(code, local_tops, is_setup)
        #if source is whl ,and checking runtime error,'root' need change to its father path
        setup_path=os.path.join(root,"setup.py")
        if not os.path.exists(setup_path):
            root=os.path.dirname(root)
        imported_local_modules = parse_relative_import(imported_local_modules, path, root)
        # find local modules' files, add then to visit queue
        new_paths = parse_local_path(imported_local_modules, root)
        for new_path in new_paths:
            if new_path in visited:
                continue
            targets.append(new_path)
        is_setup = False
    return False,None


def analysis_fix(path, func, **kwargs):
    # path: path of "setup.py"
    # if the file<path> satisfies some attributes<func>, return True immediately
    # else visit its imported local files, and check the attributes
    root = os.path.dirname(path)
    local_tops = parse_custom_modules(root)
    targets = deque([path])
    is_setup = True
    visited = set()
    incomp = False
    comp_py_versions = {x for x in config.PY_VERSIONS}
    while targets:
        kwargs |= {"is_setup": is_setup}  # is_setup = True only at the first time (parse setup.py)
        path = targets.popleft()
        visited.add(path)
        file = open(path)
        code = "".join(file.readlines())
        file.close()
        result, comp_info = func(path, **kwargs)  # analyze current file
        incomp = incomp or result  # if result == True, then incomp = True
        comp_py_versions = comp_py_versions.intersection(comp_info)
        # analyze imported local modules
        imported_local_modules = parse_local_import(code, local_tops, is_setup)
        # if source is whl ,and checking runtime error,'root' need change to its father path
        setup_path = os.path.join(root, "setup.py")
        if not os.path.exists(setup_path):
            root = os.path.dirname(root)
        imported_local_modules = parse_relative_import(imported_local_modules, path, root)
        # find local modules' files, add then to visit queue
        new_paths = parse_local_path(imported_local_modules, root)
        for new_path in new_paths:
            if new_path in visited:
                continue
            targets.append(new_path)
        is_setup = False
    return incomp, comp_py_versions



def parse_func_params(body, this_ast, func_name, analysis_func, candidates):
    params = None
    if body is None:
        return None
    for node in body:
        if isinstance(node, this_ast.If):
            params = parse_func_params(node.body, this_ast, func_name, analysis_func, candidates)
            if not params:
                params = parse_func_params(node.orelse, this_ast, func_name, analysis_func, candidates)
        elif isinstance(node, this_ast.Expr):
            params = parse_func_params_expr(node.value, this_ast, func_name, analysis_func, candidates)
        elif isinstance(node, this_ast.FunctionDef):
            params = parse_func_params(node.body, this_ast, func_name, analysis_func, candidates)
        elif isinstance(node, this_ast.Assign):
            params = parse_func_params_expr(node.value, this_ast, func_name, analysis_func, candidates)
        elif isinstance(node, this_ast.Return):
            params = parse_func_params_expr(node.value, this_ast, func_name, analysis_func, candidates)
        elif isinstance(node, ast39.Try) or isinstance(node, ast27.TryExcept):
            params = parse_func_params(node.body, this_ast, func_name, analysis_func, candidates)
            if not params:
                params = parse_func_params(node.orelse, this_ast, func_name, analysis_func, candidates)
        elif isinstance(node, this_ast.With):
            if this_ast == ast39:
                for item in node.items:
                    params = parse_func_params_expr(item.context_expr, this_ast, func_name, analysis_func, candidates)
                    if params:
                        break
            else:
                params = parse_func_params_expr(node.context_expr, this_ast, func_name, analysis_func, candidates)
            if not params:
                params = parse_func_params(node.body, this_ast, func_name, analysis_func, candidates)
        if params:
            return params
    return None


def parse_func_params_expr(expr, this_ast, func_name, analysis_func, candidates):
    open_params = None
    if isinstance(expr, this_ast.Call) and analysis_func(expr.func, this_ast, candidates):
        open_params = get_kwarg_params(expr, this_ast, func_name)

    return open_params


def get_kwarg_params(node, this_ast, func_name):
    if isinstance(node, this_ast.Call):
        func = node.func
        if isinstance(func, this_ast.Attribute) and func.attr == func_name:
            return node.keywords
        if isinstance(func, this_ast.Name) and func.id == func_name:
            return node.keywords
        return get_kwarg_params(node.func, this_ast, func_name)
    if isinstance(node, this_ast.Attribute):
        attr = node.attr
        if attr == func_name:
            return node.keywords
        return get_kwarg_params(node.value, this_ast, func_name)

    return None


def get_func(node, this_ast):
    if isinstance(node, this_ast.Call):
        return get_func(node.func, this_ast)
    if isinstance(node, this_ast.Attribute):
        attr = node.attr
        name = get_func(node.value, this_ast)
        func = f"{name}.{attr}"
        return func
    if isinstance(node, this_ast.Name):
        return node.id
    return None


def crawl_content(url, retries=3):
    for _ in range(retries):
        try:
            response = request.urlopen(url, timeout=10)
            content = response.read()
            return content
        except Exception:
            # print(url,"cral_content failed")
            time.sleep(0.1)
    return None


def compare_version(v1, v2):
    try:
        result = compareVersion(v1, v2)
    except:
        return 0
    if "less than" in result:
        return -1
    if "greater than" in result:
        return 1
    return 0


def find_custom_modules(path):
    dirs = os.listdir(path)
    meta_dirs = list(filter(lambda x: x.endswith("-info"), dirs))
    if len(meta_dirs) != 1 and "src" in dirs:
        src_path=os.path.join(path,"src")
        src_dirs=os.listdir(src_path)
        meta_dirs=list(filter(lambda x: x.endswith("-info"),src_dirs))
        if len(meta_dirs)==1:
            path=src_path
    if len(meta_dirs) != 1:
        return parse_custom_modules(path)
    meta_dir = meta_dirs[0]
    top_level = os.path.join(path, meta_dir, "top_level.txt")
    if not os.path.exists(top_level):
        return parse_custom_modules(path)
    with open(top_level) as f:
        lines = f.readlines()
    modules = set(map(lambda x: x.strip(), lines))
    return modules

def sorted_pyver_list(verL):
    verL = list(verL)
    verL.sort()
    if "3.10" in verL:
        verL.pop(verL.index("3.10"))
        verL.append("3.10")
    return verL


def suggest_pyver(version_list,removed_versions=None):
    # suggest appropriate python version expression
    sug_expr = f">={version_list[0]}"
    all_versions = config.PY_VERSIONS
    if version_list[0] in all_versions:
        inx = all_versions.index(version_list[0])
    else:
        # eg: version_list[0]==3.6.1
        big_ver = version_list[0][0:3]
        inx = all_versions.index(big_ver) + 1
    for ver_inx in range(inx, len(all_versions)):
        if all_versions[ver_inx] not in version_list:
            sug_expr = sug_expr + f",!={all_versions[ver_inx]}"
    if removed_versions:
        for version in removed_versions:
            if compare_version(version,version_list[0])>0:
                sug_expr = sug_expr+f",!={version}"

    return sug_expr

def rich_console():
    console=Console(color_system="auto")
    return console

