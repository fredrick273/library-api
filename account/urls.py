from .views import RegisterView,UserListView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path("",UserListView.as_view(),name='user-list'),
    path('register/',RegisterView.as_view(),name='register-account'),
    path("login/",TokenObtainPairView.as_view()),
    path("login/refresh/",TokenRefreshView.as_view()),

]