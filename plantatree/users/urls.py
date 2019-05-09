from django.urls import path
from . import views

urlPatterns = [
    path('register/', views.register, name='register'),
]