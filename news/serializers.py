from rest_framework import serializers
from .models import Category, User, News


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "role"]
        extra_kwargs = {
            "password": {"write_only": True},
        }


# creates a serealizer for News Model
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
