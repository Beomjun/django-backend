#!/usr/bin/env python
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from backend.common.models import UUIDModel


class User(AbstractUser, UUIDModel):
    last_accessed = models.DateTimeField(_('Last Accessed'), default=now)

    class Meta:
        verbose_name_plural = 'Users'
