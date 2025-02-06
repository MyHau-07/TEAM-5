from django.contrib import admin

from.models import Kienthuc

class KienThucAdmin(admin.ModelAdmin):
  list_display = ("tieu_de", "noi_dung", "hinh_anh", "ngay_dang")
  
admin.site.register(Kienthuc, KienThucAdmin)