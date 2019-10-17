from django.db.models.signals import pre_save,pre_delete,post_save
from .models import PhotoDetail
from django.dispatch import receiver
import os
from django.conf import settings


@receiver(post_save,sender=PhotoDetail)
def save_pre_signals(sender, instance=None, created=False, **kwargs):
    print('保存之后')
    if created:
        print(instance)
        print(kwargs)
        if instance.user != instance.Belong.user:
            del instance




@receiver(pre_delete,sender=PhotoDetail)
def delete_pre_signals(sender,instance=None,**kwargs):
    print('删除之前')
    print(instance.user)
    print(instance.Belong.user)
    print(instance.Img)
    print(kwargs)
    # os.remove(settings.MEDIA_ROOT + '/' + str(instance.Img))

