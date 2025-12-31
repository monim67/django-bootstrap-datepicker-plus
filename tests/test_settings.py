"""Tests for settings."""

from pydantic.fields import FieldInfo

from bootstrap_datepicker_plus.schemas import WidgetVariant
from bootstrap_datepicker_plus.settings import (
    DjangoSettingsSource,
    WidgetSettings,
    get_widget_settings,
)


def test_widget_settings_defaults():
    """Test default settings."""
    settings = WidgetSettings()
    assert settings.template_name is None
    assert isinstance(settings.options, dict)  # Options loaded from Django settings
    assert settings.addon_icon_classes[WidgetVariant.date] == "bi-calendar"


def test_get_widget_settings_caching():
    """Test settings caching."""
    settings1 = get_widget_settings()
    settings2 = get_widget_settings()
    assert settings1 is settings2


def test_widget_settings_custom_options():
    """Test custom options in settings."""
    settings = WidgetSettings(
        options={"locale": "en"},
        variant_options={WidgetVariant.time: {"format": "HH:mm"}},
    )
    assert settings.options["locale"] == "en"
    assert settings.variant_options[WidgetVariant.time]["format"] == "HH:mm"


def test_django_settings_source_get_field_value(settings):
    """Test DjangoSettingsSource get_field_value method."""
    source = DjangoSettingsSource(WidgetSettings)

    # Test getting a field value when BOOTSTRAP_DATEPICKER_PLUS exists
    settings.BOOTSTRAP_DATEPICKER_PLUS = {
        "debug": False,
        "template_name": "custom.html",
    }

    value, field_name, flag = source.get_field_value(FieldInfo(), "debug")
    assert value is False
    assert field_name == "debug"
    assert flag is False

    value, field_name, flag = source.get_field_value(FieldInfo(), "template_name")
    assert value == "custom.html"
    assert field_name == "template_name"
    assert flag is False

    # Test getting non-existent field
    value, field_name, flag = source.get_field_value(FieldInfo(), "non_existent")
    assert value is None
    assert field_name == "non_existent"
    assert flag is False


def test_django_settings_source_get_field_value_no_config(settings):
    """Test DjangoSettingsSource get_field_value when no BOOTSTRAP_DATEPICKER_PLUS config exists."""
    source = DjangoSettingsSource(WidgetSettings)

    # Remove BOOTSTRAP_DATEPICKER_PLUS setting if it exists
    if hasattr(settings, "BOOTSTRAP_DATEPICKER_PLUS"):
        del settings.BOOTSTRAP_DATEPICKER_PLUS

    value, field_name, flag = source.get_field_value(FieldInfo(), "debug")
    assert value is None
    assert field_name == "debug"
    assert flag is False


def test_django_settings_source_prepare_field_value():
    """Test DjangoSettingsSource prepare_field_value method."""
    source = DjangoSettingsSource(WidgetSettings)

    # Test that prepare_field_value returns value as-is
    assert (
        source.prepare_field_value("test_field", FieldInfo(), "test_value", False)
        == "test_value"
    )
    assert source.prepare_field_value(
        "test_field", FieldInfo(), {"key": "value"}, True
    ) == {"key": "value"}
    assert source.prepare_field_value("test_field", FieldInfo(), None, False) is None


def test_django_settings_source_call(settings):
    """Test DjangoSettingsSource __call__ method."""
    source = DjangoSettingsSource(WidgetSettings)

    # Test when BOOTSTRAP_DATEPICKER_PLUS exists
    test_config = {
        "debug": False,
        "template_name": "custom.html",
        "options": {"locale": "fr"},
    }
    settings.BOOTSTRAP_DATEPICKER_PLUS = test_config
    result = source()
    assert result == test_config

    # Test when BOOTSTRAP_DATEPICKER_PLUS doesn't exist
    del settings.BOOTSTRAP_DATEPICKER_PLUS
    result = source()
    assert result == {}


def test_django_settings_source_integration_with_widget_settings(settings):
    """Test DjangoSettingsSource integration with WidgetSettings."""
    # Test that DjangoSettingsSource is properly integrated with WidgetSettings
    test_config = {
        "debug": False,
        "template_name": "custom_template.html",
        "options": {"locale": "fr", "format": "DD/MM/YYYY"},
        "addon_icon_classes": {WidgetVariant.date: "custom-icon"},
    }

    settings.BOOTSTRAP_DATEPICKER_PLUS = test_config
    get_widget_settings.cache_clear()

    widget_settings = get_widget_settings()
    assert widget_settings.debug is False
    assert widget_settings.template_name == "custom_template.html"
    assert widget_settings.options["locale"] == "fr"
    assert widget_settings.options["format"] == "DD/MM/YYYY"
    assert widget_settings.addon_icon_classes[WidgetVariant.date] == "custom-icon"
    assert widget_settings.addon_icon_classes[WidgetVariant.date] == "custom-icon"
    assert widget_settings.addon_icon_classes[WidgetVariant.date] == "custom-icon"
