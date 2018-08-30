from django.db import models


class Ad(models.Model):
    class Meta:
        db_table = "ad"
        verbose_name = "ad"
        verbose_name_plural = "ad_pl"
        required_db_vendor = "mysql"

    id = models.AutoField(primary_key=True)
    title = models.TextField(blank=False, null=False, default="No title")
    description = models.TextField(blank=False, null=False, default="no description")
    creation_date = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)