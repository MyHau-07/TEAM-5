from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import timezone
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





class DichVu(models.Model):
    ten_dich_vu = models.CharField(max_length=255)
    gia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.ten_dich_vu

class GioHang(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dich_vu = models.ForeignKey(DichVu, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    so_luong = models.PositiveIntegerField(default=1)  # Cột này phải có






