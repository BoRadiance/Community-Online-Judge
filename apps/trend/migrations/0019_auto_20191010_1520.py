# Generated by Django 2.2.4 on 2019-10-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0018_auto_20191008_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否不可用'),
        ),
        migrations.AlterField(
            model_name='trendclass',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否不可用'),
        ),
    ]
