from django.shortcuts import render
from AppAvanci.models import Curso
from AppAvanci.forms import CursoFormulario
from django.http import HttpResponse


# Create your views here.

#si queremos usar CONTEXT, lo ponemos en el tercer parámetro de RENDER

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


def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "AppAvanci/formulario.html")

    curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
    curso.save()
    return render(request, "AppAvanci/inicio.html")

def procesar_formulario_2(request):
    if request.method != "POST":
        mi_formulario = CursoFormulario()
    else:
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppAvanci/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "AppAvanci/formulario_2.html", contexto)


def busqueda(request):
        return render(request, "AppAvanci/busqueda.html")

def buscar(request):
    respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
    return HttpResponse(respuesta)

def busqueda_2(request):
    return render(request, "busqueda_2.html")

def buscar_2(request):
    if not request.GET["camada"]:
        return HttpResponse("No enviaste datos")
    else:
        camada_a_buscar = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada_a_buscar)

        contexto = {
            "camada": camada_a_buscar,
            "cursos": cursos
        }

        return render(request, "AppAvanci/resultadodebusqueda2.html", contexto)


    
