from re import I
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from more_itertools import quantify
from django.db.models import Sum
from category.models import Category
from supplier.models import Supplier

class Product(models.Model):
    name=models.CharField(max_length=250,blank=True, null=True)
    code=models.CharField(max_length=100,blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=False)
    description = models.TextField()
    product_quantity = models.FloatField()
    unit_price=models.FloatField()
    total_price=models.FloatField(editable=False, default=0)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name + ' - ' + self.code

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        self.total_price = self.product_quantity * self.unit_price
        super(Product, self).save(*args, **kwargs)
