from django.db import models
from base_model import BaseModel
from user.models import User,Tag,UserInfoImg
from DjangoUeditor.models import UEditorField
from rest_framework_recursive.fields import  RecursiveField
# Create your models here.


class Article(BaseModel):
    """
    文章
    """
    title = models.CharField(max_length=255,verbose_name='标题',null=True,blank=True)
    tags = models.ManyToManyField(Tag,)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    content = UEditorField(verbose_name="文章内容", imagePath="article/images/", width=1000, height=300,
                           filePath="article/files/", default='')
    desc = models.CharField(max_length=255,verbose_name='摘要',default='')
    State = (
        (1, '审核通过'),
        (2, '审核中'),
        (3, '审核不通过')
    )

    State = models.IntegerField(choices=State, default=1,
                                    verbose_name='审核状态', null=True)

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
        return str(self.user)+str(self.title)

    class Meta:
        verbose_name = "技术文章"
        verbose_name_plural = verbose_name



class ArticleUpDown(models.Model):
    """
    点赞表
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_up = models.BooleanField(default=True)

    class Meta:
        verbose_name = "文章点赞"
        verbose_name_plural = verbose_name
        unique_together = ("user", "article")

    def __str__(self):
        return str(self.user)+str(self.article)




class Comment(models.Model):
    """
    评论表
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='发布者',related_name='commentfrom')
    content = models.CharField(max_length=255)  # 评论内容
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self", null=True, blank=True,on_delete=models.CASCADE,related_name="sub_comm")  # blank=True 在django admin里面可以不填
    layer = models.IntegerField(default=1)
    touser = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='给谁回复',related_name='commentto',null=True,blank=True)

    def __str__(self):
        return str(self.user)+str(self.touser)

    class Meta:
        verbose_name = "文章评论"
        verbose_name_plural = verbose_name






