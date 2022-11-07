from rest_framework import serializers
from .models import *

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ('id', 'user', 'profileimage')

    def create(self, validated_data):
        profileimage = ProfileImage.objects.create(**validated_data)
        return profileimage

class NameCardProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'birthday', 'major')

class NameCardContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
        