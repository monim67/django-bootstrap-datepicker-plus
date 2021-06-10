from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

app_name = "myapp"

urlpatterns = [
    # fmt: off
    url(r"^$", RedirectView.as_view(pattern_name="myapp:bootstrap3.custom-form", permanent=False)),
    url("bootstrap3/custom-form.html", views.Bootstrap3_CustomFormView.as_view(), name="bootstrap3.custom-form"),
    url(r"^bootstrap3/model-form-(?P<pk>[0-9]+).html$", views.Bootstrap3_UpdateView.as_view(), name="bootstrap3.model-form-1"),
    url("bootstrap4/custom-form.html", views.Bootstrap4_CustomFormView.as_view(), name="bootstrap4.custom-form"),
    url(r"^bootstrap4/model-form-(?P<pk>[0-9]+).html$", views.Bootstrap4_UpdateView.as_view(), name="bootstrap4.model-form-1"),
]
