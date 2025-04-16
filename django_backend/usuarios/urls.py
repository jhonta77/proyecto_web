from django.urls import path
from . import views  # Importa las vistas de esta aplicación

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),
    path('gestion/clientes/', views.lista_clientes, name='lista_clientes'),
    # Puedes agregar más rutas específicas de la aplicación usuarios aquí
]