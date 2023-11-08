from django.shortcuts import render

def login_registro(request):
    return render(request, 'myapp/login_registro.html')

def inicio_jugueteria(request):
    return render(request, 'myapp/inicio_jugueteria.html')
