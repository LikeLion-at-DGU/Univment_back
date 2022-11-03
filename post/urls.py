from django.urls import path
from .views import *
from .views import PostList, PostSerializer

app_name = "post"
urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', PostList.as_view()),
]