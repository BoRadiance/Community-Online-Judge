import xadmin
from .models import CodingContest,ContestAnnouncement,CodingContestRank

class CodingContestAdmin(object):
    style_fields = {"con_desc": "ueditor"}

class ContestAnnouncementAdmin(object):
    style_fields = {"content": "ueditor"}

class CodingContestRankAdmin(object):
    pass


xadmin.site.register(CodingContest,CodingContestAdmin)
xadmin.site.register(ContestAnnouncement,ContestAnnouncementAdmin)
xadmin.site.register(CodingContestRank,CodingContestRankAdmin)

