# Generated by Django 2.2.4 on 2019-10-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0006_auto_20190916_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemabstract',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否隐藏'),
        ),
        migrations.AlterField(
            model_name='problemtages',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否隐藏'),
        ),
    ]
