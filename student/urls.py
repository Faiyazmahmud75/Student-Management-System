from django.urls import path, include
from . import views

urlpatterns = [
    path('students/', views.student),
    path('view_students/', views.all_students),
]