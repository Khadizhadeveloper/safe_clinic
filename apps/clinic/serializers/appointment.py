from rest_framework import serializers
from apps.clinic.models.appointment import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'time', 'status']
        read_only_fields = ['status']
