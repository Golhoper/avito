# Generated by Django 2.1 on 2018-09-11 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0006_auto_20180910_1534'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['creation_date'], 'verbose_name': 'ad', 'verbose_name_plural': 'ad_pl'},
        ),
    ]
