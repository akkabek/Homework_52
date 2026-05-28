from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.task_add, name='task_add'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
]
