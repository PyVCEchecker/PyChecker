"""Amalgamation of xonsh.completers package, made up of the following modules, in order:

* bash_completion
* tools
* commands
* completer
* environment
* man
* path
* pip
* python
* xompletions
* _aliases
* base
* bash
* dirs
* init

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
# bash_completion
#
"""This module provides the implementation for the retrieving completion results
from bash.
"""
# developer note: this file should not perform any action on import.
#                 This file comes from https://github.com/xonsh/py-bash-completion
#                 and should be edited there!
os = _LazyModule.load('os', 'os')
re = _LazyModule.load('re', 're')
sys = _LazyModule.load('sys', 'sys')
shlex = _LazyModule.load('shlex', 'shlex')
shutil = _LazyModule.load('shutil', 'shutil')
pathlib = _LazyModule.load('pathlib', 'pathlib')
platform = _LazyModule.load('platform', 'platform')
functools = _LazyModule.load('functools', 'functools')
subprocess = _LazyModule.load('subprocess', 'subprocess')
tp = _LazyModule.load('typing', 'typing', 'tp')
__version__ = "0.2.7"


@functools.lru_cache(1)
def _git_for_windows_path():
    """Returns the path to git for windows, if available and None otherwise."""
    import winreg

    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\GitForWindows")
        gfwp, _ = winreg.QueryValueEx(key, "InstallPath")
    except FileNotFoundError:
        gfwp = None
    return gfwp


@functools.lru_cache(1)
def _windows_bash_command(env=None):
    """Determines the command for Bash on windows."""
    wbc = "bash"
    path = None if env is None else env.get("PATH", None)
    bash_on_path = shutil.which("bash", path=path)
    if bash_on_path:
        try:
            out = subprocess.check_output(
                [bash_on_path, "--version"],
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )
        except subprocess.CalledProcessError:
            bash_works = False
        else:
            # Check if Bash is from the "Windows Subsystem for Linux" (WSL)
            # which can't be used by xonsh foreign-shell/completer
            bash_works = out and "pc-linux-gnu" not in out.splitlines()[0]

        if bash_works:
            wbc = bash_on_path
        else:
            gfwp = _git_for_windows_path()
            if gfwp:
                bashcmd = os.path.join(gfwp, "bin\\bash.exe")
                if os.path.isfile(bashcmd):
                    wbc = bashcmd
    return wbc


def _bash_command(env=None):
    """Determines the command for Bash on the current plaform."""
    if platform.system() == "Windows":
        bc = _windows_bash_command(env=None)
    else:
        bc = "bash"
    return bc


def _bash_completion_paths_default():
    """A possibly empty tuple with default paths to Bash completions known for
    the current platform.
    """
    platform_sys = platform.system()
    if platform_sys == "Linux" or sys.platform == "cygwin":
        bcd = ("/usr/share/bash-completion/bash_completion",)
    elif platform_sys == "Darwin":
        bcd = (
            "/usr/local/share/bash-completion/bash_completion",  # v2.x
            "/usr/local/etc/bash_completion",
        )  # v1.x
    elif platform_sys == "Windows":
        gfwp = _git_for_windows_path()
        if gfwp:
            bcd = (
                os.path.join(gfwp, "usr\\share\\bash-completion\\" "bash_completion"),
                os.path.join(
                    gfwp, "mingw64\\share\\git\\completion\\" "git-completion.bash"
                ),
            )
        else:
            bcd = ()
    else:
        bcd = ()
    return bcd


_BASH_COMPLETIONS_PATHS_DEFAULT: tp.Tuple[str, ...] = ()


def _get_bash_completions_source(paths=None):
    global _BASH_COMPLETIONS_PATHS_DEFAULT
    if paths is None:
        if _BASH_COMPLETIONS_PATHS_DEFAULT is None:
            _BASH_COMPLETIONS_PATHS_DEFAULT = _bash_completion_paths_default()
        paths = _BASH_COMPLETIONS_PATHS_DEFAULT
    for path in map(pathlib.Path, paths):
        if path.is_file():
            return 'source "{}"'.format(path.as_posix())
    return None


def _bash_get_sep():
    """Returns the appropriate filepath separator char depending on OS and
    xonsh options set
    """
    if platform.system() == "Windows":
        return os.altsep
    else:
        return os.sep


_BASH_PATTERN_NEED_QUOTES: tp.Optional[tp.Pattern] = None


def _bash_pattern_need_quotes():
    global _BASH_PATTERN_NEED_QUOTES
    if _BASH_PATTERN_NEED_QUOTES is not None:
        return _BASH_PATTERN_NEED_QUOTES
    pattern = r'\s`\$\{\}\,\*\(\)"\'\?&'
    if platform.system() == "Windows":
        pattern += "%"
    pattern = "[" + pattern + "]" + r"|\band\b|\bor\b"
    _BASH_PATTERN_NEED_QUOTES = re.compile(pattern)
    return _BASH_PATTERN_NEED_QUOTES


def _bash_expand_path(s):
    """Takes a string path and expands ~ to home and environment vars."""
    # expand ~ according to Bash unquoted rules "Each variable assignment is
    # checked for unquoted tilde-prefixes immediately following a ':' or the
    # first '='". See the following for more details.
    # https://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html
    pre, char, post = s.partition("=")
    if char:
        s = os.path.expanduser(pre) + char
        s += os.pathsep.join(map(os.path.expanduser, post.split(os.pathsep)))
    else:
        s = os.path.expanduser(s)
    return s


def _bash_quote_to_use(x):
    single = "'"
    double = '"'
    if single in x and double not in x:
        return double
    else:
        return single


def _bash_quote_paths(paths, start, end):
    out = set()
    space = " "
    backslash = "\\"
    double_backslash = "\\\\"
    slash = _bash_get_sep()
    orig_start = start
    orig_end = end
    # quote on all or none, to make readline completes to max prefix
    need_quotes = any(
        re.search(_bash_pattern_need_quotes(), x)
        or (backslash in x and slash != backslash)
        for x in paths
    )

    for s in paths:
        start = orig_start
        end = orig_end
        if start == "" and need_quotes:
            start = end = _bash_quote_to_use(s)
        if os.path.isdir(_bash_expand_path(s)):
            _tail = slash
        elif end == "":
            _tail = space
        else:
            _tail = ""
        if start != "" and "r" not in start and backslash in s:
            start = "r%s" % start
        s = s + _tail
        if end != "":
            if "r" not in start.lower():
                s = s.replace(backslash, double_backslash)
            if s.endswith(backslash) and not s.endswith(double_backslash):
                s += backslash
        if end in s:
            s = s.replace(end, "".join("\\%s" % i for i in end))
        out.add(start + s + end)
    return out, need_quotes


BASH_COMPLETE_SCRIPT = r"""
{source}

# Override some functions in bash-completion, do not quote for readline
quote_readline()
{{
    echo "$1"
}}

