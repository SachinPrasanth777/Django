from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, UserRole, Article


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password", "role")

    def create(self, validated_data):
        role_name = validated_data.pop("role", None)
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )
        if role_name:
            role, _ = Role.objects.get_or_create(name=role_name)
            UserRole.objects.create(user=user, role=role)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ("id", "title", "content", "author", "created_at", "updated_at")
