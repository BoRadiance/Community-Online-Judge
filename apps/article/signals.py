from django.db.models.signals import pre_save,pre_delete,post_save,post_delete
from .models import Article,ArticleUpDown,Comment
from django.dispatch import receiver
from django.utils.html import strip_tags

@receiver(post_save,sender=Article)
def save_pre_signals(sender, instance=None, created=False, **kwargs):
    # print('保存之后')
    if created:
        instance.desc = strip_tags(instance.content)[:50]+"..."
        # instance.browse += 1
        instance.save()


@receiver(post_save,sender=ArticleUpDown)
def create_signals(sender, instance=None, created=False, **kwargs):
    # print('创建')
    if created:
        obj = instance.article
        obj.ThumbsUp += 1
        obj.save()


@receiver(post_delete,sender=ArticleUpDown)
def post_signals(sender, instance=None, created=False, **kwargs):
    # print('删除')
    obj = instance.article
    obj.ThumbsUp -= 1
    obj.save()


@receiver(pre_save,sender=Comment)
def comment_post_save(sender, instance=None, created=False, **kwargs):
    print('add comment')
    print(instance.parent_comment)
    print(instance.touser)
    obj = instance.article
    obj.CommentCount += 1
    obj.save()
    if instance.parent_comment :
        print(instance.parent_comment)
        instance.layer = 2









@receiver(post_delete,sender=Comment)
def comment_post_delete(sender, instance=None, created=False, **kwargs):
    obj = instance.article
    obj.CommentCount -= 1
    obj.save()

