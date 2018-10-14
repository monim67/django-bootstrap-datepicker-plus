TroubleShooting
---------------


If the date-picker calendar does not show up, possibility is you missed something of the installation procedure.
Check out the following errors and you might find your solution.

Errors displayed on browser screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. error:: TemplateSyntaxError: bootstrap3/4 is not a registered tag library.

This means you did not install django-bootstrap3 and add it to the list of INSTALLED_APPS. Checkout our
`configuration instructions <configuration_page_>`_ to see how to do it.

.. error:: TemplateDoesNotExist bootstrap_datepicker_plus/date-picker.html

This means you did not install django-bootstrap-datepicker-plus and add it to the list of INSTALLED_APPS.
Checkout our `configuration instructions <configuration_page_>`_ to see how to do it.

.. error:: TemplateSyntaxError: Invalid block tag 'bootstrap_form'.

You have not loaded bootstrap3/bootstrap4 tag. Checkout our
`configuration instructions <configuration_page_>`_ to see how to do it.

Errors displayed on browser console
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sometimes the page loads just fine, but errors are logged into browser's developer console.

.. error:: Uncaught TypeError: Cannot read property 'fn' of undefined
.. error:: Uncaught Error: Bootstrap's JavaScript requires jQuery
.. error:: Uncaught ReferenceError: jQuery is not defined
.. error:: Uncaught bootstrap-datetimepicker requires jQuery to be loaded first

The above errors are listed in the console if you forget to add jQuery to your template. Bootstrap's
JavaScript should be preceded by jQuery, otherwise Bootstrap will throw an error. Checkout our
`configuration instructions <configuration_page_>`_ to see various options to do it.

.. error:: Uncaught TypeError: Cannot read property 'Constructor' of undefined

You forgot to add bootstrap JavaScript file to your template, make sure you have both Bootstrap JavasScript
and CSS files to your included in your template. Checkout our `configuration instructions <configuration_page_>`_
to see various options to do it.

No errors anywhere, but the calendar does not show up!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You forgot to add ``{{ form.media }}`` to your template. Checkout our `configuration instructions <configuration_page_>`_
to learn more about this issue.

My error is not listed here
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Please `create an issue <create_issue_page_>`_ on the project's GitHub repository providing as much information
you can.


.. _create_issue_page: https://github.com/monim67/django-bootstrap-datepicker-plus/issues/new/choose
.. _configuration_page: https://monim67.github.io/django-bootstrap-datepicker-plus/configure/
