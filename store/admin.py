from django.contrib import admin

from .models import (Category, Color, Images, MyProductAttribute, Product,
                     ProductReview, ProductWishList, Size)

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "category", "in_stalk", "in_active", "in_trending", "just_arrived"]


@admin.register(MyProductAttribute)
class MyProductAttributeAdmin(admin.ModelAdmin):
    list_display = ["products", "size", "color", "main_price", "slashed_price"]


@admin.register(ProductWishList)
class ProductWishListAdmin(admin.ModelAdmin):
    list_display = ["user", "product"]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "review_text", "review_rating"]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ["products", "images"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["title"]
