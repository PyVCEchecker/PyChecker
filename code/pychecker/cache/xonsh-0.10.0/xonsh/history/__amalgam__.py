"""Amalgamation of xonsh.history package, made up of the following modules, in order:

* base
* dummy
* json
* sqlite
* main

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
# base
#
# -*- coding: utf-8 -*-
"""Base class of Xonsh History backends."""
types = _LazyModule.load('types', 'types')
uuid = _LazyModule.load('uuid', 'uuid')
class HistoryEntry(types.SimpleNamespace):
    """Represent a command in history.

    Attributes
    ----------
    cmd: str
        The command as typed by the user, including newlines
    out: str
        The output of the command, if xonsh is configured to save it
    rtn: int
        The return of the command (ie, 0 on success)
    ts: two-tuple of floats
        The timestamps of when the command started and finished, including
        fractions.
    cwd: str
        The current working directory before execution the command.
    """


class History:
    """Xonsh history backend base class.

    History objects should be created via a subclass of History.

    History acts like a sequence that can be indexed to return
    ``HistoryEntry`` objects.

    Note that the most recent command is the last item in history.

    Attributes
    ----------
    rtns : sequence of ints
        The return of the command (ie, 0 on success)
    inps : sequence of strings
        The command as typed by the user, including newlines
    tss : sequence of two-tuples of floats
        The timestamps of when the command started and finished, including
        fractions
    outs : sequence of strings
        The output of the command, if xonsh is configured to save it
    gc : A garbage collector or None
        The garbage collector

    In all of these sequences, index 0 is the oldest and -1 (the last item)
    is the newest.
    """

    def __init__(self, sessionid=None, **kwargs):
        """Represents a xonsh session's history.

        Parameters
        ----------
        sessionid : int, uuid, str, optional
            Current session identifier, will generate a new sessionid if not
            set.
        """
        self.sessionid = uuid.uuid4() if sessionid is None else sessionid
        self.gc = None
        self.buffer = None
        self.filename = None
        self.inps = None
        self.rtns = None
        self.tss = None
        self.outs = None
        self.cwds = None
        self.last_cmd_rtn = None
        self.last_cmd_out = None
        self.hist_size = None
        self.hist_units = None
        self.remember_history = True

    def __len__(self):
        """Return the number of items in current session."""
        return len(list(self.items()))

    def __getitem__(self, item):
        """Retrieve history entries, see ``History`` docs for more info."""
        if isinstance(item, int):
            if item >= len(self):
                raise IndexError("history index out of range")
            return HistoryEntry(
                cmd=self.inps[item],
                out=self.outs[item],
                rtn=self.rtns[item],
                ts=self.tss[item],
                cwd=self.cwds[item],
            )
        elif isinstance(item, slice):
            cmds = self.inps[item]
            outs = self.outs[item]
            rtns = self.rtns[item]
            tss = self.tss[item]
            cwds = self.cwds[item]
            return [
                HistoryEntry(cmd=c, out=o, rtn=r, ts=t, cwd=cwd)
                for c, o, r, t, cwd in zip(cmds, outs, rtns, tss, cwds)
            ]
        else:
            raise TypeError(
                "history indices must be integers "
                "or slices, not {}".format(type(item))
            )

    def __setitem__(self, *args):
        raise PermissionError(
            "You cannot change history! " "you can create new though."
        )

    def append(self, cmd):
        """Append a command item into history.

        Parameters
        ----------
        cmd: dict
            This dict contains information about the command that is to be
            added to the history list. It should contain the keys ``inp``,
            ``rtn`` and ``ts``. These key names mirror the same names defined
            as instance variables in the ``HistoryEntry`` class.
        """
        pass

    def flush(self, **kwargs):
        """Flush the history items to disk from a buffer."""
        pass

    def items(self, newest_first=False):
        """Get history items of current session."""
        raise NotImplementedError

    def all_items(self, newest_first=False):
        """Get all history items."""
        raise NotImplementedError

    def info(self):
        """A collection of information about the shell history.

        Returns
        -------
        dict or collections.OrderedDict
            Contains history information as str key pairs.
        """
        raise NotImplementedError

    def run_gc(self, size=None, blocking=True):
        """Run the garbage collector.

        Parameters
        ----------
        size: None or tuple of a int and a string
            Determines the size and units of what would be allowed to remain.
        blocking: bool
            If set blocking, then wait until gc action finished.
        """
        pass

    def clear(self):
        """Clears the history of the current session from both the disk and
        memory.
        """
        pass

#
# dummy
#
# -*- coding: utf-8 -*-
"""Implements the xonsh history backend."""
collections = _LazyModule.load('collections', 'collections')
# amalgamated xonsh.history.base
class DummyHistory(History):
    """A dummy implement of history backend."""

    def append(self, cmd):
        pass

    def items(self, newest_first=False):
        yield {"inp": "dummy in action", "ts": 1464652800, "ind": 0}

    def all_items(self, newest_first=False):
        return self.items(newest_first=newest_first)

    def info(self):
        data = collections.OrderedDict()
        data["backend"] = "dummy"
        data["sessionid"] = str(self.sessionid)
        return data

#
# json
#
# -*- coding: utf-8 -*-
"""Implements JSON version of xonsh history backend."""
os = _LazyModule.load('os', 'os')
sys = _LazyModule.load('sys', 'sys')
time = _LazyModule.load('time', 'time')
# amalgamated collections
threading = _LazyModule.load('threading', 'threading')
cabc = _LazyModule.load('collections', 'collections.abc', 'cabc')
from xonsh.built_ins import XSH

try:
    import ujson as json
except ImportError:
    import json  # type: ignore

# amalgamated xonsh.history.base
xt = _LazyModule.load('xonsh', 'xonsh.tools', 'xt')
xlj = _LazyModule.load('xonsh', 'xonsh.lazyjson', 'xlj')
uptime = _LazyModule.load('xonsh', 'xonsh.xoreutils.uptime', 'uptime')
def _xhj_gc_commands_to_rmfiles(hsize, files):
    """Return number of units and list of history files to remove to get under the limit,

    Parameters:
    -----------
    hsize (int):  units of history, # of commands in this case.
    files ((mod_ts, num_commands, path)[], fsize): history files, sorted oldest first.

    Returns:
    --------
    hsize_removed (int):  units of history to be removed
    rm_files ((mod_ts, num_commands, path, fsize)[]): list of files to remove.
    """
    n = 0
    ncmds = 0
    for _, fcmds, _, _ in reversed(files):
        # `files` comes in with empty files included (now), don't need special handling to gc them here.

        if ncmds + fcmds > hsize:
            break
        ncmds += fcmds
        n += 1

    cmds_removed = 0
    files_removed = files[:-n]
    for _, fcmds, _, _ in files_removed:
        cmds_removed += fcmds

    return cmds_removed, files_removed


def _xhj_gc_files_to_rmfiles(hsize, files):
    """Return the number and list of history files to remove to get under the file limit."""
    rmfiles = files[:-hsize] if len(files) > hsize else []
    return len(rmfiles), rmfiles


def _xhj_gc_seconds_to_rmfiles(hsize, files):
    """Return excess duration and list of history files to remove to get under the age limit."""
    now = time.time()
    n = 0

    for ts, _, _, _ in files:
        if (now - ts) < hsize:
            break
        n += 1

    rmfiles = files[:n]
    size_over = now - hsize - rmfiles[0][0] if n > 0 else 0
    return size_over, rmfiles


def _xhj_gc_bytes_to_rmfiles(hsize, files):
    """Return the history files to remove to get under the byte limit."""
    n = 0
    nbytes = 0
    for _, _, _, fsize in reversed(files):
        if nbytes + fsize > hsize:
            break
        nbytes += fsize
        n += 1
    bytes_removed = 0
    files_removed = files[:-n]
    for _, _, _, fsize in files_removed:
        bytes_removed += fsize

    return bytes_removed, files_removed


def _xhj_get_data_dir():
    dir = xt.expanduser_abs_path(
        os.path.join(XSH.env.get("XONSH_DATA_DIR"), "history_json")
    )
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


def _xhj_get_history_files(sort=True, newest_first=False):
    """Find and return the history files. Optionally sort files by
    modify time.
    """
    data_dirs = [
        _xhj_get_data_dir(),
        XSH.env.get("XONSH_DATA_DIR"),  # backwards compatibility, remove in the future
    ]

    files = []
    for data_dir in data_dirs:
        data_dir = xt.expanduser_abs_path(data_dir)
        try:
            files += [
                os.path.join(data_dir, f)
                for f in os.listdir(data_dir)
                if f.startswith("xonsh-") and f.endswith(".json")
            ]
        except OSError:
            if XSH.env.get("XONSH_DEBUG"):
                xt.print_exception(
                    f"Could not collect xonsh history json files from {data_dir}"
                )
    if sort:
        files.sort(key=lambda x: os.path.getmtime(x), reverse=newest_first)

    custom_history_file = XSH.env.get("XONSH_HISTORY_FILE", None)
    if custom_history_file:
        custom_history_file = xt.expanduser_abs_path(custom_history_file)
        if custom_history_file not in files:
            files.insert(0, custom_history_file)
    return files


class JsonHistoryGC(threading.Thread):
    """Shell history garbage collection."""

    def __init__(self, wait_for_shell=True, size=None, force=False, *args, **kwargs):
        """Thread responsible for garbage collecting old history.

        May wait for shell (and for xonshrc to have been loaded) to start work.
        """
        super().__init__(*args, **kwargs)
        self.daemon = True
        self.size = size
        self.wait_for_shell = wait_for_shell
        self.force_gc = force
        self.gc_units_to_rmfiles = {
            "commands": _xhj_gc_commands_to_rmfiles,
            "files": _xhj_gc_files_to_rmfiles,
            "s": _xhj_gc_seconds_to_rmfiles,
            "b": _xhj_gc_bytes_to_rmfiles,
        }
        self.start()

    def run(self):
        while self.wait_for_shell:
            time.sleep(0.01)
        env = XSH.env  # pylint: disable=no-member
        xonsh_debug = env.get("XONSH_DEBUG", 0)
        if self.size is None:
            hsize, units = env.get("XONSH_HISTORY_SIZE")
        else:
            hsize, units = xt.to_history_tuple(self.size)
        files = self.files(only_unlocked=True)
        rmfiles_fn = self.gc_units_to_rmfiles.get(units)
        if rmfiles_fn is None:
            raise ValueError("Units type {0!r} not understood".format(units))

        size_over, rm_files = rmfiles_fn(hsize, files)
        hist = getattr(XSH, "history", None)
        if hist is not None:  # remember last gc pass history size
            hist.hist_size = size_over + hsize
            hist.hist_units = units

        if self.force_gc or size_over < hsize:
            i = 0
            for _, _, f, _ in rm_files:
                try:
                    os.remove(f)
                    if xonsh_debug:
                        print(
                            f"... Deleted {i:7d} of {len(rm_files):7d} history files.\r",
                            end="",
                        )
                    pass
                except OSError:
                    pass
                i += 1
        else:
            print(
                f"Warning: History garbage collection would discard more history ({size_over} {units}) than it would keep ({hsize}).\n"
                "Not removing any history for now. Either increase your limit ($XONSH_HISTORY_SIZE), or run `history gc --force`."
            )

    def files(self, only_unlocked=False):
        """Find and return the history files. Optionally locked files may be
        excluded.

        This is sorted by the last closed time. Returns a list of
        (file_size, timestamp, number of cmds, file name) tuples.
        """
        env = XSH.env
        if env is None:
            return []

        xonsh_debug = env.get("XONSH_DEBUG", 0)
        boot = uptime.boottime()
        fs = _xhj_get_history_files(sort=False)
        files = []
        time_start = time.time()
        for f in fs:
            try:
                cur_file_size = os.path.getsize(f)
                if cur_file_size == 0:
                    # collect empty files (for gc)
                    files.append((os.path.getmtime(f), 0, f, cur_file_size))
                    continue
                lj = xlj.LazyJSON(f, reopen=False)
                if lj.get("locked", False) and lj["ts"][0] < boot:
                    # computer was rebooted between when this history was created
                    # and now and so this history should be unlocked.
                    hist = lj.load()
                    lj.close()
                    hist["locked"] = False
                    with open(f, "w", newline="\n") as fp:
                        xlj.ljdump(hist, fp, sort_keys=True)
                    lj = xlj.LazyJSON(f, reopen=False)
                if only_unlocked and lj.get("locked", False):
                    continue
                # info: file size, closing timestamp, number of commands, filename
                ts = lj.get("ts", (0.0, None))
                files.append(
                    (ts[1] or ts[0], len(lj.sizes["cmds"]) - 1, f, cur_file_size)
                )
                lj.close()
                if xonsh_debug:
                    time_lag = time.time() - time_start
                    print(
                        f"[history.{json.__name__}] Enumerated {len(files):,d} history files for {time_lag:0.4f}s.\r",
                        end="",
                        file=sys.stderr,
                    )
            except (OSError, ValueError):
                continue
        files.sort()  # this sorts by elements of the tuple,
        # the first of which just happens to be file mod time.
        # so sort by oldest first.
        return files


class JsonHistoryFlusher(threading.Thread):
    """Flush shell history to disk periodically."""

    def __init__(
        self, filename, buffer, queue, cond, at_exit=False, skip=None, *args, **kwargs
    ):
        """Thread for flushing history."""
        super(JsonHistoryFlusher, self).__init__(*args, **kwargs)
        self.filename = filename
        self.buffer = buffer
        self.queue = queue
        queue.append(self)
        self.cond = cond
        self.at_exit = at_exit
        self.skip = skip
        if at_exit:
            self.dump()
            queue.popleft()
        else:
            self.start()

    def run(self):
        with self.cond:
            self.cond.wait_for(self.i_am_at_the_front)
            self.dump()
            self.queue.popleft()

    def i_am_at_the_front(self):
        """Tests if the flusher is at the front of the queue."""
        return self is self.queue[0]

    def dump(self):
        """Write the cached history to external storage."""
        opts = XSH.env.get("HISTCONTROL", "")
        last_inp = None
        cmds = []
        for cmd in self.buffer:
            if "ignoredups" in opts and cmd["inp"] == last_inp:
                # Skipping dup cmd
                if self.skip is not None:
                    self.skip(1)
                continue
            if "ignoreerr" in opts and cmd["rtn"] != 0:
                # Skipping failed cmd
                if self.skip is not None:
                    self.skip(1)
                continue

            cmds.append(cmd)
            last_inp = cmd["inp"]
        with open(self.filename, "r", newline="\n") as f:
            hist = xlj.LazyJSON(f).load()
        load_hist_len = len(hist["cmds"])
        hist["cmds"].extend(cmds)
        if self.at_exit:
            # todo: check why this is here.
            if "ts" in hist:
                hist["ts"][1] = time.time()  # apply end time
            hist["locked"] = False
        if not XSH.env.get("XONSH_STORE_STDOUT", False):
            [cmd.pop("out") for cmd in hist["cmds"][load_hist_len:] if "out" in cmd]
        with open(self.filename, "w", newline="\n") as f:
            xlj.ljdump(hist, f, sort_keys=True)


class JsonCommandField(cabc.Sequence):
    """A field in the 'cmds' portion of history."""

    def __init__(self, field, hist, default=None):
        """Represents a field in the 'cmds' portion of history.

        Will query the buffer for the relevant data, if possible. Otherwise it
        will lazily acquire data from the file.

        Parameters
        ----------
        field : str
            The name of the field to query.
        hist : History object
            The history object to query.
        default : optional
            The default value to return if key is not present.
        """
        self.field = field
        self.hist = hist
        self.default = default

    def __len__(self):
        return len(self.hist)

    def __getitem__(self, key):
        if not self.hist.remember_history:
            return ""

        size = len(self)
        if isinstance(key, slice):
            return [self[i] for i in range(*key.indices(size))]
        elif not isinstance(key, int):
            raise IndexError("JsonCommandField may only be indexed by int or slice.")
        elif size == 0:
            raise IndexError("JsonCommandField is empty.")
        # now we know we have an int
        key = size + key if key < 0 else key  # ensure key is non-negative
        bufsize = len(self.hist.buffer)
        if size - bufsize <= key:  # key is in buffer
            return self.hist.buffer[key + bufsize - size].get(self.field, self.default)
        # now we know we have to go into the file
        queue = self.hist._queue
        queue.append(self)
        with self.hist._cond:
            self.hist._cond.wait_for(self.i_am_at_the_front)
            with open(self.hist.filename, "r", newline="\n") as f:
                lj = xlj.LazyJSON(f, reopen=False)
                rtn = lj["cmds"][key].get(self.field, self.default)
                if isinstance(rtn, xlj.LJNode):
                    rtn = rtn.load()
            queue.popleft()
        return rtn

    def i_am_at_the_front(self):
        """Tests if the command field is at the front of the queue."""
        return self is self.hist._queue[0]


class JsonHistory(History):
    """Xonsh history backend implemented with JSON files.

    JsonHistory implements an extra action: ``diff``
    """

    def __init__(
        self,
        filename=None,
        sessionid=None,
        buffersize=100,
        gc=True,
        save_cwd=None,
        **meta,
    ):
        """Represents a xonsh session's history as an in-memory buffer that is
        periodically flushed to disk.

        Parameters
        ----------
        filename : str, optional
            Location of history file, defaults to
            ``$XONSH_DATA_DIR/history_json/xonsh-{sessionid}.json``.
        sessionid : int, uuid, str, optional
            Current session identifier, will generate a new sessionid if not
            set.
        buffersize : int, optional
            Maximum buffersize in memory.
        meta : optional
            Top-level metadata to store along with the history. The kwargs
            'cmds' and 'sessionid' are not allowed and will be overwritten.
        gc : bool, optional
            Run garbage collector flag.
        """
        super().__init__(sessionid=sessionid, **meta)
        if filename is None:
            # pylint: disable=no-member
            data_dir = _xhj_get_data_dir()
            self.filename = os.path.join(
                data_dir, "xonsh-{0}.json".format(self.sessionid)
            )
        else:
            self.filename = filename

        if self.filename and not os.path.exists(os.path.expanduser(self.filename)):
            meta["cmds"] = []
            meta["sessionid"] = str(self.sessionid)
            with open(self.filename, "w", newline="\n") as f:
                xlj.ljdump(meta, f, sort_keys=True)

            try:
                os.chmod(self.filename, 0o600)
            except Exception:  # pylint: disable=broad-except
                pass

        self.buffer = []
        self.buffersize = buffersize
        self._queue = collections.deque()
        self._cond = threading.Condition()
        self._len = 0
        self._skipped = 0
        self.last_cmd_out = None
        self.last_cmd_rtn = None
        self.gc = JsonHistoryGC() if gc else None
        # command fields that are known
        self.tss = JsonCommandField("ts", self)
        self.inps = JsonCommandField("inp", self)
        self.outs = JsonCommandField("out", self)
        self.rtns = JsonCommandField("rtn", self)
        self.cwds = JsonCommandField("cwd", self)
        self.save_cwd = (
            save_cwd
            if save_cwd is not None
            else XSH.env.get("XONSH_HISTORY_SAVE_CWD", True)
        )

    def __len__(self):
        return self._len - self._skipped

    def append(self, cmd):
        """Appends command to history. Will periodically flush the history to file.

        Parameters
        ----------
        cmd : dict
            This dict contains information about the command that is to be
            added to the history list. It should contain the keys ``inp``,
            ``rtn`` and ``ts``. These key names mirror the same names defined
            as instance variables in the ``HistoryEntry`` class.
            Additionally, an optional key ``spc`` may be present which will
            affect commands from being stored if ignorespace is in $HISTCONTROL.

        Returns
        -------
        hf : JsonHistoryFlusher or None
            The thread that was spawned to flush history
        """
        if not self.remember_history:
            return

        opts = XSH.env.get("HISTCONTROL", "")
        skipped_by_ignore_space = "ignorespace" in opts and cmd.get("spc")
        if skipped_by_ignore_space:
            return None

        self.buffer.append(cmd)
        self._len += 1  # must come before flushing

        if not self.save_cwd and "cwd" in cmd:
            del cmd["cwd"]

        try:
            del cmd["spc"]
        except KeyError:
            pass

        if len(self.buffer) >= self.buffersize:
            hf = self.flush()
        else:
            hf = None
        return hf

    def flush(self, at_exit=False):
        """Flushes the current command buffer to disk.

        Parameters
        ----------
        at_exit : bool, optional
            Whether the JsonHistoryFlusher should act as a thread in the
            background, or execute immediately and block.

        Returns
        -------
        hf : JsonHistoryFlusher or None
            The thread that was spawned to flush history
        """
        # Implicitly covers case of self.remember_history being False.
        if len(self.buffer) == 0:
            return

        def skip(num):
            self._skipped += num

        hf = JsonHistoryFlusher(
            self.filename,
            tuple(self.buffer),
            self._queue,
            self._cond,
            at_exit=at_exit,
            skip=skip,
        )
        self.buffer = []
        return hf

    def items(self, newest_first=False):
        """Display history items of current session."""
        if newest_first:
            items = zip(reversed(self.inps), reversed(self.tss))
        else:
            items = zip(self.inps, self.tss)
        for item, tss in items:
            yield {"inp": item.rstrip(), "ts": tss[0]}

    def all_items(self, newest_first=False, **kwargs):
        """
        Returns all history as found in XONSH_DATA_DIR.

        yield format: {'inp': cmd, 'rtn': 0, ...}
        """
        while self.gc and self.gc.is_alive():
            time.sleep(0.011)  # gc sleeps for 0.01 secs, sleep a beat longer
        for f in _xhj_get_history_files(newest_first=newest_first):
            try:
                json_file = xlj.LazyJSON(f, reopen=False)
            except ValueError:
                # Invalid json file
                continue
            try:
                commands = json_file.load()["cmds"]
            except (json.decoder.JSONDecodeError, ValueError):
                # file is corrupted somehow
                if XSH.env.get("XONSH_DEBUG") > 0:
                    msg = "xonsh history file {0!r} is not valid JSON"
                    print(msg.format(f), file=sys.stderr)
                continue
            if newest_first:
                commands = reversed(commands)
            for c in commands:
                yield {"inp": c["inp"].rstrip(), "ts": c["ts"][0]}
        # all items should also include session items
        yield from self.items()

    def info(self):
        data = collections.OrderedDict()
        data["backend"] = "json"
        data["sessionid"] = str(self.sessionid)
        data["filename"] = self.filename
        data["length"] = len(self)
        data["buffersize"] = self.buffersize
        data["bufferlength"] = len(self.buffer)
        envs = XSH.env
        data["gc options"] = envs.get("XONSH_HISTORY_SIZE")
        data["gc_last_size"] = f"{(self.hist_size, self.hist_units)}"
        return data

    def run_gc(self, size=None, blocking=True, force=False):
        self.gc = JsonHistoryGC(wait_for_shell=False, size=size, force=force)
        if blocking:
            while self.gc.is_alive():  # while waiting for gc.
                time.sleep(0.1)  # don't monopolize the thread (or Python GIL?)

    def clear(self):
        """Clears the current session's history from both memory and disk."""

        # Wipe history from memory. Keep sessionid and other metadata.
        self.buffer = []
        self.tss = JsonCommandField("ts", self)
        self.inps = JsonCommandField("inp", self)
        self.outs = JsonCommandField("out", self)
        self.rtns = JsonCommandField("rtn", self)
        self.cwds = JsonCommandField("cwd", self)
        self._len = 0
        self._skipped = 0

        # Flush empty history object to disk, overwriting previous data.
        self.flush()

