# -*- coding: utf-8 -*-
"""Contains Base Date-Picker input class for widgets of this package."""

from json import dumps as json_dumps

from django.forms.widgets import DateTimeBaseInput

from ._helpers import DatePickerDictionary


class BasePickerInput(DateTimeBaseInput):
    """Base Date-Picker input class for widgets of this package."""

    template_name = "bootstrap_datepicker_plus/date-picker.html"
    picker_type = "DATE"
    format = "%m/%d/%Y"
    config = {}
    _default_config = {
        "id": None,
        "picker_type": None,
        "linked_to": None,
        "options": {},  # final merged options
    }
    options = {}  # options extended by user
    options_param = {}  # options passed as parameter
    _default_options = {
        "showClose": True,
        "showClear": True,
        "showTodayButton": True,
    }

    # source: https://github.com/tutorcruncher/django-bootstrap3-datetimepicker
    # file: /blob/31fbb09/bootstrap3_datetime/widgets.py#L33
    format_map = (
        ("DDD", r"%j"),
        ("DD", r"%d"),
        ("MMMM", r"%B"),
        ("MMM", r"%b"),
        ("MM", r"%m"),
        ("YYYY", r"%Y"),
        ("YY", r"%y"),
        ("HH", r"%H"),
        ("hh", r"%I"),
        ("mm", r"%M"),
        ("ss", r"%S"),
        ("a", r"%p"),
        ("ZZ", r"%z"),
    )

    class Media:
        """JS/CSS resources needed to render the date-picker calendar."""

        js = (
            "https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.9.0/"
            "moment-with-locales.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/"
            "4.17.47/js/bootstrap-datetimepicker.min.js",
            "bootstrap_datepicker_plus/js/datepicker-widget.js",
        )
        css = {
            "all": (
                "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/"
                "4.17.47/css/bootstrap-datetimepicker.css",
                "bootstrap_datepicker_plus/css/datepicker-widget.css",
            ),
        }

    @classmethod
    def format_py2js(cls, datetime_format):
        """Convert python datetime format to moment datetime format."""
        for js_format, py_format in cls.format_map:
            datetime_format = datetime_format.replace(py_format, js_format)
        return datetime_format

    @classmethod
    def format_js2py(cls, datetime_format):
        """Convert moment datetime format to python datetime format."""
        for js_format, py_format in cls.format_map:
            datetime_format = datetime_format.replace(js_format, py_format)
        return datetime_format

    def __init__(self, attrs=None, format=None, options=None):
        """Initialize the Date-picker widget."""
        # pylint: disable=redefined-builtin
        self.format_param = format
        self.options_param = options if options else {}
        self.config = self._default_config.copy()
        self.config["id"] = DatePickerDictionary.generate_id()
        self.config["picker_type"] = self.picker_type
        self.config["options"] = self._calculate_options()
        attrs = attrs if attrs else {}
        if "class" not in attrs:
            attrs["class"] = "form-control"
        super().__init__(attrs, self._calculate_format())

    def _calculate_options(self):
        """Calculate and Return the options."""
        _options = self._default_options.copy()
        _options.update(self.options)
        if self.options_param:
            _options.update(self.options_param)
        return _options

    def _calculate_format(self):
        """Calculate and Return the datetime format."""
        _format = self.format_param if self.format_param else self.format
        if self.config["options"].get("format"):
            _format = self.format_js2py(self.config["options"].get("format"))
        else:
            self.config["options"]["format"] = self.format_py2js(_format)
        return _format

    def get_context(self, name, value, attrs):
        """Return widget context dictionary."""
        # pylint: disable=no-member
        context = super().get_context(name, value, attrs)
        context["widget"]["attrs"]["data-dp-config"] = json_dumps(self.config)
        return context

    def start_of(self, event_id):
        """
        Set Date-Picker as the start-date of a date-range.

        Args:
            - event_id (string): User-defined unique id for linking two fields
        """
        DatePickerDictionary.items[str(event_id)] = self
        return self

    def end_of(self, event_id, import_options=True):
        """
        Set Date-Picker as the end-date of a date-range.

        Args:
            - event_id (string): User-defined unique id for linking two fields
            - import_options (bool): inherit options from start-date input,
              default: TRUE
        """
        event_id = str(event_id)
        if event_id in DatePickerDictionary.items:
            linked_picker = DatePickerDictionary.items[event_id]
            self.config["linked_to"] = linked_picker.config["id"]
            if import_options:
                backup_moment_format = self.config["options"]["format"]
                self.config["options"].update(linked_picker.config["options"])
                self.config["options"].update(self.options_param)
                if self.format_param or "format" in self.options_param:
                    self.config["options"]["format"] = backup_moment_format
                else:
                    self.format = linked_picker.format
            # Setting useCurrent is necessary, see following issue
            # https://github.com/Eonasdan/bootstrap-datetimepicker/issues/1075
            self.config["options"]["useCurrent"] = False
            self._link_to(linked_picker)
        else:
            raise KeyError('start-date not specified for event_id "%s"' % event_id)
        return self

    def _link_to(self, linked_picker):
        """
        Executed when two date-inputs are linked together.

        This method for sub-classes to override to customize the linking.
        """
