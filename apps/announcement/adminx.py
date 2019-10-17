from .models import Announcement
import xadmin
from .models import OjCarouselImg,BlogCarouselImg

class AnnouncementAdmin(object):
    style_fields = {"content": "ueditor"}



xadmin.site.register(Announcement,AnnouncementAdmin)
xadmin.site.register(OjCarouselImg)
xadmin.site.register(BlogCarouselImg)
