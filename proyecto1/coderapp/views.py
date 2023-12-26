from django.http import HttpResponse
from django.shortcuts import render

from coderapp.models import Vendedor, Producto, Cliente
from coderapp.forms import VentaFormulario, NuevoVendedor, NuevoCliente




def index(request):
    return render(request, "index.html")

def vendedores(request):
    return render(request, 'vendedores.html')

def clientes(request):
    return render(request,'clientes.html')

def productos(request):
    return render(request, 'productos.html')

def ventas(request):
    return render(request, 'ventas.html')



def venta_formulario(request):
    if request.method == "POST":

        formulario = VentaFormulario(request.POST) 

        # print("formulario")
        # print(formulario)

        print(f"is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data

            nombre = datos.get("producto")
            cantidad = datos.get("cantidad")
            

            producto = Producto(nombre=nombre, cantidad=cantidad,)
            producto.save()

            return render(request, 'index.html')
        
    else:
        formulario = VentaFormulario()

    
    return render(request, 'venta_formulario.html', {"formulario": formulario})

def nuevo_vendedor(request):
    if request.method == "POST":

        formulario = NuevoVendedor(request.POST) 

        # print("formulario")
        # print(formulario)

        print(f"is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data

            
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            email = datos.get("email")

            vendedor = Vendedor(nombre=nombre, apellido=apellido, email=email)
            vendedor.save()

            return render(request, 'index.html')
        
    else:
        formulario = NuevoVendedor()

    
    return render(request, 'nuevo_vendedor.html', {"formulario": formulario})

def nuevo_cliente(request):
    if request.method == "POST":

        formulario = NuevoCliente(request.POST) 

        # print("formulario")
        # print(formulario)

        print(f"is valid: {formulario.is_valid}")
        if formulario.is_valid():
            datos = formulario.cleaned_data

            
            nombre = datos.get("nombre")
            apellido = datos.get("apellido")
            email = datos.get("email")

            cliente = Cliente(nombre=nombre, apellido=apellido, email=email)
            cliente.save()

            return render(request, 'index.html')
        
    else:
        formulario = NuevoCliente()

    
    return render(request, 'nuevo_cliente.html', {"formulario": formulario})


def busqueda_producto(request):

    if request.method == "GET":
        id = request.GET.get("id")
        print(f"vamos a buscar el id: {id}")

    return render(request, 'busqueda_producto.html')
 

def buscar_producto(request):

    if request.method == "GET":

        nombre = request.GET.get("nombre")
 
        if nombre is None:
            return HttpResponse("Enviar el producto a buscar")
        
        # siguiente paso, buscar los datos

        cursos = Producto.objects.filter(nombre__icontains=id)

        contexto = { 
            "nombre": nombre,
            "productos": productos,
            
        }

        return render(request, "busqueda.html", contexto)

        print(producto)

        return HttpResponse(f"se buscomo el producto : {nombre}")