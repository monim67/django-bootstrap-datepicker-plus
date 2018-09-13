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

``jQuery`` is needed for ``datepicker`` to render, make sure you have jQuery in your template,
or you can use ``jQuery`` included with ``Bootstrap`` by setting ``include_jquery`` option to ``True``
in your ``settings.py`` file.
If you don't have ``BOOTSTRAP3``/``BOOTSTRAP4`` settings block you have to create one.

.. code:: python

    # Use BOOTSTRAP3 if you are using Bootstrap 3
    BOOTSTRAP4 = {
        'include_jquery': True,
    }

Make sure you have bootstrap tags in your template along with ``forms.media`` tag,
it adds all JS and CSS resources needed to render the date-picker.

.. code:: html

    {% load bootstrap4 %}       {# import bootstrap4/bootstrap3 #}
    {% bootstrap_css %}         {# Embed Bootstrap CSS #}
    {% bootstrap_javascript jquery='full' %}  {# Embed Bootstrap JS+jQuery #}
    {{ form.media }}            {# Adds date-picker required JS and CSS #}

The ``form.media`` tag is only for Generic Views. If you are generating the view yourself
and passing the form to ``render`` function, you have to use ``<your-form-variable>.media``.
For Example, in case of the following example you have to use ``{{ my_form.media }}``
instead of ``{{ form.media }}``.

.. code:: python

    # File: views.py
    from django.shortcuts import render
    from .forms import UserForm

    def create_user(request):
        user_form = UserForm()
        return render(request, 'my_template.html', {'my_form': user_form})
