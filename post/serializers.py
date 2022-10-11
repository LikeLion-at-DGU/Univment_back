from rest_framework import serializers
from .models import Post, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True, default=None)

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'body', 'images')

    def create(self, validated_data):
        images_data = self.context['request'].FILES
        post = Post.objects.create(**validated_data)
        for image in images_data.getlist('images'):
            Image.objects.create(post=post, image=image)
        
        return post


