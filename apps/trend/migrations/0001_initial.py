# Generated by Django 2.2.4 on 2019-08-21 20:56

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
            name='Trend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_disabled', models.BooleanField(default=False, verbose_name='是否私密')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='动态内容')),
                ('State', models.IntegerField(choices=[(1, '审核通过'), (2, '审核中'), (3, '审核不通过')], default=1, verbose_name='审核状态')),
                ('browse', models.IntegerField(default=0, verbose_name='浏览量')),
                ('ThumbsUp', models.IntegerField(default=0, verbose_name='点赞量')),
                ('CommentCount', models.IntegerField(default=0, verbose_name='评论数')),
                ('Belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发表者')),
            ],
            options={
                'verbose_name': '个人动态',
                'verbose_name_plural': '个人动态',
            },
        ),
        migrations.CreateModel(
            name='TrendUpDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_up', models.BooleanField(default=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trend.Trend')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '动态点赞',
                'verbose_name_plural': '动态点赞',
            },
        ),
        migrations.CreateModel(
            name='TrendComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trend.Trend')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trend.TrendComment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '动态评论',
                'verbose_name_plural': '动态评论',
            },
        ),
    ]
