# Generated by Django 3.1 on 2020-09-04 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0030_auto_20200904_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='finotchet',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
