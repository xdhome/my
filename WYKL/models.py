from django.db import models

# Create your models here.

class User(models.Model):
    account = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=40)
    tel = models.CharField(max_length=20)