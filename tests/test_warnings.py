import pytest

from bootstrap_datepicker_plus._base import BasePickerInput


def test_warning_when_format_parameter_is_used() -> None:
    with pytest.warns(FutureWarning):
        BasePickerInput(format="%Y-%m-%d")
