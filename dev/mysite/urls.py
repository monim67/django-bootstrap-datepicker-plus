from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponse
from django.urls import include, path

from dev.myapp import urls as myapp_urls


def _index_view(_request):
    return HttpResponse(
        '<META http-equiv="refresh" content="0;URL=bootstrap5/">'
        "<ul>"
        '<li><a href="bootstrap3/">Bootstrap 3</a></li>'
        '<li><a href="bootstrap4/">Bootstrap 4</a></li>'
        '<li><a href="bootstrap5/">Bootstrap 5</a></li>'
        "</ul>"
    )


urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("", _index_view),
] + i18n_patterns(
    path("bootstrap3/", include(myapp_urls, namespace="bootstrap3")),
    path("bootstrap4/", include(myapp_urls, namespace="bootstrap4")),
    path("bootstrap5/", include(myapp_urls, namespace="bootstrap5")),
    prefix_default_language=False,
)
