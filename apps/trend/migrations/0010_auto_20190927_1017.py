# Generated by Django 2.2.4 on 2019-09-27 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0009_auto_20190927_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trend',
            old_name='BelongTrendClass',
            new_name='tags',
        ),
        migrations.RenameField(
            model_name='trend',
            old_name='Belong',
            new_name='user',
        ),
    ]
