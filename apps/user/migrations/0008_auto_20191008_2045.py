# Generated by Django 2.2.4 on 2019-10-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20190928_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否隐藏'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否隐藏'),
        ),
        migrations.AlterField(
            model_name='userinfoimg',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否隐藏'),
        ),
    ]
