from django.shortcuts import render
from django.views.generic.edit import FormView, UpdateView
from django.http import HttpResponseRedirect

from .models import Event
from .forms import CustomForm, EventForm


class Bootstrap3_CustomFormView(FormView):
    template_name = 'demo_app/bootstrap3/custom-form.html'
    form_class = CustomForm

    def form_valid(self, form):
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class Bootstrap4_CustomFormView(FormView):
    template_name = 'demo_app/bootstrap4/custom-form.html'
    form_class = CustomForm

    def form_valid(self, form):
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class Bootstrap3_UpdateView(UpdateView):
    template_name = 'demo_app/bootstrap3/model-form.html'
    model = Event
    form_class = EventForm


class Bootstrap4_UpdateView(UpdateView):
    template_name = 'demo_app/bootstrap4/model-form.html'
    model = Event
    form_class = EventForm
