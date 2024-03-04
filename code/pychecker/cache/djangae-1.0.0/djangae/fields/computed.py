from django.db import models


class ComputedFieldMixin(object):
    def __init__(self, func, *args, **kwargs):
        self.computer = func

        kwargs["editable"] = False

        super(ComputedFieldMixin, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = self.get_computed_value(model_instance)
        setattr(model_instance, self.attname, value)
        return value

    def deconstruct(self):
        name, path, args, kwargs = super(ComputedFieldMixin, self).deconstruct()
        args = [self.computer] + args
        del kwargs["editable"]
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return self.to_python(value)

    def get_computed_value(self, model_instance):
        # self.computer is either a function or a string containing the name of a method
        if callable(self.computer):
            return self.computer(model_instance)
        else:
            computer = getattr(model_instance, self.computer)
            return computer()


class ComputedCharField(ComputedFieldMixin, models.CharField):
    pass


class ComputedIntegerField(ComputedFieldMixin, models.IntegerField):
    pass


class ComputedTextField(ComputedFieldMixin, models.TextField):
    pass


class ComputedPositiveIntegerField(ComputedFieldMixin, models.PositiveIntegerField):
    pass


class ComputedBooleanField(ComputedFieldMixin, models.BooleanField):
    pass


class ComputedNullBooleanField(ComputedFieldMixin, models.NullBooleanField):
    pass
