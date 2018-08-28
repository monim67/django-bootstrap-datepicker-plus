from django import forms
from .models import Event

from bootstrap_datepicker_plus import DatePickerInput
from bootstrap_datepicker_plus import TimePickerInput
from bootstrap_datepicker_plus import DateTimePickerInput
from bootstrap_datepicker_plus import MonthPickerInput
from bootstrap_datepicker_plus import YearPickerInput


class CustomForm(forms.Form):
    # name = forms.CharField(label="Name")
    date = forms.DateField(label="Date", widget=DatePickerInput())
    message = forms.CharField(label="Message", widget=forms.Textarea)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'start_date', 'end_date',
            'start_time', 'end_time',
            'start_datetime', 'end_datetime',
            'start_month', 'end_month',
            'start_year', 'end_year',
        ]
        widgets = {
            'start_date': DatePickerInput(options={'format': 'YYYY-MM-DD', 'debug': True}).start_of('event active days'),
            'end_date': DatePickerInput(options={'format': 'MM/DD/YYYY'}).end_of('event active days'),
            'start_datetime': DateTimePickerInput(options={'debug': True}).start_of('event active dtime'),
            'end_datetime': DateTimePickerInput().end_of('event active dtime'),
            'start_time': TimePickerInput(options={'debug': True}).start_of('event active time'),
            'end_time': TimePickerInput().end_of('event active time'),
            'start_month': MonthPickerInput().start_of('active month'),
            'end_month': MonthPickerInput().end_of('active month'),
            'start_year': YearPickerInput().start_of('active year'),
            'end_year': YearPickerInput().end_of('active year'),
        }
