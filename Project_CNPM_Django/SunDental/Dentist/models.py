from django.db import models

# Create your models here.

class Dentist(models.Model):
    FullName = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=255)
    License_number = models.CharField(max_length=50)
    Birthday = models.DateField()
    Gender = models.BooleanField()