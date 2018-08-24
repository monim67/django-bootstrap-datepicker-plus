from django.test import SimpleTestCase

from bootstrap_datepicker_plus.DatePickerBaseInput import DatePickerBaseInput


class custom_input(DatePickerBaseInput):
    format = '%Y-%m-%d'


class TestOptionOverrides(SimpleTestCase):

    def test_format_as_parameter(self):
        dp_input = DatePickerBaseInput(format='%Y-%m-%d')
        self.assertEqual(dp_input.format, '%Y-%m-%d')

    def test_format_as_option(self):
        dp_input = DatePickerBaseInput(options={'format': 'YYYY-MM-DD'})
        self.assertEqual(dp_input.format, '%Y-%m-%d')

    def test_format_as_both(self):
        dp_input = DatePickerBaseInput(
            format='%m/%d/%Y', options={'format': 'YYYY-MM-DD'})
        self.assertEqual(dp_input.format, '%Y-%m-%d')

    def test_format_as_extended_class_property(self):
        dp_input = custom_input()
        self.assertEqual(dp_input.format, '%Y-%m-%d')

    def test_format_as_parameter_to_extended_class(self):
        dp_input = custom_input(format='%m/%d/%Y')
        self.assertEqual(dp_input.format, '%m/%d/%Y')

    def test_format_as_option_to_extended_class(self):
        dp_input = custom_input(options={'format': 'MM/DD/YYYY'})
        self.assertEqual(dp_input.format, '%m/%d/%Y')

    def test_format_as_both_to_extended_class(self):
        dp_input = custom_input(
            format='%m/%d/%Y', options={'format': 'YYYY-MM-DD'})
        self.assertEqual(dp_input.format, '%Y-%m-%d')
