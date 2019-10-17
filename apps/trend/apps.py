from django.apps import AppConfig


class TrendConfig(AppConfig):
    name = 'trend'
    verbose_name = "动态管理"
    def ready(self):
        import trend.signals

