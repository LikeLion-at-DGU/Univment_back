from django.db import models
import datetime

from accounts.models import User

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    color = models.CharField(max_length=20, null=True)
    isDefault = models.BooleanField(null = False, default=False)
    generated_user = models.ForeignKey(User, null = False, on_delete = models.CASCADE)
    questions = models.JSONField(null = True)
    class Meta:
        unique_together = ["name", "generated_user"]

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100, null=False, default = '')
    answers = models.JSONField(null = True)
    image = models.ImageField(null = True)
    event_date = models.DateField(default=datetime.date.today, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'posts', null = True)
    timeline = models.BooleanField(default=False)