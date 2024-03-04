"""Amalgamation of xonsh.procs package, made up of the following modules, in order:

* readers
* pipelines
* posix
* proxies
* specs

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
# readers
#
"""File handle readers and related tools."""
os = _LazyModule.load('os', 'os')
io = _LazyModule.load('io', 'io')
sys = _LazyModule.load('sys', 'sys')
time = _LazyModule.load('time', 'time')
queue = _LazyModule.load('queue', 'queue')
ctypes = _LazyModule.load('ctypes', 'ctypes')
threading = _LazyModule.load('threading', 'threading')
xli = _LazyModule.load('xonsh', 'xonsh.lazyimps', 'xli')
from xonsh.built_ins import XSH


class QueueReader:
    """Provides a file-like interface to reading from a queue."""

    def __init__(self, fd, timeout=None):
        """
        Parameters
        ----------
        fd : int
            A file descriptor
        timeout : float or None, optional
            The queue reading timeout.
        """
        self.fd = fd
        self.timeout = timeout
        self.closed = False
        self.queue = queue.Queue()
        self.thread = None

    def close(self):
        """close the reader"""
        self.closed = True

    def is_fully_read(self):
        """Returns whether or not the queue is fully read and the reader is
        closed.
        """
        return (
            self.closed
            and (self.thread is None or not self.thread.is_alive())
            and self.queue.empty()
        )

    def read_queue(self):
        """Reads a single chunk from the queue. This is blocking if
        the timeout is None and non-blocking otherwise.
        """
        try:
            return self.queue.get(block=True, timeout=self.timeout)
        except queue.Empty:
            return b""

    def read(self, size=-1):
        """Reads bytes from the file."""
        i = 0
        buf = b""
        while size < 0 or i != size:
            line = self.read_queue()
            if line:
                buf += line
            else:
                break
            i += len(line)
        return buf

    def readline(self, size=-1):
        """Reads a line, or a partial line from the file descriptor."""
        i = 0
        nl = b"\n"
        buf = b""
        while size < 0 or i != size:
            line = self.read_queue()
            if line:
                buf += line
                if line.endswith(nl):
                    break
            else:
                break
            i += len(line)
        return buf

    def _read_all_lines(self):
        """This reads all remaining lines in a blocking fashion."""
        lines = []
        while not self.is_fully_read():
            chunk = self.read_queue()
            lines.extend(chunk.splitlines(keepends=True))
        return lines

    def readlines(self, hint=-1):
        """Reads lines from the file descriptor. This is blocking for negative
        hints (i.e. read all the remaining lines) and non-blocking otherwise.
        """
        if hint == -1:
            return self._read_all_lines()
        lines = []
        while len(lines) != hint:
            chunk = self.read_queue()
            if not chunk:
                break
            lines.extend(chunk.splitlines(keepends=True))
        return lines

    def fileno(self):
        """Returns the file descriptor number."""
        return self.fd

    @staticmethod
    def readable():
        """Returns true, because this object is always readable."""
        return True

    def iterqueue(self):
        """Iterates through all remaining chunks in a blocking fashion."""
        while not self.is_fully_read():
            chunk = self.read_queue()
            if not chunk:
                continue
            yield chunk


def populate_fd_queue(reader, fd, queue):
    """Reads 1 kb of data from a file descriptor into a queue.
    If this ends or fails, it flags the calling reader object as closed.
    """
    while True:
        try:
            c = os.read(fd, 1024)
        except OSError:
            reader.closed = True
            break
        if c:
            queue.put(c)
        else:
            reader.closed = True
            break


class NonBlockingFDReader(QueueReader):
    """A class for reading characters from a file descriptor on a background
    thread. This has the advantages that the calling thread can close the
    file and that the reading does not block the calling thread.
    """

    def __init__(self, fd, timeout=None):
        """
        Parameters
        ----------
        fd : int
            A file descriptor
        timeout : float or None, optional
            The queue reading timeout.
        """
        super().__init__(fd, timeout=timeout)
        # start reading from stream
        self.thread = threading.Thread(
            target=populate_fd_queue, args=(self, self.fd, self.queue)
        )
        self.thread.daemon = True
        self.thread.start()


def populate_buffer(reader, fd, buffer, chunksize):
    """Reads bytes from the file descriptor and copies them into a buffer.

    The reads happen in parallel using the pread() syscall; which is only
    available on POSIX systems. If the read fails for any reason, the reader is
    flagged as closed.
    """
    offset = 0
    while True:
        try:
            buf = os.pread(fd, chunksize, offset)
        except OSError:
            reader.closed = True
            break
        if buf:
            buffer.write(buf)
            offset += len(buf)
        else:
            reader.closed = True
            break


class BufferedFDParallelReader:
    """Buffered, parallel background thread reader."""

    def __init__(self, fd, buffer=None, chunksize=1024):
        """
        Parameters
        ----------
        fd : int
            File descriptor from which to read.
        buffer : binary file-like or None, optional
            A buffer to write bytes into. If None, a new BytesIO object
            is created.
        chunksize : int, optional
            The max size of the parallel reads, default 1 kb.
        """
        self.fd = fd
        self.buffer = io.BytesIO() if buffer is None else buffer
        self.chunksize = chunksize
        self.closed = False
        # start reading from stream
        self.thread = threading.Thread(
            target=populate_buffer, args=(self, fd, self.buffer, chunksize)
        )
        self.thread.daemon = True

        self.thread.start()


def _expand_console_buffer(cols, max_offset, expandsize, orig_posize, fd):
    # if we are getting close to the end of the console buffer,
    # expand it so that we can read from it successfully.
    if cols == 0:
        return orig_posize[-1], max_offset, orig_posize
    rows = ((max_offset + expandsize) // cols) + 1
    xli.winutils.set_console_screen_buffer_size(cols, rows, fd=fd)
    orig_posize = orig_posize[:3] + (rows,)
    max_offset = (rows - 1) * cols
    return rows, max_offset, orig_posize


def populate_console(reader, fd, buffer, chunksize, queue, expandsize=None):
    """Reads bytes from the file descriptor and puts lines into the queue.
    The reads happened in parallel,
    using xonsh.winutils.read_console_output_character(),
    and is thus only available on windows. If the read fails for any reason,
    the reader is flagged as closed.
    """
    # OK, so this function is super annoying because Windows stores its
    # buffers as a 2D regular, dense array -- without trailing newlines.
    # Meanwhile, we want to add *lines* to the queue. Also, as is typical
    # with parallel reads, the entire buffer that you ask for may not be
    # filled. Thus we have to deal with the full generality.
    #   1. reads may end in the middle of a line
    #   2. excess whitespace at the end of a line may not be real, unless
    #   3. you haven't read to the end of the line yet!
    # So there are alignment issues everywhere.  Also, Windows will automatically
    # read past the current cursor position, even though there is presumably
    # nothing to see there.
    #
    # These chunked reads basically need to happen like this because,
    #   a. The default buffer size is HUGE for the console (90k lines x 120 cols)
    #      as so we can't just read in everything at the end and see what we
    #      care about without a noticeable performance hit.
    #   b. Even with this huge size, it is still possible to write more lines than
    #      this, so we should scroll along with the console.
    # Unfortunately, because we do not have control over the terminal emulator,
    # It is not possible to compute how far back we should set the beginning
    # read position because we don't know how many characters have been popped
    # off the top of the buffer. If we did somehow know this number we could do
    # something like the following:
    #
    #    new_offset = (y*cols) + x
    #    if new_offset == max_offset:
    #        new_offset -= scrolled_offset
    #        x = new_offset%cols
    #        y = new_offset//cols
    #        continue
    #
    # So this method is imperfect and only works as long as the screen has
    # room to expand to.  Thus the trick here is to expand the screen size
    # when we get close enough to the end of the screen. There remain some
    # async issues related to not being able to set the cursor position.
    # but they just affect the alignment / capture of the output of the
    # first command run after a screen resize.
    if expandsize is None:
        expandsize = 100 * chunksize
    x, y, cols, rows = posize = xli.winutils.get_position_size(fd)
    pre_x = pre_y = -1
    orig_posize = posize
    offset = (cols * y) + x
    max_offset = (rows - 1) * cols
    # I believe that there is a bug in PTK that if we reset the
    # cursor position, the cursor on the next prompt is accidentally on
    # the next line.  If this is fixed, uncomment the following line.
    # if max_offset < offset + expandsize:
    #     rows, max_offset, orig_posize = _expand_console_buffer(
    #                                        cols, max_offset, expandsize,
    #                                        orig_posize, fd)
    #     winutils.set_console_cursor_position(x, y, fd=fd)
    while True:
        posize = xli.winutils.get_position_size(fd)
        offset = (cols * y) + x
        if ((posize[1], posize[0]) <= (y, x) and posize[2:] == (cols, rows)) or (
            pre_x == x and pre_y == y
        ):
            # already at or ahead of the current cursor position.
            if reader.closed:
                break
            else:
                time.sleep(reader.timeout)
                continue
        elif max_offset <= offset + expandsize:
            ecb = _expand_console_buffer(cols, max_offset, expandsize, orig_posize, fd)
            rows, max_offset, orig_posize = ecb
            continue
        elif posize[2:] == (cols, rows):
            # cursor updated but screen size is the same.
            pass
        else:
            # screen size changed, which is offset preserving
            orig_posize = posize
            cols, rows = posize[2:]
            x = offset % cols
            y = offset // cols
            pre_x = pre_y = -1
            max_offset = (rows - 1) * cols
            continue
        try:
            buf = xli.winutils.read_console_output_character(
                x=x, y=y, fd=fd, buf=buffer, bufsize=chunksize, raw=True
            )
        except OSError:
            reader.closed = True
            break
        # cursor position and offset
        if not reader.closed:
            buf = buf.rstrip()
        nread = len(buf)
        if nread == 0:
            time.sleep(reader.timeout)
            continue
        cur_x, cur_y = posize[0], posize[1]
        cur_offset = (cols * cur_y) + cur_x
        beg_offset = (cols * y) + x
        end_offset = beg_offset + nread
        if end_offset > cur_offset and cur_offset != max_offset:
            buf = buf[: cur_offset - end_offset]
        # convert to lines
        xshift = cols - x
        yshift = (nread // cols) + (1 if nread % cols > 0 else 0)
        lines = [buf[:xshift]]
        lines += [
            buf[l * cols + xshift : (l + 1) * cols + xshift]
            for l in range(yshift)  # noqa
        ]
        lines = [line for line in lines if line]
        if not lines:
            time.sleep(reader.timeout)
            continue
        # put lines in the queue
        nl = b"\n"
        for line in lines[:-1]:
            queue.put(line.rstrip() + nl)
        if len(lines[-1]) == xshift:
            queue.put(lines[-1].rstrip() + nl)
        else:
            queue.put(lines[-1])
        # update x and y locations
        if (beg_offset + len(buf)) % cols == 0:
            new_offset = beg_offset + len(buf)
        else:
            new_offset = beg_offset + len(buf.rstrip())
        pre_x = x
        pre_y = y
        x = new_offset % cols
        y = new_offset // cols
        time.sleep(reader.timeout)


class ConsoleParallelReader(QueueReader):
    """Parallel reader for consoles that runs in a background thread.
    This is only needed, available, and useful on Windows.
    """

    def __init__(self, fd, buffer=None, chunksize=1024, timeout=None):
        """
        Parameters
        ----------
        fd : int
            Standard buffer file descriptor, 0 for stdin, 1 for stdout (default),
            and 2 for stderr.
        buffer : ctypes.c_wchar_p, optional
            An existing buffer to (re-)use.
        chunksize : int, optional
            The max size of the parallel reads, default 1 kb.
        timeout : float, optional
            The queue reading timeout.
        """
        timeout = timeout or XSH.env.get("XONSH_PROC_FREQUENCY")
        super().__init__(fd, timeout=timeout)
        self._buffer = buffer  # this cannot be public
        if buffer is None:
            self._buffer = ctypes.c_char_p(b" " * chunksize)
        self.chunksize = chunksize
        # start reading from stream
        self.thread = threading.Thread(
            target=populate_console,
            args=(self, fd, self._buffer, chunksize, self.queue),
        )
        self.thread.daemon = True
        self.thread.start()


def safe_fdclose(handle, cache=None):
    """Closes a file handle in the safest way possible, and potentially
    storing the result.
    """
    if cache is not None and cache.get(handle, False):
        return
    status = True
    if handle is None:
        pass
    elif isinstance(handle, int):
        if handle >= 3:
            # don't close stdin, stdout, stderr, -1
            try:
                os.close(handle)
            except OSError:
                status = False
    elif handle is sys.stdin or handle is sys.stdout or handle is sys.stderr:
        # don't close stdin, stdout, or stderr
        pass
    else:
        try:
            handle.close()
        except OSError:
            status = False
    if cache is not None:
        cache[handle] = status

#
# pipelines
#
"""Command pipeline tools."""
# amalgamated os
re = _LazyModule.load('re', 're')
# amalgamated io
# amalgamated sys
# amalgamated time
signal = _LazyModule.load('signal', 'signal')
# amalgamated threading
subprocess = _LazyModule.load('subprocess', 'subprocess')
xl = _LazyModule.load('xonsh', 'xonsh.lazyasd', 'xl')
xt = _LazyModule.load('xonsh', 'xonsh.tools', 'xt')
xp = _LazyModule.load('xonsh', 'xonsh.platform', 'xp')
xj = _LazyModule.load('xonsh', 'xonsh.jobs', 'xj')
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.procs.readers
@xl.lazyobject
def STDOUT_CAPTURE_KINDS():
    return frozenset(["stdout", "object"])


@xl.lazyobject
def RE_HIDDEN_BYTES():
    return re.compile(b"(\001.*?\002)")


@xl.lazyobject
def RE_VT100_ESCAPE():
    return re.compile(b"(\x9B|\x1B\\[)[0-?]*[ -\\/]*[@-~]")


@xl.lazyobject
def RE_HIDE_ESCAPE():
    return re.compile(
        b"(" + RE_HIDDEN_BYTES.pattern + b"|" + RE_VT100_ESCAPE.pattern + b")"
    )


@xl.lazyobject
def SIGNAL_MESSAGES():
    sm = {
        signal.SIGABRT: "Aborted",
        signal.SIGFPE: "Floating point exception",
        signal.SIGILL: "Illegal instructions",
        signal.SIGTERM: "Terminated",
        signal.SIGSEGV: "Segmentation fault",
    }
    if xp.ON_POSIX:
        sm.update(
            {
                signal.SIGQUIT: "Quit",
                signal.SIGHUP: "Hangup",
                signal.SIGKILL: "Killed",
                signal.SIGTSTP: "Stopped",
            }
        )
    return sm


def safe_readlines(handle, hint=-1):
    """Attempts to read lines without throwing an error."""
    try:
        lines = handle.readlines(hint)
    except OSError:
        lines = []
    return lines


def safe_readable(handle):
    """Attempts to find if the handle is readable without throwing an error."""
    try:
        status = handle.readable()
    except (OSError, ValueError):
        status = False
    return status


def update_fg_process_group(pipeline_group, background):
    if background:
        return False
    if not xp.ON_POSIX:
        return False
    env = XSH.env
    if not env.get("XONSH_INTERACTIVE"):
        return False
    return xj.give_terminal_to(pipeline_group)


class CommandPipeline:
    """Represents a subprocess-mode command pipeline."""

    attrnames = (
        "stdin",
        "stdout",
        "stderr",
        "pid",
        "returncode",
        "args",
        "alias",
        "stdin_redirect",
        "stdout_redirect",
        "stderr_redirect",
        "timestamps",
        "executed_cmd",
        "input",
        "output",
        "errors",
    )

    nonblocking = (io.BytesIO, NonBlockingFDReader, ConsoleParallelReader)

    def __init__(self, specs):
        """
        Parameters
        ----------
        specs : list of SubprocSpec
            Process specifications

        Attributes
        ----------
        spec : SubprocSpec
            The last specification in specs
        proc : Popen-like
            The process in procs
        ended : bool
            Boolean for if the command has stopped executing.
        input : str
            A string of the standard input.
        output : str
            A string of the standard output.
        errors : str
            A string of the standard error.
        lines : list of str
            The output lines
        starttime : floats or None
            Pipeline start timestamp.
        """
        self.starttime = None
        self.ended = False
        self.procs = []
        self.specs = specs
        self.spec = specs[-1]
        self.captured = specs[-1].captured
        self.input = self._output = self.errors = self.endtime = None
        self._closed_handle_cache = {}
        self.lines = []
        self._raw_output = self._raw_error = b""
        self._stderr_prefix = self._stderr_postfix = None
        self.term_pgid = None

        background = self.spec.background
        pipeline_group = None
        for spec in specs:
            if self.starttime is None:
                self.starttime = time.time()
            try:
                proc = spec.run(pipeline_group=pipeline_group)
            except Exception:
                xt.print_exception()
                self._return_terminal()
                self.proc = None
                return
            if (
                proc.pid
                and pipeline_group is None
                and not spec.is_proxy
                and self.captured != "object"
            ):
                pipeline_group = proc.pid
                if update_fg_process_group(pipeline_group, background):
                    self.term_pgid = pipeline_group
            self.procs.append(proc)
        self.proc = self.procs[-1]

    def __repr__(self):
        s = self.__class__.__name__ + "(\n  "
        s += ",\n  ".join(a + "=" + repr(getattr(self, a)) for a in self.attrnames)
        s += "\n)"
        return s

    def __bool__(self):
        return self.returncode == 0

    def __int__(self):
        return self.returncode

    def __hash__(self):
        return hash(self.returncode)

    def __str__(self):
        self.end()
        return self.output

    def __len__(self):
        return len(self.procs)

    def __eq__(self, other):
        if isinstance(other, int):
            return self.returncode == other
        elif isinstance(other, str):
            return str(self) == other
        raise Exception(
            f"CommandPipeline doesn't support comparing with {type(other)}."
        )

    def __iter__(self):
        """Iterates through stdout and returns the lines, converting to
        strings and universal newlines if needed.
        """
        if self.ended:
            yield from iter(self.lines)
        else:
            yield from self.tee_stdout()

    def iterraw(self):
        """Iterates through the last stdout, and returns the lines
        exactly as found.
        """
        # get appropriate handles
        spec = self.spec
        proc = self.proc
        if proc is None:
            return
        timeout = XSH.env.get("XONSH_PROC_FREQUENCY")
        # get the correct stdout
        stdout = proc.stdout
        if (
            stdout is None or spec.stdout is None or not safe_readable(stdout)
        ) and spec.captured_stdout is not None:
            stdout = spec.captured_stdout
        if hasattr(stdout, "buffer"):
            stdout = stdout.buffer
        if stdout is not None and not isinstance(stdout, self.nonblocking):
            stdout = NonBlockingFDReader(stdout.fileno(), timeout=timeout)
        if (
            not stdout
            or self.captured == "stdout"
            or not safe_readable(stdout)
            or not spec.threadable
        ):
            # we get here if the process is not threadable or the
            # class is the real Popen
            PrevProcCloser(pipeline=self)
            task = xj.wait_for_active_job()
            if task is None or task["status"] != "stopped":
                proc.wait()
                self._endtime()
                if self.captured == "object":
                    self.end(tee_output=False)
                elif self.captured == "hiddenobject" and stdout:
                    b = stdout.read()
                    lines = b.splitlines(keepends=True)
                    yield from lines
                    self.end(tee_output=False)
                elif self.captured == "stdout":
                    b = stdout.read()
                    s = self._decode_uninew(b, universal_newlines=True)
                    self.lines = s.splitlines(keepends=True)
            return
        # get the correct stderr
        stderr = proc.stderr
        if (
            stderr is None or spec.stderr is None or not safe_readable(stderr)
        ) and spec.captured_stderr is not None:
            stderr = spec.captured_stderr
        if hasattr(stderr, "buffer"):
            stderr = stderr.buffer
        if stderr is not None and not isinstance(stderr, self.nonblocking):
            stderr = NonBlockingFDReader(stderr.fileno(), timeout=timeout)
        # read from process while it is running
        check_prev_done = len(self.procs) == 1
        prev_end_time = None
        i = j = cnt = 1
        while proc.poll() is None:
            if getattr(proc, "suspended", False):
                return
            elif getattr(proc, "in_alt_mode", False):
                time.sleep(0.1)  # probably not leaving any time soon
                continue
            elif not check_prev_done:
                # In the case of pipelines with more than one command
                # we should give the commands a little time
                # to start up fully. This is particularly true for
                # GNU Parallel, which has a long startup time.
                pass
            elif self._prev_procs_done():
                self._close_prev_procs()
                proc.prevs_are_closed = True
                break
            stdout_lines = safe_readlines(stdout, 1024)
            i = len(stdout_lines)
            if i != 0:
                yield from stdout_lines
            stderr_lines = safe_readlines(stderr, 1024)
            j = len(stderr_lines)
            if j != 0:
                self.stream_stderr(stderr_lines)
            if not check_prev_done:
                # if we are piping...
                if stdout_lines or stderr_lines:
                    # see if we have some output.
                    check_prev_done = True
                elif prev_end_time is None:
                    # or see if we already know that the next-to-last
                    # proc in the pipeline has ended.
                    if self._prev_procs_done():
                        # if it has, record the time
                        prev_end_time = time.time()
                elif time.time() - prev_end_time >= 0.1:
                    # if we still don't have any output, even though the
                    # next-to-last proc has finished, wait a bit to make
                    # sure we have fully started up, etc.
                    check_prev_done = True
            # this is for CPU usage
            if i + j == 0:
                cnt = min(cnt + 1, 1000)
            else:
                cnt = 1
            time.sleep(timeout * cnt)
        # read from process now that it is over
        yield from safe_readlines(stdout)
        self.stream_stderr(safe_readlines(stderr))
        proc.wait()
        self._endtime()
        yield from safe_readlines(stdout)
        self.stream_stderr(safe_readlines(stderr))
        if self.captured == "object":
            self.end(tee_output=False)

    def itercheck(self):
        """Iterates through the command lines and throws an error if the
        returncode is non-zero.
        """
        yield from self
        if self.returncode:
            # I included self, as providing access to stderr and other details
            # useful when instance isn't assigned to a variable in the shell.
            raise xt.XonshCalledProcessError(
                self.returncode, self.executed_cmd, self.stdout, self.stderr, self
            )

    def tee_stdout(self):
        """Writes the process stdout to the output variable, line-by-line, and
        yields each line. This may optionally accept lines (in bytes) to iterate
        over, in which case it does not call iterraw().
        """
        env = XSH.env
        enc = env.get("XONSH_ENCODING")
        err = env.get("XONSH_ENCODING_ERRORS")
        lines = self.lines
        raw_out_lines = []
        stream = self.captured not in STDOUT_CAPTURE_KINDS
        if stream and not self.spec.stdout:
            stream = False
        stdout_has_buffer = hasattr(sys.stdout, "buffer")
        nl = b"\n"
        cr = b"\r"
        crnl = b"\r\n"
        for line in self.iterraw():
            # write to stdout line ASAP, if needed
            if stream:
                if stdout_has_buffer:
                    sys.stdout.buffer.write(line)
                else:
                    sys.stdout.write(line.decode(encoding=enc, errors=err))
                sys.stdout.flush()
            # save the raw bytes
            raw_out_lines.append(line)
            # do some munging of the line before we return it
            if line.endswith(crnl):
                line = line[:-2] + nl
            elif line.endswith(cr):
                line = line[:-1] + nl
            line = RE_HIDE_ESCAPE.sub(b"", line)
            line = line.decode(encoding=enc, errors=err)
            # tee it up!
            lines.append(line)
            yield line

        # using join is more efficient than concatenating in a loop
        self._raw_output = b"".join(raw_out_lines)

    def stream_stderr(self, lines):
        """Streams lines to sys.stderr and the errors attribute."""
        if not lines:
            return
        env = XSH.env
        enc = env.get("XONSH_ENCODING")
        err = env.get("XONSH_ENCODING_ERRORS")
        b = b"".join(lines)
        if self.stderr_prefix:
            b = self.stderr_prefix + b
        if self.stderr_postfix:
            b += self.stderr_postfix
        stderr_has_buffer = hasattr(sys.stderr, "buffer")
        show_stderr = self.captured != "object" or env.get(
            "XONSH_SUBPROC_CAPTURED_PRINT_STDERR", True
        )
        if show_stderr:
            # write bytes to std stream
            if stderr_has_buffer:
                sys.stderr.buffer.write(b)
            else:
                sys.stderr.write(b.decode(encoding=enc, errors=err))
            sys.stderr.flush()
        # save the raw bytes
        self._raw_error = b
        # do some munging of the line before we save it to the attr
        b = b.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        b = RE_HIDE_ESCAPE.sub(b"", b)
        env = XSH.env
        s = b.decode(
            encoding=env.get("XONSH_ENCODING"), errors=env.get("XONSH_ENCODING_ERRORS")
        )
        # set the errors
        if self.errors is None:
            self.errors = s
        else:
            self.errors += s

    def _decode_uninew(self, b, universal_newlines=None):
        """Decode bytes into a str and apply universal newlines as needed."""
        if not b:
            return ""
        if isinstance(b, bytes):
            env = XSH.env
            s = b.decode(
                encoding=env.get("XONSH_ENCODING"),
                errors=env.get("XONSH_ENCODING_ERRORS"),
            )
        else:
            s = b
        if universal_newlines or self.spec.universal_newlines:
            s = s.replace("\r\n", "\n").replace("\r", "\n")
        return s

    #
    # Ending methods
    #

    def end(self, tee_output=True):
        """
        End the pipeline, return the controlling terminal if needed.

        Main things done in self._end().
        """
        if self.ended:
            return
        self._end(tee_output=tee_output)
        self._return_terminal()

    def _end(self, tee_output):
        """Waits for the command to complete and then runs any closing and
        cleanup procedures that need to be run.
        """
        if tee_output:
            for _ in self.tee_stdout():
                pass
        self._endtime()
        # since we are driven by getting output, input may not be available
        # until the command has completed.
        self._set_input()
        self._close_prev_procs()
        self._close_proc()
        self._check_signal()
        self._apply_to_history()
        self.ended = True
        self._raise_subproc_error()

    def _return_terminal(self):
        if xp.ON_WINDOWS or not xp.ON_POSIX:
            return
        pgid = os.getpgid(0)
        if self.term_pgid is None or pgid == self.term_pgid:
            return
        if xj.give_terminal_to(pgid):  # if gave term succeed
            self.term_pgid = pgid
            if XSH.shell is not None:
                # restoring sanity could probably be called whenever we return
                # control to the shell. But it only seems to matter after a
                # ^Z event. This *has* to be called after we give the terminal
                # back to the shell.
                XSH.shell.shell.restore_tty_sanity()

    def resume(self, job, tee_output=True):
        self.ended = False
        if xj.give_terminal_to(job["pgrp"]):
            self.term_pgid = job["pgrp"]
        xj._continue(job)
        self.end(tee_output=tee_output)

    def _endtime(self):
        """Sets the closing timestamp if it hasn't been already."""
        if self.endtime is None:
            self.endtime = time.time()

    def _safe_close(self, handle):
        safe_fdclose(handle, cache=self._closed_handle_cache)

    def _prev_procs_done(self):
        """Boolean for if all previous processes have completed. If there
        is only a single process in the pipeline, this returns False.
        """
        any_running = False
        for s, p in zip(self.specs[:-1], self.procs[:-1]):
            if p.poll() is None:
                any_running = True
                continue
            self._safe_close(s.stdin)
            self._safe_close(s.stdout)
            self._safe_close(s.stderr)
            if p is None:
                continue
            self._safe_close(p.stdin)
            self._safe_close(p.stdout)
            self._safe_close(p.stderr)
        return False if any_running else (len(self) > 1)

    def _close_prev_procs(self):
        """Closes all but the last proc's stdout."""
        for s, p in zip(self.specs[:-1], self.procs[:-1]):
            self._safe_close(s.stdin)
            self._safe_close(s.stdout)
            self._safe_close(s.stderr)
            if p is None:
                continue
            self._safe_close(p.stdin)
            self._safe_close(p.stdout)
            self._safe_close(p.stderr)

    def _close_proc(self):
        """Closes last proc's stdout."""
        s = self.spec
        p = self.proc
        self._safe_close(s.stdin)
        self._safe_close(s.stdout)
        self._safe_close(s.stderr)
        self._safe_close(s.captured_stdout)
        self._safe_close(s.captured_stderr)
        if p is None:
            return
        self._safe_close(p.stdin)
        self._safe_close(p.stdout)
        self._safe_close(p.stderr)

    def _set_input(self):
        """Sets the input variable."""
        if self.proc is None:
            return
        stdin = self.proc.stdin
        if (
            stdin is None
            or isinstance(stdin, int)
            or stdin.closed
            or not stdin.seekable()
            or not safe_readable(stdin)
        ):
            input = b""
        else:
            stdin.seek(0)
            input = stdin.read()
        self.input = self._decode_uninew(input)

    def _check_signal(self):
        """Checks if a signal was received and issues a message."""
        proc_signal = getattr(self.proc, "signal", None)
        if proc_signal is None:
            return
        sig, core = proc_signal
        sig_str = SIGNAL_MESSAGES.get(sig)
        if sig_str:
            if core:
                sig_str += " (core dumped)"
            print(sig_str, file=sys.stderr)
            if self.errors is not None:
                self.errors += sig_str + "\n"

    def _apply_to_history(self):
        """Applies the results to the current history object."""
        hist = XSH.history
        if hist is not None:
            hist.last_cmd_rtn = 1 if self.proc is None else self.proc.returncode

    def _raise_subproc_error(self):
        """Raises a subprocess error, if we are supposed to."""
        spec = self.spec
        rtn = self.returncode
        if rtn is not None and rtn != 0 and XSH.env.get("RAISE_SUBPROC_ERROR"):
            try:
                raise subprocess.CalledProcessError(rtn, spec.args, output=self.output)
            finally:
                # this is need to get a working terminal in interactive mode
                self._return_terminal()

    #
    # Properties
    #

    @property
    def stdin(self):
        """Process stdin."""
        return self.proc.stdin

    @property
    def stdout(self):
        """Process stdout."""
        return self.proc.stdout

    @property
    def stderr(self):
        """Process stderr."""
        return self.proc.stderr

    @property
    def inp(self):
        """Creates normalized input string from args."""
        return " ".join(self.args)

    @property
    def output(self):
        """Non-blocking, lazy access to output"""
        if self.ended:
            if self._output is None:
                self._output = "".join(self.lines)
            return self._output
        else:
            return "".join(self.lines)

    @property
    def out(self):
        """Output value as a str."""
        self.end()
        return self.output

    @property
    def err(self):
        """Error messages as a string."""
        self.end()
        return self.errors

    @property
    def raw_out(self):
        """Output as raw bytes."""
        self.end()
        return self._raw_output

    @property
    def raw_err(self):
        """Errors as raw bytes."""
        self.end()
        return self._raw_error

    @property
    def pid(self):
        """Process identifier."""
        return self.proc.pid

    @property
    def returncode(self):
        """Process return code, waits until command is completed."""
        self.end()
        if self.proc is None:
            return 1
        return self.proc.returncode

    @property
    def args(self):
        """Arguments to the process."""
        return self.spec.args

    @property
    def rtn(self):
        """Alias to return code."""
        return self.returncode

    @property
    def alias(self):
        """Alias the process used."""
        return self.spec.alias

    @property
    def stdin_redirect(self):
        """Redirection used for stdin."""
        stdin = self.spec.stdin
        name = getattr(stdin, "name", "<stdin>")
        mode = getattr(stdin, "mode", "r")
        return [name, mode]

    @property
    def stdout_redirect(self):
        """Redirection used for stdout."""
        stdout = self.spec.stdout
        name = getattr(stdout, "name", "<stdout>")
        mode = getattr(stdout, "mode", "a")
        return [name, mode]

    @property
    def stderr_redirect(self):
        """Redirection used for stderr."""
        stderr = self.spec.stderr
        name = getattr(stderr, "name", "<stderr>")
        mode = getattr(stderr, "mode", "r")
        return [name, mode]

    @property
    def timestamps(self):
        """The start and end time stamps."""
        return [self.starttime, self.endtime]

    @property
    def executed_cmd(self):
        """The resolve and executed command."""
        return self.spec.cmd

    @property
    def stderr_prefix(self):
        """Prefix to print in front of stderr, as bytes."""
        p = self._stderr_prefix
        if p is None:
            env = XSH.env
            t = env.get("XONSH_STDERR_PREFIX")
            s = xt.format_std_prepost(t, env=env)
            p = s.encode(
                encoding=env.get("XONSH_ENCODING"),
                errors=env.get("XONSH_ENCODING_ERRORS"),
            )
            self._stderr_prefix = p
        return p

    @property
    def stderr_postfix(self):
        """Postfix to print after stderr, as bytes."""
        p = self._stderr_postfix
        if p is None:
            env = XSH.env
            t = env.get("XONSH_STDERR_POSTFIX")
            s = xt.format_std_prepost(t, env=env)
            p = s.encode(
                encoding=env.get("XONSH_ENCODING"),
                errors=env.get("XONSH_ENCODING_ERRORS"),
            )
            self._stderr_postfix = p
        return p


