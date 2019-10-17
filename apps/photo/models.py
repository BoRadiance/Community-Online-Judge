from django.db import models
from user.models import User
from base_model import BaseModel
from utils.SomeSetting import LiterDocStorage
# Create your models here.

class Photos(BaseModel):
    Desc = models.TextField(max_length=1024,
                                      verbose_name='相册描述')

    user = models.ForeignKey(User,on_delete=models.CASCADE,)


    def __str__(self):
        return  str(self.user)+"->"+str(self.Desc)

    class Meta:
        verbose_name='用户相册'
        verbose_name_plural = verbose_name




class PhotoDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    Belong = models.ForeignKey(Photos,on_delete=models.CASCADE,related_name='pic')

    Img =  models.ImageField(upload_to="photo/",
                                             verbose_name="照片",
                                            storage= LiterDocStorage(),
                             )

    def __str__(self):
        return  str(self.Belong)

    class Meta:
        verbose_name='用户照片'
        verbose_name_plural = verbose_name




