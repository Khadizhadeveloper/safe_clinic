from django.db import models
from .doctor import Gender, Doctor


class Patient(models.Model):
    name=models.CharField(max_length=200)
    birth_date=models.DateField()
    address=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    gender=models.CharField(max_length=200, choices=Gender.choices)
    reason=models.CharField(max_length=300)
    date_attended=models.DateField()
    doctors=models.ManyToManyField(Doctor)
