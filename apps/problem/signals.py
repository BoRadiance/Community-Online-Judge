from django.db.models.signals import pre_save,pre_delete,post_save,post_delete
from .models import CodingProlemInfo
from django.dispatch import receiver
from django.utils.html import strip_tags

@receiver(pre_save,sender=CodingProlemInfo)
def save_pre_codingproblem(sender, instance=None, created=False, **kwargs):
    instance.is_disabled = True
    instance.ac_number = 0
    instance.submit_number = 0

