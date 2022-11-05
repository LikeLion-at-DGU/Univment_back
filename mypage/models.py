from django.db import models

from accounts.models import User
# from django.core.validators import RegexValidator
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    profileimage = models.ImageField(upload_to = 'profileimages/')
    name = models.ForeignKey(User, max_length = 10, on_delete = models.CASCADE, null = True)
    birthday = models.CharField(max_length = 10)
    major = models.CharField(max_length = 20)

class Contacts(models.Model):
    id = models.AutoField(primary_key = True)
    phonenumber = models.CharField(max_length = 13, unique=True)
    email = models.CharField(max_length = 30)
    insta = models.CharField(max_length = 20, blank = True)
    github = models.CharField(max_length = 30, blank = True, null = True)
    blog = models.CharField(max_length = 40, blank = True, null = True)