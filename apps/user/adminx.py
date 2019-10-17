import xadmin
from xadmin import views
from .models import Tag,UserInfoImg


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "南理社区管理后台"
    site_footer = "NCLG_Blog"
    # menu_style = "accordion"





xadmin.site.register(Tag)
xadmin.site.register(UserInfoImg)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)