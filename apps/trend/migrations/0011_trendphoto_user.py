# Generated by Django 2.2.4 on 2019-09-27 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trend', '0010_auto_20190927_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='trendphoto',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
