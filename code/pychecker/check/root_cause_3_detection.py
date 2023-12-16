from functools import cmp_to_key
from pychecker.check.visit_pypi import get_metadata, get_pkg_versions, DEPS, COMP
from pychecker.check.common import compare_version, suggest_pyver, sorted_pyver_list, rich_console
from pychecker import config

# global
suggest_pyvers = config.PY_VERSIONS
no_avl_resource_dict = dict()
no_avl_resource_dict["cause"] = "python version conflict"
no_avl_resource_dict["current-python_requires"] = ""
no_avl_resource_dict["all_dependencies"] = ""
no_avl_resource_dict["position"] = []
no_avl_resource_dict["suggest-python_requires"] = ""

has_nar = False
removed_versions = list()


def detect_no_avl_resource_pkg(pkg, ver):
    global no_avl_resource_dict,has_nar
    no_avl_resource_dict = dict()
    no_avl_resource_dict["cause"] = "python version conflict"
    no_avl_resource_dict["current-python_requires"] = ""
    no_avl_resource_dict["all_dependencies"] = ""
    no_avl_resource_dict["position"] = []
    no_avl_resource_dict["suggest-python_requires"] = ""

    has_nar = False
    metadata = get_metadata(pkg, ver)
    if not metadata:
        return False
    dep_exprs = metadata[DEPS]
    comp_expr = metadata[COMP]
    visited_lower = {f"{pkg}#{ver}"}
    visited_upper = {f"{pkg}#{ver}"}
    return detect_no_avl_resource(comp_expr, dep_exprs, visited_lower, visited_upper)


def detect_no_avl_resource(comp_expr, dep_exprs, visited_lower=None, visited_upper=None):
    # Algorithm 1
    # comp_expr: python_requires
    # dep_exprs: install_requires
    # visited_*: package-versions already visited. Avoid repeated visits and circulate visits.
    global no_avl_resource_dict, has_nar, suggest_pyvers, removed_versions
    if not comp_expr:
        no_avl_resource_dict["current-python_requires"] = "Not Set (default >=2.7)"
    else:
        no_avl_resource_dict["current-python_requires"] = comp_expr
    no_avl_resource_dict["all_dependencies"] = dep_exprs
    comp_info = parse_comp_expr(comp_expr, config.PY_VERSIONS)
    comp_info = sorted(comp_info, key=cmp_to_key(compare_version))
    if comp_info:
        suggest_pyvers = comp_info
    if not visited_lower:
        visited_lower = set()
    if not visited_upper:
        visited_upper = set()
    for expr in dep_exprs:
        dep, lower, upper = parse_dep_expr(expr)
        if not dep:
            continue
        if not lower_comp(dep, lower, comp_info[0], visited_lower):
            # check whether oldest versions of deps are compatible with the oldest Python version
            # pass  # uncomment this line and comment the next line to get the full problem domain
            # print(dep,"  lower:  ",lower)
            has_nar = True
        if not upper_comp(dep, upper, comp_info[-1], visited_upper):
            # check whether latest versions of deps are compatible with the latest Python version
            # pass  # uncomment this line and comment the next line to get the full problem domain
            # print(dep,"  upper:  ",upper)
            has_nar = True
    if has_nar == True:
        removed_versions=list(set(removed_versions))

        no_avl_resource_dict["suggest-python_requires"] = suggest_pyver(suggest_pyvers, removed_versions)
        print_pyVerConf(no_avl_resource_dict)
        return True
    else:
        return False


def lower_comp(pkg, ver, pyver, visited, parents=""):
    # Algorithm 2
    global no_avl_resource_dict, has_nar, suggest_pyvers
    metadata = get_metadata(pkg, ver)
    if not metadata:
        return True  # failed to locate the package-version, skip.
    dep_exprs = metadata[DEPS]
    comp_expr = metadata[COMP]
    comp_info = parse_comp_expr(comp_expr, config.PY_VERSIONS)
    comp_info = sorted(comp_info, key=cmp_to_key(compare_version))
    if compare_version(pyver,comp_info[0])<0:
        no_avl_resource_dict["position"].append(f"{parents}{pkg}|python_requires='{comp_expr}'")
        difference = set(suggest_pyvers) - set(comp_info)
        if len(difference):

            if comp_info[0].count('.') == 2 and compare_version(comp_info[0], suggest_pyvers[0]) > 0:
                # handle sub-version condition
                suggest_pyvers.append(comp_info[0])
                suggest_pyvers = sorted_pyver_list(suggest_pyvers)
            for dif in difference:
                if dif.count('.') == 2:
                    # if "3.6.1" do
                    if compare_version(dif, comp_info[0]) < 0:
                        suggest_pyvers.remove(dif)
                else:
                    suggest_pyvers.remove(dif)
        return False  # current package-version is not compatible with pyver
    visited.add(f"{pkg}#{ver}")  # marked as visited

    for expr in dep_exprs:
        dep, lower, _ = parse_dep_expr(expr)
        if not dep:
            continue
        pkgver = f"{dep}#{lower}"
        if pkgver in visited:
            continue  # prevent circuit
        if not lower_comp(dep, lower, pyver, visited, parents=f"{parents}{pkg}->"):
            return False  # a transitive dependency is not compatible with pyver
    return True  # compatible


