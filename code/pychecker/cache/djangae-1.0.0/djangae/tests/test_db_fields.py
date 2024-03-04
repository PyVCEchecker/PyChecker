# -*- encoding: utf-8 -*
from collections import OrderedDict
from datetime import timedelta
import datetime
import pickle

# LIBRARIES
from django import forms
from django.core import serializers
from django.db import connection
from django.db import models
from django.db.utils import IntegrityError
from django.conf import settings
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.files.base import ContentFile
from django.core.validators import EmailValidator
from django.test import override_settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.six.moves import range
import django

# DJANGAE
from djangae.contrib import sleuth
from djangae.db import transaction
from djangae.db.caching import disable_cache
from djangae.fields import (
    ComputedBooleanField,
    ComputedCharField,
    ComputedCollationField,
    ComputedIntegerField,
    ComputedPositiveIntegerField,
    ComputedTextField,
    FileField,
    GenericRelationField,
    ImageField,
    JSONField,
    ListField,
    RelatedSetField,
    RelatedListField,
    ShardedCounterField,
    SetField,
    CharField,
    CharOrNoneField,
)
from djangae.fields.counting import DEFAULT_SHARD_COUNT
from djangae.models import CounterShard
from djangae.test import TestCase

from google.appengine.api import datastore


class ComputedFieldModel(models.Model):
    def computer(self):
        return "%s_%s" % (self.int_field, self.char_field)

    int_field = models.IntegerField()
    char_field = models.CharField(max_length=50)
    test_field = ComputedCharField(computer, max_length=50)
    method_calc_field = ComputedCharField("computer", max_length=50)

    class Meta:
        app_label = "djangae"


class FileFieldModel(models.Model):

    file_field = FileField(blank=True, null=True, url_field="file_url_field")
    image_field = ImageField(blank=True, null=True, url_field="image_url_field")
    file_url_field = CharField(blank=True)
    image_url_field = CharField(blank=True)


class ComputedFieldTests(TestCase):
    def test_computed_field(self):
        instance = ComputedFieldModel(int_field=1, char_field="test")
        instance.save()
        self.assertEqual(instance.test_field, "1_test")

        # Try getting and saving the instance again
        instance = ComputedFieldModel.objects.get(test_field="1_test")
        instance.save()

    def test_computed_by_method_name_field(self):
        """ Test that a computed field which specifies its "computer" function as a string of
            the name of a method on the model.
        """
        instance = ComputedFieldModel(int_field=2, char_field="test")
        instance.save()
        self.assertEqual(instance.method_calc_field, "2_test")


class ModelWithCounter(models.Model):
    counter = ShardedCounterField()

    class Meta:
        app_label = "djangae"


class ModelWithManyCounters(models.Model):
    counter1 = ShardedCounterField()
    counter2 = ShardedCounterField()

    class Meta:
        app_label = "djangae"


def update_denormalized_counter(instance, step, is_reset=False):
    instance.denormalized_counter += step

    if is_reset:
        instance.reset_count += 1

    instance.save()


class ModelWithCountersWithCallback(models.Model):
    counter = ShardedCounterField(on_change=update_denormalized_counter)
    denormalized_counter = models.IntegerField(default=0)
    reset_count = models.IntegerField(default=0)

    class Meta:
        app_label = "djangae"


class ModelWithCounterWithManyShards(models.Model):
    # The DEFAULT_SHARD_COUNT is based on the max allowed in a Datastore transaction
    counter = ShardedCounterField(shard_count=DEFAULT_SHARD_COUNT+5)

    class Meta:
        app_label = "djangae"


