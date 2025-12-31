"""Tests for configuration."""

import pytest
from pydantic import ValidationError

from bootstrap_datepicker_plus._config import WidgetConfig
from bootstrap_datepicker_plus.schemas import WidgetVariant


def test_widget_config_update_options():
    """Test options merging in WidgetConfig."""
    config = WidgetConfig(variant=WidgetVariant.date, backend_date_format="YYYY-MM-DD")
    config.update_options({"format": "DD/MM/YYYY"}, {"locale": "en"})
    assert config.options == {"format": "DD/MM/YYYY", "locale": "en"}


def test_widget_config_to_attr_value():
    """Test JSON serialization for attributes."""
    config = WidgetConfig(
        variant=WidgetVariant.date,
        backend_date_format="YYYY-MM-DD",
        options={"format": "YYYY-MM-DD"},
        range_from="start_date",
    )
    attr_value = config.to_attr_value()
    assert '"variant":"date"' in attr_value
    assert '"options":{"format":"YYYY-MM-DD"}' in attr_value
    assert '"range_from":"start_date"' in attr_value


def test_widget_config_validation():
    """Test pydantic validation."""
    # Valid
    WidgetConfig(variant=WidgetVariant.date, backend_date_format="YYYY-MM-DD")

    # Invalid variant
    with pytest.raises(ValidationError):
        WidgetConfig(
            variant="invalid",  # pyright: ignore[reportArgumentType]
            backend_date_format="YYYY-MM-DD",
        )
