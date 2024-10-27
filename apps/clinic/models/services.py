from django.db import models
from apps.clinic.models.branch import Branch

class Service(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True, null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    branch=models.ManyToManyField(Branch, related_name='services')

    def __str__(self):
        return self.name