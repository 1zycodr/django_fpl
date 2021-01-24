# Generated by Django 3.1 on 2020-09-01 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_asset_visits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='as_type',
            field=models.CharField(choices=[('IN', 'На повышение цены'), ('DE', 'На понижение цены')], max_length=30, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='as_type_en',
            field=models.CharField(choices=[('IN', 'На повышение цены'), ('DE', 'На понижение цены')], max_length=30, null=True, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='as_type_kk',
            field=models.CharField(choices=[('IN', 'На повышение цены'), ('DE', 'На понижение цены')], max_length=30, null=True, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='as_type_ru',
            field=models.CharField(choices=[('IN', 'На повышение цены'), ('DE', 'На понижение цены')], max_length=30, null=True, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='image',
            field=models.ImageField(upload_to='img/', verbose_name='Фото', width_field='200px'),
        ),
    ]