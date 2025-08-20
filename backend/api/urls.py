#!/usr/bin/env python
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from backend.api.schema import schema
from backend.api.views import DRFAuthenticatedGraphQLView

app_name = "api"
urlpatterns = [
    path("gql/", csrf_exempt(DRFAuthenticatedGraphQLView.as_view(schema=schema))),
]
