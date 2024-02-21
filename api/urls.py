from django.urls import path

from . import views

urlpatterns = [
    path("user", views.base_user_list_create_api_view, name="base_user_list_create_api_view"),
    path("user/<int:pk>/", views.base_user_retrieve_update_view, name="base_user_retrieve_update_view"),
    path("category_list_create_api_view", views.category_list_create_api_view, name="category_list_create_api_view"),
    path("category/<slug:slug>/", views.category_retrieveandupdate_view, name="category_retrieveandupdate_view"),
    path("products_list_create_api_view", views.products_list_create_api_view, name="products_list_create_api_view"),
    path("products/<slug:slug>/", views.products_retrieve_update_view, name="products_retrieve_update_view"),
]
