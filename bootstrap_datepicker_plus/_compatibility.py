# -*- coding: utf-8 -*-
"""Contains fallback/missing classes and methods for older django versions."""

from functools import lru_cache
from pathlib import Path

from django.forms.widgets import DateTimeBaseInput
from django.template.backends.django import DjangoTemplates
from django.utils import formats
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe

ROOT = Path(__file__).parent


class BaseRenderer:
    """Missing class from django.forms.renderers module."""

    def get_template(self, template_name):
        """Return template name."""
        raise NotImplementedError("subclasses must implement get_template()")

    def render(self, template_name, context, request=None):
        """Render template from template_name."""
        template = self.get_template(template_name)
        return template.render(context, request=request).strip()


class EngineMixin:
    """Missing class from django.forms.renderers module."""

    def get_template(self, template_name):
        """Return template name."""
        return self.engine.get_template(template_name)

    @cached_property
    def engine(self):
        """Return Render Engine."""
        return self.backend(
            {
                "APP_DIRS": True,
                "DIRS": [str(ROOT / self.backend.app_dirname)],
                "NAME": "djangoforms",
                "OPTIONS": {},
            }
        )


class DjangoTemplateRenderer(EngineMixin, BaseRenderer):
    """
    Missing default template renderer from django.forms.renderers module.

    Load Django templates from the built-in widget templates in
    django/forms/templates and from apps' 'templates' directory.
    """

    backend = DjangoTemplates


@lru_cache()
def get_default_renderer():
    """Missing method from django.forms.renderers module."""
    return DjangoTemplateRenderer()


class CompatibleDateTimeBaseInput(DateTimeBaseInput):
    """Fallback class containing methods missing in older django version."""

    format = "%m/%d/%Y"
    format_key = "DATE_INPUT_FORMATS"
    template_name = "bootstrap_datepicker_plus/date-picker.html"

    def format_value(self, value):
        """
        Return a value as it should appear when rendered in a template.

        Missing method of django.forms.widgets.Widget class
        """
        if value == "" or value is None:
            return None
        return formats.localize_input(value, self.format)

    def get_context(self, name, value, attrs):
        """Missing method of django.forms.widgets.Widget class."""
        context = {}
        context["widget"] = {
            "name": name,
            "type": "text",
            "is_hidden": self.is_hidden,
            "required": self.is_required,
            "value": self.format_value(value),
            "attrs": {**self.attrs, **(attrs or {})},
            "template_name": self.template_name,
        }
        return context

    def render(self, name, value, attrs=None, renderer=None):
        """
        Render the widget as an HTML string.

        Missing method of django.forms.widgets.Widget class
        """
        # pylint: disable=arguments-differ
        context = self.get_context(name, value, attrs)
        return self._render(self.template_name, context, renderer)

    def _render(self, template_name, context, renderer=None):
        """Missing method of django.forms.widgets.Widget class."""
        if renderer is None:
            renderer = get_default_renderer()
        return mark_safe(renderer.render(template_name, context))
