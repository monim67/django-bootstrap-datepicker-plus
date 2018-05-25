import unittest

import django
from django.conf import settings
settings.configure()
django.setup()

from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from bootstrap_datepicker_plus.DatePickerBaseInput import DatePickerDictionary


class TestDatePicker(unittest.TestCase):

    def setUp(self):
        pass

    def test_format_py2js(self):
        self.assertEqual(DatePickerInput.format_py2js(
            '%Y-%m-%d'), 'YYYY-MM-DD')
        self.assertEqual(DatePickerInput.format_py2js(
            '%d/%m/%Y'), 'DD/MM/YYYY')

    def test_format_js2py(self):
        self.assertEqual(DatePickerInput.format_js2py(
            'YYYY-MM-DD'), '%Y-%m-%d')
        self.assertEqual(DatePickerInput.format_js2py(
            'DD/MM/YYYY'), '%d/%m/%Y')

    def test_year(self):
        yearpicker1 = YearPickerInput().start_of('tes1')
        yearpicker2 = YearPickerInput().end_of('tes1')
        self.assertEqual(yearpicker1.config['options']['format'], 'YYYY-01-01')
        self.assertEqual(yearpicker2.config['options']['format'], 'YYYY-12-31')

    def test_datepicker(self):
        startpicker = DatePickerInput().start_of('test')
        endpicker = DatePickerInput(
            options={'format': "YYYY-MM-DD"}).end_of('test')
        self.assertRaises(KeyError, lambda: endpicker.end_of('undefined'))
        context = startpicker.get_context("input_name", '2018-04-12', {})
        self.assertTrue(len(context['widget']['attrs']['dp_config']) > 0)

    def test_backcompatibility(self):
        DatePickerInputEx = DatePickerDictionary.get_base_input(True)
        dummypicker = DatePickerInputEx()
        self.assertEqual(dummypicker.format_value(''), None)
        # context = dummypicker.get_context("input_name", '2018-04-12', {})
        # self.assertEqual(context['widget']['attrs']['name'], "input_name")
        html = dummypicker.render("input_name", '2018-04-12', {})
        self.assertTrue(len(html) > 0)


if __name__ == "__main__":
    unittest.main()
