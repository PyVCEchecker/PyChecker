import threading
import new
import logging

import django
from django.db import router, connections, models
from django.apps import apps
from django.utils.encoding import smart_text
from djangae.crc64 import CRC64


logger = logging.getLogger(__name__)

class ListQS(list):
    """
        Hacky wrapper around a list to satisfy related_descriptors.py when accessing contenttypes through
        foreign keys
    """
    def get(self):
        return self[0]


class SimulatedContentTypeManager(models.Manager):
    """
        Simulates content types without actually hitting the datastore.

        The methods in this class are literally stubs which allow the normal Django
        code (Django admin) to believe it's talking to a database.

        ONLY A SMALL SUBSET OF CONTENTTYPE QUERIES ARE SUPPORTED AND THOSE UNSUPPORTED
        MAY JUST RETURN THE WRONG RESULTSET RATHER THAN THROWING AN ERROR. YOU HAVE BEEN WARNED! :)
    """
    use_for_related_fields = True

    _store = threading.local()

    def __init__(self, model=None, *args, **kwargs):
        super(SimulatedContentTypeManager, self).__init__(*args, **kwargs)
        self.model = model

    def _get_model(self):
        """ If we're in a migration, then the 'fake' model class will be passed
            into __init__   and we'll use that.  Otherwise we'll use the 'real'
            ContentType class.
        """
        from django.contrib.contenttypes.models import ContentType
        return self.model or ContentType

    def _get_id(self, app_label, model):
        """
            Generate a unique (ish) ID given the app label and model name
        """
        crc = CRC64()
        crc.append(app_label)
        crc.append(model)
        return crc.fini() - (2 ** 63)  # GAE integers are signed so we shift down

    def _get_opts(self, model, for_concrete_model):
        if for_concrete_model:
            model = model._meta.concrete_model
        elif getattr(model, '_deferred', False) or model is getattr(models, 'DEFERRED', None):
            model = model._meta.proxy_for_model
        return model._meta

    def _update_queries(self, models):
        """
            This is just to satisfy the contenttypes tests which check that queries are executed at certain
            times. It's a bit hacky but it works for that purpose.
        """
        ContentType = self._get_model()
        conn = connections[router.db_for_write(ContentType)]

        if getattr(conn, "use_debug_cursor", getattr(conn, "force_debug_cursor", False)):
            for model in models or []:
                if model not in self._store.queried_models:
                    conn.queries.append("select * from {}".format(ContentType._meta.db_table))
                    break

        if not hasattr(self._store, "queried_models"):
            self._store.queried_models = set()

        self._store.queried_models |= set(models or [])

    def _repopulate_if_necessary(self, models=None):
        if not hasattr(self._store, "queried_models"):
            self._store.queried_models = set()

        if not hasattr(self._store, "constructed_instances"):
            self._store.constructed_instances = {}

        self._update_queries(models)

        if not hasattr(self._store, "content_types"):
            all_models = [(x._meta.app_label, x._meta.model_name, x) for x in apps.get_models()]

            self._update_queries([(x[0], x[1]) for x in all_models])

            content_types = {}
            for app_label, model_name, model in all_models:
                content_type_id = self._get_id(app_label, model_name)

                content_types[content_type_id] = {
                    "id": content_type_id,
                    "app_label": app_label,
                    "model": model_name,
                }
                if django.VERSION < (1, 9):
                    content_types[content_type_id]["name"] = smart_text(model._meta.verbose_name_raw)

            self._store.content_types = content_types

    def get_by_natural_key(self, app_label, model):
        self._repopulate_if_necessary(models=[(app_label, model)])
        return self.get(id=self._get_id(app_label, model))

    def get_for_model(self, model, for_concrete_model=True):
        opts = self._get_opts(model, for_concrete_model)
        self._repopulate_if_necessary(models=[(opts.app_label, opts.model_name)])
        return self.get_by_natural_key(opts.app_label, opts.model_name)

    def get_for_models(self, *models, **kwargs):
        for_concrete_model = kwargs.get("for_concrete_models", True)

        self._update_queries(
            [(self._get_opts(x, for_concrete_model).app_label, self._get_opts(x, for_concrete_model).model_name) for x in models]
        )
        ret = {}
        for model in models:
            ret[model] = self.get_for_model(model, for_concrete_model)

        return ret

    def get_for_id(self, id):
        return self.get(pk=id)

    def clear_cache(self):
        self._store.queried_models = set()

    def _get_from_store(self, id):
        try:
            return self._store.content_types[id]
        except KeyError:
            ContentType = self._get_model()
            raise ContentType.DoesNotExist()

    def get(self, *args, **kwargs):
        # Special case for Django >= 1.11 which sometimes generates Q() objects
        # with a single filter when querying content types. This handles that one
        # case.. if we find there are others we'll have to do something less hacky!
        if args and not kwargs:
            if len(args) == 1 and len(args[0].children) == 1 and not args[0].negated:
                kwargs = dict(args[0].children)
            else:
                raise ValueError("Unsupported Q operation")

        ContentType = self._get_model()
        self._repopulate_if_necessary()

        if "pk" in kwargs:
            kwargs["id"] = kwargs["pk"]
            del kwargs["pk"]

        if "id" in kwargs:
            dic = self._get_from_store(int(kwargs["id"]))
        else:
            for ct in self._store.content_types.values():
                for k, v in kwargs.items():
                    if k not in ct:
                        raise ContentType.DoesNotExist()

                    if ct[k] != v:
                        break
                else:
                    dic = ct
                    break
            else:
                raise ContentType.DoesNotExist()

        def disable_save(*args, **kwargs):
            raise NotImplementedError("You can't save simulated content types")

        # We do this because some tests to comparisons with 'is' so we store
        # constructed ContentTypes in the thread local and return them if possible
        if dic["id"] in self._store.constructed_instances:
            return self._store.constructed_instances[dic["id"]]
        else:
            ContentType = self._get_model()
            result = ContentType(**dic)
            result.save = new.instancemethod(disable_save, ContentType, result)
            self._store.constructed_instances[dic["id"]] = result
            return result

    def create(self, **kwargs):
        self._repopulate_if_necessary()
        logger.warning(
            "Created simulated content type, this will not persist and will remain only on this "
            "app instance"
        )
        new_id = self._get_id(kwargs["app_label"], kwargs["model"])
        kwargs["id"] = new_id
        if "pk" in kwargs:
            del kwargs["pk"]
        self._store.content_types[new_id] = kwargs
        return self.get(id=new_id)

    def get_or_create(self, **kwargs):
        ContentType = self._get_model()
        defaults = kwargs.pop("defaults", None)
        try:
            return self.get(**kwargs), False
        except ContentType.DoesNotExist:
            if defaults:
                kwargs.update(**defaults)
            return self.create(**kwargs), True

    def filter(self, *args, **kwargs):
        self._repopulate_if_necessary()

        def _condition(ct):
            for qobj in args:
                if qobj.connector == 'AND' and not qobj.negated:
                    # normal kwargs are an AND anyway, so just use those for now
                    for child in qobj.children:
                        kwargs.update(dict([child]))
                else:
                    raise NotImplementedError("Unsupported Q object")

            for attr, val in kwargs.items():
                if getattr(ct, attr) != val:
                    return False
            return True

        # We wrap the results in a class which has a .get attribute to satisfy
        # the code which is called when a reverse relation is followed on a ForeignKey
        return ListQS([ct for ct in self.all() if _condition(ct)])

    def all(self, **kwargs):
        return self

    def __iter__(self):
        self._repopulate_if_necessary()

        for ct in self._store.content_types.keys():
            yield self.get(id=ct)

    def __len__(self):
        self._repopulate_if_necessary()
        return len(self._store.content_types)

    def using(self, *args, **kwargs):
        return self

    def bulk_create(self, *args, **kwargs):
        pass
