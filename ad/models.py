from Libraries import *
from django.db import models
from user.models import AdditionalUserInfo


class Category(models.Model):
    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "category_pl"
        required_db_vendor = "mysql"

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=40, blank=False, null=False)


class Ad(models.Model):
    class Meta:
        db_table = "ad"
        verbose_name = "ad"
        verbose_name_plural = "ad_pl"
        required_db_vendor = "mysql"
        ordering = ['creation_date']

    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=False, null=False, default="No title")
    description = models.TextField(blank=False, null=False, default="no description")
    creation_date = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    category = models.ForeignKey(Category, models.SET_NULL, blank=False, null=True, default=5)


class Favourites(models.Model):
    class Meta:
        db_table = "favourites"
        verbose_name = "favourites"
        verbose_name_plural = "favourites_pl"
        required_db_vendor = "mysql"
        ordering = ['-creation_date']

    id = models.AutoField(primary_key=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)