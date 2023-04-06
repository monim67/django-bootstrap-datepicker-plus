from typing import List, Optional, Type

from bootstrap_modal_forms.generic import BSModalCreateView
from django.forms import ModelForm, formset_factory
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django_filters.views import FilterView

from bootstrap_datepicker_plus.widgets import (
    DatePickerInput,
    DateTimePickerInput,
    MonthPickerInput,
    TimePickerInput,
    YearPickerInput,
)
from dev.myapp.forms import (
    CustomForm,
    EventFilter,
    EventForm,
    EventModalModelForm,
    ToDoForm,
)
from dev.myapp.models import Event


class SuccessRedirectMixin:
    request: HttpRequest

    def get_success_url(self) -> str:
        return self.request.META.get("HTTP_REFERER", "/")


class NamespaceTemplateMixin:
    request: HttpRequest

    def get_template_names(self) -> List[str]:
        template_names: List[str] = super().get_template_names()  # type: ignore
        if self.request.resolver_match:
            template_names = [
                name.format(namespace=self.request.resolver_match.namespace)
                for name in template_names
            ]
        return template_names


class EventListView(NamespaceTemplateMixin, FilterView):  # type: ignore
    template_name = "myapp/{namespace}/event_filter.html"
    filterset_class = EventFilter
    extra_context = {
        "title_text": "ListView with django-filter",
        "submit_text": "Search",
    }


class CustomFormView(
    NamespaceTemplateMixin, SuccessRedirectMixin, FormView[CustomForm]
):
    template_name = "myapp/{namespace}/custom-form.html"
    form_class = CustomForm
    extra_context = {
        "title_text": "Custom Form",
        "submit_text": "Submit",
    }


class EventCreateView(
    NamespaceTemplateMixin, SuccessRedirectMixin, CreateView[Event, ModelForm[Event]]
):
    template_name = "myapp/{namespace}/custom-form.html"
    model = Event
    fields = [
        "name",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "start_datetime",
        "end_datetime",
        "start_month",
        "end_month",
        "start_year",
        "end_year",
    ]
    extra_context = {
        "title_text": "Generic View without using model form",
        "submit_text": "Create Event",
    }

    def get_form(
        self, form_class: Optional[Type[ModelForm[Event]]] = None
    ) -> ModelForm[Event]:
        form = super().get_form(form_class)
        form.fields["start_date"].widget = DatePickerInput()
        form.fields["end_date"].widget = DatePickerInput(range_from="start_date")
        form.fields["start_time"].widget = TimePickerInput()
        form.fields["end_time"].widget = TimePickerInput(range_from="start_time")
        form.fields["start_datetime"].widget = DateTimePickerInput()
        form.fields["end_datetime"].widget = DateTimePickerInput(
            range_from="start_datetime"
        )
        form.fields["start_month"].widget = MonthPickerInput()
        form.fields["end_month"].widget = MonthPickerInput(range_from="start_month")
        form.fields["start_year"].widget = YearPickerInput()
        form.fields["end_year"].widget = YearPickerInput(range_from="start_year")
        return form


class EventUpdateView(
    NamespaceTemplateMixin, SuccessRedirectMixin, UpdateView[Event, EventForm]
):
    model = Event
    form_class = EventForm
    template_name = "myapp/{namespace}/custom-form.html"
    extra_context = {
        "title_text": "Model Form",
        "submit_text": "Update",
    }


class CrispyFormView(NamespaceTemplateMixin, SuccessRedirectMixin, FormView[ToDoForm]):
    template_name = "myapp/{namespace}/crispy-form.html"
    form_class = ToDoForm
    extra_context = {
        "title_text": "Use with django-crispy-forms",
    }


class DynamicFormsetView(
    NamespaceTemplateMixin, SuccessRedirectMixin, FormView[ToDoForm]
):
    form_class = formset_factory(ToDoForm, extra=2)  # type: ignore
    template_name = "myapp/{namespace}/custom-formset.html"
    extra_context = {
        "title_text": "Use with Formsets",
        "submit_text": "Submit",
    }


class EventModalCreateView(
    NamespaceTemplateMixin, SuccessRedirectMixin, BSModalCreateView  # type: ignore
):
    template_name = "myapp/{namespace}/modal-form.html"
    form_class = EventModalModelForm
    success_message = "Success: Event was created."
    success_url = reverse_lazy("index")
    extra_context = {
        "title_text": "Create new Event",
        "submit_text": "Submit",
    }


class ModalIndexTemplateView(NamespaceTemplateMixin, TemplateView):
    template_name = "myapp/{namespace}/modal-form-index.html"
    extra_context = {
        "title_text": "Usage with django-bootstrap-modal-forms",
        "submit_text": "Submit",
        "form": EventModalModelForm,  # Hack to make form.media work
    }
