from rest_framework import serializers
from .models import Profile, Contacts

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'profileimage']