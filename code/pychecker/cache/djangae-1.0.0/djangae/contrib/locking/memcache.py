import time
from datetime import datetime

from google.appengine.api import memcache

class MemcacheLock(object):
    def __init__(self, identifier, cache):
        self.identifier = identifier
        self._cache = cache

    @classmethod
    def acquire(cls, identifier, wait=True, steal_after_ms=None):
        cache = memcache.Client()

        def expired(value):
            if not value:
                # No value? We're fine
                return True

            return (datetime.utcnow() - value).total_seconds() * 1000 > steal_after_ms

        acquired = cache.add(identifier, datetime.utcnow())
        if acquired:
            # We set the key so we have the lock
            return cls(identifier, cache)
        elif not wait:
            return None
        else:
            while True:
                # We are waiting for a while
                to_set = datetime.utcnow()

                # Use compare-and-set to atomically set our new timestamp
                # if the lock has expired
                stored = cache.gets(identifier)
                if expired(stored):
                    if cache.cas(identifier, to_set):
                        break

                time.sleep(0.1)

            return cls(identifier, cache)

    def release(self):
        cache = self._cache
        cache.delete(self.identifier)
