from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import UserSerializer
from .models import UserData
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions


# view for registering users
class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserData.objects.all()
    permission_classes = [ IsAdminUser ]

class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserData.objects.all()
    permission_classes = [ IsAdminUser ]
    