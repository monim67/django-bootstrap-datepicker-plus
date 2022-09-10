# Contributing to this Project

Any contributions to this repository in the form of bug reports, bug fix, suggestions and feature requests
are warmly welcomed as long as it does not hamper the tests and coverage report.


## Getting Started

Follow the following steps to get started contributing to this project.

 1. Fork the repository on GitHub.
 2. Clone your fork locally:

        git clone https://github.com/your_username_here/django-bootstrap-datepicker-plus.git
        cd django-bootstrap-datepicker-plus
        git checkout -b name-of-your-bugfix-or-feature

 3. Create a virtual environment of your choice and activate it.
 4. Install the dependencies via poetry and activate poetry virtual environment.

        poetry install
        poetry shell

 5. Run the migrations for django application.

        python dev/manage.py migrate

 6. Press F5 if you are using vscode to start the application debugger.
 7. Otherwise you can run the django application on localhost:8000 to see the changes you make in action real-time.

        python dev/manage.py runserver


## Testing

 1. Run the tests by the following command.

        pytest

 2. See the coverage report by the following command.

        poe coverage

