from djangae.forms.fields import TrueOrNullFormField
from django.utils.translation import ugettext_lazy as _

from .files import *
from .iterable import *
from .related import *
from .computed import *
from .json import *
from .counting import *
from .language import ComputedCollationField
from .charfields import CharField, CharOrNoneField


class TrueOrNullField(models.NullBooleanField):
    """A Field only storing `Null` or `True` values.

    Why? This allows unique_together constraints on fields of this type
    ensuring that only a single instance has the `True` value.

    It mimics the NullBooleanField field in it's behaviour, while it will
    raise an exception when explicitly validated, assigning something
    unexpected (like a string) and saving, will silently convert that
    value to either True or None.
    """
    default_error_messages = {
        'invalid': _("'%s' value must be either True or None."),
    }
    description = _("Boolean (Either True or None)")

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def to_python(self, value):
        if value in (None, 'None', False):
            return None
        if value in (True, 't', 'True', '1'):
            return True
        msg = self.error_messages['invalid'] % str(value)
        raise ValidationError(msg)

    def get_prep_value(self, value):
        """Only ever save None's or True's in the db. """
        if value in (None, False, '', 0):
            return None
        return True

    def formfield(self, **kwargs):
        defaults = {
            'form_class': TrueOrNullFormField
        }
        defaults.update(kwargs)
        return super(TrueOrNullField, self).formfield(**defaults)

