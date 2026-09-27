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

