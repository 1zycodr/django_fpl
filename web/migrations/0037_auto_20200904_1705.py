# Generated by Django 3.1 on 2020-09-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0036_auto_20200904_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='f1_title',
            field=models.CharField(default='', max_length=50, verbose_name='Название файла 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='audit',
            name='f2_title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название файла 2'),
        ),
        migrations.AlterField(
            model_name='audit',
            name='file',
            field=models.FileField(upload_to='file/', verbose_name='Файл 1'),
        ),
    ]