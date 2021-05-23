#!/usr/bin/env python
from config.settings.base import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_NAME', default='db'),
        'USER': env('POSTGRES_USER', default='db'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='password'),
        'HOST': env('POSTGRES_HOST', default='postgres'),
        'PORT': env('POSTGRES_PORT', default=5432),
        'TEST': {
            'NAME': 'test_db'
        }
    }
}

# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
