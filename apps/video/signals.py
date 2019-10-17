from django.db.models.signals import pre_save,pre_delete,post_save
from .models import Video
from django.dispatch import receiver
import os
from django.conf import settings

@receiver(pre_delete,sender=Video)
def pre_delet_signal(sender,instance=None,**kwargs):
    print('删除')
    print(instance.vid)
    print(settings.MEDIA_ROOT)
    # os.remove(settings.MEDIA_ROOT+'/'+str(instance.vid))

