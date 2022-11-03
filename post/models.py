from distutils.command.upload import upload
from django.db import models

from accounts.models import User

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    body = models.TextField()

    def get_total_likes(self):
        return self.likes.user.count()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "likes")
    created = models.DateTimeField(auto_now_add = True)

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None, related_name = 'images')
    image = models.ImageField(upload_to = 'images/')
