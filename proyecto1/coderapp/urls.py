from django.urls import path
from .views import profesores, estudiantes, cursos, entregables, index   


urlpatterns = [
    
    path('profesores/', profesores, name='profesores'),
    path('alumnos/', estudiantes, name='estudiantes'),
    path('cursos/', cursos, name='cursos'),
    path('entregables/', entregables, name='entregables'),
    path('Inicio', index, name='index')
]
