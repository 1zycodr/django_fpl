# Generated by Django 3.1 on 2020-08-30 19:13

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='discription',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Информация'),
        ),
        migrations.AddField(
            model_name='leader',
            name='image',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='Фото'),
        ),
    ]
