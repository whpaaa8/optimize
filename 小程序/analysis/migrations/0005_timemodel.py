# Generated by Django 3.2 on 2023-08-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analysis', '0004_delete_timemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(verbose_name='时间')),
                ('report_link', models.CharField(default='', max_length=20, verbose_name='数据分析结果')),
            ],
        ),
    ]
