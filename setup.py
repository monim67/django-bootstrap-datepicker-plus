from setuptools import setup

import bootstrap_datepicker_plus


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="django-bootstrap-datepicker-plus",
    version=bootstrap_datepicker_plus.__version__,
    description="Bootstrap3/Bootstrap4/Bootstrap5 DatePickerInput, TimePickerInput, "
    "DateTimePickerInput, MonthPickerInput, YearPickerInput "
    "with date-range-picker functionality for django version >= 1.8",
    long_description=readme(),
    url="https://github.com/monim67/django-bootstrap-datepicker-plus",
    author="Munim Munna",
    author_email="6266677+monim67@users.noreply.github.com",
    license="Apache License 2.0",
    keywords="django bootstrap date-picker time-picker datetime-picker "
    "date-range-picker",
    packages=["bootstrap_datepicker_plus"],
    install_requires=["django>=1.8",],
    python_requires=">=3.6",
    package_data={
        "bootstrap_datepicker_plus": [
            "templates/*.html",
            "static/css/*.css",
            "static/js/*.js",
        ]
    },
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 1.10",
        "Framework :: Django :: 1.8",
    ],
)
