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