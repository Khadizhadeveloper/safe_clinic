from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.clinic.permissions import IsDoctorUser, IsDirectorUser, IsAdminUser
from apps.clinic.models.patient import Patient
from apps.clinic.serializers.patient import PatientSerializer
from django_filters import rest_framework as filters

# Фильтр для поиска пациентов
class PatientFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Patient
        fields = ['name']

# Список пациентов — доступен для врачей, директоров и администраторов
class PatientListView(ListAPIView):
    serializer_class = PatientSerializer
    permission_classes = (IsDoctorUser | IsDirectorUser | IsAdminUser,)
    filterset_class = PatientFilter

    def get_queryset(self):
        # Фильтрация по врачу, если текущий пользователь — врач
        queryset = Patient.objects.all()
        if self.request.user.role == 'doctor':
            queryset = queryset.filter(doctor=self.request.user)
        return queryset

# Детали пациента — доступ для врачей, директоров и администраторов
class PatientRetrieveView(RetrieveAPIView):
    serializer_class = PatientSerializer
    permission_classes = (IsDoctorUser | IsDirectorUser | IsAdminUser,)

    def get_queryset(self):
        queryset = Patient.objects.all()
        if self.request.user.role == 'doctor':
            queryset = queryset.filter(doctor=self.request.user)
        return queryset

# Создание пациента — доступно только для администраторов
class PatientCreateView(CreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = (IsAdminUser,)

# Обновление пациента — доступ для врача и администратора
class PatientUpdateView(UpdateAPIView):
    serializer_class = PatientSerializer
    permission_classes = (IsDoctorUser | IsAdminUser,)

    def get_queryset(self):
        queryset = Patient.objects.all()
        if self.request.user.role == 'doctor':
            queryset = queryset.filter(doctor=self.request.user)
        return queryset

# Удаление пациента — доступ для врача, директора и администратора
class PatientDestroyView(DestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        queryset = Patient.objects.all()
        if self.request.user.role == 'doctor':
            queryset = queryset.filter(doctor=self.request.user)
        return queryset
