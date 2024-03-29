# Generated by Django 2.2.4 on 2019-09-13 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0003_auto_20190912_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codingproleminfo',
            name='hit',
            field=models.CharField(blank=True, default='无', max_length=30, null=True, verbose_name='题目提示'),
        ),
        migrations.AlterField(
            model_name='problemabstract',
            name='contest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contest.CodingContest'),
        ),
        migrations.AlterField(
            model_name='problemabstract',
            name='source',
            field=models.CharField(default='原创', max_length=100, verbose_name='来源'),
        ),
    ]
