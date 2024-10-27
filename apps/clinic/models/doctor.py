from django.db import models

from .branch import Branch
from .tag import Tag
# Create your models here.
from apps.user.models import CustomUser
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
    patient=models.ManyToManyField('Patient', related_name='doctors',)
    tags = models.ManyToManyField(Tag)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



