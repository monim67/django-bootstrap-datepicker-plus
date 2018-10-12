django-bootstrap-datepicker-plus
================================

This django widget contains Bootstrap 3 and Bootstrap 4
Date-Picker, Time-Picker, DateTime-Picker, Month-Picker and Year-Picker input
with date-range-picker functionality for django version 2.1, 2.0, 1.11, 1.10 and 1.8.
The widget implements `bootstrap-datetimepicker v4 <http://eonasdan.github.io/bootstrap-datetimepicker/>`__
to show bootstrap-datepicker in django model forms and custom forms
which can be configured easily for date-range selection.


|  |ci-status| |docs-status| |coverage.io| |maintainability| |test-coverage|
|  |pyversions| |djversions| |pypi-version|
|  |format| |status| |license|

|  |date-picker-image| |datetime-picker-image| |time-picker-image| 




Demo
----
-  `With Bootstrap 3 <https://monim67.github.io/django-bootstrap-datepicker-plus/>`__.
-  `With Bootstrap 4 <https://monim67.github.io/django-bootstrap-datepicker-plus/Bootstrap4.html>`__.



Getting Started
---------------


Prerequisites
^^^^^^^^^^^^^
-  Python >= 3.3
-  Django >= 1.8
-  Bootstrap >= 3
-  jquery >= 1.7.1


Installing
^^^^^^^^^^
Install the widget via pip

::

    pip install django-bootstrap-datepicker-plus

Add ``bootstrap_datepicker_plus`` to the list of ``INSTALLED_APPS`` in your ``settings.py`` file.

.. code:: python

    INSTALLED_APPS = [
        # Add the following
        'bootstrap_datepicker_plus',
    ]

This installation instruction assumes you have ``jQuery`` and Bootstrap JS/CSS files present in your template
and you are using ``form.media`` in your django template. If not you should checkout our
`configuration instructions <https://monim67.github.io/django-bootstrap-datepicker-plus/configure/>`__
which covers almost everything you need to get the widget running.



Usage
-----


Custom Form usage
^^^^^^^^^^^^^^^^^

.. code:: python

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput
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

.. code:: python

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput
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

.. code:: python

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
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

.. code:: python

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
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


Customize the Options
^^^^^^^^^^^^^^^^^^^^^

The DatePicker can be customised by passing options to it.
The ``options`` will be passed to the JavaScript datepicker instance, and are documented and demonstrated in 
`Bootstrap Datepicker Options Reference <http://eonasdan.github.io/bootstrap-datetimepicker/Options/>`__.

.. code:: python

    # File: forms.py
    from bootstrap_datepicker_plus import DatePickerInput
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


Contributing
------------

 - `CONTRIBUTING.md <https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master/.github/CONTRIBUTING.md>`__.
 - `CODE_OF_CONDUCT.md <https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master/.github/CODE_OF_CONDUCT.md>`__.

License
-------

This project is licensed under Apache License 2.0 - see the `LICENSE <https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master/LICENSE>`__ file for details.

Acknowledgments
---------------

This project implements `Eonasdan/bootstrap-datetimepicker <https://github.com/Eonasdan/bootstrap-datetimepicker>`__ to display date-pickers.
The project was initially forked from `pbucher/django-bootstrap-datepicker <https://github.com/pbucher/django-bootstrap-datepicker>`__.


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

.. |ci-status| image:: https://travis-ci.org/monim67/django-bootstrap-datepicker-plus.svg?branch=master
    :target: https://travis-ci.org/monim67/django-bootstrap-datepicker-plus
    :alt: Build Status
    :height: 20px

.. |docs-status| image:: https://readthedocs.org/projects/django-bootstrap-datepicker-plus/badge/?version=latest
    :target: https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
    :height: 20px

.. |coverage.io| image:: https://coveralls.io/repos/github/monim67/django-bootstrap-datepicker-plus/badge.svg?branch=master
    :target: https://coveralls.io/github/monim67/django-bootstrap-datepicker-plus?branch=master
    :alt: Coverage Status
    :height: 20px

.. |maintainability| image:: https://api.codeclimate.com/v1/badges/d89033abcc5c8220f4cb/maintainability
   :target: https://codeclimate.com/github/monim67/django-bootstrap-datepicker-plus/maintainability
   :alt: Maintainability
   :height: 20px

.. |test-coverage| image:: https://api.codeclimate.com/v1/badges/d89033abcc5c8220f4cb/test_coverage
   :target: https://codeclimate.com/github/monim67/django-bootstrap-datepicker-plus/test_coverage
   :alt: Test Coverage
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

.. |format| image:: https://img.shields.io/pypi/format/django-bootstrap-datepicker-plus.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-datepicker-plus
    :alt: Format
    :height: 20px

.. |status| image:: https://img.shields.io/pypi/status/django-bootstrap-datepicker-plus.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-datepicker-plus
    :alt: Status
    :height: 20px

.. |license| image:: https://img.shields.io/pypi/l/django-bootstrap-datepicker-plus.svg
    :target: https://pypi.python.org/pypi/django-bootstrap-datepicker-plus
    :alt: Licence
    :height: 20px
