from rest_framework import serializers
from .models import Like, Post, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'post', 'created']

class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True, default=None)
    likes = LikeSerializer(many=True, default=None)

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'body', 'likes', 'images')

    def create(self, validated_data):
        images_data = self.context['request'].FILES
        post = Post.objects.create(**validated_data)
        for image in images_data.getlist('images'):
            Image.objects.create(post=post, image=image)
        
        return post


