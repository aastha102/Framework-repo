from django.urls import path
from .views import Customer, CustomerDetial

urlpatterns = [
    path('customers/', Customer.as_view()),
    path('customer/<pk>/', CustomerDetial.as_view())
]