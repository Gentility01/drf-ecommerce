import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializer import CategorySerializer
from backend.store.tests.factories_test import CategoryFactory
from store.models import Category

pytestmark = pytest.mark.django_db


class CategoryApiViewsTest(APITestCase):
    def setUp(self):
        self.url = reverse("category_list_create_api_view")

    def test_list_categories(self):
        # Create some test categories using Factory Boy
        CategoryFactory.Base()

        # Make a GET request to list categories
        response = self.client.get(self.url)

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response data matches the serialized data of the categories
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        print(response.data, "dddddddddddddddddddddddd")
        print(serializer.data, "ssssssssssssssssssssssss")
        self.assertEqual(response.data, serializer.data)
