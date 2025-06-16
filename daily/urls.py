from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_form, name='task_form'),
    path('edit/<int:row_id>/', views.task_form, name='edit_task'),
    path('delete/<int:row_id>/', views.delete_task, name='delete_task'),
]
