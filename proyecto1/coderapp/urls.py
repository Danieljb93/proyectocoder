# from django.urls import path
# from .views import profesores, estudiantes, cursos, entregables, index   


# urlpatterns = [
    
#     path('profesores/', profesores, name='profesores'),
#     path('alumnos/', estudiantes, name='estudiantes'),
#     path('cursos/', cursos, name='cursos'),
#     path('entregables/', entregables, name='entregables'),
#     path('Inicio', index, name='index')
# ]

from django.urls import path
from django.views.generic.base import RedirectView
from .views import vendedores, clientes, productos, ventas, index, venta_formulario, busqueda_producto, buscar_producto,nuevo_vendedor, nuevo_cliente

urlpatterns = [
    path('', RedirectView.as_view(url='Inicio')),  # Redirige la ruta raíz a 'Inicio'
    path('vendedores/', vendedores, name='vendedores'),
    path('clientes/', clientes, name='clientes'),
    path('productos/', productos, name='productos'),
    path('entregables/', ventas, name='ventas'),
    path('ventaFormulario', venta_formulario, name='venta_formulario'),
    path('nuevoVendedor/', nuevo_vendedor, name='nuevo_vendedor'),
    path('nuevoCliente/', nuevo_cliente, name='nuevo_cliente'),
    path('busquedaProducto', busqueda_producto, name='busqueda_producto'),
    path("buscar", buscar_producto, name='buscar_producto'),
    path('Inicio', index, name='index')
]