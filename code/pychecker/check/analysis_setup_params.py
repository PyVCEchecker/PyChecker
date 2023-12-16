from pychecker.check.common import ast_parse, parse_import_modules, parse_func_params, get_func


def find_setup_candidates(code):
    modules = parse_import_modules(code, True)
    modules = [module[0] for module in modules]
    candidates = list()
    if "setuptools" in modules:
        # import setuptools -> candidate: setuptools.setup
        candidates.append("setuptools.setup")
    if "setuptools.setup" in modules:
        # from setuptools import setup -> candidate: setup
        candidates.append("setup")
    return candidates


def is_setup_call(expr, this_ast, candidates):
    if isinstance(expr, this_ast.Attribute) or isinstance(expr, this_ast.Name):
        func_name = get_func(expr, this_ast)
        if func_name in candidates:
            return True
    return False


def analysis_setup_python_requires(code):
    body, this_ast = ast_parse(code)

    candidates = find_setup_candidates(code)
    if not candidates:
        return False  # setuptools is not imported, skip

    # 1. whether setup function is used; 2. if so, extract its keyword params.
    setup_params = parse_func_params(body, this_ast, "setup", is_setup_call, candidates)
    if not setup_params:
        return False  # setup is not used

    for param in setup_params:
        if not param.arg:
            pass
        if param.arg == "python_requires":
            return True
    return False
