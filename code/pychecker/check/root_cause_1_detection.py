from pychecker.check.analysis_setup_params import analysis_setup_python_requires
from pychecker.check.analysis_version_info_usage import analysis_sys_version_info
from pychecker.check.common import analysis,rich_console
import os
local_comp_dict=dict()
incomp_feature_dict=dict()
incomp_feature_dict["cause"]="using incompatible feature"
incomp_feature_dict["current-python_requires"]="Not Set (default: >=2.7)"
incomp_feature_dict["position"]=[]
incomp_feature_dict["specific"]=[]
incomp_feature_dict["repair_suggestion"]=[]

has_loc=False
def detect_local_comp_detection(path):
    global has_loc,incomp_feature_dict
    incomp_feature_dict = dict()
    incomp_feature_dict["cause"] = "using incompatible feature"
    incomp_feature_dict["current-python_requires"] = "Not Set (default: >=2.7)"
    incomp_feature_dict["position"] = []
    incomp_feature_dict["specific"] = []
    incomp_feature_dict["repair_suggestion"] = []

    has_loc = False
    file = open(path , encoding="ISO-8859-1")
    code = "".join(file.readlines())
    file.close()
    python_requires = analysis_setup_python_requires(code)
    use_sys_version_info,abspath = analysis(path, analysis_sys_version_info)
    if use_sys_version_info and not python_requires:
        root_path = os.path.dirname(path)
        relative_path = abspath.replace(root_path, ".")
        has_loc=True
        # 1. sys.version_info is used in comparison expressions
        # 2. setup() function does not have the param 'python_requires'
        incomp_feature_dict["position"].append(relative_path)
        incomp_feature_dict["specific"].append('''using hard-code Python version checking instead of configurating "python_requires"''')
        incomp_feature_dict["repair_suggestion"].append(
            "set\n\'\'\'\nsetup(\n\tpython_requires = _____\n)\n\'\'\'\nin setup.py"
        )
        print_locComp(incomp_feature_dict)
        return True
    return False

def print_locComp(results):
    console = rich_console()
    console.rule(f"[bold yellow]root cause 1: {results['cause']}")
    for key,value in results.items():
        if key=="repair_suggestion":
            console.print('-'*40,style="grey53")
            console.print("repair suggestion :",value[0])
            continue
        if type(value) != type(list()):
            console.print(f"{key} :{value}")
        else:
            console.print(f"{key} :{value[0]}")

