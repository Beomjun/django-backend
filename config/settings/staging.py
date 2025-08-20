#!/usr/bin/env python
from config.settings.base import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import

SECRET_KEY = env("DJANGO_SECRET_KEY")

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_NAME"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT", default=5432),
        "ATOMIC_REQUESTS": True,
    }
}

# Custom
ENVIRONMENT_NAME = "STAGING"
ENVIRONMENT_COLOR = "orange"
