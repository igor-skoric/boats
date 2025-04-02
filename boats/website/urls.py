from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('service_details', views.service_details, name='service_details'),
    path('products/<str:product_type>/', views.products, name='products'),
    path('product_details/<str:slug>/', views.product_details, name='product_details'),

]
