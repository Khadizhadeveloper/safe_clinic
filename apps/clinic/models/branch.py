from django.db import models
from django.utils.translation import gettext_lazy as _
class Director(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    address = models.CharField(max_length=255, verbose_name=_('Address'))
    phone = models.CharField(max_length=255, verbose_name=_('Phone'))
    birth_date = models.DateField(verbose_name=_('Birth date'))

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    address = models.CharField(max_length=255, verbose_name=_('Address'))
    phone = models.CharField(max_length=255, verbose_name=_('Phone'))
    director=models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name=_('Director'))
    def __str__(self):
        return self.name

