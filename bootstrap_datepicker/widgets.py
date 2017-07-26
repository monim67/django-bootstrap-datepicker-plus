# -*- coding: utf-8 -*-
from json import dumps as json_dumps

from django.forms.utils import flatatt
from django.forms.widgets import DateTimeInput
from django.utils.safestring import mark_safe
from django.utils import translation
from django.utils.html import conditional_escape
from django.utils.encoding import force_text


class DatePicker(DateTimeInput):
    class Media:
        class JSFiles(object):
            def __iter__(self):
                yield 'js/bootstrap-datepicker.min.js'
                lang = translation.get_language()
                if lang:
                    lang = lang.lower()
                    # There is language name that length>2 or contains uppercase.
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
                    if len(lang) > 2:
                        lang = lang_map.get(lang, 'en-us')
                    if lang not in ('en', 'en-us'):
                        yield 'js/locales/bootstrap-datepicker.%s.min.js' % (lang)

        js = JSFiles()
        css = {'all': ('css/bootstrap-datepicker3.standalone.min.css',), }
    # http://bootstrap-datepicker.readthedocs.org/en/stable/options.html#format
    # http://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

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

    @classmethod
    def conv_datetime_format_py2js(cls, format):
        for js, py in cls.format_map:
            format = format.replace(py, js)
        return format

    @classmethod
    def conv_datetime_format_js2py(cls, format):
        for js, py in cls.format_map:
            format = format.replace(js, py)
        return format

    html_template = """
    <div%(div_attrs)s>
      <input%(input_attrs)s/>
      <span class="input-group-addon">
        <span%(icon_attrs)s></span>
      </span>
    </div>"""

    js_template = '''
        <script>
            (function(window) {
                var callback = function() {
                    $(function(){$("#%(picker_id)s:has(input:not([readonly],[disabled]))").datepicker(%(options)s);});
                };
                if(window.addEventListener)
                    window.addEventListener("load", callback, false);
                else if (window.attachEvent)
                    window.attachEvent("onload", callback);
                else window.onload = callback;
            })(window);
        </script>'''

    def __init__(self, attrs=None, format=None, options=None, div_attrs=None, icon_attrs=None):
        if not icon_attrs:
            icon_attrs = {'class': 'fa fa-calendar fa-2'}
        if not div_attrs:
            div_attrs = {'class': 'input-group date'}
        if format is None and options and options.get('format'):
            format = self.conv_datetime_format_js2py(options.get('format'))
        super(DatePicker, self).__init__(attrs, format)
        if 'class' not in self.attrs:
            self.attrs['class'] = 'form-control'
        self.div_attrs = div_attrs and div_attrs.copy() or {}
        self.icon_attrs = icon_attrs and icon_attrs.copy() or {}
        self.picker_id = self.div_attrs.get('id') or None
        if options is False:  # datepicker will not be initalized when options is False
            self.options = False
        else:
            self.options = options and options.copy() or {}
            if format and not self.options.get('format') and not self.attrs.get('date-format'):
                self.options['format'] = self.conv_datetime_format_py2js(format)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        extra_attrs = dict()
        extra_attrs['type'] = self.input_type
        extra_attrs['name'] = name
        input_attrs = self.build_attrs(attrs, extra_attrs)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            input_attrs['value'] = force_text(self._format_value(value))
        input_attrs = {key: conditional_escape(val) for key, val in input_attrs.items()}
        if not self.picker_id:
            self.picker_id = (input_attrs.get('id', '') + '_pickers').replace(' ', '_')
        self.div_attrs['id'] = self.picker_id
        picker_id = conditional_escape(self.picker_id)
        div_attrs = {key: conditional_escape(val) for key, val in self.div_attrs.items()}
        icon_attrs = {key: conditional_escape(val) for key, val in self.icon_attrs.items()}
        html = self.html_template % dict(div_attrs=flatatt(div_attrs),
                                         input_attrs=flatatt(input_attrs),
                                         icon_attrs=flatatt(icon_attrs))
        if self.options:
            js = self.js_template % dict(picker_id=picker_id, options=json_dumps(self.options or {}))
        else:
            js = ''
        return mark_safe(force_text(html + js))
