from django.test import SimpleTestCase

from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from json import dumps as json_dumps
import re


class CustomDatePickerInput(DatePickerInput):
    template_name = 'demo_app/custom_input/date-picker.html'


class CustomTimePickerInput(TimePickerInput):
    template_name = 'demo_app/custom_input/time-picker.html'


class TestContextRender(SimpleTestCase):

    def test_get_context(self):
        dp_input = DatePickerInput()
        context = dp_input.get_context('input_name', '2018-04-12', {})
        self.assertEqual(context['widget']['name'], 'input_name')
        self.assertEqual(context['widget']['value'], '2018-04-12')
        self.assertTrue(context['widget']['attrs']
                        ['dp_config'] == json_dumps(dp_input.config))

    def test_date_input_snapshot(self):
        dp_input = DatePickerInput()
        html = dp_input.render('input_name', '2018-04-12', {})
        snapshot = open('tests/snapshots/date-input.html').read()
        html = re.sub('dp_\\d+', '', html)
        snapshot = re.sub('dp_\\d+', '', snapshot)
        self.assertEqual(html, snapshot)

    def test_time_input_snapshot(self):
        dp_input = TimePickerInput()
        html = dp_input.render('input_name', '12:30', {})
        snapshot = open('tests/snapshots/time-input.html').read()
        html = re.sub('dp_\\d+', '', html)
        snapshot = re.sub('dp_\\d+', '', snapshot)
        self.assertEqual(html, snapshot)

    def test_custom_date_input_snapshot(self):
        dp_input = CustomDatePickerInput()
        html = dp_input.render('input_name', '2018-04-12', {})
        snapshot = open('tests/snapshots/date-input-custom.html').read()
        html = re.sub('dp_\\d+', '', html)
        snapshot = re.sub('dp_\\d+', '', snapshot)
        self.assertEqual(html, snapshot)

    def test_custom_time_input_snapshot(self):
        dp_input = CustomTimePickerInput()
        html = dp_input.render('input_name', '12:30', {})
        snapshot = open('tests/snapshots/time-input-custom.html').read()
        html = re.sub('dp_\\d+', '', html)
        snapshot = re.sub('dp_\\d+', '', snapshot)
        self.assertEqual(html, snapshot)