def upper_comp(pkg, ver, pyver, visited, parents=""):
    # Algorithm 2'
    global no_avl_resource_dict, has_nar, suggest_pyvers
    metadata = get_metadata(pkg, ver)
    if not metadata:
        return True
    dep_exprs = metadata[DEPS]
    comp_expr = metadata[COMP]
    comp_info = parse_comp_expr(comp_expr, config.PY_VERSIONS)
    comp_info = sorted(comp_info, key=cmp_to_key(compare_version))
    if compare_version(pyver, comp_info[-1]) > 0:
        no_avl_resource_dict["position"].append(f"{parents}{pkg}|python_requires='{comp_expr}'")
        difference = set(suggest_pyvers) - set(comp_info)
        if len(difference):
            for dif in difference:
                suggest_pyvers.remove(dif)
        return False
    visited.add(f"{pkg}#{ver}")
    for expr in dep_exprs:
        dep, _, upper = parse_dep_expr(expr)
        if not dep:
            continue
        pkgver = f"{dep}#{upper}"
        if pkgver in visited:
            continue  # prevent circuit
        if not upper_comp(dep, upper, pyver, visited, parents=f"{parents}{pkg}->"):
            # print(pkgver)
            return False
    return True


def parse_comp_expr(expr, versions):


    # comp_expr: condition1, condition2, ...
    # condition: symbol version
    # symbol: >= | <= | > | < | == | != | ~=
    this_versions = versions[:]
    conditions = expr.split(",")
    symbols = [">=", "<=", ">", "<", "==", "!=", "~="]
    satisfied_versions = list()
    global removed_versions
    # filter versions that satisfy all conditions
    for condition in conditions:
        for symbol in symbols:
            # suggest pyvers
            if symbol in condition:
                compare_to_version = condition.replace(symbol, "").strip()
                if symbol == "!=" and compare_to_version.count(r".") == 2 and (r'.*' not in compare_to_version):
                    # handle conditions like : "!=3.6.1"
                    removed_versions.append(compare_to_version)
                # handle conditions like: !=3.0.* ,!=3.7.*
                if r'.*' in compare_to_version:
                    compare_to_version=compare_to_version.replace(r".*", "")
                if compare_to_version not in this_versions:
                    this_versions.append(compare_to_version)
                break

    for version in this_versions:
        satisfied = True
        for condition in conditions:
            if not judge_condition(version, condition):
                satisfied = False
                break
        if satisfied:
            satisfied_versions.append(version)
    return satisfied_versions


def parse_dep_expr(expr):
    # dep_expr: pkg[option] (comp_expr) [; condition] | pkg[option] comp_expr [; condition]
    dep, expr = split_dep_expr(expr)
    if dep:
        dep = dep.strip()
    if not dep:
        return None, None, None
    if dep == 'pytz':
        return None, None, None
    versions = get_pkg_versions(dep)
    if not versions:
        return None, None, None
    comp_versions = parse_comp_expr(expr, versions)
    comp_versions = sorted(comp_versions, key=cmp_to_key(compare_version))
    if len(comp_versions) == 0:
        print(dep, expr, "what happened")  # what happened?
        return None, None, None
    return dep, comp_versions[0], comp_versions[-1]


def split_dep_expr(expr):
    if ";" in expr:
        return None, None  # conditional dependency, not consider now
    try:
        # pkg[option] (comp_expr)
        condition_start = expr.index("(")
        condition_end = expr.index(")")
    except ValueError:
        # pkg[option] comp_expr
        condition_start = len(expr)
        condition_end = condition_start
    dep = expr[:condition_start].strip()
    try:
        # pkg[option]
        option_start = dep.index("[")
        dep = dep[:option_start].strip()
    except ValueError:
        pass
    condition = expr[condition_start:condition_end].strip()
    condition = condition.removeprefix("(").removesuffix(")")

    symbols = [">=", "<=", ">", "<", "==", "!=", "~="]
    this_symbol = None
    for symbol in symbols:
        try:
            condition_start = dep.index(symbol)
            this_symbol = symbol
        except ValueError:
            continue
    if this_symbol:
        condition = dep[condition_start:]
        dep = dep[:condition_start]

    return dep, condition


def judge_condition(version, condition):
    symbols = [">=", "<=", ">", "<", "==", "!=", "~="]
    # extract symbol in condition
    this_symbol = None
    for symbol in symbols:
        try:
            condition.index(symbol)
            this_symbol = symbol
            break
        except ValueError:
            continue
    if not this_symbol:
        return True  # condition = "", return True

    # the left in condition is version
    compare_to_version = condition.replace(this_symbol, "").strip()
    compare_to_version = compare_to_version.replace("'", "").replace('"', '')
    if this_symbol == "~=":
        this_symbol = ">="

    # TODO: replace eval with if-else
    if "*" not in compare_to_version:
        # print(f"compare_version('{version}', '{compare_to_version}') {this_symbol} 0")
        return eval(f"compare_version('{version}', '{compare_to_version}') {this_symbol} 0")

    else:
        # handle *
        aster_ind = compare_to_version.index("*")
        compare_to_version = compare_to_version[:aster_ind]
        tmp_version = version + "."
        if this_symbol == "==":
            return tmp_version.startswith(compare_to_version)
        if this_symbol == "!=":
            return not tmp_version.startswith(compare_to_version)
        if this_symbol == ">" or this_symbol == ">=":
            return eval(f"compare_version('{tmp_version}', '{compare_to_version}') {this_symbol} 0")

    print(version, condition, "what happened")  # what happened?
    return True


def print_pyVerConf(results):
    console = rich_console()
    console.rule(f"[bold yellow]root cause 3: {results['cause']}")
    console.print("cause : ", results["cause"])
    console.print("current python_requires :", results["current-python_requires"])
    console.print("all dependencies :")
    for dependency in results['all_dependencies']:
        console.print("  ", dependency)
    console.print("all conflict dependencies :")
    for dependency in results['position']:
        console.print("  ", dependency)
    console.print('-' * 40, style="grey53")
    console.print("suggest python_requires :", results["suggest-python_requires"])



