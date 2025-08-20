#!/usr/bin/env python
from django.conf import settings
from graphene_django.utils.testing import GraphQLTestCase
from rest_framework.test import APIClient

from backend.api.schema import schema


class CustomGraphQLTestCase(GraphQLTestCase):
    GRAPHQL_URL = f"{settings.API_URL}/gql/"
    GRAPHQL_SCHEMA = schema

    def query_with_auth(
        self,
        query,
        user,
        token,
        op_name=None,
        input_data=None,
        variables=None,
        headers=None,
    ):
        body = {"query": query}
        if op_name:
            body["operationName"] = op_name
        if variables:
            body["variables"] = variables
        if input_data:
            if variables in body:
                body["variables"]["input"] = input_data
            else:
                body["variables"] = {"input": input_data}

        client = APIClient()
        client.force_authenticate(user=user, token=token)
        if headers:
            resp = client.post(self.GRAPHQL_URL, body, format="json", **headers)
        else:
            resp = client.post(self.GRAPHQL_URL, body, format="json")

        return resp
