####################
Template Customizing
####################


The calendar is not yet available for customizing, but the input field template can be customized. 
First you have to create a HTML template for widget input.

.. code-block:: HTML

    <!-- File: my_app/templates/my_app/custom-input.html -->

    <h5>This is a customized input from template</h5>
    <div class="input-group dbdp">
        {% include 'django/forms/widgets/text.html' %}
        <div class="input-group-addon input-group-append input-group-text">
            <i class="{{ addon_icon_class }}"></i>
        </div>
    </div>


Then add it to BOOTSTRAP_DATEPICKER_PLUS settings.

.. code:: python

    BOOTSTRAP_DATEPICKER_PLUS = {
        "template_name": "my_app/custom-input.html",
    }
