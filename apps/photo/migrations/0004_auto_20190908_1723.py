# Generated by Django 2.2.4 on 2019-09-08 17:23

from django.db import migrations, models
import utils.SomeSetting


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20190908_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photodetail',
            name='Img',
            field=models.ImageField(storage=utils.SomeSetting.LiterDocStorage(), upload_to='photo/', verbose_name='照片'),
        ),
    ]
