from sre_constants import CATEGORY
from unicodedata import category
from django.db import models

# Create your models here.
class Products(models.Model):
    p_name=models.CharField(max_length=50)
    desc=models.TextField(max_length=400)
    category=models.CharField(max_length=50)
    sub_category=models.CharField(max_length=50)
    weight=models.IntegerField()
    unit=models.CharField(max_length=20)
    quantity=models.IntegerField()
    amount=models.IntegerField()

    class Meta:
        db_table='products'


class Invoice(models.Model):
    p_id=models.ForeignKey(Products,on_delete=models.CASCADE)
   
    qty=models.IntegerField()
   

    class Meta:
        db_table='invoice'