# Generated by Django 2.2.4 on 2019-10-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0010_auto_20191008_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否可用'),
        ),
    ]
