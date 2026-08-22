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

.. _configure_template:

********************
Configure template
********************

The widget requires ``jQuery``, Bootstrap JS/CSS, and ``{{ form.media }}`` in your template.
The calendar will silently not appear if ``{{ form.media }}`` is missing.

.. tip:: Tip for advanced users: For better page performance, use ``{{ form.media.css }}`` in ``<head>`` and ``{{ form.media.js }}`` just before ``</body>``.

**Option A — Plain Bootstrap (CDN/Self hosted)**

If you include Bootstrap without using any python package, load jQuery and Bootstrap dependencies in head manually.
Feel free to use your own version of jQuery and Bootstrap JS/CSS.

.. code:: html

    <!-- File: example-template.html -->
    <!DOCTYPE html>
    <html>
    <head>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5/dist/css/bootstrap.min.css">
      <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5/dist/js/bootstrap.bundle.min.js"></script>
    </head>
    <body>
      <form method="post">
        {% csrf_token %}
        {{ form.media }}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Save</button>
      </form>
    </body>
    </html>

**Option B — django-bootstrap5 / django-bootstrap4 / django-bootstrap3**

Install the package for your Bootstrap version:

.. code:: bash

    pip install django-bootstrap5   # or django-bootstrap4  or  django-bootstrap3

Add to ``INSTALLED_APPS``:

.. code:: python

    # Using Bootstrap 5
    INSTALLED_APPS = [
        # Add the following to existing apps
        "django_bootstrap5",
        "bootstrap_datepicker_plus",
    ]

    # or Bootstrap 4
    INSTALLED_APPS = [
        # Add the following to existing apps
        "bootstrap4",
        "bootstrap_datepicker_plus",
    ]

    # or Bootstrap 3
    INSTALLED_APPS = [
        # Add the following to existing apps
        "bootstrap3",
        "bootstrap_datepicker_plus",
    ]

Render form using Bootstrap 5, use jQuery version of your choice:

.. code:: html

    <!DOCTYPE html>
    {% load django_bootstrap5 %}
    <html lang="en">
    <head>
      {% bootstrap_css %}
      {% bootstrap_javascript %}
      <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    </head>
    <body>
      <form method="post">
        {% csrf_token %}
        {{ form.media }}
        {% bootstrap_form form %}
        <button type="submit" class="btn btn-primary">Save</button>
      </form>
    </body>
    </html>


Or render form using Bootstrap 4:

.. code:: html

    <!DOCTYPE html>
    {% load bootstrap4 %}
    <html lang="en">
    <head>
      {% bootstrap_css %}
      {% bootstrap_javascript jquery='full' %}
    </head>
    <body>
      <form method="post">
        {% csrf_token %}
        {{ form.media }}
        {% bootstrap_form form %}
        {% buttons %}
        <button type="submit" class="btn btn-primary">Save</button>
        {% endbuttons %}
      </form>
    </body>
    </html>


Or render form using Bootstrap 3:

.. code:: html

    <!DOCTYPE html>
    {% load bootstrap3 %}
    <html lang="en">
    <head>
      {% bootstrap_css %}
      {% bootstrap_javascript jquery='full' %}
    </head>
    <body>
      <form method="post">
        {% csrf_token %}
        {{ form.media }}
        {% bootstrap_form form %}
        {% buttons %}
        <button type="submit" class="btn btn-primary">Save</button>
        {% endbuttons %}
      </form>
    </body>
    </html>

If you are using django-crispy-forms use ``crispy`` filter to render form fields instead.

.. code:: html

    <form method="post">
      {% csrf_token %}
      {{ form.media }}
      {{ form | crispy }}
      <button type="submit" class="btn btn-primary">Save</button>
    </form>

Alternatively you can use ``{% crispy %}`` tag to render entire form.
Note: ``{% crispy form %}`` automatically loads form media along with the form, so you don't need to include ``{{ form.media }}`` in your template.
So the equivalent template code for the above form would be:

.. code:: html

    {% crispy form %}


Then head over to Usage page to see how to use it in forms and views.


********************
Quirks
********************

Formsets: use ``formset.media``, not the media of individual forms
====================================================================

Django's ``BaseFormSet`` has its own ``.media`` property that aggregates widget assets across all its forms.
Use it once (outside the loop) rather than emitting media inside the loop for each form. In Django's ``FormView``
the formset is available as ``form`` in template context:

.. code:: html

    {{ form.media }}
    {% for formset in form %}
      {% bootstrap_form formset %}
    {% endfor %}

See the `formset template in the demo app <https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master/dev/myapp/templates/myapp/bootstrap5/custom-formset.html>`_.


Modal forms: place ``form.media`` on the parent page
=====================================================

When the form is loaded dynamically into a modal (e.g. via AJAX with
`django-bootstrap-modal-forms <https://github.com/trco/django-bootstrap-modal-forms>`_), the page ``<head>`` has
already been parsed when the modal content arrives. Any ``{{ form.media }}`` inside the modal template will not
load the widget JS/CSS. Include ``{{ form.media }}`` on the **parent page** instead (before the modal is
triggered).

See the `modal index template in the demo app <https://github.com/monim67/django-bootstrap-datepicker-plus/blob/master/dev/myapp/templates/myapp/bootstrap5/modal-form-index.html>`_
for a working example.


Multiple forms on the same page: call ``media`` for each form
=============================================================

When a template renders more than one form, call ``{{ form.media }}`` (or the equivalent variable name)
for each form individually. Widget assets from a form are only emitted when that form's ``.media`` is rendered.

.. code:: html

    {{ form1.media }}
    {{ form2.media }}
    <form method="post">{% csrf_token %}{{ form1.as_p }}</form>
    <form method="post">{% csrf_token %}{{ form2.as_p }}</form>
