from django.http import HttpResponse
from django.urls import include, path

from dev.myapp.utils import http_meta_redirect_view

urlpatterns = [
    path("", http_meta_redirect_view("bootstrap5/")),
    path("bootstrap3/", include("dev.myapp.urls", namespace="bootstrap3")),
    path("bootstrap4/", include("dev.myapp.urls", namespace="bootstrap4")),
    path("bootstrap5/", include("dev.myapp.urls", namespace="bootstrap5")),
]
