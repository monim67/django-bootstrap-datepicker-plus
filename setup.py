import sys
from setuptools import setup

long_description = ''
if 'upload' in sys.argv or 'register' in sys.argv:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')

setup(
    name='django-bootstrap-datepicker',
    packages=['bootstrap_datepicker'],
    package_data={'bootstrap_datepicker': ['static/css/*.css', 
                                          'static/js/*.js',
                                          'static/js/locales/*.js',]},
    include_package_data=True,
    version='1.2.2',
    description='Bootstrap3/4 compatible datepicker for Django projects.',
    long_description=long_description,
    author='Paul Bucher',
    author_email='paulb@lctcb.org',
    url='https://github.com/pbucher/django-bootstrap-datepicker',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