#
# sqlite
#
# -*- coding: utf-8 -*-
"""Implements the xonsh history backend via sqlite3."""
# amalgamated collections
json = _LazyModule.load('json', 'json')
# amalgamated os
sqlite3 = _LazyModule.load('sqlite3', 'sqlite3')
# amalgamated sys
# amalgamated threading
# amalgamated time
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.history.base
# amalgamated xonsh.tools
XH_SQLITE_CACHE = threading.local()
XH_SQLITE_TABLE_NAME = "xonsh_history"
XH_SQLITE_CREATED_SQL_TBL = "CREATED_SQL_TABLE"


def _xh_sqlite_get_file_name():
    envs = XSH.env
    file_name = envs.get("XONSH_HISTORY_SQLITE_FILE")
    if not file_name:
        data_dir = envs.get("XONSH_DATA_DIR")
        file_name = os.path.join(data_dir, "xonsh-history.sqlite")
    return xt.expanduser_abs_path(file_name)


def _xh_sqlite_get_conn(filename=None):
    if filename is None:
        filename = _xh_sqlite_get_file_name()
    return sqlite3.connect(str(filename))


def _xh_sqlite_create_history_table(cursor):
    """Create Table for history items.

    Columns:
        info - JSON formatted, reserved for future extension.
        frequency - in case of HISTCONTROL=erasedups,
        it tracks the frequency of the inputs. helps in sorting autocompletion
    """
    if not getattr(XH_SQLITE_CACHE, XH_SQLITE_CREATED_SQL_TBL, False):
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS {}
                 (inp TEXT,
                  rtn INTEGER,
                  tsb REAL,
                  tse REAL,
                  sessionid TEXT,
                  out TEXT,
                  info TEXT,
                  frequency INTEGER default 1,
                  cwd TEXT
                 )
        """.format(
                XH_SQLITE_TABLE_NAME
            )
        )

        # add frequency column if not exists for backward compatibility
        try:
            cursor.execute(
                "ALTER TABLE "
                + XH_SQLITE_TABLE_NAME
                + " ADD COLUMN frequency INTEGER default 1"
            )
        except sqlite3.OperationalError:
            pass

        # add path column if not exists for backward compatibility
        try:
            cursor.execute(
                "ALTER TABLE " + XH_SQLITE_TABLE_NAME + " ADD COLUMN cwd TEXT"
            )
        except sqlite3.OperationalError:
            pass

        # add index on inp. since we query when erasedups is True
        cursor.execute(
            f"""\
