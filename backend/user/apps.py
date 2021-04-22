#!/usr/bin/env python
from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.user'
    verbose_name = 'Users'
