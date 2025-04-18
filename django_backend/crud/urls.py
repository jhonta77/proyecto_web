from django.urls import path
from . import views


app_name = 'crud_list' 

urlpatterns = [
    path('', views.task_list_and_create, name='task_list'),
    #path('create/', views.task_create, name='task_create'),  # ← esta línea es necesaria
   # path('update/<int:pk>/', views.task_update, name='task_update'),
    #path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]