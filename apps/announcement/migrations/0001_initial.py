# Generated by Django 2.2.4 on 2019-08-21 18:30

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_disabled', models.BooleanField(default=True, verbose_name='是否私密')),
                ('title', models.TextField(blank=True, max_length=1024, null=True, verbose_name='公告标题')),
                ('content', DjangoUeditor.models.UEditorField(verbose_name='公告内容')),
                ('Belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '首页公告',
                'verbose_name_plural': '首页公告',
                'db_table': '公告',
                'ordering': ('-create_time',),
            },
        ),
    ]
