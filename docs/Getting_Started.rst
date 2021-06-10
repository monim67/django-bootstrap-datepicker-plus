####################
Getting Started
####################


********************
Prerequisites
********************

- Python >= 3.6
- Django >= 1.8
- Bootstrap >= 3
- jquery >= 1.7.1


********************
Installing
********************

Install the widget via pip

::

    pip install django-bootstrap-datepicker-plus

Add ``bootstrap_datepicker_plus`` to the list of ``INSTALLED_APPS`` in your ``settings.py`` file.

.. code:: python

    INSTALLED_APPS = [
        # Add the following
        'bootstrap_datepicker_plus',
    ]

.. warning:: This installation instruction assumes you have ``jQuery`` and Bootstrap JS/CSS files present
    in your template and you are using ``form.media`` in your django template. If not you should checkout our
    `configuration instructions <https://monim67.github.io/django-bootstrap-datepicker-plus/configure/>`_
    which covers almost everything you need to get the widget running.
