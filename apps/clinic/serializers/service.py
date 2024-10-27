from rest_framework import serializers
from apps.clinic.models.services import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'