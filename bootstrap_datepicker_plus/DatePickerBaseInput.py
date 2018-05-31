# -*- coding: utf-8 -*-
from json import dumps as json_dumps


class DatePickerDictionary:
    _i = 0
    items = dict()

    @classmethod
    def generate_id(cls):
        cls._i += 1
        return 'dp_%s' % cls._i

    @staticmethod
    def get_base_input(test=False):
        from django.forms.widgets import DateTimeBaseInput
        if 'get_context' in dir(DateTimeBaseInput) and not test:
            # django version 1.11 and above
            return DateTimeBaseInput
        else:
            # django version below 1.11
            from .DateTimeBaseInputEx import DateTimeBaseInputEx
            return DateTimeBaseInputEx


class DatePickerBaseInput(DatePickerDictionary.get_base_input()):
    template_name = 'bootstrap_datepicker_plus/date-picker.html'
    picker_type = 'DATE'
    format = '%m/%d/%Y'
    config = {}
    _default_config = {
        'id': None,
        'picker_type': None,
        'linked_to': None,
        'options': {}  # final merged options
    }
    options = {}  # options extended by user
    options_parameter = {}  # options passed as parameter
    _default_options = {
        'showClose': True,
        'showClear': True,
        'showTodayButton': True,
    }

    # source: https://github.com/tutorcruncher/django-bootstrap3-datetimepicker/blob/master/bootstrap3_datetime/widgets.py
    format_map = (
        ('DDD', r'%j'),
        ('DD', r'%d'),
        ('MMMM', r'%B'),
        ('MMM', r'%b'),
        ('MM', r'%m'),
        ('YYYY', r'%Y'),
        ('YY', r'%y'),
        ('HH', r'%H'),
        ('hh', r'%I'),
        ('mm', r'%M'),
        ('ss', r'%S'),
        ('a', r'%p'),
        ('ZZ', r'%z'),
    )

    class Media:
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.9.0/moment-with-locales.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/js/bootstrap-datetimepicker.min.js',
            'bootstrap_datepicker_plus/js/datepicker-widget.js'
        )
        css = {'all': (
            'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datetimepicker/4.17.47/css/bootstrap-datetimepicker.css',
            'bootstrap_datepicker_plus/css/datepicker-widget.css'
        ), }

    @classmethod
    def format_py2js(cls, format):
        ''' convert python datetime format to moment format '''
        for js, py in cls.format_map:
            format = format.replace(py, js)
        return format

    @classmethod
    def format_js2py(cls, format):
        ''' convert moment format to python datetime format '''
        for js, py in cls.format_map:
            format = format.replace(js, py)
        return format

    def __init__(self, attrs={}, format=None, options={}):
        self.config = self._default_config.copy()
        self.config['id'] = DatePickerDictionary.generate_id()
        self.config['picker_type'] = self.picker_type
        self.config['options'] = self._calculate_options(options)
        # Configure Format
        if format is None:
            format = self.format
        if self.config['options'].get('format'):
            format = self.format_js2py(self.config['options'].get('format'))
        else:
            self.config['options']['format'] = self.format_py2js(format)
        # Initilize
        if 'class' not in attrs:
            attrs['class'] = 'form-control'
        super(DatePickerBaseInput, self).__init__(attrs, format)

    def _calculate_options(self, options):
        self.options_parameter = options
        _options = self._default_options.copy()
        _options.update(self.options)
        _options.update(self.options_parameter)
        return _options

    def get_context(self, name, value, attrs):
        context = super(DatePickerBaseInput, self).get_context(
            name, value, attrs)
        context['widget']['attrs']['dp_config'] = json_dumps(self.config)
        return context

    def start_of(self, event_id):
        '''
        Set Datepicker as the start-date of a date-range

        event_id => a user-defined unique string to identify the date-range
        '''
        DatePickerDictionary.items[str(event_id)] = self
        return self

    def end_of(self, event_id):
        '''
        Set Datepicker as the end-date of a date-range

        event_id => a user-defined unique string to identify the date-range
        '''
        event_id = str(event_id)
        if event_id in DatePickerDictionary.items:
            linked_picker = DatePickerDictionary.items[event_id]
            self.config['linked_to'] = linked_picker.config['id']
            self.config['options'].update(linked_picker.config['options'])
            if self.options_parameter:
                self.config['options'].update(self.options_parameter)
            # Important! See https://github.com/Eonasdan/bootstrap-datetimepicker/issues/1075
            self.config['options']['useCurrent'] = False
            self._link_to(linked_picker)
        else:
            raise KeyError(
                'start-date not specified for event_id "%s"' % event_id)
        return self

    def _link_to(self, linked_picker):
        ...
