from django.test import SimpleTestCase

from bootstrap_datepicker_plus.DateTimeBaseInputEx import BaseRenderer
from bootstrap_datepicker_plus.DatePickerDictionary import DatePickerDictionary

from json import dumps as json_dumps
import re


class TestCompatibilityPatch(SimpleTestCase):

    def setUp(self):
        self.DatePickerInputEx = DatePickerDictionary.get_base_input(True)
        self.dp_input = self.DatePickerInputEx()

    def test_raise_on_get_template(self):
        self.assertRaises(NotImplementedError,
                          lambda: BaseRenderer().get_template('test'))

    def test_format_value_method(self):
        self.assertEqual(self.dp_input.format_value(''), None)

    def test_get_context(self):
        context = self.dp_input.get_context('input_name', '2018-04-12', {})
        self.assertEqual(context['widget']['name'], 'input_name')
        self.assertEqual(context['widget']['value'], '2018-04-12')

    def test_compatible_input_snapshot(self):
        html = self.dp_input.render('input_name', '2018-04-12', {})
        snapshot = open('tests/snapshots/compatible-input.html').read()
        self.assertEqual(html, snapshot)
