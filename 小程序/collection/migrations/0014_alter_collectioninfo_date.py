# Generated by Django 3.2 on 2023-08-10 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0013_alter_collectioninfo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectioninfo',
            name='date',
            field=models.DateTimeField(verbose_name='处理时间'),
        ),
    ]
