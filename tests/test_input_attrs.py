from pytest_django.fixtures import Settings

from bootstrap_datepicker_plus._base import BasePickerInput


def test_input_config_passed_as_input_attr() -> None:
    widget_input = BasePickerInput()
    assert "data-dbdp-config" in widget_input.build_attrs({})


def test_presence_of_debug_attr_when_debug_true(settings: Settings) -> None:
    settings.DEBUG = True
    widget_input = BasePickerInput()
    assert "data-dbdp-debug" in widget_input.build_attrs({})


def test_absence_of_debug_attr_when_debug_false(settings: Settings) -> None:
    settings.DEBUG = False
    widget_input = BasePickerInput()
    assert "data-dbdp-debug" not in widget_input.build_attrs({})


def test_absence_of_debug_attr_when_debug_overrides(settings: Settings) -> None:
    settings.DEBUG = True
    settings.BOOTSTRAP_DATEPICKER_PLUS = {"debug": False}
    widget_input = BasePickerInput()
    assert "data-dbdp-debug" not in widget_input.build_attrs({})
