from typing import Dict

from django import VERSION as DJANGO_VERSION
from django import get_version as get_django_version
from django.http import HttpRequest


def site_context(request: HttpRequest) -> Dict[str, str]:
    context = {
        "django_version": DJANGO_VERSION,
        "django_version_string": get_django_version(),
    }
    return context
