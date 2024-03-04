"""Amalgamation of xonsh.prompt package, made up of the following modules, in order:

* cwd
* env
* gitstatus
* job
* times
* vc
* base

"""

from sys import modules as _modules
from types import ModuleType as _ModuleType
from importlib import import_module as _import_module


class _LazyModule(_ModuleType):

    def __init__(self, pkg, mod, asname=None):
        '''Lazy module 'pkg.mod' in package 'pkg'.'''
        self.__dct__ = {
            'loaded': False,
            'pkg': pkg,  # pkg
            'mod': mod,  # pkg.mod
            'asname': asname,  # alias
            }

    @classmethod
    def load(cls, pkg, mod, asname=None):
        if mod in _modules:
            key = pkg if asname is None else mod
            return _modules[key]
        else:
            return cls(pkg, mod, asname)

    def __getattribute__(self, name):
        if name == '__dct__':
            return super(_LazyModule, self).__getattribute__(name)
        dct = self.__dct__
        mod = dct['mod']
        if dct['loaded']:
            m = _modules[mod]
        else:
            m = _import_module(mod)
            glbs = globals()
            pkg = dct['pkg']
            asname = dct['asname']
            if asname is None:
                glbs[pkg] = m = _modules[pkg]
            else:
                glbs[asname] = m
            dct['loaded'] = True
        return getattr(m, name)

#
# cwd
#
# -*- coding: utf-8 -*-
"""CWD related prompt formatter"""

os = _LazyModule.load('os', 'os')
shutil = _LazyModule.load('shutil', 'shutil')
xt = _LazyModule.load('xonsh', 'xonsh.tools', 'xt')
xp = _LazyModule.load('xonsh', 'xonsh.platform', 'xp')
from xonsh.built_ins import XSH


def _replace_home(x):
    if xp.ON_WINDOWS:
        home = XSH.env["HOMEDRIVE"] + XSH.env["HOMEPATH"][0]
        if x.startswith(home):
            x = x.replace(home, "~", 1)

        if XSH.env.get("FORCE_POSIX_PATHS"):
            x = x.replace(os.sep, os.altsep)

        return x
    else:
        home = XSH.env["HOME"]
        if x.startswith(home):
            x = x.replace(home, "~", 1)
        return x


def _replace_home_cwd():
    return _replace_home(XSH.env["PWD"])


def _collapsed_pwd():
    sep = xt.get_sep()
    pwd = _replace_home_cwd().split(sep)
    size = len(pwd)
    leader = sep if size > 0 and len(pwd[0]) == 0 else ""
    base = [
        i[0] if ix != size - 1 and i[0] != "." else i[0:2] if ix != size - 1 else i
        for ix, i in enumerate(pwd)
        if len(i) > 0
    ]
    return leader + sep.join(base)


