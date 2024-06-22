from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics

User = get_user_model()

# class ObtainTokenView(TokenObtainPairView):
#     permission_classes = [AllowAny]
#     serializer_class = TokenObtainPairSerializer
    

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
