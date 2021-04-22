#!/usr/bin/env python
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

app_name = 'api'
urlpatterns = [
    path('gql/', csrf_exempt(GraphQLView.as_view(graphiql=False))),
]
