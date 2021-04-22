#!/usr/bin/env python
from config.settings.base import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = True

SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-##stcz7(83r6hztg-p)7b^%&c55kzq^p6xaueu6ckb9283_eu%')

INSTALLED_APPS += [
    'django_extensions',
    'rosetta',
]
