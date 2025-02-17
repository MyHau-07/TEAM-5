from django.apps import AppConfig


class EManageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'E_Manage'

    def ready(self):
        # Nếu có sử dụng signals, import chúng tại đây
        pass

