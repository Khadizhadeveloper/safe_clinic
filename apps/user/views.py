from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Регистрация пользователя (только для админа)
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # Только администратор может регистрировать новых пользователей

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user_email = request.data.get('email')
        self.send_welcome_email(user_email)
        return response

    def send_welcome_email(self, email):
        subject = 'Welcome to Our Clinic'
        message = 'Your account has been created by an admin. Please log in using your email and password.'
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

# Аутентификация пользователя (доступ для всех)
class LoginAPIView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            # Generate or retrieve token
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'email': email}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

