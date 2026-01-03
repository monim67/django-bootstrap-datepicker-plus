"""Contains Base Date-Picker input class for widgets of this package."""

import warnings
from typing import Any

from django import forms
from django.forms.widgets import DateTimeBaseInput

from ._config import WidgetConfig
from .schemas import InputAttrs, WidgetOptions, WidgetVariant
from .settings import get_widget_settings


class BasePickerInput(DateTimeBaseInput):
    """Base Date-Picker input class for widgets of this package."""

    variant = WidgetVariant.date
    _date_format = "%Y-%m-%d"
    backend_date_format = "YYYY-MM-DD"
    options: WidgetOptions | None = None
    template_name = "bootstrap_datepicker_plus/input.html"

    def __init__(
        self,
        attrs: InputAttrs | None = None,
        format: str | None = None,
        options: WidgetOptions | None = None,
        range_from: str | None = None,
    ):
        """Date-picker input widget.

        Args:
            attrs: HTML attributes of rendered HTMLInputElement
            format: Deprecated and not in use anymore
            options: Options to customize the widget, see README
            range_from: Name of input element to link with for range selection
        """
        if format is not None:
            warnings.warn(
                "The 'format' parameter is ignored, set 'format' in options instead. "
                "see https://github.com/monim67/django-bootstrap-datepicker-plus",
                category=FutureWarning,
            )
        settings = get_widget_settings()
        self.template_name = settings.template_name or self.template_name
        self.config = WidgetConfig(
            variant=self.variant,
            backend_date_format=self.backend_date_format,
            range_from=range_from,
        )
        self.config.update_options(
            settings.options,
            settings.variant_options.get(self.variant),
            self.options,
            options,
        )
        super().__init__(attrs, self._date_format)

    def build_attrs(
        self, base_attrs: InputAttrs, extra_attrs: InputAttrs | None = None
    ) -> InputAttrs:
        """Build an attribute dictionary."""
        settings = get_widget_settings()
        attrs = {
            **settings.attrs,
            **base_attrs,
            **(extra_attrs or {}),
            "data-dbdp-config": self.config.to_attr_value(),
        }
        if settings.debug:
            attrs["data-dbdp-debug"] = ""
        return attrs

    def get_context(
        self, name: str, value: Any, attrs: InputAttrs | None
    ) -> dict[str, Any]:
        """Return widget context dictionary."""
        settings = get_widget_settings()
        context = super().get_context(name, value, attrs)
        context["widget"]["addon_icon_class"] = settings.addon_icon_classes[
            self.variant
        ]
        return context

    @property
    def media(self) -> forms.Media:  # type: ignore
        """Generate widget Media."""
        settings = get_widget_settings()
        return forms.Media(
            css={
                "all": tuple_exclude_none(
                    settings.bootstrap_icon_css_url,
                    settings.datetimepicker_css_url,
                    settings.app_static_url + "css/datepicker-widget.css",
                ),
            },
            js=tuple_exclude_none(
                settings.momentjs_url,
                settings.datetimepicker_js_url,
                settings.app_static_url + "js/datepicker-widget.js",
            ),
        )


def tuple_exclude_none(*items: str | None) -> tuple[str, ...]:
    """Create a tuple removing None values."""
    return tuple(item for item in items if item is not None)