class HiddenCommandPipeline(CommandPipeline):
    def __repr__(self):
        return ""


def pause_call_resume(p, f, *args, **kwargs):
    """For a process p, this will call a function f with the remaining args and
    and kwargs. If the process cannot accept signals, the function will be called.

    Parameters
    ----------
    p : Popen object or similar
    f : callable
    args : remaining arguments
    kwargs : keyword arguments
    """
    can_send_signal = (
        hasattr(p, "send_signal")
        and xp.ON_POSIX
        and not xp.ON_MSYS
        and not xp.ON_CYGWIN
    )
    if can_send_signal:
        try:
            p.send_signal(signal.SIGSTOP)
        except PermissionError:
            pass
    try:
        f(*args, **kwargs)
    except Exception:
        pass
    if can_send_signal:
        p.send_signal(signal.SIGCONT)


class PrevProcCloser(threading.Thread):
    """Previous process closer thread for pipelines whose last command
    is itself unthreadable. This makes sure that the pipeline is
    driven forward and does not deadlock.
    """

    def __init__(self, pipeline):
        """
        Parameters
        ----------
        pipeline : CommandPipeline
            The pipeline whose prev procs we should close.
        """
        self.pipeline = pipeline
        super().__init__()
        self.daemon = True
        self.start()

    def run(self):
        """Runs the closing algorithm."""
        pipeline = self.pipeline
        check_prev_done = len(pipeline.procs) == 1
        if check_prev_done:
            return
        proc = pipeline.proc
        prev_end_time = None
        timeout = XSH.env.get("XONSH_PROC_FREQUENCY")
        sleeptime = min(timeout * 1000, 0.1)
        while proc.poll() is None:
            if not check_prev_done:
                # In the case of pipelines with more than one command
                # we should give the commands a little time
                # to start up fully. This is particularly true for
                # GNU Parallel, which has a long startup time.
                pass
            elif pipeline._prev_procs_done():
                pipeline._close_prev_procs()
                proc.prevs_are_closed = True
                break
            if not check_prev_done:
                # if we are piping...
                if prev_end_time is None:
                    # or see if we already know that the next-to-last
                    # proc in the pipeline has ended.
                    if pipeline._prev_procs_done():
                        # if it has, record the time
                        prev_end_time = time.time()
                elif time.time() - prev_end_time >= 0.1:
                    # if we still don't have any output, even though the
                    # next-to-last proc has finished, wait a bit to make
                    # sure we have fully started up, etc.
                    check_prev_done = True
            # this is for CPU usage
            time.sleep(sleeptime)

