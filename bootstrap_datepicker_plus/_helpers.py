def get_base_input(test=False):
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
    _i = 0
    items = dict()

    @classmethod
    def generate_id(cls):
        cls._i += 1
        return 'dp_%s' % cls._i
