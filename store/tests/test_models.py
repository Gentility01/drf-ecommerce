import pytest
from django.test import TestCase

from store.models import Category, Product

from .factories import CategoryFactory, ProductFactory

pytestmark = pytest.mark.django_db


class CategoryTests(TestCase):
    def test_category_creation(self):
        category = CategoryFactory.Base()
        print(category, category.slug)

        created_category = Category.objects.get(id=category.id)
        print(created_category, created_category.slug)
        self.assertIsNotNone(category)
        self.assertIsNotNone(category.slug)
        assert created_category.slug == category.slug
        assert created_category.name == category.name
        assert created_category.images == category.images


class ProductTests(TestCase):
    def test_product_creation(self):
        product = ProductFactory.Base()

        created_product = Product.objects.get(id=product.id)

        self.assertIsNotNone(product)
        self.assertIsNotNone(product.slug)
        assert created_product.slug == product.slug
        assert created_product.name == product.name
        assert created_product.thumbnail == product.thumbnail