#
# posix
#
"""Interface for running subprocess-mode commands on posix systems."""
# amalgamated os
# amalgamated io
# amalgamated sys
# amalgamated time
array = _LazyModule.load('array', 'array')
# amalgamated signal
# amalgamated threading
# amalgamated subprocess
# amalgamated xonsh.lazyasd
# amalgamated xonsh.platform
# amalgamated xonsh.tools
# amalgamated xonsh.lazyimps
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.procs.readers
MODE_NUMS = ("1049", "47", "1047")


@xl.lazyobject
def START_ALTERNATE_MODE():
    return frozenset("\x1b[?{0}h".format(i).encode() for i in MODE_NUMS)


@xl.lazyobject
def END_ALTERNATE_MODE():
    return frozenset("\x1b[?{0}l".format(i).encode() for i in MODE_NUMS)


@xl.lazyobject
def ALTERNATE_MODE_FLAGS():
    return tuple(START_ALTERNATE_MODE) + tuple(END_ALTERNATE_MODE)


class PopenThread(threading.Thread):
    """A thread for running and managing subprocess. This allows reading
    from the stdin, stdout, and stderr streams in a non-blocking fashion.

    This takes the same arguments and keyword arguments as regular Popen.
    This requires that the captured_stdout and captured_stderr attributes
    to be set following instantiation.
    """

    def __init__(self, *args, stdin=None, stdout=None, stderr=None, **kwargs):
        super().__init__()

        self.daemon = True

        self.lock = threading.RLock()
        env = XSH.env
        # stdin setup
        self.orig_stdin = stdin
        if stdin is None:
            self.stdin_fd = 0
        elif isinstance(stdin, int):
            self.stdin_fd = stdin
        else:
            self.stdin_fd = stdin.fileno()
        self.store_stdin = env.get("XONSH_STORE_STDIN")
        self.timeout = env.get("XONSH_PROC_FREQUENCY")
        self.in_alt_mode = False
        self.stdin_mode = None
        self._tc_cc_vsusp = b"\x1a"  # default is usually ^Z
        self._disable_suspend_keybind()
        # stdout setup
        self.orig_stdout = stdout
        self.stdout_fd = 1 if stdout is None else stdout.fileno()
        self._set_pty_size()
        # stderr setup
        self.orig_stderr = stderr
        # Set some signal handles, if we can. Must come before process
        # is started to prevent deadlock on windows
        self.proc = None  # has to be here for closure for handles
        self.old_int_handler = self.old_winch_handler = None
        self.old_tstp_handler = self.old_quit_handler = None
        if xt.on_main_thread():
            self.old_int_handler = signal.signal(signal.SIGINT, self._signal_int)
            if xp.ON_POSIX:
                self.old_tstp_handler = signal.signal(signal.SIGTSTP, self._signal_tstp)
                self.old_quit_handler = signal.signal(signal.SIGQUIT, self._signal_quit)
            if xp.CAN_RESIZE_WINDOW:
                self.old_winch_handler = signal.signal(
                    signal.SIGWINCH, self._signal_winch
                )
        # start up process
        if xp.ON_WINDOWS and stdout is not None:
            os.set_inheritable(stdout.fileno(), False)

        try:
            self.proc = proc = subprocess.Popen(
                *args, stdin=stdin, stdout=stdout, stderr=stderr, **kwargs
            )
        except Exception:
            self._clean_up()
            raise

        self.pid = proc.pid
        self.universal_newlines = uninew = proc.universal_newlines
        if uninew:
            self.encoding = enc = env.get("XONSH_ENCODING")
            self.encoding_errors = err = env.get("XONSH_ENCODING_ERRORS")
            self.stdin = io.BytesIO()  # stdin is always bytes!
            self.stdout = io.TextIOWrapper(io.BytesIO(), encoding=enc, errors=err)
            self.stderr = io.TextIOWrapper(io.BytesIO(), encoding=enc, errors=err)
        else:
            self.encoding = self.encoding_errors = None
            self.stdin = io.BytesIO()
            self.stdout = io.BytesIO()
            self.stderr = io.BytesIO()
        self.suspended = False
        self.prevs_are_closed = False
        self.start()

    def run(self):
        """Runs the subprocess by performing a parallel read on stdin if allowed,
        and copying bytes from captured_stdout to stdout and bytes from
        captured_stderr to stderr.
        """
        proc = self.proc
        spec = self._wait_and_getattr("spec")
        # get stdin and apply parallel reader if needed.
        stdin = self.stdin
        if self.orig_stdin is None:
            origin = None
        elif xp.ON_POSIX and self.store_stdin:
            origin = self.orig_stdin
            origfd = origin if isinstance(origin, int) else origin.fileno()
            origin = BufferedFDParallelReader(origfd, buffer=stdin)
        else:
            origin = None
        # get non-blocking stdout
        stdout = self.stdout.buffer if self.universal_newlines else self.stdout
        capout = spec.captured_stdout
        if capout is None:
            procout = None
        else:
            procout = NonBlockingFDReader(capout.fileno(), timeout=self.timeout)
        # get non-blocking stderr
        stderr = self.stderr.buffer if self.universal_newlines else self.stderr
        caperr = spec.captured_stderr
        if caperr is None:
            procerr = None
        else:
            procerr = NonBlockingFDReader(caperr.fileno(), timeout=self.timeout)
        # initial read from buffer
        self._read_write(procout, stdout, sys.__stdout__)
        self._read_write(procerr, stderr, sys.__stderr__)
        # loop over reads while process is running.
        i = j = cnt = 1
        while proc.poll() is None:
            # this is here for CPU performance reasons.
            if i + j == 0:
                cnt = min(cnt + 1, 1000)
                tout = self.timeout * cnt
                if procout is not None:
                    procout.timeout = tout
                if procerr is not None:
                    procerr.timeout = tout
            elif cnt == 1:
                pass
            else:
                cnt = 1
                if procout is not None:
                    procout.timeout = self.timeout
                if procerr is not None:
                    procerr.timeout = self.timeout
            # redirect some output!
            i = self._read_write(procout, stdout, sys.__stdout__)
            j = self._read_write(procerr, stderr, sys.__stderr__)
            if self.suspended:
                break
        if self.suspended:
            return
        # close files to send EOF to non-blocking reader.
        # capout & caperr seem to be needed only by Windows, while
        # orig_stdout & orig_stderr are need by posix and Windows.
        # Also, order seems to matter here,
        # with orig_* needed to be closed before cap*
        safe_fdclose(self.orig_stdout)
        safe_fdclose(self.orig_stderr)
        if xp.ON_WINDOWS:
            safe_fdclose(capout)
            safe_fdclose(caperr)
        # read in the remaining data in a blocking fashion.
        while (procout is not None and not procout.is_fully_read()) or (
            procerr is not None and not procerr.is_fully_read()
        ):
            self._read_write(procout, stdout, sys.__stdout__)
            self._read_write(procerr, stderr, sys.__stderr__)
        # kill the process if it is still alive. Happens when piping.
        if proc.poll() is None:
            proc.terminate()

    def _wait_and_getattr(self, name):
        """make sure the instance has a certain attr, and return it."""
        while not hasattr(self, name):
            time.sleep(1e-7)
        return getattr(self, name)

    def _read_write(self, reader, writer, stdbuf):
        """Reads a chunk of bytes from a buffer and write into memory or back
        down to the standard buffer, as appropriate. Returns the number of
        successful reads.
        """
        if reader is None:
            return 0
        i = -1
        for i, chunk in enumerate(iter(reader.read_queue, b"")):  # noqa
            self._alt_mode_switch(chunk, writer, stdbuf)
        if i >= 0:
            writer.flush()
            stdbuf.flush()
        return i + 1

    def _alt_mode_switch(self, chunk, membuf, stdbuf):
        """Enables recursively switching between normal capturing mode
        and 'alt' mode, which passes through values to the standard
        buffer. Pagers, text editors, curses applications, etc. use
        alternate mode.
        """
        i, flag = xt.findfirst(chunk, ALTERNATE_MODE_FLAGS)
        if flag is None:
            self._alt_mode_writer(chunk, membuf, stdbuf)
        else:
            # This code is executed when the child process switches the
            # terminal into or out of alternate mode. The line below assumes
            # that the user has opened vim, less, or similar, and writes writes
            # to stdin.
            j = i + len(flag)
            # write the first part of the chunk in the current mode.
            self._alt_mode_writer(chunk[:i], membuf, stdbuf)
            # switch modes
            # write the flag itself the current mode where alt mode is on
            # so that it is streamed to the terminal ASAP.
            # this is needed for terminal emulators to find the correct
            # positions before and after alt mode.
            alt_mode = flag in START_ALTERNATE_MODE
            if alt_mode:
                self.in_alt_mode = alt_mode
                self._alt_mode_writer(flag, membuf, stdbuf)
                self._enable_cbreak_stdin()
            else:
                self._alt_mode_writer(flag, membuf, stdbuf)
                self.in_alt_mode = alt_mode
                self._disable_cbreak_stdin()
            # recurse this function, but without the current flag.
            self._alt_mode_switch(chunk[j:], membuf, stdbuf)

    def _alt_mode_writer(self, chunk, membuf, stdbuf):
        """Write bytes to the standard buffer if in alt mode or otherwise
        to the in-memory buffer.
        """
        if not chunk:
            pass  # don't write empty values
        elif self.in_alt_mode:
            stdbuf.buffer.write(chunk)
        else:
            with self.lock:
                p = membuf.tell()
                membuf.seek(0, io.SEEK_END)
                membuf.write(chunk)
                membuf.seek(p)

    #
    # Window resize handlers
    #

    def _signal_winch(self, signum, frame):
        """Signal handler for SIGWINCH - window size has changed."""
        self.send_signal(signal.SIGWINCH)
        self._set_pty_size()

    def _set_pty_size(self):
        """Sets the window size of the child pty based on the window size of
        our own controlling terminal.
        """
        if xp.ON_WINDOWS or not os.isatty(self.stdout_fd):
            return
        # Get the terminal size of the real terminal, set it on the
        #       pseudoterminal.
        buf = array.array("h", [0, 0, 0, 0])
        # 1 = stdout here
        try:
            xli.fcntl.ioctl(1, xli.termios.TIOCGWINSZ, buf, True)
            xli.fcntl.ioctl(self.stdout_fd, xli.termios.TIOCSWINSZ, buf)
        except OSError:
            pass

    #
    # SIGINT handler
    #

    def _signal_int(self, signum, frame):
        """Signal handler for SIGINT - Ctrl+C may have been pressed."""
        self.send_signal(signal.CTRL_C_EVENT if xp.ON_WINDOWS else signum)
        if self.proc is not None and self.proc.poll() is not None:
            self._restore_sigint(frame=frame)
        if xt.on_main_thread() and not xp.ON_WINDOWS:
            signal.pthread_kill(threading.get_ident(), signal.SIGINT)

    def _restore_sigint(self, frame=None):
        old = self.old_int_handler
        if old is not None:
            if xt.on_main_thread():
                signal.signal(signal.SIGINT, old)
            self.old_int_handler = None
        if frame is not None:
            self._disable_cbreak_stdin()
            if old is not None and old is not self._signal_int:
                old(signal.SIGINT, frame)

    #
    # SIGTSTP handler
    #

    def _signal_tstp(self, signum, frame):
        """Signal handler for suspending SIGTSTP - Ctrl+Z may have been pressed."""
        self.suspended = True
        self.send_signal(signum)
        self._restore_sigtstp(frame=frame)

    def _restore_sigtstp(self, frame=None):
        old = self.old_tstp_handler
        if old is not None:
            if xt.on_main_thread():
                signal.signal(signal.SIGTSTP, old)
            self.old_tstp_handler = None
        if frame is not None:
            self._disable_cbreak_stdin()
        self._restore_suspend_keybind()

    def _disable_suspend_keybind(self):
        if xp.ON_WINDOWS:
            return
        try:
            mode = xli.termios.tcgetattr(0)  # only makes sense for stdin
            self._tc_cc_vsusp = mode[xp.CC][xli.termios.VSUSP]
            mode[xp.CC][xli.termios.VSUSP] = b"\x00"  # set ^Z (ie SIGSTOP) to undefined
            xli.termios.tcsetattr(0, xli.termios.TCSANOW, mode)
        except xli.termios.error:
            return

    def _restore_suspend_keybind(self):
        if xp.ON_WINDOWS:
            return
        try:
            mode = xli.termios.tcgetattr(0)  # only makes sense for stdin
            mode[xp.CC][
                xli.termios.VSUSP
            ] = self._tc_cc_vsusp  # set ^Z (ie SIGSTOP) to original
            # this usually doesn't work in interactive mode,
            # but we should try it anyway.
            xli.termios.tcsetattr(0, xli.termios.TCSANOW, mode)
        except xli.termios.error:
            pass

    #
    # SIGQUIT handler
    #

    def _signal_quit(self, signum, frame):
        r"""Signal handler for quiting SIGQUIT - Ctrl+\ may have been pressed."""
        self.send_signal(signum)
        self._restore_sigquit(frame=frame)

    def _restore_sigquit(self, frame=None):
        old = self.old_quit_handler
        if old is not None:
            if xt.on_main_thread():
                signal.signal(signal.SIGQUIT, old)
            self.old_quit_handler = None
        if frame is not None:
            self._disable_cbreak_stdin()

    #
    # cbreak mode handlers
    #

    def _enable_cbreak_stdin(self):
        if not xp.ON_POSIX:
            return
        try:
            self.stdin_mode = xli.termios.tcgetattr(self.stdin_fd)[:]
        except xli.termios.error:
            # this can happen for cases where another process is controlling
            # xonsh's tty device, such as in testing.
            self.stdin_mode = None
            return
        new = self.stdin_mode[:]
        new[xp.LFLAG] &= ~(xli.termios.ECHO | xli.termios.ICANON)
        new[xp.CC][xli.termios.VMIN] = 1
        new[xp.CC][xli.termios.VTIME] = 0
        try:
            # termios.TCSAFLUSH may be less reliable than termios.TCSANOW
            xli.termios.tcsetattr(self.stdin_fd, xli.termios.TCSANOW, new)
        except xli.termios.error:
            self._disable_cbreak_stdin()

    def _disable_cbreak_stdin(self):
        if not xp.ON_POSIX or self.stdin_mode is None:
            return
        new = self.stdin_mode[:]
        new[xp.LFLAG] |= xli.termios.ECHO | xli.termios.ICANON
        new[xp.CC][xli.termios.VMIN] = 1
        new[xp.CC][xli.termios.VTIME] = 0
        try:
            xli.termios.tcsetattr(self.stdin_fd, xli.termios.TCSANOW, new)
        except xli.termios.error:
            pass

    #
    # Dispatch methods
    #

    def poll(self):
        """Dispatches to Popen.returncode."""
        return self.proc.returncode

    def wait(self, timeout=None):
        """Dispatches to Popen.wait(), but also does process cleanup such as
        joining this thread and replacing the original window size signal
        handler.
        """
        self._disable_cbreak_stdin()
        rtn = self.proc.wait(timeout=timeout)
        self.join()
        # need to replace the old signal handlers somewhere...
        if self.old_winch_handler is not None and xt.on_main_thread():
            signal.signal(signal.SIGWINCH, self.old_winch_handler)
            self.old_winch_handler = None
        self._clean_up()
        return rtn

    def _clean_up(self):
        self._restore_sigint()
        self._restore_sigtstp()
        self._restore_sigquit()

    @property
    def returncode(self):
        """Process return code."""
        return self.proc.returncode

    @returncode.setter
    def returncode(self, value):
        """Process return code."""
        self.proc.returncode = value

    @property
    def signal(self):
        """Process signal, or None."""
        s = getattr(self.proc, "signal", None)
        if s is None:
            rtn = self.returncode
            if rtn is not None and rtn != 0:
                s = (-1 * rtn, rtn < 0 if xp.ON_WINDOWS else os.WCOREDUMP(rtn))
        return s

    @signal.setter
    def signal(self, value):
        """Process signal, or None."""
        self.proc.signal = value

    def send_signal(self, signal):
        """Dispatches to Popen.send_signal()."""
        dt = 0.0
        while self.proc is None and dt < self.timeout:
            time.sleep(1e-7)
            dt += 1e-7
        if self.proc is None:
            return
        try:
            rtn = self.proc.send_signal(signal)
        except ProcessLookupError:
            # This can happen in the case of !(cmd) when the command has ended
            rtn = None
        return rtn

    def terminate(self):
        """Dispatches to Popen.terminate()."""
        return self.proc.terminate()

    def kill(self):
        """Dispatches to Popen.kill()."""
        return self.proc.kill()

