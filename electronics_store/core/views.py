from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserRetrieveUpdateSerializer, \
    PasswordUpdateSerializer


class UserRegistrationView(CreateAPIView):
    """Create new user"""
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserLoginView(CreateAPIView):
    """Login user"""
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        # validate request data
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # authenticate
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        # login
        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)

        return Response(data={'password': ['Invalid password']}, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class PasswordUpdateView(UpdateAPIView):
    serializer_class = PasswordUpdateSerializer
    model = User
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({"old_password": ["Wrong password passed, try again."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
