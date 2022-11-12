import pytest

from bootstrap_datepicker_plus._base import BasePickerInput


def test_warning_when_format_parameter_is_used() -> None:
    with pytest.warns(FutureWarning):
        BasePickerInput(format="%Y-%m-%d")


def test_warning_when_start_of_is_used() -> None:
    widget_input = BasePickerInput()
    with pytest.warns(FutureWarning):
        widget_input.start_of("an event")


def test_warning_when_end_of_is_used() -> None:
    widget_input = BasePickerInput()
    with pytest.warns(FutureWarning):
        widget_input.end_of("an event")
