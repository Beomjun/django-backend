#!/usr/bin/env python
from typing import Optional

from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from graphene import ObjectType, Field, String

from backend.user.types import UserType

User = get_user_model()


class Query(ObjectType):
    user = Field(UserType, email=String(required=True))

    @staticmethod
    def resolve_user(parent, info, email: str) -> Optional[QuerySet]:
        try:
            return User.objects.get(email=email.strip())
        except User.DoesNotExist:
            return None
