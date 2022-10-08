from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):

    def reg_user(self, nickname, first_name, last_name, email, password):

        if not nickname:
            raise ValueError('필수 입력')
        if not first_name:
            raise ValueError('필수 입력')
        if not last_name:
            raise ValueError('필수 입력')
        if not email:
            raise ValueError('필수 입력')
        if not password:
            raise ValueError('필수 입력')

        user = self.model(
            nickname = nickname,
            first_name = first_name,
            last_name = last_name,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save()

        return user
    
    def reg_admin(self, nickname, first_name, last_name, email, password):
        user = self.reg_user(
            email,
            password = password,
            nickname = nickname,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.save()
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10, unique=True)
    email = models.EmailField()

    objects = UserManager() # 헬퍼 클래스
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']  # 필수 작성
    USERNAME_FIELD = 'nickname' # nickname으로 받은 값을 사용자의 username field에 저장

    def __str__(self):
        return self.nickname