#
# proxies
#
"""Interface for running Python functions as subprocess-mode commands.

Code for several helper methods in the `ProcProxy` class have been reproduced
without modification from `subprocess.py` in the Python 3.4.2 standard library.
The contents of `subprocess.py` (and, thus, the reproduced methods) are
Copyright (c) 2003-2005 by Peter Astrand <astrand@lysator.liu.se> and were
licensed to the Python Software foundation under a Contributor Agreement.
"""
# amalgamated os
# amalgamated io
# amalgamated sys
# amalgamated time
# amalgamated signal
inspect = _LazyModule.load('inspect', 'inspect')
functools = _LazyModule.load('functools', 'functools')
# amalgamated threading
# amalgamated subprocess
cabc = _LazyModule.load('collections', 'collections.abc', 'cabc')
# amalgamated xonsh.tools
# amalgamated xonsh.platform
# amalgamated xonsh.lazyimps
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.procs.readers
def still_writable(fd):
    """Determines whether a file descriptor is still writable by trying to
    write an empty string and seeing if it fails.
    """
    try:
        os.write(fd, b"")
        status = True
    except OSError:
        status = False
    return status


def safe_flush(handle):
    """Attempts to safely flush a file handle, returns success bool."""
    status = True
    try:
        handle.flush()
    except OSError:
        status = False
    return status


