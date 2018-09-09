from bootstrap_datepicker_plus._base import BasePickerInput

__all__ = (
    'DatePickerInput',
    'TimePickerInput',
    'DateTimePickerInput',
    'MonthPickerInput',
    'YearPickerInput',
)


class DatePickerInput(BasePickerInput):
    picker_type = 'DATE'
    format = '%m/%d/%Y'
    format_key = 'DATE_INPUT_FORMATS'


class TimePickerInput(BasePickerInput):
    picker_type = 'TIME'
    format = '%H:%M'
    format_key = 'TIME_INPUT_FORMATS'
    template_name = 'bootstrap_datepicker_plus/time-picker.html'


class DateTimePickerInput(BasePickerInput):
    picker_type = 'DATETIME'
    format = '%m/%d/%Y %H:%M'
    format_key = 'DATETIME_INPUT_FORMATS'


class MonthPickerInput(BasePickerInput):
    picker_type = 'MONTH'
    format = '%Y-%m-01'
    format_key = 'DATE_INPUT_FORMATS'


class YearPickerInput(BasePickerInput):
    picker_type = 'YEAR'
    format = '%Y-01-01'
    format_key = 'DATE_INPUT_FORMATS'

    def _link_to(self, linked_picker):
        yformat = self.config['options']['format'].replace('-01-01', '-12-31')
        self.config['options']['format'] = yformat
