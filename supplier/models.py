from django.db import models
from django.utils.timezone import now

# Create your models here.

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.supplier_name
