from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.views import BaseUserViewSet, CategoryViewSet, ProductViewSet

PREFIX = "api"  # This is a prefix used for naming the app.


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", BaseUserViewSet, basename="users")
router.register("category", CategoryViewSet, basename="category")
router.register("product", ProductViewSet, basename="product")


app_name = f"{PREFIX}"
urlpatterns = router.urls
