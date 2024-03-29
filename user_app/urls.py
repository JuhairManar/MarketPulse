from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',RegistrationView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
]