from typing import Iterable, NoReturn

from crispy_forms.helper import FormHelper
from django import forms
from django_filters import DateFilter, FilterSet

from bootstrap_datepicker_plus.widgets import (
    DatePickerInput,
    DateTimePickerInput,
    MonthPickerInput,
    TimePickerInput,
    YearPickerInput,
)
from dev.myapp.models import Event


class CustomForm(forms.Form):
    date = forms.DateField(label="Date", widget=DatePickerInput(), initial="2021-12-13")
    message = forms.CharField(label="Message", widget=forms.Textarea)

    def clean_date(self) -> NoReturn:
        raise forms.ValidationError("Just testing form errors")


class ToDoForm(forms.Form):
    start_date = forms.DateField(label="Start Date", widget=DatePickerInput())
    end_date = forms.DateField(
        label="End Date", widget=DatePickerInput(range_from="start_date")
    )

    @property
    def helper(self) -> FormHelper:
        helper = FormHelper()
        helper.include_media = False
        return helper


class EventForm(forms.ModelForm[Event]):
    class Meta:
        model = Event
        fields = [
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
        widgets = {
            "start_date": DatePickerInput(options={"format": "MM/DD/YYYY"}),
            "end_date": DatePickerInput(
                options={"format": "MM/DD/YYYY"}, range_from="start_date"
            ),
            "start_datetime": DateTimePickerInput(),
            "end_datetime": DateTimePickerInput(range_from="start_datetime"),
            "start_time": TimePickerInput(),
            "end_time": TimePickerInput(range_from="start_time"),
            "start_month": MonthPickerInput(),
            "end_month": MonthPickerInput(range_from="start_month"),
            "start_year": YearPickerInput().start_of("deprecated! do not use start_of"),
            "end_year": YearPickerInput().end_of("deprecated! do not use end_of"),
        }


class EventFilter(FilterSet):  # type: ignore
    start_date__gt = DateFilter(
        field_name="start_date",
        lookup_expr="gt",
        widget=DatePickerInput(),
    )
    start_date__lt = DateFilter(
        field_name="start_date",
        lookup_expr="lt",
        widget=DatePickerInput(range_from="start_date__gt"),
    )

    class Meta:
        model = Event
        fields: Iterable[str] = []
