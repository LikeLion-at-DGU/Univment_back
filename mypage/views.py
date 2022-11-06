from .models import Profile, Contacts
from .serializers import ProfileImageSerializer, NameCardProfileSerializer, NameCardContactsSerializer
from rest_framework import generics
from rest_framework.decorators import permission_classes
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from accounts.models import User
from .permissions import *
import re, json

# Create your views here.
# 프로필 사진 관련
class ProfileImageCreate(generics.ListCreateAPIView):
    # permission_classes = [IsOwner]
    queryset = Profile.objects.all()
    serializer_class = ProfileImageSerializer
    lookup_field = 'id'

class ProfileImageDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsOwner]
    queryset = Profile.objects.all()
    serializer_class = ProfileImageSerializer
    lookup_field = 'id'

# 명함 프로필 정보 관련
class NameCardProfile(generics.CreateAPIView):
    # permission_classes = [IsOwner]
    queryset = Profile.objects.all()
    serializer_class = NameCardProfileSerializer

class NameCardProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsOwner]
    queryset = Profile.objects.all()
    serializer_class = NameCardProfileSerializer
    lookup_field = 'id'

# 명함 contacts 관련
class NameCardContacts(generics.CreateAPIView):
    # permission_classes = [IsOwner]
    queryset = Contacts.objects.all()
    serializer_class = NameCardContactsSerializer

class NameCardContactsDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsOwner]
    queryset = Contacts.objects.all()
    serializer_class = NameCardContactsSerializer
    lookup_field = 'id'

# 전화번호 관련
def validate_phone(phonenumber):
    pattern = re.compile('^[0-9]{3}-[0-9]{3,4}-[0-9]{4}$')
    if not pattern.match(phonenumber):
        return False
    return True

class phonenumberView(View):
    def phone(self, request):
        data     = json.loads(request.body)
        phonenumber = data.get('phone', None)

        # KEY_ERROR check
        if not(phonenumber):
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

        # validation check
        if not validate_phone(phonenumber):
            return JsonResponse({'message': 'PHONE_VALIDATION_ERROR'}, status=422)
        
        # unique check
        if User.objects.filter(Q(phone=phonenumber)).exists():
            return JsonResponse({'message': 'USER_ALREADY_EXISTS'}, status=409)

        User.objects.create(
            phone    = phonenumber,
        )
        return JsonResponse({'message': 'SUCCESS'}, status=200)