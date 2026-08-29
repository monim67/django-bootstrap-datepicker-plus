"""Tests for locale inference from Django language code."""

import json

import pytest
from django.utils.translation import activate, deactivate
from pytest_django.fixtures import Settings

from bootstrap_datepicker_plus._base import BasePickerInput
from bootstrap_datepicker_plus.constants import INFER_FROM_LANGUAGE_CODE


@pytest.fixture(autouse=True)
def reset_language():
    yield
    deactivate()


def _get_config(widget: BasePickerInput) -> dict:
    return json.loads(widget.build_attrs({})["data-dbdp-config"])


def test_infer_sentinel_resolves_active_language(settings: Settings) -> None:
    activate("nl")
    widget = BasePickerInput(options={"locale": INFER_FROM_LANGUAGE_CODE})
    assert _get_config(widget)["options"]["locale"] == "nl"


def test_infer_sentinel_applies_locale_override(settings: Settings) -> None:
    settings.BOOTSTRAP_DATEPICKER_PLUS = {
        "locale_infer_overrides": {"zh-hans": "zh-cn"}
    }
    activate("zh-hans")
    widget = BasePickerInput(options={"locale": INFER_FROM_LANGUAGE_CODE})
    assert _get_config(widget)["options"]["locale"] == "zh-cn"


def test_infer_sentinel_passthrough_when_no_override(settings: Settings) -> None:
    activate("de")
    widget = BasePickerInput(options={"locale": INFER_FROM_LANGUAGE_CODE})
    assert _get_config(widget)["options"]["locale"] == "de"


def test_explicit_locale_not_overridden_by_sentinel(settings: Settings) -> None:
    activate("nl")
    widget = BasePickerInput(options={"locale": "de"})
    assert _get_config(widget)["options"]["locale"] == "de"


def test_no_sentinel_no_language_set(settings: Settings) -> None:
    settings.BOOTSTRAP_DATEPICKER_PLUS = {}
    widget = BasePickerInput()
    config = _get_config(widget)
    assert "locale" not in config.get("options", {})
