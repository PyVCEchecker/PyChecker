import logging

from .fields import IntegerField, EnumField, EnumListField, DateOrDateTimeField, DateTimeField, EWSElementField, \
    IdElementField, MONTHS, WEEK_NUMBERS, WEEKDAYS
from .properties import EWSElement, IdChangeKeyMixIn, ItemId, EWSMeta

log = logging.getLogger(__name__)


def _month_to_str(month):
    return MONTHS[month-1] if isinstance(month, int) else month


def _weekday_to_str(weekday):
    return WEEKDAYS[weekday - 1] if isinstance(weekday, int) else weekday


def _week_number_to_str(week_number):
    return WEEK_NUMBERS[week_number - 1] if isinstance(week_number, int) else week_number


class Pattern(EWSElement, metaclass=EWSMeta):
    """Base class for all classes implementing recurring pattern elements."""


class Regeneration(Pattern, metaclass=EWSMeta):
    """Base class for all classes implementing recurring regeneration elements."""


class AbsoluteYearlyPattern(Pattern):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/absoluteyearlyrecurrence
    """

    ELEMENT_NAME = 'AbsoluteYearlyRecurrence'

    # The day of month of an occurrence, in range 1 -> 31. If a particular month has less days than the day_of_month
    # value, the last day in the month is assumed
    day_of_month = IntegerField(field_uri='DayOfMonth', min=1, max=31, is_required=True)
    # The month of the year, from 1 - 12
    month = EnumField(field_uri='Month', enum=MONTHS, is_required=True)

    def __str__(self):
        return 'Occurs on day %s of %s' % (self.day_of_month, _month_to_str(self.month))


class RelativeYearlyPattern(Pattern):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/relativeyearlyrecurrence
    """

    ELEMENT_NAME = 'RelativeYearlyRecurrence'

    # The weekday of the occurrence, as a valid ISO 8601 weekday number in range 1 -> 7 (1 being Monday).
    # Alternatively, the weekday can be one of the DAY (or 8), WEEK_DAY (or 9) or WEEKEND_DAY (or 10) consts which
    # is interpreted as the first day, weekday, or weekend day in the month, respectively.
    weekday = EnumField(field_uri='DaysOfWeek', enum=WEEKDAYS, is_required=True)
    # Week number of the month, in range 1 -> 5. If 5 is specified, this assumes the last week of the month for
    # months that have only 4 weeks
    week_number = EnumField(field_uri='DayOfWeekIndex', enum=WEEK_NUMBERS, is_required=True)
    # The month of the year, from 1 - 12
    month = EnumField(field_uri='Month', enum=MONTHS, is_required=True)

    def __str__(self):
        return 'Occurs on weekday %s in the %s week of %s' % (
            _weekday_to_str(self.weekday),
            _week_number_to_str(self.week_number),
            _month_to_str(self.month)
        )


class AbsoluteMonthlyPattern(Pattern):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/absolutemonthlyrecurrence
    """

    ELEMENT_NAME = 'AbsoluteMonthlyRecurrence'

    # Interval, in months, in range 1 -> 99
    interval = IntegerField(field_uri='Interval', min=1, max=99, is_required=True)
    # The day of month of an occurrence, in range 1 -> 31. If a particular month has less days than the day_of_month
    # value, the last day in the month is assumed
    day_of_month = IntegerField(field_uri='DayOfMonth', min=1, max=31, is_required=True)

    def __str__(self):
        return 'Occurs on day %s of every %s month(s)' % (self.day_of_month, self.interval)


class RelativeMonthlyPattern(Pattern):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/relativemonthlyrecurrence
    """

    ELEMENT_NAME = 'RelativeMonthlyRecurrence'

    # Interval, in months, in range 1 -> 99
    interval = IntegerField(field_uri='Interval', min=1, max=99, is_required=True)
    # The weekday of the occurrence, as a valid ISO 8601 weekday number in range 1 -> 7 (1 being Monday).
    # Alternatively, the weekday can be one of the DAY (or 8), WEEK_DAY (or 9) or WEEKEND_DAY (or 10) consts which
    # is interpreted as the first day, weekday, or weekend day in the month, respectively.
    weekday = EnumField(field_uri='DaysOfWeek', enum=WEEKDAYS, is_required=True)
    # Week number of the month, in range 1 -> 5. If 5 is specified, this assumes the last week of the month for
    # months that have only 4 weeks.
    week_number = EnumField(field_uri='DayOfWeekIndex', enum=WEEK_NUMBERS, is_required=True)

    def __str__(self):
        return 'Occurs on weekday %s in the %s week of every %s month(s)' % (
            _weekday_to_str(self.weekday),
            _week_number_to_str(self.week_number),
            self.interval
        )


