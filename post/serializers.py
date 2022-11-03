from rest_framework import serializers
from .models import Like, Post


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'post', 'created']

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'body', 'likes', 'image')

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post


