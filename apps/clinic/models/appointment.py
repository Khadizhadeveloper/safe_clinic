from email.policy import default

from django.db import models
from apps.clinic.models.doctor import Doctor
from apps.clinic.models.patient import Patient
from apps.user.models import CustomUser

class AppointmentStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    CONFIRMED = 'confirmed', 'Confirmed'
    CANCELLED = 'cancelled', 'Cancelled'

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    status=models.CharField(max_length=20, choices=AppointmentStatus.choices, default=AppointmentStatus.PENDING)

    def __str__(self):
        return f"Appointment for {self.patient.name} with {self.doctor.name} on {self.date} at {self.time}"