class Handle(int):
    closed = False

    def Close(self, CloseHandle=None):
        CloseHandle = CloseHandle or xli._winapi.CloseHandle
        if not self.closed:
            self.closed = True
            CloseHandle(self)

    def Detach(self):
        if not self.closed:
            self.closed = True
            return int(self)
        raise ValueError("already closed")

    def __repr__(self):
        return f"Handle({int(self)})"

    __del__ = Close
    __str__ = __repr__


class FileThreadDispatcher:
    """Dispatches to different file handles depending on the
    current thread. Useful if you want file operation to go to different
    places for different threads.
    """

    def __init__(self, default=None):
        """
        Parameters
        ----------
        default : file-like or None, optional
            The file handle to write to if a thread cannot be found in
            the registry. If None, a new in-memory instance.

        Attributes
        ----------
        registry : dict
            Maps thread idents to file handles.
        """
        if default is None:
            default = io.TextIOWrapper(io.BytesIO())
        self.default = default
        self.registry = {}

    def register(self, handle):
        """Registers a file handle for the current thread. Returns self so
        that this method can be used in a with-statement.
        """
        if handle is self:
            # prevent weird recurssion errors
            return self
        self.registry[threading.get_ident()] = handle
        return self

    def deregister(self):
        """Removes the current thread from the registry."""
        ident = threading.get_ident()
        if ident in self.registry:
            # don't remove if we have already been deregistered
            del self.registry[threading.get_ident()]

    @property
    def available(self):
        """True if the thread is available in the registry."""
        return threading.get_ident() in self.registry

    @property
    def handle(self):
        """Gets the current handle for the thread."""
        return self.registry.get(threading.get_ident(), self.default)

    def __enter__(self):
        pass

    def __exit__(self, ex_type, ex_value, ex_traceback):
        self.deregister()

    #
    # io.TextIOBase interface
    #

    @property
    def encoding(self):
        """Gets the encoding for this thread's handle."""
        return self.handle.encoding

    @property
    def errors(self):
        """Gets the errors for this thread's handle."""
        return self.handle.errors

    @property
    def newlines(self):
        """Gets the newlines for this thread's handle."""
        return self.handle.newlines

    @property
    def buffer(self):
        """Gets the buffer for this thread's handle."""
        return self.handle.buffer

    def detach(self):
        """Detaches the buffer for the current thread."""
        return self.handle.detach()

    def read(self, size=None):
        """Reads from the handle for the current thread."""
        return self.handle.read(size)

    def readline(self, size=-1):
        """Reads a line from the handle for the current thread."""
        return self.handle.readline(size)

    def readlines(self, hint=-1):
        """Reads lines from the handle for the current thread."""
        return self.handle.readlines(hint)

    def seek(self, offset, whence=io.SEEK_SET):
        """Seeks the current file."""
        return self.handle.seek(offset, whence)

    def tell(self):
        """Reports the current position in the handle for the current thread."""
        return self.handle.tell()

    def write(self, s):
        """Writes to this thread's handle. This also flushes, just to be
        extra sure the string was written.
        """
        h = self.handle
        try:
            r = h.write(s)
            h.flush()
        except OSError:
            r = None
        return r

    @property
    def line_buffering(self):
        """Gets if line buffering for this thread's handle enabled."""
        return self.handle.line_buffering

    #
    # io.IOBase interface
    #

    def close(self):
        """Closes the current thread's handle."""
        return self.handle.close()

    @property
    def closed(self):
        """Is the thread's handle closed."""
        return self.handle.closed

    def fileno(self):
        """Returns the file descriptor for the current thread."""
        return self.handle.fileno()

    def flush(self):
        """Flushes the file descriptor for the current thread."""
        return safe_flush(self.handle)

    def isatty(self):
        """Returns if the file descriptor for the current thread is a tty."""
        if self.default:
            return self.default.isatty()
        return self.handle.isatty()

    def readable(self):
        """Returns if file descriptor for the current thread is readable."""
        return self.handle.readable()

    def seekable(self):
        """Returns if file descriptor for the current thread is seekable."""
        return self.handle.seekable()

    def truncate(self, size=None):
        """Truncates the file for for the current thread."""
        return self.handle.truncate()

    def writable(self, size=None):
        """Returns if file descriptor for the current thread is writable."""
        return self.handle.writable(size)

    def writelines(self):
        """Writes lines for the file descriptor for the current thread."""
        return self.handle.writelines()


# These should NOT be lazy since they *need* to get the true stdout from the
# main thread. Also their creation time should be negligible.
STDOUT_DISPATCHER = FileThreadDispatcher(default=sys.stdout)
STDERR_DISPATCHER = FileThreadDispatcher(default=sys.stderr)


def parse_proxy_return(r, stdout, stderr):
    """Proxies may return a variety of outputs. This handles them generally.

    Parameters
    ----------
    r : tuple, str, int, or None
        Return from proxy function
    stdout : file-like
        Current stdout stream
    stdout : file-like
        Current stderr stream

    Returns
    -------
    cmd_result : int
        The return code of the proxy
    """
    cmd_result = 0
    if isinstance(r, str):
        stdout.write(r)
        stdout.flush()
    elif isinstance(r, int):
        cmd_result = r
    elif isinstance(r, cabc.Sequence):
        rlen = len(r)
        if rlen > 0 and r[0] is not None:
            stdout.write(str(r[0]))
            stdout.flush()
        if rlen > 1 and r[1] is not None:
            stderr.write(str(r[1]))
            stderr.flush()
        if rlen > 2 and isinstance(r[2], int):
            cmd_result = r[2]
    elif r is not None:
        # for the random object...
        stdout.write(str(r))
        stdout.flush()
    return cmd_result


def proxy_zero(f, args, stdin, stdout, stderr, spec, stack):
    """Calls a proxy function which takes no parameters."""
    return f()


def proxy_one(f, args, stdin, stdout, stderr, spec, stack):
    """Calls a proxy function which takes one parameter: args"""
    return f(args)


def proxy_two(f, args, stdin, stdout, stderr, spec, stack):
    """Calls a proxy function which takes two parameter: args and stdin."""
    return f(args, stdin)


def proxy_three(f, args, stdin, stdout, stderr, spec, stack):
    """Calls a proxy function which takes three parameter: args, stdin, stdout."""
    return f(args, stdin, stdout)


def proxy_four(f, args, stdin, stdout, stderr, spec, stack):
    """Calls a proxy function which takes four parameter: args, stdin, stdout,
    and stderr.
    """
    return f(args, stdin, stdout, stderr)


def proxy_five(f, args, stdin, stdout, stderr, spec, stack):
    """Calls a proxy function which takes four parameter: args, stdin, stdout,
    stderr, and spec.
    """
    return f(args, stdin, stdout, stderr, spec)


PROXIES = (proxy_zero, proxy_one, proxy_two, proxy_three, proxy_four, proxy_five)


def partial_proxy(f):
    """Dispatches the appropriate proxy function based on the number of args."""
    numargs = 0
    for name, param in inspect.signature(f).parameters.items():
        if (
            param.kind == param.POSITIONAL_ONLY
            or param.kind == param.POSITIONAL_OR_KEYWORD
        ):
            numargs += 1
        elif name in xt.ALIAS_KWARG_NAMES and param.kind == param.KEYWORD_ONLY:
            numargs += 1
    if numargs < 6:
        return functools.partial(PROXIES[numargs], f)
    elif numargs == 6:
        # don't need to partial.
        return f
    else:
        e = "Expected proxy with 6 or fewer arguments for {}, not {}"
        raise xt.XonshError(e.format(", ".join(xt.ALIAS_KWARG_NAMES), numargs))


