from django.urls import path
from .views import *
from .views import ProfileImageCreate, ProfileImageDetail

app_name = "mypage"
urlpatterns = [
    path('', ProfileImageCreate.as_view()), #프로필 사진 생성
    path('<int:id>/', ProfileImageDetail.as_view()), #프로필 사진 수정, 삭제
]