CREATE INDEX IF NOT EXISTS  idx_inp_history
ON {XH_SQLITE_TABLE_NAME}(inp);"""
        )

        # mark that this function ran for this session
        setattr(XH_SQLITE_CACHE, XH_SQLITE_CREATED_SQL_TBL, True)


def _xh_sqlite_get_frequency(cursor, input):
    # type: (sqlite3.Cursor, str) -> int
    sql = "SELECT sum(frequency) FROM {} WHERE inp=?".format(XH_SQLITE_TABLE_NAME)
    cursor.execute(sql, (input,))
    return cursor.fetchone()[0] or 0


def _xh_sqlite_erase_dups(cursor, input):
    freq = _xh_sqlite_get_frequency(cursor, input)
    sql = "DELETE FROM {} WHERE inp=?".format(XH_SQLITE_TABLE_NAME)
    cursor.execute(sql, (input,))
    return freq


def _sql_insert(cursor, values):
    # type: (sqlite3.Cursor, dict) -> None
    """handy function to run insert query"""
    sql = "INSERT INTO {} ({}) VALUES ({});"
    fields = ", ".join(values)
    marks = ", ".join(["?"] * len(values))
    cursor.execute(
        sql.format(XH_SQLITE_TABLE_NAME, fields, marks), tuple(values.values())
    )


def _xh_sqlite_insert_command(cursor, cmd, sessionid, store_stdout, remove_duplicates):
    tss = cmd.get("ts", [None, None])
    values = collections.OrderedDict(
        [
            ("inp", cmd["inp"].rstrip()),
            ("rtn", cmd["rtn"]),
            ("tsb", tss[0]),
            ("tse", tss[1]),
            ("sessionid", sessionid),
        ]
    )
    if "cwd" in cmd:
        values["cwd"] = cmd["cwd"]
    if store_stdout and "out" in cmd:
        values["out"] = cmd["out"]
    if "info" in cmd:
        info = json.dumps(cmd["info"])
        values["info"] = info
    if remove_duplicates:
        values["frequency"] = _xh_sqlite_erase_dups(cursor, values["inp"]) + 1
    _sql_insert(cursor, values)


def _xh_sqlite_get_count(cursor, sessionid=None):
    sql = "SELECT count(*) FROM xonsh_history "
    params = []
    if sessionid is not None:
        sql += "WHERE sessionid = ? "
        params.append(str(sessionid))
    cursor.execute(sql, tuple(params))
    return cursor.fetchone()[0]


def _xh_sqlite_get_records(cursor, sessionid=None, limit=None, newest_first=False):
    sql = "SELECT inp, tsb, rtn, frequency, cwd FROM xonsh_history "
    params = []
    if sessionid is not None:
        sql += "WHERE sessionid = ? "
        params.append(sessionid)
    sql += "ORDER BY tsb "
    if newest_first:
        sql += "DESC "
    if limit is not None:
        sql += "LIMIT %d " % limit
    cursor.execute(sql, tuple(params))
    return cursor.fetchall()


def _xh_sqlite_delete_records(cursor, size_to_keep):
    sql = "SELECT min(tsb) FROM ("
    sql += "SELECT tsb FROM xonsh_history ORDER BY tsb DESC "
    sql += "LIMIT %d)" % size_to_keep
    cursor.execute(sql)
    result = cursor.fetchone()
    if not result:
        return
    max_tsb = result[0]
    sql = "DELETE FROM xonsh_history WHERE tsb < ?"
    result = cursor.execute(sql, (max_tsb,))
    return result.rowcount


def xh_sqlite_append_history(
    cmd, sessionid, store_stdout, filename=None, remove_duplicates=False
):
    with _xh_sqlite_get_conn(filename=filename) as conn:
        c = conn.cursor()
        _xh_sqlite_create_history_table(c)
        _xh_sqlite_insert_command(c, cmd, sessionid, store_stdout, remove_duplicates)
        conn.commit()


def xh_sqlite_get_count(sessionid=None, filename=None):
    with _xh_sqlite_get_conn(filename=filename) as conn:
        c = conn.cursor()
        return _xh_sqlite_get_count(c, sessionid=sessionid)


def xh_sqlite_items(sessionid=None, filename=None, newest_first=False):
    with _xh_sqlite_get_conn(filename=filename) as conn:
        c = conn.cursor()
        _xh_sqlite_create_history_table(c)
        return _xh_sqlite_get_records(c, sessionid=sessionid, newest_first=newest_first)


def xh_sqlite_delete_items(size_to_keep, filename=None):
    with _xh_sqlite_get_conn(filename=filename) as conn:
        c = conn.cursor()
        _xh_sqlite_create_history_table(c)
        return _xh_sqlite_delete_records(c, size_to_keep)


def xh_sqlite_wipe_session(sessionid=None, filename=None):
    """Wipe the current session's entries from the database."""
    sql = "DELETE FROM xonsh_history WHERE sessionid = ?"
    with _xh_sqlite_get_conn(filename=filename) as conn:
        c = conn.cursor()
        _xh_sqlite_create_history_table(c)
        c.execute(sql, (str(sessionid),))


