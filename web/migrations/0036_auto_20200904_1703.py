# Generated by Django 3.1 on 2020-09-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0035_auto_20200904_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='file/', verbose_name='Консолидированная финансовая отчётность'),
        ),
        migrations.AlterField(
            model_name='audit',
            name='image',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='Фоновая картинка'),
        ),
    ]
