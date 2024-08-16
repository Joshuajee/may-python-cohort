from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    profile_image = models.FileField(upload_to="uploads")
    
class Post(models.Model):
    user  = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user")
    title = models.CharField(max_length=150)
    content = models.TextField()
    views = models.IntegerField(default=0)
    date  = models.DateTimeField(default=datetime.now())
    
    
    
