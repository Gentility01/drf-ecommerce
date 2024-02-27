from django.utils.text import slugify
from rest_framework import serializers

from store.models import Category, Product
from user.models import BaseUser


class BaseUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = BaseUser
        fields = [
            "id",
            "email",
            "username",
            "firstname",
            "password1",
            "password2",
            "created",
            "updated",
        ]

    def validate(self, data):
        """
        Validate the given data.

        Args:
            self: The instance of the class.
            data: The data to be validated.

        Returns:
            The validated data.
        """
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        """
        Create a new user with the validated data and return the created user.

        :param validated_data: The validated data for creating the user.
        :return: The created user.
        """
        password = validated_data.pop("password1")  # Get 'password1' from validated_data
        # Remove 'password2' from validated_data because it's not a field in the model
        validated_data.pop("password2")
        user = BaseUser.objects.create(**validated_data)
        user.set_password(password)  # Set the password
        user.save()  # Save the user object with the password
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "parent_category", "images", "slug"]

    def create(self, validated_data):
        # Generate slug from name field
        validated_data["slug"] = slugify(validated_data["name"])
        return super().create(validated_data)


class ProductsSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Product
        fields = "__all__"