class WeeklyPattern(Pattern):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/weeklyrecurrence"""

    ELEMENT_NAME = 'WeeklyRecurrence'

    # Interval, in weeks, in range 1 -> 99
    interval = IntegerField(field_uri='Interval', min=1, max=99, is_required=True)
    # List of valid ISO 8601 weekdays, as list of numbers in range 1 -> 7 (1 being Monday)
    weekdays = EnumListField(field_uri='DaysOfWeek', enum=WEEKDAYS, is_required=True)
    # The first day of the week. Defaults to Monday
    first_day_of_week = EnumField(field_uri='FirstDayOfWeek', enum=WEEKDAYS, default=1, is_required=True)

    def __str__(self):
        if isinstance(self.weekdays, str):
            weekdays = [self.weekdays]
        elif isinstance(self.weekdays, int):
            weekdays = [_weekday_to_str(self.weekdays)]
        else:
            weekdays = [_weekday_to_str(i) for i in self.weekdays]
        return 'Occurs on weekdays %s of every %s week(s) where the first day of the week is %s' % (
            ', '.join(weekdays), self.interval, _weekday_to_str(self.first_day_of_week)
        )


class DailyPattern(Pattern):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/dailyrecurrence"""

    ELEMENT_NAME = 'DailyRecurrence'

    # Interval, in days, in range 1 -> 999
    interval = IntegerField(field_uri='Interval', min=1, max=999, is_required=True)

    def __str__(self):
        return 'Occurs every %s day(s)' % self.interval


class YearlyRegeneration(Regeneration):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/yearlyregeneration"""

    ELEMENT_NAME = 'YearlyRegeneration'

    # Interval, in years
    interval = IntegerField(field_uri='Interval', min=1, is_required=True)

    def __str__(self):
        return 'Regenerates every %s year(s)' % self.interval


class MonthlyRegeneration(Regeneration):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/monthlyregeneration"""

    ELEMENT_NAME = 'MonthlyRegeneration'

    # Interval, in months
    interval = IntegerField(field_uri='Interval', min=1, is_required=True)

    def __str__(self):
        return 'Regenerates every %s month(s)' % self.interval


class WeeklyRegeneration(Regeneration):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/weeklyregeneration"""

    ELEMENT_NAME = 'WeeklyRegeneration'

    # Interval, in weeks
    interval = IntegerField(field_uri='Interval', min=1, is_required=True)

    def __str__(self):
        return 'Regenerates every %s week(s)' % self.interval


class DailyRegeneration(Regeneration):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/dailyregeneration"""

    ELEMENT_NAME = 'DailyRegeneration'

    # Interval, in days
    interval = IntegerField(field_uri='Interval', min=1, is_required=True)

    def __str__(self):
        return 'Regenerates every %s day(s)' % self.interval


class Boundary(EWSElement, metaclass=EWSMeta):
    """Base class for all classes implementing recurring boundary elements."""


class NoEndPattern(Boundary):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/noendrecurrence"""

    ELEMENT_NAME = 'NoEndRecurrence'

    # Start date, as EWSDate or EWSDateTime
    start = DateOrDateTimeField(field_uri='StartDate', is_required=True)

    def __str__(self):
        return 'Starts on %s' % self.start


class EndDatePattern(Boundary):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/enddaterecurrence"""

    ELEMENT_NAME = 'EndDateRecurrence'

    # Start date, as EWSDate or EWSDateTime
    start = DateOrDateTimeField(field_uri='StartDate', is_required=True)
    # End date, as EWSDate
    end = DateOrDateTimeField(field_uri='EndDate', is_required=True)

    def __str__(self):
        return 'Starts on %s, ends on %s' % (self.start, self.end)


