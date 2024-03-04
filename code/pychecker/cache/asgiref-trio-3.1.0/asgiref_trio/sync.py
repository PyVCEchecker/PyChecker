import trio
import functools
import os
import threading
from concurrent.futures import Future, ThreadPoolExecutor

try:
    import contextvars  # Python 3.7+ only.
except ImportError:
    contextvars = None


# https://gist.github.com/njsmith/be24d376faea61cb3999f08318b780f3
class TrioExecutorHelper(trio.abc.AsyncResource):
    def __init__(self, executor):
        self._executor = executor
        
    async def run_sync(self, fn, *args):
        fut = self._executor.submit(fn, *args)
        
        task = trio.hazmat.current_task()
        token = trio.hazmat.current_trio_token()
        def cb(_):
            # If we successfully cancelled from cancel_fn, then
            # this callback still gets called, but we were already
            # rescheduled so we don't need to do it again.
            if not fut.cancelled():
                token.run_sync_soon(trio.hazmat.reschedule, task)
        fut.add_done_callback(cb)
        
        def cancel_fn(_):
            if fut.cancel():
                return trio.hazmat.Abort.SUCCEEDED
            else:
                return trio.hazmat.Abort.FAILED
        await trio.hazmat.wait_task_rescheduled(cancel_fn)
        
        assert fut.done()
        return fut.result()
                
    async def aclose(self):
        # shutdown() has no cancellation support, so we just have to wait it out
        with trio.CancelScope(shield=True):
            await trio.run_sync_in_worker_thread(self._executor.shutdown())


class AsyncToSync:
    """
    Utility class which turns an awaitable that only works on the thread with
    the event loop into a synchronous callable that works in a subthread.

    Must be initialised from the main thread.
    """

    def __init__(self, awaitable):
        self.awaitable = awaitable
        try:
            self.trio_portal = trio.BlockingTrioPortal()
        except RuntimeError:
            # There's no event loop in this thread. Look for the threadlocal if
            # we're inside SyncToAsync
            self.trio_portal = getattr(
                SyncToAsync.threadlocal, "trio_portal", None
            )

    def __call__(self, *args, **kwargs):
        # You can't call AsyncToSync from a thread with a running event loop
        try:
            trio.hazmat.current_trio_token()
        except RuntimeError:
            pass
        else:
            raise RuntimeError(
                "You cannot use AsyncToSync in the same thread as an async event loop - "
                "just await the async function directly."
            )

        # Make a future for the return information
        call_result = Future()

        # Use call_soon_threadsafe to schedule a synchronous callback on the
        # main event loop's thread
        if not self.trio_portal:
            return trio.run(functools.partial(self.awaitable, *args, **kwargs))
        else:
            return self.trio_portal.run(functools.partial(self.awaitable, *args, **kwargs))

    def __get__(self, parent, objtype):
        """
        Include self for methods
        """
        return functools.partial(self.__call__, parent)

    async def main_wrap(self, args, kwargs, call_result):
        """
        Wraps the awaitable with something that puts the result into the
        result/exception future.
        """
        try:
            result = await self.awaitable(*args, **kwargs)
        except Exception as e:
            call_result.set_exception(e)
        else:
            call_result.set_result(result)


class SyncToAsync:
    """
    Utility class which turns a synchronous callable into an awaitable that
    runs in a threadpool. It also sets a threadlocal inside the thread so
    calls to AsyncToSync can escape it.
    """    

    threadlocal = threading.local()

    def __init__(self, func):
        self.func = func

    async def __call__(self, *args, **kwargs):
        if contextvars is not None:
            context = contextvars.copy_context()
            child = functools.partial(self.func, *args, **kwargs)
            func = context.run
            args = (child,)
            kwargs = {}
        else:
            func = self.func

        portal = trio.BlockingTrioPortal()
        return await SyncToAsync.executor.run_sync(
            functools.partial(self.thread_handler, portal, func, *args, **kwargs)
        )

    def __get__(self, parent, objtype):
        """
        Include self for methods
        """
        return functools.partial(self.__call__, parent)

    def thread_handler(self, portal, func, *args, **kwargs):
        """
        Wraps the sync application with exception handling.
        """
        # Set the threadlocal for AsyncToSync
        self.threadlocal.trio_portal = portal
        # Run the function
        return func(*args, **kwargs)


SyncToAsync.executor = TrioExecutorHelper(ThreadPoolExecutor(max_workers=int(os.environ.get("ASGI_THREADS") or 1)))


# Lowercase is more sensible for most things
sync_to_async = SyncToAsync
async_to_sync = AsyncToSync
