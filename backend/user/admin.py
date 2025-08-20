#!/usr/bin/env python
from django.contrib import admin

from backend.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("password", "date_joined", "last_accessed")
