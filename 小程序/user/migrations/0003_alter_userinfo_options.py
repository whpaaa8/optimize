# Generated by Django 3.2 on 2023-08-07 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20230807_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'ordering': ['username'], 'verbose_name': '用户信息'},
        ),
    ]
