from collections.abc import Sequence
from typing import Any

from factory import Faker, post_generation
from factory.django import DjangoModelFactory

from user.models import BaseUser


class BaseUserFactory:
    class Base(DjangoModelFactory):
        # Define Faker providers for generating fake data
        email = Faker("email")  # Generate a fake email address
        username = Faker("user_name")  # Generate a fake username
        firstname = Faker("first_name")  # Generate a fake first name

        # Define a post-generation hook to handle password generation
        @post_generation
        def password(self, create: bool, extracted: Sequence[Any], **kwargs):
            # Generate a password if not provided explicitly
            password = (
                extracted
                if extracted
                else Faker(
                    "password", length=42, special_chars=True, digit=True, upper_case=True, lower_case=True
                ).evaluate(None, None, extra={"locale": None})
            )
            # Set the generated password for the instance
            self.set_password(password)

        class Meta:
            model = BaseUser  # Specify the model associated with the factory

        @classmethod
        def generate_unique_email(cls):
            return Faker("email").generate({})

        @classmethod
        def generate_unique_username(cls):
            return Faker("user_name").generate({})
