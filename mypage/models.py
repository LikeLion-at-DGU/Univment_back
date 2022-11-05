from django.db import models

from accounts.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    profileimage = models.ImageField(upload_to = 'profileimages/')
    name = models.CharField(User, max_length = 10)
    birthday = models.CharField(max_length = 10)
    major = models.CharField(max_length = 20)

class Contacts(models.Model):
    phonenumber = PhoneNumberField(unique = True)
    email = models.EmailField(max_length = 30, unique = True)
    insta = models.CharField(max_length = 20, blank = True)
    github = models.CharField(max_length = 30, blank = True)
