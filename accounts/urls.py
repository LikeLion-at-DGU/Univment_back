from django.urls import path, include
from .views import *
from rest_framework import urls

app_name = "accounts"
urlpatterns = [
    path('signup/', register.as_view()),
    # path('auth/', include('rest_auth.urls')),
    # path('auth/registration', include('rest_auth.registration.urls')),
]