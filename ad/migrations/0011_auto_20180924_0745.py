# Generated by Django 2.1 on 2018-09-24 07:45

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0010_auto_20180924_0733'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='ad',
            managers=[
                ('all_managers', django.db.models.manager.Manager()),
            ],
        ),
    ]