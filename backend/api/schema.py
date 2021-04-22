#!/usr/bin/env python
from graphene import Schema

from backend.api.mutation import Mutations
from backend.api.query import Queries

schema = Schema(query=Queries, mutation=Mutations)
