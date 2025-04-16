from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Importación agregada

def home(request):
    if request.user.is_authenticated:
        return redirect('perfil')
    return render(request, 'home.html')  # Crea esta plantilla o redirige a login

@login_required
def perfil(request):
    return render(request, 'perfil.html', {'user': request.user})

@login_required
def lista_clientes(request):
    # Solo permitir a administradores
    if not request.user.is_staff:
        return redirect('home')
    
    # Obtener todos los usuarios que no son staff
    clientes = User.objects.filter(is_staff=False)
    
    return render(request, 'lista_clientes.html', {
        'clientes': clientes
    })
