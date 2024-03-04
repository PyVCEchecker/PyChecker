from django.db import models
from djangae.contrib import sleuth
from djangae.test import TestCase, inconsistent_db
from djangae.utils import get_next_available_port, retry, retry_on_error
from django.utils.encoding import python_2_unicode_compatible
from djangae.db.consistency import ensure_instance_consistent, ensure_instances_consistent
from djangae.db.backends.appengine.context import CacheDict


class AvailablePortTests(TestCase):

    def test_get_next_available_port(self):
        url = "127.0.0.1"
        port = 8091
        self.assertEquals(8091, get_next_available_port(url, port))
        with sleuth.switch(
            "djangae.utils.port_is_open",
            lambda *args, **kwargs: False if args[1] < 8095 else True
        ):
            self.assertEquals(8095, get_next_available_port(url, port))


@python_2_unicode_compatible
class EnsureCreatedModel(models.Model):
    field1 = models.IntegerField()

    class Meta:
        app_label = "djangae"

    def __str__(self):
        return u"PK: {}, field1 {}".format(self.pk, self.field1)


class EnsureCreatedTests(TestCase):

    def test_basic_usage(self):
        for i in range(5):
            EnsureCreatedModel.objects.create(
                pk=i + 1,
                field1=i
            )

        with inconsistent_db():
            new_instance = EnsureCreatedModel.objects.create(
                pk=7,
                field1=3
            )

            qs = EnsureCreatedModel.objects.all()
            self.assertEqual(5, len(qs)) # Make sure we don't get the new instance
            self.assertEqual(6, len(ensure_instance_consistent(qs, new_instance.pk))) # Make sure we do
            self.assertEqual(5, len(ensure_instance_consistent(qs[:5], new_instance.pk))) # Make sure slicing returns the right number
            self.assertEqual(3, len(ensure_instance_consistent(qs[2:5], new_instance.pk))) # Make sure slicing returns the right number

            evaled = [ x for x in ensure_instance_consistent(qs.order_by("field1"), new_instance.pk) ]
            self.assertEqual(new_instance, evaled[4]) # Make sure our instance is correctly positioned

            evaled = [ x for x in ensure_instance_consistent(qs.order_by("-field1"), new_instance.pk) ]
            self.assertEqual(new_instance, evaled[1], evaled) # Make sure our instance is correctly positioned

            evaled = [ x for x in ensure_instance_consistent(qs.order_by("-field1"), new_instance.pk)[:2] ]
            self.assertEqual(new_instance, evaled[1], evaled) # Make sure our instance is correctly positioned

            another_instance = EnsureCreatedModel.objects.create(
                pk=8,
                field1=3
            )

            self.assertEqual(5, len(qs)) # Make sure we don't get the new instance
            self.assertEqual(7, len(ensure_instances_consistent(qs, [new_instance.pk, another_instance.pk]))) # Make sure we do

            instance_id = another_instance.pk
            another_instance.delete()

            self.assertEqual(6, len(ensure_instances_consistent(qs, [new_instance.pk, instance_id]))) # Make sure we do

        # Now we're in consistent land!
        self.assertTrue(EnsureCreatedModel.objects.filter(pk=7)[:1])
        self.assertEqual(6, len(ensure_instance_consistent(qs, new_instance.pk)))

        # Make sure it's not returned if it was deleted
        new_instance.delete()
        self.assertEqual(5, len(ensure_instance_consistent(qs, 7)))

        new_instance = EnsureCreatedModel.objects.create(pk=8, field1=8)
        self.assertEqual(1, list(ensure_instance_consistent(qs, 8)).count(new_instance))

    def test_add_many_instances(self):
        for i in range(5):
            EnsureCreatedModel.objects.create(
                pk=i + 1,
                field1=i + 5
            )

        with inconsistent_db():
            new_instances = []
            for i in range(3):
                instance = EnsureCreatedModel.objects.create(
                    pk=i + 7,
                    field1=i
                )
                new_instances.append(instance)

            new_instance_pks = [i.pk for i in new_instances]

            qs = EnsureCreatedModel.objects.all()
            self.assertEqual(5, len(qs))  # Make sure we don't get the new instance
            self.assertEqual(8, len(ensure_instances_consistent(qs, new_instance_pks)))

            evaled = [ x for x in ensure_instances_consistent(qs.order_by("field1"), new_instance_pks) ]
            self.assertEqual(new_instances[0], evaled[0])  # Make sure our instance is correctly positioned
            self.assertEqual(new_instances[1], evaled[1])  # Make sure our instance is correctly positioned
            self.assertEqual(new_instances[2], evaled[2])  # Make sure our instance is correctly positioned

        # Now we're in consistent land!
        self.assertTrue(EnsureCreatedModel.objects.filter(pk=7)[:1])
        self.assertTrue(EnsureCreatedModel.objects.filter(pk=8)[:1])
        self.assertEqual(8, len(ensure_instances_consistent(qs, new_instance_pks)))

        # Make sure it's not returned if it was deleted
        for instance in new_instances:
            instance.delete()
        self.assertEqual(5, len(ensure_instances_consistent(qs, new_instance_pks)))

    def test_delete_many_instances(self):
        for i in range(5):
            EnsureCreatedModel.objects.create(
                pk=i + 1,
                field1=i + 5
            )

        instances_to_delete = []
        for i in range(3):
            instance = EnsureCreatedModel.objects.create(
                pk=i + 7,
                field1=i + 1
            )
            instances_to_delete.append(instance)

        instances_to_delete_pks = [i.pk for i in instances_to_delete]

        qs = EnsureCreatedModel.objects.all()
        self.assertEqual(8, len(ensure_instances_consistent(qs, instances_to_delete_pks)))
        with inconsistent_db():
            # Make sure it's not returned if it was deleted
            for instance in instances_to_delete:
                instance.delete()
            self.assertEqual(5, len(ensure_instances_consistent(qs, instances_to_delete_pks)))


