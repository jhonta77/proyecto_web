from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca/', views.acerca, name='acerca'),
    path('contacto/', views.contacto, name='contacto'),
]