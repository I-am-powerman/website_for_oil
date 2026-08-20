from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    price_50_ml = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_100_ml = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_250_ml = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_500_ml = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class Clients(models.Model):
    id = models.AutoField(primary_key=True)
    id_vk = models.IntegerField(null=True, blank=True)
    id_telegram = models.IntegerField(null=True, blank=True)
    name_first = models.CharField(max_length=255)
    name_last = models.CharField(max_length=255)
    address = models.CharField(max_length=255)