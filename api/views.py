from django.shortcuts import get_object_or_404, render
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.response import Response

from store.models import (Category, MyProductAttribute, Product, ProductReview,
                          ProductWishList)
from user.models import BaseUser

from .serializer import (BaseUserSerializer, CategorySerializer,
                         ProductsSerializer)

# Create your views here.


# ----------------------------------------------------------- User views -----------------------------------------------------------
@extend_schema(tags=[" Drf User  List and Create"])
class BaseUserListCreateApiView(generics.ListCreateAPIView):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer

    def post(self, request, *args, **kwargs):
        """
        API endpoint that allows users list or create registration. typically for  user registration
        A description of the post method, its parameters, and its return types.
        """

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


base_user_list_create_api_view = BaseUserListCreateApiView.as_view()


@extend_schema(tags=[" Drf User  Update and Delete"])
class BaseUserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that allows users retrieve or update."""

    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer


base_user_retrieve_update_view = BaseUserRetrieveUpdateView.as_view()


# ----------------------------------------------------------- Category views -----------------------------------------------------------
@extend_schema(tags=[" Drf Category  List and Create"])
class CategoryListCreateApiView(generics.ListCreateAPIView):
    """
    API endpoint that allow user list and create category for their Products"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


category_list_create_api_view = CategoryListCreateApiView.as_view()


@extend_schema(tags=[" Drf Category  Retrieve and Update"])
class CategoryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that updates or retrieves category."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(queryset, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj


category_retrieveandupdate_view = CategoryRetrieveUpdateView.as_view()


# ----------------------------------------------------------- Products views -----------------------------------------------------------
@extend_schema(tags=[" Drf Products  List and Create"])
class ProductsListCreateApiView(generics.ListCreateAPIView):
    """
    API endpoint that allow user list and create products"""

    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


products_list_create_api_view = ProductsListCreateApiView.as_view()


@extend_schema(tags=[" Drf Products  Retrieve and Update"])
class ProductsRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    API endpoint that updates or retrieves products."""

    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(queryset, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj


products_retrieve_update_view = ProductsRetrieveUpdateView.as_view()
