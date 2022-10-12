from django.shortcuts import render
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from accounts.models import User
# from .serializers import UserLoginSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = "__all__"

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# # 로그인 할 때 이메일, 비밀번호만 사용
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def login(request):
#     if request.method == 'POST':
#         serializer = UserLoginSerializer(data=request.data)

#         if not serializer.is_valid(raise_exception=True):
#             return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
#         if serializer.validated_data['email'] == "None":
#             return Response({'message': 'fail'}, status=status.HTTP_200_OK)

#         response = {
#             'success': 'True',
#             'token': serializer.data['token']
#         }
#         return Response(response, status=status.HTTP_200_OK)