# Generated by Django 3.1 on 2020-09-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_auto_20200901_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='visits',
            field=models.IntegerField(default=0),
        ),
    ]