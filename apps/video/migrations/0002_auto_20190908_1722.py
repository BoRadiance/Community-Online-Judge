# Generated by Django 2.2.4 on 2019-09-08 17:22

from django.db import migrations, models
import utils.SomeSetting


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='vid',
            field=models.FileField(storage=utils.SomeSetting.LiterDocStorage(), upload_to='video/', verbose_name='视频'),
        ),
    ]
