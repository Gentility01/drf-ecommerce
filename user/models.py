# fmt: off
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
# fmt: on
from django.db import models
from django.utils.translation import gettext_lazy as _

# from django_countries.fields import CountryField

# Create your models here.


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):
        """
        Create a superuser with the given email, username,
        password, and other optional fields.
        Validate the optional fields to ensure is_staff,
        is_superuser, and is_active are set to True.
        Return the result of creating a user with the
        given parameters and optional fields.
        """
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):
        """
        Create a user with the given email, username, password,
        and other optional fields.
        Validate the optional fields to ensure is_staff, is_superuser,
        and is_active are set to False.
        Return the result of creating a user with the given
        parameters and optional fields.
        """

        other_fields.setdefault("is_staff", False)
        if other_fields.get("is_active") is not True:
            raise ValueError("User must be assigned to is_active=True.")
        if not email:
            raise ValueError(_("User must have an email address."))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email_address"), unique=True)
    username = models.CharField(max_length=300, unique=True)
    firstname = models.CharField(max_length=300, blank=True)
    thumbnail = models.FileField(default="/download (11).png/", upload_to="users/", null=True, blank=True)

    about = models.TextField(_("about"), max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    post_code = models.CharField(max_length=200, blank=True)
    address_line1 = models.CharField(max_length=200, blank=True)
    address_line2 = models.CharField(max_length=200, blank=True)
    town_city = models.CharField(max_length=200, blank=True)
    # user status
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
