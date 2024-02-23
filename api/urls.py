from django.urls import include, path

app_name = "api"
urlpatterns = [
    path("user/", include("api.routers", namespace="api")),
    # path("categoies/", include("api.routers", namespace="api")),
]
