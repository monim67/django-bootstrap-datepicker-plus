from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView, UpdateView

from .forms import CustomForm, EventForm
from .models import Event


class Bootstrap3_CustomFormView(FormView):
    template_name = "myapp/bootstrap3/custom-form.html"
    form_class = CustomForm

    def form_valid(self, form):
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER"))


class Bootstrap4_CustomFormView(FormView):
    template_name = "myapp/bootstrap4/custom-form.html"
    form_class = CustomForm

    def form_valid(self, form):
        return HttpResponseRedirect(self.request.META.get("HTTP_REFERER"))


class Bootstrap3_UpdateView(UpdateView):
    template_name = "myapp/bootstrap3/model-form.html"
    model = Event
    form_class = EventForm

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER")


class Bootstrap4_UpdateView(UpdateView):
    template_name = "myapp/bootstrap4/model-form.html"
    model = Event
    form_class = EventForm

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER")
