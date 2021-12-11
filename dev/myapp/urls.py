from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "myapp"

urlpatterns = [
    # fmt: off
    path("", RedirectView.as_view(pattern_name="myapp:bootstrap3.custom-form", permanent=False)),
    path("bootstrap3/custom-form.html", views.Bootstrap3_CustomFormView.as_view(), name="bootstrap3.custom-form"),
    path("bootstrap3/model-form-<int:pk>.html", views.Bootstrap3_UpdateView.as_view(), name="bootstrap3.model-form-1"),
    path("bootstrap4/custom-form.html", views.Bootstrap4_CustomFormView.as_view(), name="bootstrap4.custom-form"),
    path("bootstrap4/model-form-<int:pk>.html", views.Bootstrap4_UpdateView.as_view(), name="bootstrap4.model-form-1"),
]
