from django.db import models
from .category import Category
class Service(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=250)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name