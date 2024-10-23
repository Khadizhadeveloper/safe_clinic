from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    director=models.ManyToManyField('Director')
    def __str__(self):
        return self.name