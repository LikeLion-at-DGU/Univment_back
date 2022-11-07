from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes
from django.views import View
from django.http import JsonResponse
from django.db.models import Q
from accounts.models import User
import re, json

# Create your views here.
# 프로필 사진 관련
class ProfileImageCreate(generics.ListCreateAPIView):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

class ProfileImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

# 명함 프로필 정보 관련
class NameCardProfile(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = NameCardProfileSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

class NameCardProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = NameCardProfileSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


# 명함 contacts 관련
class NameCardContacts(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = NameCardContactsSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

class NameCardContactsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = NameCardContactsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

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
            phone = phonenumber,
        )
        return JsonResponse({'message': 'SUCCESS'}, status=200)

# 명함 clubs 관련
class NameCardClubs(generics.ListCreateAPIView):
    queryset = Clubs.objects.all()
    serializer_class = NameCardClubsSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

class NameCardClubsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clubs.objects.all()
    serializer_class = NameCardClubsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

# 명함 contests 관련
class NameCardContests(generics.ListCreateAPIView):
    queryset =Contests.objects.all()
    serializer_class = NameCardContestsSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

class NameCardContestsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =Contests.objects.all()
    serializer_class = NameCardContestsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

# 명함 projects 관련
class NameCardProjects(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = NameCardProjectsSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

class NameCardProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = NameCardProjectsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

# 명함 activities 관련
class NameCardActivities(generics.ListCreateAPIView):
    queryset = Activities.objects.all()
    serializer_class = NameCardActivitiesSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

class NameCardActivitiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activities.objects.all()
    serializer_class = NameCardActivitiesSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs