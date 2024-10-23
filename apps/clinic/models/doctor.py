from django.db import models
from .doctortag import Tag
# Create your models here.

class Gender(models.TextChoices):
    MALE = 'Male','Male'
    FEMALE = 'Female','Female'
    OTHER = 'Other','Other'

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    birth_date = models.DateField()
    address = models.CharField(max_length=200)
    gender=models.CharField(max_length=50,choices=Gender.choices)
    patient=models.ForeignKey('Patient',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

