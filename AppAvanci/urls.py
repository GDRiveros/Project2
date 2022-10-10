"""Proyecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppAvanci.views import (
    mostrar_inicio,
    mostrar_cursos,
    mostrar_entregables,
    mostrar_estudiantes,
    mostrar_profesores,
    procesar_formulario,
    procesar_formulario_2,
    busqueda,
    buscar,
    busqueda_2,
    buscar_2,
) 

urlpatterns = [
    path("inicio/", mostrar_inicio, name="inicio"),
    path("cursos/", mostrar_cursos, name="cursos"),
    path("profesores/", mostrar_profesores, name="profesores"),
    path("estudiantes/", mostrar_estudiantes, name="estudiantes"),
    path("entregables/", mostrar_entregables, name="entregables"),
    path("formulario/", procesar_formulario, name="formulario"),
    path("formulario-2/", procesar_formulario_2, name="formulario_2"),
    path("busqueda", busqueda, name="busqueda"),
    path("buscar/", buscar),
    path("busqueda-2/", busqueda_2, name="busqueda-2"),
    path("buscar-2/", buscar_2)
]
