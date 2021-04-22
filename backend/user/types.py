#!/usr/bin/env python
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        exclude = ('password', 'is_superuser', 'is_staff')
