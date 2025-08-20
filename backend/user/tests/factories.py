#!/usr/bin/env python
import factory
from django.contrib.auth import get_user_model
from faker import Faker

User = get_user_model()
fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    is_active = True
    username = factory.LazyFunction(fake.slug)
    password = factory.PostGenerationMethodCall("set_password", "password")
    email = factory.Faker("email")
    first_name = factory.Faker("name")
    last_name = factory.Faker("name")

    class Meta:
        model = User
