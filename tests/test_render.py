from pytest_django.fixtures import SettingsWrapper

from bootstrap_datepicker_plus.widgets import DatePickerInput


class CustomWidgetInput(DatePickerInput):
    template_name = "myapp/custom-input.html"


def test_presence_of_input_in_html() -> None:
    widget_input = DatePickerInput()
    assert "<input" in widget_input.render("test", "test")


def test_presence_of_input_in_custom_template() -> None:
    widget_input = CustomWidgetInput()
    assert "myapp/custom-input.html" in widget_input.render("test", "test")


def test_presence_of_script_when_debug_true() -> None:
    widget_input = DatePickerInput()
    assert "</script>" in widget_input.render("test", "test", {"data-dbdp-debug": ""})


def test_absence_of_script_when_debug_false(settings: SettingsWrapper) -> None:
    widget_input = DatePickerInput()
    assert "</script>" not in widget_input.render("test", "test")


def test_media_rendering(settings: SettingsWrapper) -> None:
    widget_input = DatePickerInput()
    assert "</script>" in widget_input.media.render()
