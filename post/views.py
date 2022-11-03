from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import generics
# Create your views here.
class PostList(generics.ListCreateAPIView):
    # get_queryset : pk(카테고리 넘버)에 맞는 글들 추출
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        return (
            super().
            get_queryset(*args, **kwargs).
            filter(category = self.kwargs['pk'])
        )

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset1 = Category.objects.filter(isDefault = True)
        queryset2 = Category.objects.filter(generated_user = self.request.user)
        queryset = queryset1.union(queryset2)
        return queryset

    

    
