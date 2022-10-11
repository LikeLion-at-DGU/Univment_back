from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')

        if not first_name:
            raise ValueError('Users must have an first_name')

        if not last_name:
            raise ValueError('Users must have an last_name')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username=None, first_name=None, last_name=None, email=None, password=None, **extra_fields):
        superuser = self.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
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

    username = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)

    objects = UserManager() # 헬퍼 클래스

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username