class SqliteHistoryGC(threading.Thread):
    """Shell history garbage collection."""

    def __init__(self, wait_for_shell=True, size=None, filename=None, *args, **kwargs):
        """Thread responsible for garbage collecting old history.

        May wait for shell (and for xonshrc to have been loaded) to start work.
        """
        super().__init__(*args, **kwargs)
        self.daemon = True
        self.filename = filename
        self.size = size
        self.wait_for_shell = wait_for_shell
        self.start()

    def run(self):
        while self.wait_for_shell:
            time.sleep(0.01)
        if self.size is not None:
            hsize, units = xt.to_history_tuple(self.size)
        else:
            envs = XSH.env
            hsize, units = envs.get("XONSH_HISTORY_SIZE")
        if units != "commands":
            print(
                "sqlite backed history gc currently only supports "
                '"commands" as units',
                file=sys.stderr,
            )
            return
        if hsize < 0:
            return
        xh_sqlite_delete_items(hsize, filename=self.filename)


class SqliteHistory(History):
    """Xonsh history backend implemented with sqlite3."""

    def __init__(self, gc=True, filename=None, save_cwd=None, **kwargs):
        super().__init__(**kwargs)
        if filename is None:
            filename = _xh_sqlite_get_file_name()
        self.filename = filename
        self.gc = SqliteHistoryGC() if gc else None
        self._last_hist_inp = None
        self.inps = []
        self.rtns = []
        self.outs = []
        self.tss = []
        self.cwds = []
        self.save_cwd = (
            save_cwd
            if save_cwd is not None
            else XSH.env.get("XONSH_HISTORY_SAVE_CWD", True)
        )

        if not os.path.exists(self.filename):
            with _xh_sqlite_get_conn(filename=self.filename) as conn:
                if conn:
                    pass
            try:
                os.chmod(self.filename, 0o600)
            except Exception:  # pylint: disable=broad-except
                pass

        # during init rerun create command
        setattr(XH_SQLITE_CACHE, XH_SQLITE_CREATED_SQL_TBL, False)

    def append(self, cmd):
        if not self.remember_history:
            return
        envs = XSH.env
        inp = cmd["inp"].rstrip()
        self.inps.append(inp)
        self.outs.append(cmd.get("out"))
        self.rtns.append(cmd["rtn"])
        self.tss.append(cmd.get("ts", (None, None)))
        self.cwds.append(cmd.get("cwd", None))

        opts = envs.get("HISTCONTROL", "")
        if "ignoredups" in opts and inp == self._last_hist_inp:
            # Skipping dup cmd
            return
        if "ignoreerr" in opts and cmd["rtn"] != 0:
            # Skipping failed cmd
            return
        if "ignorespace" in opts and cmd.get("spc"):
            # Skipping cmd starting with space
            return
        if not self.save_cwd and "cwd" in cmd:
            del cmd["cwd"]

        try:
            del cmd["spc"]
        except KeyError:
            pass
        self._last_hist_inp = inp
        try:
            xh_sqlite_append_history(
                cmd,
                str(self.sessionid),
                store_stdout=envs.get("XONSH_STORE_STDOUT", False),
                filename=self.filename,
                remove_duplicates=("erasedups" in opts),
            )
        except sqlite3.OperationalError as err:
            print(f"SQLite History Backend Error: {err}")

    def all_items(self, newest_first=False, session_id=None):
        """Display all history items."""
        for inp, ts, rtn, freq, cwd in xh_sqlite_items(
            filename=self.filename, newest_first=newest_first, sessionid=session_id
        ):
            yield {"inp": inp, "ts": ts, "rtn": rtn, "frequency": freq, "cwd": cwd}

    def items(self, newest_first=False):
        """Display history items of current session."""
        yield from self.all_items(newest_first, session_id=str(self.sessionid))

    def info(self):
        data = collections.OrderedDict()
        data["backend"] = "sqlite"
        data["sessionid"] = str(self.sessionid)
        data["filename"] = self.filename
        data["session items"] = xh_sqlite_get_count(
            sessionid=self.sessionid, filename=self.filename
        )
        data["all items"] = xh_sqlite_get_count(filename=self.filename)
        envs = XSH.env
        data["gc options"] = envs.get("XONSH_HISTORY_SIZE")
        return data

    def run_gc(self, size=None, blocking=True):
        self.gc = SqliteHistoryGC(wait_for_shell=False, size=size)
        if blocking:
            while self.gc.is_alive():
                continue

    def clear(self):
        """Clears the current session's history from both memory and disk."""
        # Wipe memory
        self.inps = []
        self.rtns = []
        self.outs = []
        self.tss = []
        self.cwds = []

        xh_sqlite_wipe_session(sessionid=self.sessionid, filename=self.filename)

