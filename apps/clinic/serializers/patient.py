from rest_framework import serializers
from apps.clinic.models.patient import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'