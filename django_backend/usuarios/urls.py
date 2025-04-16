from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Añadir esta línea para la ruta raíz
    path('perfil/', views.perfil, name='perfil'),
    path('admin/clientes/', views.lista_clientes, name='lista_clientes'),
]