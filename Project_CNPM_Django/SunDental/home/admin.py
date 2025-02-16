from django.contrib import admin
from E_Manage.models import Services
from E_Manage.models import CommentForm
from E_Manage.models import CustomUser
from E_Manage.models import Appointment 
from E_Manage.models import Booking 
from E_Manage.models import GioHang
from E_Manage.models import DangKiLichNghi
from E_Manage.models import Dentist
from django.urls import reverse
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Services)
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

class GioHangAdmin(admin.ModelAdmin):
    list_display = ('user', 'dich_vu', 'so_luong', 'get_total_price', 'dich_vu_link')

    # Thêm liên kết tới trang DichVu
    def dich_vu_link(self, obj):
        url = reverse('admin:E_Manage_dichvu_change', args=[obj.dich_vu.id])
        return mark_safe(f'<a href="{url}" target="_blank">Xem Dịch Vụ</a>')

    dich_vu_link.short_description = 'Dịch vụ'

    def get_total_price(self, obj):
        return obj.dich_vu.gia * obj.so_luong
    get_total_price.short_description = 'Tổng tiền'

# Đăng ký các model vào admin
admin.site.register(GioHang, GioHangAdmin)


class DentistAdmin(admin.ModelAdmin):
    list_display = ('id', 'FullName', 'Specialization', 'License_number', 'Dental_branch', 'Phone_Number', 'Email', 'Birthday', 'Gender')
    search_fields = ('FullName', 'Specialization', 'License_number', 'Email')
    list_filter = ('Dental_branch', 'Gender')
    ordering = ('FullName',)

admin.site.register(Dentist, DentistAdmin)