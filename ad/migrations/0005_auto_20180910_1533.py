# Generated by Django 2.1 on 2018-09-10 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0004_ad_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['creation_date'], 'verbose_name': 'ad', 'verbose_name_plural': 'ad_pl'},
        ),
    ]
