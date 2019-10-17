# Generated by Django 2.2.4 on 2019-09-26 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0006_auto_20190926_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_disabled', models.BooleanField(default=False, verbose_name='是否展示')),
                ('title', models.TextField(verbose_name='动态类别')),
            ],
            options={
                'verbose_name': '动态类',
                'verbose_name_plural': '动态类',
            },
        ),
        migrations.AddField(
            model_name='trend',
            name='BelongTrendClass',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trend.TrendClass', verbose_name='所属于类别'),
        ),
    ]