class CacheDictTests(TestCase):
    # Using a test value of size 280 (a dict), and a cache with room for 3 of them

    def test_size_limit(self):
        cache = CacheDict(max_size_in_bytes=900)
        value = dict(v=100)

        cache.set_multi(['v1'], value)
        cache.set_multi(['v2'], value)
        cache.set_multi(['v3'], value)
        self.assertEqual(set(('v1', 'v2', 'v3')), set(cache.keys()))

        # setting another key will evict the oldest value
        cache.set_multi(['v4'], value)
        self.assertEqual(set(('v2', 'v3', 'v4')), set(cache.keys()))

    def test_priorities(self):
        cache = CacheDict(max_size_in_bytes=900)
        value = dict(v=100)

        cache.set_multi(['v1'], value)
        cache.set_multi(['v2'], value)
        cache.set_multi(['v3'], value)
        cache['v1']
        cache.set_multi(['v4'], value)
        cache.set_multi(['v5'], value)
        cache['v1']
        cache.set_multi(['v6'], value)

        self.assertEqual(set(('v1', 'v5', 'v6')), set(cache.keys()))


class RetryTestCase(TestCase):
    """ Tests for djangae.utils.retry.
        We test the retry_on_error decorator because it tests `retry` by proxy.
    """

    def test_attempts_param(self):
        """ It should only try a maximum of the number of times specified. """

        @retry_on_error(_attempts=2, _initial_wait=0, _catch=Exception)
        def flakey():
            flakey.attempts += 1
            raise Exception("Oops")

        flakey.attempts = 0

        self.assertRaises(Exception, flakey)  # Should fail eventually, after 2 attempts
        self.assertEqual(flakey.attempts, 2)

    def test_catch_param(self):
        """ It should only catch the exceptions given. """

        def flakey():
            flakey.attempts += 1
            raise ValueError("Oops")

        flakey.attempts = 0

        # If we only except TypeError then ValueError should raise immediately
        self.assertRaises(ValueError, retry_on_error(_catch=TypeError)(flakey))
        self.assertEqual(flakey.attempts, 1)  # Only 1 attempt should have been made
        # With the correct _catch param, it should catch our exception
        flakey.attempts = 0  # reset
        self.assertRaises(ValueError, retry_on_error(_catch=ValueError, _initial_wait=0, _attempts=5)(flakey))
        self.assertEqual(flakey.attempts, 5)

    def test_initial_wait_param(self):
        """ The _initial_wait parameter should determine the backoff time for retries, which
            should be doubled for each subsequent retry.
        """

        @retry_on_error(_initial_wait=5, _attempts=3, _catch=Exception, _avoid_clashes=False)
        def flakey():
            raise Exception("Oops")

        with sleuth.watch("djangae.utils.time.sleep") as sleep_watch:
            try:
                flakey()
            except Exception:
                pass

            self.assertEqual(len(sleep_watch.calls), 2)  # It doesn't sleep after the final attempt
            self.assertEqual(sleep_watch.calls[0].args[0], 0.005)  # initial wait in milliseconds
            self.assertEqual(sleep_watch.calls[1].args[0], 0.01)  # initial wait doubled

    def test_max_wait_param(self):
        """ The _max_wait parameter should limit the backoff time for retries, otherwise they will
            keep on doubling.
        """

        @retry_on_error(_initial_wait=1, _max_wait=3, _attempts=10, _catch=Exception)
        def flakey():
            raise Exception("Oops")

        with sleuth.watch("djangae.utils.time.sleep") as sleep_watch:
            try:
                flakey()
            except Exception:
                pass

            self.assertTrue(sleep_watch.called)
            self.assertEqual(len(sleep_watch.calls), 9)  # It doesn't sleep after the final attempt
            sleep_times = [call.args[0] for call in sleep_watch.calls]
            self.assertEqual(max(sleep_times), 0.003)

    def test_args_and_kwargs_passed(self):
        """ Args and kwargs passed to `retry` or to the function decorated with `@retry_on_error`
            should be passed to the wrapped function.
        """

        def flakey(a, b, c=None):
            self.assertEqual(a, 1)
            self.assertEqual(b, 2)
            self.assertEqual(c, 3)

        retry(flakey, 1, 2, c=3)
        retry_on_error()(flakey)(1, 2, c=3)
