#!/usr/bin/env python
import rest_framework
from graphene_django.views import GraphQLView
from rest_framework.decorators import api_view


class DRFAuthenticatedGraphQLView(GraphQLView):
    def parse_body(self, request):
        if isinstance(request, rest_framework.request.Request):
            return request.data

        return super(DRFAuthenticatedGraphQLView, self).parse_body(request)

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(DRFAuthenticatedGraphQLView, cls).as_view(*args, **kwargs)
        view = api_view(['GET', 'POST'])(view)
        return view
