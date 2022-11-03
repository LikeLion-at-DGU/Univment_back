from django.shortcuts import get_object_or_404
from django.views import View
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

    
