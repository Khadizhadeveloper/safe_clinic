from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from apps.clinic.models.doctor import Doctor
from apps.clinic.models.tag import Tag
from apps.clinic.models.branch import Branch
from apps.clinic.permissions import IsAdminUser, IsDoctorUser, IsDirectorUser
from apps.clinic.serializers.doctor import DoctorSerializer
from django_filters import rest_framework as filters


class DoctorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    tag = filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all())
    branch = filters.ModelMultipleChoiceFilter(queryset=Branch.objects.all())

    class Meta:
        model = Doctor
        fields = ['name', 'tag', 'branch']


# Список врачей — доступен всем
class DoctorListView(ListAPIView):
    serializer_class = DoctorSerializer
    permission_classes = (AllowAny,)
    filterset_class = DoctorFilter

    def get_queryset(self):
        queryset = Doctor.objects.all()
        if self.request.user.is_authenticated and self.request.user.role == 'director':
            queryset = queryset.filter(branch=self.request.user.branch)
        return queryset


# Создание врача — доступно только для администраторов
class DoctorCreateView(CreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = (IsAdminUser,)
    queryset = Doctor.objects.all()


# Обновление врача — доступно для администратора, директора (своего филиала), и для самого врача
class DoctorUpdateView(UpdateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = (IsAdminUser | IsDirectorUser | IsDoctorUser,)

    def get_queryset(self):
        queryset = Doctor.objects.all()
        if self.request.user.role == 'director':
            queryset = queryset.filter(branch=self.request.user.branch)
        elif self.request.user.role == 'doctor':
            queryset = queryset.filter(id=self.request.user.id)  # Врач может обновлять только свои данные
        return queryset


# Получение данных врача — доступно для врачей, директоров и администраторов
class DoctorRetrieveView(RetrieveAPIView):
    serializer_class = DoctorSerializer
    permission_classes = (IsDoctorUser | IsDirectorUser | IsAdminUser,)
    queryset = Doctor.objects.all()


# Удаление врача — доступно для администраторов и директоров
class DoctorDestroyView(DestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = (IsAdminUser | IsDirectorUser,)

    def get_queryset(self):
        queryset = Doctor.objects.all()
        if self.request.user.role == 'director':
            queryset = queryset.filter(branch=self.request.user.branch)
        return queryset
