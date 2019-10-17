# 使用celery
from django.core.mail import send_mail
from django.conf import settings
from celery import Celery
import time

# 如果把任务处理者单独放在一台机器
# 在任务处理者一端加这几句
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ojblog.settings")
django.setup()

# 创建一个Celery类的实例对象
app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/8')


# 定义任务函数
@app.task
def send_register_active_email(to_email, username, token):
    print('------------------')
    print('发送邮件')
    print('------------------')
    '''发送激活邮件'''
    # 组织邮件信息
    subject = '南理社区欢迎信息'
    message = ''
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '<h1>%s, 欢迎您成为成功注册南理社区账号</h1>请点击下面链接激活您的账户,如果不进行激活将在明天删除您的账号信息!<br/><a href="http://127.0.0.1:8000/activeuser/%s">http://127.0.0.1:8000/activeuser/%s</a>' % (username, token, token)

    send_mail(subject, message, sender, receiver, html_message=html_message)

