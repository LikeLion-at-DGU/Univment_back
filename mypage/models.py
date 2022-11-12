from django.db import models
import datetime

from accounts.models import User
# from django.core.validators import RegexValidator
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ProfileImage(models.Model):
    id = models.AutoField(primary_key = True)
    profileimage = models.ImageField(upload_to = 'profileimages/')
    user = models.ForeignKey(User, max_length = 10, on_delete = models.CASCADE)

# NameCard(명함)에 들어갈 정보
class Profile(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, max_length = 10, on_delete = models.CASCADE)
    birthday = models.DateField(null = True, blank = True)
    major = models.CharField(max_length = 20, blank = True)

class Contacts(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, max_length = 10, on_delete = models.CASCADE)
    phonenumber = models.CharField(max_length = 13, unique=True)
    email = models.CharField(max_length = 30)
    insta = models.CharField(max_length = 20, blank = True)
    github = models.CharField(max_length = 30, blank = True, null = True)
    blog = models.CharField(max_length = 40, blank = True, null = True)

class Clubs(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, max_length = 10, on_delete = models.CASCADE)
    club1 = models.CharField(max_length = 23, null = True, blank = True)
    club2 = models.CharField(max_length = 23, null = True, blank = True)
    club3 = models.CharField(max_length = 23, null = True, blank = True)
    club4 = models.CharField(max_length = 23, null = True, blank = True)
    club5 = models.CharField(max_length = 23, null = True, blank = True)

class Contests(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, max_length = 10, on_delete = models.CASCADE)
    contest1 = models.CharField(max_length = 23, null = True, blank = True)
    contest2 = models.CharField(max_length = 23, null = True, blank = True)
    contest3 = models.CharField(max_length = 23, null = True, blank = True)
    contest4 = models.CharField(max_length = 23, null = True, blank = True)
    contest5 = models.CharField(max_length = 23, null = True, blank = True)

class Projects(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, max_length = 10, on_delete = models.CASCADE)
    project1 = models.CharField(max_length = 23, null = True, blank = True)
    project2 = models.CharField(max_length = 23, null = True, blank = True)
    project3 = models.CharField(max_length = 23, null = True, blank = True)
    project4 = models.CharField(max_length = 23, null = True, blank = True)
    project5 = models.CharField(max_length = 23, null = True, blank = True)

class Activities(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, max_length = 10, on_delete = models.CASCADE)
    activity1 = models.CharField(max_length = 23, null = True, blank = True)
    activity2 = models.CharField(max_length = 23, null = True, blank = True)
    activity3 = models.CharField(max_length = 23, null = True, blank = True)
    activity4 = models.CharField(max_length = 23, null = True, blank = True)
    activity5 = models.CharField(max_length = 23, null = True, blank = True)