from posixpath import dirname, relpath
from typing import Optional

from django import template
from django.http import HttpRequest
from django.urls import reverse, translate_url

register = template.Library()


@register.simple_tag(takes_context=True)
def canonical_url(context: dict) -> Optional[str]:
    request: HttpRequest = context["request"]
    try:
        url_name = request.resolver_match.url_name  # type: ignore[union-attr]
        bs5_path = reverse(f"bootstrap5:{url_name}")
        canonical_path = translate_url(bs5_path, "en-us")
        rel = relpath(canonical_path, dirname(request.path))
        return rel if rel.startswith(".") else f"./{rel}"
    except Exception:
        return None
