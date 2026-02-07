from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.StudentView),
    path('student/<int:pk>', views.StudentDetailView)
]