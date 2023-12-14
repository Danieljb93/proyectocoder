from django.urls import path
from .views import Leer_profesor, Leer_alumnos
urlpatterns = [
    
    path('profesore/', Leer_profesor),
    path('alumnos/', Leer_alumnos),
]
