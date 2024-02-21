import pytest
from rest_framework.test import APITestCase

from api.serializer import BaseUserSerializer
from backend.user.tests.factories_test import BaseUserFactory
from user.models import BaseUser

pytestmark = pytest.mark.django_db


class TestBaseUserSerializer(APITestCase):

    def setUp(self):
        BaseUser.objects.all().delete()

    def test_create_user(self):
        # Create a BaseUser instance using the factory
        user = BaseUserFactory.Base()

        # Create a dictionary containing the user data
        user_data = {
            "email": user.email,
            "username": user.username,
            "firstname": user.firstname,
            "password1": "password123",
            "password2": "password123",
        }

        print(user_data)

        # Initialize the serializer with the user data
        serializer = BaseUserSerializer(data=user_data)
        is_valid = serializer.is_valid()
        if not is_valid:
            print(serializer.errors)
        # Validate the serializer data
        self.assertTrue(serializer.is_valid())

        # Create the user using the serializer
        user_instance = serializer.save()

        # Fetch the user from the database
        created_user = BaseUser.objects.get(id=user_instance.id)

        # Assertions
        self.assertEqual(created_user.email, user.email)
        self.assertEqual(created_user.username, user.username)
        self.assertEqual(created_user.firstname, user.firstname)

        # Check that the password is correctly hashed
        self.assertTrue(created_user.check_password("password123"))
