from django.contrib import admin

from .models import BaseUser

# Register your models here.


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "is_active", "is_staff")
