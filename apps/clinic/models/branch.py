from django.db import models
class Director(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    director=models.ForeignKey(Director, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