@python_2_unicode_compatible
class ISOther(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return "%s:%s" % (self.pk, self.name)

    class Meta:
        app_label = "djangae"


class StringPkModel(models.Model):
    name = models.CharField(max_length=500, primary_key=True)


class RelationWithoutReverse(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        app_label = "djangae"


class RelationWithOverriddenDbTable(models.Model):
    class Meta:
        db_table = "bananarama"
        app_label = "djangae"


class GenericRelationModel(models.Model):
    relation_to_anything = GenericRelationField(null=True)
    unique_relation_to_anything = GenericRelationField(null=True, unique=True)

    class Meta:
        app_label = "djangae"


class ISModel(models.Model):
    related_things = RelatedSetField(ISOther)
    related_list = RelatedListField(ISOther, related_name="ismodel_list")
    limted_related = RelatedSetField(RelationWithoutReverse, limit_choices_to={'name': 'banana'}, related_name="+")
    children = RelatedSetField("self", related_name="+")

    class Meta:
        app_label = "djangae"


class IterableFieldModel(models.Model):
    set_field = SetField(models.CharField(max_length=1))
    list_field = ListField(models.CharField(max_length=1))
    set_field_int = SetField(models.BigIntegerField(max_length=1))
    list_field_int = ListField(models.BigIntegerField(max_length=1))
    set_field_dt = SetField(models.DateTimeField())
    list_field_dt = ListField(models.DateTimeField())

    class Meta:
        app_label = "djangae"


class IterableRelatedModel(models.Model):
    related_set = RelatedListField(ISOther, related_name="+")
    related_list = RelatedListField(ISOther, related_name="+")


class IterableRelatedWithNonIntPkModel(models.Model):
    related_set = RelatedListField(StringPkModel, related_name="+")
    related_list = RelatedListField(StringPkModel, related_name="+")


class IterableFieldsWithValidatorsModel(models.Model):
    set_field = SetField(models.CharField(max_length=100), min_length=2, max_length=3, blank=False)
    list_field = ListField(models.CharField(max_length=100), min_length=2, max_length=3, blank=False)
    related_set = RelatedSetField(ISOther, min_length=2, max_length=3, blank=False)
    related_list = RelatedListField(ISOther, related_name="iterable_list", min_length=2, max_length=3, blank=False)


class JSONFieldModel(models.Model):
    json_field = JSONField(use_ordered_dict=True, blank=True)


class NullableJSONFieldModel(models.Model):
    json_field = JSONField(null=True, blank=True)


class JSONFieldWithDefaultModel(models.Model):
    json_field = JSONField(use_ordered_dict=True)


class ModelWithCharField(models.Model):
    char_field_with_max = CharField(max_length=10, default='', blank=True)
    char_field_without_max = CharField(default='', blank=True)
    char_field_as_email = CharField(validators=[EmailValidator(message='failed')], blank=True)


class ModelWithCharOrNoneField(models.Model):

    char_or_none_field = CharOrNoneField(max_length=100)


class ModelDatabaseA(models.Model):
    set_of_bs = RelatedSetField('ModelDatabaseB', related_name='+')
    list_of_bs = RelatedListField('ModelDatabaseB', related_name='+')

    class Meta:
        app_label = 'djangae'


class ModelDatabaseB(models.Model):
    test_database = 'ns1'

    class Meta:
        app_label = 'djangae'


class CharFieldModel(models.Model):
    char_field = CharField(max_length=500)

    class Meta:
        app_label = "djangae"


class RelatedListFieldRemoveDuplicatesModel(models.Model):
    related_list_field = RelatedListField(CharFieldModel, remove_duplicates=True)


class RelatedListFieldRemoveDuplicatesForm(forms.ModelForm):
    class Meta:
        model = RelatedListFieldRemoveDuplicatesModel
        fields = ['related_list_field']


class ShardedCounterTest(TestCase):
    def test_basic_usage(self):
        instance = ModelWithCounter.objects.create()
        self.assertEqual(0, instance.counter.value())

        instance.counter.increment()
        self.assertEqual(1, instance.counter.value())

        instance.counter.increment()
        self.assertEqual(2, instance.counter.value())

        instance.counter.decrement()
        self.assertEqual(1, instance.counter.value())

        instance.counter.decrement()
        self.assertEqual(0, instance.counter.value())

    def test_negative_counts(self):
        instance = ModelWithCounter.objects.create()
        self.assertEqual(instance.counter.value(), 0)
        instance.counter.decrement(5)
        instance.counter.increment()
        self.assertEqual(instance.counter.value(), -4)

    def test_create_in_transaction(self):
        """ ShardedCounterField shouldn't prevent us from saving the model object inside a transaction.
        """
        with transaction.atomic():
            ModelWithCounter.objects.create()

    def test_increment_step(self):
        """ Test the behvaviour of incrementing in steps of more than 1. """
        instance = ModelWithCounter.objects.create()
        self.assertEqual(instance.counter.value(), 0)
        instance.counter.increment(3)
        instance.counter.increment(2)
        self.assertEqual(instance.counter.value(), 5)

    def test_decrement_step(self):
        """ Test the behvaviour of decrementing in steps of more than 1. """
        instance = ModelWithCounter.objects.create()
        self.assertEqual(instance.counter.value(), 0)
        instance.counter.increment(2)
        instance.counter.increment(7)
        instance.counter.increment(3)
        instance.counter.decrement(7)
        self.assertEqual(instance.counter.value(), 5)

    def test_reset(self):
        """ Test the behaviour of calling reset() on the field. """
        instance = ModelWithCounter.objects.create()
        self.assertEqual(instance.counter.value(), 0)
        instance.counter.increment(7)
        self.assertEqual(instance.counter.value(), 7)
        instance.counter.reset()
        self.assertEqual(instance.counter.value(), 0)

    def test_reset_negative_count(self):
        """ Test resetting a negative count. """
        instance = ModelWithCounter.objects.create()
        self.assertEqual(instance.counter.value(), 0)
        instance.counter.decrement(7)
        self.assertEqual(instance.counter.value(), -7)
        instance.counter.reset()
        self.assertEqual(instance.counter.value(), 0)

    def test_reset_with_many_shards(self):
        """ Test that even if the counter field has more shards than can be counted in a single
            transaction, that the `reset` method still works.
        """
        instance = ModelWithCounterWithManyShards.objects.create()
        instance.counter.populate()
        instance.counter.increment(5)
        instance.counter.reset()

    def test_populate(self):
        """ Test that the populate() method correctly generates all of the CounterShard objects. """
        instance = ModelWithCounter.objects.create()
        # Initially, none of the CounterShard objects should have been created
        self.assertEqual(len(instance.counter), 0)
        self.assertEqual(CounterShard.objects.count(), 0)
        instance.counter.populate()
        expected_num_shards = instance._meta.get_field('counter').shard_count
        self.assertEqual(len(instance.counter), expected_num_shards)

    def test_populate_is_idempotent_across_threads(self):
        """ Edge case test to make sure that 2 different threads calling .populate() on a field
            don't cause it to exceed the corrent number of shards.
        """
        instance = ModelWithCounter.objects.create()
        same_instance = ModelWithCounter.objects.get()
        instance.counter.populate()
        same_instance.counter.populate()
        # Now reload it from the DB and check that it has the correct number of shards
        instance = ModelWithCounter.objects.get()
        self.assertEqual(instance.counter.all().count(), DEFAULT_SHARD_COUNT)

    def test_label_reference_is_saved(self):
        """ Test that each CounterShard which the field creates is saved with the label of the
            model and field to which it belongs.
        """
        instance = ModelWithCounter.objects.create()
        instance.counter.populate()
        expected_shard_label = '%s.%s' % (ModelWithCounter._meta.db_table, 'counter')
        self.assertEqual(
            CounterShard.objects.filter(label=expected_shard_label).count(),
            len(instance.counter)
        )

    def test_many_counters_on_one_model(self):
        """ Test that have multiple counters on the same model doesn't cause any issues.
            This is mostly to test that the multiple reverse relations to the CounterShard model
            don't clash.
        """
        instance = ModelWithManyCounters.objects.create()
        instance.counter1.increment(5)
        instance.counter1.increment(5)
        instance.counter2.increment(1)
        self.assertEqual(instance.counter1.value(), 10)
        self.assertEqual(instance.counter2.value(), 1)
        instance.counter1.reset()
        self.assertEqual(instance.counter1.value(), 0)
        self.assertEqual(instance.counter2.value(), 1)

    def test_count_issues_deprecation_warning(self):
        """ The RelatedShardManager should warn you when using the deprecated `count()` method
            because its purpose is unclear.
        """
        instance = ModelWithCounter.objects.create()
        self.assertEqual(instance.counter.value(), 0)
        with sleuth.watch("djangae.fields.counting.warnings.warn") as warn:
            instance.counter.count()
            self.assertTrue(warn.called)

    def test_shard_count(self):
        """ The shard_count() method should return the number of CounterShard objects. """
        instance = ModelWithCounter.objects.create()
        self.assertEqual(instance.counter.shard_count(), 0)
        instance.counter.populate()
        self.assertEqual(instance.counter.shard_count(), 24)  # The default shard count is 24

    def test_on_change_callback_called(self):
        """ Test that if ShardedCounter has on_change callback specified, it
            will be called after any change to the counter.
        """
        instance = ModelWithCountersWithCallback.objects.create()
        self.assertEquals(instance.denormalized_counter, 0)

        # callback called after increment
        instance.counter.increment(5)
        instance.refresh_from_db()
        self.assertEquals(instance.denormalized_counter, 5)

        # after decrement
        instance.counter.decrement(1)
        instance.refresh_from_db()
        self.assertEquals(instance.denormalized_counter, 4)

        # and reset
        self.assertEquals(instance.reset_count, 0)
        instance.counter.reset()
        instance.refresh_from_db()
        self.assertEquals(instance.denormalized_counter, 0)
        self.assertEquals(instance.reset_count, 1)


class IterableFieldTests(TestCase):
    def test_filtering_on_iterable_fields(self):
        list1 = IterableFieldModel.objects.create(
            list_field=['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            set_field=set(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
        list2 = IterableFieldModel.objects.create(
            list_field=['A', 'B', 'C', 'H', 'I', 'J'],
            set_field=set(['A', 'B', 'C', 'H', 'I', 'J']))

        # filtering using __contains lookup with ListField:
        qry = IterableFieldModel.objects.filter(list_field__contains='A')
        self.assertEqual(sorted(x.pk for x in qry), sorted([list1.pk, list2.pk]))
        qry = IterableFieldModel.objects.filter(list_field__contains='H')
        self.assertEqual(sorted(x.pk for x in qry), [list2.pk])

        # filtering using __contains lookup with SetField:
        qry = IterableFieldModel.objects.filter(set_field__contains='A')
        self.assertEqual(sorted(x.pk for x in qry), sorted([list1.pk, list2.pk]))
        qry = IterableFieldModel.objects.filter(set_field__contains='H')
        self.assertEqual(sorted(x.pk for x in qry), [list2.pk])

        # filtering using __overlap lookup with ListField:
        qry = IterableFieldModel.objects.filter(list_field__overlap=['A', 'B', 'C'])
        self.assertEqual(sorted(x.pk for x in qry), sorted([list1.pk, list2.pk]))
        qry = IterableFieldModel.objects.filter(list_field__overlap=['H', 'I', 'J'])
        self.assertEqual(sorted(x.pk for x in qry), sorted([list2.pk]))

        # filtering using __overlap lookup with SetField:
        qry = IterableFieldModel.objects.filter(set_field__overlap=set(['A', 'B']))
        self.assertEqual(sorted(x.pk for x in qry), sorted([list1.pk, list2.pk]))
        qry = IterableFieldModel.objects.filter(set_field__overlap=['H'])
        self.assertEqual(sorted(x.pk for x in qry), [list2.pk])

    def test_empty_iterable_fields(self):
        """ Test that an empty set field always returns set(), not None """
        instance = IterableFieldModel()
        # When assigning
        self.assertEqual(instance.set_field, set())
        self.assertEqual(instance.list_field, [])
        instance.save()

        instance = IterableFieldModel.objects.get()
        # When getting it from the db
        self.assertEqual(instance.set_field, set())
        self.assertEqual(instance.list_field, [])

    def test_list_field(self):
        instance = IterableFieldModel.objects.create()
        self.assertEqual([], instance.list_field)
        instance.list_field.append("One")
        self.assertEqual(["One"], instance.list_field)
        instance.save()

        self.assertEqual(["One"], instance.list_field)

        instance = IterableFieldModel.objects.get(pk=instance.pk)
        self.assertEqual(["One"], instance.list_field)

        results = IterableFieldModel.objects.filter(list_field__contains="One")
        self.assertEqual([instance], list(results))

        self.assertEqual([1, 2], ListField(models.IntegerField).to_python("[1, 2]"))

    def test_set_field(self):
        instance = IterableFieldModel.objects.create()
        self.assertEqual(set(), instance.set_field)
        instance.set_field.add("One")
        self.assertEqual(set(["One"]), instance.set_field)
        instance.save()

        self.assertEqual(set(["One"]), instance.set_field)

        instance = IterableFieldModel.objects.get(pk=instance.pk)
        self.assertEqual(set(["One"]), instance.set_field)

        self.assertEqual({1, 2}, SetField(models.IntegerField).to_python("[1, 2]"))

    def test_empty_list_queryable_with_is_null(self):
        instance = IterableFieldModel.objects.create()

        self.assertTrue(IterableFieldModel.objects.filter(set_field__isempty=True).exists())

        instance.set_field.add(1)
        instance.save()

        self.assertFalse(IterableFieldModel.objects.filter(set_field__isempty=True).exists())
        self.assertTrue(IterableFieldModel.objects.filter(set_field__isempty=False).exists())

        self.assertFalse(IterableFieldModel.objects.exclude(set_field__isempty=False).exists())
        self.assertTrue(IterableFieldModel.objects.exclude(set_field__isempty=True).exists())

    def test_serialization(self):
        dt = datetime.datetime(2017, 1, 1, 12)
        instance = IterableFieldModel.objects.create(
            set_field={u"foo"},
            list_field=[u"bar"],
            set_field_int={123L},
            list_field_int=[456L],
            set_field_dt={dt},
            list_field_dt=[dt],
        )

        self.assertEqual("['foo']", instance._meta.get_field("set_field").value_to_string(instance))
        self.assertEqual("['bar']", instance._meta.get_field("list_field").value_to_string(instance))
        self.assertEqual("[123]", instance._meta.get_field("set_field_int").value_to_string(instance))
        self.assertEqual("[456]", instance._meta.get_field("list_field_int").value_to_string(instance))
        self.assertEqual("['2017-01-01T12:00:00']", instance._meta.get_field("set_field_dt").value_to_string(instance))
        self.assertEqual("['2017-01-01T12:00:00']", instance._meta.get_field("list_field_dt").value_to_string(instance))

    def test_saving_forms(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = IterableFieldModel
                fields = ("set_field", "list_field")

        post_data = {
            "set_field": [ "1", "2" ],
            "list_field": [ "1", "2" ]
        }

        form = TestForm(post_data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_cannot_have_min_length_and_blank(self):
        """ Having min_length=X, blank=True doesn't make any sense, especially when you consider
            that django will skip the min_length check when the value (list/set)is empty.
        """
        self.assertRaises(
            ImproperlyConfigured,
            ListField,
            CharField(max_length=100),
            min_length=1,
            blank=True
        )
        self.assertRaises(
            ImproperlyConfigured,
            SetField,
            CharField(max_length=100),
            min_length=1,
            blank=True
        )

    def test_list_field_set_field_min_max_lengths_valid(self):
        """ Test that when the min_legnth and max_length of a ListField and SetField are correct
            that no validation error is rasied.
        """
        others = []
        for x in range(2):
            others.append(ISOther.objects.create())
        instance = IterableFieldsWithValidatorsModel(
            related_set=set(others),  # not being tested here
            related_list=others,  # not being tested here
            set_field=set(["1", "2"]),
            list_field=["1", "2"],
        )
        instance.full_clean()

    def test_list_field_max_length_invalid(self):
        others = []
        for x in range(2):
            others.append(ISOther.objects.create())
        instance = IterableFieldsWithValidatorsModel(
            related_set=set(others),  # not being tested here
            related_list=others,  # not being tested here
            set_field=set(["1", "2"]),  # not being tested here
            list_field=["1", "2", "3", "4", "5"],
        )
        self.assertRaisesMessage(
            ValidationError,
            "{'list_field': [u'Ensure this field has at most 3 items (it has 5).']}",
            instance.full_clean,
        )

    def test_list_field_min_length_invalid(self):
        others = []
        for x in range(2):
            others.append(ISOther.objects.create())
        instance = IterableFieldsWithValidatorsModel(
            related_set=set(others),  # not being tested here
            related_list=others,  # not being tested here
            set_field=set(["1", "2"]),  # not being tested here
            list_field=["1"],
        )
        self.assertRaisesMessage(
            ValidationError,
            "{'list_field': [u'Ensure this field has at least 2 items (it has 1).']}",
            instance.full_clean,
        )

    def test_set_field_max_length_invalid(self):
        others = []
        for x in range(2):
            others.append(ISOther.objects.create())
        instance = IterableFieldsWithValidatorsModel(
            related_set=set(others),  # not being tested here
            related_list=others,  # not being tested here
            list_field=["1", "2"],  # not being tested here
            set_field=set(["1", "2", "3", "4", "5"]),
        )
        self.assertRaisesMessage(
            ValidationError,
            "{'set_field': [u'Ensure this field has at most 3 items (it has 5).']}",
            instance.full_clean,
        )

    def test_set_field_min_length_invalid(self):
        others = []
        for x in range(2):
            others.append(ISOther.objects.create())
        instance = IterableFieldsWithValidatorsModel(
            related_set=set(others),  # not being tested here
            related_list=others,  # not being tested here
            list_field=["1", "2"],  # not being tested here
            set_field=set(["1"]),
        )
        self.assertRaisesMessage(
            ValidationError,
            "{'set_field': [u'Ensure this field has at least 2 items (it has 1).']}",
            instance.full_clean,
        )

    def test_list_field_serializes_and_deserializes(self):
        obj = IterableFieldModel(list_field=['foo', 'bar'])
        data = serializers.serialize('json', [obj])

        new_obj = serializers.deserialize('json', data).next().object
        self.assertEqual(new_obj.list_field, ['foo', 'bar'])

    def test_set_field_serializes_and_deserializes(self):
        obj = IterableFieldModel(set_field=set(['foo', 'bar']))
        data = serializers.serialize('json', [obj])

        new_obj = serializers.deserialize('json', data).next().object
        self.assertEqual(new_obj.set_field, set(['foo', 'bar']))


class RelatedIterableFieldTests(TestCase):
    """ Combined tests for common RelatedListField and RelatedSetField tests. """
    multi_db = True

    def test_cannot_have_min_length_and_blank(self):
        """ Having min_length=X, blank=True doesn't make any sense, especially when you consider
            that django will skip the min_length check when the value (list/set)is empty.
        """
        self.assertRaises(
            ImproperlyConfigured,
            RelatedListField,
            ISModel,
            min_length=1,
            blank=True
        )
        self.assertRaises(
            ImproperlyConfigured,
            RelatedSetField,
            ISModel,
            min_length=1,
            blank=True
        )

    def test_related_list_field_set_field_min_max_lengths_valid(self):
        """ Test that when the min_legnth and max_length of a ListField and SetField are correct
            that no validation error is rasied.
        """
        others = []
        for x in range(2):
            others.append(ISOther.objects.create())
        instance = IterableFieldsWithValidatorsModel(
            list_field=["1", "2"],  # not being tested here
            set_field=set(["1", "2"]),  # not being tested here
            related_set=set(others),
            related_list=others,
        )
        instance.full_clean()

    def test_related_list_field_max_length_invalid(self):
        others = []
        for x in range(5):
            others.append(ISOther.objects.create())
        instance = IterableFieldsWithValidatorsModel(
            list_field=["1", "2"],  # not being tested here
            set_field=set(["1", "2"]),  # not being tested here
            related_set=set(others[:2]),  # not being tested here
            related_list=others,
        )
        self.assertRaisesMessage(
            ValidationError,
            "{'related_list': [u'Ensure this field has at most 3 items (it has 5).']}",
            instance.full_clean,
        )

    def test_related_list_field_min_length_invalid(self):
        others = []
        for x in range(2):
            others.append(ISOther.objects.create())
        instance = IterableFieldsWithValidatorsModel(
            list_field=["1", "2"],  # not being tested here
            set_field=set(["1", "2"]),  # not being tested here
            related_set=set(others),
            related_list=others[:1],
        )
        self.assertRaisesMessage(
            ValidationError,
            "{'related_list': [u'Ensure this field has at least 2 items (it has 1).']}",
            instance.full_clean,
        )

    def test_related_set_field_max_length_invalid(self):
        others = []
        for x in range(5):
            others.append(ISOther.objects.create())
        instance = IterableFieldsWithValidatorsModel(
            list_field=["1", "2"],  # not being tested here
            set_field=set(["1", "2"]),  # not being tested here
            related_list=others[:2],  # not being tested here
            related_set=set(others),
        )
        self.assertRaisesMessage(
            ValidationError,
            "{'related_set': [u'Ensure this field has at most 3 items (it has 5).']}",
            instance.full_clean,
        )

    def test_related_set_field_min_length_invalid(self):
        others = []
        for x in range(2):
            others.append(ISOther.objects.create())
        instance = IterableFieldsWithValidatorsModel(
            list_field=["1", "2"],  # not being tested here
            set_field=set(["1", "2"]),  # not being tested here
            related_list=others,  # not being tested here
            related_set=set(others[:1]),
        )
        self.assertRaisesMessage(
            ValidationError,
            "{'related_set': [u'Ensure this field has at least 2 items (it has 1).']}",
            instance.full_clean,
        )

    def test_model_stores_ids_as_integers_when_saving(self):
        others = []
        for x in range(2):
            others.append(ISOther.objects.create())

        instance = IterableRelatedModel(
            related_set_ids=[str(x.pk) for x in others],
            related_list_ids=[str(x.pk) for x in others],
        )

        instance.save()
        instance.refresh_from_db()

        self.assertEqual(instance.related_set_ids, [int(x.pk) for x in others])
        self.assertEqual(instance.related_list_ids, [int(x.pk) for x in others])

    def test_model_stores_ids_as_non_integers(self):
        others = []
        for x in range(2):
            others.append(StringPkModel.objects.create(name=str(x)))

        instance = IterableRelatedWithNonIntPkModel(
            related_set_ids=[x.pk for x in others],
            related_list_ids=[x.pk for x in others],
        )

        instance.save()
        instance.refresh_from_db()

        self.assertEqual(instance.related_set_ids, [x.pk for x in others])
        self.assertEqual(instance.related_list_ids, [x.pk for x in others])

    def test_related_set_field_cross_database(self):
        a = ModelDatabaseA.objects.create()
        b = ModelDatabaseB.objects.create()

        self.assertItemsEqual(a.set_of_bs.all(), [])

        a.set_of_bs.add(b)
        a.save()
        self.assertItemsEqual(a.set_of_bs.all(), [b])

        a.set_of_bs.remove(b)
        a.save()
        self.assertItemsEqual(a.set_of_bs.all(), [])

    def test_related_list_field_cross_database(self):
        a = ModelDatabaseA.objects.create()
        b = ModelDatabaseB.objects.create()

        self.assertItemsEqual(a.list_of_bs.all(), [])

        a.list_of_bs.add(b)
        a.save()
        self.assertItemsEqual(a.list_of_bs.all(), [b])

        a.list_of_bs.remove(b)
        a.save()
        self.assertItemsEqual(a.list_of_bs.all(), [])


class RelatedListFieldModelTests(TestCase):

    def test_values_list_queries_work(self):
        a, b = ISOther.objects.create(name="A"), ISOther.objects.create(name="B")
        thing = ISModel.objects.create(related_list_ids=[a.pk, b.pk])

        result = list(thing.related_list.values_list("pk"))
        self.assertEqual(result, [(a.pk,), (b.pk,)])

        result = list(thing.related_list.values_list("pk", flat=True))
        self.assertEqual(result, [a.pk, b.pk])

        result = list(thing.related_list.values_list("name", flat=True))
        self.assertEqual(result, ["A", "B"])

        result = list(thing.related_list.values_list("name"))
        self.assertEqual(result, [("A",), ("B",)])

        result = list(thing.related_list.values_list("pk", "name"))
        self.assertEqual(result, [(a.pk, "A"), (b.pk, "B")])

    def test_indexing_doesnt_over_fetch(self):
        a, b = ISOther.objects.create(), ISOther.objects.create()
        thing = ISModel.objects.create(related_list_ids=[a.pk, b.pk])

        with sleuth.watch('djangae.db.backends.appengine.meta_queries.QueryByKeys.__init__') as get:
            ret = thing.related_list.all()[0]

            self.assertEqual(1, get.call_count)
            self.assertEqual(1, len(get.calls[0].args[2]))

    def test_can_update_related_field_from_form(self):
        related = ISOther.objects.create()
        thing = ISModel.objects.create(related_list=[related])
        before_list = thing.related_list
        thing.related_list.field.save_form_data(thing, [])
        self.assertNotEqual(before_list.all(), thing.related_list.all())

    def test_filtering_on_iterable_fields(self):
        related1 = ISOther.objects.create()
        related2 = ISOther.objects.create()
        related3 = ISOther.objects.create()
        thing = ISModel.objects.create(related_list=[related1, related2])
        # filtering using __contains lookup with ListField:
        qry = ISModel.objects.filter(related_list__contains=related1)
        self.assertEqual(sorted(x.pk for x in qry), [thing.pk])
        # filtering using __overlap lookup with ListField:
        qry = ISModel.objects.filter(related_list__overlap=[related2, related3])
        self.assertEqual(sorted(x.pk for x in qry), [thing.pk])

    def test_saving_forms(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = ISModel
                fields = ("related_list", )

        related = ISOther.objects.create()
        post_data = {
            "related_list": [ str(related.pk) ],
        }

        form = TestForm(post_data)
        self.assertTrue(form.is_valid())
        instance = form.save()
        self.assertEqual([related.pk], instance.related_list_ids)

    def test_remove_duplicates(self):
        """
        make sure that remove_duplicates option works fine for RelatedListField
        """
        instance_one, instance_two, instance_three, instance_four, instance_five = [
            CharFieldModel.objects.create(
                char_field=str(x)
            ) for x in range(5)
        ]
        data = {'related_list_field': [
            instance_two.pk, instance_three.pk, instance_one.pk, instance_two.pk, instance_four.pk
        ]}
        form = RelatedListFieldRemoveDuplicatesForm(data)
        self.assertTrue(form.is_valid())
        obj = form.save()

        self.assertEqual(
            obj.related_list_field_ids,
            [instance_two.pk, instance_three.pk, instance_one.pk, instance_four.pk]
        )
        obj.related_list_field.add(instance_four, instance_five)
        obj.save()
        self.assertEqual(
            obj.related_list_field_ids,
            [instance_two.pk, instance_three.pk, instance_one.pk, instance_four.pk, instance_five.pk]
        )


class Post(models.Model):
    content = models.TextField()
    tags = RelatedSetField('Tag', related_name='posts')
    ordered_tags = RelatedListField('Tag')


class Tag(models.Model):
    name = models.CharField(max_length=64)


class RelatedSetFieldModelTests(TestCase):

    def test_can_update_related_field_from_form(self):
        related = ISOther.objects.create()
        thing = ISModel.objects.create(related_things={related})
        before_set = thing.related_things
        thing.related_list.field.save_form_data(thing, set())
        thing.save()
        self.assertNotEqual(before_set.all(), thing.related_things.all())

    def test_prefetch_related(self):
        tag = Tag.objects.create(name="Apples")

        for i in range(2):
            Post.objects.create(content="Bananas", tags={tag})

        posts = list(Post.objects.prefetch_related('tags').all())
        self.assertNumQueries(0, list, posts[0].tags.all())

    def test_saving_forms(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = ISModel
                fields = ("related_things", )

        related = ISOther.objects.create()
        post_data = {
            "related_things": [ str(related.pk) ],
        }

        form = TestForm(post_data)
        self.assertTrue(form.is_valid())
        instance = form.save()
        self.assertEqual({related.pk}, instance.related_things_ids)


class InstanceListFieldTests(TestCase):

    def test_deserialization(self):
        i1 = ISOther.objects.create(pk=1)
        i2 = ISOther.objects.create(pk=2)
        # Does the to_python need to return ordered list? SetField test only passes because the set
        # happens to order it correctly
        self.assertItemsEqual([i1, i2], ISModel._meta.get_field("related_list").to_python("[1, 2]"))

    def test_prefetch_related(self):
        tags = [
            Tag.objects.create(name="1"),
            Tag.objects.create(name="2"),
            Tag.objects.create(name="3")
        ]

        # Extra one to make sure we're filtering properly
        Tag.objects.create(name="unused")

        for i in range(3):
            Post.objects.create(content="Bananas", ordered_tags=tags)

        with self.assertNumQueries(2):
            # 1 query on Posts + 1 query on Tags
            posts = list(Post.objects.prefetch_related('ordered_tags').all())

        with self.assertNumQueries(0):
            posts[0].tags.all()
            posts[1].tags.all()
            posts[2].tags.all()

        self.assertEqual(posts[0].ordered_tags.all()[0].name, "1")
        self.assertEqual(posts[0].ordered_tags.all()[1].name, "2")
        self.assertEqual(posts[0].ordered_tags.all()[2].name, "3")

    def test_default_on_delete_does_nothing(self):
        child = ISOther.objects.create(pk=1)
        parent = ISModel.objects.create(related_list=[child])

        child.delete()

        try:
            parent = ISModel.objects.get(pk=parent.pk)
            self.assertEqual([1], parent.related_list_ids)
        except ISModel.DoesNotExist:
            self.fail("Parent instance was deleted, apparently by on_delete=CASCADE")

    def test_save_and_load_empty(self):
        """
        Create a main object with no related items,
        get a copy of it back from the db and try to read items.
        """
        main = ISModel.objects.create()
        main_from_db = ISModel.objects.get(pk=main.pk)

        # Fetch the container from the database and read its items
        self.assertItemsEqual(main_from_db.related_list.all(), [])

    def test_basic_usage(self):
        main = ISModel.objects.create()
        other = ISOther.objects.create(name="test")
        other2 = ISOther.objects.create(name="test2")

        main.related_list.add(other)
        main.save()

        self.assertEqual([other.pk,], main.related_list_ids)
        self.assertEqual(list(ISOther.objects.filter(pk__in=main.related_list_ids)), list(main.related_list.all()))
        self.assertEqual([main], list(other.ismodel_list.all()))

        main.related_list.remove(other)
        self.assertFalse(main.related_list)

        main.related_list = [other2, ]
        self.assertEqual([other2.pk, ], main.related_list_ids)

        with self.assertRaises(AttributeError):
            other.ismodel_list = [main, ]

        without_reverse = RelationWithoutReverse.objects.create(name="test3")
        self.assertFalse(hasattr(without_reverse, "ismodel_list"))

    def test_add_to_empty(self):
        """
        Create a main object with no related items,
        get a copy of it back from the db and try to add items.
        """
        main = ISModel.objects.create()
        main_from_db = ISModel.objects.get(pk=main.pk)

        other = ISOther.objects.create()
        main_from_db.related_list.add(other)
        main_from_db.save()

    def test_add_another(self):
        """
        Create a main object with related items,
        get a copy of it back from the db and try to add more.
        """
        main = ISModel.objects.create()
        other1 = ISOther.objects.create()
        main.related_things.add(other1)
        main.save()

        main_from_db = ISModel.objects.get(pk=main.pk)
        other2 = ISOther.objects.create()

        main_from_db.related_list.add(other2)
        main_from_db.save()

    def test_multiple_objects(self):
        main = ISModel.objects.create()
        other1 = ISOther.objects.create()
        other2 = ISOther.objects.create()

        main.related_list.add(other1, other2)
        main.save()

        main_from_db = ISModel.objects.get(pk=main.pk)
        self.assertEqual(main_from_db.related_list.count(), 2)

    def test_deletion(self):
        """
        Delete one of the objects referred to by the related field
        """
        main = ISModel.objects.create()
        other = ISOther.objects.create()
        main.related_list.add(other)
        main.save()

        other.delete()
        self.assertEqual(main.related_list.count(), 0)

    def test_ordering_is_maintained(self):
        main = ISModel.objects.create()
        other = ISOther.objects.create()
        other1 = ISOther.objects.create()
        other2 = ISOther.objects.create()
        other3 = ISOther.objects.create()
        main.related_list.add(other, other1, other2, other3)
        main.save()
        self.assertEqual(main.related_list.count(), 4)
        self.assertEqual([other.pk, other1.pk, other2.pk, other3.pk, ], main.related_list_ids)
        self.assertItemsEqual([other, other1, other2, other3, ], main.related_list.all())
        main.related_list.clear()
        main.save()
        self.assertEqual([], main.related_list_ids)

    def test_duplicates_maintained(self):
        """
            For whatever reason you might want many of the same relation in the
            list
        """
        main = ISModel.objects.create()
        other = ISOther.objects.create()
        other1 = ISOther.objects.create()
        other2 = ISOther.objects.create()
        other3 = ISOther.objects.create()
        main.related_list.add(other, other1, other2, other1, other3,)
        main.save()
        self.assertEqual([other.pk, other1.pk, other2.pk, other1.pk, other3.pk, ], main.related_list_ids)
        self.assertItemsEqual([other, other1, other2, other1, other3, ], main.related_list.all())

    def test_slicing(self):
        main = ISModel.objects.create()
        other = ISOther.objects.create()
        other1 = ISOther.objects.create()
        other2 = ISOther.objects.create()
        other3 = ISOther.objects.create()
        main.related_list.add(other, other1, other2, other1, other3,)
        main.save()
        self.assertItemsEqual([other, other1, ], main.related_list.all()[:2])
        self.assertItemsEqual([other1, ], main.related_list.all()[1:2])
        self.assertEqual(other1, main.related_list.all()[1:2][0])

    def test_filtering(self):
        main = ISModel.objects.create()
        other = ISOther.objects.create(name="one")
        other1 = ISOther.objects.create(name="two")
        other2 = ISOther.objects.create(name="one")
        ISOther.objects.create(name="three")
        main.related_list.add(other, other1, other2, other1, other2,)
        main.save()
        self.assertItemsEqual([other, other2, other2], main.related_list.filter(name="one"))

    def test_related_list_field_serializes_and_deserializes(self):
        obj = ISModel.objects.create()
        foo = ISOther.objects.create(name='foo')
        bar = ISOther.objects.create(name='bar')
        obj.related_list.add(foo, bar)
        obj.save()

        data = serializers.serialize('json', [obj])
        new_obj = serializers.deserialize('json', data).next().object
        self.assertEqual(
            list(new_obj.related_list.all()),
            [foo, bar],
        )


class InstanceSetFieldTests(TestCase):

    def test_deserialization(self):
        i1 = ISOther.objects.create(pk=1)
        i2 = ISOther.objects.create(pk=2)

        self.assertEqual(set([i1, i2]), ISModel._meta.get_field("related_things").to_python("[1, 2]"))

    def test_basic_usage(self):
        main = ISModel.objects.create()
        other = ISOther.objects.create(name="test")
        other2 = ISOther.objects.create(name="test2")

        main.related_things.add(other)
        main.save()

        self.assertEqual({other.pk}, main.related_things_ids)
        self.assertEqual(list(ISOther.objects.filter(pk__in=main.related_things_ids)), list(main.related_things.all()))

        self.assertItemsEqual([main], ISModel.objects.filter(related_things__contains=other).all())
        self.assertItemsEqual([main], list(other.ismodel_set.all()))

        main.related_things.remove(other)
        self.assertFalse(main.related_things_ids)

        main.related_things = {other2}
        self.assertEqual({other2.pk}, main.related_things_ids)

        with self.assertRaises(AttributeError):
            other.ismodel_set = {main}

        without_reverse = RelationWithoutReverse.objects.create(name="test3")
        self.assertFalse(hasattr(without_reverse, "ismodel_set"))

    def test_save_and_load_empty(self):
        """
        Create a main object with no related items,
        get a copy of it back from the db and try to read items.
        """
        main = ISModel.objects.create()
        main_from_db = ISModel.objects.get(pk=main.pk)

        # Fetch the container from the database and read its items
        self.assertItemsEqual(main_from_db.related_things.all(), [])

    def test_add_to_empty(self):
        """
        Create a main object with no related items,
        get a copy of it back from the db and try to add items.
        """
        main = ISModel.objects.create()
        main_from_db = ISModel.objects.get(pk=main.pk)

        other = ISOther.objects.create()
        main_from_db.related_things.add(other)
        main_from_db.save()

    def test_add_another(self):
        """
        Create a main object with related items,
        get a copy of it back from the db and try to add more.
        """
        main = ISModel.objects.create()
        other1 = ISOther.objects.create()
        main.related_things.add(other1)
        main.save()

        main_from_db = ISModel.objects.get(pk=main.pk)
        other2 = ISOther.objects.create()

        main_from_db.related_things.add(other2)
        main_from_db.save()

    def test_multiple_objects(self):
        main = ISModel.objects.create()
        other1 = ISOther.objects.create()
        other2 = ISOther.objects.create()

        main.related_things.add(other1, other2)
        main.save()

        main_from_db = ISModel.objects.get(pk=main.pk)
        self.assertEqual(main_from_db.related_things.count(), 2)

    def test_deletion(self):
        """
        Delete one of the objects referred to by the related field
        """
        main = ISModel.objects.create()
        other = ISOther.objects.create()
        main.related_things.add(other)
        main.save()

        other.delete()
        self.assertEqual(main.related_things.count(), 0)

    def test_querying_with_isnull(self):
        obj = ISModel.objects.create()

        self.assertItemsEqual([obj], ISModel.objects.filter(related_things__isempty=True))
        self.assertItemsEqual([obj], ISModel.objects.filter(related_things_ids__isempty=True))

    def test_related_set_field_serializes_and_deserializes(self):
        obj = ISModel.objects.create()
        foo = ISOther.objects.create(name='foo')
        bar = ISOther.objects.create(name='bar')
        obj.related_things.add(foo, bar)
        obj.save()

        data = serializers.serialize('json', [obj])

        new_obj = serializers.deserialize('json', data).next().object
        self.assertEqual(
            set(new_obj.related_things.all()),
            set([foo, bar]),
        )


class TestGenericRelationField(TestCase):
    def test_basic_usage(self):
        instance = GenericRelationModel.objects.create()
        self.assertIsNone(instance.relation_to_anything)

        thing = ISOther.objects.create()
        instance.relation_to_anything = thing
        instance.save()

        self.assertTrue(instance.relation_to_anything_id)

        instance = GenericRelationModel.objects.get()
        self.assertEqual(thing, instance.relation_to_anything)

    def test_overridden_dbtable(self):
        """ Check that the related object having a custom `db_table` doesn't affect the functionality. """
        instance = GenericRelationModel.objects.create()
        self.assertIsNone(instance.relation_to_anything)

        weird = RelationWithOverriddenDbTable.objects.create()
        instance.relation_to_anything = weird
        instance.save()

        self.assertTrue(instance.relation_to_anything)

        instance = GenericRelationModel.objects.get()
        self.assertEqual(weird, instance.relation_to_anything)

    def test_querying(self):
        thing = ISOther.objects.create()
        instance = GenericRelationModel.objects.create(relation_to_anything=thing)
        self.assertEqual(GenericRelationModel.objects.filter(relation_to_anything=thing)[0], instance)

    def test_unique(self):
        thing = ISOther.objects.create()
        instance = GenericRelationModel.objects.create(unique_relation_to_anything=thing)
        # Trying to create another instance which relates to the same 'thing' should fail
        self.assertRaises(IntegrityError, GenericRelationModel.objects.create, unique_relation_to_anything=thing)
        # But creating 2 objects which both have `unique_relation_to_anything` set to None should be fine
        instance.unique_relation_to_anything = None
        instance.save()
        GenericRelationModel.objects.create(unique_relation_to_anything=None)
        GenericRelationModel.objects.create() # It should work even if we don't explicitly set it to None

    def test_saving_forms(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = GenericRelationModel
                fields = ("relation_to_anything",)

        related = ISOther.objects.create()
        post_data = {
            "relation_to_anything_0": related.__class__._meta.db_table,
            "relation_to_anything_1": related.pk
        }

        form = TestForm(post_data)
        self.assertTrue(form.is_valid())
        instance = form.save()
        self.assertEqual(related, instance.relation_to_anything)


class JSONFieldModelTests(TestCase):

    def test_invalid_data_in_datastore_doesnt_throw_an_error(self):
        """
            If invalid data is found while reading the entity data, then
            we should silently ignore the error and just return the data as-is
            rather than converting to list/dict.

            The reason is that if we blow up on load, then there's no way to load the
            entity (in Django) to repair the data. This is also consistent with the behaviour
            of Django when (for example) you load a NULL from the database into a field that is
            non-nullable. The field value will still be None when read.
        """
        entity = datastore.Entity(JSONFieldModel._meta.db_table, id=1, namespace=settings.DATABASES["default"]["NAMESPACE"])
        entity["json_field"] = "bananas"
        datastore.Put(entity)

        instance = JSONFieldModel.objects.get(pk=1)
        self.assertEqual(instance.json_field, "bananas")

    def test_object_pairs_hook_with_ordereddict(self):
        items = [('first', 1), ('second', 2), ('third', 3), ('fourth', 4)]
        od = OrderedDict(items)

        thing = JSONFieldModel(json_field=od)
        thing.save()

        thing = JSONFieldModel.objects.get()
        self.assertEqual(od, thing.json_field)

    def test_object_pairs_hook_with_normal_dict(self):
        """
        Check that dict is not stored as OrderedDict if
        object_pairs_hook is not set
        """

        # monkey patch field
        field = JSONFieldModel._meta.get_field('json_field')
        field.use_ordered_dict = False

        normal_dict = {'a': 1, 'b': 2, 'c': 3}

        thing = JSONFieldModel(json_field=normal_dict)
        self.assertFalse(isinstance(thing.json_field, OrderedDict))
        thing.save()

        thing = JSONFieldModel.objects.get()
        self.assertFalse(isinstance(thing.json_field, OrderedDict))

        field.use_ordered_dict = True

    def test_float_values(self):
        """ Tests that float values in JSONFields are correctly serialized over repeated saves.
            Regression test for 46e685d4, which fixes floats being returned as strings after a second save.
        """
        test_instance = JSONFieldModel(json_field={'test': 0.1})
        test_instance.save()

        test_instance = JSONFieldModel.objects.get()
        test_instance.save()

        test_instance = JSONFieldModel.objects.get()
        self.assertEqual(test_instance.json_field['test'], 0.1)

    def test_defaults_are_handled_as_pythonic_data_structures(self):
        """ Tests that default values are handled as python data structures and
            not as strings. This seems to be a regression after changes were
            made to remove Subfield from the JSONField and simply use TextField
            instead.
        """
        thing = JSONFieldModel()
        self.assertEqual(thing.json_field, {})

    def test_default_value_correctly_handled_as_data_structure(self):
        """ Test that default value - if provided is not transformed into
            string anymore. Previously we needed string, since we used
            SubfieldBase in JSONField. Since it is now deprecated we need
            to change handling of default value.
        """
        thing = JSONFieldWithDefaultModel()
        self.assertEqual(thing.json_field, {})


class CharFieldModelTests(TestCase):

    def test_char_field_with_max_length_set(self):
        test_bytestrings = [
            (u'01234567891', 11),
            (u'ążźsęćńół', 17),
        ]

        for test_text, byte_len in test_bytestrings:
            test_instance = ModelWithCharField(
                char_field_with_max=test_text,
            )
            self.assertRaisesMessage(
                ValidationError,
                'Ensure this value has at most 10 bytes (it has %d).' % byte_len,
                test_instance.full_clean,
            )

    def test_char_field_with_not_max_length_set(self):
        longest_valid_value = u'0123456789' * 150
        too_long_value = longest_valid_value + u'more'

        test_instance = ModelWithCharField(
            char_field_without_max=longest_valid_value,
        )
        test_instance.full_clean()  # max not reached so it's all good

        test_instance.char_field_without_max = too_long_value
        self.assertRaisesMessage(
            ValidationError,
            u'Ensure this value has at most 1500 bytes (it has 1504).',
            test_instance.full_clean,
         )

    def test_additional_validators_work(self):
        test_instance = ModelWithCharField(char_field_as_email='bananas')
        self.assertRaisesMessage(ValidationError, 'failed', test_instance.full_clean)

    def test_too_long_max_value_set(self):
        try:
            class TestModel(models.Model):
                test_char_field = CharField(max_length=1501)
        except AssertionError as e:
            self.assertEqual(
                e.message,
                'CharFields max_length must not be greater than 1500 bytes.',
            )


class CharOrNoneFieldTests(TestCase):

    def test_char_or_none_field(self):
        # Ensure that empty strings are coerced to None on save
        obj = ModelWithCharOrNoneField.objects.create(char_or_none_field="")
        obj.refresh_from_db()
        self.assertIsNone(obj.char_or_none_field)


class ISStringReferenceModel(models.Model):
    related_things = RelatedSetField('ISOther')
    related_list = RelatedListField('ISOther', related_name="ismodel_list_string")
    limted_related = RelatedSetField('RelationWithoutReverse', limit_choices_to={'name': 'banana'}, related_name="+")
    children = RelatedSetField("self", related_name="+")

    class Meta:
        app_label = "djangae"


class StringReferenceRelatedSetFieldModelTests(TestCase):

    def test_can_update_related_field_from_form(self):
        related = ISOther.objects.create()
        thing = ISStringReferenceModel.objects.create(related_things={related})
        before_set = thing.related_things
        thing.related_list.field.save_form_data(thing, set())
        thing.save()
        self.assertNotEqual(before_set.all(), thing.related_things.all())

    def test_saving_forms(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = ISStringReferenceModel
                fields = ("related_things", )

        related = ISOther.objects.create()
        post_data = {
            "related_things": [ str(related.pk) ],
        }

        form = TestForm(post_data)
        self.assertTrue(form.is_valid())
        instance = form.save()
        self.assertEqual({related.pk}, instance.related_things_ids)


class PFPost(models.Model):
    content = models.TextField()
    authors = RelatedSetField('PFAuthor', related_name='posts')

    class Meta:
        app_label = "djangae"


class PFAuthor(models.Model):
    name = models.CharField(max_length=32)
    awards = RelatedSetField('PFAwards')

    class Meta:
        app_label = "djangae"


class PFAwards(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        app_label = "djangae"


class RelatedFieldPrefetchTests(TestCase):

    def test_prefetch_related(self):
        award = PFAwards.objects.create(name="award")
        author = PFAuthor.objects.create(awards={award})
        post = PFPost.objects.create(authors={author})

        posts = list(PFPost.objects.all().prefetch_related('authors__awards'))

        with self.assertNumQueries(0):
            awards = list(posts[0].authors.all()[0].awards.all())


class PickleTests(TestCase):

    def test_all_fields_are_pickleable(self):
        """ In order to work with Djangae's migrations, all fields must be pickeable. """
        fields = [
            CharField(),
            CharOrNoneField(),
            ComputedBooleanField("method_name"),
            ComputedCharField("method_name"),
            ComputedIntegerField("method_name"),
            ComputedPositiveIntegerField("method_name"),
            ComputedTextField("method_name"),
            GenericRelationField(),
            JSONField(default=list),
            ListField(CharField(), default=["badger"]),
            SetField(CharField(), default=set(["badger"])),
        ]
        if django.VERSION[1] > 8:
            # These 2 fields have different logic for Django 1.8, which prevents them being pickled
            fields.extend([
                RelatedListField(ModelWithCharField),
                RelatedSetField(ModelWithCharField),
                ShardedCounterField(),
            ])
        for field in fields:
            try:
                pickle.dumps(field)
            except (pickle.PicklingError, TypeError) as e:
                self.fail("Could not pickle %r: %s" % (field, e))


class FileFieldTests(TestCase):

    def test_url_field_is_populated(self):
        """ When the `url_field` attribute is passed to the file/image field, that field should be
            populated when the object is saved.
        """
        obj = FileFieldModel.objects.create(
            file_field=ContentFile('file content', name='my_file'),
            image_field=ContentFile('image content', name='my_file'),
        )
        self.assertTrue(obj.file_url_field)
        self.assertTrue(obj.image_url_field)

    def test_get_serving_url_only_called_when_file_modified(self):
        """ App Engine's `get_serving_url` function should only be called when the file is created
            or modified, not on every save.
        """
        with sleuth.watch("djangae.storage.get_serving_url") as get_serving_url_watcher:
            obj = FileFieldModel.objects.create(
                file_field=ContentFile('file content', name='my_file'),
                image_field=ContentFile('image content', name='my_file'),
            )
            self.assertEqual(get_serving_url_watcher.call_count, 2)
            # Re-save the object; the call_count should be unchanged
            obj.save()
            self.assertEqual(get_serving_url_watcher.call_count, 2)
            # Modify the files, the call_count should increase again
            obj.file_field = ContentFile('new file content', name='my_file')
            obj.image_field = ContentFile('new image content', name='my_file')
            obj.save()
            self.assertEqual(get_serving_url_watcher.call_count, 4)


class ModelWithComputedCollationField(models.Model):
    """Test model for `ComputedCollationField`."""

    name = models.CharField(max_length=100)
    name_order = ComputedCollationField('name')

    class Meta:  # noqa
        app_label = "djangae"


class ComputedCollationFieldTests(TestCase):
    """Tests for `ComputedCollationField`."""

    def test_model(self):
        """Tests for a model using a `ComputedCollationField`."""
        ModelWithComputedCollationField.objects.create(name='demo1')


class BinaryFieldModel(models.Model):
    binary = models.BinaryField(null=True)

    class Meta:
        app_label = "djangae"


class BinaryFieldModelTests(TestCase):
    binary_value = b'\xff'

    def test_insert(self):

        obj = BinaryFieldModel.objects.create(binary = self.binary_value)
        obj.save()

        readout = BinaryFieldModel.objects.get(pk = obj.pk)

        assert(readout.binary == self.binary_value)

    def test_none(self):

        obj = BinaryFieldModel.objects.create()
        obj.save()

        readout = BinaryFieldModel.objects.get(pk = obj.pk)

        assert(readout.binary is None)

    def test_update(self):

        obj = BinaryFieldModel.objects.create()
        obj.save()

        toupdate = BinaryFieldModel.objects.get(pk = obj.pk)
        toupdate.binary = self.binary_value
        toupdate.save()

        readout = BinaryFieldModel.objects.get(pk = obj.pk)

        assert(readout.binary == self.binary_value)


class CharFieldModelTest(TestCase):

    def test_query(self):
        instance = CharFieldModel(char_field="foo")
        instance.save()

        readout = CharFieldModel.objects.get(char_field="foo")
        self.assertEqual(readout, instance)

    def test_query_unicode(self):
        name = u'Jacqu\xe9s'

        instance = CharFieldModel(char_field=name)
        instance.save()

        readout = CharFieldModel.objects.get(char_field=name)
        self.assertEqual(readout, instance)

    @override_settings(DEBUG=True)
    def test_query_unicode_debug(self):
        """ Test that unicode query can be performed in DEBUG mode,
            which will use CursorDebugWrapper and call last_executed_query.
        """
        name = u'Jacqu\xe9s'

        instance = CharFieldModel(char_field=name)
        instance.save()

        readout = CharFieldModel.objects.get(char_field=name)
        self.assertEqual(readout, instance)


class DurationFieldModelWithDefault(models.Model):
    duration = models.DurationField(default=timedelta(1,0))

    class Meta:
        app_label = "djangae"


class DurationFieldModelTests(TestCase):

    def test_creates_with_default(self):
        instance = DurationFieldModelWithDefault()

        self.assertEqual(instance.duration, timedelta(1,0))

        instance.save()

        readout = DurationFieldModelWithDefault.objects.get(pk=instance.pk)
        self.assertEqual(readout.duration, timedelta(1,0))

    def test_none_saves_as_default(self):
        instance = DurationFieldModelWithDefault()
        # this could happen if we were reading an existing instance out of the database that didn't have this field
        instance.duration = None
        instance.save()

        readout = DurationFieldModelWithDefault.objects.get(pk=instance.pk)
        self.assertEqual(readout.duration, timedelta(1,0))


class ModelWithNonNullableFieldAndDefaultValue(models.Model):
    some_field = models.IntegerField(null=False, default=1086)


# ModelWithNonNullableFieldAndDefaultValueTests verifies that we maintain same
# behavior as Django with respect to a model field that is non-nullable with default value.
class ModelWithNonNullableFieldAndDefaultValueTests(TestCase):

    def _create_instance_with_null_field_value(self):

        instance = ModelWithNonNullableFieldAndDefaultValue.objects.create(some_field=1)

        entity = datastore.Get(datastore.Key.from_path(ModelWithNonNullableFieldAndDefaultValue._meta.db_table,
                               instance.pk, namespace=connection.settings_dict["NAMESPACE"]))
        del entity["some_field"]
        datastore.Put(entity)

        instance.refresh_from_db()

        return instance

    @disable_cache()
    def test_none_in_db_reads_as_none_in_model(self):

        instance = self._create_instance_with_null_field_value()

        self.assertIsNone(instance.some_field)

    @disable_cache()
    def test_none_in_model_saved_as_default(self):

        instance = self._create_instance_with_null_field_value()

        instance.save()
        instance.refresh_from_db()

        self.assertEqual(instance.some_field, 1086)


