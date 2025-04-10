from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('service_details/', views.service_details, name='service_details'),
    path('products/', views.products, {'product_type': 'all'}, name='all_products'),  # Svi proizvodi
    path('products/new/', views.products, {'product_type': 'new'}, name='new_products'),  # Novi proizvodi
    path('products/used/', views.products, {'product_type': 'used'}, name='used_products'),  # Polovni proizvodi
    path('product_details/<str:slug>/', views.product_details, name='product_details'),

]
