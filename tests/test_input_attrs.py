from pytest_django.fixtures import SettingsWrapper

from bootstrap_datepicker_plus._base import BasePickerInput


def test_input_config_passed_as_input_attr() -> None:
    widget_input = BasePickerInput()
    assert "data-dbdp-config" in widget_input.build_attrs({})


def test_presence_of_debug_attr_when_debug_true(settings: SettingsWrapper) -> None:
    settings.DEBUG = True
    widget_input = BasePickerInput()
    assert "data-dbdp-debug" in widget_input.build_attrs({})


def test_absence_of_debug_attr_when_debug_false(settings: SettingsWrapper) -> None:
    settings.DEBUG = False
    widget_input = BasePickerInput()
    assert "data-dbdp-debug" not in widget_input.build_attrs({})


def test_absence_of_debug_attr_when_debug_overrides(settings: SettingsWrapper) -> None:
    settings.DEBUG = True
    settings.BOOTSTRAP_DATEPICKER_PLUS = {"debug": False}
    widget_input = BasePickerInput()
    assert "data-dbdp-debug" not in widget_input.build_attrs({})


def test_autocomplete_off_by_default() -> None:
    widget_input = BasePickerInput()
    assert widget_input.build_attrs({})["autocomplete"] == "off"


def test_autocomplete_can_be_overridden_via_base_attrs() -> None:
    widget_input = BasePickerInput()
    assert widget_input.build_attrs({"autocomplete": "on"})["autocomplete"] == "on"


def test_autocomplete_can_be_overridden_via_settings(
    settings: SettingsWrapper,
) -> None:
    settings.BOOTSTRAP_DATEPICKER_PLUS = {"attrs": {"autocomplete": "on"}}
    widget_input = BasePickerInput()
    assert widget_input.build_attrs({})["autocomplete"] == "on"
