import pytest
from django.test import TestCase

from user.models import BaseUser
from user.tests.factories import BaseUserFactory

pytestmark = pytest.mark.django_db


class TestBaseUserSerializer(TestCase):

    def test_create_user(self):
        # Use the BaseUserFactory to create a new BaseUser instance
        user = BaseUserFactory.Base()

        # Fetch the user from the database
        created_user = BaseUser.objects.get(id=user.id)

        # Assert that the user is created with the correct data
        assert created_user is not None
        assert created_user.email == user.email
        assert created_user.username == user.username
        assert created_user.firstname == user.firstname
