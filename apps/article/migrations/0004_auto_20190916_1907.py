# Generated by Django 2.2.4 on 2019-09-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20190912_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_disabled',
            field=models.BooleanField(default=False, verbose_name='是否展示'),
        ),
    ]
