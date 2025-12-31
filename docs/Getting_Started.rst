####################
Getting Started
####################


********************
Prerequisites
********************

- Python >= 3.10
- Django >= 2.0
- Bootstrap >= 3
- jquery >= 1.7.1


********************
Install
********************

Install the PyPI package via pip

::

    pip install django-bootstrap-datepicker-plus

Add ``bootstrap_datepicker_plus`` to the list of ``INSTALLED_APPS`` in your ``settings.py`` file.

.. code:: python

    INSTALLED_APPS = [
        # Add the following
        "bootstrap_datepicker_plus",
    ]


********************
Configure template
********************

The following step requires ``jQuery`` and Bootstrap JS/CSS files to be present in your template.
You can also use django-bootstrap3, django-bootstrap4, django-bootstrap5 or django-crispy-forms to
render the form.

.. code:: html

    <!-- File: example-template.html -->
    {{ form.media }}  {# Adds widget's JS/CSS files from CDN #}
    <form method="post">
      {% csrf_token %}
      {% bootstrap_form form %}  {# Renders form fields using django-bootstrapX #}
    </form>

If you are using django-crispy-forms use ``crispy`` filter to render form fields instead.

.. code:: html

    <!-- File: example-template.html -->
    {{ form.media }}  {# Adds widget's JS/CSS files from CDN #}
    <form method="post">
      {% csrf_token %}
      {{ form | crispy }}  {# Renders form fields #}
    </form>

Alternatively you can use ``{% crispy %}`` tag to render entire form.

.. code:: html

    <!-- File: example-template.html -->
    {% crispy form %} {# Adds widget's JS/CSS files from CDN and renders the form #}


Then head over to Usage page to see how to use it in forms and views.
