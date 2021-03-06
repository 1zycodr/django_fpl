# Generated by Django 3.1 on 2020-09-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_auto_20200904_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finotchet',
            name='file2',
        ),
        migrations.AddField(
            model_name='audit',
            name='file2',
            field=models.FileField(default='', upload_to='file/', verbose_name='Консолидированная финансовая отчётность'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audit',
            name='file',
            field=models.FileField(upload_to='file/', verbose_name='Финансовая отчётность'),
        ),
        migrations.AlterField(
            model_name='finotchet',
            name='file',
            field=models.FileField(upload_to='file/', verbose_name='Документ'),
        ),
    ]
