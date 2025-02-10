from django.db import models

# Create your models here.
class Customer (models.Model):
    name = models.CharField(max_length=255)
    gender = models.BooleanField()
    birth_day = models.DateField()

class Services (models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    image = models.ImageField(null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name}"
    
class CommentForm (models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=11)
    message = models.TextField()
    def __str__(self):
        return f"{self.name}"
    
class Dentist(models.Model):
    FullName = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=255)
    License_number = models.CharField(max_length=50)
    Birthday = models.DateField()
    Gender = models.BooleanField()