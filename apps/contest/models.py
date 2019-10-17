from django.db import models
from django.utils.timezone import now
from DjangoUeditor.models import UEditorField

from user.models import User

# Create your models here.
class ContestType:
    PUBLIC_CONTEST = "Public"
    PASSWORD_PROTECTED_CONTEST = "Password Protected"


class ContestStatus:
    CONTEST_NOT_START = "1"
    CONTEST_ENDED = "-1"
    CONTEST_UNDERWAY = "0"


class ContestAbstract(models.Model):
    title = models.TextField(verbose_name='标题')
    created_by = models.ForeignKey(User,verbose_name='创建人',on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CodingContest(ContestAbstract):
    '''
    编程比赛表
    '''

    con_desc = UEditorField(verbose_name="竞赛描述", imagePath="contest/images/", width=1000, height=300,
                              filePath="contest/files/", default='')

    visible = models.BooleanField(default=True, verbose_name='是否可见')

    start_time = models.DateTimeField(verbose_name='开始时间')

    end_time = models.DateTimeField(verbose_name='结束时间')

    password = models.TextField(null=True,blank=True)

    @property
    def status(self):
        if self.start_time > now():
            # 没有开始 返回1
            return ContestStatus.CONTEST_NOT_START
        elif self.end_time < now():
            # 已经结束 返回-1
            return ContestStatus.CONTEST_ENDED
        else:
            # 正在进行 返回0
            return ContestStatus.CONTEST_UNDERWAY

    @property
    def contest_type(self):
        if self.password:
            return ContestType.PASSWORD_PROTECTED_CONTEST
        return ContestType.PUBLIC_CONTEST

    class Meta:
        db_table = "竞赛"
        ordering = ("-start_time",)
        verbose_name = u'比赛'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ContestAnnouncement(ContestAbstract):
    '''
    比赛公告表
    '''
    contest = models.ForeignKey(CodingContest,on_delete=models.CASCADE)

    content = UEditorField(verbose_name="竞赛公告", imagePath="contest/images/", width=1000, height=300,
                           filePath="contest/files/", default='')

    class Meta:
        db_table = "contest_announcement"
        ordering = ("-create_time",)
        verbose_name = u'比赛公告'
        verbose_name_plural = verbose_name



class AbstractContestRank(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contest = models.ForeignKey(CodingContest,on_delete=models.CASCADE)

    class Meta:
        abstract = True



class CodingContestRank(AbstractContestRank):
    accepted_number = models.IntegerField(default=0)
    # total_time is only for ACM contest, total_time =  ac time + none-ac times * 20 * 60
    total_time = models.IntegerField(default=0)

    # {"23": {"is_ac": True, "ac_time": 8999, "error_number": 2, "is_first_ac": True}
    #  "24":{...}}
    # key is problem id
    sumbission_info = models.TextField()

    class Meta:
        db_table = "排行表"
        verbose_name = u'比赛排行'
        verbose_name_plural = verbose_name

