from django.db import models
from user.models import User
from base_model import BaseModel
from utils.SomeSetting import LiterDocStorage

# Create your models here.

class Video(BaseModel):
    Desc = models.TextField(max_length=1024,
                            verbose_name='视频描述')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    vid = models.FileField(upload_to='video/',

                           verbose_name="视频",storage= LiterDocStorage())


    def __str__(self):
        return  str(self.user) + '->' +str(self.Desc)

    class Meta:
        verbose_name='用户视频'
        verbose_name_plural = verbose_name




