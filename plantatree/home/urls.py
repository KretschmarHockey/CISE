from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]