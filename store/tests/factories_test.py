import factory
import factory.fuzzy
from factory.django import DjangoModelFactory

from store.models import Category, Product
from user.tests.factories_test import BaseUserFactory


class CategoryFactory:
    class Base(DjangoModelFactory):
        class Meta:
            model = Category

        name = factory.Faker("name")
        slug = factory.Faker("slug")
        images = factory.Faker("file_path", category="image")
        # parent_category = fuzzy.FuzzyChoice(Category.objects.all())

    # Define a custom class method to create multiple instances of the factory  #p2


class ProductFactory:
    class Base(DjangoModelFactory):
        class Meta:
            model = Product

        name = factory.Faker("name")
        slug = factory.Faker("slug")
        thumbnail = factory.Faker("file_path", category="image")
        created_by = factory.SubFactory(BaseUserFactory.Base)
        category = factory.SubFactory(CategoryFactory.Base)
        description = factory.Faker("text")
