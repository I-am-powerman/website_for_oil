from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    id_vk = models.IntegerField(null=True, blank=True)
    id_telegram = models.IntegerField(null=True, blank=True)
    name_first = models.CharField(max_length=255)
    name_last = models.CharField(max_length=255)
    address = models.CharField(max_length=255)