from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save()
        return superuser


class User(AbstractUser):

    username = models.CharField(max_length=10)
    email = models.EmailField(max_length=30, unique=True)

    objects = UserManager() # 헬퍼 클래스

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username