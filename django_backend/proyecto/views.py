from django.shortcuts import render

def perfil(request):
    return render(request, 'perfil.html')

def lista_clientes(request):
    return render(request, 'lista_clientes.html')