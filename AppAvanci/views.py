from django.shortcuts import render


# Create your views here.

def mostrar_inicio(request):
    return render(request, "AppAvanci/inicio.html")

def mostrar_cursos(request):
    return render(request, "AppAvanci/cursos.html")

def mostrar_profesores(request):
    return render(request, "AppAvanci/profesores.html")

def mostrar_estudiantes(request):
    return render(request, "AppAvanci/estudiantes.html")

def mostrar_entregables(request):
    return render(request, "AppAvanci/entregables.html")