#
# main
#
# -*- coding: utf-8 -*-
"""Main entry points of the xonsh history."""
argparse = _LazyModule.load('argparse', 'argparse')
datetime = _LazyModule.load('datetime', 'datetime')
functools = _LazyModule.load('functools', 'functools')
# amalgamated json
# amalgamated os
# amalgamated sys
# amalgamated threading
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.history.base
# amalgamated xonsh.history.dummy
# amalgamated xonsh.history.json
# amalgamated xonsh.history.sqlite
xdh = _LazyModule.load('xonsh', 'xonsh.diff_history', 'xdh')
xla = _LazyModule.load('xonsh', 'xonsh.lazyasd', 'xla')
# amalgamated xonsh.tools
HISTORY_BACKENDS = {"dummy": DummyHistory, "json": JsonHistory, "sqlite": SqliteHistory}


def construct_history(**kwargs):
    """Construct the history backend object."""
    env = XSH.env
    backend = env.get("XONSH_HISTORY_BACKEND")
    if isinstance(backend, str) and backend in HISTORY_BACKENDS:
        kls_history = HISTORY_BACKENDS[backend]
    elif xt.is_class(backend):
        kls_history = backend
    elif isinstance(backend, History):
        return backend
    else:
        print(
            "Unknown history backend: {}. Using JSON version".format(backend),
            file=sys.stderr,
        )
        kls_history = JsonHistory
    return kls_history(**kwargs)


