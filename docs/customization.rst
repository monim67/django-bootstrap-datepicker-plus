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


JavaScript events and some options can only be set using JavaScript. Starting from v5.0, you can set events and options
globally for all widgets like below in your html template inside a ``<script>`` tag.

.. code:: javascript

    window.dbdpOptions = {
        widgetParent: jQuery("#myWidgetParent"),
    }
    window.dbdpEvents = {
        "dp.change": e => console.log("Date selected:", e.date, e.oldDate),
        "dp.show": e => console.log("Calendar opened"),
        "dp.hide": e => console.log("Calendar closed", e.date),
        "dp.error": e => console.log("Invalid date input", e.date, e.oldDate),
        "dp.update": e => console.log("viewDate changed", e.viewDate, e.change),
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

JavaScript events and some options can only be set using JavaScript. Starting from v5.0, you can set events and options
for a specific widget for a widget with field name ``deadline_date`` like below in your html template inside a ``<script>`` tag.

.. code:: javascript

    // Applies to a widget with field name `deadline_date`
    window.dbdpOptions_deadline_date = {
        widgetParent: jQuery("#myWidgetParent"),
    }
    window.dbdpEvents_deadline_date = {
        "dp.change": (e) => console.log("Deadline changed:", e.date?.format('YYYY-MM-DD')),
        "dp.show": e => console.log("Deadline picker opened"),
        "dp.hide": e => console.log("Deadline picker closed", e.date),
        "dp.error": e => console.log("Invalid date input", e.date, e.oldDate),
        "dp.update": e => console.log("viewDate changed", e.viewDate, e.change),
    }


.. _settings_block: https://github.com/monim67/django-bootstrap-datepicker-plus/blob/5.0.0/dev/mysite/settings.py#L140-L250
