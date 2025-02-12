# E_Manage/admin.py
from django.contrib import admin
from .models import DichVu, GioHang
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Work_Schedule

@admin.register(Work_Schedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name', 'Specialty_Name', 'Work_Date', 'Start_Time', 'End_Time')
    search_fields = ('name', 'Specialty_Name')
    list_filter = ('Work_Date', 'Specialty_Name')
    ordering = ('Work_Date', 'Start_Time')

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

class DichVuAdmin(admin.ModelAdmin):
    # Hiển thị thông tin dịch vụ bao gồm tên và giá
    list_display = ('ten_dich_vu', 'gia')
    # Thêm tính năng tìm kiếm theo tên dịch vụ
    search_fields = ('ten_dich_vu',)


# Đăng ký các model vào admin
admin.site.register(DichVu, DichVuAdmin)
admin.site.register(GioHang, GioHangAdmin)

