#!/usr/bin/env python
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),

    path('', include('backend.api.urls', namespace='graphql')),
]

if settings.DEBUG:
    if 'rosetta' in settings.INSTALLED_APPS:
        urlpatterns += [
            path('rosetta/', include('rosetta.urls')),
        ]
