from .DatePickerBaseInput import DatePickerBaseInput


class DatePickerInput(DatePickerBaseInput):
    picker_type = 'DATE'
    format = '%m/%d/%Y'
    format_key = 'DATE_INPUT_FORMATS'


class TimePickerInput(DatePickerBaseInput):
    picker_type = 'TIME'
    format = '%H:%M'
    format_key = 'TIME_INPUT_FORMATS'
    template_name = 'bootstrap_datepicker_plus/time-picker.html'


class DateTimePickerInput(DatePickerBaseInput):
    picker_type = 'DATETIME'
    format = '%m/%d/%Y %H:%M'
    format_key = 'DATETIME_INPUT_FORMATS'


class MonthPickerInput(DatePickerBaseInput):
    picker_type = 'MONTH'
    format = '%Y-%m-01'
    format_key = 'DATE_INPUT_FORMATS'


class YearPickerInput(DatePickerBaseInput):
    picker_type = 'YEAR'
    format = '%Y-01-01'
    format_key = 'DATE_INPUT_FORMATS'

    def _link_to(self, linked_picker):
        self.config['options']['format'] = self.config['options']['format'].replace(
            '-01-01', '-12-31')
