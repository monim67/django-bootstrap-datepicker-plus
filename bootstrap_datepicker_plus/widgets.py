"""This module contains the widget classes."""

__all__ = (
    "DatePickerInput",
    "TimePickerInput",
    "DateTimePickerInput",
    "MonthPickerInput",
    "YearPickerInput",
)

from ._base import BasePickerInput


class DatePickerInput(BasePickerInput):
    """
    Widget to display a Date-Picker Calendar on a DateField property.

    Args:
        - attrs (dict): HTML attributes of rendered HTML input
        - format (string): Python DateTime format eg. "%Y-%m-%d"
        - options (dict): Options to customize the widget, see README
    """

    picker_type = "DATE"
    format = "%m/%d/%Y"
    format_key = "DATE_INPUT_FORMATS"


class TimePickerInput(BasePickerInput):
    """
    Widget to display a Time-Picker Calendar on a TimeField property.

    Args:
        - attrs (dict): HTML attributes of rendered HTML input
        - format (string): Python DateTime format eg. "%Y-%m-%d"
        - options (dict): Options to customize the widget, see README
    """

    picker_type = "TIME"
    format = "%H:%M"
    format_key = "TIME_INPUT_FORMATS"
    template_name = "bootstrap_datepicker_plus/time-picker.html"


class DateTimePickerInput(BasePickerInput):
    """
    Widget to display a DateTime-Picker Calendar on a DateTimeField property.

    Args:
        - attrs (dict): HTML attributes of rendered HTML input
        - format (string): Python DateTime format eg. "%Y-%m-%d"
        - options (dict): Options to customize the widget, see README
    """

    picker_type = "DATETIME"
    format = "%m/%d/%Y %H:%M"
    format_key = "DATETIME_INPUT_FORMATS"


class MonthPickerInput(BasePickerInput):
    """
    Widget to display a Month-Picker Calendar on a DateField property.

    Args:
        - attrs (dict): HTML attributes of rendered HTML input
        - format (string): Python DateTime format eg. "%Y-%m-%d"
        - options (dict): Options to customize the widget, see README
    """

    picker_type = "MONTH"
    format = "%Y-%m-01"
    format_key = "DATE_INPUT_FORMATS"


class YearPickerInput(BasePickerInput):
    """
    Widget to display a Year-Picker Calendar on a DateField property.

    Args:
        - attrs (dict): HTML attributes of rendered HTML input
        - format (string): Python DateTime format eg. "%Y-%m-%d"
        - options (dict): Options to customize the widget, see README
    """

    picker_type = "YEAR"
    format = "%Y-01-01"
    format_key = "DATE_INPUT_FORMATS"

    def _link_to(self, linked_picker):
        """Customize the options when linked with other date-time input"""
        yformat = self.config["options"]["format"].replace("-01-01", "-12-31")
        self.config["options"]["format"] = yformat
