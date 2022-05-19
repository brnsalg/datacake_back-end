from django.db import models

# Create your models here.

class Todo(models.Model):
    TodoId = models.AutoField(primary_key=True)
    TodoTitle = models.CharField(max_length=100)
    TodoDescription = models.CharField(max_length=200)
    TodoStatus = models.BooleanField(default=False)