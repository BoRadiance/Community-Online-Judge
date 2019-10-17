from django.apps import AppConfig


class VideoConfig(AppConfig):
    name = 'video'
    verbose_name = "用户视频管理"


    def ready(self):
        import video.signals