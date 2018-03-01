import sys
from setuptools import setup

long_description = ''
if 'upload' in sys.argv or 'register' in sys.argv:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')

setup(
    name='django-bootstrap-datepicker-plus',
    packages=['bootstrap_datepicker'],
    package_data={
        'bootstrap_datepicker': [
            'static/css/*.css',
            'static/js/*.js',
            'static/js/locales/*.js',
        ]
    },
    install_requires=[
        'django>=1.8',
    ],
    include_package_data=True,
    version='1.0.0',
    description='Bootstrap 3/4 compatible datepicker for Django projects.',
    long_description=long_description,
    author='Munim Munna',
    author_email='monim67@yahoo.com',
    url='https://github.com/monim67/django-bootstrap-datepicker',
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
