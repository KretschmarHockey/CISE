from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('results/', views.SearchResultsView.as_view(), name='results'),
    path('product-<int:pk>/', views.ProductView.as_view(), name='product')
]
