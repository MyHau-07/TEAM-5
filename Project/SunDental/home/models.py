from django.db import models

# Create your models here.
class Customer (models.Model):
    name = models.CharField(max_length=255)
    gender = models.BooleanField()
    birth_day = models.DateField()

class Services (models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)