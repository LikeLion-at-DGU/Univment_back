from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    
    def create(self, validated_data):

        user = User.objects.reg_user(
            nickname=validated_data['nickname'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        return user

    class Meta:
        model = User
        fields = ['nickname','password','first_name','last_name','email']