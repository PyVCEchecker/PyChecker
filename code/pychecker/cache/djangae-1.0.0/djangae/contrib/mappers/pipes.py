from django.db import router
from djangae.contrib.processing.mapreduce import map_queryset

from djangae.contrib.processing.mapreduce.utils import qualname

class MapReduceTask(object):
    """
        MapReduceTask base class, inherit this in a statically defined class and
        use .start() to run a mapreduce task

        You must define a staticmethod 'map' which takes in an arg of the entity being mapped over.
        Optionally define a staticmethod 'reduce' for the reduce stage (Not Implemented).

        You can pass any additional args and/or kwargs to .start(), which will then be passed into
        each call of .map() for you.

        Overwrite 'finish' with a static definition for a finish callback
    """
    shard_count = None
    job_name = None
    queue_name = 'default'
    output_writer_spec = None
    mapreduce_parameters = {}
    model = None
    map_args = []
    map_kwargs = {}

    def __init__(self, model=None, db=None):
        if model:
            self.model = model
            self.db = db or router.db_for_read(self.model)
        else:
            self.db = db or 'default'

        if not self.job_name:
            # No job name then we will just use the class
            self.job_name = self.get_class_path()

    def get_model_app_(self):
        app = self.model._meta.app_label
        name = self.model.__name__
        return '{app}.{name}'.format(
            app=app,
            name=name,
        )

    def get_class_path(self):
        return '{mod}.{cls}'.format(
            mod=self.__class__.__module__,
            cls=self.__class__.__name__,
        )

    @classmethod
    def get_relative_path(cls, func):
        return '{mod}.{cls}.{func}'.format(
            mod=cls.__module__,
            cls=cls.__name__,
            func=func.__name__,
        )

    @staticmethod
    def map(entity, *args, **kwargs):
        """
            Override this definition with a staticmethod map definition
        """
        raise NotImplementedError('You must supply a map function')

    @staticmethod
    def finish(**kwargs):
        """
            Override this with a static method for the finish callback
        """
        raise NotImplementedError('You must supply a finish function')

    @classmethod
    def run_map(cls, entity, *args, **kwargs):
        ret = cls.map(entity, *args, **kwargs)
        if hasattr(ret, "next"):
            return ret.next()
        return ret

    def start(self, *args, **kwargs):
        if 'map' not in self.__class__.__dict__:
            raise TypeError('No static map method defined on class {cls}'.format(self.__class__))

        if 'finish' in self.__class__.__dict__:
            finish = self.finish
        else:
            finish = None

        # We have to pass dotted paths to functions here because staticmethods don't have
        # any concept of self, or the class they are defined in.

        return map_queryset(
            self.model.objects.using(self.db).all(),
            ".".join([qualname(self.__class__), "run_map"]),
            finalize_func=".".join([qualname(self.__class__), "finish"]) if finish else None,
            _shards=self.shard_count,
            _output_writer=self.output_writer_spec,
            _output_writer_kwargs=None,
            _job_name=self.job_name,
            _queue_name=kwargs.pop('queue_name', self.queue_name),
            *args,
            **kwargs
        )
