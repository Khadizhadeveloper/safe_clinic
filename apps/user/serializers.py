from rest_framework import serializers
from .models import CustomUser
from apps.clinic.models.tag import Tag, TagType

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'role', 'phone_number', 'birth_date', 'specialization', 'is_active', 'password']

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, data):
        # Проверка, что у врачей есть специализация, а у других ролей она не указана
        if data.get('role') == 'doctor':
            specialization = data.get('specialization')
            if not specialization or specialization.tag_type != TagType.SPECIALIZATION:
                raise serializers.ValidationError("Doctors must have a valid specialization.")
        elif data.get('specialization') is not None:
            raise serializers.ValidationError("Only doctors can have a specialization.")
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
