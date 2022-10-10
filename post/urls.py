from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .views import PostList, PostSerializer

app_name = "post"
urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)