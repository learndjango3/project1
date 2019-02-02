from django.shortcuts import render
from django.urls import path

from . import views

app_name='poll1'
urlpatterns = [
    path('', views.home, name='home'),
]

# Create your views here.
