from django.db import models


# Create your models here.
class Customer (models.Model):
    name = models.CharField(max_length=255)
    gender = models.BooleanField()
    birth_day = models.DateField()


