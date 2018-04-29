import unittest
from django.conf import settings
settings.configure()
from bootstrap_datepicker_plus import DatePickerInput


class TestDatePicker(unittest.TestCase):

    def setUp(self):
        pass

    def test_convert_datetime_format_py2js(self):
        self.assertEqual(DatePickerInput.convert_datetime_format_py2js(
            '%Y-%m-%d'), 'yyyy-mm-dd')
        self.assertEqual(DatePickerInput.convert_datetime_format_py2js(
            '%d/%m/%Y'), 'dd/mm/yyyy')

    def test_convert_datetime_format_js2py(self):
        self.assertEqual(DatePickerInput.convert_datetime_format_js2py(
            'yyyy-mm-dd'), '%Y-%m-%d')
        self.assertEqual(DatePickerInput.convert_datetime_format_js2py(
            'dd/mm/yyyy'), '%d/%m/%Y')

    def test_media(self):
        datepicker = DatePickerInput()
        for files in reversed(datepicker.Media.js):
            files
        self.assertTrue(True)

    def test__init__(self):
        datepicker = DatePickerInput()
        self.render_datepicker(datepicker)
        datepicker = DatePickerInput(format='%Y-%m-%d')
        self.render_datepicker(datepicker)
        datepicker = DatePickerInput(options={'format':'%m/%d/%Y'})
        self.render_datepicker(datepicker)
        self.assertTrue(True)
        self.assertRaises(ValueError, lambda:DatePickerInput(format='%Y-%d-%m'))

    def render_datepicker(self, datepicker):
        html = datepicker.render("input_name", None, {})
        self.assertTrue(len(html) > 0)
        html = datepicker.render("input_name", None, {})
        self.assertTrue(len(html) > 0)
        html = datepicker.render("input_name", '2018-04-12', {})
        self.assertTrue(len(html) > 0)


if __name__ == "__main__":
    unittest.main()
