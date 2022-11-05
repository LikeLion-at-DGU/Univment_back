from .models import Profile, Contacts
from .serializers import ProfileImageSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes

# Create your views here.
# @permission_classes([IsAuthenticatedOrReadOnly])
class ProfileImageCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileImageSerializer
    lookup_field = 'id'

# @permission_classes([IsAuthenticatedOrReadOnly])
class ProfileImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileImageSerializer
    lookup_field = 'id'