class ProcProxyThread(threading.Thread):
    """
    Class representing a function to be run as a subprocess-mode command.
    """

    def __init__(
        self,
        f,
        args,
        stdin=None,
        stdout=None,
        stderr=None,
        universal_newlines=False,
        close_fds=False,
        env=None,
    ):
        """Parameters
        ----------
        f : function
            The function to be executed.
        args : list
            A (possibly empty) list containing the arguments that were given on
            the command line
        stdin : file-like, optional
            A file-like object representing stdin (input can be read from
            here).  If `stdin` is not provided or if it is explicitly set to
            `None`, then an instance of `io.StringIO` representing an empty
            file is used.
        stdout : file-like, optional
            A file-like object representing stdout (normal output can be
            written here).  If `stdout` is not provided or if it is explicitly
            set to `None`, then `sys.stdout` is used.
        stderr : file-like, optional
            A file-like object representing stderr (error output can be
            written here).  If `stderr` is not provided or if it is explicitly
            set to `None`, then `sys.stderr` is used.
        universal_newlines : bool, optional
            Whether or not to use universal newlines.
        close_fds : bool, optional
            Whether or not to close file descriptors. This is here for Popen
            compatability and currently does nothing.
        env : Mapping, optional
            Environment mapping.
        """
        self.orig_f = f
        self.f = partial_proxy(f)
        self.args = args
        self.pid = None
        self.returncode = None
        self._closed_handle_cache = {}

        handles = self._get_handles(stdin, stdout, stderr)
        (
            self.p2cread,
            self.p2cwrite,
            self.c2pread,
            self.c2pwrite,
            self.errread,
            self.errwrite,
        ) = handles

        # default values
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.close_fds = close_fds
        self.env = env or XSH.env
        self._interrupted = False

        if xp.ON_WINDOWS:
            if self.p2cwrite != -1:
                self.p2cwrite = xli.msvcrt.open_osfhandle(self.p2cwrite.Detach(), 0)
            if self.c2pread != -1:
                self.c2pread = xli.msvcrt.open_osfhandle(self.c2pread.Detach(), 0)
            if self.errread != -1:
                self.errread = xli.msvcrt.open_osfhandle(self.errread.Detach(), 0)

        if self.p2cwrite != -1:
            self.stdin = io.open(self.p2cwrite, "wb", -1)
            if universal_newlines:
                self.stdin = io.TextIOWrapper(
                    self.stdin, write_through=True, line_buffering=False
                )
        elif isinstance(stdin, int) and stdin != 0:
            self.stdin = io.open(stdin, "wb", -1)

        if self.c2pread != -1:
            self.stdout = io.open(self.c2pread, "rb", -1)
            if universal_newlines:
                self.stdout = io.TextIOWrapper(self.stdout)

        if self.errread != -1:
            self.stderr = io.open(self.errread, "rb", -1)
            if universal_newlines:
                self.stderr = io.TextIOWrapper(self.stderr)

        # Set some signal handles, if we can. Must come before process
        # is started to prevent deadlock on windows
        self.old_int_handler = None
        if xt.on_main_thread():
            self.old_int_handler = signal.signal(signal.SIGINT, self._signal_int)
        # start up the proc
        super().__init__()
        self.start()

    def __del__(self):
        self._restore_sigint()

    def run(self):
        """Set up input/output streams and execute the child function in a new
        thread.  This is part of the `threading.Thread` interface and should
        not be called directly.
        """
        if self.f is None:
            return
        spec = self._wait_and_getattr("spec")
        last_in_pipeline = spec.last_in_pipeline
        if last_in_pipeline:
            capout = spec.captured_stdout  # NOQA
            caperr = spec.captured_stderr  # NOQA
        env = XSH.env
        enc = env.get("XONSH_ENCODING")
        err = env.get("XONSH_ENCODING_ERRORS")
        if xp.ON_WINDOWS:
            if self.p2cread != -1:
                self.p2cread = xli.msvcrt.open_osfhandle(self.p2cread.Detach(), 0)
            if self.c2pwrite != -1:
                self.c2pwrite = xli.msvcrt.open_osfhandle(self.c2pwrite.Detach(), 0)
            if self.errwrite != -1:
                self.errwrite = xli.msvcrt.open_osfhandle(self.errwrite.Detach(), 0)
        # get stdin
        if self.stdin is None:
            sp_stdin = None
        elif self.p2cread != -1:
            sp_stdin = io.TextIOWrapper(
                io.open(self.p2cread, "rb", -1), encoding=enc, errors=err
            )
        else:
            sp_stdin = sys.stdin
        # stdout
        if self.c2pwrite != -1:
            sp_stdout = io.TextIOWrapper(
                io.open(self.c2pwrite, "wb", -1), encoding=enc, errors=err
            )
        else:
            sp_stdout = sys.stdout
        # stderr
        if self.errwrite == self.c2pwrite:
            sp_stderr = sp_stdout
        elif self.errwrite != -1:
            sp_stderr = io.TextIOWrapper(
                io.open(self.errwrite, "wb", -1), encoding=enc, errors=err
            )
        else:
            sp_stderr = sys.stderr
        # run the function itself
        try:
            alias_stack = XSH.env.get("__ALIAS_STACK", "")
            if self.env.get("__ALIAS_NAME"):
                alias_stack += ":" + self.env["__ALIAS_NAME"]

            with STDOUT_DISPATCHER.register(sp_stdout), STDERR_DISPATCHER.register(
                sp_stderr
            ), xt.redirect_stdout(STDOUT_DISPATCHER), xt.redirect_stderr(
                STDERR_DISPATCHER
            ), XSH.env.swap(
                __ALIAS_STACK=alias_stack
            ):
                r = self.f(self.args, sp_stdin, sp_stdout, sp_stderr, spec, spec.stack)
        except SystemExit as e:
            r = e.code if isinstance(e.code, int) else int(bool(e.code))
        except OSError:
            status = still_writable(self.c2pwrite) and still_writable(self.errwrite)
            if status:
                # stdout and stderr are still writable, so error must
                # come from function itself.
                xt.print_exception()
                r = 1
            else:
                # stdout and stderr are no longer writable, so error must
                # come from the fact that the next process in the pipeline
                # has closed the other side of the pipe. The function then
                # attempted to write to this side of the pipe anyway. This
                # is not truly an error and we should exit gracefully.
                r = 0
        except Exception:
            xt.print_exception()
            r = 1
        safe_flush(sp_stdout)
        safe_flush(sp_stderr)
        self.returncode = parse_proxy_return(r, sp_stdout, sp_stderr)
        if not last_in_pipeline and not xp.ON_WINDOWS:
            # mac requires us *not to* close the handles here while
            # windows requires us *to* close the handles here
            return
        # clean up
        # scopz: not sure why this is needed, but stdin cannot go here
        # and stdout & stderr must.
        handles = [self.stdout, self.stderr]
        for handle in handles:
            safe_fdclose(handle, cache=self._closed_handle_cache)

    def _wait_and_getattr(self, name):
        """make sure the instance has a certain attr, and return it."""
        while not hasattr(self, name):
            time.sleep(1e-7)
        return getattr(self, name)

    def poll(self):
        """Check if the function has completed.

        Returns
        -------
        None if the function is still executing, and the returncode otherwise
        """
        return self.returncode

    def wait(self, timeout=None):
        """Waits for the process to finish and returns the return code."""
        self.join()
        self._restore_sigint()
        return self.returncode

    #
    # SIGINT handler
    #

    def _signal_int(self, signum, frame):
        """Signal handler for SIGINT - Ctrl+C may have been pressed."""
        # Check if we have already been interrupted. This should prevent
        # the possibility of infinite recursion.
        if self._interrupted:
            return
        self._interrupted = True
        # close file handles here to stop an processes piped to us.
        handles = (
            self.p2cread,
            self.p2cwrite,
            self.c2pread,
            self.c2pwrite,
            self.errread,
            self.errwrite,
        )
        for handle in handles:
            safe_fdclose(handle)
        if self.poll() is not None:
            self._restore_sigint(frame=frame)
        if xt.on_main_thread() and not xp.ON_WINDOWS:
            signal.pthread_kill(threading.get_ident(), signal.SIGINT)

    def _restore_sigint(self, frame=None):
        old = self.old_int_handler
        if old is not None:
            if xt.on_main_thread():
                signal.signal(signal.SIGINT, old)
            self.old_int_handler = None
        if frame is not None:
            if old is not None and old is not self._signal_int:
                old(signal.SIGINT, frame)
        if self._interrupted:
            self.returncode = 1

    # The code below (_get_devnull, _get_handles, and _make_inheritable) comes
    # from subprocess.py in the Python 3.4.2 Standard Library
    def _get_devnull(self):
        if not hasattr(self, "_devnull"):
            self._devnull = os.open(os.devnull, os.O_RDWR)
        return self._devnull

    if xp.ON_WINDOWS:

        def _make_inheritable(self, handle):
            """Return a duplicate of handle, which is inheritable"""
            h = xli._winapi.DuplicateHandle(
                xli._winapi.GetCurrentProcess(),
                handle,
                xli._winapi.GetCurrentProcess(),
                0,
                1,
                xli._winapi.DUPLICATE_SAME_ACCESS,
            )
            return Handle(h)

        def _get_handles(self, stdin, stdout, stderr):
            """Construct and return tuple with IO objects:
            p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite
            """
            if stdin is None and stdout is None and stderr is None:
                return (-1, -1, -1, -1, -1, -1)

            p2cread, p2cwrite = -1, -1
            c2pread, c2pwrite = -1, -1
            errread, errwrite = -1, -1

            if stdin is None:
                p2cread = xli._winapi.GetStdHandle(xli._winapi.STD_INPUT_HANDLE)
                if p2cread is None:
                    p2cread, _ = xli._winapi.CreatePipe(None, 0)
                    p2cread = Handle(p2cread)
                    xli._winapi.CloseHandle(_)
            elif stdin == subprocess.PIPE:
                p2cread, p2cwrite = Handle(p2cread), Handle(p2cwrite)
            elif stdin == subprocess.DEVNULL:
                p2cread = xli.msvcrt.get_osfhandle(self._get_devnull())
            elif isinstance(stdin, int):
                p2cread = xli.msvcrt.get_osfhandle(stdin)
            else:
                # Assuming file-like object
                p2cread = xli.msvcrt.get_osfhandle(stdin.fileno())
            p2cread = self._make_inheritable(p2cread)

            if stdout is None:
                c2pwrite = xli._winapi.GetStdHandle(xli._winapi.STD_OUTPUT_HANDLE)
                if c2pwrite is None:
                    _, c2pwrite = xli._winapi.CreatePipe(None, 0)
                    c2pwrite = Handle(c2pwrite)
                    xli._winapi.CloseHandle(_)
            elif stdout == subprocess.PIPE:
                c2pread, c2pwrite = xli._winapi.CreatePipe(None, 0)
                c2pread, c2pwrite = Handle(c2pread), Handle(c2pwrite)
            elif stdout == subprocess.DEVNULL:
                c2pwrite = xli.msvcrt.get_osfhandle(self._get_devnull())
            elif isinstance(stdout, int):
                c2pwrite = xli.msvcrt.get_osfhandle(stdout)
            else:
                # Assuming file-like object
                c2pwrite = xli.msvcrt.get_osfhandle(stdout.fileno())
            c2pwrite = self._make_inheritable(c2pwrite)

            if stderr is None:
                errwrite = xli._winapi.GetStdHandle(xli._winapi.STD_ERROR_HANDLE)
                if errwrite is None:
                    _, errwrite = xli._winapi.CreatePipe(None, 0)
                    errwrite = Handle(errwrite)
                    xli._winapi.CloseHandle(_)
            elif stderr == subprocess.PIPE:
                errread, errwrite = xli._winapi.CreatePipe(None, 0)
                errread, errwrite = Handle(errread), Handle(errwrite)
            elif stderr == subprocess.STDOUT:
                errwrite = c2pwrite
            elif stderr == subprocess.DEVNULL:
                errwrite = xli.msvcrt.get_osfhandle(self._get_devnull())
            elif isinstance(stderr, int):
                errwrite = xli.msvcrt.get_osfhandle(stderr)
            else:
                # Assuming file-like object
                errwrite = xli.msvcrt.get_osfhandle(stderr.fileno())
            errwrite = self._make_inheritable(errwrite)

            return (p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite)

    else:
        # POSIX versions
        def _get_handles(self, stdin, stdout, stderr):
            """Construct and return tuple with IO objects:
            p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite
            """
            p2cread, p2cwrite = -1, -1
            c2pread, c2pwrite = -1, -1
            errread, errwrite = -1, -1

            if stdin is None:
                pass
            elif stdin == subprocess.PIPE:
                p2cread, p2cwrite = os.pipe()
            elif stdin == subprocess.DEVNULL:
                p2cread = self._get_devnull()
            elif isinstance(stdin, int):
                p2cread = stdin
            else:
                # Assuming file-like object
                p2cread = stdin.fileno()

            if stdout is None:
                pass
            elif stdout == subprocess.PIPE:
                c2pread, c2pwrite = os.pipe()
            elif stdout == subprocess.DEVNULL:
                c2pwrite = self._get_devnull()
            elif isinstance(stdout, int):
                c2pwrite = stdout
            else:
                # Assuming file-like object
                c2pwrite = stdout.fileno()

            if stderr is None:
                pass
            elif stderr == subprocess.PIPE:
                errread, errwrite = os.pipe()
            elif stderr == subprocess.STDOUT:
                errwrite = c2pwrite
            elif stderr == subprocess.DEVNULL:
                errwrite = self._get_devnull()
            elif isinstance(stderr, int):
                errwrite = stderr
            else:
                # Assuming file-like object
                errwrite = stderr.fileno()

            return (p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite)


#
# Foreground Thread Process Proxies
#


class ProcProxy:
    """This is process proxy class that runs its alias functions on the
    same thread that it was called from, which is typically the main thread.
    This prevents the process from running on a background thread, but enables
    debugger and profiler tools (functions) be run on the same thread that they
    are attempting to debug.
    """

    def __init__(
        self,
        f,
        args,
        stdin=None,
        stdout=None,
        stderr=None,
        universal_newlines=False,
        close_fds=False,
        env=None,
    ):
        self.orig_f = f
        self.f = partial_proxy(f)
        self.args = args
        self.pid = os.getpid()
        self.returncode = None
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.universal_newlines = universal_newlines
        self.close_fds = close_fds
        self.env = env

    def poll(self):
        """Check if the function has completed via the returncode or None."""
        return self.returncode

    def wait(self, timeout=None):
        """Runs the function and returns the result. Timeout argument only
        present for API compatibility.
        """
        if self.f is None:
            return 0
        env = XSH.env
        enc = env.get("XONSH_ENCODING")
        err = env.get("XONSH_ENCODING_ERRORS")
        spec = self._wait_and_getattr("spec")
        # set file handles
        if self.stdin is None:
            stdin = None
        else:
            if isinstance(self.stdin, int):
                inbuf = io.open(self.stdin, "rb", -1)
            else:
                inbuf = self.stdin
            stdin = io.TextIOWrapper(inbuf, encoding=enc, errors=err)
        stdout = self._pick_buf(self.stdout, sys.stdout, enc, err)
        stderr = self._pick_buf(self.stderr, sys.stderr, enc, err)
        # run the actual function
        try:
            r = self.f(self.args, stdin, stdout, stderr, spec, spec.stack)
        except Exception:
            xt.print_exception()
            r = 1
        self.returncode = parse_proxy_return(r, stdout, stderr)
        safe_flush(stdout)
        safe_flush(stderr)
        return self.returncode

    @staticmethod
    def _pick_buf(handle, sysbuf, enc, err):
        if handle is None or handle is sysbuf:
            buf = sysbuf
        elif isinstance(handle, int):
            if handle < 3:
                buf = sysbuf
            else:
                buf = io.TextIOWrapper(
                    io.open(handle, "wb", -1), encoding=enc, errors=err
                )
        elif hasattr(handle, "encoding"):
            # must be a text stream, no need to wrap.
            buf = handle
        else:
            # must be a binary stream, should wrap it.
            buf = io.TextIOWrapper(handle, encoding=enc, errors=err)
        return buf

    def _wait_and_getattr(self, name):
        """make sure the instance has a certain attr, and return it."""
        while not hasattr(self, name):
            time.sleep(1e-7)
        return getattr(self, name)

#
# specs
#
"""Subprocess specification and related utilities."""
# amalgamated os
# amalgamated io
# amalgamated re
# amalgamated sys
shlex = _LazyModule.load('shlex', 'shlex')
# amalgamated signal
# amalgamated inspect
pathlib = _LazyModule.load('pathlib', 'pathlib')
# amalgamated subprocess
contextlib = _LazyModule.load('contextlib', 'contextlib')
# amalgamated from xonsh.built_ins import XSH
# amalgamated xonsh.tools
# amalgamated xonsh.lazyasd
# amalgamated xonsh.platform
xenv = _LazyModule.load('xonsh', 'xonsh.environ', 'xenv')
# amalgamated xonsh.lazyimps
# amalgamated xonsh.jobs
# amalgamated xonsh.procs.readers
# amalgamated xonsh.procs.posix
# amalgamated xonsh.procs.proxies
# amalgamated xonsh.procs.pipelines
@xl.lazyobject
def RE_SHEBANG():
    return re.compile(r"#![ \t]*(.+?)$")


def is_app_execution_alias(fname):
    """App execution aliases behave strangly on Windows and Python.
    Here we try to detect if a file is an app execution alias.
    """
    fname = pathlib.Path(fname)
    return not os.path.exists(fname) and fname.name in os.listdir(fname.parent)


def _is_binary(fname, limit=80):
    try:
        with open(fname, "rb") as f:
            for _ in range(limit):
                char = f.read(1)
                if char == b"\0":
                    return True
                if char == b"\n":
                    return False
                if char == b"":
                    return
    except OSError as e:
        if xp.ON_WINDOWS and is_app_execution_alias(fname):
            return True
        raise e

    return False


def _un_shebang(x):
    if x == "/usr/bin/env":
        return []
    elif any(x.startswith(i) for i in ["/usr/bin", "/usr/local/bin", "/bin"]):
        x = os.path.basename(x)
    elif x.endswith("python") or x.endswith("python.exe"):
        x = "python"
    if x == "xonsh":
        return ["python", "-m", "xonsh.main"]
    return [x]


def get_script_subproc_command(fname, args):
    """Given the name of a script outside the path, returns a list representing
    an appropriate subprocess command to execute the script or None if
    the argument is not readable or not a script. Raises PermissionError
    if the script is not executable.
    """
    # make sure file is executable
    if not os.access(fname, os.X_OK):
        if not xp.ON_CYGWIN:
            raise PermissionError
        # explicitly look at all PATH entries for cmd
        w_path = os.getenv("PATH").split(":")
        w_fpath = list(map(lambda p: p + os.sep + fname, w_path))
        if not any(list(map(lambda c: os.access(c, os.X_OK), w_fpath))):
            raise PermissionError
    if xp.ON_POSIX and not os.access(fname, os.R_OK):
        # on some systems, some important programs (e.g. sudo) will have
        # execute permissions but not read/write permissions. This enables
        # things with the SUID set to be run. Needs to come before _is_binary()
        # is called, because that function tries to read the file.
        return None
    elif _is_binary(fname):
        # if the file is a binary, we should call it directly
        return None
    if xp.ON_WINDOWS:
        # Windows can execute various filetypes directly
        # as given in PATHEXT
        _, ext = os.path.splitext(fname)
        if ext.upper() in XSH.env.get("PATHEXT"):
            return [fname] + args
    # find interpreter
    with open(fname, "rb") as f:
        first_line = f.readline().decode().strip()
    m = RE_SHEBANG.match(first_line)
    # xonsh is the default interpreter
    if m is None:
        interp = ["xonsh"]
    else:
        interp = m.group(1).strip()
        if len(interp) > 0:
            interp = shlex.split(interp)
        else:
            interp = ["xonsh"]
    if xp.ON_WINDOWS:
        o = []
        for i in interp:
            o.extend(_un_shebang(i))
        interp = o
    return interp + [fname] + args


@xl.lazyobject
def _REDIR_REGEX():
    name = r"(o(?:ut)?|e(?:rr)?|a(?:ll)?|&?\d?)"
    return re.compile("{r}(>?>|<){r}$".format(r=name))


@xl.lazyobject
def _MODES():
    return {">>": "a", ">": "w", "<": "r"}


@xl.lazyobject
def _WRITE_MODES():
    return frozenset({"w", "a"})


@xl.lazyobject
def _REDIR_ALL():
    return frozenset({"&", "a", "all"})


@xl.lazyobject
def _REDIR_ERR():
    return frozenset({"2", "e", "err"})


@xl.lazyobject
def _REDIR_OUT():
    return frozenset({"", "1", "o", "out"})


@xl.lazyobject
def _E2O_MAP():
    return frozenset(
        {"{}>{}".format(e, o) for e in _REDIR_ERR for o in _REDIR_OUT if o != ""}
    )


@xl.lazyobject
def _O2E_MAP():
    return frozenset(
        {"{}>{}".format(o, e) for e in _REDIR_ERR for o in _REDIR_OUT if o != ""}
    )


def _is_redirect(x):
    return isinstance(x, str) and _REDIR_REGEX.match(x)


def safe_open(fname, mode, buffering=-1):
    """Safely attempts to open a file in for xonsh subprocs."""
    # file descriptors
    try:
        return io.open(fname, mode, buffering=buffering)
    except PermissionError:
        raise xt.XonshError(f"xonsh: {fname}: permission denied")
    except FileNotFoundError:
        raise xt.XonshError(f"xonsh: {fname}: no such file or directory")
    except Exception:
        raise xt.XonshError(f"xonsh: {fname}: unable to open file")


def safe_close(x):
    """Safely attempts to close an object."""
    if not isinstance(x, io.IOBase):
        return
    if x.closed:
        return
    try:
        x.close()
    except Exception:
        pass


def _parse_redirects(r, loc=None):
    """returns origin, mode, destination tuple"""
    orig, mode, dest = _REDIR_REGEX.match(r).groups()
    # redirect to fd
    if dest.startswith("&"):
        try:
            dest = int(dest[1:])
            if loc is None:
                loc, dest = dest, ""  # NOQA
            else:
                e = f"Unrecognized redirection command: {r}"
                raise xt.XonshError(e)
        except (ValueError, xt.XonshError):
            raise
        except Exception:
            pass
    mode = _MODES.get(mode, None)
    if mode == "r" and (len(orig) > 0 or len(dest) > 0):
        raise xt.XonshError(f"Unrecognized redirection command: {r}")
    elif mode in _WRITE_MODES and len(dest) > 0:
        raise xt.XonshError(f"Unrecognized redirection command: {r}")
    return orig, mode, dest


def _redirect_streams(r, loc=None):
    """Returns stdin, stdout, stderr tuple of redirections."""
    stdin = stdout = stderr = None
    no_ampersand = r.replace("&", "")
    # special case of redirecting stderr to stdout
    if no_ampersand in _E2O_MAP:
        stderr = subprocess.STDOUT
        return stdin, stdout, stderr
    elif no_ampersand in _O2E_MAP:
        stdout = 2  # using 2 as a flag, rather than using a file object
        return stdin, stdout, stderr
    # get streams
    orig, mode, dest = _parse_redirects(r)
    if mode == "r":
        stdin = safe_open(loc, mode)
    elif mode in _WRITE_MODES:
        if orig in _REDIR_ALL:
            stdout = stderr = safe_open(loc, mode)
        elif orig in _REDIR_OUT:
            stdout = safe_open(loc, mode)
        elif orig in _REDIR_ERR:
            stderr = safe_open(loc, mode)
        else:
            raise xt.XonshError(f"Unrecognized redirection command: {r}")
    else:
        raise xt.XonshError(f"Unrecognized redirection command: {r}")
    return stdin, stdout, stderr


def default_signal_pauser(n, f):
    """Pauses a signal, as needed."""
    signal.pause()


def no_pg_xonsh_preexec_fn():
    """Default subprocess preexec function for when there is no existing
    pipeline group.
    """
    os.setpgrp()
    signal.signal(signal.SIGTSTP, default_signal_pauser)


class SubprocSpec:
    """A container for specifying how a subprocess command should be
    executed.
    """

    kwnames = ("stdin", "stdout", "stderr", "universal_newlines", "close_fds")

    def __init__(
        self,
        cmd,
        cls=subprocess.Popen,
        stdin=None,
        stdout=None,
        stderr=None,
        universal_newlines=False,
        close_fds=False,
        captured=False,
        env=None,
    ):
        """
        Parameters
        ----------
        cmd : list of str
            Command to be run.
        cls : Popen-like
            Class to run the subprocess with.
        stdin : file-like
            Popen file descriptor or flag for stdin.
        stdout : file-like
            Popen file descriptor or flag for stdout.
        stderr : file-like
            Popen file descriptor or flag for stderr.
        universal_newlines : bool
            Whether or not to use universal newlines.
        close_fds : bool
            Whether or not to close the file descriptiors when the
            process exits.
        captured : bool or str, optional
            The flag for if the subprocess is captured, may be one of:
            False for $[], 'stdout' for $(), 'hiddenobject' for ![], or
            'object' for !().
        env : dict
            Replacement environment to run the subporcess in.

        Attributes
        ----------
        args : list of str
            Arguments as originally supplied.
        alias : list of str, callable, or None
            The alias that was resolved for this command, if any.
        binary_loc : str or None
            Path to binary to execute.
        is_proxy : bool
            Whether or not the subprocess is or should be run as a proxy.
        background : bool
            Whether or not the subprocess should be started in the background.
        threadable : bool
            Whether or not the subprocess is able to be run in a background
            thread, rather than the main thread.
        pipeline_index : int or None
            The index number of this sepc into the pipeline that is being setup.
        last_in_pipeline : bool
            Whether the subprocess is the last in the execution pipeline.
        captured_stdout : file-like
            Handle to captured stdin
        captured_stderr : file-like
            Handle to captured stderr
        stack : list of FrameInfo namedtuples or None
            The stack of the call-site of alias, if the alias requires it.
            None otherwise.
        """
        self._stdin = self._stdout = self._stderr = None
        # args
        self.cmd = list(cmd)
        self.cls = cls
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.universal_newlines = universal_newlines
        self.close_fds = close_fds
        self.captured = captured
        if env is not None:
            self.env = {
                k: v if not (isinstance(v, list)) or len(v) > 1 else v[0]
                for (k, v) in env.items()
            }
        else:
            self.env = None
        # pure attrs
        self.args = list(cmd)
        self.alias = None
        self.alias_name = None
        self.alias_stack = XSH.env.get("__ALIAS_STACK", "").split(":")
        self.binary_loc = None
        self.is_proxy = False
        self.background = False
        self.threadable = True
        self.pipeline_index = None
        self.last_in_pipeline = False
        self.captured_stdout = None
        self.captured_stderr = None
        self.stack = None

    def __str__(self):
        s = self.__class__.__name__ + "(" + str(self.cmd) + ", "
        s += self.cls.__name__ + ", "
        kws = [n + "=" + str(getattr(self, n)) for n in self.kwnames]
        s += ", ".join(kws) + ")"
        return s

    def __repr__(self):
        s = self.__class__.__name__ + "(" + repr(self.cmd) + ", "
        s += self.cls.__name__ + ", "
        kws = [n + "=" + repr(getattr(self, n)) for n in self.kwnames]
        s += ", ".join(kws) + ")"
        return s

    #
    # Properties
    #

    @property
    def stdin(self):
        return self._stdin

    @stdin.setter
    def stdin(self, value):
        if self._stdin is None:
            self._stdin = value
        elif value is None:
            pass
        else:
            safe_close(value)
            msg = "Multiple inputs for stdin for {0!r}"
            msg = msg.format(" ".join(self.args))
            raise xt.XonshError(msg)

    @property
    def stdout(self):
        return self._stdout

    @stdout.setter
    def stdout(self, value):
        if self._stdout is None:
            self._stdout = value
        elif value is None:
            pass
        else:
            safe_close(value)
            msg = "Multiple redirections for stdout for {0!r}"
            msg = msg.format(" ".join(self.args))
            raise xt.XonshError(msg)

    @property
    def stderr(self):
        return self._stderr

    @stderr.setter
    def stderr(self, value):
        if self._stderr is None:
            self._stderr = value
        elif value is None:
            pass
        else:
            safe_close(value)
            msg = "Multiple redirections for stderr for {0!r}"
            msg = msg.format(" ".join(self.args))
            raise xt.XonshError(msg)

    #
    # Execution methods
    #

    def run(self, *, pipeline_group=None):
        """Launches the subprocess and returns the object."""
        event_name = self._cmd_event_name()
        self._pre_run_event_fire(event_name)
        kwargs = {n: getattr(self, n) for n in self.kwnames}
        self.prep_env(kwargs)
        if callable(self.alias):
            kwargs["env"]["__ALIAS_NAME"] = self.alias_name or ""
            p = self.cls(self.alias, self.cmd, **kwargs)
        else:
            self.prep_preexec_fn(kwargs, pipeline_group=pipeline_group)
            self._fix_null_cmd_bytes()
            p = self._run_binary(kwargs)
        p.spec = self
        p.last_in_pipeline = self.last_in_pipeline
        p.captured_stdout = self.captured_stdout
        p.captured_stderr = self.captured_stderr
        self._post_run_event_fire(event_name, p)
        return p

    def _run_binary(self, kwargs):
        if not self.cmd[0]:
            raise xt.XonshError("xonsh: subprocess mode: command is empty")
        bufsize = 1
        try:
            p = self.cls(self.cmd, bufsize=bufsize, **kwargs)
        except PermissionError:
            e = "xonsh: subprocess mode: permission denied: {0}"
            raise xt.XonshError(e.format(self.cmd[0]))
        except FileNotFoundError:
            cmd0 = self.cmd[0]
            if len(self.cmd) == 1 and cmd0.endswith("?"):
                with contextlib.suppress(OSError):
                    return self.cls(
                        ["man", cmd0.rstrip("?")], bufsize=bufsize, **kwargs
                    )
            e = "xonsh: subprocess mode: command not found: {0}".format(cmd0)
            env = XSH.env
            sug = xt.suggest_commands(cmd0, env, XSH.aliases)
            if len(sug.strip()) > 0:
                e += "\n" + xt.suggest_commands(cmd0, env, XSH.aliases)
            raise xt.XonshError(e)
        return p

    def prep_env(self, kwargs):
        """Prepares the environment to use in the subprocess."""
        with XSH.env.swap(self.env) as env:
            denv = env.detype()
        if xp.ON_WINDOWS:
            # Over write prompt variable as xonsh's $PROMPT does
            # not make much sense for other subprocs
            denv["PROMPT"] = "$P$G"
        kwargs["env"] = denv

    def prep_preexec_fn(self, kwargs, pipeline_group=None):
        """Prepares the 'preexec_fn' keyword argument"""
        if not xp.ON_POSIX:
            return
        if not XSH.env.get("XONSH_INTERACTIVE"):
            return
        if pipeline_group is None or xp.ON_WSL:
            # If there is no pipeline group
            # or the platform is windows subsystem for linux (WSL)
            xonsh_preexec_fn = no_pg_xonsh_preexec_fn
        else:

            def xonsh_preexec_fn():
                """Preexec function bound to a pipeline group."""
                os.setpgid(0, pipeline_group)
                signal.signal(
                    signal.SIGTERM if xp.ON_WINDOWS else signal.SIGTSTP,
                    default_signal_pauser,
                )

        kwargs["preexec_fn"] = xonsh_preexec_fn

    def _fix_null_cmd_bytes(self):
        # Popen does not accept null bytes in its input commands.
        # That doesn't stop some subprocesses from using them. Here we
        # escape them just in case.
        cmd = self.cmd
        for i in range(len(cmd)):
            if callable(cmd[i]):
                raise Exception(f"The command contains callable argument: {cmd[i]}")
            cmd[i] = cmd[i].replace("\0", "\\0")

    def _cmd_event_name(self):
        if callable(self.alias):
            return getattr(self.alias, "__name__", repr(self.alias))
        elif self.binary_loc is None:
            return "<not-found>"
        else:
            return os.path.basename(self.binary_loc)

    def _pre_run_event_fire(self, name):
        events = XSH.builtins.events
        event_name = "on_pre_spec_run_" + name
        if events.exists(event_name):
            event = getattr(events, event_name)
            event.fire(spec=self)

    def _post_run_event_fire(self, name, proc):
        events = XSH.builtins.events
        event_name = "on_post_spec_run_" + name
        if events.exists(event_name):
            event = getattr(events, event_name)
            event.fire(spec=self, proc=proc)

    #
    # Building methods
    #

    @classmethod
    def build(kls, cmd, *, cls=subprocess.Popen, **kwargs):
        """Creates an instance of the subprocess command, with any
        modifications and adjustments based on the actual cmd that
        was received.
        """
        if not cmd:
            raise xt.XonshError("xonsh: subprocess mode: command is empty")
        # modifications that do not alter cmds may come before creating instance
        spec = kls(cmd, cls=cls, **kwargs)
        # modifications that alter cmds must come after creating instance
        # perform initial redirects
        spec.redirect_leading()
        spec.redirect_trailing()
        # apply aliases
        spec.resolve_alias()
        spec.resolve_binary_loc()
        spec.resolve_auto_cd()
        spec.resolve_executable_commands()
        spec.resolve_alias_cls()
        spec.resolve_stack()
        return spec

    def redirect_leading(self):
        """Manage leading redirects such as with '< input.txt COMMAND'."""
        while len(self.cmd) >= 3 and self.cmd[0] == "<":
            self.stdin = safe_open(self.cmd[1], "r")
            self.cmd = self.cmd[2:]

    def redirect_trailing(self):
        """Manages trailing redirects."""
        while True:
            cmd = self.cmd
            if len(cmd) >= 3 and _is_redirect(cmd[-2]):
                streams = _redirect_streams(cmd[-2], cmd[-1])
                self.stdin, self.stdout, self.stderr = streams
                self.cmd = cmd[:-2]
            elif len(cmd) >= 2 and _is_redirect(cmd[-1]):
                streams = _redirect_streams(cmd[-1])
                self.stdin, self.stdout, self.stderr = streams
                self.cmd = cmd[:-1]
            else:
                break

    def resolve_alias(self):
        """Sets alias in command, if applicable."""
        cmd0 = self.cmd[0]

        if cmd0 in self.alias_stack:
            # Disabling the alias resolving to prevent infinite loop in call stack
            # and futher using binary_loc to resolve the alias name.
            self.alias = None
            return

        if callable(cmd0):
            alias = cmd0
        else:
            alias = XSH.aliases.get(cmd0, None)
            if alias is not None:
                self.alias_name = cmd0
        self.alias = alias

    def resolve_binary_loc(self):
        """Sets the binary location"""
        alias = self.alias
        if alias is None:
            cmd0 = self.cmd[0]
            binary_loc = xenv.locate_binary(cmd0)
            if binary_loc == cmd0 and cmd0 in self.alias_stack:
                raise Exception(f'Recursive calls to "{cmd0}" alias.')
        elif callable(alias):
            binary_loc = None
        else:
            binary_loc = xenv.locate_binary(alias[0])
        self.binary_loc = binary_loc

    def resolve_auto_cd(self):
        """Implements AUTO_CD functionality."""
        if not (
            self.alias is None
            and self.binary_loc is None
            and len(self.cmd) == 1
            and XSH.env.get("AUTO_CD")
            and os.path.isdir(self.cmd[0])
        ):
            return
        self.cmd.insert(0, "cd")
        self.alias = XSH.aliases.get("cd", None)

    def resolve_executable_commands(self):
        """Resolve command executables, if applicable."""
        alias = self.alias
        if alias is None:
            pass
        elif callable(alias):
            self.cmd.pop(0)
            return
        else:
            self.cmd = alias + self.cmd[1:]
            # resolve any redirects the aliases may have applied
            self.redirect_leading()
            self.redirect_trailing()
        if self.binary_loc is None:
            return
        try:
            scriptcmd = get_script_subproc_command(self.binary_loc, self.cmd[1:])
            if scriptcmd is not None:
                self.cmd = scriptcmd
        except PermissionError:
            e = "xonsh: subprocess mode: permission denied: {0}"
            raise xt.XonshError(e.format(self.cmd[0]))

    def resolve_alias_cls(self):
        """Determine which proxy class to run an alias with."""
        alias = self.alias
        if not callable(alias):
            return
        self.is_proxy = True
        env = XSH.env
        thable = env.get("THREAD_SUBPROCS") and getattr(
            alias, "__xonsh_threadable__", True
        )
        cls = ProcProxyThread if thable else ProcProxy
        self.cls = cls
        self.threadable = thable
        # also check capturability, while we are here
        cpable = getattr(alias, "__xonsh_capturable__", self.captured)
        self.captured = cpable

    def resolve_stack(self):
        """Computes the stack for a callable alias's call-site, if needed."""
        if not callable(self.alias):
            return
        # check that we actual need the stack
        sig = inspect.signature(self.alias)
        if len(sig.parameters) <= 5 and "stack" not in sig.parameters:
            return
        # compute the stack, and filter out these build methods
        # run_subproc() is the 4th command in the stack
        # we want to filter out one up, e.g. subproc_captured_hiddenobject()
        # after that the stack from the call site starts.
        stack = inspect.stack(context=0)
        assert stack[3][3] == "run_subproc", "xonsh stack has changed!"
        del stack[:5]
        self.stack = stack


