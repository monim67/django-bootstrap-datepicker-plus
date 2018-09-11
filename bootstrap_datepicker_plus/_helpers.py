"""Contains the helper classes and methods used throughout the project."""


def get_base_input(test=False):
    """
    Return DateTimeBaseInput class from django.forms.widgets module

    Return _compatibility.DateTimeBaseInput class for older django versions.
    """
    from django.forms.widgets import DateTimeBaseInput
    if 'get_context' in dir(DateTimeBaseInput) and not test:
        # django version 1.11 and above
        base_input = DateTimeBaseInput
    else:
        # django version below 1.11
        from bootstrap_datepicker_plus._compatibility import (
            CompatibleDateTimeBaseInput
        )
        base_input = CompatibleDateTimeBaseInput
    return base_input


class DatePickerDictionary:
    """Keeps track of all date-picker input classes."""

    _i = 0
    items = dict()

    @classmethod
    def generate_id(cls):
        """Return a unique ID for each date-picker input class."""
        cls._i += 1
        return 'dp_%s' % cls._i
