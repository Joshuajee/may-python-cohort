from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=6)
    title = models.CharField(max_length=150)
    content = models.TextField()    
    date = models.DateTimeField(default=datetime.now())

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=6)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now())
    
class Person(models.Model):
    name = models.CharField(max_length=20)
    
class Wallet(models.Model):
    person = models.OneToOneField(Person, on_delete=models.RESTRICT, related_name="wallet")
    btc = models.DecimalField(default=0.0, max_digits=1000000000, decimal_places=10)
    usdt = models.DecimalField(default=100.0, max_digits=100000000, decimal_places=10)