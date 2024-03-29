# Generated by Django 2.2.4 on 2019-09-27 10:06

from django.db import migrations, models
import utils.SomeSetting


class Migration(migrations.Migration):

    dependencies = [
        ('trend', '0008_auto_20190926_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='trend',
            name='desc',
            field=models.CharField(default='', max_length=255, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='trendphoto',
            name='Image',
            field=models.ImageField(blank=True, null=True, storage=utils.SomeSetting.LiterDocStorage(), upload_to='trend/', verbose_name='个人动态的图片'),
        ),
    ]
