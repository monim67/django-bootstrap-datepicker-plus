####################
Customization
####################

******************************
Customize All Inputs
******************************

To customize the look and features copy the settings block below
to your ``settings.py`` file and uncomment the options you want to change.

.. code:: python

    BOOTSTRAP_DATEPICKER_PLUS = {
        # Options applied to all widgets. Full list: https://getdatepicker.com/4/Options/
        # "options": {
        #     "locale": "bn",
        # },
        #
        # Override options for a specific picker variant only (it overrides "options" above)
        # "variant_options": {
        #     "date": {
        #         "format": "MM/DD/YYYY",
        #     },
        #     "datetime": {
        #         "format": "MM/DD/YYYY HH:mm",
        #     },
        #     "time": {
        #         "format": "HH:mm",
        #     },
        # },
        #
        # HTML attributes for the widget <input> element
        # "attrs": {
        #     "class": "my-input-class",
        # },
        #
        # Override the calendar icon for a specific variant
        # "addon_icon_classes": {
        #     "month": "bi-calendar-month",
        # },
        #
        # Use a custom HTML template for the input widget
        # detailed here https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/Template_Customizing.html
        # "template_name": "your-app/custom-input.html",
        #
        # Advanced: Override CDN URLs for the datepicker JS/CSS/moment.js.
        # defaults: https://github.com/monim67/django-bootstrap-datepicker-plus/blob/6.0.0/src/bootstrap_datepicker_plus/settings.py#L55-L69
        # Set to None if you already include those files in your template.
        # "datetimepicker_js_url": "https://...",
        # "datetimepicker_css_url": "https://...",
        # "momentjs_url": None,
        # "bootstrap_icon_css_url": None,
        #
        # Advanced: To serve static files from Django's staticfiles instead of a CDN
        # (e.g. for GDPR / offline / compliance requirements), download the JS/CSS
        # files into a static directory, update the URLs above, and set:
        # Note: you will be responsible for static file deployment in production
        # including collecting django static files and serving them from your web server.
        # "app_static_url": "bootstrap_datepicker_plus/",
    }

.. note::

    The ``format`` option controls the **display format** shown to the user only.
    The widget always submits values to Django in a fixed backend format, so
    ``input_formats`` on the form field is not required regardless of what ``format`` is set to.


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
                # "allowInputToggle": True,                      # open picker on input click, not just the icon
                # "minDate": "today",                              # disable past dates
                # "maxDate": "2099-12-31",                        # disable future dates
                # "disabledDates": ["2024-12-25", "2025-01-01"], # block specific dates
                # "enabledDates": ["2024-12-20", "2024-12-21"],  # allow only these dates
            },
        ))

To control the **width** of a picker input, wrap the field in a Bootstrap grid column rather than setting a fixed
width on the input itself — the calendar icon is part of a Bootstrap input-group and won't follow the input's width alone.

.. code:: html

    <div class="row">
      <div class="col-md-4">
        {{ form.deadline_date }}
      </div>
    </div>

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

