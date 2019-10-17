from django.db import models

class BaseModel(models.Model):
    '''
    一般的模型基类
    '''
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_disabled = models.BooleanField(default=False, verbose_name='是否不可用')

    class Meta:
        abstract = True




