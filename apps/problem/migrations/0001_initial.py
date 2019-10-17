# Generated by Django 2.2.4 on 2019-08-21 21:21

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemAbstract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_disabled', models.BooleanField(default=False, verbose_name='是否私密')),
                ('title', models.CharField(max_length=30, verbose_name='题目标题')),
                ('pro_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='题目描述')),
                ('source', models.CharField(max_length=100, verbose_name='来源')),
                ('contest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contest.CodingContest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProblemTages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_disabled', models.BooleanField(default=False, verbose_name='是否私密')),
                ('name', models.TextField()),
            ],
            options={
                'verbose_name': '问题标签',
                'verbose_name_plural': '问题标签',
            },
        ),
        migrations.CreateModel(
            name='OtherProblem',
            fields=[
                ('problemabstract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problem.ProblemAbstract')),
                ('answer', models.TextField(verbose_name='答案')),
            ],
            options={
                'verbose_name': '非编程问题',
                'verbose_name_plural': '非编程问题',
            },
            bases=('problem.problemabstract',),
        ),
        migrations.CreateModel(
            name='CodingProlemInfo',
            fields=[
                ('problemabstract_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='problem.ProblemAbstract')),
                ('pro_input', DjangoUeditor.models.UEditorField(default='', verbose_name='输入描述')),
                ('pro_output', DjangoUeditor.models.UEditorField(default='', verbose_name='输出描述')),
                ('sample_input', DjangoUeditor.models.UEditorField(default='', verbose_name='样例输入')),
                ('sample_output', DjangoUeditor.models.UEditorField(default='', verbose_name='样例输出')),
                ('ac_number', models.IntegerField(default=0, verbose_name='总AC数')),
                ('submit_number', models.IntegerField(default=0, verbose_name='总提交数')),
                ('time_limit', models.IntegerField(default=1, verbose_name='限制时间 （ms）')),
                ('memory_limit', models.IntegerField(default=128, verbose_name='空间限制（mb）')),
                ('hit', models.CharField(max_length=30, verbose_name='题目提示')),
                ('spj', models.BooleanField(default=False, verbose_name='题目是否特判')),
                ('tags', models.ManyToManyField(to='problem.ProblemTages')),
            ],
            options={
                'verbose_name': '编程问题',
                'verbose_name_plural': '编程问题',
            },
            bases=('problem.problemabstract',),
        ),
    ]