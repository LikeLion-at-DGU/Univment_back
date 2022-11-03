from rest_framework import serializers
from .models import Like, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'answers', 'image', 'event_date', 'category')

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post


