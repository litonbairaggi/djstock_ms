from re import I
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from more_itertools import quantify
from django.db.models import Sum
from category.models import Category

class Product(models.Model):
    name=models.CharField(max_length=250,blank=True, null=True)
    code=models.CharField(max_length=100,blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    description = models.TextField()
    product_quantity = models.FloatField(default=0, blank=True)
    unit_price=models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True, blank=True)
    total_price=models.DecimalField(default=0.00, max_digits=10, decimal_places=2, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.code
