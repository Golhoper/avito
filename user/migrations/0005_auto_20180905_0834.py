# Generated by Django 2.1 on 2018-09-05 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='to_whom_send',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='whom', to=settings.AUTH_USER_MODEL, verbose_name='Кому отправляют'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='who_send',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='who', to=settings.AUTH_USER_MODEL, verbose_name='Кто отправляет'),
        ),
    ]