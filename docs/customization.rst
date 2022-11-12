####################
Customization
####################

******************************
Customize All Inputs
******************************

To customize the look and features copy the `settings block <settings_block_>`_
to your settings.py file and customize it following instruction comments.
Settings applies globally to all widgets used in your site.

.. code:: python

    # The link above contains all settings
    BOOTSTRAP_DATEPICKER_PLUS = {
        "options": {
            "locale": "bn",
        },
        "variant_options": {
            "date": {
                "format": "MM/DD/YYYY",
            },
        }
    }


You can set date and event hook options using JavaScript.

.. code:: javascript

    window.dbdpOptions = {
        widgetParent: jQuery("#myWidgetParent"),
    }
    window.dbdpEvents = {
        "dp.show": e => console.log("Calendar opened"),
    }


******************************
Customize Single Input
******************************

You should use options in settings.py file to apply to all widget instances.
If you need to customize a single widget input pass attrs and options directly
to widget instance.

.. code-block:: python
    :emphasize-lines: 9-13

    # File: forms.py
    from bootstrap_datepicker_plus.widgets import DatePickerInput
    from .models import Event
    from django import forms

    class ToDoForm(forms.Form):
        todo = forms.CharField()
        deadline_date = forms.DateField(widget=DatePickerInput(
            attrs={"class": "my-exclusive-input"},
            options={
                "format": "MM/DD/YYYY",
                "showTodayButton": False,
            },
        ))

Similarly set date and event hook options using JavaScript.

.. code:: javascript

    window.dbdpOptions_deadline_date = {
        widgetParent: jQuery("#myWidgetParent"),
    }
    window.dbdpEvents_deadline_date = {
        "dp.show": e => console.log("Calendar opened"),
    }


.. _settings_block: https://github.com/monim67/django-bootstrap-datepicker-plus/blob/5.0.0/dev/mysite/settings.py#L140-L250
