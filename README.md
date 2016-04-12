# django-bootstrap3-datetimepicker

This package uses [Bootstrap datepicker widget version 1.6.1 ](https://github.com/eternicode/bootstrap-datepicker.git).

## Install

    pip install git+https://github.com/pbucher/django-bootstrap-datepicker.git

## ToDo

    General cleanup and testing

## Example

#### forms.py

```python
from bootstrap_date.widgets import DatePicker
from django import forms

  class ToDoForm(forms.Form):
      todo = forms.CharField(
          widget=forms.TextInput(attrs={"class": "form-control"}))
      date = forms.DateField(
          widget=DatePicker(options={"format": "mm/dd/yyyy"}))

```

The `options` will be passed to the JavaScript datepicker instance. 
Available `options` are explained in the following documents:

* [Online Docs](http://bootstrap-datepicker.readthedocs.org/en/stable/) (ReadTheDocs.com)

Checkout the online demo to help with exploring different options:

* [Online Demo](http://eternicode.github.io/bootstrap-datepicker/)

You don't need to set the `language` option, 
because it will be set the current language of the thread automatically.

#### template.html

```html
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
```

Here we assume you're using [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) or 
[django-jinja-bootstrap-form](https://github.com/samuelcolvin/django-jinja-bootstrap-form) but you can
draw out your HTML manually.

## Requirements

* Python >= 3.3
* Django >= 1.8
* Bootstrap == 4.0-alpha2
* font-awesome == 4.5.X
