"""Fixtures for tests."""

from typing import Iterable

import pytest
from pytest_django.fixtures import SettingsWrapper

from bootstrap_datepicker_plus.settings import get_widget_settings


@pytest.fixture
def settings(settings: SettingsWrapper) -> Iterable[SettingsWrapper]:
    """Override pytest-django settings to clear get_widget_settings cache."""
    get_widget_settings.cache_clear()
    yield settings
    get_widget_settings.cache_clear()
