from django.db import models
from base_model import BaseModel
from user.models import User
from utils.SomeSetting import  LiterDocStorage


# Create your models here.

class TrendClass(BaseModel):
    title = models.TextField(verbose_name="动态类别")
    desc = models.TextField(verbose_name='动态类别描述',default='')
    Image = models.ImageField(upload_to="trend/", null=True,
                              blank=True, verbose_name="动态分类图",
                              )

    class Meta:
        verbose_name = "动态类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Trend(BaseModel):
    """
    动态
    """
    tags = models.ForeignKey(TrendClass, on_delete=models.CASCADE, verbose_name='所属于类别',null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='发表者')
    content = models.TextField(verbose_name="动态内容", default='')
    desc = models.CharField(max_length=255, verbose_name='摘要', default='')
    State = (
        (1, '审核通过'),
        (2, '审核中'),
        (3, '审核不通过')
    )

    State = models.IntegerField(choices=State, default=1,
                                    verbose_name='审核状态',)

    browse = models.IntegerField(default=0, verbose_name='浏览量')

    ThumbsUp = models.IntegerField(default=0, verbose_name='点赞量')

    CommentCount = models.IntegerField(default=0, verbose_name='评论数')

    def BrowseAdd(self):
        self.browse = self.browse + 1

    def ThumbsUpAdd(self):
        self.ThumbsUp = self.ThumbsUp + 1

    def CommentAdd(self):
        self.CommentCount = self.CommentCount + 1

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = "个人动态"
        verbose_name_plural = verbose_name




class TrendPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='1')

    article = models.ForeignKey(Trend, on_delete=models.CASCADE,related_name='photo')
    Image = models.ImageField(upload_to="trend/", null=True,
                                            blank=True, verbose_name="个人动态的图片",
                                            storage=LiterDocStorage())

    class Meta:
        verbose_name = "个人动态图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.article)


class TrendUpDown(models.Model):
    """
    点赞表
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Trend, on_delete=models.CASCADE)
    is_up = models.BooleanField(default=True)

    class Meta:
        verbose_name = "动态点赞"
        verbose_name_plural = verbose_name
        unique_together = ("user", "article")

    def __str__(self):
        return str(self.user)+str(self.article)




class TrendComment(models.Model):
    """
    评论表
    """
    article = models.ForeignKey(Trend, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='发布者', related_name='trendcommentfrom')
    content = models.CharField(max_length=255)  # 评论内容
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE,
                                       related_name="trendsub_comm")  # blank=True 在django admin里面可以不填
    layer = models.IntegerField(default=1)
    touser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='给谁回复', related_name='trendcommentto', null=True,
                               blank=True)

    def __str__(self):
        return str(self.user) + str(self.touser)

    class Meta:
        verbose_name = "动态评论"
        verbose_name_plural = verbose_name






