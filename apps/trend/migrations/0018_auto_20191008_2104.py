# Generated by Django 2.2.4 on 2019-10-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0017_auto_20191008_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否可用'),
        ),
        migrations.AlterField(
            model_name='trendclass',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否可用'),
        ),
    ]