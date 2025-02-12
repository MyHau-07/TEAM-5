# Generated by Django 5.0.11 on 2025-02-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_Manage', '0009_customuser_dentist_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='lichhen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='nhacnho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
