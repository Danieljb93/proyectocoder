from django.http import HttpResponse
from django.shortcuts import render

def Leer_profesor(request):
    profe = Profesor(nombre="Andres", apellido="Benavides", email="andres@gmail.com")
    profe.save()
    return HttpResponse("El profesor se creo")


def Leer_alumnos(request):

    contexto = {
        "nombre": "Daniel",
        "apellido": "Jurado",
        "edad": 31,
        "cursos": ["python", "C", "java"],
    }

    return render(request, 'plantilla.html', contexto)


def index(request):
    return render(request, "index.html")

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return render(request,'estudiantes.html')

def cursos(request):
    return render(request, 'cursos.html')

def entregables(request):
    return render(request, 'entregables.html')