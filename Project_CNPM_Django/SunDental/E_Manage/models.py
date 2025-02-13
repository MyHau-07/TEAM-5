from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission 
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


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.patient_name} ({self.date} {self.time})"
    

class Booking(models.Model):
    # Danh sách địa chỉ có thể chọn
    ADDRESS_CHOICES = [
    ('02 Võ Oanh, Phường 25, Bình Thạnh, Hồ Chí Minh', '02 Võ Oanh, Phường 25, Bình Thạnh, Hồ Chí Minh'),
    ('70 Tô Ký, Tân Chánh Hiệp, Quận 12, TPHCM', '70 Tô Ký, Tân Chánh Hiệp, Quận 12, TPHCM'),
    ('10/12 Trần Não, KP3, P. Bình An, TP. Thủ Đức, TP. HCM', '10/12 Trần Não, KP3, P. Bình An, TP. Thủ Đức, TP. HCM'),
    ]


    # Danh sách dịch vụ có thể chọn
    SERVICE_CHOICES = [
    ('nho_rang', 'Nhổ răng'),
    ('han_rang', 'Hàn răng'),
    ('dieu_tri_tuy', 'Điều trị tủy'),
    
    ('nieng_rang_kim_loai', 'Niềng răng kim loại'),
    ('nieng_rang_trong_suot', 'Niềng răng trong suốt'),
    ('dieu_tri_lech_khop_can', 'Điều trị lệch khớp cắn'),
    
    ('lam_rang_su', 'Làm răng sứ'),
    ('cay_ghep_implant', 'Cấy ghép Implant'),
    ('mat_dan_su_veneer', 'Mặt dán sứ Veneer'),
    
    ('cao_voi_rang', 'Cạo vôi răng'),
    ('dieu_tri_viem_nuou', 'Điều trị viêm nướu'),
    ('ghep_nuou', 'Ghép nướu'),
    ('lay_cao_rang_sau', 'Lấy cao răng sâu dưới nướu'),
    
    ('dieu_tri_ap_xe_rang', 'Điều trị áp xe răng'),
    ('tai_tao_xuong_o_rang', 'Tái tạo xương ổ răng'),
    
    ('kham_dinh_ky', 'Khám sức khỏe răng miệng định kỳ'),
    ('chup_x_quang_toan_ham', 'Chụp X-quang răng toàn hàm'),
    ('tu_van_ke_hoach_dieu_tri', 'Tư vấn kế hoạch điều trị'),
    ('chup_ct_cone_beam_3d', 'Chụp CT Cone Beam 3D'),
    ('do_khop_can_ky_thuat_so', 'Đo khớp cắn kỹ thuật số'),
    ('chup_phim_panorama', 'Chụp phim Panorama'),
    
    ('tay_trang_bang_laser', 'Tẩy trắng răng bằng công nghệ Laser'),
    ('tu_van_dinh_duong', 'Tư vấn dinh dưỡng và phòng ngừa bệnh lý răng miệng'),
    ('danh_gia_suc_khoe_rang_mieng', 'Đánh giá sức khỏe răng miệng chuyên sâu'),
    ]

    # Danh sách các khung giờ
    TIME_SLOTS = [
        ('08:00', '08:00 AM'),
        ('08:45', '08:45 AM'),
        ('09:30', '09:30 AM'),
        ('10:15', '10:15 AM'),
        ('11:00', '11:00 AM'),
        ('11:45', '11:45 AM'),
        
        ('13:15', '01:15 PM'),
        ('14:00', '02:00 PM'),
        ('14:45', '02:45 PM'),
        ('15:30', '03:30 PM'),
        ('16:15', '04:15 PM'),
    ]

    address = models.CharField(max_length=255, choices=ADDRESS_CHOICES)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    day_appointment = models.DateField(max_length=10)
    time_appointment = models.CharField(max_length=5, choices=TIME_SLOTS)
    name = models.CharField(max_length=255,null=True, blank=True)
    email = models.EmailField(max_length=255,null=True, blank=True)
    phone = models.CharField(max_length=11,null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    Image = models.ImageField(upload_to='booking_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.address} - {self.service} - {self.day_appointment} {self.time_appointment}"

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

