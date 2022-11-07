from django.urls import path
from .views import *
from .views import CategoryDetail, PostSerializer, PostCreate

app_name = "post"
urlpatterns = [
    path('', PostCreate.as_view()), #글 생성
    path('<int:id>/', PostDetail.as_view()), #글 세부사항 / 수정 / 삭제
    path('category/', CategoryList.as_view()), # 카테고리 생성
    path('category/<int:category>/', CategoryDetail.as_view()), # 카테고리의 글 목록 / 카테고리 삭제
]