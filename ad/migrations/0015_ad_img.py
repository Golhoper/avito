# Generated by Django 2.1 on 2018-10-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0014_auto_20180924_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='img',
            field=models.ImageField(blank=True, upload_to='users/ad/'),
        ),
    ]