"""Contains input widget classes."""

from bootstrap_datepicker_plus.schemas import WidgetVariant

from ._base import BasePickerInput

__all__ = (
    "DatePickerInput",
    "TimePickerInput",
    "DateTimePickerInput",
    "MonthPickerInput",
    "YearPickerInput",
)


class DatePickerInput(BasePickerInput):
    """Widget to display a Date-Picker Calendar on a DateField."""


class TimePickerInput(BasePickerInput):
    """Widget to display a Time-Picker Calendar on a TimeField."""

    variant = WidgetVariant.time
    backend_date_format = "HH:mm:ss"
    format_key = "TIME_INPUT_FORMATS"


class DateTimePickerInput(BasePickerInput):
    """Widget to display a DateTime-Picker Calendar on a DateTimeField."""

    variant = WidgetVariant.datetime
    backend_date_format = "YYYY-MM-DD HH:mm:ss"
    format_key = "DATETIME_INPUT_FORMATS"


class MonthPickerInput(BasePickerInput):
    """Widget to display a Month-Picker Calendar on a DateField."""

    variant = WidgetVariant.month
    backend_date_format = "YYYY-MM-01"
    format_key = "DATE_INPUT_FORMATS"


class YearPickerInput(BasePickerInput):
    """Widget to display a Year-Picker Calendar on a DateField."""

    variant = WidgetVariant.year
    backend_date_format = "YYYY-01-01"
    format_key = "DATE_INPUT_FORMATS"
