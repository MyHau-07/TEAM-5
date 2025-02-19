# Generated by Django 5.0.11 on 2025-02-18 09:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='day_of_week',
            field=models.CharField(choices=[('Monday', 'Thứ Hai'), ('Tuesday', 'Thứ Ba'), ('Wednesday', 'Thứ Tư'), ('Thursday', 'Thứ Năm'), ('Friday', 'Thứ Sáu'), ('Saturday', 'Thứ Bảy'), ('Sunday', 'Chủ Nhật')], max_length=9, verbose_name='Ngày trong tuần'),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Bác sĩ'),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='end_time',
            field=models.TimeField(verbose_name='Giờ kết thúc'),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='shift',
            field=models.CharField(choices=[('morning', 'Sáng'), ('afternoon', 'Chiều'), ('evening', 'Tối')], max_length=10, verbose_name='Ca làm việc'),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='start_time',
            field=models.TimeField(verbose_name='Giờ bắt đầu'),
        ),
    ]
