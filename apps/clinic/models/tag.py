from django.db import models


class TagType(models.TextChoices):
    ROLE='role', 'Role'
    SPECIALIZATION='specialization', 'Specialization'


class Tag(models.Model):
    name=models.CharField(max_length=100, verbose_name='Название тега')
    type=models.CharField(max_length=30, choices=TagType.choices)
    def __str__(self):
        return self.name
