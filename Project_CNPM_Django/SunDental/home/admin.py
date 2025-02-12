from django.contrib import admin
from E_Manage.models import Services
from E_Manage.models import CommentForm
from E_Manage.models import CustomUser
from django.contrib.auth.admin import UserAdmin



# Register your models here.
admin.site.register(Services)
admin.site.register(CommentForm)


class CustomUserAdmin(UserAdmin):
    fieldsets = (
            (None, {'fields': ('username', 'password')}),
            ('Personal info', {'fields': ( 'full_name', 'role', 'email', 'phone_number', 'birth_date', 'address', 'gender','image')}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            ('Important dates', {'fields': ('last_login', 'date_joined')}),
        )

    list_display = ('id', 'username', 'full_name', 'role', 'email', 'phone_number', 'birth_date', 'address', 'gender', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)