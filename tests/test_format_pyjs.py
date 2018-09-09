from django.test import SimpleTestCase

from bootstrap_datepicker_plus._base import BasePickerInput


class TestDateFormatConversion(SimpleTestCase):

    def test_format_py2js(self):
        self.assertEqual(BasePickerInput.format_py2js(
            '%Y-%m-%d'), 'YYYY-MM-DD')
        self.assertEqual(BasePickerInput.format_py2js(
            '%d/%m/%Y'), 'DD/MM/YYYY')

    def test_format_js2py(self):
        self.assertEqual(BasePickerInput.format_js2py(
            'YYYY-MM-DD'), '%Y-%m-%d')
        self.assertEqual(BasePickerInput.format_js2py(
            'DD/MM/YYYY'), '%d/%m/%Y')
