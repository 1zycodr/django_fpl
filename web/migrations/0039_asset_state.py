# Generated by Django 3.1 on 2020-09-16 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0038_auto_20200907_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]