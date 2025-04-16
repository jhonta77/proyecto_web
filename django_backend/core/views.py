from django.shortcuts import render, redirect

def home(request):
    # Redireccionar a perfil si el usuario ya está autenticado
    if request.user.is_authenticated:
        return redirect('perfil')
    
    # Si no está autenticado, mostrar la página principal
    return render(request, 'home.html')

def acerca(request):
    return render(request, 'acerca.html')

def contacto(request):
    return render(request, 'contacto.html')