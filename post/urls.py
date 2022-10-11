from django.urls import path
from .views import *
from .views import PostList, PostSerializer

app_name = "post"
urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]