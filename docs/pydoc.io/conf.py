# -*- coding: utf-8 -*-
import os

# exec(open('docs/conf.py').read())
exec(open(os.path.abspath('../conf.py')).read())

extensions = [
    # 'sphinx.ext.autodoc',
    'autoapi.extension'
]

autoapi_type = 'python'
autoapi_dirs = ['../../bootstrap_datepicker_plus']
autoapi_options = [
    'members',
    'undoc-members',
    'private-members',
    'special-members'
]
autoapi_keep_files = False
autoapi_include_summaries = True