def _xh_session_parser(hist=None, newest_first=False, **kwargs):
    """Returns history items of current session."""
    if hist is None:
        hist = XSH.history
    return hist.items()


def _xh_all_parser(hist=None, newest_first=False, **kwargs):
    """Returns all history items."""
    if hist is None:
        hist = XSH.history
    return hist.all_items(newest_first=newest_first)


def _xh_find_histfile_var(file_list, default=None):
    """Return the path of the history file
    from the value of the envvar HISTFILE.
    """
    for f in file_list:
        f = xt.expanduser_abs_path(f)
        if not os.path.isfile(f):
            continue
        with open(f, "r") as rc_file:
            for line in rc_file:
                if line.startswith("HISTFILE="):
                    hist_file = line.split("=", 1)[1].strip("'\"\n")
                    hist_file = xt.expanduser_abs_path(hist_file)
                    if os.path.isfile(hist_file):
                        return hist_file
    else:
        if default:
            default = xt.expanduser_abs_path(default)
            if os.path.isfile(default):
                return default


def _xh_bash_hist_parser(location=None, **kwargs):
    """Yield commands from bash history file"""
    if location is None:
        location = _xh_find_histfile_var(
            [os.path.join("~", ".bashrc"), os.path.join("~", ".bash_profile")],
            os.path.join("~", ".bash_history"),
        )
    if location:
        with open(location, "r", errors="backslashreplace") as bash_hist:
            for ind, line in enumerate(bash_hist):
                yield {"inp": line.rstrip(), "ts": 0.0, "ind": ind}
    else:
        print("No bash history file", file=sys.stderr)


