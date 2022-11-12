from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
    path(
        "",
        lambda _: HttpResponse(
            '<META http-equiv="refresh" content="0;URL=bootstrap5/">'
        ),
    ),
    path("bootstrap3/", include("dev.myapp.urls", namespace="bootstrap3")),
    path("bootstrap4/", include("dev.myapp.urls", namespace="bootstrap4")),
    path("bootstrap5/", include("dev.myapp.urls", namespace="bootstrap5")),
]
