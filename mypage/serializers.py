from rest_framework import serializers
from .models import *

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ('id', 'profileimage')

    def create(self, validated_data):
        profileimage = ProfileImage.objects.create(**validated_data)
        return profileimage

class NameCardProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'birthday', 'major')

class NameCardContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id', 'phonenumber', 'email', 'insta', 'github', 'blog')
        