def _xh_zsh_hist_parser(location=None, **kwargs):
    """Yield commands from zsh history file"""
    if location is None:
        location = _xh_find_histfile_var(
            [os.path.join("~", ".zshrc"), os.path.join("~", ".zprofile")],
            os.path.join("~", ".zsh_history"),
        )
    if location:
        with open(location, "r", errors="backslashreplace") as zsh_hist:
            for ind, line in enumerate(zsh_hist):
                if line.startswith(":"):
                    try:
                        start_time, command = line.split(";", 1)
                    except ValueError:
                        # Invalid history entry
                        continue
                    try:
                        start_time = float(start_time.split(":")[1])
                    except ValueError:
                        start_time = 0.0
                    yield {"inp": command.rstrip(), "ts": start_time, "ind": ind}
                else:
                    yield {"inp": line.rstrip(), "ts": 0.0, "ind": ind}

    else:
        print("No zsh history file found", file=sys.stderr)


def _xh_filter_ts(commands, start_time, end_time):
    """Yield only the commands between start and end time."""
    for cmd in commands:
        if start_time <= cmd["ts"] < end_time:
            yield cmd


def _xh_get_history(
    session="session",
    *,
    slices=None,
    datetime_format=None,
    start_time=None,
    end_time=None,
    location=None
):
    """Get the requested portion of shell history.

    Parameters
    ----------
    session: {'session', 'all', 'xonsh', 'bash', 'zsh'}
        The history session to get.
    slices : list of slice-like objects, optional
        Get only portions of history.
    start_time, end_time: float, optional
        Filter commands by timestamp.
    location: string, optional
        The history file location (bash or zsh)

    Returns
    -------
    generator
       A filtered list of commands
    """
    cmds = []
    for i, item in enumerate(_XH_HISTORY_SESSIONS[session](location=location)):
        item["ind"] = i
        cmds.append(item)
    if slices:
        # transform/check all slices
        slices = [xt.ensure_slice(s) for s in slices]
        cmds = xt.get_portions(cmds, slices)
    if start_time or end_time:
        if start_time is None:
            start_time = 0.0
        else:
            start_time = xt.ensure_timestamp(start_time, datetime_format)
        if end_time is None:
            end_time = float("inf")
        else:
            end_time = xt.ensure_timestamp(end_time, datetime_format)
        cmds = _xh_filter_ts(cmds, start_time, end_time)
    return cmds


def _xh_show_history(hist, ns, stdout=None, stderr=None):
    """Show the requested portion of shell history.
    Accepts same parameters with `_xh_get_history`.
    """
    try:
        commands = _xh_get_history(
            ns.session,
            slices=ns.slices,
            start_time=ns.start_time,
            end_time=ns.end_time,
            datetime_format=ns.datetime_format,
        )
    except Exception as err:
        print("history: error: {}".format(err), file=stderr)
        return
    if ns.reverse:
        commands = reversed(list(commands))
    end = "\0" if ns.null_byte else "\n"
    if ns.numerate and ns.timestamp:
        for c in commands:
            dt = datetime.datetime.fromtimestamp(c["ts"])
            print(
                "{}:({}) {}".format(c["ind"], xt.format_datetime(dt), c["inp"]),
                file=stdout,
                end=end,
            )
    elif ns.numerate:
        for c in commands:
            print("{}: {}".format(c["ind"], c["inp"]), file=stdout, end=end)
    elif ns.timestamp:
        for c in commands:
            dt = datetime.datetime.fromtimestamp(c["ts"])
            print(
                "({}) {}".format(xt.format_datetime(dt), c["inp"]), file=stdout, end=end
            )
    else:
        for c in commands:
            print(c["inp"], file=stdout, end=end)


@xla.lazyobject
def _XH_HISTORY_SESSIONS():
    return {
        "session": _xh_session_parser,
        "xonsh": _xh_all_parser,
        "all": _xh_all_parser,
        "zsh": _xh_zsh_hist_parser,
        "bash": _xh_bash_hist_parser,
    }


