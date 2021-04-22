#!/usr/bin/env python
import uuid

from django.db import models


class UUIDModel(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
