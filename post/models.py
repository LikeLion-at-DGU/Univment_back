from distutils.command.upload import upload
from django.db import models

from accounts.models import User

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    body = models.TextField()
    image = models.ImageField()

