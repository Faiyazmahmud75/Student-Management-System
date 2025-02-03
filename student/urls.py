from django.urls import path, include
from . import views

urlpatterns = [
    path('create_student/', views.create_student, name='create_student'),
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),
]