# Generated by Django 3.1 on 2020-09-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_auto_20200901_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file/', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'внешний аудит',
                'verbose_name_plural': 'Внешние аудиты',
            },
        ),
        migrations.CreateModel(
            name='FinOtchet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='file/', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'финансовый отчёт',
                'verbose_name_plural': 'Финансовые отчёты',
            },
        ),
    ]