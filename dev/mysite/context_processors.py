from django import VERSION as django_version
from django import get_version as get_django_version


def demo_context(request):
    context = {
        "django_version": django_version,
        "django_version_string": get_django_version(),
        "url_section": "",
        "url_sub_section": "",
        "bootstrap_version": "",
        "bootstrap4_supported": django_version > (1, 11),
    }
    url_name_parts = request.resolver_match.url_name.split(".", 1)
    if len(url_name_parts) == 2 and url_name_parts[0][:-1] == "bootstrap":
        context["url_section"] = url_name_parts[0]
        context["url_sub_section"] = url_name_parts[1]
        context["bootstrap_version"] = int(url_name_parts[0][-1])
    return context
