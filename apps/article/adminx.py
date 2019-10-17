import xadmin
from .models import Article,ArticleUpDown,Comment

class ArticleAdmin(object):
    style_fields = {"content": "ueditor"}



xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(ArticleUpDown)
xadmin.site.register(Comment)
