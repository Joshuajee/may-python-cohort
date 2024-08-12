from django.db import models
from datetime import datetime
# Create your models here.
from django.db.models import Model

class Todo(models.Model):
    activity = models.CharField(max_length=20)
    point = models.IntegerField()
    nothing = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now())


class Person(Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True, default="Doe")
    description = models.TextField()
    