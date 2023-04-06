from django.http import HttpResponse
from django.urls import path

from dev.myapp import views

app_name = "myapp"

urlpatterns = [
    path(
        "",
        lambda _: HttpResponse(
            '<META http-equiv="refresh" content="0;URL=custom-form.html">'
        ),
    ),
    path("custom-form.html", views.CustomFormView.as_view(), name="custom-form"),
    path(
        "model-form.html", views.EventUpdateView.as_view(), {"pk": 1}, name="model-form"
    ),
    path("generic-view.html", views.EventCreateView.as_view(), name="generic-view"),
    path("crispy-form.html", views.CrispyFormView.as_view(), name="crispy-form"),
    path("django-filter.html", views.EventListView.as_view(), name="django-filter"),
    path(
        "dynamic-formset.html",
        views.DynamicFormsetView.as_view(),
        name="dynamic-formset",
    ),
    path(
        "modal-form.html",
        views.EventModalCreateView.as_view(),
        name="modal-form",
    ),
    path(
        "modal-form-index.html",
        views.ModalIndexTemplateView.as_view(),
        name="modal-form-index",
    ),
]
