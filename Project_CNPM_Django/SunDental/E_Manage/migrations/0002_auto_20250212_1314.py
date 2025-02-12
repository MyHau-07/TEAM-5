from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('E_Manage', '0001_initial'),  # Giữ nguyên phần này
    ]

    operations = [
        migrations.AddField(
            model_name='giohang',
            name='so_luong',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
