import auto_prefetch
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.text import slugify
from django_resized import ResizedImageField

from ecommerce.utils.choices import RATING, STATUS_CHOICES
from ecommerce.utils.media import MediaHelper
from ecommerce.utils.models import NamedTimeBasedModel, TimeBasedModel
from user.models import BaseUser

# from django.forms import CharField


# from PIL import Image


class ProductManager(models.Manager):
    def get_queryset(self):
        """
        Return a filtered queryset of products that are inactive.
        """
        return super().get_queryset().filter(in_active=True)


class Banner(TimeBasedModel):
    image = ResizedImageField(upload_to=MediaHelper.get_image_upload_path, verbose_name="Image")
    h1_text = models.CharField(max_length=100)
    h5_text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.h1_text


class Category(NamedTimeBasedModel):
    parent_category = auto_prefetch.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, null=True, blank=True
    )
    images = ResizedImageField(upload_to=MediaHelper.get_image_upload_path, verbose_name="Image")
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("selcorshop:product_list_by_category", args=[self.slug])

    def __str__(self):
        return self.name

    class Meta(NamedTimeBasedModel.Meta):
        base_manager_name = "prefetch_manager"
        verbose_name_plural = "Categories"


class Color(NamedTimeBasedModel):
    color_code = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title


class Product(NamedTimeBasedModel):
    slug = models.SlugField(max_length=255)
    category = auto_prefetch.ForeignKey("Category", related_name="product", on_delete=models.CASCADE)
    created_by = auto_prefetch.ForeignKey(BaseUser, related_name="product_user", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    information = models.TextField(blank=True, null=True)
    thumbnail = ResizedImageField(upload_to=MediaHelper.get_image_upload_path, verbose_name="Image")
    in_stalk = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    in_trending = models.BooleanField(default=True, null=True)
    just_arrived = models.BooleanField(default=True, null=True)

    # objects = models.Manager()
    # products = ProductManager()

    class Meta(NamedTimeBasedModel.Meta):
        base_manager_name = "prefetch_manager"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# this will help to create price for same product with diffrient color and size


class MyProductAttribute(models.Model):
    products = auto_prefetch.ForeignKey(Product, on_delete=models.CASCADE)
    size = auto_prefetch.ForeignKey(Size, on_delete=models.CASCADE)
    color = auto_prefetch.ForeignKey(Color, on_delete=models.CASCADE)
    main_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    slashed_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.products.title


class Images(models.Model):
    products = auto_prefetch.ForeignKey(Product, on_delete=models.CASCADE)
    images = ResizedImageField(upload_to=MediaHelper.get_image_upload_path, verbose_name="Image")

    def __str__(self):
        return f"image from {self.products.title}"


class CartOrder(models.Model):
    user = auto_prefetch.ForeignKey(BaseUser, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(choices=STATUS_CHOICES, max_length=200)


class CartOrderItem(models.Model):
    order = auto_prefetch.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=150)
    item = models.CharField(max_length=150)
    image = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))


class ProductReview(models.Model):
    user = auto_prefetch.ForeignKey(BaseUser, on_delete=models.CASCADE)
    product = auto_prefetch.ForeignKey(Product, on_delete=models.CASCADE)
    review_text = models.TextField()
    review_rating = models.CharField(choices=RATING, max_length=150)

    def getreview_rating(self):
        return self.review_rating


class ProductWishList(models.Model):
    user = auto_prefetch.ForeignKey(BaseUser, on_delete=models.CASCADE)
    product = auto_prefetch.ForeignKey(Product, on_delete=models.CASCADE)


class UserAddressBook(models.Model):
    user = auto_prefetch.ForeignKey(BaseUser, on_delete=models.CASCADE)
    address = models.TextField()
    status = models.BooleanField(default=False)