_XH_MAIN_ACTIONS = {
    "show",
    "id",
    "file",
    "info",
    "diff",
    "gc",
    "flush",
    "off",
    "on",
    "clear",
}


@functools.lru_cache()
def _xh_create_parser():
    """Create a parser for the "history" command."""
    p = argparse.ArgumentParser(
        prog="history", description="try 'history <command> --help' " "for more info"
    )
    subp = p.add_subparsers(title="commands", dest="action")
    # session action
    show = subp.add_parser(
        "show", prefix_chars="-+", help="display history of a session, default command"
    )
    show.add_argument(
        "-r",
        dest="reverse",
        default=False,
        action="store_true",
        help="reverses the direction",
    )
    show.add_argument(
        "-n",
        dest="numerate",
        default=False,
        action="store_true",
        help="numerate each command",
    )
    show.add_argument(
        "-t",
        dest="timestamp",
        default=False,
        action="store_true",
        help="show command timestamps",
    )
    show.add_argument(
        "-T", dest="end_time", default=None, help="show only commands before timestamp"
    )
    show.add_argument(
        "+T", dest="start_time", default=None, help="show only commands after timestamp"
    )
    show.add_argument(
        "-f",
        dest="datetime_format",
        default=None,
        help="the datetime format to be used for" "filtering and printing",
    )
    show.add_argument(
        "-0",
        dest="null_byte",
        default=False,
        action="store_true",
        help="separate commands by the null character for piping "
        "history to external filters",
    )
    show.add_argument(
        "session",
        nargs="?",
        choices=_XH_HISTORY_SESSIONS.keys(),
        default="session",
        metavar="session",
        help="{} (default: current session, all is an alias for xonsh)"
        "".format(", ".join(map(repr, _XH_HISTORY_SESSIONS.keys()))),
    )
    show.add_argument(
        "slices",
        nargs="*",
        default=None,
        metavar="slice",
        help="integer or slice notation",
    )
    # 'id' subcommand
    subp.add_parser("id", help="display the current session id")
    # 'file' subcommand
    subp.add_parser("file", help="display the current history filename")
    # 'info' subcommand
    info = subp.add_parser(
        "info", help=("display information about the " "current history")
    )
    info.add_argument(
        "--json",
        dest="json",
        default=False,
        action="store_true",
        help="print in JSON format",
    )

    # gc
    gcp = subp.add_parser("gc", help="launches a new history garbage collector")
    gcp.add_argument(
        "--size",
        nargs=2,
        dest="size",
        default=None,
        help=(
            "next two arguments represent the history size and "
            'units; e.g. "--size 8128 commands"'
        ),
    )
    gcp.add_argument(
        "--force",
        dest="force_gc",
        default=False,
        action="store_true",
        help="perform garbage collection even if history much bigger than configured limit",
    )
    bgcp = gcp.add_mutually_exclusive_group()
    bgcp.add_argument(
        "--blocking",
        dest="blocking",
        default=True,
        action="store_true",
        help=("ensures that the gc blocks the main thread, " "default True"),
    )
    bgcp.add_argument(
        "--non-blocking",
        dest="blocking",
        action="store_false",
        help="makes the gc non-blocking, and thus return sooner",
    )

    hist = XSH.history
    if isinstance(hist, JsonHistory):
        # add actions belong only to JsonHistory
        diff = subp.add_parser("diff", help="diff two xonsh history files")
        xdh.dh_create_parser(p=diff)

    # 'flush' subcommand
    subp.add_parser("flush", help="flush the current history to disk")

    # 'off' subcommand
    subp.add_parser("off", help="history will not be saved for this session")

    # 'on' subcommand
    subp.add_parser(
        "on", help="history will be saved for the rest of the session (default)"
    )

    # 'clear' subcommand
    subp.add_parser("clear", help="one-time wipe of session history")

    return p


def _xh_parse_args(args):
    """Prepare and parse arguments for the history command.

    Add default action for ``history`` and
    default session for ``history show``.
    """
    parser = _xh_create_parser()
    if not args:
        args = ["show", "session"]
    elif args[0] not in _XH_MAIN_ACTIONS and args[0] not in ("-h", "--help"):
        args = ["show", "session"] + args
    if args[0] == "show":
        if not any(a in _XH_HISTORY_SESSIONS for a in args):
            args.insert(1, "session")
        ns, slices = parser.parse_known_args(args)
        if slices:
            if not ns.slices:
                ns.slices = slices
            else:
                ns.slices.extend(slices)
    else:
        ns = parser.parse_args(args)
    return ns


def history_main(
    args=None, stdin=None, stdout=None, stderr=None, spec=None, stack=None
):
    """This is the history command entry point."""
    hist = XSH.history
    ns = _xh_parse_args(args)
    if not ns or not ns.action:
        return
    if ns.action == "show":
        _xh_show_history(hist, ns, stdout=stdout, stderr=stderr)
    elif ns.action == "info":
        data = hist.info()
        if ns.json:
            s = json.dumps(data)
            print(s, file=stdout)
        else:
            lines = ["{0}: {1}".format(k, v) for k, v in data.items()]
            print("\n".join(lines), file=stdout)
    elif ns.action == "id":
        if not hist.sessionid:
            return
        print(str(hist.sessionid), file=stdout)
    elif ns.action == "file":
        if not hist.filename:
            return
        print(str(hist.filename), file=stdout)
    elif ns.action == "gc":
        hist.run_gc(size=ns.size, blocking=ns.blocking, force=ns.force_gc)
    elif ns.action == "diff":
        if isinstance(hist, JsonHistory):
            xdh.dh_main_action(ns)
    elif ns.action == "flush":
        hf = hist.flush()
        if isinstance(hf, threading.Thread):
            hf.join()
    elif ns.action == "off":
        if hist.remember_history:
            hist.clear()
            hist.remember_history = False
            print("History off", file=sys.stderr)
    elif ns.action == "on":
        if not hist.remember_history:
            hist.remember_history = True
            print("History on", file=sys.stderr)
    elif ns.action == "clear":
        hist.clear()
        print("History cleared", file=sys.stderr)
    else:
        print("Unknown history action {}".format(ns.action), file=sys.stderr)

