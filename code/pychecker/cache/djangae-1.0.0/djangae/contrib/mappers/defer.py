# STANDARD LIB
import logging

# THIRD PARTY
from google.appengine.ext.deferred import defer
from google.appengine.runtime import DeadlineExceededError


logger = logging.getLogger(__name__)


class Redefer(Exception):
    pass


def _process_shard(model, instance_ids, callback):
    logger.debug(
        "Processing shard for model %s, PKs %s to %s",
        model.__name__, instance_ids[0], instance_ids[-1]
    )
    for instance in model.objects.filter(pk__in=instance_ids).iterator():
        callback(instance)
    logger.debug("Done processing shard.")


def _shard(model, query, callback, shard_size, queue, offset=0):
    logger.debug("Sharding PKs for model %s into tasks on queue %s", model.__name__, queue)
    keys_queryset = model.objects.all()
    keys_queryset.query = query
    keys_queryset = keys_queryset.values_list("pk", flat=True)

    # Keep iterating until we are done, or until we might be hitting the task deadline
    shards_deferred = 0
    max_shards_to_defer_in_this_task = 250  # number which we think we can safely do in 10 minutes
    while True:
        try:
            ids = list(keys_queryset.all()[offset:offset + shard_size])
            if not ids:
                # We're done!
                logger.debug(
                    "Finished sharding PKs for model %s into tasks on queue %s.",
                    model.__name__, queue
                )
                return

            # Fire off the first shard
            defer(_process_shard, model, ids, callback, _queue=queue)
            shards_deferred += 1

            # Set the offset to the last pk
            offset += shard_size

            if shards_deferred >= max_shards_to_defer_in_this_task:
                logger.debug("Redeferring. Offset PK: %s", offset)
                raise Redefer()

        except (DeadlineExceededError, Redefer):
            # If we run out of time, or have done enough shards that we might be running out of
            # time, then defer this function again, continuing from the offset.
            defer(
                _shard,
                model,
                query,
                callback,
                shard_size,
                queue,
                offset=offset,
                _queue=queue
            )
            return


def defer_iteration(queryset, callback, shard_size=500, _queue="default", _target=None):
    """
        Shards background tasks to call 'callback' with each instance in queryset

        - `queryset` - The queryset to iterate
        - `callback` - A callable which accepts an instance as a parameter
        - `shard_size` - The number instances to process per shard (default 500)
        - `_queue` - The name of the queue to run the shards on

        Note, your callback must be indempotent, shards may retry and your callback
        may be called multiple times on the same instance. If you notice that your
        tasks are receiving DeadlineExceededErrors you probably need to reduce the
        shard size. The shards will work in parallel and will not be sequential.
    """
    # We immediately defer the _shard function so that we don't hold up execution
    defer(
        _shard, queryset.model, queryset.query, callback, shard_size, _queue,
        _queue=_queue, _target=_target,
    )
