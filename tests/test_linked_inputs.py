from django.test import SimpleTestCase

from bootstrap_datepicker_plus._base import BasePickerInput
from bootstrap_datepicker_plus import YearPickerInput


class TestLinkedInputs(SimpleTestCase):

    def test_raising_error_on_no_start_of_key(self):
        endpicker = BasePickerInput()
        self.assertRaises(KeyError, lambda: endpicker.end_of('undefined'))

    def test_format_copy(self):
        dp_input1 = BasePickerInput(
            format='%Y-%m-%d').start_of('format_copy')
        dp_input2 = BasePickerInput().end_of('format_copy')
        self.assertEqual(dp_input1.format, '%Y-%m-%d')
        self.assertEqual(dp_input2.format, '%Y-%m-%d')

    def test_format_copy_override(self):
        dp_input1 = BasePickerInput(
            format='%Y-%m-%d').start_of('format_copy_override')
        dp_input2 = BasePickerInput(
            format='%m/%d/%Y').end_of('format_copy_override')
        self.assertEqual(dp_input1.format, '%Y-%m-%d')
        self.assertEqual(dp_input2.format, '%m/%d/%Y')

    def test_year_picker_formats(self):
        yearpicker1 = YearPickerInput().start_of('tes1')
        yearpicker2 = YearPickerInput().end_of('tes1')
        self.assertEqual(yearpicker1.config['options']['format'], 'YYYY-01-01')
        self.assertEqual(yearpicker2.config['options']['format'], 'YYYY-12-31')
