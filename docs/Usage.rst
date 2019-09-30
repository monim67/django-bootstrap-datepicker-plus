Usage
-----


Usage in Generic View
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
   :emphasize-lines: 2,11

    # File: views.py
    from bootstrap_datepicker_plus import DateTimePickerInput
    from django.views import generic
    from .models import Question

    class CreateView(generic.edit.CreateView):
        model = Question
        fields = ['question_text', 'pub_date']
        def get_form(self):
            form = super().get_form()
            form.fields['pub_date'].widget = DateTimePickerInput()
            return form


Custom Form usage
^^^^^^^^^^^^^^^^^

.. code-block:: python
   :emphasize-lines: 2,11

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput
    from .models import Event
    from django import forms

    class ToDoForm(forms.Form):
        todo = forms.CharField(
            widget=forms.TextInput(attrs={"class": "form-control"})
        )
        date = forms.DateField(
            widget=DatePickerInput(format='%m/%d/%Y')
        )


Model Form usage
^^^^^^^^^^^^^^^^

.. code-block:: python
   :emphasize-lines: 2,11-12

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput
    from .models import Event
    from django import forms

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'start_date', 'end_date']
            widgets = {
                'start_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
                'end_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
            }


Types of DatePickers
^^^^^^^^^^^^^^^^^^^^

The widget contains all types of date-picker you may ever need.

.. code-block:: python
   :emphasize-lines: 2,11-15

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
    from .models import Event
    from django import forms

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = ['start_date', 'start_time', 'start_datetime', 'start_month', 'start_year']
            widgets = {
                'start_date': DatePickerInput(),
                'start_time': TimePickerInput(),
                'start_datetime': DateTimePickerInput(),
                'start_month': MonthPickerInput(),
                'start_year': YearPickerInput(),
            }


Implement date-range-picker
^^^^^^^^^^^^^^^^^^^^^^^^^^^

DatePickers can be linked to select a date-range or time-range.

.. code-block:: python
   :emphasize-lines: 2,11-12

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
    from .models import Event
    from django import forms

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'start_date', 'end_date', 'start_time', 'end_time']
            widgets = {
                'start_date':DatePickerInput().start_of('event days'),
                'end_date':DatePickerInput().end_of('event days'),
                'start_time':TimePickerInput().start_of('party time'),
                'end_time':TimePickerInput().end_of('party time'),
            }


Customize Datepicker Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The DatePicker can be customized by passing options to it.
The ``options`` will be passed to the JavaScript datepicker instance, and are documented and demonstrated in 
`Bootstrap Datepicker Options Reference <http://eonasdan.github.io/bootstrap-datetimepicker/Options/>`__.

.. code-block:: python
   :emphasize-lines: 14-17

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput
    from .models import Event
    from django import forms

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'start_date', 'end_date']
            widgets = {
                'start_date': DatePickerInput(format='%m/%d%Y'), # python date-time format
                'end_date': DatePickerInput(
                    options={
                        "format": "MM/DD/YYYY", # moment date-time format 
                        "showClose": True,
                        "showClear": True,
                        "showTodayButton": True,
                    }
                ),
            }

**Note:** You can specify the date-time format by passing a
`python date-time format <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`__
as format parameter (see start_date in the example), or by passing a
`moment date-time format <http://momentjs.com/docs/#/displaying/format/>`__
as an option (see end_date in the example).
If both are specified then the moment format in options will take precedence.


Customize the Language
^^^^^^^^^^^^^^^^^^^^^^^

The DatePicker language can be customized by passing a ``locale`` option to datepicker input.
See `moment.js locales <https://github.com/moment/moment/tree/develop/locale>`__ for valid locales.

.. code-block:: python
   :emphasize-lines: 14

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput
    from .models import Event
    from django import forms

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'pub_date']
            widgets = {
                'pub_date': DatePickerInput(
                    options={
                        "format": "MM/DD/YYYY",
                        "locale": "bn",
                    }
                ),
            }


Event Handling
^^^^^^^^^^^^^^

Datepicker support event handling, which can be configured by passing a configuation dictionary.

The following events are supported: http://eonasdan.github.io/bootstrap-datetimepicker/Events/

.. code-block:: python
   :emphasize-lines: 13-15

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput
    from .models import Event
    from django import forms

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'pub_date']
            widgets = {
                'pub_date': DatePickerInput(
                    options={},
                    events = {
                        "dp.show": "myJavascriptFunction"
                    }
                ),
            }