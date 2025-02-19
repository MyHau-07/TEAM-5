from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission 
from django.contrib.auth.models import BaseUserManager
from datetime import date
from django.contrib.auth import get_user_model


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

    
class CommentForm (models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=11)
    message = models.TextField()
    def __str__(self):
        return f"{self.name}"
    
# class CommentFormDentist (models.Model):
#     message = models.TextField()
#     def __str__(self):
#         return f"{self.name}"
    
class Dentist(models.Model):
    id = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=255)
    License_number = models.CharField(max_length=50)
    Dental_branch = models.CharField(max_length=255,null=True, blank=True)
    Phone_Number = models.CharField(max_length=11,null=True, blank=True)
    Email = models.EmailField(max_length=255,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [
        ('M', 'Nam'),
        ('F', 'Nữ'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return f"{self.FullName}"
    



class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.patient_name} ({self.date} {self.time})"
    

class Booking(models.Model):
    fullname = models.CharField(max_length=100)  # Họ và tên
    phone = models.CharField(max_length=15)  # Số điện thoại
    email = models.EmailField()  # Địa chỉ email
    location = models.CharField(max_length=255)  # Địa điểm
    service = models.CharField(max_length=100)  # Dịch vụ
    message = models.TextField(blank=True, null=True)  # Thông tin bệnh (nếu có)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)  # Tải ảnh (nếu có)
    appointment_date = models.DateField(null=True, default=date.today)  # Ngày hẹn
    appointment_time = models.CharField(max_length=25,null=False)  # Giờ hẹn
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="bookings", null=True, blank=True)
    def __str__(self):
        return f"{self.fullname}"

class Services (models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    image = models.ImageField(null=True)
    info = models.TextField(null=True, blank=True)
    time = models.CharField(max_length=255, null=True )
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name}" 
    
class GioHang(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dich_vu = models.ForeignKey(Services, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    so_luong = models.PositiveIntegerField(default=1)  # Cột này phải có

class HoaDon(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    dich_vu = models.CharField(max_length=255)  # Lưu tên dịch vụ (hoặc danh sách dịch vụ)
    ngay_thanh_toan = models.DateTimeField(auto_now_add=True)
    tong_tien = models.FloatField(default=0)

    def __str__(self):
        return f"Hóa đơn #{self.id} - {self.dich_vu}"   
User = get_user_model()
class MedicalRecord(models.Model):
    patient = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='medical_record'
    )
    diagnosis = models.TextField(blank=True, null=True, verbose_name="Chẩn đoán")
    treatment_plan = models.TextField(blank=True, null=True, verbose_name="Kế hoạch điều trị")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Hồ sơ của {self.patient.full_name or self.patient.username}"


class lichhen(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name='appointments'
    )
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='doctor_appointments'
    )
    appointment_date = models.DateField(verbose_name="Ngày hẹn")
    appointment_time = models.TimeField(verbose_name="Giờ hẹn")
    notes = models.TextField(blank=True, null=True, verbose_name="Ghi chú (nếu có)")
    STATUS_CHOICES = (
        ('scheduled', 'Đã lên lịch'),
        ('completed', 'Đã khám'),
        ('cancelled', 'Đã hủy'),
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='scheduled', verbose_name="Trạng thái"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Lịch khám của {self.medical_record.patient.full_name} với "
                f"{self.doctor.full_name} vào {self.appointment_date} - {self.appointment_time}")


class Communication(models.Model):
    medical_record = models.ForeignKey(
        MedicalRecord, on_delete=models.CASCADE, related_name='communications'
    )
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_messages'
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_messages'
    )
    message = models.TextField(verbose_name="Nội dung tin nhắn")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"Tin nhắn từ {self.sender.full_name} đến "
                f"{self.receiver.full_name} lúc {self.timestamp}")
    
class DangKiLichNghi(models.Model):
    id = models.AutoField(primary_key=True)  # ID tự động tăng
    full_name = models.CharField(max_length=255, null=True, blank=True)  # Tên nhân viên
    ngay_nghi = models.DateField(null=True, blank=True)  # Ngày nghỉ
    ca_nghi = models.CharField(max_length=50, null=True, blank=True)  # Ca nghỉ (VD: sáng, chiều, tối)
    ly_do_nghi = models.CharField(max_length=255, null=True, blank=True)  # Lý do nghỉ
    mo_ta = models.TextField(null=True, blank=True)  # Mô tả cụ thể

    def __str__(self):
        return f"{self.full_name} - {self.ngay_nghi}"