from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "username", "password")

    def create(self, validated_data):
        validated_data["is_active"] = True  # Ensure is_active is set to True
        return super().create(validated_data)
