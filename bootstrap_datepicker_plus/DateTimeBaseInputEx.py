# -*- coding: utf-8 -*-
from pathlib import Path

from django.forms.widgets import DateTimeBaseInput
from django.template.backends.django import DjangoTemplates
from django.utils import formats
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe

ROOT = Path(__file__).parent


class BaseRenderer:
    def get_template(self, template_name):
        raise NotImplementedError('subclasses must implement get_template()')

    def render(self, template_name, context, request=None):
        template = self.get_template(template_name)
        return template.render(context, request=request).strip()


class EngineMixin:
    def get_template(self, template_name):
        return self.engine.get_template(template_name)

    @cached_property
    def engine(self):
        return self.backend({
            'APP_DIRS': True,
            'DIRS': [str(ROOT / self.backend.app_dirname)],
            'NAME': 'djangoforms',
            'OPTIONS': {},
        })


class DjangoTemplatesEx(EngineMixin, BaseRenderer):
    """
    Load Django templates from the built-in widget templates in
    django/forms/templates and from apps' 'templates' directory.
    """
    backend = DjangoTemplates


class DateTimeBaseInputEx(DateTimeBaseInput):
    format = '%m/%d/%Y'
    format_key = 'DATE_INPUT_FORMATS'
    template_name = 'bootstrap_datepicker_plus/date-picker.html'

    def format_value(self, value):
        if value == '' or value is None:
            return None
        return formats.localize_input(value, self.format)

    def get_context(self, name, value, attrs):
        context = {}
        context['widget'] = {
            'name': name,
            'is_hidden': self.is_hidden,
            'required': self.is_required,
            'value': self.format_value(value),
            'attrs': {**self.attrs, **(attrs or {})},
            'template_name': self.template_name,
        }
        return context

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget as an HTML string."""
        context = self.get_context(name, value, attrs)
        return self._render(self.template_name, context, renderer)

    def _render(self, template_name, context, renderer=None):
        if renderer is None:
            renderer = DjangoTemplatesEx()
        return mark_safe(renderer.render(template_name, context))
