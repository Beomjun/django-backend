#!/usr/bin/env python
from config.settings.base import *  # noqa pylint: disable=wildcard-import, unused-wildcard-import

SECRET_KEY = env('DJANGO_SECRET_KEY')

# Custom
ENVIRONMENT_NAME = 'PRODUCTION'
ENVIRONMENT_COLOR = 'red'
