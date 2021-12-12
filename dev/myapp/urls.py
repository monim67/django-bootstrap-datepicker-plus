from django.urls import re_path
from django.views.generic import RedirectView

from . import views

app_name = "myapp"

urlpatterns = [
    # fmt: off
    re_path(r"^$", RedirectView.as_view(pattern_name="myapp:bootstrap3.custom-form", permanent=False)),
    re_path("bootstrap3/custom-form.html", views.Bootstrap3_CustomFormView.as_view(), name="bootstrap3.custom-form"),
    re_path(r"^bootstrap3/model-form-(?P<pk>[0-9]+).html$", views.Bootstrap3_UpdateView.as_view(), name="bootstrap3.model-form-1"),
    re_path("bootstrap4/custom-form.html", views.Bootstrap4_CustomFormView.as_view(), name="bootstrap4.custom-form"),
    re_path(r"^bootstrap4/model-form-(?P<pk>[0-9]+).html$", views.Bootstrap4_UpdateView.as_view(), name="bootstrap4.model-form-1"),
]
