# Generated by Django 3.1 on 2020-09-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0052_auto_20200920_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_kk',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='document',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
    ]
