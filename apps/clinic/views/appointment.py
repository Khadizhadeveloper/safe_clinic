from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.clinic.models.appointment import Appointment, AppointmentStatus
from apps.clinic.serializers.appointment import AppointmentSerializer
from apps.clinic.permissions import IsDoctorUser, IsAdminUser, IsPatientUser, IsDirectorUser


class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user=self.request.user
        if user.role == 'patient':
            return Appointment.objects.filter(patient=user)
        elif user.role == 'doctor':
            return Appointment.objects.filter(doctor=user)
        else:
            return Appointment.objects.all()


class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsPatientUser,]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)


class AppointmentUpdateView(generics.UpdateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsPatientUser| IsDoctorUser | IsAdminUser]
    queryset = Appointment.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        status=request.data.get('status')
        if status not in dict(AppointmentStatus.choices):
            return Response({'error':'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        instance.status = status
        instance.save()
        return Response({'status':'Appointment status updated'}, status=status.HTTP_200_OK)
