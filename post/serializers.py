from rest_framework import serializers
from .models import Category, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'answers', 'image', 'event_date', 'category')

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'isDefault', 'generated_user', 'questions')

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category

