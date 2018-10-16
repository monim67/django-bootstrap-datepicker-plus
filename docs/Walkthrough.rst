Quick Walkthrough Tutorial
--------------------------

This tutorial will take off where django official tutorial `Writing your first Django app, part 4 <django_tutorial_04_>`_
left off. If you don't have the project you can clone the following repository and checkout to completion of tutorial 04.

::

    git clone https://github.com/monim67/django-polls
    cd django-polls
    git checkout d2.1t4


The Question model has a datetime field. We are going to create a page to add new poll questions and a page to edit
them with a date-time-picker calendar on the datetime field.
We are going to use Bootstrap 4 here, if you are using Bootstrap 3 just replace the 4's with 3's in the codes
and instructions below.
Install following packages:

::

    pip install django-bootstrap4
    pip install django-bootstrap-datepicker-plus


Add these packages to the list of INSTALLED_APPS as you did here on `Tutorial 02 <django_tutorial_activating_model_>`_.

.. code:: python

    # FIle: mysite/settings.py
    INSTALLED_APPS = [
        'polls.apps.PollsConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "bootstrap4",
        "bootstrap_datepicker_plus",
    ]


CreateView for Question model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a CreateView for Question model. The ``get_form`` method is used to specify widgets on the form fields.

.. code:: python

    # FIle: polls/views.py
    from django.http import HttpResponseRedirect
    from django.shortcuts import get_object_or_404, render
    from django.urls import reverse
    from django.views import generic

    from bootstrap_datepicker_plus import DateTimePickerInput

    from .models import Choice, Question


    class CreateView(generic.edit.CreateView):
        model = Question
        fields = ['question_text', 'pub_date']
        def get_form(self):
            form = super().get_form()
            form.fields['pub_date'].widget = DateTimePickerInput()
            return form
    
    # Leave other classes unchanged


Create a template named question_form.html in your app to render the form. If you use a different name you have to
set template_name property of CreateView class in your views.py file above.

.. code:: html

    <!-- File: polls/templates/polls/question_form.html -->
    {% load bootstrap4 %}
    {% bootstrap_css %}
    {% bootstrap_javascript jquery='full' %}
    {{ form.media }}

    <form method="post">{% csrf_token %}
      {% bootstrap_form form %}
      <input type="submit" value="Save">
    </form>

Add a ``get_absolute_url`` method to your Question model.

.. code:: python

    # FIle: polls/models.py
    import datetime

    from django.db import models
    from django.urls import reverse
    from django.utils import timezone


    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

        def __str__(self):
            return self.question_text

        def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
        def get_absolute_url(self):
            return reverse('polls:detail', kwargs={'pk': self.pk})


Add an urlpattern for creating new poll question.

.. code:: python

    # FIle: polls/urls.py
    from django.urls import path

    from . import views

    app_name = 'polls'
    urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('create', views.CreateView.as_view(), name='create'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
    ]


Now run the developement server and visit http://localhost:8000/polls/create, if everything works fine
you can wrap up your template in proper HTML.

.. code:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
      {% load bootstrap4 %}
      {% bootstrap_css %}
      {% bootstrap_javascript jquery='full' %}
      {{ form.media }}
    </head>
    <body>
      <div class="container">
        <div class="col-md-3">
          <form method="post">{% csrf_token %}
            {% bootstrap_form form %}
            {% buttons %}
            <button type="submit" class="btn btn-primary">Save</button>
            {% endbuttons %}
          </form>
        </div>
      </div>
    </body>
    </html>


UpdateView for Question model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can now add a page to update a poll question. First we add an UpdateView to our views.

.. code:: python

    # FIle: add these to polls/views.py
    class UpdateView(generic.edit.UpdateView):
        model = Question
        fields = ['question_text', 'pub_date']
        def get_form(self):
            form = super().get_form()
            form.fields['pub_date'].widget = DateTimePickerInput()
            return form

Then add a urlpattern to access the question update page.

.. code:: python

    # FIle: polls/urls.py
    from django.urls import path

    from . import views

    app_name = 'polls'
    urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('create', views.CreateView.as_view(), name='create'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/update', views.UpdateView.as_view(), name='update'),
        path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
    ]

That's it, run the developement server and visit http://localhost:8000/polls/1/update, if everything works fine
you can checkout usage in custom form and model form in Usage page of the docs.


.. _django_tutorial_04: https://docs.djangoproject.com/en/2.1/intro/tutorial04/
.. _django_tutorial_activating_model: https://docs.djangoproject.com/en/2.1/intro/tutorial02/#activating-models
