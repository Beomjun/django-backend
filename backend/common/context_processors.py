#!/usr/bin/env python
from django.conf import settings
from django.utils.translation import gettext_lazy as _


def project_config(context) -> dict:  # noqa pylint: disable=unused-argument
    return {
        "DEBUG": settings.DEBUG,
        "ENVIRONMENT_NAME": _(settings.ENVIRONMENT_NAME),
        "ENVIRONMENT_COLOR": settings.ENVIRONMENT_COLOR,
    }
