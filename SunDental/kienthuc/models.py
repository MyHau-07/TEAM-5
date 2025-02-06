from django.db import models

# Create your models here.


class Kienthuc(models.Model):
    tieu_de = models.CharField(max_length=200)
    noi_dung = models.TextField()
    hinh_anh = models.ImageField(upload_to='kien_thuc', null=True, blank=True)
    ngay_dang = models.DateField()
    
    def __str__(self):
        return self.tieu_de
