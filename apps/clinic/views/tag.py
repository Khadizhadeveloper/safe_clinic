from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.clinic.models.tag import Tag, TagType
from apps.clinic.permissions import IsAdminUser, IsDirectorUser
from apps.clinic.serializers.tag import TagSerializer


class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset=Tag.objects.all()

        if self.request.user.is_authenticated and self.request.user.role=='patient':
            queryset = queryset.filter(type=TagType.SPECIALIZATION)

        return queryset

class TagCreateView(generics.CreateAPIView):
    serializer_class = TagSerializer

    def get_permissions(self):
        if self.request.data.get('type') == TagType.SPECIALIZATION:
            return [IsAuthenticated,IsAdminUser() | IsDirectorUser()]
        return [IsAdminUser()]


class TagUpdateView(generics.UpdateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def get_permissions(self):
        tag=self.get_object()
        if tag.type == TagType.SPECIALIZATION:
            return [IsAuthenticated(),IsAdminUser() | IsDirectorUser()]
        return [IsAdminUser()]

class TagDestroyView(generics.DestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def get_permissions(self):
        tag = self.get_object()
        if tag.type == TagType.SPECIALIZATION:
            return [IsAuthenticated(), IsAdminUser() | IsDirectorUser()]
        return [IsAdminUser()]