def _dynamically_collapsed_pwd():
    """Return the compact current working directory.  It respects the
    environment variable DYNAMIC_CWD_WIDTH.
    """
    original_path = _replace_home_cwd()
    target_width, units = XSH.env["DYNAMIC_CWD_WIDTH"]
    elision_char = XSH.env["DYNAMIC_CWD_ELISION_CHAR"]
    if target_width == float("inf"):
        return original_path
    if units == "%":
        cols, _ = shutil.get_terminal_size()
        target_width = (cols * target_width) // 100
    sep = xt.get_sep()
    pwd = original_path.split(sep)
    last = pwd.pop()
    remaining_space = target_width - len(last)
    # Reserve space for separators
    remaining_space_for_text = remaining_space - len(pwd)
    parts = []
    for i in range(len(pwd)):
        part = pwd[i]
        part_len = int(
            min(len(part), max(1, remaining_space_for_text // (len(pwd) - i)))
        )
        remaining_space_for_text -= part_len
        if len(part) > part_len:
            reduced_part = part[0 : part_len - len(elision_char)] + elision_char
            parts.append(reduced_part)
        else:
            parts.append(part)
    parts.append(last)
    full = sep.join(parts)
    truncature_char = elision_char if elision_char else "..."
    # If even if displaying one letter per dir we are too long
    if len(full) > target_width:
        # We truncate the left most part
        full = truncature_char + full[int(-target_width) + len(truncature_char) :]
        # if there is not even a single separator we still
        # want to display at least the beginning of the directory
        if full.find(sep) == -1:
            full = (truncature_char + sep + last)[
                0 : int(target_width) - len(truncature_char)
            ] + truncature_char
    return full

#
# env
#
# -*- coding: utf-8 -*-
"""Prompt formatter for virtualenv and others"""

# amalgamated os
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.platform
def find_env_name():
    """Finds the current environment name from $VIRTUAL_ENV or
    $CONDA_DEFAULT_ENV if that is set.
    """
    env_path = XSH.env.get("VIRTUAL_ENV", "")
    if len(env_path) == 0 and xp.ON_ANACONDA:
        env_path = XSH.env.get("CONDA_DEFAULT_ENV", "")
    env_name = os.path.basename(env_path)
    return env_name


def env_name():
    """Returns the current env_name if it non-empty, surrounded by the
    ``{env_prefix}`` and ``{env_postfix}`` fields.
    """
    env_name = find_env_name()
    if XSH.env.get("VIRTUAL_ENV_DISABLE_PROMPT") or not env_name:
        # env name prompt printing disabled, or no environment; just return
        return

    venv_prompt = XSH.env.get("VIRTUAL_ENV_PROMPT")
    if venv_prompt is not None:
        return venv_prompt
    else:
        pf = XSH.shell.prompt_formatter
        pre = pf._get_field_value("env_prefix")
        post = pf._get_field_value("env_postfix")
        return pre + env_name + post


def vte_new_tab_cwd():
    """This prints an escape sequence that tells VTE terminals the hostname
    and pwd. This should not be needed in most cases, but sometimes is for
    certain Linux terminals that do not read the PWD from the environment
    on startup. Note that this does not return a string, it simply prints
    and flushes the escape sequence to stdout directly.
    """
    env = XSH.env
    t = "\033]7;file://{}{}\007"
    s = t.format(env.get("HOSTNAME"), env.get("PWD"))
    print(s, end="", flush=True)

#
# gitstatus
#
# -*- coding: utf-8 -*-
"""Informative git status prompt formatter"""
# amalgamated os
subprocess = _LazyModule.load('subprocess', 'subprocess')
# amalgamated from xonsh.built_ins import XSH
from xonsh.color_tools import COLORS
from xonsh.tools import NamedConstantMeta, XAttr


def _check_output(*args, **kwargs) -> str:
    denv = XSH.env.detype()
    denv.update({"GIT_OPTIONAL_LOCKS": "0"})

    kwargs.update(
        dict(
            env=denv,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            universal_newlines=True,
        )
    )
    timeout = XSH.env["VC_BRANCH_TIMEOUT"]
    # See https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate
    with subprocess.Popen(*args, **kwargs) as proc:
        try:
            out, err = proc.communicate(timeout=timeout)
            if proc.returncode != 0:
                raise subprocess.CalledProcessError(
                    proc.returncode, proc.args, output=out, stderr=err
                )  # note err will always be empty as we redirect stderr to DEVNULL abvoe
            return out
        except subprocess.TimeoutExpired:
            # We use `.terminate()` (SIGTERM) instead of `.kill()` (SIGKILL) here
            # because otherwise we guarantee that a `.git/index.lock` file will be
            # left over, and subsequent git operations will fail.
            # We don't want that.
            # As a result, we must rely on git to exit properly on SIGTERM.
            proc.terminate()
            # We wait() to ensure that git has finished before the next
            # `gitstatus` prompt is rendered (otherwise `index.lock` still exists,
            # and it will fail).
            # We don't technically have to call `wait()` here as the
            # `with subprocess.Popen()` context manager above would do that
            # for us, but we do it to be explicit that waiting is being done.
            proc.wait()  # we ignore what git says after we sent it SIGTERM
            raise


class _DEFS(metaclass=NamedConstantMeta):
    HASH_INDICATOR = XAttr(":")
    BRANCH = XAttr("{CYAN}")
    OPERATION = XAttr("{CYAN}")
    STAGED = XAttr("{RED}●")
    CONFLICTS = XAttr("{RED}×")
    CHANGED = XAttr("{BLUE}+")
    DELETED = XAttr("{RED}-")
    UNTRACKED = XAttr("…")
    STASHED = XAttr("⚑")
    CLEAN = XAttr("{BOLD_GREEN}✓")
    AHEAD = XAttr("↑·")
    BEHIND = XAttr("↓·")
    LINES_ADDED = XAttr("{BLUE}+")
    LINES_REMOVED = XAttr("{RED}-")


def _get_def(attr: XAttr) -> str:
    key = attr.name.upper()
    def_ = XSH.env.get("XONSH_GITSTATUS_" + key)
    return def_ if def_ is not None else attr.value


def _is_hidden(attr: XAttr) -> bool:
    hidden = XSH.env.get("XONSH_GITSTATUS_FIELDS_HIDDEN") or set()
    return attr.name.upper() in hidden or attr.name.lower() in hidden


def _get_tag_or_hash() -> str:
    tag_or_hash = _check_output(["git", "describe", "--always"]).strip()
    hash_ = _check_output(["git", "rev-parse", "--short", "HEAD"]).strip()
    have_tag_name = tag_or_hash != hash_
    return tag_or_hash if have_tag_name else _get_def(_DEFS.HASH_INDICATOR) + hash_


def _parse_int(val: str, default=0):
    if val.isdigit():
        return int(val)
    return default


def _get_files_changed():
    try:
        changed = _check_output(["git", "diff", "--numstat"])
    except subprocess.CalledProcessError:
        return {}

    insert = 0
    delete = 0

    if changed:
        for line in changed.splitlines():
            x = line.split(maxsplit=2)
            if len(x) > 1:
                insert += _parse_int(x[0])
                delete += _parse_int(x[1])

    return {_DEFS.LINES_ADDED: insert, _DEFS.LINES_REMOVED: delete}


def _get_stash(gitdir):
    try:
        with open(os.path.join(gitdir, "logs/refs/stash")) as f:
            return sum(1 for _ in f)
    except IOError:
        return 0


def _gitoperation(gitdir):
    files = (
        ("rebase-merge", "REBASE"),
        ("rebase-apply", "AM/REBASE"),
        ("MERGE_HEAD", "MERGING"),
        ("CHERRY_PICK_HEAD", "CHERRY-PICKING"),
        ("REVERT_HEAD", "REVERTING"),
        ("BISECT_LOG", "BISECTING"),
    )
    operations = [f[1] for f in files if os.path.exists(os.path.join(gitdir, f[0]))]
    if operations:
        return "|" + "|".join(operations)
    return ""


def _get_operation_stashed():
    gitdir = _check_output(["git", "rev-parse", "--git-dir"]).strip()
    stashed = _get_stash(gitdir)
    operation = _gitoperation(gitdir)
    return {_DEFS.OPERATION: operation, _DEFS.STASHED: stashed}


def _get_status_fields():
    """Return parsed values from ``git status``"""

    status = _check_output(["git", "status", "--porcelain", "--branch"])
    branch = ""
    ahead, behind = 0, 0
    untracked, changed, deleted, conflicts, staged = 0, 0, 0, 0, 0
    for line in status.splitlines():
        if line.startswith("##"):
            line = line[2:].strip()
            if "Initial commit on" in line:
                branch = line.split()[-1]
            elif "no branch" in line:
                branch = _get_tag_or_hash()
            elif "..." not in line:
                branch = line
            else:
                branch, rest = line.split("...")
                if " " in rest:
                    divergence = rest.split(" ", 1)[-1]
                    divergence = divergence.strip("[]")
                    for div in divergence.split(", "):
                        if "ahead" in div:
                            ahead = int(div[len("ahead ") :].strip())
                        elif "behind" in div:
                            behind = int(div[len("behind ") :].strip())
        elif line.startswith("??"):
            untracked += 1
        else:
            if len(line) > 1:
                if line[1] == "M":
                    changed += 1
                elif line[1] == "D":
                    deleted += 1
            if len(line) > 0 and line[0] == "U":
                conflicts += 1
            elif len(line) > 0 and line[0] != " ":
                staged += 1

    return {
        _DEFS.BRANCH: branch,
        _DEFS.AHEAD: ahead,
        _DEFS.BEHIND: behind,
        _DEFS.UNTRACKED: untracked,
        _DEFS.CHANGED: changed,
        _DEFS.DELETED: deleted,
        _DEFS.CONFLICTS: conflicts,
        _DEFS.STAGED: staged,
    }


def get_gitstatus_fields():
    """return all shown fields"""
    fields = {}
    for keys, provider in (
        (
            (
                _DEFS.BRANCH,
                _DEFS.AHEAD,
                _DEFS.BEHIND,
                _DEFS.UNTRACKED,
                _DEFS.CHANGED,
                _DEFS.DELETED,
                _DEFS.CONFLICTS,
                _DEFS.STAGED,
            ),
            _get_status_fields,
        ),
        (
            (
                _DEFS.OPERATION,
                _DEFS.STASHED,
            ),
            _get_operation_stashed,
        ),
        (
            (
                _DEFS.LINES_ADDED,
                _DEFS.LINES_REMOVED,
            ),
            _get_files_changed,
        ),
    ):
        if any(map(lambda x: not _is_hidden(x), keys)):
            try:
                fields.update(provider())
            except subprocess.SubprocessError:
                return None
    return fields


def gitstatus_prompt():
    """Return str `BRANCH|OPERATOR|numbers`"""
    fields = get_gitstatus_fields()
    if fields is None:
        return None

    ret = ""
    for fld in (_DEFS.BRANCH, _DEFS.AHEAD, _DEFS.BEHIND, _DEFS.OPERATION):
        if not _is_hidden(fld):
            val = fields[fld]
            if not val:
                continue
            ret += _get_def(fld) + str(val)

    if ret:
        ret += COLORS.RESET + "|"

    number_flds = (
        _DEFS.STAGED,
        _DEFS.CONFLICTS,
        _DEFS.CHANGED,
        _DEFS.DELETED,
        _DEFS.UNTRACKED,
        _DEFS.STASHED,
        _DEFS.LINES_ADDED,
        _DEFS.LINES_REMOVED,
    )
    for fld in number_flds:
        if _is_hidden(fld):
            continue
        symbol = _get_def(fld)
        value = fields[fld]
        if symbol and value > 0:
            ret += symbol + str(value) + COLORS.RESET
    if sum((fields.get(fld, 0) for fld in number_flds)) == 0 and not _is_hidden(
        _DEFS.CLEAN
    ):
        symbol = _get_def(_DEFS.CLEAN)
        if symbol:
            ret += symbol + COLORS.RESET
    ret = ret.rstrip("|")

    if not ret.endswith(COLORS.RESET):
        ret += COLORS.RESET

    return ret

#
# job
#
# -*- coding: utf-8 -*-
"""Prompt formatter for current jobs"""

xj = _LazyModule.load('xonsh', 'xonsh.jobs', 'xj')
def _current_job():
    j = xj.get_next_task()
    if j is not None:
        if not j["bg"]:
            cmd = j["cmds"][-1]
            s = cmd[0]
            if s == "sudo" and len(cmd) > 1:
                s = cmd[1]
            return s

#
# times
#
# -*- coding: utf-8 -*-
"""date & time related prompt formatter"""
time = _LazyModule.load('time', 'time')
# amalgamated from xonsh.built_ins import XSH
def _localtime():
    pf = XSH.env.get("PROMPT_FIELDS", {})
    tf = pf.get("time_format", "%H:%M:%S")
    return time.strftime(tf, time.localtime())

#
# vc
#
# -*- coding: utf-8 -*-
"""Prompt formatter for simple version control branches"""
# pylint:disable=no-member, invalid-name

# amalgamated os
pathlib = _LazyModule.load('pathlib', 'pathlib')
queue = _LazyModule.load('queue', 'queue')
re = _LazyModule.load('re', 're')
# amalgamated subprocess
sys = _LazyModule.load('sys', 'sys')
threading = _LazyModule.load('threading', 'threading')
# amalgamated xonsh.tools
# amalgamated from xonsh.built_ins import XSH
from xonsh.lazyasd import LazyObject

RE_REMOVE_ANSI = LazyObject(
    lambda: re.compile(r"(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]"),
    globals(),
    "RE_REMOVE_ANSI",
)


def _run_git_cmd(cmd):
    # create a safe detyped env dictionary and update with the additional git environment variables
    # when running git status commands we do not want to acquire locks running command like git status
    denv = dict(XSH.env.detype())
    denv.update({"GIT_OPTIONAL_LOCKS": "0"})
    return subprocess.check_output(cmd, env=denv, stderr=subprocess.DEVNULL)


def _get_git_branch(q):
    try:
        cmd = ["git", "rev-parse", "--abbrev-ref", "HEAD"]
        branch = xt.decode_bytes(_run_git_cmd(cmd))
    except (subprocess.CalledProcessError, OSError):
        q.put(None)
    else:
        q.put(branch.splitlines()[0] if branch else None)


def get_git_branch():
    """Attempts to find the current git branch. If this could not
    be determined (timeout, not in a git repo, etc.) then this returns None.
    """
    branch = None
    timeout = XSH.env.get("VC_BRANCH_TIMEOUT")
    q = queue.Queue()

    t = threading.Thread(target=_get_git_branch, args=(q,))
    t.start()
    t.join(timeout=timeout)
    try:
        branch = q.get_nowait()
        if branch:
            branch = RE_REMOVE_ANSI.sub("", branch)
    except queue.Empty:
        branch = None
    return branch


def _get_hg_root(q):
    _curpwd = XSH.env["PWD"]
    while True:
        if not os.path.isdir(_curpwd):
            return False
        try:
            dot_hg_is_in_curwd = any([b.name == ".hg" for b in os.scandir(_curpwd)])
        except OSError:
            return False
        if dot_hg_is_in_curwd:
            q.put(_curpwd)
            break
        else:
            _oldpwd = _curpwd
            _curpwd = os.path.split(_curpwd)[0]
            if _oldpwd == _curpwd:
                return False


def get_hg_branch(root=None):
    """Try to get the mercurial branch of the current directory,
    return None if not in a repo or subprocess.TimeoutExpired if timed out.
    """
    env = XSH.env
    timeout = env["VC_BRANCH_TIMEOUT"]
    q = queue.Queue()
    t = threading.Thread(target=_get_hg_root, args=(q,))
    t.start()
    t.join(timeout=timeout)
    try:
        root = pathlib.Path(q.get_nowait())
    except queue.Empty:
        return None
    if env.get("VC_HG_SHOW_BRANCH"):
        # get branch name
        branch_path = root / ".hg" / "branch"
        if branch_path.exists():
            with open(branch_path, "r") as branch_file:
                branch = branch_file.read().strip()
        else:
            branch = "default"
    else:
        branch = ""
    # add activated bookmark and topic
    for filename in ["bookmarks.current", "topic"]:
        feature_branch_path = root / ".hg" / filename
        if feature_branch_path.exists():
            with open(feature_branch_path) as file:
                feature_branch = file.read().strip()
            if feature_branch:
                if branch:
                    if filename == "topic":
                        branch = f"{branch}/{feature_branch}"
                    else:
                        branch = f"{branch}, {feature_branch}"
                else:
                    branch = feature_branch

    return branch


_FIRST_BRANCH_TIMEOUT = True


def _first_branch_timeout_message():
    global _FIRST_BRANCH_TIMEOUT
    sbtm = XSH.env["SUPPRESS_BRANCH_TIMEOUT_MESSAGE"]
    if not _FIRST_BRANCH_TIMEOUT or sbtm:
        return
    _FIRST_BRANCH_TIMEOUT = False
    print(
        "xonsh: branch timeout: computing the branch name, color, or both "
        "timed out while formatting the prompt. You may avoid this by "
        "increasing the value of $VC_BRANCH_TIMEOUT or by removing branch "
        "fields, like {curr_branch}, from your $PROMPT. See the FAQ "
        "for more details. This message will be suppressed for the remainder "
        "of this session. To suppress this message permanently, set "
        "$SUPPRESS_BRANCH_TIMEOUT_MESSAGE = True in your xonshrc file.",
        file=sys.stderr,
    )


def _vc_has(binary):
    """This allows us to locate binaries after git only if necessary"""
    cmds = XSH.commands_cache
    if cmds.is_empty():
        return bool(cmds.locate_binary(binary, ignore_alias=True))
    else:
        return bool(cmds.lazy_locate_binary(binary, ignore_alias=True))


def current_branch():
    """Gets the branch for a current working directory. Returns an empty string
    if the cwd is not a repository.  This currently only works for git and hg
    and should be extended in the future.  If a timeout occurred, the string
    '<branch-timeout>' is returned.
    """
    branch = None
    if _vc_has("git"):
        branch = get_git_branch()
    if not branch and _vc_has("hg"):
        branch = get_hg_branch()
    if isinstance(branch, subprocess.TimeoutExpired):
        branch = "<branch-timeout>"
        _first_branch_timeout_message()
    return branch or None


def _git_dirty_working_directory(q, include_untracked):
    try:
        cmd = ["git", "status", "--porcelain"]
        if include_untracked:
            cmd += ["--untracked-files=normal"]
        else:
            cmd += ["--untracked-files=no"]
        status = _run_git_cmd(cmd)
        if status is not None:
            q.put(bool(status))
        else:
            q.put(None)
    except (subprocess.CalledProcessError, OSError):
        q.put(None)


def git_dirty_working_directory():
    """Returns whether or not the git directory is dirty. If this could not
    be determined (timeout, file not found, etc.) then this returns None.
    """
    env = XSH.env
    timeout = env.get("VC_BRANCH_TIMEOUT")
    include_untracked = env.get("VC_GIT_INCLUDE_UNTRACKED")
    q = queue.Queue()
    t = threading.Thread(
        target=_git_dirty_working_directory, args=(q, include_untracked)
    )
    t.start()
    t.join(timeout=timeout)
    try:
        return q.get_nowait()
    except queue.Empty:
        return None


def hg_dirty_working_directory():
    """Computes whether or not the mercurial working directory is dirty or not.
    If this cannot be determined, None is returned.
    """
    env = XSH.env
    cwd = env["PWD"]
    denv = env.detype()
    vcbt = env["VC_BRANCH_TIMEOUT"]
    # Override user configurations settings and aliases
    denv["HGRCPATH"] = ""
    try:
        s = subprocess.check_output(
            ["hg", "identify", "--id"],
            stderr=subprocess.PIPE,
            cwd=cwd,
            timeout=vcbt,
            universal_newlines=True,
            env=denv,
        )
        return s.strip(os.linesep).endswith("+")
    except (
        subprocess.CalledProcessError,
        subprocess.TimeoutExpired,
        FileNotFoundError,
    ):
        return None


def dirty_working_directory():
    """Returns a boolean as to whether there are uncommitted files in version
    control repository we are inside. If this cannot be determined, returns
    None. Currently supports git and hg.
    """
    dwd = None
    if _vc_has("git"):
        dwd = git_dirty_working_directory()
    if dwd is None and _vc_has("hg"):
        dwd = hg_dirty_working_directory()
    return dwd


def branch_color():
    """Return red if the current branch is dirty, yellow if the dirtiness can
    not be determined, and green if it clean. These are bold, intense colors
    for the foreground.
    """
    dwd = dirty_working_directory()
    if dwd is None:
        color = "{BOLD_INTENSE_YELLOW}"
    elif dwd:
        color = "{BOLD_INTENSE_RED}"
    else:
        color = "{BOLD_INTENSE_GREEN}"
    return color


def branch_bg_color():
    """Return red if the current branch is dirty, yellow if the dirtiness can
    not be determined, and green if it clean. These are background colors.
    """
    dwd = dirty_working_directory()
    if dwd is None:
        color = "{BACKGROUND_YELLOW}"
    elif dwd:
        color = "{BACKGROUND_RED}"
    else:
        color = "{BACKGROUND_GREEN}"
    return color

#
# base
#
# -*- coding: utf-8 -*-
"""Base prompt, provides PROMPT_FIELDS and prompt related functions"""

itertools = _LazyModule.load('itertools', 'itertools')
# amalgamated os
# amalgamated re
socket = _LazyModule.load('socket', 'socket')
# amalgamated sys
tp = _LazyModule.load('typing', 'typing', 'tp')
xl = _LazyModule.load('xonsh', 'xonsh.lazyasd', 'xl')
# amalgamated xonsh.tools
# amalgamated xonsh.platform
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.prompt.cwd
# amalgamated xonsh.prompt.job
# amalgamated xonsh.prompt.env
# amalgamated xonsh.prompt.vc
# amalgamated xonsh.prompt.gitstatus
# amalgamated xonsh.prompt.times
@xt.lazyobject
def DEFAULT_PROMPT():
    return default_prompt()


class _ParsedToken(tp.NamedTuple):
    """It can either be a literal value alone or a field and its resultant value"""

    value: str
    field: tp.Optional[str] = None


class ParsedTokens(tp.NamedTuple):
    tokens: tp.List[_ParsedToken]
    template: tp.Union[str, tp.Callable]

    def process(self) -> str:
        """Wrapper that gets formatter-function from environment and returns final prompt."""
        processor = XSH.env.get(  # type: ignore
            "PROMPT_TOKENS_FORMATTER", prompt_tokens_formatter_default
        )
        return processor(self)

    def update(
        self,
        idx: int,
        val: tp.Optional[str],
        spec: tp.Optional[str],
        conv: tp.Optional[str],
    ) -> None:
        """Update tokens list in-place"""
        if idx < len(self.tokens):
            tok = self.tokens[idx]
            self.tokens[idx] = _ParsedToken(_format_value(val, spec, conv), tok.field)


def prompt_tokens_formatter_default(container: ParsedTokens) -> str:
    """
        Join the tokens

    Parameters
    ----------
    container: ParsedTokens
        parsed tokens holder

    Returns
    -------
    str
        process the tokens and finally return the prompt string
    """
    return "".join([tok.value for tok in container.tokens])


class PromptFormatter:
    """Class that holds all the related prompt formatting methods,
    uses the ``PROMPT_FIELDS`` envvar (no color formatting).
    """

    def __init__(self):
        self.cache = {}

    def __call__(self, template=DEFAULT_PROMPT, fields=None, **kwargs) -> str:
        """Formats a xonsh prompt template string."""

        # keep cache only during building prompt
        self.cache.clear()

        if fields is None:
            self.fields = XSH.env.get("PROMPT_FIELDS", PROMPT_FIELDS)  # type: ignore
        else:
            self.fields = fields
        try:
            toks = self._format_prompt(template=template, **kwargs)
            prompt = toks.process()
        except Exception as ex:
            # make it obvious why it has failed
            print(
                f"Failed to format prompt `{template}`-> {type(ex)}:{ex}",
                file=sys.stderr,
            )
            return _failover_template_format(template)
        return prompt

    def _format_prompt(self, template=DEFAULT_PROMPT, **kwargs) -> ParsedTokens:
        tmpl = template() if callable(template) else template
        toks = []
        for literal, field, spec, conv in xt.FORMATTER.parse(tmpl):
            if literal:
                toks.append(_ParsedToken(literal))
            entry = self._format_field(field, spec, conv, idx=len(toks), **kwargs)
            if entry is not None:
                toks.append(_ParsedToken(entry, field))

        return ParsedTokens(toks, template)

    def _format_field(self, field, spec="", conv=None, **kwargs):
        if field is None:
            return
        elif field.startswith("$"):
            val = XSH.env[field[1:]]
            return _format_value(val, spec, conv)
        elif field in self.fields:
            val = self._get_field_value(field, spec=spec, conv=conv, **kwargs)
            return _format_value(val, spec, conv)
        else:
            # color or unknown field, return as is
            return "{" + field + "}"

    def _get_field_value(self, field, **kwargs):
        field_value = self.fields[field]
        if field_value in self.cache:
            return self.cache[field_value]
        return self._no_cache_field_value(field, field_value, **kwargs)

    def _no_cache_field_value(self, field, field_value, **_):
        try:
            value = field_value() if callable(field_value) else field_value
            self.cache[field_value] = value
        except Exception:
            print("prompt: error: on field {!r}" "".format(field), file=sys.stderr)
            xt.print_exception()
            value = "{{BACKGROUND_RED}}{{ERROR:{}}}{{RESET}}".format(field)
        return value


@xl.lazyobject
def PROMPT_FIELDS():
    return dict(
        user=xp.os_environ.get("USERNAME" if xp.ON_WINDOWS else "USER", "<user>"),
        prompt_end="#" if xt.is_superuser() else "$",
        hostname=socket.gethostname().split(".", 1)[0],
        cwd=_dynamically_collapsed_pwd,
        cwd_dir=lambda: os.path.join(os.path.dirname(_replace_home_cwd()), ""),
        cwd_base=lambda: os.path.basename(_replace_home_cwd()),
        short_cwd=_collapsed_pwd,
        curr_branch=current_branch,
        branch_color=branch_color,
        branch_bg_color=branch_bg_color,
        current_job=_current_job,
        env_name=env_name,
        env_prefix="(",
        env_postfix=") ",
        vte_new_tab_cwd=vte_new_tab_cwd,
        gitstatus=gitstatus_prompt,
        time_format="%H:%M:%S",
        localtime=_localtime,
    )


def default_prompt():
    """Creates a new instance of the default prompt."""
    if xp.ON_CYGWIN or xp.ON_MSYS:
        dp = (
            "{env_name}"
            "{BOLD_GREEN}{user}@{hostname}"
            "{BOLD_BLUE} {cwd} {prompt_end}{RESET} "
        )
    elif xp.ON_WINDOWS and not xp.win_ansi_support():
        dp = (
            "{env_name}"
            "{BOLD_INTENSE_GREEN}{user}@{hostname}{BOLD_INTENSE_CYAN} "
            "{cwd}{branch_color}{curr_branch: {}}{RESET} "
            "{BOLD_INTENSE_CYAN}{prompt_end}{RESET} "
        )
    else:
        dp = (
            "{env_name}"
            "{BOLD_GREEN}{user}@{hostname}{BOLD_BLUE} "
            "{cwd}{branch_color}{curr_branch: {}}{RESET} "
            "{BOLD_BLUE}{prompt_end}{RESET} "
        )
    return dp


def _failover_template_format(template):
    if callable(template):
        try:
            # Exceptions raises from function of producing $PROMPT
            # in user's xonshrc should not crash xonsh
            return template()
        except Exception:
            xt.print_exception()
            return "$ "
    return template


@xt.lazyobject
def RE_HIDDEN():
    return re.compile("\001.*?\002")


def multiline_prompt(curr=""):
    """Returns the filler text for the prompt in multiline scenarios."""
    line = curr.rsplit("\n", 1)[1] if "\n" in curr else curr
    line = RE_HIDDEN.sub("", line)  # gets rid of colors
    # most prompts end in whitespace, head is the part before that.
    head = line.rstrip()
    headlen = len(head)
    # tail is the trailing whitespace
    tail = line if headlen == 0 else line.rsplit(head[-1], 1)[1]
    # now to construct the actual string
    dots = XSH.env.get("MULTILINE_PROMPT")
    dots = dots() if callable(dots) else dots
    if dots is None or len(dots) == 0:
        return ""
    tokstr = xt.format_color(dots, hide=True)
    baselen = 0
    basetoks = []
    for x in tokstr.split("\001"):
        pre, sep, post = x.partition("\002")
        if len(sep) == 0:
            basetoks.append(("", pre))
            baselen += len(pre)
        else:
            basetoks.append(("\001" + pre + "\002", post))
            baselen += len(post)
    if baselen == 0:
        return xt.format_color("{RESET}" + tail, hide=True)
    toks = basetoks * (headlen // baselen)
    n = headlen % baselen
    count = 0
    for tok in basetoks:
        slen = len(tok[1])
        newcount = slen + count
        if slen == 0:
            continue
        elif newcount <= n:
            toks.append(tok)
        else:
            toks.append((tok[0], tok[1][: n - count]))
        count = newcount
        if n <= count:
            break
    toks.append((xt.format_color("{RESET}", hide=True), tail))
    rtn = "".join(itertools.chain.from_iterable(toks))
    return rtn


def is_template_string(template, PROMPT_FIELDS=None):
    """Returns whether or not the string is a valid template."""
    template = template() if callable(template) else template
    try:
        included_names = set(i[1] for i in xt.FORMATTER.parse(template))
    except ValueError:
        return False
    included_names.discard(None)
    if PROMPT_FIELDS is None:
        fmtter = XSH.env.get("PROMPT_FIELDS", PROMPT_FIELDS)
    else:
        fmtter = PROMPT_FIELDS
    known_names = set(fmtter.keys())
    return included_names <= known_names


def _format_value(val, spec, conv):
    """Formats a value from a template string {val!conv:spec}. The spec is
    applied as a format string itself, but if the value is None, the result
    will be empty. The purpose of this is to allow optional parts in a
    prompt string. For example, if the prompt contains '{current_job:{} | }',
    and 'current_job' returns 'sleep', the result is 'sleep | ', and if
    'current_job' returns None, the result is ''.
    """
    if val is None:
        return ""
    val = xt.FORMATTER.convert_field(val, conv)
    if spec:
        val = xt.FORMATTER.format(spec, val)
    if not isinstance(val, str):
        val = str(val)
    return val

