from distutils.command.upload import upload
from django.db import models

from accounts.models import User

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    generated_user = models.ForeignKey(User, null = False, on_delete = models.CASCADE)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    answers = models.JSONField()
    image = models.ImageField()
    event_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'posts')