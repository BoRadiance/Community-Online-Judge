# Generated by Django 2.2.4 on 2019-09-27 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0011_trendphoto_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trendphoto',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
