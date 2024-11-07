from django.contrib import admin
from apps.clinic.models.branch import Branch, Director
from apps.clinic.models.doctor import Doctor
from apps.clinic.models.patient import Patient
from apps.clinic.models.appointment import Appointment
from apps.clinic.models.services import Service
from apps.clinic.models.tag import Tag


class AppointmentAdmin(admin.ModelAdmin):
    # Добавьте фильтры для полей doctor, patient, status, и date
    list_filter = ('doctor', 'patient', 'status', 'date')

    # Добавьте возможность поиска по полям name и email пациента и доктора
    search_fields = ('name', 'name', 'email', 'email')

    # Опционально: добавьте поля для отображения в списке
    list_display = ('doctor', 'patient', 'date', 'time', 'status')


class DoctorAdmin(admin.ModelAdmin):
    # Фильтрация по полям
    list_filter = ('gender', 'branch', 'tags')

    # Поиск по полям name, email, и phone_number
    search_fields = ('name', 'email', 'phone')

    # Поля для отображения в списке
    list_display = ('name', 'email', 'phone', 'gender', 'branch',)


class PatientAdmin(admin.ModelAdmin):
    # Фильтрация по полям
    list_filter = ('gender', 'birth_date', 'date_attended')

    # Поиск по полям name, email, и phone_number
    search_fields = ('name', 'email', 'phone_number')

    # Поля для отображения в списке
    list_display = ('name', 'email', 'phone_number', 'birth_date', 'gender', 'date_attended')


# Зарегистрируйте модель и класс админки


# Register your models here.
admin.site.register(Branch)
admin.site.register(Director)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Tag)
admin.site.register(Service)