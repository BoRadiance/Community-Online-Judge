# Generated by Django 2.2.4 on 2019-08-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_auto_20190821_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否私密'),
        ),
        migrations.AlterField(
            model_name='blogcarouselimg',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否私密'),
        ),
        migrations.AlterField(
            model_name='ojcarouselimg',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否私密'),
        ),
    ]
