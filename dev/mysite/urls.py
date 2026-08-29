from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

from dev.myapp import urls as myapp_urls
from dev.myapp.utils import http_meta_redirect_view

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("", http_meta_redirect_view("bootstrap5/")),
] + i18n_patterns(
    path("bootstrap3/", include(myapp_urls, namespace="bootstrap3")),
    path("bootstrap4/", include(myapp_urls, namespace="bootstrap4")),
    path("bootstrap5/", include(myapp_urls, namespace="bootstrap5")),
    prefix_default_language=False,
)
