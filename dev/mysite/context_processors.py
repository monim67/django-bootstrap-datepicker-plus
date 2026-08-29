from typing import Any, Dict

from django import VERSION as DJANGO_VERSION
from django import get_version as get_django_version
from django.http import HttpRequest
from django.urls import translate_url

LANG_CHOICES = [
    ("en-us", "English"),
    ("bn", "Bengali"),
    ("fr", "French"),
    ("es", "Spanish"),
    ("ja", "Japanese"),
]


def site_context(request: HttpRequest) -> Dict[str, Any]:
    path = request.get_full_path()
    context = {
        "django_version": DJANGO_VERSION,
        "django_version_string": get_django_version(),
        "lang_choices": LANG_CHOICES,
        "lang_url_choices": [
            (code, label, translate_url(path, code)) for code, label in LANG_CHOICES
        ],
    }
    return context
