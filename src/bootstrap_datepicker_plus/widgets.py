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

    _date_format = "%Y-%m-%d"
    backend_date_format = "YYYY-MM-DD"
    _preferred_options = {
        "format": "ll",
    }


class TimePickerInput(BasePickerInput):
    """Widget to display a Time-Picker Calendar on a TimeField."""

    variant = WidgetVariant.time
    _date_format = "%H:%M:%S"
    backend_date_format = "HH:mm:ss"
    _preferred_options = {
        "format": "LTS",
        "tooltips": {"today": "Go to now"},
    }


class DateTimePickerInput(BasePickerInput):
    """Widget to display a DateTime-Picker Calendar on a DateTimeField."""

    variant = WidgetVariant.datetime
    _date_format = "%Y-%m-%d %H:%M:%S"
    backend_date_format = "YYYY-MM-DD HH:mm:ss"
    _preferred_options = {
        "format": "ll LTS",
        "tooltips": {"today": "Go to now"},
    }


class MonthPickerInput(BasePickerInput):
    """Widget to display a Month-Picker Calendar on a DateField."""

    variant = WidgetVariant.month
    _date_format = "%Y-%m-%d"
    backend_date_format = "YYYY-MM-01"
    _preferred_options = {
        "format": "MMMM, Y",
    }


class YearPickerInput(BasePickerInput):
    """Widget to display a Year-Picker Calendar on a DateField."""

    variant = WidgetVariant.year
    _date_format = "%Y-%m-%d"
    backend_date_format = "YYYY-01-01"
    _preferred_options = {
        "format": "Y",
    }
