# Generated by Django 2.1 on 2018-08-30 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180829_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaluserinfo',
            name='metro',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='additionaluserinfo',
            name='phone_mobile',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
