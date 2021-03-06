# Generated by Django 3.1 on 2020-09-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0037_auto_20200904_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audit',
            options={'verbose_name': 'внешний аудит', 'verbose_name_plural': 'Внешний аудит'},
        ),
        migrations.AddField(
            model_name='purchase',
            name='desc_file_title',
            field=models.CharField(default='', max_length=250, verbose_name='Название файла описания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audit',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='file/', verbose_name='Файл 2'),
        ),
    ]
