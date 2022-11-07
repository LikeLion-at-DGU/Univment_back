from django.urls import path
from .views import *
from .views import ProfileImageCreate, ProfileImageDetail

app_name = "mypage"
urlpatterns = [
    path('', ProfileImageCreate.as_view()), #프로필 사진 생성
    path('<int:id>/', ProfileImageDetail.as_view()), #프로필 사진 보기, 수정, 삭제
    path('namecardprofile/', NameCardProfile.as_view()), #명함 프로필 내용 작성
    path('namecardprofile/<int:id>/', NameCardProfileDetail.as_view()), #명함 프로필 보기, 수정, 삭제
    path('namecardcontacts/', NameCardContacts.as_view()), #명함 contacts 내용 작성
    path('namecardcontacts/<int:id>/', NameCardContactsDetail.as_view()), #명함 contacts 내용 보기, 수정, 삭제
]