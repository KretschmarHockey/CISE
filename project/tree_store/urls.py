from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='index'),
    path('results/', views.SearchResultsView.as_view(), name='results'),
]