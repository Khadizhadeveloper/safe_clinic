from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
    )
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from apps.clinic.models.branch import Branch, Director
from apps.clinic.serializers.branch import BranchSerializer, DirectorSerializer
from apps.clinic.permissions import IsAdminUser, IsDirectorUser


class BranchListView(ListAPIView):
    serializer_class = BranchSerializer
    permission_classes = (AllowAny,)
    queryset = Branch.objects.all()

class BranchRetrieveView(RetrieveAPIView):
    serializer_class = BranchSerializer
    permission_classes = (AllowAny,)
    queryset = Branch.objects.all()

class BranchCreateView(CreateAPIView):
    serializer_class = BranchSerializer
    permission_classes = (IsAdminUser,)

class BranchUpdateView(UpdateAPIView):
    serializer_class = BranchSerializer
    permission_classes = (IsAdminUser,IsDirectorUser)
    queryset = Branch.objects.all()

class BranchDestroyView(DestroyAPIView):
    serializer_class = BranchSerializer
    permission_classes = (IsAdminUser,)

class DirectorListCreateView(ListCreateAPIView):
    serializer_class = DirectorSerializer
    permission_classes = (IsAdminUser,)

class DirectorRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = DirectorSerializer
    permission_classes = (IsAdminUser,)





