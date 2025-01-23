from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    ArticleSerializer,
)
from .permissions import HasRole
from .models import Article


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": user_serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"detail": "Invalid credentials. Please try again."},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class DashboardView(APIView):
    permission_classes = [IsAuthenticated, HasRole]
    required_role = "student"

    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response(
            {"message": "Welcome to dashboard", "user": user_serializer.data}, 200
        )


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user.id)
        return Article.objects.filter(author=self.request.user.id)
