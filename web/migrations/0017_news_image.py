# Generated by Django 3.1 on 2020-08-31 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20200831_0449'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default='', upload_to='img/', verbose_name='Фото'),
            preserve_default=False,
        ),
    ]