def _safe_pipe_properties(fd, use_tty=False):
    """Makes sure that a pipe file descriptor properties are sane."""
    if not use_tty:
        return
    # due to some weird, long standing issue in Python, PTYs come out
    # replacing newline \n with \r\n. This causes issues for raw unix
    # protocols, like git and ssh, which expect unix line endings.
    # see https://mail.python.org/pipermail/python-list/2013-June/650460.html
    # for more details and the following solution.
    props = xli.termios.tcgetattr(fd)
    props[1] = props[1] & (~xli.termios.ONLCR) | xli.termios.ONLRET
    xli.termios.tcsetattr(fd, xli.termios.TCSANOW, props)
    # newly created PTYs have a stardard size (24x80), set size to the same size
    # than the current terminal
    winsize = None
    if sys.stdin.isatty():
        winsize = xli.fcntl.ioctl(sys.stdin.fileno(), xli.termios.TIOCGWINSZ, b"0000")
    elif sys.stdout.isatty():
        winsize = xli.fcntl.ioctl(sys.stdout.fileno(), xli.termios.TIOCGWINSZ, b"0000")
    elif sys.stderr.isatty():
        winsize = xli.fcntl.ioctl(sys.stderr.fileno(), xli.termios.TIOCGWINSZ, b"0000")
    if winsize is not None:
        xli.fcntl.ioctl(fd, xli.termios.TIOCSWINSZ, winsize)


def _update_last_spec(last):
    env = XSH.env
    captured = last.captured
    last.last_in_pipeline = True
    if not captured:
        return
    callable_alias = callable(last.alias)
    if callable_alias:
        pass
    else:
        cmds_cache = XSH.commands_cache
        thable = (
            env.get("THREAD_SUBPROCS")
            and (captured != "hiddenobject" or env.get("XONSH_CAPTURE_ALWAYS"))
            and cmds_cache.predict_threadable(last.args)
            and cmds_cache.predict_threadable(last.cmd)
        )
        if captured and thable:
            last.cls = PopenThread
        elif not thable:
            # foreground processes should use Popen
            last.threadable = False
            if captured == "object" or captured == "hiddenobject":
                # CommandPipeline objects should not pipe stdout, stderr
                return
    # cannot used PTY pipes for aliases, for some dark reason,
    # and must use normal pipes instead.
    use_tty = xp.ON_POSIX and not callable_alias
    # Do not set standard in! Popen is not a fan of redirections here
    # set standard out
    if last.stdout is not None:
        last.universal_newlines = True
    elif captured in STDOUT_CAPTURE_KINDS:
        last.universal_newlines = False
        r, w = os.pipe()
        last.stdout = safe_open(w, "wb")
        last.captured_stdout = safe_open(r, "rb")
    elif XSH.stdout_uncaptured is not None:
        last.universal_newlines = True
        last.stdout = XSH.stdout_uncaptured
        last.captured_stdout = last.stdout
    elif xp.ON_WINDOWS and not callable_alias:
        last.universal_newlines = True
        last.stdout = None  # must truly stream on windows
        last.captured_stdout = ConsoleParallelReader(1)
    else:
        last.universal_newlines = True
        r, w = xli.pty.openpty() if use_tty else os.pipe()
        _safe_pipe_properties(w, use_tty=use_tty)
        last.stdout = safe_open(w, "w")
        _safe_pipe_properties(r, use_tty=use_tty)
        last.captured_stdout = safe_open(r, "r")
    # set standard error
    if last.stderr is not None:
        pass
    elif captured == "stdout":
        pass
    elif captured == "object":
        r, w = os.pipe()
        last.stderr = safe_open(w, "w")
        last.captured_stderr = safe_open(r, "r")
    elif XSH.stderr_uncaptured is not None:
        last.stderr = XSH.stderr_uncaptured
        last.captured_stderr = last.stderr
    elif xp.ON_WINDOWS and not callable_alias:
        last.universal_newlines = True
        last.stderr = None  # must truly stream on windows
    else:
        r, w = xli.pty.openpty() if use_tty else os.pipe()
        _safe_pipe_properties(w, use_tty=use_tty)
        last.stderr = safe_open(w, "w")
        _safe_pipe_properties(r, use_tty=use_tty)
        last.captured_stderr = safe_open(r, "r")
    # redirect stdout to stderr, if we should
    if isinstance(last.stdout, int) and last.stdout == 2:
        # need to use private interface to avoid duplication.
        last._stdout = last.stderr
    # redirect stderr to stdout, if we should
    if callable_alias and last.stderr == subprocess.STDOUT:
        last._stderr = last.stdout
        last.captured_stderr = last.captured_stdout


def cmds_to_specs(cmds, captured=False, envs=None):
    """Converts a list of cmds to a list of SubprocSpec objects that are
    ready to be executed.
    """
    # first build the subprocs independently and separate from the redirects
    i = 0
    specs = []
    redirects = []
    for i, cmd in enumerate(cmds):
        if isinstance(cmd, str):
            redirects.append(cmd)
        else:
            env = envs[i] if envs is not None else None
            spec = SubprocSpec.build(cmd, captured=captured, env=env)
            spec.pipeline_index = i
            specs.append(spec)
            i += 1
    # now modify the subprocs based on the redirects.
    for i, redirect in enumerate(redirects):
        if redirect == "|":
            # these should remain integer file descriptors, and not Python
            # file objects since they connect processes.
            r, w = os.pipe()
            specs[i].stdout = w
            specs[i + 1].stdin = r
        elif redirect == "&" and i == len(redirects) - 1:
            specs[i].background = True
        else:
            raise xt.XonshError(f"unrecognized redirect {redirect!r}")
    # Apply boundary conditions
    _update_last_spec(specs[-1])
    return specs


def _should_set_title(captured=False):
    env = XSH.env
    return (
        env.get("XONSH_INTERACTIVE")
        and not env.get("XONSH_STORE_STDOUT")
        and captured not in STDOUT_CAPTURE_KINDS
        and XSH.shell is not None
    )


def run_subproc(cmds, captured=False, envs=None):
    """Runs a subprocess, in its many forms. This takes a list of 'commands,'
    which may be a list of command line arguments or a string, representing
    a special connecting character.  For example::

        $ ls | grep wakka

    is represented by the following cmds::

        [['ls'], '|', ['grep', 'wakka']]

    Lastly, the captured argument affects only the last real command.
    """
    if XSH.env.get("XONSH_TRACE_SUBPROC"):
        print(f"TRACE SUBPROC: {cmds}, captured={captured}", file=sys.stderr)

    specs = cmds_to_specs(cmds, captured=captured, envs=envs)
    captured = specs[-1].captured
    if captured == "hiddenobject":
        command = HiddenCommandPipeline(specs)
    else:
        command = CommandPipeline(specs)
    proc = command.proc
    background = command.spec.background
    if not all(x.is_proxy for x in specs):
        xj.add_job(
            {
                "cmds": cmds,
                "pids": [i.pid for i in command.procs],
                "obj": proc,
                "bg": background,
                "pipeline": command,
                "pgrp": command.term_pgid,
            }
        )
    if _should_set_title(captured=captured):
        # set title here to get currently executing command
        pause_call_resume(proc, XSH.shell.settitle)
    else:
        # for some reason, some programs are in a stopped state when the flow
        # reaches this point, hence a SIGCONT should be sent to `proc` to make
        # sure that the shell doesn't hang. This `pause_call_resume` invocation
        # does this
        pause_call_resume(proc, int)
    # create command or return if backgrounding.
    if background:
        return
    # now figure out what we should return.
    if captured == "stdout":
        command.end()
        return command.output
    elif captured == "object":
        return command
    elif captured == "hiddenobject":
        command.end()
        return command
    else:
        command.end()
        return

