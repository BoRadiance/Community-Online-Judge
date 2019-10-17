from django.db import models
from base_model import BaseModel
from DjangoUeditor.models import UEditorField
from user.models import User

# Create your models here.
"""
这里给出oj的公告和博客的幻灯片
"""

class Announcement(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True,
                                      verbose_name='公告标题')

    content = UEditorField(verbose_name="公告内容", imagePath="announcement/images/", width=1000, height=300,
                              filePath="announcement/files/")


    Belong = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='发布者')


    def __str__(self):
        return self.title

    class Meta:
        db_table = "announcement"
        ordering = ("-create_time",)
        verbose_name = '首页公告'
        verbose_name_plural = verbose_name


class OjCarouselImg(BaseModel):
    image = models.ImageField(upload_to="announcement/", verbose_name="图片", null=True, blank=True)
    class Meta:
        verbose_name = 'OJ轮播图'
        verbose_name_plural = verbose_name



class BlogCarouselImg(BaseModel):
    image = models.ImageField(upload_to="announcement/", verbose_name="图片", null=True, blank=True)
    class Meta:
        verbose_name = '博客社区轮播图'
        verbose_name_plural = verbose_name