_quote_readline_by_ref()
{{
    if [[ $1 == \'* || $1 == \"* ]]; then
        # Leave out first character
        printf -v $2 %s "${{1:1}}"
    else
        printf -v $2 %s "$1"
    fi

    [[ ${{!2}} == \$* ]] && eval $2=${{!2}}
}}


function _get_complete_statement {{
    complete -p {cmd} 2> /dev/null || echo "-F _minimal"
}}

function getarg {{
    find=$1
    shift 1
    prev=""
    for i in $* ; do
        if [ "$prev" = "$find" ] ; then
            echo $i
        fi
        prev=$i
    done
}}

_complete_stmt=$(_get_complete_statement)
if echo "$_complete_stmt" | grep --quiet -e "_minimal"
then
    declare -f _completion_loader > /dev/null && _completion_loader {cmd}
    _complete_stmt=$(_get_complete_statement)
fi

# Is -C (subshell) or -F (function) completion used?
if [[ $_complete_stmt =~ "-C" ]] ; then
    _func=$(eval getarg "-C" $_complete_stmt)
else
    _func=$(eval getarg "-F" $_complete_stmt)
    declare -f "$_func" > /dev/null || exit 1
fi

echo "$_complete_stmt"
export COMP_WORDS=({line})
export COMP_LINE={comp_line}
export COMP_POINT=${{#COMP_LINE}}
export COMP_COUNT={end}
export COMP_CWORD={n}
$_func {cmd} {prefix} {prev}

# print out completions, right-stripped if they contain no internal spaces
shopt -s extglob
for ((i=0;i<${{#COMPREPLY[*]}};i++))
do
    no_spaces="${{COMPREPLY[i]//[[:space:]]}}"
    no_trailing_spaces="${{COMPREPLY[i]%%+([[:space:]])}}"
    if [[ "$no_spaces" == "$no_trailing_spaces" ]]; then
        echo "$no_trailing_spaces"
    else
        echo "${{COMPREPLY[i]}}"
    fi
done
"""


def bash_completions(
    prefix,
    line,
    begidx,
    endidx,
    env=None,
    paths=None,
    command=None,
    quote_paths=_bash_quote_paths,
    line_args=None,
    opening_quote="",
    closing_quote="",
    arg_index=None,
    **kwargs
):
    """Completes based on results from BASH completion.

    Parameters
    ----------
    prefix : str
        The string to match
    line : str
        The line that prefix appears on.
    begidx : int
        The index in line that prefix starts on.
    endidx : int
        The index in line that prefix ends on.
    env : Mapping, optional
        The environment dict to execute the Bash subprocess in.
    paths : list or tuple of str or None, optional
        This is a list (or tuple) of strings that specifies where the
        ``bash_completion`` script may be found. The first valid path will
        be used. For better performance, bash-completion v2.x is recommended
        since it lazy-loads individual completion scripts. For both
        bash-completion v1.x and v2.x, paths of individual completion scripts
        (like ``.../completes/ssh``) do not need to be included here. The
        default values are platform dependent, but sane.
    command : str or None, optional
        The /path/to/bash to use. If None, it will be selected based on the
        from the environment and platform.
    quote_paths : callable, optional
        A functions that quotes file system paths. You shouldn't normally need
        this as the default is acceptable 99+% of the time. This function should
        return a set of the new paths and a boolean for whether the paths were
        quoted.
    line_args : list of str, optional
        A list of the args in the current line to be used instead of ``line.split()``.
        This is usefull with a space in an argument, e.g. ``ls 'a dir/'<TAB>``.
    opening_quote : str, optional
        The current argument's opening quote. This is passed to the `quote_paths` function.
    closing_quote : str, optional
        The closing quote that **should** be used. This is also passed to the `quote_paths` function.
    arg_index : int, optional
        The current prefix's index in the args.

    Returns
    -------
    rtn : set of str
        Possible completions of prefix
    lprefix : int
        Length of the prefix to be replaced in the completion.
    """
    source = _get_bash_completions_source(paths) or ""

    if prefix.startswith("$"):  # do not complete env variables
        return set(), 0

    splt = line_args or line.split()
    cmd = splt[0]
    cmd = os.path.basename(cmd)
    prev = ""

    if arg_index is not None:
        n = arg_index
        if arg_index > 0:
            prev = splt[arg_index - 1]
    else:
        # find `n` and `prev` by ourselves
        idx = n = 0
        for n, tok in enumerate(splt):  # noqa
            if tok == prefix:
                idx = line.find(prefix, idx)
                if idx >= begidx:
                    break
            prev = tok

        if len(prefix) == 0:
            n += 1

    prefix_quoted = shlex.quote(prefix)

    script = BASH_COMPLETE_SCRIPT.format(
        source=source,
        line=" ".join(shlex.quote(p) for p in splt if p),
        comp_line=shlex.quote(line),
        n=n,
        cmd=shlex.quote(cmd),
        end=endidx + 1,
        prefix=prefix_quoted,
        prev=shlex.quote(prev),
    )

    if command is None:
        command = _bash_command(env=env)
    try:
        out = subprocess.check_output(
            [command, "-c", script],
            universal_newlines=True,
            stderr=subprocess.PIPE,
            env=env,
        )
        if not out:
            raise ValueError
    except (
        subprocess.CalledProcessError,
        FileNotFoundError,
        ValueError,
    ):
        return set(), 0

    out = out.splitlines()
    complete_stmt = out[0]
    out = set(out[1:])

    # From GNU Bash document: The results of the expansion are prefix-matched
    # against the word being completed

    # Ensure input to `commonprefix` is a list (now required by Python 3.6)
    commprefix = os.path.commonprefix(list(out))
    strip_len = 0
    strip_prefix = prefix.strip("\"'")
    while strip_len < len(strip_prefix) and strip_len < len(commprefix):
        if commprefix[strip_len] == strip_prefix[strip_len]:
            break
        strip_len += 1

    if "-o noquote" not in complete_stmt:
        out, need_quotes = quote_paths(out, opening_quote, closing_quote)
    if "-o nospace" in complete_stmt:
        out = set([x.rstrip() for x in out])

    return out, max(len(prefix) - strip_len, 0)


def bash_complete_line(line, return_line=True, **kwargs):
    """Provides the completion from the end of the line.

    Parameters
    ----------
    line : str
        Line to complete
    return_line : bool, optional
        If true (default), will return the entire line, with the completion added.
        If false, this will instead return the strings to append to the original line.
    kwargs : optional
        All other keyword arguments are passed to the bash_completions() function.

    Returns
    -------
    rtn : set of str
        Possible completions of prefix
    """
    # set up for completing from the end of the line
    split = line.split()
    if len(split) > 1 and not line.endswith(" "):
        prefix = split[-1]
        begidx = len(line.rsplit(prefix)[0])
    else:
        prefix = ""
        begidx = len(line)
    endidx = len(line)
    # get completions
    out, lprefix = bash_completions(prefix, line, begidx, endidx, **kwargs)
    # reformat output
    if return_line:
        preline = line[:-lprefix]
        rtn = {preline + o for o in out}
    else:
        rtn = {o[lprefix:] for o in out}
    return rtn


def _bc_main(args=None):
    """Runs complete_line() and prints the output."""
    from argparse import ArgumentParser

    p = ArgumentParser("bash_completions")
    p.add_argument(
        "--return-line",
        action="store_true",
        dest="return_line",
        default=True,
        help="will return the entire line, with the completion added",
    )
    p.add_argument(
        "--no-return-line",
        action="store_false",
        dest="return_line",
        help="will instead return the strings to append to the original line",
    )
    p.add_argument("line", help="line to complete")
    ns = p.parse_args(args=args)
    out = bash_complete_line(ns.line, return_line=ns.return_line)
    for o in sorted(out):
        print(o)


if __name__ == "__main__":
    _bc_main()

#
# tools
#
"""Xonsh completer tools."""
inspect = _LazyModule.load('inspect', 'inspect')
textwrap = _LazyModule.load('textwrap', 'textwrap')
# amalgamated typing
from functools import wraps

from xonsh.built_ins import XSH
from xonsh.lazyasd import lazyobject
from xonsh.parsers.completion_context import CompletionContext, CommandContext


def _filter_normal(s, x):
    return s.startswith(x)


def _filter_ignorecase(s, x):
    return s.lower().startswith(x.lower())


def get_filter_function():
    """
    Return an appropriate filtering function for completions, given the valid
    of $CASE_SENSITIVE_COMPLETIONS
    """
    csc = XSH.env.get("CASE_SENSITIVE_COMPLETIONS")
    if csc:
        return _filter_normal
    else:
        return _filter_ignorecase


def justify(s, max_length, left_pad=0):
    """
    Re-wrap the string s so that each line is no more than max_length
    characters long, padding all lines but the first on the left with the
    string left_pad.
    """
    txt = textwrap.wrap(s, width=max_length, subsequent_indent=" " * left_pad)
    return "\n".join(txt)


class RichCompletion(str):
    """A rich completion that completers can return instead of a string"""

    def __new__(cls, value, *args, **kwargs):
        completion = super().__new__(cls, value)
        # ``str``'s ``__new__`` doesn't call ``__init__``, so we'll call it ourselves
        cls.__init__(completion, value, *args, **kwargs)
        return completion

    def __init__(
        self,
        value: str,
        prefix_len: tp.Optional[int] = None,
        display: tp.Optional[str] = None,
        description: str = "",
        style: str = "",
        append_closing_quote: bool = True,
        append_space: bool = False,
    ):
        """
        Parameters
        ----------
        value :
            The completion's actual value.
        prefix_len :
            Length of the prefix to be replaced in the completion.
            If None, the default prefix len will be used.
        display :
            Text to display in completion option list instead of ``value``.
            NOTE: If supplied, the common prefix with other completions won't be removed.
        description :
            Extra text to display when the completion is selected.
        style :
            Style to pass to prompt-toolkit's ``Completion`` object.
        append_closing_quote :
            Whether to append a closing quote to the completion if the cursor is after it.
            See ``Completer.complete`` in ``xonsh/completer.py``
        append_space :
            Whether to append a space after the completion.
            This is intended to work with ``appending_closing_quote``, so the space will be added correctly **after** the closing quote.
            This is used in ``Completer.complete``.
            An extra bonus is that the space won't show up in the ``display`` attribute.
        """
        super().__init__()
        self.prefix_len = prefix_len
        self.display = display
        self.description = description
        self.style = style
        self.append_closing_quote = append_closing_quote
        self.append_space = append_space

    @property
    def value(self):
        return str(self)

    def __repr__(self):
        # don't print default values
        attrs = ", ".join(
            f"{name}={getattr(self, name)!r}"
            for name, default in RICH_COMPLETION_DEFAULTS
            if getattr(self, name) != default
        )
        return f"RichCompletion({self.value!r}, {attrs})"

    def replace(self, **kwargs):
        """Create a new RichCompletion with replaced attributes"""
        default_kwargs = dict(
            value=self.value,
            **self.__dict__,
        )
        default_kwargs.update(kwargs)
        return RichCompletion(**default_kwargs)


@lazyobject
def RICH_COMPLETION_DEFAULTS():
    """The ``__init__`` parameters' default values (excluding ``self`` and ``value``)."""
    return [
        (name, param.default)
        for name, param in inspect.signature(RichCompletion.__init__).parameters.items()
        if name not in ("self", "value")
    ]


Completion = tp.Union[RichCompletion, str]
CompleterResult = tp.Union[tp.Set[Completion], tp.Tuple[tp.Set[Completion], int], None]
ContextualCompleter = tp.Callable[[CompletionContext], CompleterResult]


def contextual_completer(func: ContextualCompleter):
    """Decorator for a contextual completer

    This is used to mark completers that want to use the parsed completion context.
    See ``xonsh/parsers/completion_context.py``.

    ``func`` receives a single CompletionContext object.
    """
    func.contextual = True  # type: ignore
    return func


def is_contextual_completer(func):
    return getattr(func, "contextual", False)


def contextual_command_completer(func: tp.Callable[[CommandContext], CompleterResult]):
    """like ``contextual_completer``,
    but will only run when completing a command and will directly receive the ``CommandContext`` object"""

    @contextual_completer
    @wraps(func)
    def _completer(context: CompletionContext) -> CompleterResult:
        if context.command is not None:
            return func(context.command)
        return None

    return _completer


def contextual_command_completer_for(cmd: str):
    """like ``contextual_command_completer``,
    but will only run when completing the ``cmd`` command"""

    def decor(func: tp.Callable[[CommandContext], CompleterResult]):
        @contextual_completer
        @wraps(func)
        def _completer(context: CompletionContext) -> CompleterResult:
            if context.command is not None and context.command.completing_command(cmd):
                return func(context.command)
            return None

        return _completer

    return decor


def non_exclusive_completer(func):
    """Decorator for a non-exclusive completer

    This is used to mark completers that will be collected with other completer's results.
    """
    func.non_exclusive = True  # type: ignore
    return func


def is_exclusive_completer(func):
    return not getattr(func, "non_exclusive", False)


def apply_lprefix(comps, lprefix):
    if lprefix is None:
        return comps

    for comp in comps:
        if isinstance(comp, RichCompletion):
            if comp.prefix_len is None:
                yield comp.replace(prefix_len=lprefix)
            else:
                # this comp has a custom prefix len
                yield comp
        else:
            yield RichCompletion(comp, prefix_len=lprefix)

#
# commands
#
# amalgamated os
# amalgamated typing
xt = _LazyModule.load('xonsh', 'xonsh.tools', 'xt')
xp = _LazyModule.load('xonsh', 'xonsh.platform', 'xp')
from xonsh.completer import Completer
# amalgamated xonsh.completers.tools
# amalgamated from xonsh.parsers.completion_context import CompletionContext, CommandContext
# amalgamated from xonsh.built_ins import XSH
SKIP_TOKENS = {"sudo", "time", "timeit", "which", "showcmd", "man"}
END_PROC_TOKENS = ("|", ";", "&&")  # includes ||
END_PROC_KEYWORDS = {"and", "or"}


def complete_command(command: CommandContext):
    """
    Returns a list of valid commands starting with the first argument
    """
    cmd = command.prefix
    out: tp.Set[Completion] = {
        RichCompletion(s, append_space=True)
        for s in XSH.commands_cache  # type: ignore
        if get_filter_function()(s, cmd)
    }
    if xp.ON_WINDOWS:
        out |= {i for i in xt.executables_in(".") if i.startswith(cmd)}
    base = os.path.basename(cmd)
    if os.path.isdir(base):
        out |= {
            os.path.join(base, i) for i in xt.executables_in(base) if i.startswith(cmd)
        }
    return out


@contextual_command_completer
def complete_skipper(command_context: CommandContext):
    """
    Skip over several tokens (e.g., sudo) and complete based on the rest of the command.

    Contextual completers don't need us to skip tokens since they get the correct completion context -
    meaning we only need to skip commands like ``sudo``.
    """
    skip_part_num = 0
    # all the args before the current argument
    for arg in command_context.args[: command_context.arg_index]:
        if arg.value not in SKIP_TOKENS:
            break
        skip_part_num += 1

    if skip_part_num == 0:
        return None

    skipped_command_context = command_context._replace(
        args=command_context.args[skip_part_num:],
        arg_index=command_context.arg_index - skip_part_num,
    )

    if skipped_command_context.arg_index == 0:
        # completing the command after a SKIP_TOKEN
        return complete_command(skipped_command_context)

    completer: Completer = XSH.shell.shell.completer  # type: ignore
    return completer.complete_from_context(CompletionContext(skipped_command_context))


@non_exclusive_completer
@contextual_command_completer
def complete_end_proc_tokens(command_context: CommandContext):
    """If there's no space following an END_PROC_TOKEN, insert one"""
    if command_context.opening_quote or not command_context.prefix:
        return None
    prefix = command_context.prefix
    # for example `echo a|`, `echo a&&`, `echo a ;`
    if any(prefix.endswith(ending) for ending in END_PROC_TOKENS):
        return {RichCompletion(prefix, append_space=True)}
    return None


@non_exclusive_completer
@contextual_command_completer
def complete_end_proc_keywords(command_context: CommandContext):
    """If there's no space following an END_PROC_KEYWORD, insert one"""
    if command_context.opening_quote or not command_context.prefix:
        return None
    prefix = command_context.prefix
    if prefix in END_PROC_KEYWORDS:
        return {RichCompletion(prefix, append_space=True)}
    return None

#
# completer
#
collections = _LazyModule.load('collections', 'collections')
# amalgamated from xonsh.parsers.completion_context import CommandContext
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.completers.tools
@contextual_command_completer_for("completer")
def complete_completer(command: CommandContext):
    """
    Completion for "completer"
    """
    if command.suffix:
        # completing in a middle of a word
        # (e.g. "completer some<TAB>thing")
        return None

    curix = command.arg_index

    compnames = set(XSH.completers.keys())
    if curix == 1:
        possible = {"list", "help", "add", "remove"}
    elif curix == 2:
        first_arg = command.args[1].value
        if first_arg == "help":
            possible = {"list", "add", "remove"}
        elif first_arg == "remove":
            possible = compnames
        else:
            raise StopIteration
    else:
        if command.args[1].value != "add":
            raise StopIteration
        if curix == 3:
            possible = {i for i, j in XSH.ctx.items() if callable(j)}
        elif curix == 4:
            possible = (
                {"start", "end"}
                | {">" + n for n in compnames}
                | {"<" + n for n in compnames}
            )
        else:
            raise StopIteration
    return {i for i in possible if i.startswith(command.prefix)}


def add_one_completer(name, func, loc="end"):
    new = collections.OrderedDict()
    if loc == "start":
        # Add new completer before the first exclusive one.
        # We don't want new completers to be before the non-exclusive ones,
        # because then they won't be used when this completer is successful.
        # On the other hand, if the new completer is non-exclusive,
        # we want it to be before all other exclusive completers so that is will always work.
        items = list(XSH.completers.items())
        first_exclusive = next(
            (i for i, (_, v) in enumerate(items) if is_exclusive_completer(v)),
            len(items),
        )
        for k, v in items[:first_exclusive]:
            new[k] = v
        new[name] = func
        for k, v in items[first_exclusive:]:
            new[k] = v
    elif loc == "end":
        for (k, v) in XSH.completers.items():
            new[k] = v
        new[name] = func
    else:
        direction, rel = loc[0], loc[1:]
        found = False
        for (k, v) in XSH.completers.items():
            if rel == k and direction == "<":
                new[name] = func
                found = True
            new[k] = v
            if rel == k and direction == ">":
                new[name] = func
                found = True
        if not found:
            new[name] = func
    XSH.completers.clear()
    XSH.completers.update(new)


def list_completers():
    """List the active completers"""
    o = "Registered Completer Functions: (NX = Non Exclusive)\n\n"
    non_exclusive = " [NX]"
    _comp = XSH.completers
    ml = max((len(i) for i in _comp), default=0)
    exclusive_len = ml + len(non_exclusive) + 1
    _strs = []
    for c in _comp:
        if _comp[c].__doc__ is None:
            doc = "No description provided"
        else:
            doc = " ".join(_comp[c].__doc__.split())
        doc = justify(doc, 80, exclusive_len + 3)
        if is_exclusive_completer(_comp[c]):
            _strs.append("{: <{}} : {}".format(c, exclusive_len, doc))
        else:
            _strs.append("{: <{}} {} : {}".format(c, ml, non_exclusive, doc))
    return o + "\n".join(_strs) + "\n"


def remove_completer(name: str):
    """removes a completer from xonsh

    Parameters
    ----------
    name:
        NAME is a unique name of a completer (run "completer list" to see the current
        completers in order)
    """
    err = None
    if name not in XSH.completers:
        err = f"The name {name} is not a registered completer function."
    if err is None:
        del XSH.completers[name]
        return
    else:
        return None, err + "\n", 1

#
# environment
#
# amalgamated from xonsh.built_ins import XSH
# amalgamated from xonsh.parsers.completion_context import CompletionContext
# amalgamated xonsh.completers.tools
@contextual_completer
@non_exclusive_completer
def complete_environment_vars(context: CompletionContext):
    if context.command:
        prefix = context.command.prefix
    elif context.python:
        prefix = context.python.prefix
    else:
        return None

    dollar_location = prefix.rfind("$")
    if dollar_location == -1:
        return None

    key = prefix[dollar_location + 1 :]
    lprefix = len(key) + 1
    filter_func = get_filter_function()
    env_names = XSH.env

    return {"$" + k for k in env_names if filter_func(k, key)}, lprefix

#
# man
#
# amalgamated os
# amalgamated re
pickle = _LazyModule.load('pickle', 'pickle')
# amalgamated subprocess
# amalgamated typing
# amalgamated from xonsh.parsers.completion_context import CommandContext
# amalgamated from xonsh.built_ins import XSH
xl = _LazyModule.load('xonsh', 'xonsh.lazyasd', 'xl')
# amalgamated xonsh.completers.tools
OPTIONS: tp.Optional[tp.Dict[str, tp.Any]] = None
OPTIONS_PATH: tp.Optional[str] = None


@xl.lazyobject
def SCRAPE_RE():
    return re.compile(r"^(?:\s*(?:-\w|--[a-z0-9-]+)[\s,])+", re.M)


@xl.lazyobject
def INNER_OPTIONS_RE():
    return re.compile(r"-\w|--[a-z0-9-]+")


@contextual_command_completer
def complete_from_man(context: CommandContext):
    """
    Completes an option name, based on the contents of the associated man
    page.
    """
    global OPTIONS, OPTIONS_PATH
    if OPTIONS is None:
        datadir: str = XSH.env["XONSH_DATA_DIR"]  # type: ignore
        OPTIONS_PATH = os.path.join(datadir, "man_completions_cache")
        try:
            with open(OPTIONS_PATH, "rb") as f:
                OPTIONS = pickle.load(f)
        except Exception:
            OPTIONS = {}
    if context.arg_index == 0 or not context.prefix.startswith("-"):
        return set()
    cmd = context.args[0].value
    if cmd not in OPTIONS:
        try:
            manpage = subprocess.Popen(
                ["man", cmd], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
            )
            # This is a trick to get rid of reverse line feeds
            enc_text = subprocess.check_output(["col", "-b"], stdin=manpage.stdout)
            text = enc_text.decode("utf-8")
            scraped_text = " ".join(SCRAPE_RE.findall(text))
            matches = INNER_OPTIONS_RE.findall(scraped_text)
            OPTIONS[cmd] = matches
            with open(tp.cast(str, OPTIONS_PATH), "wb") as f:
                pickle.dump(OPTIONS, f)
        except Exception:
            return set()
    return {s for s in OPTIONS[cmd] if get_filter_function()(s, context.prefix)}

#
# path
#
# amalgamated os
# amalgamated re
ast = _LazyModule.load('ast', 'ast')
glob = _LazyModule.load('glob', 'glob')
# amalgamated from xonsh.built_ins import XSH
# amalgamated from xonsh.parsers.completion_context import CommandContext
# amalgamated xonsh.tools
# amalgamated xonsh.platform
# amalgamated xonsh.lazyasd
# amalgamated xonsh.completers.tools
@xl.lazyobject
def PATTERN_NEED_QUOTES():
    pattern = r'\s`\$\{\}\,\*\(\)"\'\?&#'
    if xp.ON_WINDOWS:
        pattern += "%"
    pattern = "[" + pattern + "]" + r"|\band\b|\bor\b"
    return re.compile(pattern)


def cd_in_command(line):
    """Returns True if "cd" is a token in the line, False otherwise."""
    lexer = XSH.execer.parser.lexer
    lexer.reset()
    lexer.input(line)
    have_cd = False
    for tok in lexer:
        if tok.type == "NAME" and tok.value == "cd":
            have_cd = True
            break
    return have_cd


def _get_normalized_pstring_quote(s):
    for pre, norm_pre in (("p", "p"), ("pr", "pr"), ("rp", "pr"), ("fp", "pf")):
        for q in ('"', "'"):
            if s.startswith(f"{pre}{q}"):
                return norm_pre, q
    return (None, None)


def _path_from_partial_string(inp, pos=None):
    if pos is None:
        pos = len(inp)
    partial = inp[:pos]
    startix, endix, quote = xt.check_for_partial_string(partial)
    _post = ""
    if startix is None:
        return None
    elif endix is None:
        string = partial[startix:]
    else:
        if endix != pos:
            _test = partial[endix:pos]
            if not any(i == " " for i in _test):
                _post = _test
            else:
                return None
        string = partial[startix:endix]

    # If 'pr'/'rp', treat as raw string, otherwise strip leading 'p'
    pstring_pre = _get_normalized_pstring_quote(quote)[0]
    if pstring_pre == "pr":
        string = f"r{string[2:]}"
    elif pstring_pre == "p":
        string = string[1:]

    end = xt.RE_STRING_START.sub("", quote)
    _string = string
    if not _string.endswith(end):
        _string = _string + end
    try:
        val = ast.literal_eval(_string)
    except (SyntaxError, ValueError):
        return None
    if isinstance(val, bytes):
        env = XSH.env
        val = val.decode(
            encoding=env.get("XONSH_ENCODING"), errors=env.get("XONSH_ENCODING_ERRORS")
        )
    return string + _post, val + _post, quote, end


def _normpath(p):
    """
    Wraps os.normpath() to avoid removing './' at the beginning
    and '/' at the end. On windows it does the same with backslashes
    """
    initial_dotslash = p.startswith(os.curdir + os.sep)
    initial_dotslash |= xp.ON_WINDOWS and p.startswith(os.curdir + os.altsep)
    p = p.rstrip()
    trailing_slash = p.endswith(os.sep)
    trailing_slash |= xp.ON_WINDOWS and p.endswith(os.altsep)
    p = os.path.normpath(p)
    if initial_dotslash and p != ".":
        p = os.path.join(os.curdir, p)
    if trailing_slash:
        p = os.path.join(p, "")
    if xp.ON_WINDOWS and XSH.env.get("FORCE_POSIX_PATHS"):
        p = p.replace(os.sep, os.altsep)
    return p


def _startswithlow(x, start, startlow=None):
    if startlow is None:
        startlow = start.lower()
    return x.startswith(start) or x.lower().startswith(startlow)


def _startswithnorm(x, start, startlow=None):
    return x.startswith(start)


def _dots(prefix):
    complete_dots = XSH.env.get("COMPLETE_DOTS", "matching").lower()
    if complete_dots == "never":
        return ()
    slash = xt.get_sep()
    if slash == "\\":
        slash = ""
    prefixes = {"."}
    if complete_dots == "always":
        prefixes.add("")
    if prefix in prefixes:
        return ("." + slash, ".." + slash)
    elif prefix == "..":
        return (".." + slash,)
    else:
        return ()


def _add_cdpaths(paths, prefix):
    """Completes current prefix using CDPATH"""
    env = XSH.env
    csc = env.get("CASE_SENSITIVE_COMPLETIONS")
    glob_sorted = env.get("GLOB_SORTED")
    for cdp in env.get("CDPATH"):
        test_glob = os.path.join(cdp, prefix) + "*"
        for s in xt.iglobpath(
            test_glob, ignore_case=(not csc), sort_result=glob_sorted
        ):
            if os.path.isdir(s):
                paths.add(os.path.relpath(s, cdp))


def _quote_to_use(x):
    single = "'"
    double = '"'
    if single in x and double not in x:
        return double
    else:
        return single


def _is_directory_in_cdpath(path):
    env = XSH.env
    for cdp in env.get("CDPATH"):
        if os.path.isdir(os.path.join(cdp, path)):
            return True
    return False


def _quote_paths(paths, start, end, append_end=True, cdpath=False):
    expand_path = XSH.expand_path
    out = set()
    space = " "
    backslash = "\\"
    double_backslash = "\\\\"
    slash = xt.get_sep()
    orig_start = start
    orig_end = end
    # quote on all or none, to make readline completes to max prefix
    need_quotes = any(
        re.search(PATTERN_NEED_QUOTES, x) or (backslash in x and slash != backslash)
        for x in paths
    )

    for s in paths:
        start = orig_start
        end = orig_end
        if start == "" and need_quotes:
            start = end = _quote_to_use(s)
        expanded = expand_path(s)
        if os.path.isdir(expanded) or (cdpath and _is_directory_in_cdpath(expanded)):
            _tail = slash
        elif end == "":
            _tail = space
        else:
            _tail = ""
        if start != "" and "r" not in start and backslash in s:
            start = "r%s" % start
        s = s + _tail
        if end != "":
            if "r" not in start.lower():
                s = s.replace(backslash, double_backslash)
        if end in s:
            s = s.replace(end, "".join("\\%s" % i for i in end))
        s = start + s + end if append_end else start + s
        out.add(s)
    return out, need_quotes


def _joinpath(path):
    # convert our tuple representation back into a string representing a path
    if path is None:
        return ""
    elif len(path) == 0:
        return ""
    elif path == ("",):
        return xt.get_sep()
    elif path[0] == "":
        return xt.get_sep() + _normpath(os.path.join(*path))
    else:
        return _normpath(os.path.join(*path))


def _splitpath(path):
    # convert a path into an intermediate tuple representation
    # if this tuple starts with '', it means that the path was an absolute path
    path = _normpath(path)
    if path.startswith(xt.get_sep()):
        pre = ("",)
    else:
        pre = ()
    return pre + _splitpath_helper(path, ())


def _splitpath_helper(path, sofar=()):
    folder, path = os.path.split(path)
    if path:
        sofar = sofar + (path,)
    if not folder or folder == xt.get_sep():
        return sofar[::-1]
    elif xp.ON_WINDOWS and not path:
        return os.path.splitdrive(folder)[:1] + sofar[::-1]
    elif xp.ON_WINDOWS and os.path.splitdrive(path)[0]:
        return sofar[::-1]
    return _splitpath_helper(folder, sofar)


def subsequence_match(ref, typed, csc):
    """
    Detects whether typed is a subsequence of ref.

    Returns ``True`` if the characters in ``typed`` appear (in order) in
    ``ref``, regardless of exactly where in ``ref`` they occur.  If ``csc`` is
    ``False``, ignore the case of ``ref`` and ``typed``.

    Used in "subsequence" path completion (e.g., ``~/u/ro`` expands to
    ``~/lou/carcohl``)
    """
    if csc:
        return _subsequence_match_iter(ref, typed)
    else:
        return _subsequence_match_iter(ref.lower(), typed.lower())


def _subsequence_match_iter(ref, typed):
    if len(typed) == 0:
        return True
    elif len(ref) == 0:
        return False
    elif ref[0] == typed[0]:
        return _subsequence_match_iter(ref[1:], typed[1:])
    else:
        return _subsequence_match_iter(ref[1:], typed)


def _expand_one(sofar, nextone, csc):
    out = set()
    glob_sorted = XSH.env.get("GLOB_SORTED")
    for i in sofar:
        _glob = os.path.join(_joinpath(i), "*") if i is not None else "*"
        for j in xt.iglobpath(_glob, sort_result=glob_sorted):
            j = os.path.basename(j)
            if subsequence_match(j, nextone, csc):
                out.add((i or ()) + (j,))
    return out


def _complete_path_raw(prefix, line, start, end, ctx, cdpath=True, filtfunc=None):
    """Completes based on a path name."""
    # string stuff for automatic quoting
    path_str_start = ""
    path_str_end = ""
    append_end = True
    p = _path_from_partial_string(line, end)
    lprefix = len(prefix)
    if p is not None:
        lprefix = len(p[0])
        # Compensate for 'p' if p-string variant
        pstring_pre = _get_normalized_pstring_quote(p[2])[0]
        if pstring_pre in ("pr", "p"):
            lprefix += 1
        prefix = p[1]
        path_str_start = p[2]
        path_str_end = p[3]
        if len(line) >= end + 1 and line[end] == path_str_end:
            append_end = False
    tilde = "~"
    paths = set()
    env = XSH.env
    csc = env.get("CASE_SENSITIVE_COMPLETIONS")
    glob_sorted = env.get("GLOB_SORTED")
    prefix = glob.escape(prefix)
    for s in xt.iglobpath(prefix + "*", ignore_case=(not csc), sort_result=glob_sorted):
        paths.add(s)
    if len(paths) == 0 and env.get("SUBSEQUENCE_PATH_COMPLETION"):
        # this block implements 'subsequence' matching, similar to fish and zsh.
        # matches are based on subsequences, not substrings.
        # e.g., ~/u/ro completes to ~/lou/carcolh
        # see above functions for details.
        p = _splitpath(os.path.expanduser(prefix))
        p_len = len(p)
        if p_len != 0:
            relative_char = ["", ".", ".."]
            if p[0] in relative_char:
                i = 0
                while i < p_len and p[i] in relative_char:
                    i += 1
                basedir = p[:i]
                p = p[i:]
            else:
                basedir = None
            matches_so_far = {basedir}
            for i in p:
                matches_so_far = _expand_one(matches_so_far, i, csc)
            paths |= {_joinpath(i) for i in matches_so_far}
    if len(paths) == 0 and env.get("FUZZY_PATH_COMPLETION"):
        threshold = env.get("SUGGEST_THRESHOLD")
        for s in xt.iglobpath(
            os.path.dirname(prefix) + "*",
            ignore_case=(not csc),
            sort_result=glob_sorted,
        ):
            if xt.levenshtein(prefix, s, threshold) < threshold:
                paths.add(s)
    if cdpath and cd_in_command(line):
        _add_cdpaths(paths, prefix)
    paths = set(filter(filtfunc, paths))
    if tilde in prefix:
        home = os.path.expanduser(tilde)
        paths = {s.replace(home, tilde) for s in paths}
    paths, _ = _quote_paths(
        {_normpath(s) for s in paths}, path_str_start, path_str_end, append_end, cdpath
    )
    paths.update(filter(filtfunc, _dots(prefix)))
    return paths, lprefix


@contextual_completer
def complete_path(context):
    if context.command:
        return contextual_complete_path(context.command)
    elif context.python:
        line = context.python.prefix
        # simple prefix _complete_path_raw will handle gracefully:
        prefix = line.rsplit(" ", 1)[1]
        return _complete_path_raw(prefix, line, len(line) - len(prefix), len(line), {})
    return set(), 0


def contextual_complete_path(command: CommandContext, cdpath=True, filtfunc=None):
    # ``_complete_path_raw`` may add opening quotes:
    prefix = command.raw_prefix

    completions, lprefix = _complete_path_raw(
        prefix,
        prefix,
        0,
        len(prefix),
        ctx={},
        cdpath=cdpath,
        filtfunc=filtfunc,
    )

    # ``_complete_path_raw`` may have added closing quotes:
    rich_completions = {
        RichCompletion(comp, append_closing_quote=False) for comp in completions
    }

    return rich_completions, lprefix


def complete_dir(command: CommandContext):
    return contextual_complete_path(command, filtfunc=os.path.isdir)

#
# pip
#
"""Completers for pip."""
# pylint: disable=invalid-name, missing-docstring, unsupported-membership-test
# pylint: disable=unused-argument, not-an-iterable
# amalgamated re
# amalgamated subprocess
# amalgamated xonsh.lazyasd
# amalgamated xonsh.completers.tools
# amalgamated from xonsh.parsers.completion_context import CommandContext
PIP_LIST_COMMANDS = {"uninstall", "show"}


@xl.lazyobject
def PIP_RE():
    return re.compile(r"\bx?pip(?:\d|\.)*$")


@xl.lazyobject
def PACKAGE_IGNORE_PATTERN():
    # These are the first and second lines in `pip list`'s output
    return re.compile(r"^Package$|^-+$")


@xl.lazyobject
def ALL_COMMANDS():
    try:
        help_text = str(
            subprocess.check_output(["pip", "--help"], stderr=subprocess.DEVNULL)
        )
    except FileNotFoundError:
        try:
            help_text = str(
                subprocess.check_output(["pip3", "--help"], stderr=subprocess.DEVNULL)
            )
        except FileNotFoundError:
            return []
    commands = re.findall(r"  (\w+)  ", help_text)
    return [c for c in commands if c not in ["completion", "help"]]


@contextual_command_completer
def complete_pip(context: CommandContext):
    """Completes python's package manager pip"""
    prefix = context.prefix
    if context.arg_index == 0 or (not PIP_RE.search(context.args[0].value)):
        return None
    filter_func = get_filter_function()

    if context.arg_index == 2 and context.args[1].value in PIP_LIST_COMMANDS:
        # `pip show PREFIX` - complete package names
        try:
            enc_items = subprocess.check_output(
                [context.args[0].value, "list"], stderr=subprocess.DEVNULL
            )
        except FileNotFoundError:
            return None
        packages = (
            line.split(maxsplit=1)[0] for line in enc_items.decode("utf-8").splitlines()
        )
        return {
            package
            for package in packages
            if filter_func(package, prefix)
            and not PACKAGE_IGNORE_PATTERN.match(package)
        }

    if context.arg_index == 1:
        # `pip PREFIX` - complete pip commands
        suggestions = {
            RichCompletion(c, append_space=True)
            for c in ALL_COMMANDS
            if filter_func(c, prefix)
        }
        return suggestions

    return None

#
# python
#
"""Completers for Python code"""
# amalgamated re
# amalgamated sys
# amalgamated inspect
builtins = _LazyModule.load('builtins', 'builtins')
importlib = _LazyModule.load('importlib', 'importlib')
warnings = _LazyModule.load('warnings', 'warnings')
cabc = _LazyModule.load('collections', 'collections.abc', 'cabc')
from xonsh.parsers.completion_context import PythonContext
# amalgamated xonsh.tools
# amalgamated xonsh.lazyasd
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.completers.tools
@xl.lazyobject
def RE_ATTR():
    return re.compile(r"([^\s\(\)]+(\.[^\s\(\)]+)*)\.(\w*)$")


@xl.lazyobject
def XONSH_EXPR_TOKENS():
    return {
        RichCompletion("and", append_space=True),
        "else",
        RichCompletion("for", append_space=True),
        RichCompletion("if", append_space=True),
        RichCompletion("in", append_space=True),
        RichCompletion("is", append_space=True),
        RichCompletion("lambda", append_space=True),
        RichCompletion("not", append_space=True),
        RichCompletion("or", append_space=True),
        "+",
        "-",
        "/",
        "//",
        "%",
        "**",
        "|",
        "&",
        "~",
        "^",
        ">>",
        "<<",
        "<",
        "<=",
        ">",
        ">=",
        "==",
        "!=",
        RichCompletion(",", append_space=True),
        "?",
        "??",
        "$(",
        "${",
        "$[",
        "...",
        "![",
        "!(",
        "@(",
        "@$(",
        "@",
    }


@xl.lazyobject
def XONSH_STMT_TOKENS():
    return {
        RichCompletion("as", append_space=True),
        RichCompletion("assert", append_space=True),
        "break",
        RichCompletion("class", append_space=True),
        "continue",
        RichCompletion("def", append_space=True),
        RichCompletion("del", append_space=True),
        RichCompletion("elif", append_space=True),
        RichCompletion("except", append_space=True),
        "finally:",
        RichCompletion("from", append_space=True),
        RichCompletion("global", append_space=True),
        RichCompletion("import", append_space=True),
        RichCompletion("nonlocal", append_space=True),
        "pass",
        RichCompletion("raise", append_space=True),
        RichCompletion("return", append_space=True),
        "try:",
        RichCompletion("while", append_space=True),
        RichCompletion("with", append_space=True),
        RichCompletion("yield", append_space=True),
        "-",
        "/",
        "//",
        "%",
        "**",
        "|",
        "&",
        "~",
        "^",
        ">>",
        "<<",
        "<",
        "<=",
        "->",
        "=",
        "+=",
        "-=",
        "*=",
        "/=",
        "%=",
        "**=",
        ">>=",
        "<<=",
        "&=",
        "^=",
        "|=",
        "//=",
        ";",
        ":",
        "..",
    }


@xl.lazyobject
def XONSH_TOKENS():
    return set(XONSH_EXPR_TOKENS) | set(XONSH_STMT_TOKENS)


@contextual_completer
def complete_python(context: CompletionContext) -> CompleterResult:
    """
    Completes based on the contents of the current Python environment,
    the Python built-ins, and xonsh operators.
    If there are no matches, split on common delimiters and try again.
    """
    if context.python is None:
        return None

    if context.command and context.command.arg_index != 0:
        # this can be a command (i.e. not a subexpression)
        first = context.command.args[0].value
        ctx = context.python.ctx or {}
        if first in XSH.commands_cache and first not in ctx:  # type: ignore
            # this is a known command, so it won't be python code
            return None

    line = context.python.multiline_code
    prefix = (line.rsplit(maxsplit=1) or [""])[-1]
    rtn = _complete_python(prefix, context.python)
    if not rtn:
        prefix = (
            re.split(r"\(|=|{|\[|,", prefix)[-1]
            if not prefix.startswith(",")
            else prefix
        )
        rtn = _complete_python(prefix, context.python)
    return rtn, len(prefix)


def _complete_python(prefix, context: PythonContext):
    """
    Completes based on the contents of the current Python environment,
    the Python built-ins, and xonsh operators.
    """
    line = context.multiline_code
    end = context.cursor_index
    ctx = context.ctx
    filt = get_filter_function()
    rtn = set()
    if ctx is not None:
        if "." in prefix:
            rtn |= attr_complete(prefix, ctx, filt)
        args = python_signature_complete(prefix, line, end, ctx, filt)
        rtn |= args
        rtn |= {s for s in ctx if filt(s, prefix)}
    else:
        args = ()
    if len(args) == 0:
        # not in a function call, so we can add non-expression tokens
        rtn |= {s for s in XONSH_TOKENS if filt(s, prefix)}
    else:
        rtn |= {s for s in XONSH_EXPR_TOKENS if filt(s, prefix)}
    rtn |= {s for s in dir(builtins) if filt(s, prefix)}
    return rtn


def _turn_off_warning(func):
    """Decorator to turn off warning temporarily."""

    def wrapper(*args, **kwargs):
        warnings.filterwarnings("ignore")
        r = func(*args, **kwargs)
        warnings.filterwarnings("once", category=DeprecationWarning)
        return r

    return wrapper


def _safe_eval(expr, ctx):
    """Safely tries to evaluate an expression. If this fails, it will return
    a (None, None) tuple.
    """
    _ctx = None
    xonsh_safe_eval = XSH.execer.eval
    try:
        val = xonsh_safe_eval(expr, ctx, ctx, transform=False)
        _ctx = ctx
    except Exception:
        try:
            val = xonsh_safe_eval(expr, builtins.__dict__, transform=False)
            _ctx = builtins.__dict__
        except Exception:
            val = _ctx = None
    return val, _ctx


@_turn_off_warning
def attr_complete(prefix, ctx, filter_func):
    """Complete attributes of an object."""
    attrs = set()
    m = RE_ATTR.match(prefix)
    if m is None:
        return attrs
    expr, attr = m.group(1, 3)
    expr = xt.subexpr_from_unbalanced(expr, "(", ")")
    expr = xt.subexpr_from_unbalanced(expr, "[", "]")
    expr = xt.subexpr_from_unbalanced(expr, "{", "}")
    val, _ctx = _safe_eval(expr, ctx)
    if val is None and _ctx is None:
        return attrs
    if len(attr) == 0:
        opts = [o for o in dir(val) if not o.startswith("_")]
    else:
        opts = [o for o in dir(val) if filter_func(o, attr)]
    prelen = len(prefix)
    for opt in opts:
        # check whether these options actually work (e.g., disallow 7.imag)
        _expr = "{0}.{1}".format(expr, opt)
        _val_, _ctx_ = _safe_eval(_expr, _ctx)
        if _val_ is None and _ctx_ is None:
            continue
        a = getattr(val, opt)
        if XSH.env["COMPLETIONS_BRACKETS"]:
            if callable(a):
                rpl = opt + "("
            elif isinstance(a, (cabc.Sequence, cabc.Mapping)):
                rpl = opt + "["
            else:
                rpl = opt
        else:
            rpl = opt
        # note that prefix[:prelen-len(attr)] != prefix[:-len(attr)]
        # when len(attr) == 0.
        comp = prefix[: prelen - len(attr)] + rpl
        attrs.add(comp)
    return attrs


@_turn_off_warning
def python_signature_complete(prefix, line, end, ctx, filter_func):
    """Completes a python function (or other callable) call by completing
    argument and keyword argument names.
    """
    front = line[:end]
    if xt.is_balanced(front, "(", ")"):
        return set()
    funcname = xt.subexpr_before_unbalanced(front, "(", ")")
    val, _ctx = _safe_eval(funcname, ctx)
    if val is None:
        return set()
    try:
        sig = inspect.signature(val)
    except ValueError:
        return set()
    args = {p + "=" for p in sig.parameters if filter_func(p, prefix)}
    return args


@contextual_completer
def complete_import(context: CompletionContext):
    """
    Completes module names and contents for "import ..." and "from ... import
    ..."
    """
    if not (context.command and context.python):
        # Imports are only possible in independent lines (not in `$()` or `@()`).
        # This means it's python code, but also can be a command as far as the parser is concerned.
        return None

    command = context.command

    if command.opening_quote:
        # can't have a quoted import
        return None

    arg_index = command.arg_index
    prefix = command.prefix
    args = command.args

    if arg_index == 1 and args[0].value == "from":
        # completing module to import
        return {"{} ".format(i) for i in complete_module(prefix)}
    if arg_index >= 1 and args[0].value == "import":
        # completing module to import
        return complete_module(prefix)
    if arg_index == 2 and args[0].value == "from":
        return {RichCompletion("import", append_space=True)}
    if arg_index > 2 and args[0].value == "from" and args[2].value == "import":
        # complete thing inside a module
        try:
            mod = importlib.import_module(args[1].value)
        except ImportError:
            return set()
        out = {i[0] for i in inspect.getmembers(mod) if i[0].startswith(prefix)}
        return out
    return set()


def complete_module(prefix):
    return {s for s in sys.modules if get_filter_function()(s, prefix)}

#
# xompletions
#
"""Provides completions for xonsh internal utilities"""

# amalgamated from xonsh.parsers.completion_context import CommandContext
xx = _LazyModule.load('xonsh', 'xonsh.xontribs', 'xx')
xmt = _LazyModule.load('xonsh', 'xonsh.xontribs_meta', 'xmt')
# amalgamated xonsh.tools
from xonsh.xonfig import XONFIG_MAIN_ACTIONS
# amalgamated xonsh.completers.tools
@contextual_command_completer_for("xonfig")
def complete_xonfig(command: CommandContext):
    """Completion for ``xonfig``"""
    curix = command.arg_index
    if curix == 1:
        possible = set(XONFIG_MAIN_ACTIONS.keys()) | {"-h"}
    elif curix == 2 and command.args[1].value == "colors":
        possible = set(xt.color_style_names())
    else:
        raise StopIteration
    return {i for i in possible if i.startswith(command.prefix)}


def _list_installed_xontribs():
    meta = xmt.get_xontribs()
    installed = []
    for name in meta:
        spec = xx.find_xontrib(name)
        if spec is not None:
            installed.append(spec.name.rsplit(".")[-1])

    return installed


@contextual_command_completer_for("xontrib")
def complete_xontrib(command: CommandContext):
    """Completion for ``xontrib``"""
    curix = command.arg_index
    if curix == 1:
        possible = {"list", "load"}
    elif curix == 2 and command.args[1].value == "load":
        possible = _list_installed_xontribs()
    else:
        raise StopIteration

    return {i for i in possible if i.startswith(command.prefix)}

#
# _aliases
#
ap = _LazyModule.load('argparse', 'argparse', 'ap')
xcli = _LazyModule.load('xonsh', 'xonsh.cli_utils', 'xcli')
# amalgamated xonsh.lazyasd
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.completers.completer
_add_one_completer = add_one_completer


def _remove_completer(args):
    """for backward compatibility"""
    return remove_completer(args[0])


def _register_completer(name: str, func: str, pos="start", stack=None):
    """adds a new completer to xonsh

    Parameters
    ----------
    name
        unique name to use in the listing (run "completer list" to see the
        current completers in order)

    func
        the name of a completer function to use.  This should be a function
         of the following arguments, and should return a set of valid completions
         for the given prefix.  If this completer should not be used in a given
         context, it should return an empty set or None.

         Arguments to FUNC:
           * prefix: the string to be matched
           * line: a string representing the whole current line, for context
           * begidx: the index at which prefix starts in line
           * endidx: the index at which prefix ends in line
           * ctx: the current Python environment

         If the completer expands the prefix in any way, it should return a tuple
         of two elements: the first should be the set of completions, and the
         second should be the length of the modified prefix (for an example, see
         xonsh.completers.path.complete_path).

    pos
        position into the list of completers at which the new
        completer should be added.  It can be one of the following values:
        * "start" indicates that the completer should be added to the start of
                 the list of completers (it should be run before all other exclusive completers)
        * "end" indicates that the completer should be added to the end of the
               list of completers (it should be run after all others)
        * ">KEY", where KEY is a pre-existing name, indicates that this should
                 be added after the completer named KEY
        * "<KEY", where KEY is a pre-existing name, indicates that this should
                 be added before the completer named KEY
        (Default value: "start")
    """
    err = None
    func_name = func
    xsh = XSH
    if name in xsh.completers:
        err = f"The name {name} is already a registered completer function."
    else:
        if func_name in xsh.ctx:
            func = xsh.ctx[func_name]
            if not callable(func):
                err = f"{func_name} is not callable"
        else:
            for frame_info in stack:
                frame = frame_info[0]
                if func_name in frame.f_locals:
                    func = frame.f_locals[func_name]
                    break
                elif func_name in frame.f_globals:
                    func = frame.f_globals[func_name]
                    break
            else:
                err = "No such function: %s" % func_name
    if err is None:
        _add_one_completer(name, func, pos)
    else:
        return None, err + "\n", 1


@xl.lazyobject
def _parser() -> ap.ArgumentParser:
    parser = xcli.make_parser(completer_alias)
    commands = parser.add_subparsers(title="commands")

    xcli.make_parser(
        _register_completer,
        commands,
        params={
            "name": {},
            "func": {},
            "pos": {"default": "start", "nargs": "?"},
        },
        prog="add",
    )

    xcli.make_parser(
        remove_completer,
        commands,
        params={"name": {}},
        prog="remove",
    )

    xcli.make_parser(list_completers, commands, prog="list")
    return parser


def completer_alias(args, stdin=None, stdout=None, stderr=None, spec=None, stack=None):
    """CLI to add/remove/list xonsh auto-complete functions"""
    ns = _parser.parse_args(args)
    kwargs = vars(ns)
    return xcli.dispatch(**kwargs, stdin=stdin, stdout=stdout, stack=stack)

#
# base
#
"""Base completer for xonsh."""
# amalgamated typing
# amalgamated collections.abc
# amalgamated from xonsh.parsers.completion_context import CompletionContext
# amalgamated xonsh.completers.tools
# amalgamated xonsh.completers.path
# amalgamated xonsh.completers.python
# amalgamated xonsh.completers.commands
@contextual_completer
def complete_base(context: CompletionContext):
    """If the line is empty, complete based on valid commands, python names,
    and paths.  If we are completing the first argument, complete based on
    valid commands and python names.
    """
    out: tp.Set[Completion] = set()
    if context.command is None or context.command.arg_index != 0:
        # don't do unnecessary completions
        return out

    # get and unpack python completions
    python_comps = complete_python(context) or set()
    if isinstance(python_comps, cabc.Sequence):
        python_comps, python_comps_len = python_comps  # type: ignore
        out.update(apply_lprefix(python_comps, python_comps_len))
    else:
        out.update(python_comps)

    # add command completions
    out.update(complete_command(context.command))

    # add paths, if needed
    if not context.command.prefix:
        path_comps, path_comp_len = contextual_complete_path(
            context.command, cdpath=False
        )
        out.update(apply_lprefix(path_comps, path_comp_len))

    return out

#
# bash
#
"""Xonsh hooks into bash completions."""

# amalgamated xonsh.tools
# amalgamated xonsh.platform
# amalgamated xonsh.completers.path
# amalgamated xonsh.completers.bash_completion
# amalgamated xonsh.completers.tools
# amalgamated from xonsh.parsers.completion_context import CommandContext
# amalgamated from xonsh.built_ins import XSH
@contextual_command_completer
def complete_from_bash(context: CommandContext):
    """Completes based on results from BASH completion."""
    env = XSH.env.detype()  # type: ignore
    paths = XSH.env.get("BASH_COMPLETIONS", ())  # type: ignore
    command = xp.bash_command()
    args = [arg.value for arg in context.args]
    prefix = context.prefix  # without the quotes
    args.insert(context.arg_index, prefix)
    line = " ".join(args)

    # lengths of all args + joining spaces
    begidx = sum(len(a) for a in args[: context.arg_index]) + context.arg_index
    endidx = begidx + len(prefix)

    opening_quote = context.opening_quote
    closing_quote = context.closing_quote
    if closing_quote and not context.is_after_closing_quote:
        # there already are closing quotes after our cursor, don't complete new ones (i.e. `ls "/pro<TAB>"`)
        closing_quote = ""
    elif opening_quote and not closing_quote:
        # get the proper closing quote
        closing_quote = xt.RE_STRING_START.sub("", opening_quote)

    comps, lprefix = bash_completions(
        prefix,
        line,
        begidx,
        endidx,
        env=env,
        paths=paths,
        command=command,
        quote_paths=_quote_paths,
        line_args=args,
        opening_quote=opening_quote,
        closing_quote=closing_quote,
        arg_index=context.arg_index,
    )

    def enrich_comps(comp: str):
        append_space = False
        if comp.endswith(" "):
            append_space = True
            comp = comp.rstrip()

        # ``bash_completions`` may have added closing quotes:
        return RichCompletion(
            comp, append_closing_quote=False, append_space=append_space
        )

    comps = set(map(enrich_comps, comps))

    if lprefix == len(prefix):
        lprefix += len(context.opening_quote)
    if context.is_after_closing_quote:
        # since bash doesn't see the closing quote, we need to add its length to lprefix
        lprefix += len(context.closing_quote)

    return comps, lprefix

#
# dirs
#
# amalgamated xonsh.completers.man
# amalgamated xonsh.completers.path
# amalgamated xonsh.completers.tools
# amalgamated from xonsh.parsers.completion_context import CompletionContext, CommandContext
@contextual_command_completer_for("cd")
def complete_cd(command: CommandContext):
    """
    Completion for "cd", includes only valid directory names.
    """
    results, lprefix = complete_dir(command)
    if len(results) == 0:
        raise StopIteration
    return results, lprefix


@contextual_command_completer_for("rmdir")
def complete_rmdir(command: CommandContext):
    """
    Completion for "rmdir", includes only valid directory names.
    """
    opts = complete_from_man(CompletionContext(command))
    comps, lp = complete_dir(command)
    if len(comps) == 0 and len(opts) == 0:
        raise StopIteration
    return comps | opts, lp

#
# init
#
"""Constructor for xonsh completer objects."""
# amalgamated collections
# amalgamated xonsh.completers.pip
# amalgamated xonsh.completers.man
# amalgamated xonsh.completers.bash
# amalgamated xonsh.completers.base
# amalgamated xonsh.completers.path
# amalgamated xonsh.completers.dirs
# amalgamated xonsh.completers.python
# amalgamated xonsh.completers.commands
# amalgamated xonsh.completers.completer
# amalgamated xonsh.completers.xompletions
# amalgamated xonsh.completers.environment
def default_completers():
    """Creates a copy of the default completers."""
    return collections.OrderedDict(
        [
            # non-exclusive completers:
            ("end_proc_tokens", complete_end_proc_tokens),
            ("end_proc_keywords", complete_end_proc_keywords),
            ("environment_vars", complete_environment_vars),
            # exclusive completers:
            ("base", complete_base),
            ("completer", complete_completer),
            ("skip", complete_skipper),
            ("pip", complete_pip),
            ("cd", complete_cd),
            ("rmdir", complete_rmdir),
            ("xonfig", complete_xonfig),
            ("xontrib", complete_xontrib),
            ("import", complete_import),
            ("bash", complete_from_bash),
            ("man", complete_from_man),
            ("python", complete_python),
            ("path", complete_path),
        ]
    )

