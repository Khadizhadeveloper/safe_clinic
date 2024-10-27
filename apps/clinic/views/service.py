from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.clinic.models.branch import Branch
from apps.clinic.models.services import Service
from apps.clinic.permissions import IsAdminUser, IsDirectorUser
from apps.clinic.serializers.service import ServiceSerializer
from django_filters import rest_framework as filters

class ServiceFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    branch=filters.ModelMultipleChoiceFilter(queryset=Branch.objects.all())

    class Meta:
        model = Service
        fields = ['name', 'branch']


class ServiceListView(ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (AllowAny,)
    queryset = Service.objects.all()
    filterset_class = ServiceFilter


class ServiceRetrieveView(RetrieveAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (AllowAny,)
    queryset = Service.objects.all()


class ServiceCreateView(CreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminUser,IsDirectorUser)


class ServiceUpdateView(UpdateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminUser, IsDirectorUser)
    queryset = Service.objects.all()


class ServiceDestroyView(DestroyAPIView):
    serializer_class = ServiceSerializer
    permission_classes = (IsAdminUser, IsDirectorUser)
    queryset = Service.objects.all()