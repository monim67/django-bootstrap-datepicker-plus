django-bootstrap-datepicker-plus
================================

|  |ci-status| |coverage.io| |maintainability| |test-coverage|
|  |pyversions| |djversions| |pypi-version|
|  |format| |status| |license|

This Django widget implements `Bootstrap Datepicker v1.6.4 <https://github.com/uxsolutions/bootstrap-datepicker>`__ to display date-pickers with Bootstrap 3 or Bootstrap 4. It has been tested in django version 1.8, 1.10, 1.11 and 2.0.4.

|  |datepicker-image|

Install
-------

::

    pip install django-bootstrap-datepicker-plus

Add jQuery
----------

``jQuery`` is needed for the ``datepicker`` to render, make sure you have jQuery in your template, or you can enable Bootstraps included ``jQuery`` by setting ``include_jquery`` option to ``True`` in your ``settings.py``.

settings.py
^^^^^^^^^^^

.. code:: python

    BOOTSTRAP3 = {
        'include_jquery': True,
    }

Simple Usage
------------

forms.py
^^^^^^^^

.. code:: python

    from bootstrap_datepicker_plus import DatePickerInput
    from django import forms

    class ToDoForm(forms.Form):
        todo = forms.CharField(
            widget=forms.TextInput(attrs={"class": "form-control"}))
        date = forms.DateField(
            widget=DatePickerInput(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                }
            )
        )

The ``options`` will be passed to the JavaScript datepicker instance, and are documented and demonstrated here:

-  `Bootstrap Datepicker Documentation <https://bootstrap-datepicker.readthedocs.org/en/stable/>`__ (ReadTheDocs.com)
-  `Interactive Demo Sandbox of All Options <https://uxsolutions.github.io/bootstrap-datepicker/>`__

You don't need to set the ``language`` option, because it will be set the current language of the thread automatically.

template.html
^^^^^^^^^^^^^

.. code:: html

    <!DOCTYPE html>
    <html>
      <head>
        <link rel="stylesheet" href="{% static 'contrib/bootstrap.css' %}">
        <link rel="stylesheet" href="{% static 'contrib/font-awesome.min.css' %}">
        <script src="{% static 'contrib/bootstrap.js' %}"></script>
      </head>
      <body>
        <form method="post" role="form">
          {{ form|bootstrap }}
          {% csrf_token %}
          <div class="form-group">
            <input type="submit" value="Submit" class="btn btn-primary" />
          </div>
        </form>
      </body>
    </html>

Here we assume you're using `django-bootstrap-form <https://github.com/tzangms/django-bootstrap-form>`__ or `django-jinja-bootstrap-form <https://github.com/samuelcolvin/django-jinja-bootstrap-form>`__ but you can draw out your HTML manually.

Usage in Model Form
-------------------

forms.py
^^^^^^^^

.. code:: python

    from bootstrap_datepicker_plus import DatePickerInput
    from django import forms

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'start_date', 'end_date']
            widgets = {
                'start_date': DatePickerInput(), # default date format will be used
                'end_date': DatePickerInput(options={'format':'mm/dd/yyyy'}),
            }

event.update.html
^^^^^^^^^^^^^^^^^

.. code:: html

    {% load bootstrap3 %}       {# imports bootstrap3 #}
    {% bootstrap_css %}         {# Embeds Bootstrap CSS #}
    {% bootstrap_javascript %}  {# Embeds Bootstrap JS #}

    {% block extrahead %}   {# Extra Resources Start #}
    {{ form.media }}        {# Form required JS and CSS #}
    {% endblock %}          {# Extra Resources End #}

    <form action="" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Update" />
    </form>


More Customization
------------------

You can extend the DatePickerInput to customize it further.

forms.py
^^^^^^^^

.. code:: python

    from bootstrap_datepicker_plus import DatePickerInput
    from django import forms

    class CustomizedDatePickerInput(DatePickerInput):
        def __init__(self):
            super(DatePickerInput, self).__init__(options={
                'format': 'mm/dd/yyyy',
                'autoclose': True
                })
            self.div_attrs = {'class': 'input-group date custom-class1', custom-attribute="Hi"}
            self.icon_attrs = {'class': 'fa fa-calendar fa-2 custom-class2'}

    class EventForm(forms.ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'start_date', 'end_date']
            widgets = {
                'start_date': CustomizedDatePickerInput(),
                'end_date': CustomizedDatePickerInput(),
            }

You can define custom html template for DatePickerInput to render

forms.py
^^^^^^^^

.. code:: python

    from bootstrap_datepicker_plus import DatePickerInput
    from django import forms

    class CustomizedDatePickerInput(DatePickerInput):
        def __init__(self):
            super(DatePickerInput, self).__init__(options={
                'format': 'mm/dd/yyyy',
                'autoclose': True
                })
            self.html_template = '''
                <div%(div_attrs)s>
                    <input%(input_attrs)s/>
                    <span class="input-group-addon">
                        <span%(icon_attrs)s></span>
                    </span>
                </div>'''


Requirements
------------

-  Python >= 3.3
-  Django >= 1.8
-  Bootstrap >= 3
-  jquery >= 1.7.1

This project has been originally forked from `pbucher/django-bootstrap-datepicker <https://github.com/pbucher/django-bootstrap-datepicker>`__.


.. |datepicker-image| image:: https://bootstrap-datepicker.readthedocs.io/en/latest/_images/demo_head.png
    :alt: Datepickers
    :height: 306px

.. |ci-status| image:: https://travis-ci.org/monim67/django-bootstrap-datepicker-plus.svg?branch=master
    :target: https://travis-ci.org/monim67/django-bootstrap-datepicker-plus
    :alt: Build Status
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
