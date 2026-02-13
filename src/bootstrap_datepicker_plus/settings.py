"""Package settings."""

import functools
from typing import Any

from django.conf import settings as django_settings
from pydantic import Field, field_validator
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
)

from .schemas import WidgetOptions, WidgetVariant


class DjangoSettingsSource(PydanticBaseSettingsSource):
    """Custom settings source that reads from Django settings."""

    def get_field_value(self, field, field_name: str):
        """Get field value from Django settings."""
        django_config = getattr(django_settings, "BOOTSTRAP_DATEPICKER_PLUS", {})
        return django_config.get(field_name), field_name, False

    def prepare_field_value(
        self, field_name: str, field, value: Any, value_is_complex: bool
    ) -> Any:
        """Prepare field value."""
        return value

    def __call__(self) -> dict[str, Any]:
        """Return all settings from Django config."""
        return getattr(django_settings, "BOOTSTRAP_DATEPICKER_PLUS", {})


addon_icon_default_classes = {
    WidgetVariant.date: "bi-calendar",
    WidgetVariant.time: "bi-clock",
    WidgetVariant.datetime: "bi-calendar",
    WidgetVariant.month: "bi-calendar",
    WidgetVariant.year: "bi-calendar",
}


class WidgetSettings(BaseSettings):
    """Settings to customize input widgets."""

    template_name: str | None = None
    attrs: dict[str, str] = Field(default_factory=dict)
    options: WidgetOptions = Field(default_factory=dict)
    variant_options: dict[WidgetVariant, WidgetOptions] = Field(default_factory=dict)
    addon_icon_classes: dict[WidgetVariant, str] = Field(
        default_factory=lambda: addon_icon_default_classes.copy()
    )
    momentjs_url: str | None = (
        "https://cdn.jsdelivr.net/npm/moment@2.29.4/min/moment-with-locales.min.js"
    )
    datetimepicker_js_url: str | None = (
        "https://cdn.jsdelivr.net/npm/eonasdan-bootstrap-datetimepicker@4.17.49/build/js/bootstrap-datetimepicker.min.js"
    )
    datetimepicker_css_url: str | None = (
        "https://cdn.jsdelivr.net/npm/eonasdan-bootstrap-datetimepicker@4.17.49/build/css/bootstrap-datetimepicker.min.css"
    )
    bootstrap_icon_css_url: str | None = (
        "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css"
    )
    app_static_url: str = (
        "https://cdn.jsdelivr.net/gh/monim67/django-bootstrap-datepicker-plus@4c7f504/src/bootstrap_datepicker_plus/static/bootstrap_datepicker_plus/"
    )
    debug: bool = Field(default_factory=lambda: getattr(django_settings, "DEBUG", True))

    model_config = SettingsConfigDict(
        env_prefix="BOOTSTRAP_DATEPICKER_PLUS_",
    )

    @field_validator("addon_icon_classes")
    @classmethod
    def _merge_with_default_dict_value(
        cls, v: dict[WidgetVariant, str]
    ) -> dict[WidgetVariant, str]:
        """Merge provided addon_icon_classes with defaults."""
        return {**addon_icon_default_classes, **v}

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """Add django settings as config source."""
        return (
            init_settings,
            env_settings,
            file_secret_settings,
            DjangoSettingsSource(settings_cls),
        )


@functools.lru_cache(maxsize=1)
def get_widget_settings() -> WidgetSettings:
    """Initialize and return WidgetSettings."""
    return WidgetSettings()
