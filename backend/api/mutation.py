#!/usr/bin/env python
import importlib
import os
from inspect import getmembers, isclass

from graphene import ObjectType


# Reference: https://github.com/graphql-python/graphene/issues/545#issuecomment-329630141
class MutationAbstract(ObjectType):
    pass


mutations_base_classes = [MutationAbstract]
current_directory = os.path.dirname(os.path.abspath(__file__))
search_directory = os.path.dirname(current_directory)
current_module = search_directory.split("/")[-1]
exclude_directories = [current_module, "__pycache__", "templates", "media", "static"]
subdirectories = [
    x
    for x in os.listdir(search_directory)
    if os.path.isdir(os.path.join(search_directory, x)) and x not in exclude_directories
]
for directory in subdirectories:
    try:
        module = importlib.import_module(f"{current_module}.{directory}.mutations")
        if module:
            classes = [x for x in getmembers(module, isclass)]
            queries = [x[1] for x in classes if "Mutation" in x[0]]
            mutations_base_classes += queries
    except ModuleNotFoundError:
        pass

mutations_base_classes = mutations_base_classes[::-1]
properties = {}
for base_class in mutations_base_classes:
    properties.update(base_class.__dict__["_meta"].fields)

Mutations = (
    type("Mutations", tuple(mutations_base_classes), properties)
    if len(mutations_base_classes) > 1
    else None
)
