from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    GENDER_CHOICES = [
        ('M', 'Nam'),
        ('F', 'Nữ'),
    ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    chi_nhanh = models.CharField(max_length=15, null=True, blank=True)
    chuyen_nganh = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='img/avt/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Nếu không có ảnh, đặt ảnh mặc định theo giới tính
        if not self.image or self.image.name == "":
            if self.gender == 'M':
                self.image.name = 'img/avt/default_male.png'
            elif self.gender == 'F':
                self.image.name = 'img/avt/default_female.png'
            else:
                self.image.name = 'img/avt/default_male.png'  # Mặc định nếu không có giới tính

        super().save(*args, **kwargs)
    
    
    ROLE_CHOICES = (
        ('dentist', 'Dentist'),
        ('clinic_owner', 'Clinic Owner'),
        ('patient', 'Patient'),
    )
    # Thêm trường role
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, role="patient", **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, **extra_fields)


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
    

    