from django.db import models
from django.utils.timezone import now
from category.models import Category
from product.models import Product

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True, unique=True)
    product_name=models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    description = models.TextField(max_length=700, null=True, blank=True)
    DELIVERYS = (
        ('', 'Select'),
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
    )
    delivery = models.CharField(max_length=100, null=True, blank=True, choices=DELIVERYS)
    quantity = models.FloatField()
    unit_price=models.FloatField()
    total_price=models.FloatField(editable=False, default=0)
    created_date = models.DateTimeField(default=now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name.name

    def save(self,*args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super(Order, self).save(*args, **kwargs)
    
    # @property
    # def get_total(self):
    #     total = self.product.price * self.quantity
    #     return total

    # def save(self, *args, **kwargs):
    #     self.quantity = self.product_name.product_quantity - self.quantity
    #     super(Order, self).save(*args, **kwargs)