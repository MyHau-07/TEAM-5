from django.contrib import admin
from E_Manage.models import Services
from E_Manage.models import CommentForm
from E_Manage.models import Work_Schedule
from E_Manage.models import Work_day

# Register your models here.
admin.site.register(Services)
admin.site.register(CommentForm)
admin.site.register(Work_Schedule)
admin.site.register(Work_day)