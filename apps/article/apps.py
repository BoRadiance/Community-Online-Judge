from django.apps import AppConfig


class ArticleConfig(AppConfig):
    name = 'article'
    verbose_name = "文章管理"

    def ready(self):
        import article.signals
