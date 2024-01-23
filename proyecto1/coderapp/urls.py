

from django.urls import path
from django.views.generic.base import RedirectView
from coderapp.views import(
    vendedores,
    clientes,
    productos,
    ventas,
    index,
    venta_formulario,
   
    nuevo_vendedor,
    nuevo_cliente,
    leer_vendedores,
    leer_cliente,
    eliminar_vendedor,
    editar_vendedor,
    avatar,
    ProductoList,
    ProductoDetalle,
    ProductoCreacion,
    ProductoUpdate,
    ProductoDelete,
    
    login_request,
    registrar,
    

) 

from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', RedirectView.as_view(url='Inicio')),  # Redirige la ruta raíz a 'Inicio'
    path('vendedores/', vendedores, name='vendedores'),
    path('clientes/', clientes, name='clientes'),
    path('productos/', productos, name='productos'),
    path('entregables/', ventas, name='ventas'),
    path('ventaFormulario', venta_formulario, name='venta_formulario'),
    path('nuevoVendedor/', nuevo_vendedor, name='nuevo_vendedor'),
    path('nuevoCliente/', nuevo_cliente, name='nuevo_cliente'),
    path("leerVendedores", leer_vendedores, name='leer_vendedores'),
    path("leerClientes", leer_cliente, name='leer_clientes'),
    path("eliminarVendedor/<nombre_vendedor>", eliminar_vendedor, name="eliminar_vendedor"),
    path("producto/list", ProductoList.as_view(), name='List' ),
    path('detalle_producto/<pk>', ProductoDetalle.as_view(), name='Detail'),
    path('editar_producto/<pk>',ProductoUpdate.as_view(), name='Edit'),
    path('crear_producto', ProductoCreacion.as_view(), name='New'),
    path('eliminar_producto/<pk>', ProductoDelete.as_view(), name='Delete'),
    path('editar_vendedor/<nombre_vendedor>', editar_vendedor, name= "editar_vendedor"),
    path("login", login_request, name='login'),
    path("registrar", registrar, name='registrar'),
    path("logout", LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('avatar', avatar, name='avatar'),
    path('Inicio', index, name='index')
]