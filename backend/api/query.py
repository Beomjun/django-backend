#!/usr/bin/env python
import importlib
import os
from inspect import getmembers, isclass

from graphene import ObjectType


# Reference: https://github.com/graphql-python/graphene/issues/545#issuecomment-329630141
class QueriesAbstract(ObjectType):
    pass


queries_base_classes = [QueriesAbstract]
current_directory = os.path.dirname(os.path.abspath(__file__))
search_directory = os.path.dirname(current_directory)
current_module = search_directory.split('/')[-1]
exclude_directories = [current_module, '__pycache__', 'templates', 'media', 'static']
subdirectories = [
    x
    for x in os.listdir(search_directory)
    if os.path.isdir(os.path.join(search_directory, x)) and x not in exclude_directories
]
for directory in subdirectories:
    try:
        module = importlib.import_module(f'{current_module}.{directory}.queries')
        if module:
            classes = [x for x in getmembers(module, isclass)]
            queries = [x[1] for x in classes if 'Query' in x[0]]
            queries_base_classes += queries
    except ModuleNotFoundError:
        pass

base_classes = []
queries_base_classes = queries_base_classes[::-1]
properties = {}
for base_class in queries_base_classes:
    if '_meta' in base_class.__dict__ and base_class.__dict__['_meta'].fields:
        base_classes.append(base_class)
        properties.update(base_class.__dict__['_meta'].fields)

Queries = type('Queries', tuple(base_classes), properties) if len(queries_base_classes) > 1 else None
