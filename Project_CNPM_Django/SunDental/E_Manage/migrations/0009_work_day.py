# Generated by Django 5.0.11 on 2025-02-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Manage', '0008_work_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('Specialty_Name', models.CharField(max_length=255)),
                ('Actual_Working_Day', models.IntegerField()),
            ],
        ),
    ]
