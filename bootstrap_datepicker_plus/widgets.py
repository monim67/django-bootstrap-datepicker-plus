# -*- coding: utf-8 -*-
# http://bootstrap-datepicker.readthedocs.org/en/stable/options.html#format
# http://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

from json import dumps as json_dumps

from django.forms.utils import flatatt
from django.forms.widgets import DateTimeInput
from django.utils import translation, formats
from django.utils.encoding import force_text
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe


class DatePickerMedia:

    lang_map = {
        'en-au': 'en-AU',
        'en-gb': 'en-GB',
        'en-us': 'en-us',
        'fr-CH': 'fr-CH',
        'it-ch': 'it-CH',
        'nl-be': 'nl-BE',
        'pt-br': 'pt-BR',
        'rs-latin': 'rs-latin',
        'sr-latin': 'sr-latin',
        'zh-cn': 'zh-CN',
        'zh-tw': 'zh-TW',
    }

    @staticmethod
    def css():
        return {'all': ('css/bootstrap-datepicker3.standalone.min.css',), }

    @staticmethod
    def js():
        scripts = ['js/bootstrap-datepicker.min.js']
        lang = translation.get_language()
        if lang:
            lang = lang.lower()
            if len(lang) > 2:
                lang = DatePickerMedia.lang_map.get(lang, 'en-us')
            if lang not in ('en', 'en-us'):
                scripts.append(
                    'js/locales/bootstrap-datepicker.%s.min.js' % (lang))
        return scripts


class DatePickerInput(DateTimeInput):

    class Media:
        js = DatePickerMedia.js()
        css = DatePickerMedia.css()

    format_map = (
        ('dd', r'%d'),
        ('DD', r'%A'),
        ('D', r'%a'),
        ('MM', r'%B'),
        ('M', r'%b'),
        ('mm', r'%m'),
        ('yyyy', r'%Y'),
        ('yy', r'%y'),
    )

    html_template = '''
        <div%(div_attrs)s>
            <input%(input_attrs)s/>
            <span class="input-group-addon">
                <span%(icon_attrs)s></span>
            </span>
        </div>'''

    js_template = '''
        <script>
            (function(window) {
                var callback = function() {
                    $(function(){$("input#%(picker_id)s:not([readonly],[disabled])").datepicker(%(options)s);});
                };
                if(window.addEventListener)
                    window.addEventListener("load", callback, false);
                else if (window.attachEvent)
                    window.attachEvent("onload", callback);
                else window.onload = callback;
            })(window);
        </script>'''

    @classmethod
    def convert_datetime_format_py2js(cls, format):
        for js, py in cls.format_map:
            format = format.replace(py, js)
        return format

    @classmethod
    def convert_datetime_format_js2py(cls, format):
        for js, py in cls.format_map:
            format = format.replace(js, py)
        return format

    def __init__(self, attrs={}, format='%Y-%m-%d', options={}):
        self.div_attrs = {'class': 'input-group date'}
        self.icon_attrs = {'class': 'fa fa-calendar fa-2'}
        self.options = options.copy()
        # Override format by options['format']
        if self.options.get('format'):
            format = self.convert_datetime_format_js2py(
                self.options.get('format'))
        if format not in formats.get_format(self.format_key):
            raise ValueError(
                'DateFormat %s is not supported by django' % format)
        # Add form-control class to input
        if 'class' not in attrs:
            attrs['class'] = 'form-control'
        # Initialize
        super(DatePickerInput, self).__init__(attrs, format)
        # Add format to options if not exists
        if not self.options.get('format') and not self.attrs.get('date-format'):
            self.options['format'] = self.convert_datetime_format_py2js(format)

    def render(self, name, value='', attrs={}):
        # Format input id, value and attributes
        input_attrs = {**attrs, 'name': name, 'type': self.input_type}
        if value != '':
            input_attrs['value'] = force_text(
                formats.localize_input(value, self.format))
        # Escape attributes
        input_attrs = {key: conditional_escape(
            val) for key, val in input_attrs.items()}
        div_attrs = {key: conditional_escape(
            val) for key, val in self.div_attrs.items()}
        icon_attrs = {key: conditional_escape(
            val) for key, val in self.icon_attrs.items()}
        # Render widget
        html = self.html_template % dict(div_attrs=flatatt(div_attrs),
                                         input_attrs=flatatt(input_attrs),
                                         icon_attrs=flatatt(icon_attrs))
        js = self.js_template % dict(
            picker_id=input_attrs.get('id'), options=json_dumps(self.options or {}))
        return mark_safe(force_text(html + js))
