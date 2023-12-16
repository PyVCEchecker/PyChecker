from pychecker.check.common import ast_parse

def parse_importfrom(node):
    module = node.module
    if module != "sys":
        return False
    names = node.names
    for name in names:
        if name.name == "version_info":
            return True
    return False


def parse_import(node):
    names = node.names
    for name in names:
        if name.name == "sys":
            return True
    return False


def parse_id(node, this_ast):
    if isinstance(node, this_ast.Constant):
        return None
    if isinstance(node, this_ast.Subscript):
        return parse_id(node.value, this_ast)
    if isinstance(node, this_ast.Attribute):
        attr = node.attr
        name = parse_id(node.value, this_ast)
        return f"{name}.{attr}"
    if isinstance(node, this_ast.Name):
        return node.id


def parse_expr(expr, version_info_ids, this_ast):
    if isinstance(expr, this_ast.Compare):
        id = parse_id(expr.left, this_ast)
        if id in version_info_ids:
            return True
        for item in expr.comparators:
            id = parse_id(item, this_ast)
            if id in version_info_ids:
                return True
        return False
    if isinstance(expr, this_ast.BoolOp):
        for value in expr.values:
            if parse_expr(value, version_info_ids, this_ast):
                return True
    if isinstance(expr, this_ast.UnaryOp):
        if parse_expr(expr.operand,version_info_ids,this_ast):
            return True
    return False


def parse_stmt(node, version_info_ids, this_ast):
    if isinstance(node, this_ast.Assign):
        return parse_expr(node.value, version_info_ids, this_ast)
    if isinstance(node, this_ast.If):
        if parse_expr(node.test, version_info_ids, this_ast):
            if parse_if_context(node, this_ast):
                # TODO: Something should be done for other cases?
                # if the program not raises error or not exits in if-body, it should not be considered further
                return True
        if parse_body(node.body, version_info_ids, this_ast):
            return True
        if parse_body(node.orelse, version_info_ids, this_ast):
            return True
    if isinstance(node, this_ast.Expr):
        return parse_expr(node.value, version_info_ids, this_ast)
    return False


def parse_if_context(if_node, this_ast):
    for node in if_node.body:
        if is_finish_stmt(node, this_ast):
            return True
    for node in if_node.orelse:
        if is_finish_stmt(node, this_ast):
            return True
    return False


def is_finish_stmt(node, this_ast):
    # raise, return, exit
    if isinstance(node, this_ast.Raise) or isinstance(node, this_ast.Return):
        return True
    if isinstance(node, this_ast.Expr):
        value = node.value
        if not isinstance(value, this_ast.Call):
            return False
        func = value.func
        # semantic analysis
        if isinstance(func, this_ast.Name) and "exit" in func.id:
            return True
        if isinstance(func, this_ast.Attribute) and "exit" in func.attr:
            return True
    return False


def parse_body(body, version_info_ids, this_ast):
    # whether sys.version_info is used in comparison expressions
    # ast related: refer to Python doc >> ast
    for node in body:
        try:
            if parse_stmt(node, version_info_ids, this_ast):
                return True
        except:
            print("there is an error in parse_body")
            return False
    return False


def analysis_sys_version_info(path, **kwargs):
    with open(path , encoding="ISO-8859-1") as f:
        code = "".join(f.readlines())
    # root = ast.parse(code)
    body, this_ast = ast_parse(code)
    # sys.version_info candidates
    # import sys -> candidate: sys.version_info
    # from sys import version_info -> candidate: version_info
    # TODO: refactor with functions in common
    version_info_ids = list()
    if body is None:
        return False
    for node in body:
        if isinstance(node, this_ast.Import):
            sys_used = parse_import(node)
            if sys_used:
                version_info_ids.append("sys.version_info")
        if isinstance(node, this_ast.ImportFrom):
            version_info_used = parse_importfrom(node)
            if version_info_used:
                version_info_ids.append("version_info")

    if not version_info_ids:
        return False  # sys is not imported

    return parse_body(body, version_info_ids, this_ast)
