from modeltranslation.translator import TranslationOptions, translator
from apps.clinic.models.branch import Branch, Director
from apps.clinic.models.doctor import Doctor
from apps.clinic.models.patient import Patient
from apps.clinic.models.appointment import Appointment
from apps.clinic.models.services import Service
from apps.clinic.models.tag import Tag


class DoctorTranslationOptions(TranslationOptions):
    fields = ("name", "address",  "gender")


class PatientTranslationOptions(TranslationOptions):
    fields = ("name", "address", "reason", "gender",)


class BranchTranslationOptions(TranslationOptions):
    fields = ("name", "address",)


class ServiceTranslationOptions(TranslationOptions):
    fields = ("name", "description",)


class TagTranslationOptions(TranslationOptions):
    fields = ("name", "type")


class DirectorTranslationOptions(TranslationOptions):
    fields = ("name", "address",)


class AppointmentTranslationOptions(TranslationOptions):
    fields = ( "status",)


# Регистрация моделей для перевода
translator.register(Doctor, DoctorTranslationOptions)
translator.register(Patient, PatientTranslationOptions)
translator.register(Branch, BranchTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
translator.register(Tag, TagTranslationOptions)
translator.register(Appointment, AppointmentTranslationOptions)
translator.register(Director, DirectorTranslationOptions)
