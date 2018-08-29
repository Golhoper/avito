from django.db import models
from Libraries import *


class AdditionalUserInfo(models.Model):
    class Meta:
        db_table = "user_info"
        verbose_name = "user_info"
        verbose_name_plural = "user_info_pl"
        required_db_vendor = "mysql"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField(auto_now=False, blank=True, null=True)
    avatar = models.ImageField(upload_to="users/avatars/")
    country = models.TextField(blank=True)
    city = models.TextField(blank=True)
    street = models.TextField(blank=True)
    house_number = models.TextField(blank=True, help_text="Номер дома")
    house_block = models.TextField(blank=True, help_text="Корпус дома")