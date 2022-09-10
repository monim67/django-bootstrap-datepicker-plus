from json import dumps as json_dumps

from django.test import SimpleTestCase

from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput


class CustomDatePickerInput(DatePickerInput):
    template_name = "myapp/custom_input/date-picker.html"


class CustomTimePickerInput(TimePickerInput):
    template_name = "myapp/custom_input/time-picker.html"


class TestContextRender(SimpleTestCase):
    def test_get_context(self):
        dp_input = DatePickerInput()
        context = dp_input.get_context("input_name", "2018-04-12", {})
        self.assertEqual(context["widget"]["name"], "input_name")
        self.assertEqual(context["widget"]["value"], "2018-04-12")
        self.assertTrue(
            context["widget"]["attrs"]["data-dp-config"] == json_dumps(dp_input.config)
        )

    def test_date_input_snapshot(self):
        dp_input = DatePickerInput()
        html = dp_input.render("input_name", "2018-04-12", {})
        self.assertGreater(len(html), 0)

    def test_time_input_snapshot(self):
        dp_input = TimePickerInput()
        html = dp_input.render("input_name", "12:30", {})
        self.assertGreater(len(html), 0)

    def test_custom_date_input_snapshot(self):
        dp_input = CustomDatePickerInput()
        html = dp_input.render("input_name", "2018-04-12", {})
        self.assertGreater(len(html), 0)

    def test_custom_time_input_snapshot(self):
        dp_input = CustomTimePickerInput()
        html = dp_input.render("input_name", "12:30", {})
        self.assertGreater(len(html), 0)
