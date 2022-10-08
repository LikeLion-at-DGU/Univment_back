from django.urls import path, include
from .views import *
from rest_framework import urls

app_name = "accounts"
urlpatterns = [
    path('signup/', register.as_view()),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('auth/', include('rest_auth.urls')),
    # path('auth/registration', include('rest_auth.registration.urls')),
]