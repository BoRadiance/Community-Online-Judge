from django.db import models
from contest.models import CodingContest
from user.models import User
from problem.models import CodingProlemInfo
# Create your models here.

class JudgeStatus:
    COMPILE_ERROR = -2
    WRONG_ANSWER = -1
    ACCEPTED = 0
    CPU_TIME_LIMIT_EXCEEDED = 1
    REAL_TIME_LIMIT_EXCEEDED = 2
    MEMORY_LIMIT_EXCEEDED = 3
    RUNTIME_ERROR = 4
    SYSTEM_ERROR = 5
    PENDING = 6
    JUDGING = 7



class CodingSubmission(models.Model):

    content = models.ForeignKey(CodingContest,null=True,verbose_name='哪场比赛',on_delete=models.CASCADE)

    problem = models.ForeignKey(CodingProlemInfo,verbose_name='对应问题',on_delete=models.CASCADE)

    create_time = models.DateTimeField(auto_now_add=True,verbose_name='提交时间')

    user_id = models.ForeignKey(User,db_index=True,verbose_name='哪个人交的',on_delete=models.CASCADE)

    status = models.IntegerField(db_index=True, default=JudgeStatus.PENDING,verbose_name='评测状态')

    use_time = models.IntegerField(default=0,verbose_name='耗时 （ms）')

    use_memory = models.IntegerField(default=0,verbose_name='耗空（mb）')

    # json
    # {"time_cost":222,"memory_cost":222,"status":Accept...}
    info = models.TextField(verbose_name='判题器返回信息')

    language = models.TextField(verbose_name='选择的语言')

    # 为防止比赛中 作弊，记录每次提交的IP地址
    ip = models.CharField(max_length=50,verbose_name='该次提交时的IP地址')

    class Meta:
        db_table = "提交表"
        ordering = ("-create_time",)
        verbose_name = u'提交'
        verbose_name_plural = verbose_name


class SourceCode(models.Model):
    Sumission =models.ForeignKey(CodingSubmission,verbose_name='提交ID',on_delete=models.CASCADE)
    code = models.TextField(verbose_name='提交的源代码')

    class Meta:
        db_table = "源代码表"
        verbose_name = u'源代码'
        verbose_name_plural = verbose_name






