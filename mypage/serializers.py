from rest_framework import serializers
from .models import *

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ('id', 'user', 'profileimage')

    def create(self, validated_data):
        profileimage = ProfileImage.objects.create(**validated_data)
        return profileimage

#NameCard(명함) 관련된 시리얼라이저
class NameCardProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'myname', 'email', 'major', 'birthday')

class NameCardContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('id', 'user', 'phonenumber', 'insta', 'github', 'blog')

class NameCardClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs
        fields = ('id', 'user', 'club1', 'club2', 'club3', 'club4', 'club5')

class NameCardContestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contests
        fields = ('id', 'user', 'contest1', 'contest2', 'contest3', 'contest4', 'contest5')

class NameCardProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'user', 'project1', 'project2', 'project3', 'project4', 'project5')

class NameCardActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = ('id', 'user', 'activity1', 'activity2', 'activity3', 'activity4', 'activity5')
        