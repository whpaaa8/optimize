# Generated by Django 3.2 on 2023-08-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20230817_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemodel',
            name='timestamp',
            field=models.DateField(verbose_name='时间'),
        ),
    ]
