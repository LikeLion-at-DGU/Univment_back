from django.db import models
import datetime

from accounts.models import User

# Create your models here.

# questions - answers 어떻게 처리할지

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    isDefault = models.BooleanField(default = False)
    generated_user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    questions = models.JSONField(null = True)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200, default = '')
    answers = models.JSONField(null = True)
    image = models.ImageField(null = True)
    event_date = models.DateField(default=datetime.date.today)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'posts', null = True)
