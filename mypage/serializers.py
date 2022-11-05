from rest_framework import serializers
from .models import Profile, Contacts

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'profileimage']

class NameCardProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'birthday', 'major']

class NameCardContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
        