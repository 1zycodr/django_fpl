# Generated by Django 3.1 on 2020-09-17 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0040_auto_20200917_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='filee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.document', verbose_name='Документ'),
        ),
    ]
