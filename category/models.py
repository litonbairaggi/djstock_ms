from django.db import models
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, unique=True, blank=True)
    created_date = models.DateTimeField(default=now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name      