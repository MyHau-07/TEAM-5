from django.contrib import admin
from E_Manage.models import Services
from E_Manage.models import CommentForm
from E_Manage.models import CustomUser
from E_Manage.models import Appointment 
from E_Manage.models import Booking
from E_Manage.models import DangKiLichNghi
from E_Manage.models import GioHang
from E_Manage.models import Dentist
from E_Manage.models import CaLamViec, LichLamViec
from django.urls import reverse
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe  # Thêm dòng này
from E_Manage.models import MedicalRecord, lichhen, Communication
# Register your models here.
admin.site.register(CommentForm)
admin.site.register(DangKiLichNghi)

class CustomUserAdmin(UserAdmin):
    fieldsets = (
            (None, {'fields': ('username', 'password')}),
            ('Personal info', {'fields': ( 'full_name', 'role', 'email', 'phone_number', 'birth_date', 'address', 'gender','image')}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            ('Important dates', {'fields': ('last_login', 'date_joined')}),
        )

    list_display = ('id', 'username', 'full_name', 'role', 'email', 'phone_number', 'birth_date', 'address', 'gender', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'formatted_date', 'time', 'notes')
    search_fields = ('patient_name', 'date')

    def formatted_date(self, obj):
        return obj.date
    formatted_date.admin_order_field = 'date'
    formatted_date.short_description = 'Ngày hẹn'


admin.site.register( Booking)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "time", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "info")
    list_editable = ("price", "is_active")
    ordering = ("name",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        """Hiển thị ảnh xem trước trong Admin"""
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px"/>')
        return "(Không có ảnh)"

    image_preview.short_description = "Xem trước ảnh"
admin.site.register(Services, ServicesAdmin)
class GioHangAdmin(admin.ModelAdmin):
    list_display = ('user', 'dich_vu', 'so_luong', 'get_total_price', 'dich_vu_link')

    # Thêm liên kết tới trang DichVu
    def dich_vu_link(self, obj):
        url = reverse('admin:E_Manage_dichvu_change', args=[obj.dich_vu.id])
        return mark_safe(f'<a href="{url}" target="_blank">Xem Dịch Vụ</a>')

    def dich_vu_link(self, obj):
        if obj.dich_vu:
            url = reverse('admin:E_Manage_services_change', args=[obj.dich_vu.id])  # Dùng "services"
            return mark_safe(f'<a href="{url}" target="_blank">Xem Dịch Vụ</a>')
        return "(Không có dịch vụ)"


    def get_total_price(self, obj):
        return float(obj.dich_vu.price) * obj.so_luong
    get_total_price.short_description = 'Tổng tiền'

# Đăng ký các model vào admin
admin.site.register(GioHang, GioHangAdmin)




@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'diagnosis', 'treatment_plan', 'created_at')
    search_fields = ('patient__full_name', 'patient__username')
    list_filter = ('created_at',)

@admin.register(lichhen)
class lichhen(admin.ModelAdmin):
    list_display = ('id', 'medical_record', 'doctor', 'appointment_date', 'appointment_time', 'status', 'created_at')
    search_fields = ('medical_record__patient__full_name', 'doctor__full_name')
    list_filter = ('appointment_date', 'status')

@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'medical_record', 'sender', 'receiver', 'timestamp')
    search_fields = ('medical_record__patient__full_name', 'sender__full_name', 'receiver__full_name')
    list_filter = ('timestamp',)

class DentistAdmin(admin.ModelAdmin):
    list_display = ('id', 'FullName', 'Specialization', 'License_number', 'Dental_branch', 'Phone_Number', 'Email', 'birth_date', 'gender')
    search_fields = ('FullName', 'Specialization', 'License_number', 'Email')
    list_filter = ('Dental_branch', 'gender')
    ordering = ('FullName',)

admin.site.register(Dentist, DentistAdmin)


#lịch làm
@admin.register(CaLamViec)
class CaLamViecAdmin(admin.ModelAdmin):
    list_display = ['ten_ca']
    search_fields = ['ten_ca']

@admin.register(LichLamViec)
class LichLamViecAdmin(admin.ModelAdmin):
    list_display = ('bac_si', 'ngay', 'thu', 'get_ca_lam', 'trang_thai', 'ghi_chu')
    list_filter = ('thu', 'trang_thai', 'ca_lam')
    search_fields = ('bac_si__username', 'ghi_chu')
    ordering = ['thu', 'ngay']

    def get_ca_lam(self, obj):
        return ", ".join([ca.get_ten_ca_display() for ca in obj.ca_lam.all()])
    get_ca_lam.short_description = "Ca làm việc"