class NumberedPattern(Boundary):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/numberedrecurrence"""

    ELEMENT_NAME = 'NumberedRecurrence'

    # Start date, as EWSDate or EWSDateTime
    start = DateOrDateTimeField(field_uri='StartDate', is_required=True)
    # The number of occurrences in this pattern, in range 1 -> 999
    number = IntegerField(field_uri='NumberOfOccurrences', min=1, max=999, is_required=True)

    def __str__(self):
        return 'Starts on %s and occurs %s times' % (self.start, self.number)


class Occurrence(IdChangeKeyMixIn):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/occurrence"""

    ELEMENT_NAME = 'Occurrence'
    ID_ELEMENT_CLS = ItemId

    _id = IdElementField(field_uri='ItemId', value_cls=ID_ELEMENT_CLS)
    # The modified start time of the item, as EWSDateTime
    start = DateTimeField(field_uri='Start')
    # The modified end time of the item, as EWSDateTime
    end = DateTimeField(field_uri='End')
    # The original start time of the item, as EWSDateTime
    original_start = DateTimeField(field_uri='OriginalStart')


# Container elements:
# 'ModifiedOccurrences'
# 'DeletedOccurrences'


class FirstOccurrence(Occurrence):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/firstoccurrence"""

    ELEMENT_NAME = 'FirstOccurrence'


class LastOccurrence(Occurrence):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/lastoccurrence"""

    ELEMENT_NAME = 'LastOccurrence'


class DeletedOccurrence(EWSElement):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/deletedoccurrence"""

    ELEMENT_NAME = 'DeletedOccurrence'

    # The modified start time of the item, as EWSDateTime
    start = DateTimeField(field_uri='Start')


PATTERN_CLASSES = AbsoluteYearlyPattern, RelativeYearlyPattern, AbsoluteMonthlyPattern, RelativeMonthlyPattern, \
                   WeeklyPattern, DailyPattern
REGENERATION_CLASSES = YearlyRegeneration, MonthlyRegeneration, WeeklyRegeneration, DailyRegeneration
BOUNDARY_CLASSES = NoEndPattern, EndDatePattern, NumberedPattern


class Recurrence(EWSElement):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/recurrence-recurrencetype
    """

    ELEMENT_NAME = 'Recurrence'
    PATTERN_CLASSES = PATTERN_CLASSES

    pattern = EWSElementField(value_cls=Pattern)
    boundary = EWSElementField(value_cls=Boundary)

    def __init__(self, **kwargs):
        # Allow specifying a start, end and/or number as a shortcut to creating a boundary
        start = kwargs.pop('start', None)
        end = kwargs.pop('end', None)
        number = kwargs.pop('number', None)
        if any([start, end, number]):
            if 'boundary' in kwargs:
                raise ValueError("'boundary' is not allowed in combination with 'start', 'end' or 'number'")
            if start and not end and not number:
                kwargs['boundary'] = NoEndPattern(start=start)
            elif start and end and not number:
                kwargs['boundary'] = EndDatePattern(start=start, end=end)
            elif start and number and not end:
                kwargs['boundary'] = NumberedPattern(start=start, number=number)
            else:
                raise ValueError("Unsupported 'start', 'end', 'number' combination")
        super().__init__(**kwargs)

    @classmethod
    def from_xml(cls, elem, account):
        for pattern_cls in cls.PATTERN_CLASSES:
            pattern_elem = elem.find(pattern_cls.response_tag())
            if pattern_elem is None:
                continue
            pattern = pattern_cls.from_xml(elem=pattern_elem, account=account)
            break
        else:
            pattern = None
        for boundary_cls in BOUNDARY_CLASSES:
            boundary_elem = elem.find(boundary_cls.response_tag())
            if boundary_elem is None:
                continue
            boundary = boundary_cls.from_xml(elem=boundary_elem, account=account)
            break
        else:
            boundary = None
        return cls(pattern=pattern, boundary=boundary)

    def __str__(self):
        return 'Pattern: %s, Boundary: %s' % (self.pattern, self.boundary)


class TaskRecurrence(Recurrence):
    """MSDN:
    https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/recurrence-taskrecurrencetype
    """

    PATTERN_CLASSES = PATTERN_CLASSES + REGENERATION_CLASSES
