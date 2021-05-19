#!/usr/bin/env python
from config.settings.base import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import

DEBUG = True

SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-##stcz7(83r6hztg-p)7b^%&c55kzq^p6xaueu6ckb9283_eu%')

INSTALLED_APPS += [
    'django_extensions',
    'rosetta',
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_NAME'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT', default=5432),
        'ATOMIC_REQUESTS': True
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['debug_toolbar', ]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
