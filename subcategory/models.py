from django.db import models
from django.utils import timezone
from category.models import Category

# Create your models here.

class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100, null=True, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    created_date = models.DateTimeField(null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name    