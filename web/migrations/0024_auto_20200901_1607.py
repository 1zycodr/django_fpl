# Generated by Django 3.1 on 2020-09-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_auto_20200901_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='price',
            field=models.CharField(max_length=250, verbose_name='Цена'),
        ),
    ]
