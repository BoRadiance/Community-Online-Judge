from user.models import User
from base_model import BaseModel
from django.db import models
from DjangoUeditor.models import UEditorField
from contest.models import CodingContest


# Create your models here.

class ProblemTages(BaseModel):
    '''
    问题标签表
    '''
    name = models.TextField()
    is_hot = models.BooleanField(default=False, verbose_name='是否为热门题型')
    class Meta:
        verbose_name = '问题标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProblemAbstract(BaseModel):
    '''
    问题抽象表
    '''

    title = models.CharField(max_length=30, verbose_name='题目标题')

    pro_desc = UEditorField(verbose_name="题目描述", imagePath="problem/images/", width=1000, height=300,
                            filePath="problem/files/", default='')

    # source 来源 用于后期制作爬虫抄题，显示版权
    source = models.CharField(max_length=100, verbose_name='来源',default="原创",null=True,blank=True)

    # 属于竞赛
    contest = models.ForeignKey(CodingContest, null=True,on_delete=models.DO_NOTHING,blank=True,related_name='belongcontent')

    # 每个人都可以上传自己编造的题目，但是需要后台审核
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    State = (
        (1, 'Low'),
        (2, 'Mid'),
        (3, 'Hard')
    )

    degree =models.IntegerField(choices=State, default=2,
                                verbose_name='题目难度', )



class CodingProlemInfo(ProblemAbstract):
    '''
    编程问题表
    '''

    pro_input = UEditorField(verbose_name="输入描述", imagePath="problem/images/", width=1000, height=300,
                              filePath="problem/files/", default='')

    pro_output = UEditorField(verbose_name="输出描述", imagePath="problem/images/", width=1000, height=300,
                             filePath="problem/files/", default='')

    sample_input = UEditorField(verbose_name="样例输入", imagePath="problem/images/", width=1000, height=300,
                             filePath="problem/files/", default='')

    sample_output = UEditorField(verbose_name="样例输出", imagePath="problem/images/", width=1000, height=300,
                             filePath="problem/files/", default='')

    ac_number = models.IntegerField(default=0,verbose_name='总AC数')

    submit_number = models.IntegerField(default=0,verbose_name='总提交数')

    time_limit = models.IntegerField(default=1,verbose_name='限制时间 （ms）')

    memory_limit = models.IntegerField(default=128,verbose_name='空间限制（mb）')

    tags = models.ManyToManyField(ProblemTages)

    hit = models.CharField(max_length=30,verbose_name='题目提示',null=True,blank=True,default="无")

    spj = models.BooleanField(default=False,verbose_name='题目是否特判')

    def addAC(self):
        self.ac_number += 1

    def addSub(self):
        self.submit_number += 1

    class Meta:
        verbose_name = '编程问题'
        verbose_name_plural = verbose_name
        ordering = ['create_time',]

    def __str__(self):
        return self.title


class OtherProblem(ProblemAbstract):
    '''
    其他题型，只为一些选拔比赛的时候使用。（比如蓝桥杯）
    '''

    answer = models.TextField(verbose_name='答案')

    class Meta:
        verbose_name = '非编程问题'
        verbose_name_plural = verbose_name
