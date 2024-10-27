from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from apps.clinic.models.tag import Tag, TagType


# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('director', 'Director'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]

    role = models.CharField(choices=ROLE_CHOICES, max_length=50)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    specialization = models.ForeignKey(
        Tag,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        limit_choices_to={'tag_type': TagType.SPECIALIZATION})

    # Переопределите поля groups и user_permissions с unique related_name
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Уникальное имя обратной ссылки
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Уникальное имя обратной ссылки
        blank=True,
    )

    def __str__(self):
        return f"{self.email} ({self.role})"

