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
    """Sets proper bootstrap version based on active demo app url user is visiting."""

    request: HttpRequest
    agent_prompt: str | None = None

    def get_template_names(self) -> List[str]:
        template_names: List[str] = super().get_template_names()  # type: ignore
        if self.request.resolver_match:
            template_names = [
                name.format(namespace=self.request.resolver_match.namespace)
                for name in template_names
            ]
        return template_names

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)  # type: ignore
        if self.request.resolver_match and self.agent_prompt:
            agent_prompt = self.agent_prompt.format(
                docs_url="https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/llms.txt",
                repo_baseurl="https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master",
                namespace=self.request.resolver_match.namespace,
            )
            context.update({"agent_prompt": agent_prompt})
        return context


class EventListView(NamespaceTemplateMixin, FilterView):  # type: ignore
    agent_prompt = """
- Docs: {docs_url}
- EventFilter (note range_from uses FilterSet field name): {repo_baseurl}/dev/myapp/forms.py
- EventListView: {repo_baseurl}/dev/myapp/views.py
- template: {repo_baseurl}/dev/myapp/templates/myapp/{namespace}/event_filter.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    template_name = "myapp/{namespace}/event_filter.html"
    filterset_class = EventFilter
    extra_context = {
        "title_text": "ListView with django-filter",
        "submit_text": "Search",
        "lead_text": 'Shows how to use date picker widgets in a <a href="https://pypi.org/project/django-filter/">django-filter</a> FilterSet.',
    }


class CustomFormView(
    NamespaceTemplateMixin, SuccessRedirectMixin, FormView[CustomForm]
):
    agent_prompt = """
- Docs: {docs_url}
- CustomForm: {repo_baseurl}/dev/myapp/forms.py
- CustomFormView: {repo_baseurl}/dev/myapp/views.py
- template (note how form.media is placed): {repo_baseurl}/dev/myapp/templates/myapp/{namespace}/custom-form.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    template_name = "myapp/{namespace}/custom-form.html"
    form_class = CustomForm
    extra_context = {
        "title_text": "Custom Form",
        "submit_text": "Submit",
        "lead_text": "Shows how to add a date picker to a plain Django form.",
    }


class EventCreateView(
    NamespaceTemplateMixin, SuccessRedirectMixin, CreateView[Event, ModelForm[Event]]
):
    agent_prompt = """
- Docs: {docs_url}
- EventCreateView (note get_form method): {repo_baseurl}/dev/myapp/views.py
- template (note how form.media is placed): {repo_baseurl}/dev/myapp/templates/myapp/{namespace}/custom-form.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
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
        "lead_text": "Shows how to add date pickers to a generic CreateView by overriding get_form().",
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
    agent_prompt = """
- Docs: {docs_url}
- EventForm: {repo_baseurl}/dev/myapp/forms.py
- EventUpdateView: {repo_baseurl}/dev/myapp/views.py
- template (note how form.media is placed): {repo_baseurl}/dev/myapp/templates/myapp/{namespace}/custom-form.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    model = Event
    form_class = EventForm
    template_name = "myapp/{namespace}/custom-form.html"
    extra_context = {
        "title_text": "Model Form",
        "submit_text": "Update",
        "lead_text": "Shows how to add date pickers to a ModelForm using the Meta.widgets option.",
    }


class CrispyFormView(NamespaceTemplateMixin, SuccessRedirectMixin, FormView[ToDoForm]):
    agent_prompt = """
- Docs: {docs_url}
- ToDoForm (note helper.include_media = False): {repo_baseurl}/dev/myapp/forms.py
- CrispyFormView: {repo_baseurl}/dev/myapp/views.py
- template: {repo_baseurl}/dev/myapp/templates/myapp/{namespace}/crispy-form.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    template_name = "myapp/{namespace}/crispy-form.html"
    form_class = ToDoForm
    extra_context = {
        "title_text": "Use with django-crispy-forms",
        "lead_text": 'Shows how to use date pickers with <a href="https://pypi.org/project/django-crispy-forms/">django-crispy-forms</a>.',
    }


class DynamicFormsetView(
    NamespaceTemplateMixin, SuccessRedirectMixin, FormView[ToDoForm]
):
    agent_prompt = """
- Docs: {docs_url}
- DynamicFormsetView: {repo_baseurl}/dev/myapp/views.py
- template (note management_form and media outside loop): {repo_baseurl}/dev/myapp/templates/myapp/{namespace}/custom-formset.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    form_class = formset_factory(ToDoForm, extra=2)  # type: ignore
    template_name = "myapp/{namespace}/custom-formset.html"
    extra_context = {
        "title_text": "Use with Formsets",
        "submit_text": "Submit",
        "lead_text": "Shows how to use date pickers in a Django formset.",
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
    agent_prompt = """
- Docs: {docs_url}
- EventModalModelForm: {repo_baseurl}/dev/myapp/forms.py
- ModalIndexTemplateView, EventModalCreateView: {repo_baseurl}/dev/myapp/views.py
- template (note form.media is on parent page, not in modal): {repo_baseurl}/dev/myapp/templates/myapp/{namespace}/modal-form-index.html

Study these files, then make the minimal changes required to my existing setup to add datepicker to
"""
    template_name = "myapp/{namespace}/modal-form-index.html"
    extra_context = {
        "title_text": "Usage with django-bootstrap-modal-forms",
        "submit_text": "Submit",
        "lead_text": 'Shows how to use date pickers with <a href="https://pypi.org/project/django-bootstrap-modal-forms/">django-bootstrap-modal-forms</a>.',
        "form": EventModalModelForm,  # Hack to make form.media work
    }
