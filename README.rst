########################################
django-bootstrap-datepicker-plus
########################################

This django widget contains Bootstrap 3, Bootstrap 4 and Bootstrap 5
Date-Picker, Time-Picker, DateTime-Picker, Month-Picker and Year-Picker input
with date-range-picker functionality for django version >= 2.0.
The widget implements `bootstrap-datetimepicker v4 <http://eonasdan.github.io/bootstrap-datetimepicker/>`_
to show bootstrap-datepicker in django model forms and custom forms
which can be configured easily for date-range selection.


|  |build-status| |docs-status| |coverage|
|  |pyversions| |djversions| |pypi-version| |license|

|  |date-picker-image| |datetime-picker-image| |time-picker-image|



********************
Demo
********************

- `With Bootstrap 3 <https://monim67.github.io/django-bootstrap-datepicker-plus/>`_.
- `With Bootstrap 4 <https://monim67.github.io/django-bootstrap-datepicker-plus/Bootstrap4.html>`_.



********************
Getting Started
********************

++++++++++++++++++++
Prerequisites
++++++++++++++++++++

- Python >= 3.6
- Django >= 2.0
- Bootstrap >= 3
- jquery >= 1.7.1


++++++++++++++++++++
Installing
++++++++++++++++++++

Install the PyPI package via pip

::

    pip install django-bootstrap-datepicker-plus

Add ``bootstrap_datepicker_plus`` to the list of ``INSTALLED_APPS`` in your ``settings.py`` file.

.. code:: python

    INSTALLED_APPS = [
        # Add the following
        'bootstrap_datepicker_plus',
    ]

This installation instruction assumes you have ``jQuery`` and Bootstrap JS/CSS files present in your template
and you are using ``form.media`` in your django template. If not you have to configure your template.


++++++++++++++++++++
Next Steps
++++++++++++++++++++

- `Template configuration <https://monim67.github.io/django-bootstrap-datepicker-plus/configure/>`_
- `Documentation on ReadTheDocs <https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/>`_
- `Quick Walkthrough Tutorial <https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Walkthrough.html>`_
- `I am having errors <https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Troubleshooting.html>`_



********************
Usage
********************


++++++++++++++++++++++++++++++
Usage in Generic View
++++++++++++++++++++++++++++++

.. code:: python

    # File: views.py
    from bootstrap_datepicker_plus.widgets import DateTimePickerInput
    from django.views import generic
    from .models import Question

    class CreateView(generic.edit.CreateView):
        model = Question
        fields = ['question_text', 'pub_date']
        def get_form(self):
            form = super().get_form()
            form.fields['pub_date'].widget = DateTimePickerInput()
            return form


++++++++++++++++++++++++++++++
Advanced Usage
++++++++++++++++++++++++++++++

- `Usage in Custom Form <https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Usage.html#custom-form-usage>`_
- `Usage in Model Form <https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Usage.html#model-form-usage>`_


++++++++++++++++++++++++++++++
Types of DatePickers
++++++++++++++++++++++++++++++

The widget contains all types of date-picker you may ever need.

.. code:: python

    # File: forms.py
    from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
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


++++++++++++++++++++++++++++++
Implement date-range-picker
++++++++++++++++++++++++++++++

DatePickers can be linked to select a date-range or time-range.

.. code:: python

    # File: forms.py
    from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
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


++++++++++++++++++++++++++++++
Customization
++++++++++++++++++++++++++++++

- `Datepicker Options <https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Usage.html#customize-datepicker-options>`_
- `Input field HTML template <https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Template_Customizing.html>`_
- `Language <https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Usage.html#customize-the-language>`_


********************
Contributing
********************

- `CONTRIBUTING.md <https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master/.github/CONTRIBUTING.md>`_.
- `CODE_OF_CONDUCT.md <https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master/.github/CODE_OF_CONDUCT.md>`_.

********************
License
********************

This project is licensed under Apache License 2.0 - see the `LICENSE <https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master/LICENSE>`_ file for details.

********************
Acknowledgments
********************

This project implements `Eonasdan/bootstrap-datetimepicker <https://github.com/Eonasdan/bootstrap-datetimepicker>`_ to display date-pickers.
The project was initially forked from `pbucher/django-bootstrap-datepicker <https://github.com/pbucher/django-bootstrap-datepicker>`_.

|buymeacoffee|


.. |date-picker-image| image:: https://raw.githubusercontent.com/monim67/django-bootstrap-datepicker-plus/26d89a744d403a895422313a48c02885c4718251/images/date-picker.png
    :alt: Date-picker
    :width: 218px
    :height: 280px

.. |datetime-picker-image| image:: https://raw.githubusercontent.com/monim67/django-bootstrap-datepicker-plus/26d89a744d403a895422313a48c02885c4718251/images/datetime-picker.png
    :alt: Datetime-picker
    :width: 218px
    :height: 280px

.. |time-picker-image| image:: https://raw.githubusercontent.com/monim67/django-bootstrap-datepicker-plus/26d89a744d403a895422313a48c02885c4718251/images/time-picker.png
    :alt: Time-picker
    :width: 218px
    :height: 280px

.. |build-status| image:: https://github.com/monim67/django-bootstrap-datepicker-plus/workflows/build/badge.svg?event=push
    :target: https://github.com/monim67/django-bootstrap-datepicker-plus/actions/workflows/build.yml
    :alt: Build Status
    :height: 20px

.. |docs-status| image:: https://readthedocs.org/projects/django-bootstrap-datepicker-plus/badge/?version=latest
    :target: https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
    :height: 20px

.. |coverage| image:: https://coveralls.io/repos/github/monim67/django-bootstrap-datepicker-plus/badge.svg?branch=master
    :target: https://coveralls.io/github/monim67/django-bootstrap-datepicker-plus?branch=master
    :alt: Coverage Status
    :height: 20px

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/django-bootstrap-datepicker-plus.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-datepicker-plus
    :alt: Python Versions
    :height: 20px

.. |djversions| image:: https://img.shields.io/pypi/djversions/django-bootstrap-datepicker-plus.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-datepicker-plus
    :alt: DJango Versions
    :height: 20px

.. |pypi-version| image:: https://badge.fury.io/py/django-bootstrap-datepicker-plus.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-datepicker-plus
    :alt: PyPI version
    :height: 20px

.. |license| image:: https://img.shields.io/pypi/l/django-bootstrap-datepicker-plus.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-datepicker-plus
    :alt: Licence
    :height: 20px

.. |buymeacoffee| image:: https://cdn.buymeacoffee.com/buttons/v2/default-orange.png
   :target: https://www.buymeacoffee.com/monim67
   :alt: Buy Me A Coffee
   :height: 48px
