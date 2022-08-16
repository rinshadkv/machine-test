import email
from operator import mod
from django.db import models

# Create your models here.

class User(models.Model):
    f_name=models.CharField(max_length=40)
    l_name=models.CharField(max_length=40)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    password=models.CharField(max_length=16)
