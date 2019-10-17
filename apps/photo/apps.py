from django.apps import AppConfig


class PhotoConfig(AppConfig):
    name = 'photo'
    verbose_name = "用户相册管理"

    def ready(self):
        import photo.signals