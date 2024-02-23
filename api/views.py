# fmt: off
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from store.models import Category, Product
from user.models import BaseUser

from .serializer import (BaseUserSerializer, CategorySerializer,
                         ProductsSerializer)


class BaseUserViewSet(ModelViewSet):  # noqa
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer

    @extend_schema(tags=["User"], summary="List base user", description="Retrieve a list of base users.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=["User"], summary="Create base user", description="Create a new base user.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=["User"], summary="Retrieve base user", description="Retrieve a specific base user by ID.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(tags=["User"], summary="Update base user", description="Update a specific base user by ID.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        tags=["User"], summary="Partial update base user", description="Partially update a specific base user by ID."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=["User"], summary="Delete base user", description="Delete a specific base user by ID.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @extend_schema(tags=["Category"], summary="List all categories", description="List all categories")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=["Category"], summary="Create category", description="Create a category")
    def create(self, request, *args, **kwargs):
        """
        Create a new category.
        """
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=["Category"], summary="Retrieve category", description="Retrieve a paticular category.")
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a category.
        """
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(tags=["Category"], summary="Update Category", description="Update a category.")
    def update(self, request, *args, **kwargs):
        """
        Update a category.
        """
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=["Category"], summary="Partial update Category", description="Update a category partially.")
    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a category.
        """
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=["Category"], summary="Delete category", description="Delete a category.")
    def destroy(self, request, *args, **kwargs):
        """
        Delete a category.
        """
        return super().destroy(request, *args, **kwargs)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    @extend_schema(tags=["Product"], summary="List all Product", description="List all products")
    def list(self, request, *args, **kwargs):
        """
        List of prpoducts.
        """
        return super().list(request, *args, **kwargs)

    @extend_schema(tags=["Product"], summary="Create product", description="Create a product")
    def create(self, request, *args, **kwargs):
        """
        Create a new category.
        """
        return super().create(request, *args, **kwargs)

    @extend_schema(tags=["Product"], summary="Retrieve  product", description="Retrieve a paticular product.")
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a a particular product using its id.
        """
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(tags=["Product"], summary="Update Product", description="Update a product.")
    def update(self, request, *args, **kwargs):
        """
        Update a paticular product using its id.
        """
        return super().update(request, *args, **kwargs)

    @extend_schema(tags=["Product"], summary="Partially update product", description="Update a product partially.")
    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a product.
        """
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(tags=["Product"], summary="Delete product", description="Delete a product.")
    def destroy(self, request, *args, **kwargs):
        """
        Delete a particular product with its id.
        """
        return super().destroy(request, *args, **kwargs)
# fmt: on
