# # 로그인 serializer
# from rest_framework import serializers
# from .models import User

# from django.contrib.auth.models import update_last_login
# from django.contrib.auth import authenticate

# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=64)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)

#     def validate(self, data):
#         email = data.get("email", None)
#         password = data.get("password", None)
#         user = authenticate(email=email, password=password)

#         if user is None:
#             return {
#                 'email': 'None'
#             }
#         try:
#             payload = JWT_PAYLOAD_HANDLER(user)
#             jwt_token = JWT_ENCODE_HANDLER(payload)
#             update_last_login(None, user)
#         except User.DoesNotExist:
#             raise serializers.ValidationError(
#                 'User with given email and password does not exists'
#             )
#         return {
#             'email': user.email,
#             'token': jwt_token
#         }